# Ukrainian Translation Rules

Use language code `uk`, display name `Українська`, language root `docs/uk/`, and site path `/router/uk/4/`. This adds documentation language support; it does not imply Ukrainian support in the router firmware UI.

## Style

- Use professional, concise Ukrainian suitable for technical support documentation. Follow current Ukrainian spelling; remove Russian vocabulary, calques, and unintended mixed-language prose.
- Use the plural imperative consistently for instructions: `Відкрийте`, `Виберіть`, `Натисніть`, `Увімкніть`, `Вимкніть`, `Введіть`, `Підключіть`. Avoid switching to the singular imperative or impersonal infinitives within a workflow.
- Use `ви` and `ваш` in lowercase when needed; omit redundant address. Keep explanations neutral and preserve every condition, warning, limitation, and default state.
- Use Ukrainian apostrophes consistently in prose (`з’єднання`, `комп’ютер`); do not alter literal code, commands, option values, or identifiers. Escape apostrophes correctly in JavaScript strings.

## Terminology

These translations apply to explanatory prose and website navigation. Literal firmware UI labels take precedence.

| English | Ukrainian |
| --- | --- |
| router | маршрутизатор |
| firmware | прошивка |
| web Admin Panel | вебпанель адміністрування |
| subnet / subnet mask | підмережа / маска підмережі |
| gateway / default gateway | шлюз / шлюз за замовчуванням |
| tunnel | тунель |
| port forwarding | перенаправлення портів |
| firewall | міжмережевий екран |
| IP address / MAC address | IP-адреса / MAC-адреса |
| wireless network / guest network | бездротова мережа / гостьова мережа |
| access point | точка доступу |
| repeater | ретранслятор |
| tethering | спільний доступ до інтернету через USB |
| VPN client / VPN server | клієнт VPN / сервер VPN |
| remote access / remote peer | віддалений доступ / віддалений вузол |
| listening port | порт прослуховування |
| client virtual IP | віртуальна IP-адреса клієнта |
| IP Masquerading | маскарадинг IP |
| Global Mode / Policy Mode | глобальний режим / режим політик |
| All Other Traffic | увесь інший трафік |
| traffic source / traffic destination | джерело трафіку / призначення трафіку |
| routing / routing method | маршрутизація / метод маршрутизації |
| failover | аварійне перемикання |
| load balancing | балансування навантаження |
| site-to-site | з’єднання між мережами (site-to-site) |
| Kill Switch | аварійне блокування VPN (Kill Switch) |
| port role / negotiated speed | роль порту / узгоджена швидкість |
| enabled / disabled | увімкнено / вимкнено |
| by default | за замовчуванням |
| upstream DNS server | DNS-сервер вищого рівня |
| cookie / cookie preferences | файл cookie / налаштування файлів cookie |

Keep brands, model names, protocols, and standards unchanged, including `GL.iNet`, `GoodCloud`, `GoodPAS`, `AstroWarp`, `OpenVPN`, `WireGuard`, `AdGuard Home`, `DDNS`, `WAN`, `LAN`, `MTU`, `DNS`, `SSID`, `TCP`, `UDP`, and `Wi-Fi`.

## UI, Links, and Technical Review

- Preserve screenshot labels and literal router navigation paths, for example `**VPN** -> **VPN Dashboard**`. Do not invent Ukrainian firmware labels. Translate website labels, homepage content, accessibility text, and feedback prompts.
- Preserve custom heading IDs exactly. For translated headings referenced by links or redirects, retain a corresponding explicit English ID or update every reference and verify the resulting HTML anchor.
- Distinguish clients, servers, routers, devices, and remote peers. Do not conflate the source and destination of traffic or matching and excluded traffic.
- Preserve whether unmatched traffic is allowed, blocked, or sent through local WAN; whether failover uses another tunnel or `All Other Traffic`; and whether settings apply globally or to an individual tunnel.
- Translate `only`, `all`, `must`, negation, default states, and VPN blocking conditions with particular care.

## Repository Expectations for Ukrainian

- Exclude Downloads from the source set and keep trailing Regulatory Statements out of translated content. Do not add declarations that exist only in other localized guides. Link the homepage Manuals card explicitly to the English Downloads page.
- Keep consent categories, callbacks, analytics behavior, program identifiers, and non-text resource URLs equivalent to English when translating CookieConsent and other JavaScript text.
- When site templates or JavaScript change, check Cyrillic text and fonts, Ukrainian search, homepage layout, links, and image viewer/accessibility labels.

## Ukrainian Final Check

- The Ukrainian reads naturally from start to finish.
- No source-language or Russian artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Ukrainian docs.
