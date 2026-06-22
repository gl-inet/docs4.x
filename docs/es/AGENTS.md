---
description: "Use when translating English GL.iNet router documentation into Spanish or editing files under docs/es/docs/**. Covers Spanish terminology, style, and common translation pitfalls."
name: "Spanish Docs Translation Rules"
applyTo: "docs/es/docs/**/*.md"
---

# Spanish Translation Rules

- Write natural, professional Spanish suitable for official technical support documentation.
- Keep tone consistent across the whole page. Do not switch between regional variants or between formal and informal address within one file.
- Remove machine-translation artifacts completely. Do not leave stray Chinese, Japanese, Korean, Russian, or partially untranslated English in Spanish prose.

## Spanish Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `WireGuard`, `OpenVPN`, `GoodCloud`, `DDNS`, `WebDAV`, `DLNA`, `Samba`, `MAC`, `MTU`, `WAN`, `LAN`.
- Prefer `túnel` for `tunnel`.
- Prefer `interruptor de corte` or `Kill Switch` consistently within one file, following whichever style becomes standard in nearby Spanish docs.
- Prefer `enmascaramiento de IP` for `IP Masquerading`.
- Prefer `IP virtual del cliente` for `client virtual IP`.
- Prefer `acceso remoto` for `remote access`.
- Prefer `puerto de escucha` consistently within one file.

## Fixed Network and VPN Vocabulary

- Use one consistent translation for these concepts within a file: `Global Mode`, `Policy Mode`, `All Other Traffic`, `VPN Client`, `VPN Server`, `fail over`, `site-to-site`, `guest network`, `traffic source`, `traffic destination`, `routing method`, `port role`, `negotiated speed`.
- Prefer `modo global` for `Global Mode`.
- Prefer `modo de políticas` for `Policy Mode`.
- Prefer `todo el resto del tráfico` for `All Other Traffic`.
- Prefer `cliente VPN` and `servidor VPN`.
- Prefer `conmutación por error` for `fail over`.
- Prefer `site-to-site` or `sitio a sitio` consistently within one file.
- Prefer `red de invitados` for `guest network`.
- Prefer `origen del tráfico` for `traffic source`.
- Prefer `destino del tráfico` for `traffic destination`.
- Prefer `método de enrutamiento` for `routing method`.
- Prefer `función del puerto` for `port role`.
- Prefer `velocidad negociada` for `negotiated speed`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For left-navigation paths, keep the structure exactly as in the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent Spanish UI labels that are not shown in the product.

## Spanish-Specific Pitfalls

- Do not mix English and Spanish inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `tunnel`, `Enabled`, `Sort`, or similar English UI words inside Spanish prose unless they are literal UI labels.
- Do not mistranslate option scope, for example mixing `Allow Access Samba from WAN` with `Allow Access WebDAV from WAN`.
- Do not confuse `traffic source`, `traffic destination`, and `routing method`.
- Do not confuse `remote peer`, `server`, `client`, `device`, and `router`.
- Prefer clear technical Spanish over overly literal syntax copied from English.

## VPN and Routing Accuracy Check

- Preserve the distinction between traffic that is matched by a rule and traffic that is excluded from a rule.
- Preserve whether unmatched traffic is allowed, blocked, or routed via local WAN.
- Preserve whether a tunnel fails over to another tunnel, to `All Other Traffic`, or does not fail over at all.
- Preserve whether a setting is per-tunnel or global.
- Translate `enabled`, `disabled`, `default`, `only`, and `all` with extra care because they often change device behavior.

## Repository Expectations for Spanish

- Match the style of official router setup and administration documentation.
- Prefer wording that is clear, neutral, and instructional rather than promotional.
- If the current Spanish page contains low-quality machine translation, clean it fully instead of editing only one sentence and leaving the rest broken.

## Spanish Final Check

- The Spanish reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Spanish docs.
