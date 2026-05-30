# Flint 2 (GL-MT6000) Benutzerhandbuch

## Produktübersicht

Flint 2 (GL-MT6000) ist ein Wi-Fi-6-Router für Zuhause und Büro, der sich ideal für datenintensive Übertragungen, viele gleichzeitig verbundene Geräte oder Gaming-Umgebungen mit extrem geringer Latenz eignet. Flint 2 bietet besonders schnelle WireGuard-VPN-Geschwindigkeiten von bis zu 900 Mbit/s. Darüber hinaus unterstützt er erweiterte Netzwerkredundanzen wie Multi-WAN, Failover und Lastverteilung, um ein unterbrechungsfreies Netzwerk sicherzustellen.

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## Lieferumfang

- 1 x Flint 2 (GL-MT6000)
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 1 x Ethernet-Kabel
- 1 x Netzadapter
- 1 x Adapter (je nach Versandland)

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

Sehen Sie sich unten das Unboxing-Video von Flint 2 an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## So richten Sie Flint 2 ein

Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Dieses Video verwendet einen anderen GL.iNet-Router zur Demonstration der Einrichtung, die Schritte sind jedoch bei Flint 2 und anderen Routermodellen identisch.)</small>

### 1. Einschalten

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an Ihren Router an und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Gerät verbinden

Verbinden Sie ein Gerät (z. B. Computer, Laptop oder Smartphone) per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

  Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

  Suchen Sie auf Ihrem Gerät in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett des Routers.

### 3. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie Ihre Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie anschließend auf **Apply**.

Beachten Sie beim Bestätigen der Wi‑Fi-Daten: Wenn Sie die Wi‑Fi-Informationen ändern, müssen Sie Ihr Gerät mit den aktualisierten Zugangsdaten erneut mit dem Wi‑Fi des Routers verbinden.

### 4. Internet einrichten

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Flint 2 mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_ethernet.png){class="glboxshadow"}

    Verbinden Sie den WAN-Port Ihres Routers per Ethernet-Kabel mit einem vorgelagerten Gerät, z. B. einem Modem.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_repeater.png){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder USB-Dongle, per USB-Kabel mit dem USB-Port des Routers.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Bereich Tethering auf **Connect**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Tethering-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_cellular.png){class="glboxshadow"}

    Schließen Sie ein Mobilfunk-USB-Modem an den USB-Port des Routers an. Das ist nützlich, um die Internetverbindung eines USB-Modems mit allen verbundenen Geräten zu teilen.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Cellular-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über Cellular eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

---

## So richten Sie ein VPN ein

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Flint 2 und andere GL.iNet-Router unterstützen OpenVPN und WireGuard. Zusätzlich wird Tor unterstützt.

=== "OpenVPN"

    Flint 2 und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2 und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Privatsphäre ausgerichtetes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Es leitet den Internetverkehr über eine Reihe von freiwillig betriebenen Servern (Nodes), um den Standort und die Nutzung des Benutzers zu verschleiern und Online-Aktivitäten nur schwer nachvollziehbar zu machen.

    * [So richten Sie Tor ein](../../interface_guide/tor.md).

## WLAN und Clients

=== "Wireless"

    Auf der Seite Wireless können Sie Einstellungen für die 5-GHz- und 2.4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren oder Deaktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Definieren des Wi-Fi-Namens (SSID), das Aktivieren oder Deaktivieren randomisierter BSSID, die Auswahl des Wi-Fi-Sicherheitsmodus, das Festlegen des Wi-Fi-Passworts sowie die Konfiguration von SSID-Sichtbarkeit, Wi-Fi-Modus, Bandbreite und Kanal.

    Zum Einrichten von Wireless lesen Sie bitte [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client sehen Sie den Gerätenamen, den Verbindungstyp (also über Ethernet oder Wi-Fi), IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten, das gesamte Datenvolumen sowie die Möglichkeit, eine IP zu reservieren, den Client zu blockieren oder weitere Aktionen auszuführen.

    Zum Einrichten von Clients lesen Sie bitte [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    Der Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Remote-Vernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt ein umfassendes Gerätemanagement über ganze Netzwerke hinweg, einschließlich der Verwaltung über- und untergeordneter Geräte. Mit seinem Fokus auf netzwerkweites Management und zukünftiger Unterstützung für Hardware-Steuerung bietet AstroWarp eine robuste und verlässliche Lösung für die Geräteverwaltung sowie für sichere und stabile Netzwerke.

    Zum Einrichten von AstroWarp lesen Sie bitte [AstroWarp](../../interface_guide/astrowarp.md).

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen oder Erweiterungen hinzufügt und so dessen Anpassung und Erweiterung ermöglicht.

    Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.

    Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, die es mehreren Benutzern und Geräten ermöglicht, über ein Netzwerk auf Dateien zuzugreifen und sie gemeinsam zu nutzen.

    Zum Einrichten von Network Storage lesen Sie bitte [Network Storage](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern, die als DNS-Server fungiert, um unerwünschte Inhalte auf allen Geräten eines Heimnetzwerks zu filtern.

    Zum Einrichten von AdGuard Home lesen Sie bitte [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu steuern. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Flint 2 bietet zwei Optionen für Parental Control: die lokale, von GL.iNet entwickelte Version und die integrierte Version von Bark.

    Zum Einrichten von Parental Control lesen Sie bitte [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier ist eine Software-defined-Networking-Lösung, mit der Benutzer sichere virtuelle Netzwerke über das Internet erstellen können, sodass Geräte miteinander verbunden werden, als befänden sie sich im selben lokalen Netzwerk.

    Zum Einrichten von ZeroTier lesen Sie bitte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können.

    Zum Einrichten von Tailscale lesen Sie bitte [Tailscale](../../interface_guide/tailscale.md).

---

## Netzwerkeinstellungen

=== "Portweiterleitung"

    Port forwarding ermöglicht es entfernten Servern und Geräten im Internet, auf Geräte in einem privaten Netzwerk zuzugreifen.

    Zum Einrichten der Portweiterleitung lesen Sie bitte [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen einrichten können, z. B. Cellular, Repeater und Ethernet. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, kurz für Local Area Network, ist ein Netzwerk, das Computer und Geräte in einem begrenzten geografischen Bereich wie einem Zuhause oder Büro verbindet. Es ermöglicht schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Zum Einrichten von LAN lesen Sie bitte [Lan](../../interface_guide/lan.md).

=== "Gastnetzwerk"

    Auf der Seite Guest Network können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, Gateway- und Netmasken-IP-Adressen angeben und Sicherheitseinstellungen wie AP Isolation für das Gastnetzwerk konfigurieren.

    Zum Einrichten des Gastnetzwerks lesen Sie bitte [Lan Tutorial](../../interface_guide/guest_network.md).

---

=== "DNS"

    Auf der Seite DNS können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren und die DNS-Einstellungen aller Clients überschreiben. Außerdem können Sie erlauben, dass benutzerdefiniertes DNS VPN-DNS überschreibt, und den DNS-Servermodus auf automatisch setzen oder DNS-Server der Ethernet-Verbindung manuell angeben.

    Zum Einrichten von DNS lesen Sie bitte [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie die WAN- und LAN-Ports konfigurieren, die WAN/LAN-Schnittstelle auf Ethernet setzen, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle festlegen und die ausgehandelte Portgeschwindigkeit anzeigen.

    Zum Verwalten der Ethernet-Ports lesen Sie bitte [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "Network Mode"

    Der Netzwerkmodus bezeichnet die Konfigurationseinstellungen, die festlegen, wie sich ein Gerät mit einem Netzwerk verbindet und mit anderen Geräten kommuniziert.

    Zum Einrichten des Netzwerkmodus lesen Sie bitte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, kurz für Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen wesentlich größeren Adressraum und damit nahezu unbegrenzt viele eindeutige IP-Adressen, was für die stetig wachsende Zahl internetfähiger Geräte entscheidend ist.

    Zum Einrichten von IPv6 lesen Sie bitte [IPv6](../../interface_guide/network_mode.md).

---

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen, die er möglicherweise nicht bietet, darunter AdGuard Home, verschlüsseltes DNS und VPN.

    Zum Einrichten von Drop-in Gateway lesen Sie bitte [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches eingesetzt wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Zum Einrichten von IGMP Snooping lesen Sie bitte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkbeschleunigung"

    Netzwerkbeschleunigung kann die CPU-Last reduzieren und die Weiterleitung von Datenpaketen beschleunigen.

    Zum Einrichten der Netzwerkbeschleunigung lesen Sie bitte [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT-Einstellungen"

    Auf der Seite NAT Settings können Sie die Funktionen Full Cone NAT und SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Zum Einrichten der NAT-Einstellungen lesen Sie bitte [NAT Settings](../../interface_guide/nat_settings.md).

---

## Systemeinstellungen

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der Router-CPU, um die Leistung zu bewerten und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers aktuell genutzt wird, um Ressourcen besser zu verwalten.
    * LED Control: Schalten Sie die LED-Anzeigen des Routers ein oder aus, um die optischen Signale des Geräts anzupassen.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten verfügbar bleibt.
    * Device Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, darunter Uptime, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Geräte-S/N.
    * External Storage: Prüfen Sie den Status externer Speichergeräte, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Auf der Seite Upgrade können Sie die Firmware Ihres Routers auf die neueste Version aktualisieren, um bessere Leistung, mehr Sicherheit und neue Funktionen zu erhalten. Diese Seite bietet mehrere Upgrade-Optionen:

    * Firmware Online Upgrade: Prüfen Sie automatisch auf die neueste Firmware-Version und installieren Sie sie direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Firmware Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren, und behalten Sie dabei die Kontrolle über Version und Zeitpunkt des Upgrades.

    Mit diesen Optionen halten Sie Ihren Router auf dem neuesten Stand und profitieren von aktuellen Verbesserungen und Fehlerbehebungen.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Routerfunktionen anhand eines festgelegten Zeitplans automatisieren und so Komfort und Effizienz erhöhen. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Anzeigen des Routers automatisch ein- oder auszuschalten und so die Lichtemission zu bestimmten Zeiten zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität aufrechtzuerhalten.
    * 5GHz / 2.4GHz Wi-Fi Status Schedule: Legen Sie einen Zeitplan fest, um das 5GHz-/2.4GHz-Wi-Fi-Band zu steuern und Verfügbarkeit sowie Stromverbrauch besser zu verwalten.

    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers und helfen dabei, ihn an Ihre Anforderungen und Vorlieben anzupassen.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle Zeitpläne, Protokolle und Systemereignisse präzise mit Ihrer Ortszeit versehen werden. Diese Einstellung ist wichtig für genaue Aufzeichnungen und die korrekte Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Auf der Seite Log erhalten Sie Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und so die Fehlerbehebung sowie Leistungsüberwachung unterstützen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle von Systemereignissen und -aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, die bei der Diagnose kritischer Probleme helfen.
    * Cloud Log: Protokolle zu Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern dieser vom Router genutzt wird, mit Informationen zu Webverkehr und Serverbetrieb.

    Zusätzlich verfügt die Seite über die Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders hilfreich bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md).

---

=== "Security"

    Auf der Seite Security können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite enthält Optionen für:

    * Admin Password: Legen Sie das Passwort für die Administrationsoberfläche des Routers fest oder ändern Sie es, damit nur autorisierte Benutzer Einstellungen ändern können.
    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten in Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche aus entfernten Standorten über das Internet, um die Sicherheit vor externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports am Router geöffnet sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch verbundene Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen, wodurch alle benutzerdefinierten Konfigurationen gelöscht werden. Dabei wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Das ist hilfreich, um hartnäckige Probleme zu beheben oder mit der Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Auf der Seite Advanced Settings erhalten erfahrene Benutzer über die OpenWrt-LuCI-Oberfläche Zugriff auf erweiterte Konfigurationsoptionen, um Routereinstellungen und Funktionen über die grundlegenden Oberflächenoptionen hinaus fein abzustimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
