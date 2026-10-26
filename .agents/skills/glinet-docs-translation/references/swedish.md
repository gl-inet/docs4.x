# Swedish Translation Rules

Use language code `sv`, display name `Svenska`, language root `docs/sv/`, and site path `/router/sv/4/`. This adds documentation language support; it does not imply Swedish support in the router firmware UI.

## Style

- Use professional, concise Swedish suitable for technical support documentation. Prefer natural Swedish phrasing over literal English syntax.
- Address the reader consistently with `du` and `din`; omit redundant forms of address. Keep explanations neutral and preserve every condition, warning, limitation, and default state.
- Use the imperative consistently for instructions: `Klicka på`, `Välj`, `Aktivera`, `Inaktivera`, `Ange`, `Anslut`.
- Follow Swedish compound and hyphenation conventions, including `VPN-klient` and `IP-adress`. Keep product names and literal UI labels unchanged.
- Preserve numbers, units, IP addresses, ports, and version numbers exactly as written in English. Do not replace decimal points with commas.

## Terminology

These translations apply to explanatory prose and website navigation. Literal firmware UI labels take precedence.

| English | Swedish |
| --- | --- |
| router | router |
| firmware | firmware |
| web Admin Panel | webbadministrationspanelen |
| subnet / subnet mask | subnät / nätmask |
| gateway / default gateway | gateway / standardgateway |
| tunnel | tunnel |
| port forwarding | portvidarebefordran |
| firewall | brandvägg |
| IP address / MAC address | IP-adress / MAC-adress |
| wireless network / guest network | trådlöst nätverk / gästnätverk |
| access point | åtkomstpunkt |
| repeater | repeater |
| tethering | internetdelning (tethering) |
| VPN client / VPN server | VPN-klient / VPN-server |
| remote access / remote peer | fjärråtkomst / fjärrpeer |
| listening port | lyssningsport |
| client virtual IP | klientens virtuella IP-adress |
| IP Masquerading | IP-maskering |
| Global Mode / Policy Mode | globalt läge / policyläge |
| All Other Traffic | all annan trafik |
| traffic source / traffic destination | trafikkälla / trafikdestination |
| routing / routing method | routning / routningsmetod |
| failover | redundansväxling (failover) |
| load balancing | lastbalansering |
| site-to-site | plats-till-plats (site-to-site) |
| Kill Switch | Kill Switch |
| port role / negotiated speed | portroll / förhandlad hastighet |
| enabled / disabled | aktiverad / inaktiverad |
| by default | som standard |
| upstream DNS server | uppströms DNS-server |
| cookie / cookie preferences | cookie / cookieinställningar |

Keep brands, model names, protocols, and standards unchanged, including `GL.iNet`, `GoodCloud`, `GoodPAS`, `AstroWarp`, `OpenVPN`, `WireGuard`, `AdGuard Home`, `DDNS`, `WAN`, `LAN`, `MTU`, `DNS`, `SSID`, `TCP`, `UDP`, and `Wi-Fi`.

## UI, Links, and Technical Review

- Preserve screenshot labels and literal router navigation paths, for example `**VPN** -> **VPN Dashboard**`. Do not invent Swedish firmware labels. Translate website labels, homepage content, accessibility text, and feedback prompts.
- Follow the shared heading ID rules in `common.md`: every heading keeps the explicit English ID of the matching English heading.
- Distinguish clients, servers, routers, devices, and remote peers. Do not conflate the source and destination of traffic or matching and excluded traffic.
- Preserve whether unmatched traffic is allowed, blocked, or sent through local WAN; whether failover uses another tunnel or `All Other Traffic`; and whether settings apply globally or to an individual tunnel.
- Translate `only`, `all`, `must`, negation, default states, and VPN blocking conditions with particular care.

## Repository Expectations for Swedish

- Exclude Downloads from the source set and keep trailing Regulatory Statements out of translated content. Do not add declarations that exist only in other localized guides. Link the homepage Manuals card explicitly to the English Downloads page; do not add that link to the top navigation.
- Keep consent categories, callbacks, analytics behavior, program identifiers, and non-text resource URLs equivalent to English when translating CookieConsent and other JavaScript text.
- When site templates or JavaScript change, check Swedish search, homepage layout, links, image viewer labels, and accessibility text.

## Swedish Final Check

- The Swedish reads naturally from start to finish and consistently uses `du` and `din`.
- No unintended source-language artifacts remain in prose.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby Swedish docs.
