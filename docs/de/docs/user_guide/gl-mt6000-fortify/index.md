# Fortify (GL-MT6000) Benutzerhandbuch

## Sicherheitshinweise

Lesen Sie vor der Verwendung des Geräts alle nachstehenden Sicherheitsinformationen sorgfältig durch. Die nachfolgenden Sicherheitsempfehlungen können nicht sämtliche möglicherweise auftretenden Gefahrensituationen abdecken.

Installieren oder verwenden Sie das Gerät nicht in Umgebungen mit hohen Temperaturen, starker Staubentwicklung, schädlichen Gasen, Brandgefahr, Explosionsgefahr, starken elektromagnetischen Störungen, instabiler Netzspannung, starken Vibrationen oder starker Lärmeinwirkung.

Installieren oder verwenden Sie das Gerät nicht in feuchten Umgebungen, in denen Wasseransammlungen, eindringendes Wasser, Tropfwasser oder Kondensat auftreten können, da dies einen Stromschlag verursachen kann.

Elektromagnetische Störungen können von jedem Gerät ausgehen, das elektromagnetische Signale aussendet. Um Störungen medizinischer Geräte zu vermeiden, befolgen Sie beim Betrieb dieses Geräts insbesondere in Krankenhäusern, ambulanten Gesundheitszentren, Arztpraxen und sonstigen medizinischen Einrichtungen die Anweisungen und Vorgaben des autorisierten Personals, um eine Beeinflussung empfindlicher medizinischer Geräte auszuschließen.

Sofern das Gerät mit einem Netzteil ausgeliefert wird, verwenden Sie zur Stromversorgung ausschließlich das mitgelieferte Netzteil.

Sofern das Gerät mit einem Bildschirm ausgestattet ist und dieser Risse oder Beschädigungen aufweist, verwenden Sie das Gerät nicht weiter. Gebrochenes Glas oder gebrochener Kunststoff kann zu Verletzungen an Händen oder im Gesicht führen.

Sofern das Gerät mit einer Batterie ausgestattet ist, verwenden Sie ausschließlich Batterien, die den Anforderungen der Spezifikation entsprechen. Weist die Batterie sichtbare Beschädigungen auf, tauschen Sie sie aus, da es andernfalls zu Personenschäden kommen kann. Funkendgeräte dürfen nur bei geschlossener Batterieabdeckung betrieben werden.

Bewahren Sie kleine Batterien und Kleinteile, die verschluckt werden könnten, für Kinder unzugänglich auf. Das Verschlucken einer Batterie kann schwere Verletzungen verursachen; nehmen Sie in diesem Fall unverzüglich ärztliche Hilfe in Anspruch.

Vermeiden Sie ein häufiges Umstellen des Geräts. Schalten Sie vor jedem Bewegen oder Transportieren sämtliche Stromversorgungen aus und ziehen Sie alle Netz- und Anschlusskabel ab.

Überlastete Steckdosen, Verlängerungskabel und Steckdosenleisten können Brände und Stromschläge verursachen.

Durch Wärmestau kann sich das Gerät übermäßig erhitzen. Stellen Sie das Gerät daher nicht auf Teppiche oder weiche Unterlagen und sorgen Sie für eine ausreichende Luftzirkulation im Umfeld des Geräts. Stellen Sie das Gerät nicht auf Oberflächen von Gegenständen, die empfindlich auf Wärme reagieren.

Um den einwandfreien Betrieb des Geräts zu gewährleisten, beachten Sie die in den technischen Daten angegebene zulässige Betriebsumgebungstemperatur des Geräts.

Unsachgemäßes Öffnen oder unsachgemäße Instandsetzung kann den Benutzer des Geräts gefährden.

Schalten Sie bei einem Störfall zuerst den Netzschalter aus.

## Produktübersicht

Fortify (GL-MT6000) ist ein von GL.iNet und ExpressVPN gemeinsam veröffentlichter Wi-Fi-6-Router. Jedes Gerät enthält ein kostenloses einjähriges ExpressVPN-Abonnement. Benutzer können das Abonnement direkt im web Admin Panel des Routers einlösen und ihr Konto binden. Nach der Aktivierung nutzt der gesamte Datenverkehr über den Router das Hochgeschwindigkeitsnetzwerk und die starke Verschlüsselung von ExpressVPN, um Netzwerkverbindung und Online-Privatsphäre zu schützen.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Fortify einrichten

### 1. Einschalten

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an den Fortify-Router an und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Gerät verbinden

Verbinden Sie ein Gerät, z. B. Computer, Laptop oder Smartphone, per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät mit einem Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Öffnen Sie auf Ihrem Gerät Settings -> WLAN, wählen Sie den Wi-Fi-Netzwerknamen des Routers aus und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett des Routers.

### 3. Im web Admin Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie oben rechts die Sprache aus, legen Sie Ihr Admin-Passwort fest und klicken Sie auf **Next**. Das Passwort muss 10 bis 63 Zeichen lang sein und mindestens zwei der folgenden Zeichenarten enthalten: Großbuchstaben, Kleinbuchstaben, Zahlen und Sonderzeichen.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Richten Sie Ihr Wi-Fi ein. Wenn Sie die Wi-Fi-Informationen ändern, müssen Sie Ihr Gerät mit den neuen Zugangsdaten erneut mit dem Wi-Fi des Routers verbinden.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Internet einrichten

**Note:** Die folgenden Anweisungen gelten für die Einrichtung über das GL.iNet web Admin Panel. Wenn Sie die [GL.iNet App](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"} bevorzugen, laden Sie sie herunter und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Fortify mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering oder Cellular. Wenn Sie [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Verbinden Sie den WAN-Port Ihres Fortify-Routers mit einem Ethernet-Kabel mit einem Upstream-Gerät, z. B. einem Modem.

    Nach erfolgreicher Internetverbindung leuchtet die Router-LED dauerhaft weiß.

    Weitere Informationen finden Sie unter [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Gehen Sie im web Admin Panel zum Abschnitt INTERNET -> Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi aus der Liste der verfügbaren Netzwerke aus.
    3. Geben Sie das Passwort ein und klicken Sie auf **Apply**.

    Nach erfolgreicher Internetverbindung leuchtet die Router-LED dauerhaft weiß.

    Weitere Informationen finden Sie unter [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Smartphone über ein USB-Kabel mit dem USB-Port des Routers.
    2. Aktivieren Sie auf dem Smartphone USB Tethering. Vertrauen Sie bei einem iPhone diesem Gerät und aktivieren Sie Personal Hotspot.
    3. Gehen Sie im web Admin Panel zum Abschnitt INTERNET -> Tethering und klicken Sie auf **Connect**.

    Nach erfolgreicher Internetverbindung leuchtet die Router-LED dauerhaft weiß.

    Weitere Informationen finden Sie unter [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Schließen Sie ein USB-Mobilfunkmodem an den USB-Port des Routers an, um dessen Internetverbindung für alle verbundenen Geräte freizugeben.

    Nach erfolgreicher Internetverbindung leuchtet die Router-LED dauerhaft weiß.

    Weitere Informationen finden Sie unter [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Nachfolgend finden Sie eine Übersicht der Funktionen im Fortify web Admin Panel.

## Wireless

Die Wireless-Seite dient zum Konfigurieren der Wi-Fi-Netzwerke von Fortify, einschließlich Main Network, Guest Network und IoT Network. Jedes Netzwerk unterstützt 2,4 GHz und 5 GHz.

Informationen zur Einrichtung finden Sie unter [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

Die Clients-Seite zeigt verbundene Geräte mit Gerätename, Verbindungstyp, IP- und MAC-Adresse, Download- und Upload-Geschwindigkeit sowie Datenverkehr an. Außerdem können Sie bestimmte Clients mit einem Klick blockieren oder weitere Aktionen ausführen.

Weitere Informationen finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, GL.iNet-Router aus der Ferne aufzurufen und zu verwalten.

    Weitere Informationen finden Sie unter [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist für nahtlose Remote-Netzwerke auf GL.iNet-Routern vorgesehen. Es nutzt das AmneziaWG-Protokoll mit integrierter Datenverkehrsverschleierung für stabilen und sicheren Fernzugriff.

    Weitere Informationen finden Sie unter [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (Virtual Private Network) erstellt sichere, verschlüsselte Datenverkehrstunnel zwischen Ihrem lokalen Gerät und dem VPN-Server. Es erhöht Privatsphäre und Sicherheit des VPN-Clients und ermöglicht den Zugriff auf das entfernte VPN-Servernetzwerk.

Fortify ist in [ExpressVPN](https://www.expressvpn.com/){target="_blank"} integriert, sodass Sie eine ExpressVPN-Verbindung schnell aktivieren können. Jedes Fortify-Gerät enthält ein kostenloses einjähriges ExpressVPN-Abonnement, das Sie direkt im web Admin Panel einlösen und mit Ihrem ExpressVPN-Konto binden können.

Zum Einlösen des kostenlosen Abonnements und Einrichten eines VPN-Tunnels lesen Sie [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

Zum Einrichten eines OpenVPN-Servers lesen Sie [OpenVPN Server](../../interface_guide/openvpn_server.md).

Zum Einrichten eines WireGuard-Servers lesen Sie [WireGuard Server](../../interface_guide/wireguard_server.md).

## Netzwerk

=== "Multi-WAN"

    Multi-WAN ermöglicht mehrere gleichzeitige Internetverbindungen, z. B. Cellular, Repeater und Ethernet. Fällt die aktuelle Verbindung aus, wechselt der Router automatisch zu einer anderen Verbindung.

    Weitere Informationen finden Sie unter [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN bezeichnet das lokale Netzwerk, dem Ihr Gerät beitritt, wenn es mit dem Main Wi-Fi oder per Ethernet verbunden ist. Die LAN-Seite enthält Basic Settings, DHCP Server Settings und Address Reservation.

    Weitere Informationen finden Sie unter [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Guest Network erstellt ein separates Wi-Fi-Netzwerk für Besucher. Es ist vom Hauptnetzwerk isoliert und kann mit einem Gast-Subnetz aus privaten IPv4-Bereichen wie `192.168.0.0/16`, `172.16.0.0/12` oder `10.0.0.0/8` konfiguriert werden.

    Weitere Informationen finden Sie unter [Guest Network](../../interface_guide/guest_network.md).

=== "IoT Network"

    IoT Network erstellt ein separates Wi-Fi-Netzwerk für IoT-Geräte und verbessert Kompatibilität und Sicherheit durch Trennung vom Hauptnetzwerk.

    Weitere Informationen finden Sie unter [IoT Network](../../interface_guide/iot_network.md).

<br>

=== "DNS"

    DNS-Einstellungen steuern, wie Domainnamen in IP-Adressen übersetzt werden. Sie können automatisch bezogene DNS-Server verwenden, eigene Server festlegen und DNS-Prioritäten konfigurieren.

    Weitere Informationen finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Ethernet Port dient zum Verwalten der Portrollen WAN/LAN und zum Anzeigen von Portdetails wie MAC-Adresse und ausgehandelter Geschwindigkeit.

    Weitere Informationen finden Sie unter [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6 ist die aktuelle Version des Internetprotokolls und bietet einen wesentlich größeren Adressraum als IPv4.

    Weitere Informationen finden Sie unter [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP Snooping ist eine Optimierung für Ethernet-Switches zur Verwaltung und Steuerung von Multicast-Datenverkehr.

    Weitere Informationen finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

<br>

=== "Network Mode"

    Network Mode legt fest, wie ein Gerät eine Netzwerkverbindung herstellt und mit anderen Geräten kommuniziert.

    Informationen zur Einrichtung finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert Ihren Hauptrouter um Funktionen wie AdGuard Home, verschlüsseltes DNS und VPN.

    Informationen zur Einrichtung finden Sie unter [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Network Acceleration kann die CPU-Last reduzieren und die Paketweiterleitung beschleunigen.

    Informationen zur Einrichtung finden Sie unter [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) analysiert Paketnutzdaten und kann Anwendungen und Websites anhand von Signaturdatenbanken genauer erkennen. Die GL.iNet DPI-Funktion ist in [Netify](https://www.netify.ai/){target="_blank"} integriert.

    Weitere Informationen finden Sie unter [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics kategorisiert und visualisiert die Netzwerknutzung nach Anwendungen, damit Sie aktuellen und historischen Datenverkehr überwachen können.

    Weitere Informationen finden Sie unter [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter nutzt DPI-basierte Klassifizierung, um schädliche oder bösartige Websites automatisch zu blockieren.

    Weitere Informationen finden Sie unter [Content Filter](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS priorisiert wichtige Aktivitäten wie Videoanrufe oder Gaming bei Netzwerküberlastung. Dies gilt für lokalen Client-Datenverkehr und VPN-Client-Tunnelverkehr, nicht für Datenverkehr, den der Router als VPN-Server empfängt.

    Weitere Informationen finden Sie unter [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) verwaltet den Netzwerkdatenverkehr, um Latenz und Bufferbloat zu reduzieren.

    Weitere Informationen finden Sie unter [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control hilft beim Verwalten der Geräte Ihrer Kinder, einschließlich Bildschirmzeitbegrenzung und Inhaltsbeschränkungen.

    Weitere Informationen finden Sie unter [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Sicherheit

=== "Port forwarding"

    Port forwarding ermöglicht entfernten Servern und Geräten im Internet den Zugriff auf Geräte in einem privaten Netzwerk.

    Weitere Informationen finden Sie unter [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL (Access Control List) erstellt Regeln zur Steuerung des Netzwerkzugriffs anhand von Protokollen, Geräteadressen und Ports. Bei Regelkonflikten gilt die Regel mit der höheren Priorität.

    Weitere Informationen finden Sie unter [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access enthält Sicherheitseinstellungen zum Schutz von Netzwerk und Router vor unbefugtem Zugriff, einschließlich Access Control, Remote Access Control und Open Ports on Router.

    Weitere Informationen finden Sie unter [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    NAT Mode ermöglicht das Aktivieren oder Deaktivieren von Full Cone NAT und SIP ALG.

    Weitere Informationen finden Sie unter [NAT Mode](../../interface_guide/nat_settings.md).

## Anwendungen

=== "Plug-ins"

    Plug-ins sind Softwarekomponenten, die einem bestehenden System zusätzliche Funktionen hinzufügen.

    Weitere Informationen finden Sie unter [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert die mit einer Domain verknüpfte IP-Adresse automatisch in Echtzeit.

    Weitere Informationen finden Sie unter [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage stellt zentralen Speicher bereit, auf den mehrere Benutzer und Geräte über das Netzwerk zugreifen können.

    Weitere Informationen finden Sie unter [Network Storage](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern und filtert unerwünschte Inhalte über DNS.

    Weitere Informationen finden Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} kann helfen, die digitale Umgebung Ihres Kindes zu schützen. Im Rahmen der Partnerschaft von GL.iNet mit Bark bietet Fortify (GL-MT6000) den Bark Home Plan kostenlos an.

    Weitere Informationen finden Sie unter [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale macht eigene Geräte und Anwendungen weltweit sicher erreichbar. Fortify (GL-MT6000) kann einem Tailscale-virtuellen Netzwerk beitreten, sodass Sie remote auf WAN- und LAN-Ressourcen zugreifen können.

    Weitere Informationen finden Sie unter [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier erstellt sichere virtuelle Netzwerke über das Internet und verbindet Geräte so, als befänden sie sich im selben lokalen Netzwerk.

    Weitere Informationen finden Sie unter [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor ist freie Open-Source-Software für anonyme Kommunikation und unterstützt privateres Surfen.

    Weitere Informationen finden Sie unter [Tor](../../interface_guide/tor.md).

## System

=== "Overview"

    Overview zeigt den aktuellen Status und Leistungsdaten des Routers, darunter CPU Average Load, Memory Usage, LED Control, Flash Usage, Device Info und External Storage.

    Weitere Informationen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Admin Password dient zum Festlegen oder Ändern des Passworts für die Administrationsoberfläche des Routers.

    Weitere Informationen finden Sie unter [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    Upgrade dient zum Aktualisieren der Router-Firmware. Es unterstützt Firmware Online Upgrade und Firmware Local Upgrade.

    Weitere Informationen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Scheduled Tasks automatisiert Routerfunktionen nach Zeitplan, darunter LED Display Schedule, Schedule Reboot und 5GHz / 2.4GHz Wi-Fi Status Schedule.

    Weitere Informationen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

<br>

=== "Time Zone"

    Time Zone legt die korrekte Zeitzone fest, damit geplante Aufgaben, Protokolle und Systemereignisse korrekt zeitgestempelt werden.

    Weitere Informationen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Reset Firmware setzt die aktuell installierte Firmware auf die Standardeinstellungen zurück und löscht benutzerdefinierte Konfigurationen.

    Weitere Informationen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Log bietet Zugriff auf System Log, Kernel Log, Crash Log, Cloud Log und Nginx Log. Über Export Log können die gesammelten Protokolle für die technische Analyse exportiert werden.

    Weitere Informationen finden Sie unter [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Advanced Settings öffnet die OpenWrt LuCI-Oberfläche für erweiterte Konfigurationen.

    Weitere Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
