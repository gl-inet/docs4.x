#!/usr/bin/env python3
"""Auto-translate updated English docs into localized markdown files."""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys
import time
from functools import lru_cache
from dataclasses import dataclass
from typing import Iterable

import requests

DOCS_ROOT = pathlib.Path(os.getenv("DOCS_ROOT", "docs"))
CACHE_FILE = pathlib.Path(os.getenv("TRANSLATION_CACHE_FILE", ".translation-cache.json"))
EN_DOCS_PREFIX = "docs/en/docs/"
TARGET_LANGS = [
    lang.strip()
    for lang in os.getenv("TARGET_LANGS", "de,es,fr,it,jp,pl").split(",")
    if lang.strip()
]
API_KEY = os.getenv("LLM_API_KEY", "").strip()
API_BASE_URL = (os.getenv("LLM_BASE_URL", "") or "https://models.inference.ai.azure.com").strip().rstrip("/")
MODEL = (os.getenv("LLM_MODEL", "") or "gpt-4.1-mini").strip()
FORCE_FULL = os.getenv("FORCE_FULL", "false").lower() in {"1", "true", "yes", "on"}
MAX_FILES = int(os.getenv("MAX_FILES", "0") or "0")

REPO_INSTRUCTION_FILE = pathlib.Path("AGENTS.md")
LANGUAGE_INSTRUCTION_FILES = {
    "de": pathlib.Path("docs/de/AGENTS.md"),
    "es": pathlib.Path("docs/es/AGENTS.md"),
    "fr": pathlib.Path("docs/fr/AGENTS.md"),
    "it": pathlib.Path("docs/it/AGENTS.md"),
    "jp": pathlib.Path("docs/jp/AGENTS.md"),
    "pl": pathlib.Path("docs/pl/AGENTS.md"),
}

SYSTEM_PROMPT = (
    "You are a senior technical documentation translator for networking products. "
    "Return only translated markdown without code fences."
)

LANGUAGE_NAMES = {
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
    "jp": "Japanese",
    "pl": "Polish",
}

EN_ROOT_PREFIX = "docs/en/"
EN_EXTRA_FILES = [
    "docs/en/mkdocs.yml",
    "docs/en/overrides/home.html",
    "docs/en/overrides/main.html",
]
# MkDocs material language codes differ from our directory names for JP
MKDOCS_LANG_CODES = {
    "de": "de",
    "es": "es",
    "fr": "fr",
    "it": "it",
    "jp": "ja",
    "pl": "pl",
}


@dataclass
class TranslationTask:
    source_path: pathlib.Path
    source_rel: str
    target_lang: str
    target_path: pathlib.Path


def normalize_repo_path(path: str) -> str:
    return path.strip().replace("\\", "/")


def is_en_markdown_path(path: str) -> bool:
    return path.startswith(EN_DOCS_PREFIX) and path.endswith(".md")


def is_en_tracked_path(path: str) -> bool:
    return is_en_markdown_path(path) or path in EN_EXTRA_FILES


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_paths_list(raw: str) -> list[str]:
    if not raw.strip():
        return []

    normalized: list[str] = []
    for line in raw.replace(",", "\n").splitlines():
        p = line.strip().replace("\\", "/")
        if p:
            normalized.append(p)
    return normalized


def parse_renamed_pairs(raw: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    if not raw.strip():
        return pairs

    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        old_path = ""
        new_path = ""
        if "\t" in stripped:
            parts = stripped.split("\t")
            if len(parts) >= 2:
                old_path, new_path = parts[0], parts[1]
        elif "=>" in stripped:
            parts = stripped.split("=>", maxsplit=1)
            old_path, new_path = parts[0], parts[1]
        else:
            continue

        old_norm = normalize_repo_path(old_path)
        new_norm = normalize_repo_path(new_path)
        if old_norm and new_norm:
            pairs.append((old_norm, new_norm))

    return pairs


def load_cache(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"[warn] cache file is invalid JSON: {path}")
        return {}


def save_cache(path: pathlib.Path, cache: dict) -> None:
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_text_if_exists(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


@lru_cache
def get_instruction_bundle(target_lang: str) -> str:
    chunks: list[str] = []

    repo_instructions = read_text_if_exists(REPO_INSTRUCTION_FILE)
    if repo_instructions:
        chunks.append("Repository translation instructions:\n" + repo_instructions)

    lang_instruction_path = LANGUAGE_INSTRUCTION_FILES.get(target_lang)
    if lang_instruction_path:
        lang_instructions = read_text_if_exists(lang_instruction_path)
        if lang_instructions:
            chunks.append("Language-specific instructions:\n" + lang_instructions)

    return "\n\n".join(chunks)


def collect_english_files() -> list[pathlib.Path]:
    en_root = DOCS_ROOT / "en" / "docs"
    if not en_root.exists():
        raise FileNotFoundError(f"English docs root not found: {en_root}")
    md_files = sorted(en_root.rglob("*.md"))
    extra_files = [p for rel in EN_EXTRA_FILES if (p := pathlib.Path(rel)).exists()]
    return extra_files + md_files


def source_rel_path(source_path: pathlib.Path) -> str:
    return source_path.as_posix()


def target_path_for_lang(source_path: pathlib.Path, lang: str) -> pathlib.Path:
    src = source_path.as_posix()
    if src.startswith(EN_DOCS_PREFIX):
        return pathlib.Path(src.replace(EN_DOCS_PREFIX, f"docs/{lang}/docs/", 1))
    if src.startswith(EN_ROOT_PREFIX):
        return pathlib.Path(src.replace(EN_ROOT_PREFIX, f"docs/{lang}/", 1))
    raise ValueError(f"Unexpected source path: {src}")


def lang_docs_root(lang: str) -> pathlib.Path:
    return DOCS_ROOT / lang / "docs"


def prune_empty_parents(path: pathlib.Path, stop_at: pathlib.Path) -> None:
    stop_at_resolved = stop_at.resolve()

    try:
        path.resolve().relative_to(stop_at_resolved)
    except ValueError:
        print(f"[cleanup] skip outside language root: {path.as_posix()}")
        return

    current = path.parent
    while current.exists():
        current_resolved = current.resolve()
        if current_resolved == stop_at_resolved:
            break

        try:
            current.rmdir()
            print(f"[cleanup] removed empty dir: {current.as_posix()}")
            current = current.parent
        except OSError:
            break


def migrate_renamed_files_and_cache(
    cache: dict,
    renamed_pairs: list[tuple[str, str]],
) -> None:
    if not renamed_pairs:
        return

    for old_rel, new_rel in renamed_pairs:
        if not (is_en_tracked_path(old_rel) and is_en_tracked_path(new_rel)):
            continue

        moved_any = False
        for lang in TARGET_LANGS:
            old_target = target_path_for_lang(pathlib.Path(old_rel), lang)
            new_target = target_path_for_lang(pathlib.Path(new_rel), lang)

            if old_target.exists() and not new_target.exists():
                new_target.parent.mkdir(parents=True, exist_ok=True)
                old_target.rename(new_target)
                prune_empty_parents(old_target, lang_docs_root(lang))
                moved_any = True
                print(f"[rename] {lang}: {old_target.as_posix()} -> {new_target.as_posix()}")

        old_entry = cache.pop(old_rel, None)
        old_hash = ""
        if isinstance(old_entry, dict):
            old_hash = str(old_entry.get("source_hash", ""))
        any_target_exists = any(
            target_path_for_lang(pathlib.Path(new_rel), lang).exists() for lang in TARGET_LANGS
        )

        if not any_target_exists:
            continue

        new_source_path = pathlib.Path(new_rel)
        if not new_source_path.exists():
            continue

        new_hash = sha256_text(new_source_path.read_text(encoding="utf-8"))
        content_unchanged = bool(old_hash) and old_hash == new_hash
        current_entry = cache.get(new_rel, {})
        merged_targets = {}
        if isinstance(old_entry, dict):
            merged_targets.update(old_entry.get("targets", {}))
        if isinstance(current_entry, dict):
            merged_targets.update(current_entry.get("targets", {}))

        cache_entry: dict[str, object] = {
            "targets": merged_targets,
        }
        if content_unchanged:
            # Rename-only change: keep hash in sync so translation is skipped.
            cache_entry["source_hash"] = new_hash
        elif isinstance(current_entry, dict) and "source_hash" in current_entry:
            # Keep mismatch to force re-translation when content changed.
            cache_entry["source_hash"] = current_entry["source_hash"]

        cache[new_rel] = cache_entry

        if moved_any:
            print(f"[cache] migrated key: {old_rel} -> {new_rel}")


def remove_deleted_targets_and_cache(
    cache: dict,
    deleted_paths: set[str],
) -> None:
    if not deleted_paths:
        return

    for deleted_rel in deleted_paths:
        if not is_en_tracked_path(deleted_rel):
            continue

        removed_any = False
        for lang in TARGET_LANGS:
            target_path = target_path_for_lang(pathlib.Path(deleted_rel), lang)
            if target_path.exists():
                target_path.unlink()
                prune_empty_parents(target_path, lang_docs_root(lang))
                removed_any = True
                print(f"[delete] {lang}: removed {target_path.as_posix()}")

        if deleted_rel in cache:
            cache.pop(deleted_rel, None)
            removed_any = True
            print(f"[cache] removed key: {deleted_rel}")

        if not removed_any:
            print(f"[delete] no localized files found for {deleted_rel}")


def build_tasks(
    english_files: Iterable[pathlib.Path],
    cache: dict,
    changed_paths: set[str],
) -> list[TranslationTask]:
    tasks: list[TranslationTask] = []
    changed_mode = len(changed_paths) > 0 and not FORCE_FULL

    for source_path in english_files:
        rel = source_rel_path(source_path)

        if changed_mode and rel not in changed_paths:
            continue

        source_text = source_path.read_text(encoding="utf-8")
        source_hash = sha256_text(source_text)
        cache_entry = cache.get(rel, {})
        cached_source_hash = cache_entry.get("source_hash", "")

        for lang in TARGET_LANGS:
            target_path = target_path_for_lang(source_path, lang)
            should_translate = FORCE_FULL or not target_path.exists() or source_hash != cached_source_hash
            if should_translate:
                tasks.append(
                    TranslationTask(
                        source_path=source_path,
                        source_rel=rel,
                        target_lang=lang,
                        target_path=target_path,
                    )
                )

    if MAX_FILES > 0:
        tasks = tasks[:MAX_FILES]

    return tasks


def translate_markdown(
    source_markdown: str,
    target_lang: str,
    existing_translation: str | None,
) -> str:
    if not API_KEY:
        raise RuntimeError("Missing LLM_API_KEY environment variable")

    target_language = LANGUAGE_NAMES.get(target_lang, target_lang)
    instruction_bundle = get_instruction_bundle(target_lang)
    prompt_parts = [
        f"Translate the markdown below into {target_language}.",
        "Rules:",
        "1. Preserve markdown structure exactly: headings, lists, tables, links, images, admonitions, separators.",
        "2. Preserve exact product names, model names, protocol names, versions, URLs, paths, code, and values.",
        "3. Keep explicit custom heading anchors unchanged, e.g. {#id} or {custom-anchor}.",
        "4. Keep UI labels in English when they are literal product labels in bold/navigation paths.",
        "5. Output only final markdown, no explanation.",
    ]

    if instruction_bundle:
        prompt_parts.extend(
            [
                "Apply these project instructions strictly:",
                instruction_bundle,
            ]
        )

    if existing_translation:
        prompt_parts.extend(
            [
                "There is an existing translation. Update only what is needed to sync with the latest English source.",
                "Keep unchanged lines untouched when they are already correct and compliant with instructions.",
                "Existing translation:",
                existing_translation,
            ]
        )

    prompt_parts.extend(["Markdown to translate:", source_markdown])
    return _call_llm("\n\n".join(prompt_parts))


def _call_llm(user_prompt: str) -> str:
    """Send a prompt to the LLM and return the response text, with retries."""
    if not API_KEY:
        raise RuntimeError("Missing LLM_API_KEY environment variable")

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.1,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    url = f"{API_BASE_URL}/chat/completions"
    last_error = None

    for attempt in range(1, 4):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=180)
            if response.status_code >= 400:
                raise RuntimeError(f"HTTP {response.status_code}: {response.text[:400]}")

            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            if not content:
                raise RuntimeError("empty model output")
            return content + ("\n" if not content.endswith("\n") else "")
        except Exception as exc:  # pylint: disable=broad-except
            last_error = exc
            if attempt < 3:
                time.sleep(2 * attempt)

    raise RuntimeError(f"translation failed after retries: {last_error}")


def translate_html(
    source_html: str,
    target_lang: str,
    existing_translation: str | None,
) -> str:
    if not API_KEY:
        raise RuntimeError("Missing LLM_API_KEY environment variable")

    target_language = LANGUAGE_NAMES.get(target_lang, target_lang)
    instruction_bundle = get_instruction_bundle(target_lang)
    prompt_parts = [
        f"Translate the HTML template below into {target_language}.",
        "Rules:",
        "1. Translate ONLY user-visible text content inside HTML tags.",
        "2. Do NOT translate: CSS, HTML attributes (class, id, href, src, alt), Jinja2 template tags ({% %} {{ }}), JavaScript, or HTML comments.",
        "3. Preserve all HTML structure, tags, attributes, and indentation exactly.",
        "4. Preserve all URLs, file paths, and technical values unchanged.",
        "5. Output only the final HTML with no explanation.",
    ]

    if instruction_bundle:
        prompt_parts.extend(
            [
                "Apply these project instructions strictly:",
                instruction_bundle,
            ]
        )

    if existing_translation:
        prompt_parts.extend(
            [
                "There is an existing translation. Update only what is needed to sync with the latest English source.",
                "Keep unchanged lines untouched when they are already correct.",
                "Existing translation:",
                existing_translation,
            ]
        )

    prompt_parts.extend(["HTML to translate:", source_html])
    return _call_llm("\n\n".join(prompt_parts))


def _fix_mkdocs_lang_fields(yaml_text: str, target_lang: str) -> str:
    """Post-process translated mkdocs.yml to set the correct theme.language and site_url."""
    lang_code = MKDOCS_LANG_CODES.get(target_lang, target_lang)
    # Fix theme.language (indented under theme:)
    yaml_text = re.sub(r"(\s{2}language:\s*)[\w-]+", rf"\g<1>{lang_code}", yaml_text)
    # Fix site_url — replace the language segment in the GL.iNet docs URL
    yaml_text = re.sub(
        r"(site_url:\s*https://docs\.gl-inet\.com/router/)[a-z]+(/)",
        rf"\g<1>{target_lang}\2",
        yaml_text,
    )
    return yaml_text


def translate_yaml_config(
    source_yaml: str,
    target_lang: str,
    existing_translation: str | None,
) -> str:
    if not API_KEY:
        raise RuntimeError("Missing LLM_API_KEY environment variable")

    target_language = LANGUAGE_NAMES.get(target_lang, target_lang)
    prompt_parts = [
        f"Translate the MkDocs YAML configuration below into {target_language}.",
        "Rules:",
        "1. Translate ONLY: the value of 'site_name', the value of 'site_description', and navigation label text (human-readable page titles on the left of colons in the nav: section).",
        "2. Do NOT change: 'site_url', 'theme.language', file paths, YAML keys, plugin settings, URLs, social links, or any technical values.",
        "3. Keep all YAML structure and indentation exactly as in the source.",
        "4. Output only the final YAML with no explanation.",
    ]

    if existing_translation:
        prompt_parts.extend(
            [
                "There is an existing translation. Update only what is needed to sync with the latest English source.",
                "Keep unchanged lines untouched when they are already correct.",
                "Existing translation:",
                existing_translation,
            ]
        )

    prompt_parts.extend(["YAML to translate:", source_yaml])
    translated = _call_llm("\n\n".join(prompt_parts))
    return _fix_mkdocs_lang_fields(translated, target_lang)


def translate_content(
    source_text: str,
    source_rel: str,
    target_lang: str,
    existing_translation: str | None,
) -> str:
    """Dispatch to the appropriate translation function based on file type."""
    if source_rel.endswith(".html"):
        return translate_html(source_text, target_lang, existing_translation)
    if source_rel.endswith(".yml"):
        return translate_yaml_config(source_text, target_lang, existing_translation)
    return translate_markdown(source_text, target_lang, existing_translation)


def main() -> int:
    changed_raw = os.getenv("CHANGED_EN_FILES", "")
    renamed_raw = os.getenv("RENAMED_EN_FILES", "")
    deleted_raw = os.getenv("DELETED_EN_FILES", "")
    changed_paths = set(normalize_paths_list(changed_raw))
    renamed_pairs = parse_renamed_pairs(renamed_raw)
    deleted_paths = set(normalize_paths_list(deleted_raw))
    cache = load_cache(CACHE_FILE)

    remove_deleted_targets_and_cache(cache, deleted_paths)
    migrate_renamed_files_and_cache(cache, renamed_pairs)

    english_files = collect_english_files()
    tasks = build_tasks(english_files, cache, changed_paths)

    print(f"[info] english files scanned: {len(english_files)}")
    print(f"[info] translation tasks: {len(tasks)}")

    if not tasks:
        print("[info] no translation work needed")
        return 0

    translated_count = 0
    for task in tasks:
        source_text = task.source_path.read_text(encoding="utf-8")
        source_hash = sha256_text(source_text)

        print(f"[translate] {task.source_rel} -> {task.target_lang}")
        current_text = task.target_path.read_text(encoding="utf-8") if task.target_path.exists() else None
        translated_text = translate_content(
            source_text,
            task.source_rel,
            task.target_lang,
            current_text,
        )

        task.target_path.parent.mkdir(parents=True, exist_ok=True)

        if current_text != translated_text:
            task.target_path.write_text(translated_text, encoding="utf-8")
            translated_count += 1

        cache.setdefault(task.source_rel, {})
        cache[task.source_rel]["source_hash"] = source_hash
        cache[task.source_rel].setdefault("targets", {})
        cache[task.source_rel]["targets"][task.target_lang] = {
            "model": MODEL,
            "updated_at": int(time.time()),
        }

    save_cache(CACHE_FILE, cache)
    print(f"[info] files updated: {translated_count}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:  # pylint: disable=broad-except
        print(f"[error] {error}", file=sys.stderr)
        raise
