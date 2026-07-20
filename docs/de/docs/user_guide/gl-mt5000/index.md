# Brume 3 (GL-MT5000) Benutzerhandbuch

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

Brume 3 (GL-MT5000) ist ein leistungsstarkes Security Gateway mit OpenWrt v21.02. Es ist mit einer MediaTek Quad-Core-Cortex-A53-CPU, 1 GB RAM und 8 GB eMMC-Speicher für die Erweiterung per Plug-ins ausgestattet. Dank seines kompakten Designs eignet es sich ideal für Installationen mit begrenztem Platzangebot und unterstützt VPN-Hosting zu Hause, Site-to-Site-SD-WAN sowie mehr als 30 VPN-Dienste für sichere standortübergreifende Verbindungen. Darüber hinaus verfügt es über die DPI-Funktion von GL.iNet sowie Kindersicherung und AdGuard Home und deckt damit die unterschiedlichen Anforderungen von Technikbegeisterten und Geschäftsanwendern ab.

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## Lieferumfang

- 1 x Brume 3 (GL-MT5000)
- 1 x Netzadapter
- 1 x Ethernet-Kabel
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 1 x Adapter (abhängig von Ihrem Zielland)

Sehen Sie sich unten das Unboxing-Video von Brume 3 an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## So richten Sie Brume 3 ein

Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Einschalten

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an Ihren Brume 3 an und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Gerät verbinden

Verbinden Sie ein kabelgebundenes Gerät, z. B. einen Computer oder Laptop, per Ethernet-Kabel mit dem LAN-Port des Brume 3.

### 3. Im Web-Admin-Panel anmelden

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren.

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie Ihre Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie anschließend auf **Apply**.

### 4. Internet einrichten

Richten Sie Brume 3 mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Tethering und Cellular (optional). Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Verbinden Sie den WAN-Port des Brume 3 per Ethernet-Kabel mit einem vorgelagerten Gerät, beispielsweise einem Modem.

    Sobald Brume 3 erfolgreich mit dem Internet verbunden ist, erscheint auf der Seite INTERNET des Web-Admin-Panels neben "Ethernet" ein grüner Punkt und die physische LED des Brume 3 leuchtet dauerhaft weiß.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät über ein USB-3.0-Datenkabel mit dem USB-Type-C-Port des Brume 3.
    2. Aktivieren Sie in den Einstellungen Ihres Mobilgeräts USB-Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Abschnitt "Tethering" auf **Connect**.

    Sobald Brume 3 erfolgreich mit dem Internet verbunden ist, erscheint auf der Seite INTERNET des Web-Admin-Panels neben "Tethering" ein grüner Punkt und die physische LED des Brume 3 leuchtet dauerhaft weiß.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    Für diese Verbindungsmethode wird zusätzlich ein Adapterkabel von USB-C auf USB-A benötigt.

    Schließen Sie ein Mobilfunk-USB-Modem über ein zusätzliches USB-C-auf-USB-A-Adapterkabel an den USB-Type-C-Port des Brume 3 an. Dies ist nützlich, um die Internetverbindung eines USB-Modems mit allen verbundenen Client-Geräten zu teilen.

    Sobald Brume 3 erfolgreich mit dem Internet verbunden ist, erscheint auf der Seite INTERNET des Web-Admin-Panels neben "Cellular" ein grüner Punkt und die physische LED des Brume 3 leuchtet dauerhaft weiß.

    Detaillierte Anweisungen finden Sie unter [Über Mobilfunk eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

---

Im Folgenden finden Sie einen Überblick über die Funktionen im Web-Admin-Panel von Brume 3.

## Clients

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Name, IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie den Client blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    Der Cloud-Management-Dienst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} von GL.iNet bietet eine einfache und unkomplizierte Möglichkeit, per Fernzugriff auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Informationen zur Einrichtung finden Sie unter [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Fernvernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt eine umfassende Geräteverwaltung über ganze Netzwerke hinweg, einschließlich der Steuerung über- und untergeordneter Geräte. Mit seinem Fokus auf netzweite Verwaltung und künftiger Unterstützung für hardwarebasierte Steuerung bietet AstroWarp eine robuste und zuverlässige Lösung für Gerätemanagement sowie den Betrieb sicherer und stabiler Netzwerke.

    Informationen zur Einrichtung finden Sie unter [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Brume 3 unterstützt OpenVPN und WireGuard.

=== "OpenVPN"

    Brume 3 und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 3 und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

## Netzwerk

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen, z. B. Cellular, Repeater und Ethernet, einrichten können. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang reibungslos und unterbrechungsfrei.

    Informationen zur Einrichtung finden Sie unter [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, kurz für Local Area Network, ist ein Netzwerk, das Computer und Geräte innerhalb eines begrenzten geografischen Bereichs wie eines Hauses oder Büros verbindet. Es ermöglicht Hochgeschwindigkeits-Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Informationen zur Einrichtung finden Sie unter [LAN](../../interface_guide/lan.md).

=== "DNS"

    Auf der DNS-Seite können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren, die DNS-Einstellungen aller Clients überschreiben, benutzerdefiniertes DNS das VPN-DNS überschreiben lassen und den Modus für die DNS-Servereinstellungen auf automatisch setzen oder DNS-Server aus der Ethernet-Verbindung manuell angeben.

    Informationen zur Einrichtung finden Sie unter [DNS](../../interface_guide/dns.md).

---

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie die WAN- und LAN-Ports konfigurieren, die WAN/LAN-Schnittstelle auf Ethernet festlegen, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle angeben sowie die ausgehandelte Portgeschwindigkeit anzeigen.

    Informationen zur Verwaltung finden Sie unter [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, auch Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es stellt einen deutlich größeren Adressraum bereit, sodass nahezu unbegrenzt viele eindeutige IP-Adressen verfügbar sind, was für die wachsende Zahl internetverbundener Geräte entscheidend ist.

    Informationen zur Einrichtung finden Sie unter [IPv6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches verwendet wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Informationen zur Einrichtung finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Network Mode bezeichnet die Konfigurationseinstellungen, die bestimmen, wie ein Gerät eine Verbindung zu einem Netzwerk herstellt und mit anderen Geräten kommuniziert.

    Informationen zur Einrichtung finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in Gateway erweitert die Funktionen Ihres Hauptrouters um Features wie AdGuard Home, verschlüsseltes DNS und VPN-Client.

    Informationen zur Einrichtung finden Sie unter diesen Links:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Drop-in Gateway einrichten](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Netzwerkbeschleunigung"

    Netzwerkbeschleunigung kann die CPU-Last reduzieren und die Weiterleitung von Datenpaketen beschleunigen.

    Informationen zur Einrichtung finden Sie unter [Network Acceleration](../../interface_guide/network_acceleration.md).

## Durchflusskontrolle

=== "DPI Engine"

    DPI (Deep Packet Inspection) ist eine Kernfunktion des intelligenten Netzwerkmanagements. Sie überwindet die Einschränkungen herkömmlicher Router, die nur Quell- oder Zieladressen erkennen, analysiert Nutzdatenpakete eingehend und identifiziert über den Vergleich mit Signaturdatenbanken präzise die vom Benutzer aufgerufenen Anwendungen und Websites. Dadurch wird eine feinere Klassifizierung und Steuerung des Datenverkehrs möglich.

    In Verbindung mit [Netify](https://www.netify.ai/){target="_blank"} verwendet die DPI-Funktion von GL.iNet ein leichtgewichtiges eingebettetes Plug-in für eine effiziente Bereitstellung. Mit der online aktualisierten Signaturdatenbank von Netify wird ein zuverlässiges Management ermöglicht, wodurch die Netzwerkkontrolle präziser und effizienter wird.

    Weitere Informationen finden Sie unter [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics bietet ein intelligentes Dashboard zur Analyse des Datenverkehrs, das die Netzwerknutzung nach Anwendungen kategorisiert und visualisiert. So können Sie Echtzeit- und Verlaufsdaten besser überwachen und Ihr Netzwerk gezielter kontrollieren.

    Detaillierte Anweisungen finden Sie unter [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter bietet intelligente Online-Sicherheit auf Basis DPI-gestützter Klassifizierung und blockiert automatisch schädliche oder bösartige Websites, damit Ihr Netzwerk sauber und sicher bleibt.

    Detaillierte Anweisungen finden Sie unter [Content Filter](../../interface_guide/content_filter.md).

---

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu kontrollieren. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Informationen zur Einrichtung finden Sie unter [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optimiert die Bandbreitenzuweisung, indem kritische Aktivitäten wie Videoanrufe oder Gaming bei Netzwerkauslastung priorisiert werden. Dadurch werden Latenzen reduziert und die Gesamtleistung des Netzwerks verbessert. Beachten Sie, dass dies für lokalen Client-Datenverkehr und VPN-Client-Tunnelverkehr gilt, nicht jedoch für Datenverkehr, den der Router als VPN-Server empfängt.

    Detaillierte Anweisungen finden Sie unter [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) verwaltet den Netzwerkverkehr Ihres Routers intelligent, um Latenzen und "Bufferbloat" zu minimieren und dadurch flüssigeres Gaming sowie bessere Sprachanrufe zu ermöglichen.

    Detaillierte Anweisungen finden Sie unter [SQM](../../interface_guide/sqm.md).

## Sicherheit

=== "Port Forwarding"

    Portweiterleitung ermöglicht es entfernten Servern und Geräten im Internet, auf Geräte in einem privaten Netzwerk zuzugreifen.

    Informationen zur Einrichtung finden Sie unter [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Mit Management Control können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite enthält die folgenden Optionen:

    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten in Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche von entfernten Standorten über das Internet, um die Sicherheit gegen externe Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports am Router geöffnet sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch verbundene Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "NAT Mode"

    Auf der Seite NAT Mode können Sie die Funktionen Full Cone NAT und SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Informationen zur Einrichtung finden Sie unter [NAT Mode](../../interface_guide/nat_settings.md).

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen oder Erweiterungen hinzufügt und so eine Anpassung und Erweiterung seiner Möglichkeiten erlaubt.

    Informationen zur Einrichtung finden Sie unter [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert die mit einer Domain verknüpfte IP-Adresse automatisch in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.

    Informationen zur Einrichtung finden Sie unter [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, über die mehrere Benutzer und Geräte über ein Netzwerk auf Dateien zugreifen und sie gemeinsam nutzen können.

    Informationen zur Einrichtung finden Sie unter [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern, die als DNS-Server fungiert und unerwünschte Inhalte auf allen mit dem Heimnetzwerk verbundenen Geräten filtert.

    Informationen zur Einrichtung finden Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier ist eine softwaredefinierte Netzwerklösung, mit der Benutzer sichere, virtuelle Netzwerke über das Internet erstellen können, sodass Geräte so verbunden werden, als befänden sie sich im selben lokalen Netzwerk.

    Informationen zur Einrichtung finden Sie unter [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können.

    Informationen zur Einrichtung finden Sie unter [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Datenschutz ausgelegtes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Der Internetverkehr wird über eine Reihe freiwillig betriebener Server (Knoten) geleitet, um Standort und Nutzung des Benutzers zu verschleiern und Online-Aktivitäten schwerer nachverfolgbar zu machen.

    * [So richten Sie Tor ein](../../interface_guide/tor.md)

## System

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der CPU Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um Ressourcen besser verwalten zu können.
    * LED Control: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die optischen Anzeigen des Geräts anzupassen.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, um sicherzustellen, dass genügend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * Device Info: Rufen Sie detaillierte Systeminformationen zu Ihrem Router ab, darunter Laufzeit, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Seriennummer.
    * External Storage: Prüfen Sie den Status externer Speichergeräte, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.

    Diese Funktionen bieten wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche des Routers festlegen oder ändern, damit nur autorisierte Benutzer Einstellungen ändern können.

    Aus Sicherheitsgründen empfehlen wir, **Prevent Weak Password** zu aktivieren.

    Wenn **Prevent Weak Password** aktiviert ist, gelten für neue Passwörter die folgenden Anforderungen.

    * Mindestens 5 und höchstens 63 Zeichen.
    * Buchstaben (Groß- und Kleinschreibung wird unterschieden), Zahlen und die Symbole `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sind zulässig.
    * Mindestens zwei der folgenden Kategorien sind erforderlich: Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole.

=== "Upgrade"

    Die Seite Upgrade dient dazu, die Firmware Ihres Routers auf die neueste Version zu aktualisieren und so bessere Leistung, höhere Sicherheit und neue Funktionen bereitzustellen. Diese Seite bietet zwei Upgrade-Optionen:

    * Firmware Online Upgrade: Prüft automatisch auf die neueste Firmware-Version und installiert sie direkt vom Server des Herstellers, was den Aktualisierungsprozess vereinfacht.
    * Firmware Local Upgrade: Lädt eine Firmware-Datei manuell von Ihrem Computer hoch, damit Sie Version und Zeitpunkt des Upgrades selbst steuern können.

    Mit diesen Optionen halten Sie Ihren Router mit den neuesten Verbesserungen und Fehlerbehebungen auf dem aktuellen Stand.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Die Seite Scheduled Tasks ermöglicht es Ihnen, verschiedene Routerfunktionen auf Basis eines vordefinierten Zeitplans zu automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten die Lichtbelastung zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie den Router so, dass er in festgelegten Intervallen automatisch neu startet, um optimale Leistung und Stabilität zu erhalten.

    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers und helfen dabei, ihn an Ihre Anforderungen und Vorlieben anzupassen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle geplanten Aufgaben, Protokolle und Systemereignisse mit Ihrer lokalen Zeit korrekt zeitgestempelt werden. Diese Einstellung ist entscheidend für präzise Aufzeichnungen und die ordnungsgemäße Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Die Seite Log bietet Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und bei der Fehlerbehebung sowie der Leistungsüberwachung helfen. Diese Seite enthält:

    * System Log: Detaillierte Protokolle von Systemereignissen und Aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, nützlich zur Diagnose kritischer Probleme.
    * Cloud Log: Protokolle von Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern er vom Router verwendet wird, mit Details zum Webverkehr und Serverbetrieb.

    Zusätzlich verfügt die Seite über eine Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Log](../../interface_guide/log.md).

---

=== "Reset Firmware"

    Die Seite Reset Firmware ermöglicht es Ihnen, die aktuell installierte Firmware-Version Ihres Routers auf die Standardeinstellungen zurückzusetzen, wobei alle benutzerdefinierten Konfigurationen gelöscht werden. Dadurch wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Dies kann bei der Fehlerbehebung hartnäckiger Probleme hilfreich sein oder wenn Sie mit der Standardkonfiguration der aktuellen Firmware neu beginnen möchten.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche, sodass erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen können. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
