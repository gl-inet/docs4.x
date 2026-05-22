# Marble (GL-B3000) Benutzerhandbuch

## Produktübersicht

Der Router Marble (GL-B3000) ist ein eigenständiges Designobjekt und kann geschickt als Bilderrahmen genutzt werden, um Ihr Lieblingsmotiv zu präsentieren und Ihren Wohnraum aufzuwerten. Marble (GL-B3000) ist nicht nur optisch ansprechend, sondern bietet dank Wi-Fi 6 und Unterstützung für VPN-Funktionen auch erstklassige Leistung.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Lieferumfang

- 1 x Marble (GL-B3000)
- 1 x Benutzerhandbuch
- 1 x Dankeskarte
- 1 x Ethernet-Kabel
- 1 x Wandmontageset
- 1 x Klebepad
- 1 x Routerständer
- 1 x Bilderrahmen (optional)
- 1 x Netzadapter
- 1 x Adapter (abhängig von Ihrem Zielland)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## So richten Sie Marble ein

Sehen Sie sich diese Installations- und Einrichtungsvideos an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Einschalten

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an Ihren Router an und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Gerät verbinden

Verbinden Sie ein Gerät, z. B. einen Computer, Laptop oder ein Smartphone, per Wi-Fi oder Ethernet-Kabel mit dem Router.

- Ethernet

  Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

  Öffnen Sie auf Ihrem Gerät Einstellungen -> WLAN, suchen Sie in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett Ihres Routers.

### 3. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie Ihre Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie anschließend auf **Apply**.

### 4. Internet einrichten

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Marble mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet oder Repeater. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte zwei Internetverbindungen ein.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}

    Verbinden Sie den WAN-Port Ihres Routers per Ethernet-Kabel mit einem vorgelagerten Gerät, z. B. einem Modem.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Netzwerkpasswort ein und klicken Sie dann auf **Apply**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

---

## So richten Sie ein VPN ein

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Marble und andere GL.iNet-Router unterstützen OpenVPN, WireGuard und zusätzlich auch Tor.

=== "OpenVPN"

    Marble und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor ist ein auf Privatsphäre ausgerichteter Dienst, mit dem Sie anonym auf das Internet zugreifen können. Folgen Sie zum Einrichten von Tor dieser Anleitung:

    * [So richten Sie Tor ein](../../interface_guide/tor.md)

---

## WLAN und Clients

=== "Wireless"

    Auf der Seite Wireless können Sie Einstellungen für die 5-GHz- und 2.4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren oder Deaktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Definieren des Wi-Fi-Namens (SSID), das Aktivieren oder Deaktivieren randomisierter BSSID, die Auswahl des Wi-Fi-Sicherheitsmodus, das Festlegen des Wi-Fi-Passworts sowie die Konfiguration von SSID-Sichtbarkeit, Wi-Fi-Modus, Bandbreite und Kanal.

    Zum Einrichten von Wireless lesen Sie bitte [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client sehen Sie den Gerätenamen, den Verbindungstyp (also per Ethernet oder Wi-Fi), IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten, das gesamte Datenvolumen sowie die Möglichkeit, den Client zu blockieren oder weitere Aktionen auszuführen.

    Zum Einrichten von Clients lesen Sie bitte [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    Der Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Diese Funktion ist ab Firmware v4.7 verfügbar.

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Remote-Vernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt ein umfassendes Gerätemanagement über ganze Netzwerke hinweg, einschließlich der Verwaltung über- und untergeordneter Geräte. Mit seinem Fokus auf netzwerkweites Management und zukünftiger Unterstützung für Hardware-Steuerung bietet AstroWarp eine robuste und verlässliche Lösung für die Geräteverwaltung sowie für sichere und stabile Netzwerke.

## Anwendungen

=== "Plug-ins"

    Plug-ins sind Zusatzfunktionen, die den Funktionsumfang Ihres Routers erweitern. Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen. Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home ist ein Drittanbieter-Tool, das Werbung und Tracking blockiert, um Sie besser zu schützen.

    Informationen zum Aktivieren von AdGuard Home finden Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control ist eine Gruppe von Einstellungen, mit denen Sie die Geräte Ihrer Kinder verwalten und steuern können. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte. Marble bietet zwei Optionen für Parental Control: die lokal von GL.iNet entwickelte Version und die integrierte Version von Bark, einer App für Kindersicherung.

    Zum Einrichten von Parental Control lesen Sie bitte [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können. Zum Einrichten von Tailscale lesen Sie bitte [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier ist ein VPN-Dienst, mit dem Sie Ihre Geräte mit einem virtuellen Netzwerk verbinden können. Zum Einrichten von ZeroTier lesen Sie bitte [ZeroTier](../../interface_guide/zerotier.md).

---

## Netzwerkeinstellungen

=== "Firewall"

    Die Seite Firewall bietet wichtige Sicherheitsfunktionen für Ihr Netzwerk. Sie enthält Funktionen wie Port Forwarding, Open Ports und DMZ. Mit diesen Werkzeugen können Sie den Datenverkehr Ihres Netzwerks steuern, anpassen und seine Sicherheit erhöhen.

    * Port Forwarding: Leiten Sie bestimmten Datenverkehr aus dem Internet an festgelegte Geräte in Ihrem Netzwerk weiter, um den Zugriff auf Dienste wie Spieleserver oder Webserver zu ermöglichen.
    * Open Ports: Überwachen und steuern Sie, welche Ports auf Ihrem Router offen sind, um unbefugten Zugriff und potenzielle Sicherheitsbedrohungen zu vermeiden.
    * DMZ (Demilitarized Zone): Platzieren Sie ein Gerät außerhalb der Haupt-Firewall, damit es uneingeschränkt auf das Internet zugreifen kann, während der Rest Ihres Netzwerks weiterhin geschützt bleibt.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen, z. B. Cellular, Repeater und Ethernet, konfigurieren können. Fällt Ihre aktuelle Internetverbindung aus, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt Ihr Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Auf der Seite LAN können Sie die Einstellungen des lokalen Netzwerks Ihres Routers verwalten und konfigurieren. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Router IP Address: Ändern Sie die IP-Adresse Ihres Routers, damit sie besser zu Ihrer Netzwerkkonfiguration passt.
    * Netmask: Legen Sie die Subnetzmaske Ihres Netzwerks fest, die Größe und Adressbereich des Netzwerks bestimmt.
    * DHCP: Aktivieren oder konfigurieren Sie das Dynamic Host Configuration Protocol, das Geräten in Ihrem Netzwerk automatisch IP-Adressen zuweist.
    * Address Reservation: Reservieren Sie bestimmte IP-Adressen für einzelne Geräte, damit diese vom DHCP-Server immer dieselbe IP-Adresse erhalten.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [LAN](../../interface_guide/lan.md).

---

=== "Gastnetzwerk"

    Auf der Seite Guest Network können Sie ein separates Netzwerk für Ihre Gäste erstellen und verwalten. So erhalten diese Internetzugang, während Ihr Hauptnetzwerk geschützt bleibt. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Gateway: Legen Sie einen bestimmten IP-Adressbereich für das Gastnetzwerk fest, um es von Ihrem Hauptnetzwerk zu unterscheiden.
    * DHCP: Konfigurieren Sie das Dynamic Host Configuration Protocol für das Gastnetzwerk, damit verbundenen Geräten automatisch IP-Adressen zugewiesen werden.

    Diese Funktionen stellen sicher, dass Ihre Gäste das Internet nutzen können, ohne die Sicherheit und Leistung Ihres Hauptnetzwerks zu beeinträchtigen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Die Seite DNS bietet Optionen zum Anpassen der Domain-Name-System-Einstellungen Ihres Routers und verbessert sowohl Sicherheit als auch Leistung. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Encrypted DNS: Konfigurieren Sie verschlüsseltes DNS, um Ihre Browserdaten vor Überwachung oder Manipulation zu schützen und so Privatsphäre und Sicherheit zu gewährleisten.
    * Manual DNS: Legen Sie DNS-Server Ihrer Wahl manuell fest, um DNS-Abfragen gezielt zu steuern und möglicherweise schnellere Auflösungszeiten zu erreichen.
    * DNS Proxy: Aktivieren Sie DNS Proxy, um DNS-Anfragen Ihrer Geräte über einen bestimmten DNS-Server zu leiten und so eine zusätzliche Kontrolle über den DNS-Datenverkehr zu erhalten.

    Mit diesen Einstellungen können Sie die DNS-Leistung und Sicherheit Ihres Netzwerks an Ihre Anforderungen anpassen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Auf der Seite Network Mode können Sie Ihren Router für verschiedene Betriebsarten konfigurieren, um unterschiedliche Netzwerkanforderungen flexibel abzudecken. Verfügbare Modi sind:

    * Router: Arbeiten Sie als Standardrouter, verwalten Sie den Datenverkehr zwischen lokalem Netzwerk und Internet und nutzen Sie Funktionen wie NAT, Firewall und DHCP.
    * Access Point: Nutzen Sie den Router als Access Point, um Ihr bestehendes kabelgebundenes Netzwerk mit drahtloser Konnektivität zu erweitern, ohne Routing durchzuführen.
    * Extender: Verwenden Sie den Router als Reichweitenverlängerer, um das Signal Ihres bestehenden drahtlosen Netzwerks zu verstärken, größere Bereiche abzudecken und Funklöcher zu vermeiden.
    * WDS (Wireless Distribution System): Ähnlich wie Extender; wählen Sie WDS, wenn Ihr Hauptrouter den WDS-Modus unterstützt.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    Auf der Seite IPv6 können Sie IPv6-Einstellungen für Ihr Netzwerk konfigurieren und Unterstützung für das neueste Internetprotokoll bereitstellen. Auf dieser Seite können Sie IPv6 aktivieren und aus vier verschiedenen Modi wählen, die zu Ihren Netzwerkanforderungen passen:

    * Native: Beziehen Sie eine IPv6-Adresse direkt von Ihrem ISP, um eine einfache und effiziente native IPv6-Konnektivität zu nutzen.
    * Passthrough: Lassen Sie IPv6-Datenverkehr durch den Router zu den Geräten in Ihrem Netzwerk weiterleiten, wobei die Verbindung effektiv durchgereicht wird, ohne dass der Router selbst IPv6-Routing übernimmt.
    * NAT6: Verwenden Sie Network Address Translation für IPv6 (NAT6), um zwischen internen und externen IPv6-Adressen zu übersetzen, ähnlich wie NAT bei IPv4 funktioniert.
    * Static IPv6: Konfigurieren Sie manuell eine statische IPv6-Adresse für Ihren Router, um eine feste Adresse für stabile Konnektivität und einfachere Verwaltung von Netzwerkdiensten bereitzustellen.

    Diese Einstellungen helfen Ihnen, die Vorteile von IPv6 zu nutzen, darunter ein größerer Adressraum, verbesserte Sicherheitsfunktionen und bessere Leistung.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    Auf der Seite MAC Address können Sie die mit Ihrem Router verbundenen Media-Access-Control-(MAC-)Adressen anzeigen und verwalten. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Factory Default: Zeigen Sie die Standard-MAC-Adressen für die Ethernet- und Repeater-Modi des Routers an, um die ursprünglichen Hardware-Einstellungen nachzuvollziehen.
    * Clone: Klonen Sie die MAC-Adresse eines bestimmten Client-Geräts. Dies ist besonders nützlich, wenn der Netzwerkzugang auf bestimmte Geräte beschränkt ist.
    * Manual: Legen Sie manuell eine benutzerdefinierte MAC-Adresse für Ihren Router fest. Zusätzlich können Sie mit der Schaltfläche Random eine zufällige MAC-Adresse erzeugen, was mehr Flexibilität und Privatsphäre bietet.

    Mit diesen Funktionen können Sie die MAC-Adressen Ihres Routers effektiv verwalten und so Kompatibilität und Flexibilität in unterschiedlichen Netzwerkumgebungen sicherstellen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen, die er möglicherweise nicht besitzt, darunter AdGuard Home, verschlüsseltes DNS und VPN. Zum Einrichten von Drop-in Gateway lesen Sie bitte [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    Auf der Seite IGMP Snooping können Sie Einstellungen konfigurieren, die das Multicast-Verkehrsmanagement in Ihrem Netzwerk optimieren. IGMP Snooping überwacht IGMP-Protokollpakete und extrahiert Informationen daraus, um Multicast-Weiterleitungstabellen auf Layer 2 aufzubauen und zu pflegen. So wird sichergestellt, dass Multicast-Gruppendaten nur an Hosts weitergeleitet werden, die der Multicast-Gruppe beigetreten sind, und unerwünschter Multicast-Verkehr andere Hosts nicht erreicht.

    Diese Einstellungen helfen, Netzwerkleistung und Effizienz zu optimieren, insbesondere in Umgebungen mit hohem Multicast-Aufkommen, etwa bei Video-Streaming oder Online-Gaming.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkbeschleunigung"

    Auf der Seite Network Acceleration können Sie Funktionen aktivieren, die die CPU-Last verringern und die Weiterleitung von Datenpaketen beschleunigen, wodurch die allgemeine Netzwerkleistung verbessert wird. Allerdings kann die Aktivierung der Netzwerkbeschleunigung mit bestimmten Funktionen in Konflikt geraten.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT-Einstellungen"

    Auf der Seite NAT Settings können Sie Optionen für Network Address Translation (NAT) konfigurieren, um bestimmte Anwendungen zu optimieren und die Netzwerkleistung zu verbessern. Zu den wichtigsten Einstellungen auf dieser Seite gehören:

    * Enable Full Cone NAT: Full Cone NAT kann verwendet werden, um die Spiel-Latenz zu verringern, indem es einen direkteren und weniger restriktiven Pfad für den Netzwerkverkehr bereitstellt. Allerdings kann aktiviertes Full Cone NAT weniger sicher sein, da externe Hosts einfacher Verbindungen zu internen Geräten initiieren können.
    * Enable SIP ALG: Das Session Initiation Protocol Application Layer Gateway (SIP ALG) kann helfen, Probleme durch mehrere NAT-Instanzen zu mindern, die VoIP-Dienste beeinträchtigen können. In den meisten Fällen ist SIP ALG jedoch nicht vorteilhaft und kann Probleme wie einseitiges Audio, nicht klingelnde Telefone während eines Anrufs, Verbindungsabbrüche oder direkt auf die Mailbox geleitete Anrufe verursachen.

    Mit diesen Einstellungen können Sie das NAT-Verhalten Ihres Routers besser an die Anforderungen Ihres Netzwerks anpassen und dabei Leistungsverbesserungen gegen mögliche Auswirkungen auf Sicherheit und Funktionalität abwägen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [NAT Settings](../../interface_guide/nat_settings.md).

---

## Systemeinstellungen

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungskennzahlen Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche CPU-Auslastung Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um die Ressourcennutzung besser zu verwalten.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers des Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * System Info: Greifen Sie auf detaillierte Informationen zum System Ihres Routers zu, einschließlich Firmware-Version, Uptime und Netzwerkstatus.
    * LED Control: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die visuellen Anzeigen des Geräts anzupassen.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Die Seite Upgrade dient dazu, die Firmware Ihres Routers auf die neueste Version zu aktualisieren, um Leistung, Sicherheit und neue Funktionen bereitzustellen. Diese Seite bietet zwei Upgrade-Optionen:

    * Online Upgrade: Prüfen und installieren Sie automatisch die neueste Firmware-Version direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren und dabei Version und Zeitpunkt des Upgrades selbst zu bestimmen.

    Mit diesen Optionen halten Sie Ihren Router mit den neuesten Verbesserungen und Fehlerbehebungen aktuell.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Router-Funktionen anhand eines vordefinierten Zeitplans automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten Lichtemissionen zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um optimale Leistung und Stabilität zu erhalten.
    * 5GHz Wi-Fi Status Schedule: Erstellen Sie einen Zeitplan, um das 5GHz-Wi-Fi-Band zu bestimmten Zeiten zu aktivieren oder zu deaktivieren und so Netzwerknutzung und Energieeffizienz zu optimieren.
    * 2.4GHz Wi-Fi Status Schedule: Legen Sie einen Zeitplan zur Steuerung des 2.4GHz-Wi-Fi-Bands fest, um Netzwerkverfügbarkeit und Stromverbrauch besser zu verwalten.

    Diese Planungsoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers, damit er Ihren Anforderungen und Vorlieben besser entspricht.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle geplanten Aufgaben, Protokolle und Systemereignisse gemäß Ihrer Ortszeit korrekt mit Zeitstempeln versehen werden. Diese Einstellung ist wichtig für eine präzise Protokollierung und die ordnungsgemäße Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Die Seite Log bietet Zugriff auf verschiedene Protokolle, die Aktivitäten und Ereignisse des Routers aufzeichnen und so bei Fehlersuche und Leistungsüberwachung helfen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle zu Ereignissen und Aktivitäten auf Systemebene.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen über Systemabstürze und Fehler, hilfreich bei der Diagnose kritischer Probleme.
    * Cloud Log: Protokolle über Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, falls dieser auf dem Router verwendet wird, mit Details zu Webverkehr und Serveroperationen.

    Zusätzlich verfügt die Seite über eine Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll bei der Diagnose komplexer Probleme und wenn professionelle Unterstützung erforderlich ist.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Log](../../interface_guide/log.md).

=== "Security"

    Auf der Seite Security können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite umfasst Optionen für:

    * Admin Password: Legen Sie das Passwort für die Administrationsoberfläche des Routers fest oder ändern Sie es, damit nur autorisierte Benutzer Einstellungen ändern können.
    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Router-Oberfläche von Geräten aus Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Router-Oberfläche von entfernten Standorten über das Internet, um die Sicherheit gegenüber externen Bedrohungen zu erhöhen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch die verbundenen Geräte zu schützen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf die Werkseinstellungen zurücksetzen, wobei alle benutzerdefinierten Konfigurationen gelöscht werden. Dieser Vorgang stellt die Standardeinstellungen der derzeit installierten Firmware-Version wieder her. Das kann hilfreich sein, um hartnäckige Probleme zu beheben oder mit einer sauberen Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche. Damit können erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
