# Dutch Translation Rules

Use language code `nl`, display name `Nederlands`, language root `docs/nl/`, and site path `/router/nl/4/`. This adds documentation language support; it does not imply Dutch support in the router firmware UI.

## Style

- Use professional, concise Dutch suitable for technical support documentation. Prefer natural Dutch phrasing over literal English syntax.
- Address the reader consistently with informal `je` and `jouw`; omit redundant forms of address. Keep explanations neutral and preserve every condition, warning, limitation, and default state.
- Use the imperative consistently for instructions: `Klik op`, `Selecteer`, `Schakel ... in`, `Schakel ... uit`, `Voer ... in`, `Sluit ... aan`.
- Follow Dutch compound and hyphenation conventions, including `VPN-client` and `Wi-Fi-netwerk`. Keep product names and literal UI labels unchanged.
- Preserve numbers, units, IP addresses, ports, and version numbers exactly as written in English. Do not replace decimal points with commas.

## Terminology

These translations apply to explanatory prose and website navigation. Literal firmware UI labels take precedence.

| English | Dutch |
| --- | --- |
| router | router |
| firmware | firmware |
| web Admin Panel | webbeheerpaneel |
| subnet / subnet mask | subnet / subnetmasker |
| gateway / default gateway | gateway / standaardgateway |
| tunnel | tunnel |
| port forwarding | port forwarding |
| firewall | firewall |
| IP address / MAC address | IP-adres / MAC-adres |
| wireless network / guest network | draadloos netwerk / gastnetwerk |
| access point | access point |
| repeater | repeater |
| tethering | tethering |
| VPN client / VPN server | VPN-client / VPN-server |
| remote access / remote peer | externe toegang / externe peer |
| listening port | luisterpoort |
| client virtual IP | virtueel IP-adres van de client |
| IP Masquerading | IP-masquerading |
| Global Mode / Policy Mode | globale modus / beleidsmodus |
| All Other Traffic | al het overige verkeer |
| traffic source / traffic destination | verkeersbron / verkeersbestemming |
| routing / routing method | routering / routeringsmethode |
| failover | failover |
| load balancing | load balancing |
| site-to-site | site-to-site |
| Kill Switch | Kill Switch |
| port role / negotiated speed | poortrol / onderhandelde snelheid |
| enabled / disabled | ingeschakeld / uitgeschakeld |
| by default | standaard |
| upstream DNS server | upstream DNS-server |
| cookie / cookie preferences | cookie / cookievoorkeuren |

Keep brands, model names, protocols, and standards unchanged, including `GL.iNet`, `GoodCloud`, `GoodPAS`, `AstroWarp`, `OpenVPN`, `WireGuard`, `AdGuard Home`, `DDNS`, `WAN`, `LAN`, `MTU`, `DNS`, `SSID`, `TCP`, `UDP`, and `Wi-Fi`.

## UI, Links, and Technical Review

- Preserve screenshot labels and literal router navigation paths, for example `**VPN** -> **VPN Dashboard**`. Do not invent Dutch firmware labels. Translate website labels, homepage content, accessibility text, and feedback prompts.
- Follow the shared heading ID rules in `common.md`: every heading keeps the explicit English ID of the matching English heading.
- Distinguish clients, servers, routers, devices, and remote peers. Do not conflate the source and destination of traffic or matching and excluded traffic.
- Preserve whether unmatched traffic is allowed, blocked, or sent through local WAN; whether failover uses another tunnel or `All Other Traffic`; and whether settings apply globally or to an individual tunnel.
- Translate `only`, `all`, `must`, negation, default states, and VPN blocking conditions with particular care.

## Repository Expectations for Dutch

- Exclude Downloads from the source set and keep trailing Regulatory Statements out of translated content. Do not add declarations that exist only in other localized guides. Link the homepage Manuals card explicitly to the English Downloads page; do not add that link to the top navigation.
- Keep consent categories, callbacks, analytics behavior, program identifiers, and non-text resource URLs equivalent to English when translating CookieConsent and other JavaScript text.
- When site templates or JavaScript change, check Dutch search, homepage layout, links, image viewer labels, and accessibility text.

## Dutch Final Check

- The Dutch reads naturally from start to finish and consistently uses `je` and `jouw`.
- No unintended source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Dutch docs.
