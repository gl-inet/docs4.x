# VPN Dashboard (firmware v4.7 och tidigare) {#vpn-dashboard-firmware-v47-and-earlier}

Innehållet bygger på firmware v4.7.x och tidigare. Använd väljaren för en annan version.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.7 and earlier" markdown="1">

- [Firmware v4.8](vpn_dashboard_v4.8.md)
- [Firmware v4.9 and above](vpn_dashboard.md)

</div>

Logga in och öppna **VPN** -> **VPN Dashboard**.

VPN Dashboard visar serveradress, trafikstatistik, klientens virtuella IP och anslutningslogg samt Kill Switch, VPN-princip, IP Masquerading, MTU och VPN Cascading.

This page is divided into two sections: [VPN Client](#vpn-client) and [VPN Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN Client {#vpn-client}

Om ingen OpenVPN- eller WireGuard-konfiguration finns klickar du på **Set Up Now** för att öppna [OpenVPN Client](openvpn_client.md) eller [WireGuard Client](wireguard_client.md) och ladda upp filen.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_setup.png){class="glboxshadow"}

Konfigurationen visas i kolumnen **Configuration File**. Klicka på rutan för att byta mellan flera filer.

![configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_config.png){class="glboxshadow"}

### Client Options {#client-options}

Klicka på kugghjulet till höger för klientalternativ.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options.png){class="glboxshadow"}

The OpenVPN Client Options displays as follows.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_ovpn.png){class="glboxshadow"}

The WireGuard Client Options displays as follows.

![wg client options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: Tillåter fjärråtkomst till routern och LAN-enheter via VPN. Servern måste annonsera en väg till LAN-subnätet.

    I diagrammet fungerar GL.iNet-routern som VPN-klient. När alternativet är aktiverat kan enheter på serversidan nå routern och LAN-enheterna. En routningsregel till routerns LAN-subnät krävs på servern.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver reseroutern om Laptop-käll-IP `192.168.10.200` till tunneladressen `10.1.0.2` vid trafik till NAS `192.168.8.100`.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Anpassar tunnelns MTU och åsidosätter konfigurationsfilens värde.

### Proxy Mode {#proxy-mode}

Standardläget är **Global Proxy**. Klicka på rutan uppe till höger för andra lägen.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_proxy.png){class="glboxshadow"}

Three proxy modes are available: **Global Proxy**, **Policy Mode** and **Route Mode**.

1. Global Proxy

    All trafik dirigeras genom VPN. Endast en VPN-klientinstans kan aktiveras.

2. Policy Mode

    Läget har tre principer.

    - Based on the Target Domain or IP.

        Endast trafik till vissa IP-adresser eller domäner dirigeras genom VPN. En klientinstans kan aktiveras.

    - Based on the Client Device.

        Endast trafik från vissa LAN-enheter identifierade med MAC-adress dirigeras genom VPN.

    - Based on the VLAN.

        Endast trafik från vissa VLAN dirigeras genom VPN.

3. Route Mode

    - Auto Detect

        The routing rules defined in each VPN client configuration file or issued by the VPN server will be used.

    - Customize Routing Rules

        Routningsregler kan konfigureras manuellt för varje klientinstans.

### Global Options {#global-options}

Klicka på **Global Options** uppe till höger för avancerade klientinställningar.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: Tvingar all internettrafik genom VPN och blockerar den vid frånkoppling för att förhindra läckor.

    Funktionen kallas även [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} och stänger automatiskt av internet vid VPN-fel.

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN**: Låter lokala klienter nå skrivare, NAS och andra enheter i uppströms subnät när VPN är aktivt.

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Lokala enheter kan då nå värdar som skrivare och NAS i det uppströms subnätet.

    Routern kan inte skilja uppströms subnätstrafik från vanlig internettrafik, vilket kan medföra läckagerisk via offentliga IP-adresser. **Allow Access WAN** och **Block Non-VPN Traffic** kan därför inte aktiveras samtidigt.

- **Services from GL.iNet Use VPN**: GoodCloud, DDNS och rtty skickar paket genom VPN-tunnlar när alternativet är aktiverat. Det är inaktiverat som standard eftersom tjänsterna normalt kräver enhetens verkliga IP-adress.

## VPN Server {#vpn-server}

Om ingen VPN-server har konfigurerats klickar du på **Set Up Now** för **OpenVPN Server** eller **WireGuard Server**.

![vpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_setup.png){class="glboxshadow"}

After the OpenVPN Server or WireGuard Server is enabled, the page will display the server status as follows.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_connected.png){class="glboxshadow"}

### Server Options {#server-options}

Klicka på kugghjulet till höger för serveralternativ.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options.png){class="glboxshadow"}

The OpenVPN Server Options displays as follows.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_ovpn.png){class="glboxshadow"}

The WireGuard Server Options displays as follows.

![wg server options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: Tillåter åtkomst till resurser i serverns LAN-subnät genom tunneln.

* **IP Masquerading**: Skriver om LAN-klienternas käll-IP till routerns tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver hemroutern om NAS-käll-IP `192.168.8.100` till serverns tunneladress `10.1.0.1` vid trafik till Laptop `192.168.10.200`.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/ip_masquerading.png){class="glboxshadow"}

* **MTU**: Tunnelns MTU åsidosätter konfigurationsfilens värde.

* **Client to Client**: Låter VPN-klienter nå varandra via tunnel-IP. För åtkomst mellan LAN-subnät krävs routningsregler på servern.

### Server Route Rule {#server-route-rule}

Klicka på routningsikonen till höger för egna regler.

![server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule.png){class="glboxshadow"}

Under OpenVPN Server Route Rule klickar du på **Add Route Rule**, anger **Target Address** och **Gateway** och klickar på den gröna bocken.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

Under WireGuard Server Route Rule klickar du på **Add Route Rule**, anger **Target Address** och **Gateway** och klickar på den gröna bocken.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Obs!** Serverns routningsregler låter dig definiera egna routningsposter på VPN-servern med måladress, gateway och andra parametrar för varje regel. Manuellt konfigurerade poster har företräde framför standardinställningarna för routning i VPN-konfigurationsfilen och avgör vilken klienttrafik som skickas genom den krypterade tunneln.

### Global Options {#global-options_1}

Klicka på **Global Options** uppe till höger för avancerade serverinställningar.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: När routern samtidigt är VPN-server och klient dirigeras fjärrklienternas trafik genom den uppströms tunnel som routern använder. [Läs mer](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
