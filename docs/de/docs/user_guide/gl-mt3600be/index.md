# Beryl 7 (GL-MT3600BE) Benutzerhandbuch

## Produktübersicht

Beryl 7 (GL-MT3600BE) ist ein tragbarer Dualband-Wi-Fi-7-Reiserouter, der speziell für mobile Einsatzszenarien wie Geschäftsreisen und Urlaube entwickelt wurde. Als verbesserte Version des Beryl AX unterstützt er Wi-Fi-7-Technologien wie Multi-Link Operation (MLO) und 4K QAM. Die theoretischen Dualband-Geschwindigkeiten erreichen 688 Mbit/s (2,4 GHz) + 2882 Mbit/s (5 GHz) und decken damit hohe Anforderungen wie 8K-Streaming und mobiles Gaming ab.

Angetrieben von einem MediaTek-Quad-Core-Prozessor und ausgestattet mit 512 MB NAND-Flashspeicher gewährleistet er stabiles Multitasking und die Kompatibilität mit verschiedenen OpenWrt-Plug-ins. Er verfügt über 2 x 2,5G-Ethernet-Ports und 1 x USB-3.0-Port und eignet sich damit sowohl für schnelle kabelgebundene Verbindungen als auch für Speichererweiterungen. Dank PD-Kompatibilität kann er mit einem gewöhnlichen Handy-Ladekabel betrieben werden, wodurch Gewicht und Kabelsalat im Gepäck reduziert werden. Mit Unterstützung für mehr als 120 Geräte gleichzeitig und einem schlanken, tragbaren Design ist er ideal für unterwegs.

![gl-mt3600be interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/hardware_info/mt3600be_interface.png){class="glboxshadow"}

## Lieferumfang

- 1 x Beryl 7 (GL-MT3600BE)
- 1 x Netzadapter
- 1 x Ethernet-Kabel
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 3 x Adapter (EU-, UK- und AU-Stecker)

Sehen Sie sich unten das Unboxing-Video von Beryl 7 an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xZHmP3B8VlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## So richten Sie Beryl 7 ein

Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ey-Z3MEOPpw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Einschalten

Setzen Sie die beiden Teile des Netzadapters zusammen. Schließen Sie ihn an Ihren Router an und stecken Sie ihn in eine Steckdose. Das Gerät startet anschließend automatisch.

### 2. Gerät verbinden

Verbinden Sie Ihren Computer oder Ihr Mobilgerät per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Öffnen Sie auf Ihrem Gerät **Einstellungen** -> **WLAN**, suchen Sie den Wi-Fi-Netzwerknamen des Routers in der Liste der verfügbaren Netzwerke und geben Sie das Passwort ein, um die Verbindung herzustellen. Den standardmäßigen Netzwerknamen und das Passwort finden Sie auf dem Geräteetikett.

### 3. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie eine Sprache aus, legen Sie Ihr Admin-Passwort fest und klicken Sie anschließend auf **Apply**.

### 4. Internet einrichten

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet-Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Ihren Beryl 7 mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_ethernet.png){class="glboxshadow"}

    Verbinden Sie den WAN-Port des Beryl 7 per Ethernet-Kabel mit einem vorgeschalteten Gerät, zum Beispiel einem Modem.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Bereich Ethernet auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Mit einem Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_repeater.png){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Bereich Repeater auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, zum Beispiel ein Smartphone oder einen USB-Dongle, per USB-Kabel mit dem USB-Port des Beryl 7.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Bereich Tethering auf **Connect**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Bereich Tethering auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt3600be/internet/mt3600be_cellular.png){class="glboxshadow"}

    Schließen Sie ein Mobilfunk-USB-Modem an den USB-Port des Beryl 7 an. Das ist nützlich, wenn Sie die Internetverbindung eines USB-Modems mit allen verbundenen Geräten teilen möchten.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Bereich Cellular auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über Mobilfunk eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

---

Im Folgenden finden Sie eine Übersicht über die Funktionen im Web-Admin-Panel des Beryl 7.

## WLAN

Auf der Seite Wireless können Sie Einstellungen für die Wi-Fi-Netzwerke im 5-GHz- und 2,4-GHz-Band konfigurieren. Dazu gehören das Aktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Angeben des Wi-Fi-Namens (SSID), das Aktivieren einer zufälligen BSSID, die Auswahl des Wi-Fi-Sicherheitsmodus und Passworts, die Konfiguration der Sichtbarkeit der SSID sowie die Wahl von Wi-Fi-Modus, Bandbreite und Kanal.

Darüber hinaus unterstützt Beryl 7 MLO-Wi-Fi, also Multi-Link Operation. Dabei werden mehrere drahtlose Netzwerke gleichzeitig kombiniert, um eine höhere Bandbreite und zuverlässigere Verbindungen zu erreichen.

Informationen zur Einrichtung von Wireless finden Sie unter [Wireless](../../interface_guide/wireless.md).

## Clients

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Name, IP- und MAC-Adresse, Download- und Upload-Geschwindigkeit sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie den Client blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, GL.iNet-Router per Fernzugriff zu erreichen und zu verwalten.

    Informationen zur Einrichtung von GoodCloud finden Sie unter [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Fernvernetzung und Remote-Geräteverwaltung. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt eine umfassende Geräteverwaltung über ganze Netzwerke hinweg, einschließlich der Steuerung übergeordneter und untergeordneter Geräte. Mit dem Fokus auf netzwerkweite Verwaltung und künftiger Unterstützung für die Steuerung auf Hardwareebene bietet AstroWarp eine robustere und verlässlichere Lösung für das Gerätemanagement sowie für den Erhalt sicherer, stabiler Netzwerke.

    Informationen zur Einrichtung von AstroWarp finden Sie unter [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (Virtual Private Network) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht den Zugriff auf ein entferntes Netzwerk (VPN-Server). Beryl 7 unterstützt OpenVPN, WireGuard und Tor.

=== "OpenVPN"

    Beryl 7 und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das eine hohe Sicherheit bietet. Folgen Sie zur Einrichtung von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Beryl 7 und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Einrichtung bietet. Folgen Sie zur Einrichtung von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Datenschutz ausgelegtes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Der Internetverkehr wird über eine Reihe freiwillig betriebener Server (Knoten) geleitet, um den Standort und die Nutzung des Benutzers zu verschleiern und Online-Aktivitäten schwerer nachverfolgbar zu machen.

    * [So richten Sie Tor ein](../../interface_guide/tor.md)

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen oder Erweiterungen hinzufügt und so dessen Fähigkeiten anpassbar erweitert.

    Informationen zur Einrichtung von Plug-ins finden Sie unter [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt die mit einer Domain verknüpfte IP-Adresse automatisch und aktualisiert sie in Echtzeit. Das ist nützlich für Benutzer, die eine statische IP-Adresse benötigen, um auf ein entferntes Netzwerk zuzugreifen.

    Informationen zur Einrichtung von Dynamic DNS finden Sie unter [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, über die mehrere Benutzer und Geräte über ein Netzwerk auf Dateien zugreifen und sie gemeinsam nutzen können.

    Informationen zur Einrichtung von Network Storage finden Sie unter [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern. Sie fungiert als DNS-Server, um unerwünschte Inhalte auf allen mit dem Heimnetzwerk verbundenen Geräten zu filtern.

    Informationen zur Einrichtung von AdGuard Home finden Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu kontrollieren. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Informationen zur Einrichtung von Parental Control finden Sie unter [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier ist eine softwaredefinierte Netzwerklösung, mit der Benutzer sichere virtuelle Netzwerke über das Internet erstellen können. Dabei werden Geräte so verbunden, als befänden sie sich im selben lokalen Netzwerk.

    Informationen zur Einrichtung von ZeroTier finden Sie unter [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie überall auf Ihre Geräte und Anwendungen zugreifen können.

    Informationen zur Einrichtung von Tailscale finden Sie unter [Tailscale](../../interface_guide/tailscale.md).

## Netzwerk

=== "Portweiterleitung"

    Mit der Portweiterleitung können entfernte Server und Geräte im Internet auf Geräte in einem privaten Netzwerk zugreifen.

    Informationen zur Einrichtung der Portweiterleitung finden Sie unter [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen einrichten können, zum Beispiel Cellular, Repeater und Ethernet. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang stabil und unterbrechungsfrei.

    Informationen zur Einrichtung von Multi-WAN finden Sie unter [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, also Local Area Network, ist ein Netzwerk, das Computer und Geräte in einem begrenzten geografischen Bereich wie einem Zuhause oder Büro miteinander verbindet. Es ermöglicht eine schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Informationen zur Einrichtung von LAN finden Sie unter [Lan](../../interface_guide/lan.md).

---

=== "Gastnetzwerk"

    Hier können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, die Gateway- und Netzmasken-IP-Adressen angeben und Sicherheitseinstellungen wie AP-Isolation für das Gastnetzwerk konfigurieren.

    Informationen zur Einrichtung des Gastnetzwerks finden Sie unter [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Auf der Seite DNS können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren und die DNS-Einstellungen aller Clients überschreiben. Außerdem können Sie benutzerdefiniertes DNS das VPN-DNS überschreiben lassen und den DNS-Servermodus entweder auf automatisch setzen oder DNS-Server aus der Ethernet-Verbindung manuell angeben.

    Informationen zur Einrichtung von DNS finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie die WAN- und LAN-Ports konfigurieren, die WAN-/LAN-Schnittstelle auf Ethernet festlegen, den MAC-Modus und die MAC-Adresse der WAN-Schnittstelle angeben und die ausgehandelte Portgeschwindigkeit anzeigen.

    Informationen zur Verwaltung der Ethernet-Ports finden Sie unter [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Der Netzwerkmodus bezeichnet die Konfigurationseinstellungen, die festlegen, wie sich ein Gerät mit einem Netzwerk verbindet und mit anderen Geräten kommuniziert.

    Informationen zur Einrichtung des Netzwerkmodus finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, also Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen deutlich größeren Adressraum und damit eine nahezu unbegrenzte Anzahl eindeutiger IP-Adressen, was für die wachsende Zahl internetfähiger Geräte entscheidend ist.

    Informationen zur Einrichtung von IPv6 finden Sie unter [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionen Ihres Hauptrouters, darunter AdGuard Home, verschlüsseltes DNS und VPN-Client.

    Informationen zur Einrichtung von Drop-in Gateway finden Sie unter diesen Links:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches eingesetzt wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Informationen zur Einrichtung von IGMP Snooping finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkbeschleunigung"

    Die Netzwerkbeschleunigung kann die CPU-Last verringern und die Weiterleitung von Datenpaketen beschleunigen.

    Informationen zur Einrichtung der Netzwerkbeschleunigung finden Sie unter [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT-Einstellungen"

    Auf der Seite NAT Settings können Sie die Funktionen Full Cone NAT und SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Informationen zur Einrichtung der NAT-Einstellungen finden Sie unter [NAT Settings](../../interface_guide/nat_settings.md).

## System

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * Durchschnittliche CPU-Auslastung: Überwachen Sie die durchschnittliche Belastung der CPU Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Speicherauslastung: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um Ressourcen besser verwalten zu können.
    * LED-Steuerung: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die optischen Anzeigen des Geräts anzupassen.
    * Flash-Auslastung: Zeigen Sie die Nutzung des Flashspeichers Ihres Routers an, um sicherzustellen, dass genügend Platz für Firmware und Konfigurationsdaten vorhanden ist.
    * Geräteinformationen: Greifen Sie auf detaillierte Informationen über Ihr Routersystem zu, darunter Betriebszeit, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Geräte-S/N.
    * Externer Speicher: Prüfen Sie den Status externer Speichermedien, die mit dem Router verbunden sind, zum Beispiel USB-Laufwerke oder TF-Karten.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Die Seite Upgrade wird verwendet, um die Firmware Ihres Routers auf die neueste Version zu aktualisieren und so Leistung, Sicherheit und Funktionsumfang zu verbessern. Auf dieser Seite stehen zwei Upgrade-Optionen zur Verfügung:

    * Firmware Online Upgrade: Die neueste Firmware-Version wird automatisch auf dem Server des Herstellers gesucht und direkt installiert, was den Aktualisierungsprozess vereinfacht.
    * Firmware Local Upgrade: Laden Sie eine Firmware-Datei manuell von Ihrem Computer hoch, um den Router zu aktualisieren. Dadurch haben Sie Kontrolle über Version und Zeitpunkt des Upgrades.

    Mit diesen Optionen bleibt Ihr Router mit den neuesten Verbesserungen und Fehlerbehebungen auf dem aktuellen Stand.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Routerfunktionen nach einem vordefinierten Zeitplan automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen dieser Seite gehören:

    * Zeitplan für LED-Anzeige: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers zu bestimmten Zeiten automatisch ein- oder auszuschalten und so Lichtbelastung zu reduzieren.
    * Geplanter Neustart: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität aufrechtzuerhalten.
    * Zeitplan für Wi-Fi-Status: Legen Sie einen Zeitplan fest, um das 5-GHz-, 2,4-GHz- oder MLO-Wi-Fi-Band zu steuern und so Netzwerkverfügbarkeit und Stromverbrauch besser zu verwalten.

    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers und helfen dabei, ihn an Ihre Anforderungen und Vorlieben anzupassen.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Time Zone"

    Auf der Seite Time Zone können Sie die richtige Zeitzone für Ihren Router festlegen, sodass alle geplanten Aufgaben, Protokolle und Systemereignisse korrekt mit Ihrer lokalen Zeit versehen werden. Diese Einstellung ist wichtig für präzise Aufzeichnungen und die korrekte Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Toggle Button Settings"

    Auf der Seite Toggle Button Settings können Sie den physischen Kippschalter Ihres Routers konfigurieren und ihm bestimmte Funktionen für den schnellen Zugriff und die direkte Steuerung zuweisen. Diese Funktion bietet praktische Kurzbefehle für häufig verwendete Aufgaben und Einstellungen, verbessert die Benutzererfahrung und vereinfacht die Routerverwaltung.

    Detaillierte Anweisungen finden Sie unter [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Auf der Seite Log erhalten Sie Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und bei der Fehlersuche sowie Leistungsüberwachung helfen. Diese Seite enthält:

    * System Log: Detaillierte Protokolle über Ereignisse und Aktivitäten auf Systemebene.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen über Systemabstürze und Fehler, hilfreich bei der Diagnose kritischer Probleme.
    * Cloud Log: Protokolle über Interaktionen und Aktivitäten im Zusammenhang mit GoodCloud-Diensten, die in den Router integriert sind.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern er vom Router verwendet wird, einschließlich Informationen über Webverkehr und Serverbetrieb.

    Zusätzlich gibt es auf der Seite die Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md).

---

=== "Security"

    Auf der Seite Security können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite enthält Optionen für:

    * Admin Password: Legen Sie das Passwort für die Administrationsoberfläche des Routers fest oder ändern Sie es, damit nur autorisierte Benutzer Einstellungen ändern können.
    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten aus Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche aus entfernten Standorten über das Internet, um die Sicherheit gegenüber externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports auf dem Router geöffnet sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen dabei, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch die verbundenen Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen und dabei alle benutzerdefinierten Konfigurationen löschen. Dabei werden die Standardeinstellungen der derzeit installierten Firmware-Version wiederhergestellt. Das kann nützlich sein, um hartnäckige Probleme zu beheben oder mit der Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche. So können erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
