---
description: "Use when translating English GL.iNet router documentation into Japanese or editing files under docs/jp/docs/**. Covers Japanese terminology, style, and common translation pitfalls."
name: "Japanese Docs Translation Rules"
applyTo: "docs/jp/docs/**/*.md"
---

# Japanese Translation Rules

- Write natural, professional Japanese suitable for official support documentation.
- Keep tone consistent. Do not switch between formal and casual styles within a page.
- Remove machine-translation artifacts completely. Do not leave Chinese, Korean, Russian, or stray English fragments in Japanese prose.

## Japanese Terminology

- Keep product names, model names, protocol names, and brand names unchanged: `GL.iNet`, `WireGuard`, `OpenVPN`, `GoodCloud`, `DDNS`, `WebDAV`, `DLNA`, `Samba`, `MAC`, `MTU`, `WAN`, `LAN`.
- Prefer `トンネル` for `tunnel`.
- Prefer `キルスイッチ` for `Kill Switch`.
- Prefer `IPマスカレーディング` for `IP Masquerading`.
- Prefer `クライアント仮想IP` for `client virtual IP`.
- Prefer `リモートアクセス` for `remote access`.
- Prefer `待受ポート` or `リスニングポート` consistently within one file.

## Fixed Network and VPN Vocabulary

- Use one consistent translation for these concepts within a file: `Global Mode`, `Policy Mode`, `All Other Traffic`, `VPN Client`, `VPN Server`, `fail over`, `site-to-site`, `guest network`, `traffic source`, `traffic destination`, `routing method`, `port role`, `negotiated speed`.
- Prefer `グローバルモード` for `Global Mode`.
- Prefer `ポリシーモード` for `Policy Mode`.
- Prefer `その他のすべてのトラフィック` for `All Other Traffic`.
- Prefer `VPNクライアント` and `VPNサーバー`.
- Prefer `フェイルオーバー` for `fail over`.
- Prefer `サイトツーサイト` for `site-to-site`.
- Prefer `ゲストネットワーク` for `guest network`.
- Prefer `トラフィック送信元` for `traffic source`.
- Prefer `トラフィック宛先` for `traffic destination`.
- Prefer `ルーティング方法` for `routing method`.
- Prefer `ポートの役割` for `port role`.
- Prefer `ネゴシエート速度` for `negotiated speed`.

## UI and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- For left-navigation paths, keep the structure exactly as in the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent Japanese UI labels that are not shown in the product.

## Japanese-Specific Pitfalls

- Do not mix `隧道` and `トンネル`. Use `トンネル`.
- Do not leave untranslated fragments such as `tunnel`, `Enabled`, `Sort`, or similar English UI words inside Japanese prose unless they are literal UI labels.
- Do not mistranslate option scope, for example mixing `Allow Access Samba from WAN` with `Allow Access WebDAV from WAN`.
- Do not confuse `traffic source`, `traffic destination`, and `routing method`.
- Do not confuse `remote peer`, `server`, `client`, `device`, and `router`.

## VPN and Routing Accuracy Check

- Preserve the distinction between traffic that is matched by a rule and traffic that is excluded from a rule.
- Preserve whether unmatched traffic is allowed, blocked, or routed via local WAN.
- Preserve whether a tunnel fails over to another tunnel, to `All Other Traffic`, or does not fail over at all.
- Preserve whether a setting is per-tunnel or global.
- Translate `enabled`, `disabled`, `default`, `only`, and `all` with extra care because they often change device behavior.

## Repository Expectations for Japanese

- Match the style used in well-written files under `docs/jp/docs/`.
- Prefer wording that reads like official support documentation for router setup and administration.
- If the current Japanese page contains low-quality machine translation, clean it fully instead of only editing one sentence and leaving the rest broken.

## Japanese Final Check

- The Japanese reads naturally from start to finish.
- No source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Japanese docs.
