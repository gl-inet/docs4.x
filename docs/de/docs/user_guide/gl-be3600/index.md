# Slate 7 (GL-BE3600) Benutzerhandbuch

## Produktübersicht

Slate 7 (GL-BE3600) ist der erste tragbare Dualband-Wi-Fi-7-Reiserouter von GL.iNet und basiert auf führenden Wi-Fi-7-Technologien wie Multi-Link Operation und 4K QAM. Er erreicht theoretische Dualband-Geschwindigkeiten von 688 Mbit/s (2,4 GHz) und 2882 Mbit/s (5 GHz) und ermöglicht damit nahtloses 8K-Streaming und mobile Gaming-Erlebnisse. Über den Touchscreen können Sie den Netzwerkstatus auf einen Blick prüfen und grundlegende Funktionen intuitiv bedienen.

Ausgestattet mit 2 × 2.5G-Ethernet-Ports (1 WAN + 1 LAN) und 1 × USB-3.0-Port erfüllt der Router die Anforderungen an schnelle kabelgebundene Verbindungen und flexible Speichererweiterung. Er unterstützt außerdem die Stromversorgung über Type-C PD (5V/3A, 9V/3A, 12V/2.5A) und verfügt über ein kompaktes, leichtes Design für hohe Mobilität. Mit vorinstalliertem AdGuard Home und kompatibel mit mehr als 30 VPN-Diensten bietet er zuverlässige Sicherheit für Ihr Netzwerk. Durch die Kombination aus mobilem Komfort und professioneller Leistung ist Slate 7 die ideale Wahl für Remote-Arbeit und die gemeinsame Nutzung von Netzwerken unterwegs.

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## Lieferumfang

- 1 x Slate 7 (GL-BE3600)
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 1 x Ethernet-Kabel
- 1 x Stromkabel
- 1 x US-Netzadapter
- 3 x Steckeradapter (EU-, UK- und AU-Stecker)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Sehen Sie sich unten das Unboxing-Video von Slate 7 an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Touchscreen

| Bildschirmanzeige | Beschreibung |
| :--- | :--- |
| ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){width="400"} | Startvorgang |
| ![network](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){width="400"} | Netzwerkverbindungstypen und -status<br>**Grün**: Aktiv / Verbunden<br>**Gelb**: Verbindung wird hergestellt / Fehler<br>**Weiß**: Inaktive Verbindung |
| ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){width="400"} | Wi-Fi-Details, einschließlich SSID, Passwort, QR-Code und der Ein-/Aus-Schaltfläche |
| ![vpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/vpn_client.png){width="400"} | VPN-Status. Die Ersteinrichtung erfolgt im Web-Admin-Panel |
| ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){width="400"} | AdGuard Home |
| ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){width="400"} | Tor |
| ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){width="400"} | Datenverkehrsstatistiken<br>Dies ist die Durchschnittsgeschwindigkeit des gesamten Datenverkehrs, der durch den Router läuft; sie wird alle 3 Sekunden berechnet |
| ![system usage](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){width="400"} | Systemauslastung |
| ![time zone](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){width="400"} | Zeitzone |
| ![system menu](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){width="400"} | Systemmenü<br>Wischen Sie von oben nach unten, um das Systemmenü zu öffnen |
| ![unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){width="400"} | Tippen Sie auf den Bildschirm, um ihn zu aktivieren, und wischen Sie von links nach rechts, um ihn zu entsperren |
| ![reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){width="400"} | Klicken Sie auf „Reboot“ und wischen Sie dann von links nach rechts, um zu bestätigen |

## So richten Sie Slate 7 ein

Sehen Sie sich dieses Setup-Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In diesem Video demonstrieren wir die Einrichtung, indem wir Slate 7 als Repeater konfigurieren. Wenn Sie Slate 7 mit einer anderen Internetverbindungsmethode einrichten möchten, folgen Sie bitte den untenstehenden Schritten.)</small>

### 1. Einschalten

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an Ihren Router an und stecken Sie ihn in eine Steckdose. Der Router startet automatisch.

### 2. Gerät verbinden

Verbinden Sie ein Gerät, z. B. einen Computer, Laptop oder ein Smartphone, per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Suchen Sie auf Ihrem Gerät in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein, um dem Netzwerk beizutreten. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett Ihres Routers.

### 3. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie eine Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie dann auf **Apply**.

### 4. Internet einrichten

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Slate 7 mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}

    Verbinden Sie den WAN-Port von Slate 7 per Ethernet-Kabel mit einem vorgelagerten Gerät, z. B. einem Modem.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. Suchen Sie auf der INTERNET-Seite des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder einen USB-Dongle, per USB-Kabel mit dem USB-Port des Routers.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der INTERNET-Seite des Web-Admin-Panels im Bereich Tethering auf **Connect**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Tethering-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Schließen Sie ein Cellular-USB-Modem an den USB-Port von Slate 7 an. Das ist nützlich, um die Internetverbindung eines USB-Modems mit allen verbundenen Geräten zu teilen.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Cellular-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über Cellular eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

---

Nachfolgend finden Sie einen Überblick über die Funktionen im Web-Admin-Panel von Slate 7.

## WLAN

Auf der Seite Wireless können Sie Einstellungen für die 5-GHz- und 2.4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Definieren des Wi-Fi-Namens (SSID), das Aktivieren randomisierter BSSID, die Auswahl des Wi-Fi-Sicherheitsmodus und Passworts sowie die Konfiguration von SSID-Sichtbarkeit, Wi-Fi-Modus, Bandbreite und Kanal.

Darüber hinaus unterstützt Slate 7 MLO Wi-Fi, also Multi-Link Operation, bei der mehrere drahtlose Netzwerke gleichzeitig kombiniert werden, um höhere Bandbreite und zuverlässigere Verbindungen zu erreichen.

Informationen zur Einrichtung von Wireless finden Sie unter [Wireless](../../interface_guide/wireless.md).

## Clients

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Name, IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie den Client blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Remote-Vernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt ein umfassendes Gerätemanagement über ganze Netzwerke hinweg, einschließlich der Verwaltung über- und untergeordneter Geräte. Mit seinem Fokus auf netzwerkweites Management und zukünftiger Unterstützung für Hardware-Steuerung bietet AstroWarp eine robuste und verlässliche Lösung für die Geräteverwaltung sowie für sichere und stabile Netzwerke.

    Zum Einrichten von AstroWarp lesen Sie bitte [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Slate 7 unterstützt OpenVPN, WireGuard und Tor.

=== "OpenVPN"

    Slate 7 und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Privatsphäre ausgerichtetes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Es leitet den Internetverkehr über eine Reihe von freiwillig betriebenen Servern (Nodes), um den Standort und die Nutzung des Benutzers zu verschleiern und Online-Aktivitäten nur schwer nachvollziehbar zu machen.

    * [So richten Sie Tor ein](../../interface_guide/tor.md)

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen hinzufügt und so dessen Anpassung und Erweiterung ermöglicht.

    Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.

    Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, die es mehreren Benutzern und Geräten ermöglicht, über ein Netzwerk auf Dateien zuzugreifen und sie gemeinsam zu nutzen.

    Zum Einrichten von Network Storage lesen Sie bitte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern, die als DNS-Server fungiert, um unerwünschte Inhalte auf allen Geräten eines Heimnetzwerks zu filtern.

    Zum Einrichten von AdGuard Home lesen Sie bitte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu steuern. Dazu gehören unter anderem die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Zum Einrichten von Parental Control lesen Sie bitte [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier ist eine Software-defined-Networking-Lösung, mit der Benutzer sichere virtuelle Netzwerke über das Internet erstellen können, sodass Geräte miteinander verbunden werden, als befänden sie sich im selben lokalen Netzwerk.

    Zum Einrichten von ZeroTier lesen Sie bitte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können.

    Zum Einrichten von Tailscale lesen Sie bitte [Tailscale](../../interface_guide/tailscale.md).

## Netzwerk

=== "Portweiterleitung"

    Mit Port Forwarding können entfernte Server und Geräte im Internet auf Geräte in einem privaten Netzwerk zugreifen.

    Zum Einrichten von Port Forwarding lesen Sie bitte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen, z. B. Cellular, Repeater und Ethernet, konfigurieren können. Fällt Ihre aktuelle Internetverbindung aus, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt Ihr Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, also Local Area Network, ist ein Netzwerk, das Computer und Geräte in einem begrenzten geografischen Bereich wie einem Zuhause oder Büro verbindet. Es ermöglicht schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Zum Einrichten von LAN lesen Sie bitte [Lan](../../interface_guide/lan.md).

---

=== "Gastnetzwerk"

    Damit können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, Gateway- und Netmask-IP-Adressen angeben und Sicherheitseinstellungen wie AP-Isolation für das Gastnetzwerk konfigurieren.

    Zum Einrichten des Gastnetzwerks lesen Sie bitte [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Auf der Seite DNS können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren und die DNS-Einstellungen aller Clients überschreiben. Außerdem können Sie zulassen, dass benutzerdefiniertes DNS VPN-DNS überschreibt, und den Modus für die DNS-Server-Einstellungen auf automatisch setzen oder DNS-Server der Ethernet-Verbindung manuell festlegen.

    Zum Einrichten von DNS lesen Sie bitte [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie die WAN- und LAN-Ports konfigurieren, die WAN-/LAN-Schnittstelle auf Ethernet setzen, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle festlegen sowie die ausgehandelte Geschwindigkeit des Netzwerkports anzeigen.

    Zum Verwalten der Ethernet-Ports lesen Sie bitte [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Network Mode bezeichnet die Konfigurationseinstellungen, die bestimmen, wie sich ein Gerät mit einem Netzwerk verbindet und mit anderen Geräten kommuniziert.

    Zum Einrichten des Network Mode lesen Sie bitte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, also Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und als Nachfolger von IPv4 vorgesehen. Es bietet einen deutlich größeren Adressraum und ermöglicht eine nahezu unbegrenzte Anzahl eindeutiger IP-Adressen, was für die wachsende Zahl internetverbundener Geräte entscheidend ist.

    Zum Einrichten von IPv6 lesen Sie bitte [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen wie AdGuard Home, verschlüsseltes DNS und VPN-Client.

    Zum Einrichten von Drop-in Gateway lesen Sie bitte diese Links:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches eingesetzt wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Zum Einrichten von IGMP Snooping lesen Sie bitte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkbeschleunigung"

    Netzwerkbeschleunigung kann die CPU-Last verringern und die Weiterleitung von Datenpaketen beschleunigen.

    Zum Einrichten der Netzwerkbeschleunigung lesen Sie bitte [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT-Einstellungen"

    Auf der Seite NAT Settings können Sie Full Cone NAT und die Funktion SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Zum Einrichten der NAT-Einstellungen lesen Sie bitte [NAT Settings](../../interface_guide/nat_settings.md).

## System

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungskennzahlen Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche CPU-Auslastung Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um die Ressourcennutzung besser zu verwalten.
    * LED Control: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die visuellen Anzeigen des Geräts anzupassen.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers des Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * Device Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, einschließlich Uptime, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Geräte-Seriennummer.
    * External Storage: Prüfen Sie den Status externer Speichergeräte, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Die Seite Upgrade dient dazu, die Firmware Ihres Routers auf die neueste Version zu aktualisieren, um Leistung, Sicherheit und neue Funktionen bereitzustellen. Diese Seite bietet zwei Upgrade-Optionen:

    * Firmware Online Upgrade: Prüfen und installieren Sie automatisch die neueste Firmware-Version direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Firmware Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren und dabei Version und Zeitpunkt des Upgrades selbst zu bestimmen.

    Mit diesen Optionen halten Sie Ihren Router mit den neuesten Verbesserungen und Fehlerbehebungen aktuell.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Router-Funktionen anhand eines vordefinierten Zeitplans automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten Lichtemissionen zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um optimale Leistung und Stabilität zu erhalten.
    * Wi-Fi Status Schedule: Legen Sie einen Zeitplan zur Steuerung des 5GHz-/2.4GHz-/MLO-Wi-Fi-Bands fest, um Netzwerkverfügbarkeit und Stromverbrauch besser zu verwalten.

    Diese Planungsoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers, damit er Ihren Anforderungen und Vorlieben besser entspricht.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Display Management"

    Die Seite Display Management bietet Ihnen umfassende Funktionen zur Verwaltung des Touchscreen-Displays und der zugehörigen Einstellungen.

    - Function Management: Legen Sie fest, welche Funktionen auf dem Touchscreen angezeigt werden, und passen Sie die Anzeige an Ihre Bedürfnisse an.
    - Lock Screen: Passen Sie die Sperrbildschirm-Einstellungen an. Sie können das Hintergrundbild festlegen und das Aktivieren des Displays konfigurieren.
    - Brightness: Passen Sie die Helligkeit des Touchscreens an. Verwenden Sie den Schieberegler oder geben Sie einen bestimmten Wert ein (Bereich von 1 bis 10), um unterschiedliche Lichtverhältnisse abzudecken.
    - Auto Lock: Stellen Sie die Verzögerung ein, nach der sich der Bildschirm bei Inaktivität automatisch sperrt. Der Bereich liegt zwischen 1 und 30 Minuten.
    - Screen Always On: Schalten Sie diese Option um, um festzulegen, ob der Touchscreen dauerhaft eingeschaltet bleibt oder sich nach Inaktivität ausschaltet.
    - Enable Screen Passcode: Fügen Sie eine zusätzliche Sicherheitsebene hinzu, indem Sie einen Passcode für den Touchscreen aktivieren.

    Detaillierte Anweisungen finden Sie unter [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle geplanten Aufgaben, Protokolle und Systemereignisse gemäß Ihrer Ortszeit korrekt mit Zeitstempeln versehen werden. Diese Einstellung ist wichtig für eine präzise Protokollierung und die ordnungsgemäße Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Auf der Seite Toggle Button Settings können Sie den physischen Kippschalter Ihres Routers konfigurieren und ihm bestimmte Funktionen für schnellen Zugriff und einfache Steuerung zuweisen. Diese Funktion bietet praktische Schnellzugriffe für häufige Aufgaben und Einstellungen, verbessert die Benutzererfahrung und vereinfacht die Router-Verwaltung.

    Detaillierte Anweisungen finden Sie unter [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Die Seite Log bietet Zugriff auf verschiedene Protokolle, die Aktivitäten und Ereignisse des Routers aufzeichnen und so bei Fehlersuche und Leistungsüberwachung helfen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle zu Ereignissen und Aktivitäten auf Systemebene.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen über Systemabstürze und Fehler, hilfreich bei der Diagnose kritischer Probleme.
    * Cloud Log: Protokolle über Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, falls dieser auf dem Router verwendet wird, mit Details zu Webverkehr und Serveroperationen.

    Zusätzlich verfügt die Seite über eine Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll bei der Diagnose komplexer Probleme und wenn professionelle Unterstützung erforderlich ist.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md).

=== "Security"

    Auf der Seite Security können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite umfasst Optionen für:

    * Admin Password: Legen Sie das Passwort für die Administrationsoberfläche des Routers fest oder ändern Sie es, damit nur autorisierte Benutzer Einstellungen ändern können.
    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Router-Oberfläche von Geräten aus Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Router-Oberfläche von entfernten Standorten über das Internet, um die Sicherheit gegenüber externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports auf dem Router offen sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch die verbundenen Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf die Werkseinstellungen zurücksetzen, wobei alle benutzerdefinierten Konfigurationen gelöscht werden. Dieser Vorgang stellt die Standardeinstellungen der derzeit installierten Firmware-Version wieder her. Das kann hilfreich sein, um hartnäckige Probleme zu beheben oder mit einer sauberen Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche. Damit können erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
