# VPN Dashboard (Firmware v4.7 und früher)

**Hinweis**: Diese Anleitung basiert auf Firmware v4.7 und früher. Für neuere Versionen lesen Sie bitte [hier](vpn_dashboard.md) weiter.

---

Melden Sie sich am webbasierten Admin Panel an und gehen Sie zu **VPN** -> **VPN Dashboard**.

Die Seite VPN Dashboard dient zur Anzeige des Status und der Einstellungen des VPN. Es gibt zwei Bereiche: [VPN Client](#vpn-client) und [VPN Server](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN-Client

Zu Beginn ist weder für OpenVPN noch für WireGuard eine Konfiguration vorhanden. Klicken Sie auf **Set Up Now**; Sie gelangen dann zu den Seiten [OpenVPN Client](openvpn_client.md) bzw. [WireGuard Client](wireguard_client.md).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Sobald die Konfiguration abgeschlossen ist, können Sie die Konfigurationsdatei in der Spalte Configuration file auswählen.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### VPN-Client-Optionen

Klicken Sie auf das Zahnradsymbol von OpenVPN oder WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

OpenVPN-Client-Optionen.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

WireGuard-Client-Optionen.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* Allow Remote Access LAN

    Wenn diese Option aktiviert ist, dürfen die mit dem Router verbundenen Geräte auf das LAN auf der Seite des VPN-Servers zugreifen. Dafür sind auch die entsprechenden Einstellungen auf der VPN-Server-Seite erforderlich.

    Im folgenden Bild bedeutet dies zum Beispiel: Wenn diese Option aktiviert ist, darf *Your Device* auf das *NAS* zugreifen, vorausgesetzt, der *VPN Server* erlaubt den Zugriff auf das NAS in seinem Subnetz ebenfalls.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IP Masquerading

    Wenn diese Option aktiviert ist und LAN-Client-Geräte ihre IP-Pakete senden, ersetzt der Router die Quell-IP-Adresse durch seine eigene Adresse und leitet die Pakete dann in den VPN-Tunnel weiter.

* MTU

    Steht für Maximum Transmission Unit. Die MTU, die Sie für diese Instanz festlegen, überschreibt den MTU-Eintrag in der Konfigurationsdatei.

### Proxy-Modus

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

Wie in der obigen Abbildung zu sehen, ist der aktuelle Proxy-Modus Global Proxy. Klicken Sie auf Global Proxy, um zu anderen Proxy-Modi zu wechseln. Es gibt drei Typen: **Global Proxy**, **Policy Mode** und **Route Mode**.

1. Global Proxy

    Der gesamte Datenverkehr wird durch das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

2. Policy Mode

    1. Basierend auf der Zieldomain oder IP.

        In diesem Modus wird nur der Datenverkehr bestimmter Websites, die über IP-Adresse oder Domainnamen definiert sind, durch das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

    2. Basierend auf dem Client-Gerät.

        In diesem Modus wird nur der Datenverkehr bestimmter lokaler Client-Geräte, die über ihre MAC-Adresse definiert sind, durch das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

    3. Basierend auf dem VLAN.

        In diesem Modus wird nur der Datenverkehr bestimmter VLANs durch das VPN geleitet. Es kann nur eine VPN-Client-Instanz aktiviert werden.

3. Route Mode

    1. Auto detect

        Es werden die Routing-Regeln verwendet, die in jeder VPN-Client-Konfigurationsdatei definiert oder vom VPN-Server bereitgestellt werden.
    
    2. Routing-Regeln anpassen

        Sie können Routing-Regeln für jede VPN-Client-Instanz manuell konfigurieren.

### Globale Optionen des VPN-Clients

Beim Klicken auf **Global Options** wird ein Dialog mit globalen Optionen geöffnet.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    Wenn diese Option aktiviert ist, wird der gesamte Datenverkehr von Client-Geräten blockiert, der versucht, den VPN-Tunnel zu umgehen. Dadurch werden VPN-Lecks wirksam verhindert, die z. B. durch DNS-Konfigurationen von Clients, unterbrochene VPN-Verbindungen oder Anfragen von Client-Apps per IP entstehen.

    Diese Funktion ist auch als [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"} bekannt. Sie soll verhindern, dass Ihre Daten ins Internet durchsickern. Die meisten VPN-Anbieter bieten eine Kill-Switch-Funktion an, die Ihren Computer, Ihr Telefon oder Tablet automatisch vom Internet trennt, wenn die VPN-Verbindung abbricht. Die Funktion Block Non-VPN Traffic auf GL.iNet-Routern deckt noch weitere Leck-Szenarien ab, darunter die folgenden sechs:

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. Dropped VPN Connection

    5. Programs Started Before VPN

    6. Application Specific Leaks

2. Allow Access WAN

    Wenn diese Option aktiviert ist, können Client-Geräte auch bei aktiver VPN-Verbindung weiterhin auf das WAN zugreifen, z. B. auf Drucker, NAS usw. im vorgelagerten Subnetz.

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Wie oben dargestellt, hat Ihr Gerät bei aktivierter Funktion Zugriff auf Geräte im vorgelagerten Subnetz, z. B. auf Drucker und NAS.

    Das Hauptszenario ist, Clients den Zugriff auf Geräte im vorgelagerten Subnetz zu ermöglichen. Da der Router jedoch nicht zwischen dem vorgelagerten Subnetz und dem Internet unterscheiden kann, besteht ein Leckrisiko, wenn Datenverkehr des Client-Geräts direkt per IP erfolgt. Deshalb schließen sich diese Option und Block Non-VPN Traffic gegenseitig aus.

3. Services From GL.iNet Use VPN

    Wenn diese Option aktiviert ist, verwenden Dienste auf dem Router, die normalerweise eine echte IP benötigen, das VPN. Dazu gehören GoodCloud, DDNS und rtty. Zu rtty gehören **Remote SSH** und **Remote Web Access** auf der [GoodCloud-Seite](cloud.md#enable-goodcloud-on-router).

    Der Hauptzweck besteht darin, VPN Client gleichzeitig mit [GoodCloud](cloud.md) und/oder [DDNS](ddns.md) zu verwenden. Wenn Sie GoodCloud nutzen möchten, wird empfohlen, diese Option zu deaktivieren, da GoodCloud sonst durch den VPN-Status in seiner Stabilität beeinträchtigt werden kann. Wenn Sie DDNS nutzen möchten, müssen Sie diese Option deaktivieren, da DDNS sonst auf die IP-Adresse des VPN-Servers zeigt.

## VPN-Server

Zu Beginn sind beide VPN-Server noch nicht initialisiert. Klicken Sie auf **Set Up Now**; Sie gelangen dann zu den Seiten [OpenVPN Server](openvpn_server.md) bzw. [WireGuard Server](wireguard_server.md).

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

Nachdem der OpenVPN-Server und der WireGuard-Server gestartet wurden:

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### OpenVPN-Server-Optionen

Klicken Sie auf das Zahnradsymbol des OpenVPN-Servers.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Wenn diese Option aktiviert ist, kann über den VPN-Tunnel auf Ressourcen innerhalb des LAN-Subnetzes zugegriffen werden.

* **IP Masquerading**

    Wenn diese Option aktiviert ist und LAN-Client-Geräte ihre IP-Pakete senden, ersetzt der Router die Quell-IP-Adresse durch seine eigene Adresse und leitet die Pakete dann in den VPN-Tunnel weiter.

* **MTU**

    Die MTU, die Sie für die Instanz festlegen, überschreibt den MTU-Eintrag in der Konfigurationsdatei.

### Routing-Regeln des OpenVPN-Servers

Klicken Sie auf das Netzwerksymbol des OpenVPN-Servers.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

Im Modus für benutzerdefinierte Routen ignoriert der VPN-Client die Konfigurationsdatei und die vom Server bereitgestellte Routing-Konfiguration. Ob beim Zugriff auf ein Netzwerksegment der vom VPN bereitgestellte verschlüsselte Tunnel verwendet wird, wird durch die von Ihnen manuell festgelegten Routing-Regeln bestimmt.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### WireGuard-Server-Optionen

Klicken Sie auf das Zahnradsymbol des WireGuard-Servers.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Wenn diese Option aktiviert ist, kann über den VPN-Tunnel auf Ressourcen innerhalb des LAN-Subnetzes zugegriffen werden.

* **IP Masquerading**

    Wenn diese Option aktiviert ist und LAN-Client-Geräte ihre IP-Pakete senden, ersetzt der Router die Quell-IP-Adresse durch seine eigene Adresse und leitet die Pakete dann in den VPN-Tunnel weiter.

* **MTU**

    Die MTU, die Sie für die Instanz festlegen, überschreibt den MTU-Eintrag in der Konfigurationsdatei.

* **Client to Client**

    WireGuard-Clients können gegenseitig auf Daten zugreifen. Benutzer können damit im Fernzugriff auf interne Netzwerkgeräte zu Hause oder im Büro zugreifen. Der Datenzugriff über den WireGuard-Server ist dank Verschlüsselung sicherer als Portweiterleitung und nach dem Verbindungsaufbau in der Regel stabiler und schneller.

### Routing-Regeln des WireGuard-Servers

Klicken Sie auf das Netzwerksymbol des WireGuard-Servers.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

Im Modus für benutzerdefinierte Routen ignoriert der VPN-Client die Konfigurationsdatei und die vom Server bereitgestellte Routing-Konfiguration. Ob beim Zugriff auf ein Netzwerksegment der vom VPN bereitgestellte verschlüsselte Tunnel verwendet wird, wird durch die von Ihnen manuell festgelegten Routing-Regeln bestimmt.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Globale Optionen des VPN-Servers

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading**: Wenn diese Option aktiviert ist und auf diesem Router sowohl ein VPN-Server als auch ein VPN-Client laufen, wird der Datenverkehr von Clients, die mit dem VPN-Server verbunden sind, zusätzlich in den Tunnel des VPN-Clients geleitet. [Mehr über VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
