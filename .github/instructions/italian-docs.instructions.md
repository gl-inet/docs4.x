---
description: "Use when translating English GL.iNet router documentation into Italian or editing files under docs/it/docs/**. Covers Italian terminology, style, and common translation pitfalls."
name: "Italian Docs Translation Rules"
applyTo: "docs/it/docs/**/*.md"
---

# Italian Translation Rules

- Write natural, professional Italian suitable for official technical support documentation.
- Keep tone consistent across the whole page. Do not switch between formal and informal address within one file.
- Remove machine-translation artifacts completely. Do not leave stray Chinese, Japanese, Korean, Russian, or partially untranslated English in Italian prose.

## Italian Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `WireGuard`, `OpenVPN`, `GoodCloud`, `DDNS`, `WebDAV`, `DLNA`, `Samba`, `MAC`, `MTU`, `WAN`, `LAN`.
- Prefer `tunnel` for `tunnel`.
- Prefer `Kill Switch` or `interruttore di blocco` consistently within one file, following whichever style becomes standard in nearby Italian docs.
- Prefer `mascheramento IP` for `IP Masquerading`.
- Prefer `IP virtuale del client` for `client virtual IP`.
- Prefer `accesso remoto` for `remote access`.
- Prefer `porta di ascolto` consistently within one file.

## Fixed Network and VPN Vocabulary

- Use one consistent translation for these concepts within a file: `Global Mode`, `Policy Mode`, `All Other Traffic`, `VPN Client`, `VPN Server`, `fail over`, `site-to-site`, `guest network`, `traffic source`, `traffic destination`, `routing method`, `port role`, `negotiated speed`.
- Prefer `modalità globale` for `Global Mode`.
- Prefer `modalità criteri` for `Policy Mode`.
- Prefer `tutto il resto del traffico` for `All Other Traffic`.
- Prefer `client VPN` and `server VPN`.
- Prefer `failover` for `fail over`.
- Prefer `site-to-site` or `da sito a sito` consistently within one file.
- Prefer `rete ospite` for `guest network`.
- Prefer `origine del traffico` for `traffic source`.
- Prefer `destinazione del traffico` for `traffic destination`.
- Prefer `metodo di instradamento` for `routing method`.
- Prefer `ruolo della porta` for `port role`.
- Prefer `velocità negoziata` for `negotiated speed`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For left-navigation paths, keep the structure exactly as in the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent Italian UI labels that are not shown in the product.

## Italian-Specific Pitfalls

- Do not mix English and Italian inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `tunnel`, `Enabled`, `Sort`, or similar English UI words inside Italian prose unless they are literal UI labels.
- Do not mistranslate option scope, for example mixing `Allow Access Samba from WAN` with `Allow Access WebDAV from WAN`.
- Do not confuse `traffic source`, `traffic destination`, and `routing method`.
- Do not confuse `remote peer`, `server`, `client`, `device`, and `router`.
- Prefer clear technical Italian over overly literal syntax copied from English.

## VPN and Routing Accuracy Check

- Preserve the distinction between traffic that is matched by a rule and traffic that is excluded from a rule.
- Preserve whether unmatched traffic is allowed, blocked, or routed via local WAN.
- Preserve whether a tunnel fails over to another tunnel, to `All Other Traffic`, or does not fail over at all.
- Preserve whether a setting is per-tunnel or global.
- Translate `enabled`, `disabled`, `default`, `only`, and `all` with extra care because they often change device behavior.

## Repository Expectations for Italian

- Match the style of official router setup and administration documentation.
- Prefer wording that is clear, neutral, and instructional rather than promotional.
- If the current Italian page contains low-quality machine translation, clean it fully instead of editing only one sentence and leaving the rest broken.

## Italian Final Check

- The Italian reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Italian docs.
