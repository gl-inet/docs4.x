# VPN Dashboard (Firmware v4.7 und früher)

Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **VPN** -> **VPN Dashboard**.

Die Seite VPN Dashboard zeigt Details zur VPN-Verbindung an, z. B. Serveradresse, Datenverkehrsstatistiken, virtuelle Client-IP und Verbindungsprotokoll. Außerdem können Sie dort erweiterte Einstellungen wie VPN Kill Switch, VPN-Richtlinie, IP-Maskierung, MTU und VPN Cascading konfigurieren.

Diese Seite ist in zwei Bereiche unterteilt: [VPN-Client](#vpn-client) und [VPN-Server](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## VPN-Client

Wenn Sie diese Seite zum ersten Mal aufrufen und noch keine Konfigurationsdatei für OpenVPN und WireGuard vorhanden ist, wird die Seite wie folgt angezeigt. Klicken Sie auf **Set Up Now**. Sie werden dann zur Seite [OpenVPN Client](openvpn_client.md) oder [WireGuard Client](wireguard_client.md) weitergeleitet, um Ihre VPN-Konfigurationsdatei hochzuladen.

![vpn client set up](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

Nach dem Hochladen wird Ihre Konfiguration in der Spalte **Configuration File** angezeigt. Wenn Sie mehrere Konfigurationsdateien hochgeladen haben, können Sie durch Klicken auf das Feld zwischen ihnen wechseln.

![configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### Client-Optionen

Klicken Sie rechts auf das Zahnradsymbol, um die Optionen des OpenVPN- oder WireGuard-Clients aufzurufen.

![vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

Die Optionen des OpenVPN-Clients werden wie folgt angezeigt.

![openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

Die Optionen des WireGuard-Clients werden wie folgt angezeigt.

![wg client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: Wenn aktiviert, ist der Fernzugriff auf diesen Router und seine LAN-Geräte über VPN erlaubt. Der VPN-Server muss eine Route zum LAN-Subnetz dieses Routers bekanntgeben.

    Wie im Diagramm unten gezeigt, arbeitet der GL.iNet-Router als VPN-Client und verbindet sich über den VPN-Tunnel mit einem VPN-Server. Wenn diese Option aktiviert ist, können sowohl der GL.iNet-Router als auch seine LAN-seitigen Geräte von Geräten auf der VPN-Server-Seite (z. B. einem NAS) erreicht werden. Dafür müssen Sie auf dem VPN-Server eine Routing-Regel hinzufügen, damit das LAN-Subnetz des GL.iNet-Routers erreichbar ist.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: Wenn aktiviert, werden die Quell-IP-Adressen von LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie dies nur bei Site-to-Site-Setups, in denen der entfernte Peer Ihre LAN-Subnetze kennt.

- **MTU**: Kurz für Maximum Transmission Unit. Mit dieser optionalen Einstellung können Sie die MTU des VPN-Tunnels anpassen; sie überschreibt den in der Konfigurationsdatei definierten Wert.

### Proxy-Modus

Der Standard-Proxy-Modus für die VPN-Verbindung ist **Global Proxy**. Sie können oben rechts auf das Feld klicken, um zu anderen Proxy-Modi zu wechseln.

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

Es stehen drei Proxy-Modi zur Verfügung: **Global Proxy**, **Policy Mode** und **Route Mode**.

1. Global Proxy

    In diesem Modus wird der gesamte Datenverkehr über das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

2. Policy Mode

    Dieser Modus kann weiter in drei Richtlinien unterteilt werden.

    - Based on the Target Domain or IP.

        In diesem Modus wird nur der Datenverkehr bestimmter Websites, die über IP-Adresse oder Domainnamen identifiziert werden, über das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

    - Based on the Client Device.

        In diesem Modus wird nur der Datenverkehr bestimmter LAN-Geräte, die über MAC-Adressen identifiziert werden, über das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

    - Based on the VLAN.

        In diesem Modus wird nur der Datenverkehr bestimmter VLANs über das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

3. Route Mode

    - Auto Detect

        Es werden die Routing-Regeln verwendet, die in jeder VPN-Client-Konfigurationsdatei definiert oder vom VPN-Server bereitgestellt werden.

    - Customize Routing Rules

        Sie können die Routing-Regeln für jede VPN-Client-Instanz manuell konfigurieren.

### Globale Optionen

Klicken Sie oben rechts auf **Global Options**, um erweiterte Einstellungen für Ihren VPN-Client zu konfigurieren.

![vpnclient global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: Wenn aktiviert, wird der gesamte Internetverkehr gezwungen, ausschließlich durch den VPN-Tunnel zu laufen, und kann nicht über andere Schnittstellen wie das lokale ISP-WAN geleitet werden. Wenn die VPN-Verbindung unerwartet abbricht, wird der gesamte Internetverkehr vollständig blockiert, damit kein Rückfall auf das normale WAN erfolgt. So werden VPN-Lecks durch VPN-Ausfälle, falsche DNS-Einstellungen auf Client-Geräten und ähnliche Probleme vermieden.

    Diese Funktion ist auch als [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} bekannt. Sie verhindert, dass Benutzerdaten online offengelegt werden. Ein typischer Kill Switch kappt den Internetzugang automatisch, wenn die VPN-Verbindung fehlschlägt. Die Funktion Block Non-VPN Traffic auf GL.iNet-Routern bietet einen umfassenderen Schutz vor Lecks und deckt die folgenden Szenarien ab:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN**: Wenn aktiviert, können lokale Client-Geräte auch bei aktivem VPN weiterhin auf WAN-seitige Dienste zugreifen (z. B. auf Drucker, NAS und andere Geräte im vorgelagerten Subnetz).

    ![vpn client allow access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Wie im obigen Diagramm gezeigt, können Ihre lokalen Geräte mit dieser Funktion Hosts im vorgelagerten Subnetz erreichen, z. B. Drucker und NAS.

    Diese Option ist in erster Linie dafür gedacht, Clients den Zugriff auf Geräte im vorgelagerten Subnetz zu ermöglichen. Der Router kann jedoch Datenverkehr zum vorgelagerten Subnetz nicht von normalem Internetverkehr unterscheiden. Wenn Client-Geräte Ressourcen direkt über öffentliche IP-Adressen aufrufen, besteht ein potenzielles Risiko für Datenverkehrslecks. Deshalb schließen sich **Allow Access WAN** und **Block Non-VPN Traffic** gegenseitig aus und können nicht gleichzeitig aktiviert werden.

- **Services From GL.iNet Use VPN**: Wenn aktiviert, übertragen GoodCloud, DDNS und rtty ihre Pakete über VPN-Tunnel. Diese Option ist standardmäßig deaktiviert, da diese Dienste normalerweise die echte IP-Adresse des Geräts benötigen, um ordnungsgemäß zu funktionieren.

## VPN-Server

Wenn der Router noch nie als OpenVPN- oder WireGuard-Server konfiguriert wurde, wird die Seite wie unten gezeigt angezeigt. Klicken Sie auf **Set Up Now**. Sie werden dann zur Seite **OpenVPN Server** oder **WireGuard Server** weitergeleitet, um Ihren VPN-Server zu initialisieren.

![vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

Sobald der OpenVPN-Server oder WireGuard-Server aktiviert ist, zeigt die Seite den Serverstatus wie folgt an.

![vpn server enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### Server-Optionen

Klicken Sie rechts auf das Zahnradsymbol, um die Optionen des OpenVPN- oder WireGuard-Servers aufzurufen.

![vpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

Die Optionen des OpenVPN-Servers werden wie folgt angezeigt.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

Die Optionen des WireGuard-Servers werden wie folgt angezeigt.

![wg server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: Wenn aktiviert, kann über den VPN-Tunnel auf Ressourcen innerhalb des LAN-Subnetzes des Servers zugegriffen werden.

* **IP Masquerading**: Wenn aktiviert, werden die Quell-IP-Adressen von LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie dies nur bei Site-to-Site-Setups, in denen der entfernte Peer Ihre LAN-Subnetze kennt.

* **MTU**: Kurz für Maximum Transmission Unit. Der MTU-Wert, den Sie für den Tunnel festlegen, überschreibt die MTU-Einstellungen in der Konfigurationsdatei.

* **Client to Client**: Wenn aktiviert, können VPN-Clients, die mit diesem Server verbunden sind, über ihre VPN-Tunnel-IPs aufeinander zugreifen. Wenn Sie möchten, dass Clients zusätzlich auf die LAN-Subnetze der jeweils anderen zugreifen können, muss der VPN-Server entsprechende Routen zu diesen entfernten LAN-Subnetzen bekanntgeben.

* **Client to Client**: Wenn aktiviert, können VPN-Clients, die mit diesem Server verbunden sind, über ihre VPN-Tunnel-IPs aufeinander zugreifen. Wenn Sie möchten, dass Clients zusätzlich auf die LAN-Subnetze der jeweils anderen zugreifen können, müssen Sie auf dem VPN-Server Routing-Regeln hinzufügen, die Routen zu diesen entfernten LAN-Subnetzen bekanntgeben.

### Server-Routenregel

Klicken Sie rechts auf das Routensymbol, um die OpenVPN- oder WireGuard-Routenregeln nach Bedarf anzupassen.

![server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

Die OpenVPN-Server-Routenregel wird wie folgt angezeigt. Klicken Sie auf **Add Route Rule**, geben Sie **Target Address** und **Gateway** ein und klicken Sie dann zum Übernehmen auf das grüne Häkchen-Symbol.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

Die WireGuard-Server-Routenregel wird wie folgt angezeigt. Klicken Sie auf **Add Route Rule**, geben Sie **Target Address** und **Gateway** ein und klicken Sie dann zum Übernehmen auf das grüne Häkchen-Symbol.

![wg server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Hinweis**: Im Modus für benutzerdefinierte Routen ignoriert der VPN-Client die Konfigurationsdatei und die vom Server bereitgestellte Routing-Konfiguration. Ob beim Zugriff auf ein beliebiges Netzwerksegment der vom VPN bereitgestellte verschlüsselte Tunnel verwendet wird, wird durch die von Ihnen manuell festgelegten Routing-Regeln bestimmt.

### Globale Optionen

Klicken Sie oben rechts auf **Global Options**, um erweiterte Einstellungen für Ihren VPN-Server zu konfigurieren.

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![vpn server global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: Wenn aktiviert und dieser Router gleichzeitig als VPN-Server und VPN-Client arbeitet, wird der Datenverkehr entfernter VPN-Clients, die mit dem VPN-Server dieses Routers verbunden sind, durch den vorgelagerten VPN-Tunnel geleitet, den dieser Router als VPN-Client verwendet. [Mehr über VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
