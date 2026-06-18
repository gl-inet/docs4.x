---
description: "Use when translating English GL.iNet router documentation into Polish or editing files under docs/pl/docs/**. Covers Polish terminology, style, and common translation pitfalls."
name: "Polish Docs Translation Rules"
applyTo: "docs/pl/docs/**/*.md"
---

# Polish Translation Rules

- Write natural, professional Polish suitable for official technical support documentation.
- Keep tone consistent across the whole page. Do not switch between formal and informal address within one file.
- Remove machine-translation artifacts completely. Do not leave stray Chinese, Japanese, Korean, Russian, or partially untranslated English in Polish prose.

## Polish Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `WireGuard`, `OpenVPN`, `GoodCloud`, `DDNS`, `WebDAV`, `DLNA`, `Samba`, `MAC`, `MTU`, `WAN`, `LAN`.
- Prefer `tunel` for `tunnel`.
- Prefer `Kill Switch` or `wyłącznik awaryjny VPN` consistently within one file, following whichever style becomes standard in nearby Polish docs.
- Prefer `maskowanie IP` for `IP Masquerading`.
- Prefer `wirtualny adres IP klienta` for `client virtual IP`.
- Prefer `zdalny dostęp` for `remote access`.
- Prefer `port nasłuchu` consistently within one file.

## Fixed Network and VPN Vocabulary

- Use one consistent translation for these concepts within a file: `Global Mode`, `Policy Mode`, `All Other Traffic`, `VPN Client`, `VPN Server`, `fail over`, `site-to-site`, `guest network`, `traffic source`, `traffic destination`, `routing method`, `port role`, `negotiated speed`.
- Prefer `tryb globalny` for `Global Mode`.
- Prefer `tryb polityk` for `Policy Mode`.
- Prefer `cały pozostały ruch` for `All Other Traffic`.
- Prefer `klient VPN` and `serwer VPN`.
- Prefer `przełączenie awaryjne` for `fail over`.
- Prefer `site-to-site` or `lokacja-lokacja` consistently within one file.
- Prefer `sieć gościnna` for `guest network`.
- Prefer `źródło ruchu` for `traffic source`.
- Prefer `cel ruchu` for `traffic destination`.
- Prefer `metoda routingu` for `routing method`.
- Prefer `rola portu` for `port role`.
- Prefer `wynegocjowana prędkość` for `negotiated speed`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For left-navigation paths, keep the structure exactly as in the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent Polish UI labels that are not shown in the product.

## Polish-Specific Pitfalls

- Do not mix English and Polish inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `tunnel`, `Enabled`, `Sort`, or similar English UI words inside Polish prose unless they are literal UI labels.
- Do not mistranslate option scope, for example mixing `Allow Access Samba from WAN` with `Allow Access WebDAV from WAN`.
- Do not confuse `traffic source`, `traffic destination`, and `routing method`.
- Do not confuse `remote peer`, `server`, `client`, `device`, and `router`.
- Prefer clear technical Polish over overly literal syntax copied from English.

## VPN and Routing Accuracy Check

- Preserve the distinction between traffic that is matched by a rule and traffic that is excluded from a rule.
- Preserve whether unmatched traffic is allowed, blocked, or routed via local WAN.
- Preserve whether a tunnel fails over to another tunnel, to `All Other Traffic`, or does not fail over at all.
- Preserve whether a setting is per-tunnel or global.
- Translate `enabled`, `disabled`, `default`, `only`, and `all` with extra care because they often change device behavior.

## Repository Expectations for Polish

- Match the style of official router setup and administration documentation.
- Prefer wording that is clear, neutral, and instructional rather than promotional.
- If the current Polish page contains low-quality machine translation, clean it fully instead of editing only one sentence and leaving the rest broken.

## Polish Final Check

- The Polish reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Polish docs.
