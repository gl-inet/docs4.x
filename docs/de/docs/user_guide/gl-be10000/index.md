# Slate 7 Pro (GL-BE10000) Benutzerhandbuch

## Produktübersicht

Slate 7 Pro (GL-BE10000) ist ein tragbarer Tri-Band-Wi-Fi-7-Reiserouter. Als aufgerüstete Version des Slate 7 (GL-BE3600) verfügt er über einen größeren Touchscreen auf der Oberseite sowie über 1 GB DDR4-RAM und 8 GB eMMC-Flash-Speicher für stabile Leistung und Plug-in-Kompatibilität. Er erreicht hohe VPN-Geschwindigkeiten von bis zu 1.100 Mbit/s mit WireGuard® und 1.000 Mbit/s mit OpenVPN-DCO. Mit 2 × 2,5G-Ethernet-Ports (1 WAN + 1 LAN), 1 × USB-C-3.0-Port und Unterstützung für PD-Stromversorgung bietet er starke Konnektivität und hohen Komfort für Reisen und den mobilen Einsatz.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Lieferumfang

Im Lieferumfang enthalten sind:

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 1 x Ethernet-Kabel
- 1 x Stromkabel
- 1 x Netzadapter
- 4 x Steckeraufsätze (US, EU, UK und AU)

## So richten Sie Slate 7 Pro ein

Für die Einrichtung von Slate 7 Pro verwenden Sie eine der vier unterstützten Methoden für den Internetzugang: Ethernet, Repeater, Tethering und Cellular. Folgen Sie den untenstehenden Schritten.

### 1. Einschalten

Setzen Sie die beiden Teile des Netzadapters zusammen. Verbinden Sie ihn mit Ihrem Router und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Touchscreen

Wenn der Router eingeschaltet wird, erscheint auf dem Bildschirm das GL.iNet-Logo, gefolgt von einer Startfortschrittsanzeige.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

Sobald der Fortschrittsbalken vollständig geladen ist, ist der Startvorgang abgeschlossen und das Gerät wechselt zum Begrüßungsbildschirm. Folgen Sie den Anweisungen, um Ihr Admin-Passwort und das Wi-Fi-Netzwerk einzurichten.

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

Anschließend gelangen Sie zum Startbildschirm. Auf der linken Seite werden Systeminformationen in Echtzeit angezeigt, darunter Systemzeit und Netzwerkgeschwindigkeit, sowie Schnellzugriffskacheln für Wi-Fi, Clients, VPN und weitere Funktionen. Auf der rechten Seite befinden sich Schnellzugriffskacheln für die vier Verbindungsmodi Ethernet, Repeater, Tethering und Cellular.

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

Die unterschiedlichen Farben der vier Schnellzugriffskacheln zeigen verschiedene Netzwerkstatus an.

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **Blau**: Aktiv / mit dem Internet verbunden
- **Gelb**: Verbindung wird hergestellt / Netzwerkfehler
- **Weiß**: Inaktive Verbindung

### 3. Gerät verbinden

Verbinden Sie ein Gerät (z. B. Computer, Laptop oder Smartphone) per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Suchen Sie auf Ihrem Gerät in der Liste der verfügbaren Netzwerke nach dem Wi-Fi-Namen Ihres Routers und geben Sie das Passwort ein, um sich zu verbinden. Den Standardnetzwerknamen (SSID) und das Passwort finden Sie auf dem Etikett des Routers.

### 4. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie eine Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie anschließend auf **Apply**.

### 5. Internet einrichten

Richten Sie Ihren Slate 7 Pro mit einer der unterstützten Methoden für den Internetzugang ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}
    
    1. Verbinden Sie den WAN-Port des Slate 7 Pro per Ethernet-Kabel mit einem Upstream-Gerät (z. B. ISP-Modem, Netzwerkswitch oder Ethernet-Wandanschluss).
    2. Slate 7 Pro versucht automatisch, Netzwerkparameter wie IP-Adresse, Gateway und DNS-Server abzurufen, um eine Ethernet-Verbindung herzustellen.
    3. Sobald die Internetverbindung erfolgreich hergestellt wurde, wird der Ethernet-Bereich auf der Touchscreen-Startseite blau angezeigt (aktiv). Sie können entweder auf der Touchscreen-Startseite auf Ethernet tippen oder sich im Web-Admin-Panel anmelden, um die Verbindungsdetails zu prüfen.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Tippen Sie auf dem Touchscreen auf **Repeater**. Das Gerät beginnt dann mit der Suche nach verfügbaren Wi-Fi-Netzwerken.
    2. Wählen Sie das Wi-Fi-Netzwerk aus, das Slate 7 Pro erweitern soll.
    3. Geben Sie das Passwort ein und tippen Sie auf **Apply**.
    4. Sobald die Internetverbindung erfolgreich hergestellt wurde, wird der Repeater-Bereich auf der Touchscreen-Startseite blau angezeigt (aktiv). Sie können entweder auf der Touchscreen-Startseite auf Repeater tippen oder sich im Web-Admin-Panel anmelden, um die Verbindungsdetails zu prüfen.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät (z. B. Smartphone oder USB-Dongle) über ein USB-Kabel mit dem USB-Port des Routers.
    2. Gehen Sie auf Ihrem Mobilgerät zu den Einstellungen und aktivieren Sie **USB Tethering** oder **Personal Hotspot**. Beim iPhone tippen Sie bei Bedarf auf **Trust This Device**.
    3. Wählen Sie auf dem Touchscreen **Tethering** und tippen Sie auf **Connect**. Der Router stellt dann die Verbindung zu Ihrem Gerät her.
    4. Sobald die Internetverbindung erfolgreich hergestellt wurde, wird der Tethering-Bereich auf der Touchscreen-Startseite blau angezeigt (aktiv). Sie können entweder auf der Touchscreen-Startseite auf Tethering tippen oder sich im Web-Admin-Panel anmelden, um die Verbindungsdetails zu prüfen.

    **Hinweis**: Wenn die Verbindung fehlschlägt, stellen Sie sicher, dass die Versorgungsspannung über 9 V / 3 A liegt, da eine zu niedrige Stromversorgung verhindern kann, dass der USB-Port aktiviert wird. Wiederholen Sie die obigen Schritte oder melden Sie sich im Web-Admin-Panel an, um den Status der Tethering-Verbindung zu prüfen.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Stecken Sie ein Mobilfunk-USB-Modem in den USB-Port des Slate 7 Pro. Das ist nützlich, wenn Sie die Internetverbindung eines USB-Modems mit allen verbundenen Geräten teilen möchten.
    2. Sobald die Internetverbindung erfolgreich hergestellt wurde, wird der Cellular-Bereich auf der Touchscreen-Startseite blau angezeigt (aktiv). Sie können entweder auf der Touchscreen-Startseite auf Cellular tippen oder sich im Web-Admin-Panel anmelden, um die Verbindungsdetails zu prüfen.

---

Nachfolgend finden Sie eine Übersicht über die Funktionen im Web-Admin-Panel von Slate 7 Pro.

## WLAN

Auf der Seite Wireless können Sie Einstellungen für die 6-GHz-, 5-GHz- und 2,4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Definieren von Wi-Fi-Name (SSID), das Aktivieren einer zufälligen BSSID, die Auswahl von Wi-Fi-Sicherheitsmodus und Passwort, die Konfiguration der SSID-Sichtbarkeit sowie die Auswahl von Wi-Fi-Modus, Bandbreite und Kanal.

Darüber hinaus unterstützt Slate 7 Pro MLO-Wi-Fi, also Multi-Link Operation, bei dem mehrere drahtlose Netzwerke gleichzeitig kombiniert werden, um eine höhere Bandbreite und zuverlässigere Verbindungen zu erreichen.

Informationen zur Einrichtung von Wireless finden Sie unter [Wireless](../../interface_guide/wireless.md).

## Clients

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Name, IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie Clients blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, GL.iNet-Router aus der Ferne zu verwalten und auf sie zuzugreifen.
    
    Informationen zur Einrichtung finden Sie unter [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine erweiterte Netzwerkfunktion, die in GL.iNet-Router integriert ist. Sie ermöglicht nahtlosen Fernzugriff auf Ihr Heimnetzwerk ohne Registrierung oder Anmeldung. Mit dem AmneziaWG-Protokoll und integrierter Datenverkehrsverschleierung bleibt Ihre Verbindung stabil und sicher, sodass AstroWarp ideal für zuverlässigen Fernzugriff unterwegs ist. Benutzer können ein AstroWarp-Netzwerk direkt über das Admin-Panel des GL.iNet-Routers einrichten. Koppeln Sie Ihre Router einfach mit einem Zugriffscode, und schon können Sie Ihren Reiserouter in wenigen Sekunden sicher mit Ihrem Heimnetzwerk verbinden.
    
    Informationen zur Einrichtung finden Sie unter [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (Virtual Private Network) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Privatsphäre und Sicherheit (VPN-Client) und ermöglicht den Zugriff auf ein entferntes Netzwerk (VPN-Server). Slate 7 Pro unterstützt die Protokolle OpenVPN und WireGuard.

=== "OpenVPN"

    Slate 7 Pro (und andere GL.iNet-Router) unterstützt das OpenVPN-Protokoll, das starke Sicherheit bietet. Zum Einrichten von OpenVPN folgen Sie diesen Anleitungen:

    * [OpenVPN-Client einrichten](../../interface_guide/openvpn_client.md)
    * [OpenVPN-Server einrichten](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro (und andere GL.iNet-Router) unterstützt das WireGuard-Protokoll, das hohe Geschwindigkeiten und Komfort bietet. Zum Einrichten von WireGuard folgen Sie diesen Anleitungen:

    * [WireGuard-Client einrichten](../../interface_guide/wireguard_client.md)
    * [WireGuard-Server einrichten](../../interface_guide/wireguard_server.md)

## Netzwerk

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen (z. B. Cellular, Repeater und Ethernet) einrichten können. Wenn Ihre aktuelle Internetverbindung ausfällt, schaltet der Router automatisch auf eine andere Internetverbindung um. Dadurch bleibt der Internetzugang reibungslos und unterbrechungsfrei.

    Informationen zur Einrichtung finden Sie unter [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, kurz für Local Area Network, ist ein Netzwerk, das Computer und Geräte innerhalb eines begrenzten geografischen Bereichs wie zu Hause oder im Büro verbindet. Es ermöglicht schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.
    
    Informationen zur Einrichtung finden Sie unter [Lan](../../interface_guide/lan.md).

=== "Gastnetzwerk"

    Damit können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, Gateway- und Netmask-IP-Adressen angeben und Sicherheitseinstellungen wie AP-Isolation für das Gastnetzwerk konfigurieren.

    Informationen zur Einrichtung finden Sie unter [Gastnetzwerk](../../interface_guide/guest_network.md).

---

=== "DNS"

    Auf der DNS-Seite können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren, die DNS-Einstellungen aller Clients überschreiben, benutzerdefinierte DNS-Einstellungen gegenüber VPN-DNS bevorzugen und den DNS-Servermodus auf automatisch oder auf manuell angegebene DNS-Server aus der Ethernet-Verbindung setzen.

    Informationen zur Einrichtung finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie WAN- und LAN-Ports konfigurieren, die WAN-/LAN-Schnittstelle auf Ethernet setzen, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle festlegen sowie die ausgehandelte Portgeschwindigkeit anzeigen.

    Informationen zur Verwaltung der Ethernet-Ports finden Sie unter [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, kurz für Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen deutlich größeren Adressraum und damit praktisch unbegrenzt viele eindeutige IP-Adressen, was für die wachsende Zahl internetfähiger Geräte entscheidend ist.
    
    Informationen zur Einrichtung finden Sie unter [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP Snooping ist eine Technik zur Netzwerkoptimierung in Ethernet-Switches, mit der Multicast-Datenverkehr verwaltet und gesteuert wird.
    
    Informationen zur Einrichtung finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkmodus"

    Der Netzwerkmodus bezeichnet die Konfiguration, die bestimmt, wie ein Gerät eine Verbindung zu einem Netzwerk herstellt und mit anderen Geräten kommuniziert.
    
    Informationen zur Einrichtung finden Sie unter [Netzwerkmodus](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionen Ihres Hauptrouters, einschließlich AdGuard Home, verschlüsseltem DNS und VPN-Client.
    
    Informationen zur Einrichtung finden Sie in diesen Anleitungen:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Drop-in Gateway einrichten](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Netzwerkbeschleunigung kann die CPU-Last senken und die Weiterleitung von Datenpaketen beschleunigen.
    
    Informationen zur Einrichtung finden Sie unter [Network Acceleration](../../interface_guide/network_acceleration.md).

## Durchflusskontrolle

=== "DPI Engine"

    DPI (Deep Packet Inspection) ist eine Kernfunktion des intelligenten Netzwerkmanagements. Sie überwindet die Einschränkungen herkömmlicher Router, die nur Quell- oder Zieladressen identifizieren, analysiert Paketnutzdaten im Detail und erkennt über den Abgleich mit einer Signaturdatenbank präzise die vom Benutzer aufgerufenen Anwendungen und Websites. So werden eine feinere Klassifizierung und Steuerung des Datenverkehrs ermöglicht.
    
    In Kombination mit [Netify](https://www.netify.ai/){target="_blank"} nutzt die DPI-Funktion von GL.iNet ein leichtgewichtiges eingebettetes Plug-in für eine effiziente Bereitstellung. Mit der online aktualisierten Signaturdatenbank von Netify wird zuverlässiges Management ermöglicht, sodass die Netzwerksteuerung präziser und effizienter wird.

    Detaillierte Informationen finden Sie unter [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics bietet ein intelligentes Dashboard zur Datenverkehrsanalyse, das die Netzwerknutzung nach Anwendungen kategorisiert und visualisiert. So können Sie den aktuellen und historischen Datenverkehr besser überwachen und kontrollieren.

    Detaillierte Informationen finden Sie unter [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter bietet intelligente Online-Sicherheit auf Basis einer DPI-gestützten Klassifizierung und blockiert automatisch schädliche oder bösartige Websites, damit Ihr Netzwerk sauber und sicher bleibt.

    Detaillierte Informationen finden Sie unter [Content Filter](../../interface_guide/content_filter.md).

---

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu kontrollieren. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Informationen zur Einrichtung finden Sie unter [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optimiert die Bandbreitenzuweisung, indem wichtige Aktivitäten wie Videoanrufe oder Gaming bei Netzwerküberlastung priorisiert werden. Dadurch werden Latenzen reduziert und die Gesamtleistung des Netzwerks verbessert. Dies gilt für lokalen Client-Datenverkehr und VPN-Client-Tunnel-Datenverkehr, jedoch nicht für Datenverkehr, den der Router als VPN-Server empfängt.

    Detaillierte Informationen finden Sie unter [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) verwaltet den Netzwerkverkehr Ihres Routers intelligent, um Latenzen und „Bufferbloat“ zu minimieren und so Gaming und Sprachanrufe flüssiger zu machen.

    Detaillierte Informationen finden Sie unter [SQM](../../interface_guide/sqm.md).

## Sicherheit

=== "Port Forwarding"

    Portweiterleitung ermöglicht es entfernten Servern und Geräten im Internet, auf Geräte in einem privaten Netzwerk zuzugreifen.
    
    Informationen zur Einrichtung finden Sie unter [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Mit Management Control können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite umfasst die folgenden Optionen:

    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten in Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche aus der Ferne über das Internet, um die Sicherheit gegenüber externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Legen Sie fest, welche Ports am Router geöffnet sind, um potenzielle Schwachstellen und unbefugte Zugriffe zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch verbundene Geräte zu schützen.

    Detaillierte Informationen finden Sie unter [Security](../../interface_guide/security.md).

=== "NAT Mode"

    Auf der Seite NAT Mode können Sie Full Cone NAT und SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Informationen zur Einrichtung finden Sie unter [NAT Mode](../../interface_guide/nat_settings.md).

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen hinzufügt und so eine Anpassung und Erweiterung seiner Möglichkeiten erlaubt.
    
    Informationen zur Einrichtung finden Sie unter [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert die einer Domain zugeordnete IP-Adresse in Echtzeit automatisch. Es ist besonders nützlich für Benutzer, die eine statische IP-Adresse benötigen, um auf ein entferntes Netzwerk zuzugreifen.
    
    Informationen zur Einrichtung finden Sie unter [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Netzwerkspeicher bezeichnet eine zentrale Datenspeicherlösung, die mehreren Benutzern und Geräten den Zugriff auf Dateien und deren gemeinsame Nutzung über ein Netzwerk ermöglicht.
    
    Informationen zur Einrichtung finden Sie unter [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern, die als DNS-Server fungiert, um unerwünschte Inhalte auf allen Geräten in einem Heimnetzwerk zu filtern.
    
    Informationen zur Einrichtung finden Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie überall auf Ihre Geräte und Anwendungen zugreifen können.
    
    Informationen zur Einrichtung finden Sie unter [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier ist eine softwaredefinierte Netzwerklösung, mit der Benutzer sichere virtuelle Netzwerke über das Internet erstellen können, sodass Geräte miteinander verbunden sind, als befänden sie sich im selben lokalen Netzwerk.
    
    Informationen zur Einrichtung finden Sie unter [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Privatsphäre fokussiertes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Es leitet den Internetverkehr über eine Reihe von freiwillig betriebenen Servern (Knoten) weiter, um Standort und Nutzung des Benutzers zu verschleiern und Online-Aktivitäten schwerer nachvollziehbar zu machen.
    
    * [Tor einrichten](../../interface_guide/tor.md)

## System

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungskennzahlen Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche CPU-Auslastung Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um Ressourcen besser zu verwalten.
    * LED Control: Schalten Sie die LED-Anzeigen des Routers ein oder aus, um die optischen Anzeigen anzupassen.
    * Flash Usage: Zeigen Sie die Auslastung des Flash-Speichers Ihres Routers an, damit ausreichend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * Device Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, darunter Uptime, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Device ID, Geräte-MAC und Device S/N.
    * External Storage: Prüfen Sie den Status aller externen Speichermedien, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.
    
    Diese Funktionen liefern wichtige Einblicke und Steuerelemente, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Informationen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche des Routers festlegen oder ändern, damit nur autorisierte Benutzer Einstellungen ändern können.

    Aus Sicherheitsgründen empfehlen wir, **Prevent Weak Password** zu aktivieren.

    Wenn **Prevent Weak Password** aktiviert ist, gelten für neue Passwörter folgende Anforderungen:

    * mindestens 5 und höchstens 63 Zeichen
    * Buchstaben (Groß-/Kleinschreibung wird unterschieden), Zahlen und die Symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sind zulässig
    * Es müssen mindestens zwei der folgenden Kategorien enthalten sein: Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole.

    Detaillierte Informationen finden Sie unter [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Auf der Seite Upgrade können Sie die Firmware Ihres Routers auf die neueste Version aktualisieren, um Leistung, Sicherheit und neue Funktionen zu verbessern. Diese Seite bietet zwei Upgrade-Optionen:

    * Firmware Online Upgrade: Prüft automatisch die neueste Firmware-Version direkt vom Hersteller-Server und installiert sie, was den Aktualisierungsvorgang vereinfacht.
    * Firmware Local Upgrade: Lädt eine Firmware-Datei manuell von Ihrem Computer hoch, sodass Sie Version und Zeitpunkt des Upgrades selbst bestimmen können.

    Mit diesen Optionen halten Sie Ihren Router auf dem neuesten Stand und profitieren von den neuesten Verbesserungen und Fehlerbehebungen.

    Detaillierte Informationen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Mit der Seite Scheduled Tasks können Sie verschiedene Routerfunktionen zeitgesteuert automatisieren und so den Komfort und die Effizienz erhöhen. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LCD Display Schedule: Legen Sie einen Zeitplan fest, um das LCD-Display des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten Lichtemissionen zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie, dass Ihr Router in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität zu erhalten.
    * Wi-Fi Status Schedule: Legen Sie einen Zeitplan für die 6-GHz-/5-GHz-/2,4-GHz-/MLO-Wi-Fi-Bänder fest, um Netzverfügbarkeit und Energieverbrauch besser zu steuern.
    
    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers, damit er Ihren Anforderungen und Vorlieben entspricht.

    Detaillierte Informationen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    Die Seite Display Management bietet Ihnen umfassende Funktionen zur Verwaltung des Touchscreen-Displays und zugehöriger Einstellungen.

    ‒ Wallpaper: Passen Sie Hintergrundbild und Stil beim Aktivieren des Displays an.
    ‒ Brightness: Stellen Sie die Helligkeit des Touchscreens ein. Verwenden Sie den Schieberegler oder geben Sie einen Prozentsatz ein, damit die Anzeige zu unterschiedlichen Lichtverhältnissen passt.
    ‒ Auto Lock: Legen Sie die Zeitspanne fest, nach der sich der Bildschirm bei Inaktivität automatisch sperrt. Der Bereich reicht von 1 Minute bis 30 Minuten.
    ‒ Screen Always On: Mit dieser Option legen Sie fest, ob der Touchscreen dauerhaft eingeschaltet bleibt oder sich nach Inaktivität ausschaltet.
    ‒ Enable Screen Passcode: Legen Sie einen Passcode für den Touchscreen fest, um eine zusätzliche Sicherheitsebene zu schaffen.

    Detaillierte Informationen finden Sie unter [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router einstellen, damit alle geplanten Aufgaben, Protokolle und Systemereignisse korrekt mit Ihrer lokalen Uhrzeit versehen werden. Diese Einstellung ist entscheidend für genaue Aufzeichnungen und die ordnungsgemäße Ausführung zeitbasierter Konfigurationen.

    Detaillierte Informationen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

---

=== "Toggle Button Settings"

    Auf der Seite Toggle Button Settings können Sie die physische Umschalttaste Ihres Routers konfigurieren und ihr bestimmte Funktionen für schnellen Zugriff und einfache Steuerung zuweisen. Damit erhalten Sie praktische Kurzbefehle für häufig verwendete Aufgaben und Einstellungen, was die Benutzerfreundlichkeit verbessert und die Routerverwaltung vereinfacht.

    Detaillierte Informationen finden Sie unter [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen und dabei alle benutzerdefinierten Konfigurationen löschen. Dieser Vorgang stellt die Standardwerte der derzeit installierten Firmware wieder her. Das ist nützlich, wenn Sie hartnäckige Probleme beheben oder mit der Standardkonfiguration der aktuellen Firmware neu beginnen möchten.

    Detaillierte Informationen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Die Seite Log bietet Zugriff auf verschiedene Protokolle, die Aktivitäten und Ereignisse des Routers aufzeichnen, und unterstützt so die Fehlersuche und Leistungsüberwachung. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle zu Systemereignissen und -aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, nützlich zur Diagnose kritischer Probleme.
    * Cloud Log: Protokolle von Interaktionen und Aktivitäten im Zusammenhang mit GoodCloud-Diensten, die in den Router integriert sind.
    * Nginx Log: Protokolle des Nginx-Webservers, falls dieser vom Router verwendet wird, einschließlich Webverkehr und Servervorgängen.
    
    Zusätzlich gibt es auf dieser Seite eine Schaltfläche **Export Log**, mit der Sie alle gesammelten Protokolle für die Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll, um komplexe Probleme zu diagnostizieren und professionelle Hilfe zu erhalten.

    Detaillierte Informationen finden Sie unter [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche. Erfahrene Benutzer können dort Routereinstellungen und Funktionen über die grundlegenden Optionen hinaus fein abstimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
