# VPN Dashboard (firmware v4.7 en ouder) {#vpn-dashboard-firmware-v47-and-earlier}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.7.x en ouder. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.7 en ouder" markdown="1">

- [Firmware v4.8](vpn_dashboard_v4.8.md)
- [Firmware v4.9 en hoger](vpn_dashboard.md)

</div>

Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **VPN Dashboard**.

VPN Dashboard toont VPN-verbindingsgegevens, zoals serveradres, verkeersstatistieken, virtueel IP-adres van de client en verbindingslogboek. Je kunt ook VPN Kill Switch, VPN-beleid, IP Masquerading, MTU en VPN Cascading configureren.

De pagina bestaat uit [VPN Client](#vpn-client) en [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client {#vpn-client}

Als bij het eerste bezoek geen configuratiebestand voor OpenVPN of WireGuard beschikbaar is, ziet de pagina er als volgt uit. Klik op **Set Up Now** om via [OpenVPN Client](openvpn_client.md) of [WireGuard Client](wireguard_client.md) een configuratiebestand te uploaden.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_setup.png){class="glboxshadow"}

Na uploaden verschijnt de configuratie in de kolom **Configuration File**. Klik op het vak om tussen meerdere bestanden te wisselen.

![configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_config.png){class="glboxshadow"}

### Clientopties {#client-options}

Klik rechts op het tandwielpictogram om de OpenVPN- of WireGuard-clientopties te openen.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options.png){class="glboxshadow"}

OpenVPN Client Options ziet er als volgt uit.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_ovpn.png){class="glboxshadow"}

WireGuard Client Options ziet er als volgt uit.

![wg client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: staat via VPN externe toegang tot deze router en LAN-apparaten toe. De VPN-server moet een route naar het LAN-subnet bekendmaken.

    In het onderstaande diagram werkt de GL.iNet-router als VPN-client en verbindt via de tunnel met een VPN-server. Wanneer deze optie is ingeschakeld, kunnen apparaten aan de serverzijde zowel de router als de LAN-apparaten bereiken. Hiervoor moet op de VPN-server een routeringsregel naar het LAN-subnet worden toegevoegd.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en Laptop (192.168.10.200) op het reis-LAN verkeer naar de thuis-NAS (192.168.8.100) stuurt, herschrijft de reisrouter het bron-IP van `192.168.10.200` naar het tunneladres `10.1.0.2`. De serverzijde ziet het verkeer daardoor als afkomstig van de client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

- **MTU**: afkorting van Maximum Transmission Unit. Deze optionele instelling overschrijft de MTU uit het configuratiebestand.

### Proxymodus {#proxy-mode}

De standaardproxymodus is **Global Proxy**. Klik rechtsboven op het vak om een andere modus te selecteren.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_proxy.png){class="glboxshadow"}

Er zijn drie proxymodi: **Global Proxy**, **Policy Mode** en **Route Mode**.

1. Global Proxy

    In deze modus wordt al het verkeer via de VPN gerouteerd. Er kan slechts één VPN-clientinstantie actief zijn.

2. Policy Mode

    Deze modus bevat drie beleidsopties.

    - Op basis van het doeldomein of IP-adres.

        Alleen verkeer naar bepaalde websites, geïdentificeerd via IP-adres of domeinnaam, wordt via VPN gerouteerd. Er kan slechts één clientinstantie actief zijn.

    - Op basis van het clientapparaat.

        Alleen verkeer van bepaalde LAN-apparaten, geïdentificeerd via MAC-adres, wordt via VPN gerouteerd.

    - Op basis van VLAN.

        Alleen verkeer van een bepaald VLAN wordt via VPN gerouteerd.

3. Route Mode

    - Auto Detect

        De routeringsregels uit elk clientconfiguratiebestand of van de VPN-server worden gebruikt.

    - Customize Routing Rules

        Je kunt routeringsregels voor elke VPN-clientinstantie handmatig configureren.

### Globale opties {#global-options}

Klik rechtsboven op **Global Options** om geavanceerde clientinstellingen te configureren.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: dwingt al het internetverkeer uitsluitend via de VPN-tunnel en blokkeert bij uitval alle internettoegang. Hierdoor valt verkeer niet terug op WAN en worden VPN-lekken door uitval of onjuiste DNS-instellingen voorkomen.

    Deze functie heet ook [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} en voorkomt dat gebruikersgegevens online worden blootgesteld. Block Non-VPN Traffic biedt brede bescherming tegen DNS-, IPv6-, WebRTC- en toepassingslekken en VPN-uitval.

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN**: lokale clients kunnen tijdens een actieve VPN WAN-diensten bereiken, zoals printers, NAS en apparaten in het upstream subnet.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Met deze functie kunnen lokale apparaten hosts in het upstream subnet, zoals printers en NAS, bereiken.

    De optie is bedoeld voor toegang tot apparaten in het upstream subnet. De router kan dit verkeer echter niet van normaal internetverkeer onderscheiden. Directe toegang via openbare IP-adressen kan verkeer lekken. Daarom kunnen **Allow Access WAN** en **Block Non-VPN Traffic** niet tegelijk worden ingeschakeld.

- **Services From GL.iNet Use VPN**: GoodCloud, DDNS en rtty verzenden pakketten via VPN-tunnels. Standaard uitgeschakeld omdat deze diensten gewoonlijk het werkelijke IP-adres vereisen.

## VPN Server {#vpn-server}

Als de router nog niet als OpenVPN- of WireGuard-server is geconfigureerd, ziet de pagina er als volgt uit. Klik op **Set Up Now** om via **OpenVPN Server** of **WireGuard Server** de server te initialiseren.

![vpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_setup.png){class="glboxshadow"}

Na inschakeling van OpenVPN Server of WireGuard Server wordt de serverstatus als volgt weergegeven.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_connected.png){class="glboxshadow"}

### Serveropties {#server-options}

Klik rechts op het tandwielpictogram om de serveropties te openen.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options.png){class="glboxshadow"}

OpenVPN Server Options ziet er als volgt uit.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_ovpn.png){class="glboxshadow"}

WireGuard Server Options ziet er als volgt uit.

![wg server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: bronnen in het LAN-subnet van de server zijn via de VPN-tunnel toegankelijk.

* **IP Masquerading**: herschrijft bron-IP-adressen van LAN-clients naar het tunnel-IP van de router. Schakel dit alleen uit bij Site-to-Site als de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en NAS (192.168.8.100) op het thuis-LAN verkeer naar Laptop (192.168.10.200) stuurt, herschrijft de thuisrouter het bron-IP naar server-tunneladres `10.1.0.1`. De externe zijde ziet het verkeer daardoor als afkomstig van de server.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

* **MTU**: afkorting van Maximum Transmission Unit. De ingestelde tunnelwaarde overschrijft de MTU in het configuratiebestand.

* **Client to Client**: clients op deze server kunnen elkaar via hun tunnel-IP bereiken. Voeg serverrouteringsregels toe om ook toegang tot elkaars LAN-subnets toe te staan.

### Serverrouteringsregel {#server-route-rule}

Klik rechts op het routepictogram om OpenVPN- of WireGuard-routeringsregels aan te passen.

![server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule.png){class="glboxshadow"}

OpenVPN Server Route Rule ziet er als volgt uit. Klik op **Add Route Rule**, voer **Target Address** en **Gateway** in en klik op het groene vinkje.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

WireGuard Server Route Rule ziet er als volgt uit. Klik op **Add Route Rule**, voer **Target Address** en **Gateway** in en klik op het groene vinkje.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Opmerking**: in de modus voor aangepaste routes negeert de VPN-client het configuratiebestand en de serverroutes. Handmatige routeringsregels bepalen of een netwerksegment via de versleutelde tunnel wordt bereikt.

### Globale opties {#global-options_1}

Klik rechtsboven op **Global Options** om geavanceerde serverinstellingen te configureren.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: als de router tegelijk server en client is, wordt verkeer van externe clients op de server via de upstream VPN-tunnel van de client gerouteerd. [Lees meer over VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
