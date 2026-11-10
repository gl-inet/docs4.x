# GL.iNet Documentation

This repository contains the source files for GL.iNet router firmware 4.x documentation.

It is now a multilingual documentation repository. The current language sites in this repo are:

- English: `docs/en/`
- German: `docs/de/`
- Spanish: `docs/es/`
- French: `docs/fr/`
- Italian: `docs/it/`
- Japanese: `docs/ja/`
- Dutch (Nederlands): `docs/nl/`
- Polish: `docs/pl/`
- Swedish (Svenska): `docs/sv/`
- Ukrainian (Українська): `docs/uk/`

Each language has its own `mkdocs.yml`, `docs/`, and `overrides/` directory.

## Environment

The documentation is built with [MkDocs](https://www.mkdocs.org/) 1.5.3 and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme 9.4.6.

## Installation

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

You can also install Material for MkDocs directly:

```bash
pip install mkdocs-material
```

Reference: [https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip](https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip)

## Repository Structure

The root `docs/` folder contains one MkDocs project per language:

```text
docs/
  en/
    mkdocs.yml
    docs/
    overrides/
  de/
    mkdocs.yml
    docs/
    overrides/
  es/
    mkdocs.yml
    docs/
    overrides/
  fr/
    mkdocs.yml
    docs/
    overrides/
  it/
    mkdocs.yml
    docs/
    overrides/
  ja/
    mkdocs.yml
    docs/
    overrides/
  nl/
    mkdocs.yml
    docs/
    overrides/
  pl/
    mkdocs.yml
    docs/
    overrides/
  sv/
    mkdocs.yml
    docs/
    overrides/
  uk/
    mkdocs.yml
    docs/
    overrides/
```

In most cases, localized pages should mirror the corresponding English page path under `docs/en/docs/`.

## Local Preview

Run MkDocs against the language you want to preview.

Examples:

```bash
mkdocs serve -f docs/en/mkdocs.yml
mkdocs serve -f docs/de/mkdocs.yml
mkdocs serve -f docs/es/mkdocs.yml
mkdocs serve -f docs/ja/mkdocs.yml
mkdocs serve -f docs/nl/mkdocs.yml
mkdocs serve -f docs/sv/mkdocs.yml
mkdocs serve -f docs/uk/mkdocs.yml
```

If you are reviewing or translating localized content, open the English source page and the matching localized page side by side in VS Code.

## Checks Before Committing

Enable the repository's pre-commit hook once per clone:

```bash
git config core.hooksPath .githooks
```

The hook checks only the files staged for the commit:

- Heading IDs and anchor links (`scripts/anchors.py`).
- Localized pages: structure compared with the English page, untranslated English, and language rules such as Italian accents (`scripts/i18n_check.py`).
- Changed localized files with an English counterpart: `.translation-cache.json` must contain an independent per-language `source_hash` matching the staged English content and a `target_hash` matching the staged localized content. This includes Markdown, configuration, overrides, text assets and binary files. Unstaged updates to any of these files cannot satisfy the check. Other languages may remain pending; the Downloads page remains excluded.

After translating and validating a file, record its reviewed versions and stage both the localized file and `.translation-cache.json`:

```bash
python scripts/translation_delta.py mark docs/en/docs/interface_guide/vpn_dashboard.md --lang de --model manual-sync
git add docs/de/docs/interface_guide/vpn_dashboard.md .translation-cache.json
```

If English changed but the localized text needs no edit, review both versions and use `--no-target-change` with explicit languages. This flag does not bypass validation. Stage the intended versions together: fixing a file or updating `.translation-cache.json` in the working directory does not change a version already staged.

PR checks use the committed `HEAD` versions of these files rather than the working directory or index, and mismatches fail the check. English-only trailing Regulatory Statements remain excluded from the English hash, using the existing router-specific rules.

Commits that change only English pages do not require translations in the same commit, but heading and anchor errors still block them. To bypass the hook in an emergency, use `git commit --no-verify`.

## Online View

Published documentation:

- English: [https://docs.gl-inet.com/router/en/4/](https://docs.gl-inet.com/router/en/4/)
- German: [https://docs.gl-inet.com/router/de/4/](https://docs.gl-inet.com/router/de/4/)
- Spanish: [https://docs.gl-inet.com/router/es/4/](https://docs.gl-inet.com/router/es/4/)
- French: [https://docs.gl-inet.com/router/fr/4/](https://docs.gl-inet.com/router/fr/4/)
- Italian: [https://docs.gl-inet.com/router/it/4/](https://docs.gl-inet.com/router/it/4/)
- Japanese: [https://docs.gl-inet.com/router/ja/4/](https://docs.gl-inet.com/router/ja/4/)
- Dutch: [https://docs.gl-inet.com/router/nl/4/](https://docs.gl-inet.com/router/nl/4/)
- Polish: [https://docs.gl-inet.com/router/pl/4/](https://docs.gl-inet.com/router/pl/4/)
- Swedish: [https://docs.gl-inet.com/router/sv/4/](https://docs.gl-inet.com/router/sv/4/)
- Ukrainian: [https://docs.gl-inet.com/router/uk/4/](https://docs.gl-inet.com/router/uk/4/)

## Writing Guide

### Markdown Syntax

All pages are written in Markdown. For basic syntax, see [Markdown Guide](https://www.markdownguide.org/basic-syntax/).

### Open a Link in a New Tab

To open a link in a new tab, add `{target="_blank"}` at the end of the link.

### Image File Type

Prefer PNG unless there is a clear reason to use another format.

### Image Lightbox

If an image is large, use PhotoSwipe. See [About PhotoSwipe](#about-photoswipe).

### Image Size

Use `gl-50-desktop`, `gl-60-desktop`, `gl-70-desktop`, `gl-80-desktop`, or `gl-90-desktop` to control image width on desktop.

Example:

`![gl.inet enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="gl-50-desktop"}`

### Image Shadow Effect

Use `{class="glboxshadow"}` to add a shadow to an image.

Example:

`![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}`

### Image Captions

```html
<figure>
  <img src="https://dummyimage.com/600x400/eee/aaa" width="300" />
  <figcaption>Image caption</figcaption>
</figure>
```

### Internal Links

Use relative paths for internal links.

```md
[easytethering](../../../tutorials/tether)
```

## About PhotoSwipe

This project currently uses PhotoSwipe v4. Version 5 looks better, but it requires loading JavaScript modules and is not integrated here.

Use PhotoSwipe when the image width is larger than 1021 px.

```html
<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure
    itemprop="associatedMedia"
    itemscope
    itemtype="http://schema.org/ImageObject"
  >
    <a
      href="https://static.gl-inet.com/docs/router/en/4/setup/gl-b2200/hardware/hardware_1.jpg"
      itemprop="contentUrl"
      data-size="3167x2480"
    >
      <img
        src="https://static.gl-inet.com/docs/router/en/4/setup/gl-b2200/hardware/hardware_1.jpg"
        itemprop="thumbnail"
        alt="gl-b2200 pcb pinout"
      />
    </a>
  </figure>
</div>
```

Reference:

- [https://photoswipe.com/documentation/getting-started.html](https://photoswipe.com/documentation/getting-started.html)
- [https://codepen.io/dimsemenov/pen/ZYbPJM](https://codepen.io/dimsemenov/pen/ZYbPJM)

## About Versioning

The `mike` plugin is designed for versioned MkDocs deployments, usually with GitHub Pages. This repository does not deploy with GitHub Pages, but it follows a similar output structure.

Reference:

- [Setting up versioning](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)
- [mkdocs-material-example-versioning](https://github.com/squidfunk/mkdocs-material-example-versioning)
