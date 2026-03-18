---
description: "Use when translating English GL.iNet router documentation into German or editing files under docs/de/docs/**. Covers German terminology, style, and common translation pitfalls."
name: "German Docs Translation Rules"
applyTo: "docs/de/docs/**/*.md"
---

# German Translation Rules

- Write natural, professional German suitable for official technical support documentation.
- Keep tone consistent across the whole page. Do not switch between formal and informal address within one file.
- Remove machine-translation artifacts completely. Do not leave stray Chinese, Japanese, Korean, Russian, or partially untranslated English in German prose.

## German Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `WireGuard`, `OpenVPN`, `GoodCloud`, `DDNS`, `WebDAV`, `DLNA`, `Samba`, `MAC`, `MTU`, `WAN`, `LAN`.
- Prefer `Tunnel` for `tunnel`.
- Prefer `Kill Switch` for `Kill Switch` unless there is a clearly better established term in nearby German docs.
- Prefer `IP-Maskierung` for `IP Masquerading`.
- Prefer `virtuelle Client-IP` for `client virtual IP`.
- Prefer `Fernzugriff` for `remote access`.
- Prefer `Listening-Port` or `Lauschport` consistently within one file.

## Fixed Network and VPN Vocabulary

- Use one consistent translation for these concepts within a file: `Global Mode`, `Policy Mode`, `All Other Traffic`, `VPN Client`, `VPN Server`, `fail over`, `site-to-site`, `guest network`, `traffic source`, `traffic destination`, `routing method`, `port role`, `negotiated speed`.
- Prefer `Global Mode` or `Globaler Modus` consistently within one file.
- Prefer `Policy Mode` or `Richtlinienmodus` consistently within one file.
- Prefer `All Other Traffic` or `gesamter übriger Datenverkehr` consistently within one file.
- Prefer `VPN-Client` and `VPN-Server`.
- Prefer `Failover` for `fail over`.
- Prefer `Site-to-Site` for `site-to-site`.
- Prefer `Gastnetzwerk` for `guest network`.
- Prefer `Datenverkehrsquelle` for `traffic source`.
- Prefer `Datenverkehrsziel` for `traffic destination`.
- Prefer `Routing-Methode` for `routing method`.
- Prefer `Portrolle` for `port role`.
- Prefer `ausgehandelte Geschwindigkeit` for `negotiated speed`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For left-navigation paths, keep the structure exactly as in the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent German UI labels that are not shown in the product.

## German-Specific Pitfalls

- Do not mix English and German inside one sentence unless the English term is an intentional product or UI label.
- Do not leave untranslated fragments such as `tunnel`, `Enabled`, `Sort`, or similar English UI words inside German prose unless they are literal UI labels.
- Do not mistranslate option scope, for example mixing `Allow Access Samba from WAN` with `Allow Access WebDAV from WAN`.
- Do not confuse `traffic source`, `traffic destination`, and `routing method`.
- Do not confuse `remote peer`, `server`, `client`, `device`, and `router`.
- Prefer concise technical German over overly literal sentence structures copied from English.

## VPN and Routing Accuracy Check

- Preserve the distinction between traffic that is matched by a rule and traffic that is excluded from a rule.
- Preserve whether unmatched traffic is allowed, blocked, or routed via local WAN.
- Preserve whether a tunnel fails over to another tunnel, to `All Other Traffic`, or does not fail over at all.
- Preserve whether a setting is per-tunnel or global.
- Translate `enabled`, `disabled`, `default`, `only`, and `all` with extra care because they often change device behavior.

## Repository Expectations for German

- Match the style of official router setup and administration documentation.
- Prefer wording that is clear, neutral, and instructional rather than promotional.
- If the current German page contains low-quality machine translation, clean it fully instead of editing only one sentence and leaving the rest broken.

## German Final Check

- The German reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby German docs.
