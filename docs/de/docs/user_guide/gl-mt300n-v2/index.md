# Mango (GL-MT300N-V2) Benutzerhandbuch

## Produktübersicht

Mango (GL-MT300N-V2) ist ein Mini-Router im Taschenformat, der für den mobilen Einsatz und Reisen entwickelt wurde und drahtlose Übertragungsraten von bis zu 300 Mbit/s unterstützt. Mango bietet erweiterte Sicherheitsfunktionen, darunter Unterstützung für OpenVPN, WireGuard® und einen DNS-Server. Sie können damit nicht nur ein öffentliches Netzwerk in ein privates Wi-Fi für sicheres Surfen umwandeln, sondern auch VPN-Konfigurationsdateien von mehr als 30 VPN-Dienstanbietern hochladen und den Router als VPN-Client verwenden, um eine zusätzliche Ebene für Datenschutz und Sicherheit durch verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server bereitzustellen.

![mt300n-v2 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## So richten Sie Mango ein

Um Mango einzurichten, verwenden Sie eine der vier unterstützten Internetverbindungsmethoden: Ethernet, Repeater, Tethering und Cellular. Folgen Sie den untenstehenden Schritten.

### 1. Einschalten

Stecken Sie das Micro-USB-Stromkabel in den Stromanschluss des Routers, verbinden Sie das andere Ende mit einem 5V/2A-Netzadapter (nicht im Lieferumfang enthalten) und stecken Sie ihn in eine Steckdose.

### 2. Gerät verbinden

Verbinden Sie ein Gerät, z. B. einen Computer, Laptop oder ein Smartphone, per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Öffnen Sie auf Ihrem Gerät Einstellungen -> WLAN, suchen Sie in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett an der Unterseite des Routers.

### 3. Im Web-Admin-Panel anmelden

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie Ihre Sprache aus und legen Sie Ihr Admin-Passwort fest. Klicken Sie anschließend auf **Apply**.

Bitte beachten Sie: Wenn Sie die Wi-Fi-Daten ändern, müssen Sie Ihr Gerät mit den aktualisierten Zugangsdaten erneut mit dem Wi-Fi des Routers verbinden.

### 4. Internet einrichten

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Mango mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/ethernet.png){class="glboxshadow"}
    
    Verbinden Sie den WAN-Port Ihres Routers per Ethernet-Kabel mit einem vorgelagerten Gerät, beispielsweise einem Modem.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/repeater.png){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder einen USB-Dongle, per USB-Kabel mit dem USB-Port des Routers.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Abschnitt Tethering auf **Connect**.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Tethering-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/usb_modem.png){class="glboxshadow"}

    Diese Methode eignet sich, um die Internetverbindung eines USB-Modems mit allen verbundenen Geräten zu teilen.

    1. Schließen Sie ein mobilfunkfähiges USB-Modem an den USB-Port des Routers an.
    2. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Cellular und klicken Sie auf **Connect**.
    3. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Cellular-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein USB-Modem eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

## So richten Sie ein VPN ein

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Mango und andere GL.iNet-Router unterstützen OpenVPN und WireGuard.

=== "OpenVPN" 

    Mango und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

## Anwendungen

=== "Plug-ins"

    Plug-ins sind Zusatzfunktionen, die die Funktionalität Ihres Routers erweitern.
    
    Informationen zur Einrichtung finden Sie unter [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert die mit einer Domain verknüpfte IP-Adresse automatisch in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.
    
    Informationen zur Einrichtung finden Sie unter [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Der Cloud-Management-Dienst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} von GL.iNet bietet eine einfache und unkomplizierte Möglichkeit, per Fernzugriff auf GL.iNet-Router zuzugreifen und sie zu verwalten.
    
    Informationen zur Einrichtung finden Sie unter [GoodCloud](../../interface_guide/cloud.md).

## Netzwerkeinstellungen

=== "Firewall"

    Die Seite Firewall bietet wichtige Sicherheitsverbesserungen für Ihr Netzwerk. Sie umfasst Funktionen wie Port Forwarding, Open Ports und DMZ. Mit diesen Werkzeugen können Sie den Datenverkehr Ihres Netzwerks verwalten, anpassen und dessen Sicherheit erhöhen.

    * Port Forwarding: Leiten Sie bestimmten Datenverkehr aus dem Internet an festgelegte Geräte in Ihrem Netzwerk weiter, um beispielsweise den Zugriff auf Spieleserver oder Webserver zu ermöglichen.
    * Open Ports: Überwachen und steuern Sie, welche Ports an Ihrem Router geöffnet sind, um unbefugten Zugriff und potenzielle Sicherheitsbedrohungen zu verhindern.
    * DMZ (Demilitarized Zone): Platzieren Sie ein Gerät außerhalb der Haupt-Firewall, sodass es uneingeschränkten Internetzugang erhält, während der Rest Ihres Netzwerks vor potenziellen Bedrohungen geschützt bleibt.

    Informationen zur Einrichtung finden Sie unter [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen, z. B. Cellular, Repeater und Ethernet, einrichten können. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang reibungslos und unterbrechungsfrei.

    Informationen zur Einrichtung finden Sie unter [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Auf der Seite LAN können Sie die Einstellungen des lokalen Netzwerks Ihres Routers verwalten und konfigurieren. Zu den wichtigsten Funktionen dieser Seite gehören:

    * Router IP Address: Ändern Sie die IP-Adresse Ihres Routers, damit sie besser zu Ihrer Netzwerkkonfiguration passt.
    * Netmask: Legen Sie die Subnetzmaske für Ihr Netzwerk fest, die Größe und Bereich der IP-Adressen bestimmt.
    * DHCP: Aktivieren oder konfigurieren Sie das Dynamic Host Configuration Protocol, das Geräten in Ihrem Netzwerk automatisch IP-Adressen zuweist.
    * Address Reservation: Reservieren Sie bestimmte IP-Adressen für einzelne Geräte, damit diese vom DHCP-Server immer dieselbe IP-Adresse erhalten.

    Informationen zur Einrichtung finden Sie unter [LAN](../../interface_guide/lan.md).

---

=== "DNS"

    Die DNS-Seite bietet Optionen zur Anpassung der Domain-Name-System-Einstellungen Ihres Routers und verbessert dadurch sowohl Sicherheit als auch Leistung. Zu den wichtigsten Funktionen dieser Seite gehören:

    * Encrypted DNS: Konfigurieren Sie verschlüsseltes DNS, um Ihre Browserdaten vor Überwachung oder Manipulation zu schützen und so Datenschutz und Sicherheit zu gewährleisten.
    * Manual DNS: Legen Sie DNS-Server Ihrer Wahl manuell fest, um DNS-Abfragen individuell zu steuern und unter Umständen schnellere Auflösungszeiten zu erreichen.
    * DNS Proxy: Aktivieren Sie den DNS-Proxy, um DNS-Anfragen Ihrer Geräte über einen bestimmten DNS-Server zu leiten und eine zusätzliche Kontrollschicht über den DNS-Datenverkehr zu erhalten.

    Mit diesen Einstellungen können Sie die DNS-Leistung und -Sicherheit Ihres Netzwerks an Ihre Anforderungen anpassen.

    Informationen zur Einrichtung finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Die Seite Network Mode ermöglicht es Ihnen, Ihren Router in verschiedenen Modi zu betreiben und so flexibel auf unterschiedliche Netzwerkanforderungen zu reagieren. Die verfügbaren Modi umfassen:

    * Router: Arbeitet als Standardrouter, verwaltet den Datenverkehr zwischen Ihrem lokalen Netzwerk und dem Internet und stellt Funktionen wie NAT, Firewall und DHCP bereit.
    * Access Point: Arbeitet als Access Point und erweitert Ihr bestehendes kabelgebundenes Netzwerk um drahtlose Konnektivität, ohne den Datenverkehr zu routen.
    * Extender: Arbeitet als Reichweitenverlängerer und verstärkt das Signal Ihres bestehenden drahtlosen Netzwerks, um einen größeren Bereich abzudecken und Funklöcher zu beseitigen.
    * WDS (Wireless Distribution System): Ähnlich wie Extender; wählen Sie WDS, wenn Ihr Hauptrouter den WDS-Modus unterstützt.

    Informationen zur Einrichtung finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    Die Seite IPv6 ermöglicht es Ihnen, IPv6-Einstellungen für Ihr Netzwerk zu konfigurieren und damit das neueste Internetprotokoll zu nutzen. Auf dieser Seite können Sie IPv6 aktivieren und aus vier verschiedenen Modi wählen, passend zu Ihren Netzwerkanforderungen:

    * Native: Beziehen Sie direkt von Ihrem ISP eine IPv6-Adresse und nutzen Sie eine direkte und effiziente native IPv6-Verbindung.
    * Passthrough: Lassen Sie IPv6-Datenverkehr durch den Router zu den Geräten in Ihrem Netzwerk durchreichen, ohne dass der Router selbst das IPv6-Routing übernimmt.
    * NAT6: Verwenden Sie Network Address Translation für IPv6 (NAT6), um zwischen internen und externen IPv6-Adressen zu übersetzen, ähnlich wie NAT bei IPv4.
    * Static IPv6: Konfigurieren Sie manuell eine statische IPv6-Adresse für Ihren Router, um eine feste Adresse für konsistente Konnektivität und einfachere Verwaltung von Netzwerkdiensten bereitzustellen.

    Diese Einstellungen helfen Ihnen, die Vorteile von IPv6 zu nutzen, darunter ein größerer Adressraum, verbesserte Sicherheitsfunktionen und bessere Leistung.

    Informationen zur Einrichtung finden Sie unter [IPv6](../../interface_guide/network_mode.md).

---

=== "MAC Address"

    Auf der Seite MAC Address können Sie die mit Ihrem Router verknüpften MAC-Adressen anzeigen und verwalten. Zu den wichtigsten Funktionen dieser Seite gehören:

    * Factory Default: Zeigt die Standard-MAC-Adressen für den Ethernet- und Repeater-Modus des Routers an und dient als Referenz für die ursprünglichen Hardwareeinstellungen.
    * Clone: Klonen Sie die MAC-Adresse eines bestimmten Client-Geräts. Das ist besonders nützlich, wenn der Netzwerkzugang auf bestimmte Geräte beschränkt ist.
    * Manual: Geben Sie manuell eine benutzerdefinierte MAC-Adresse für Ihren Router an. Zusätzlich können Sie mit der Schaltfläche Random eine zufällige MAC-Adresse erzeugen, was mehr Flexibilität und zusätzlichen Datenschutz bietet.

    Mit diesen Funktionen können Sie die MAC-Adressen Ihres Routers effektiv verwalten und so Kompatibilität und Flexibilität in verschiedenen Netzwerkumgebungen sicherstellen.

    Informationen zur Verwaltung finden Sie unter [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionen Ihres Hauptrouters um Features, die er möglicherweise nicht besitzt, darunter AdGuard Home, verschlüsseltes DNS und VPN.
    
    Informationen zur Einrichtung finden Sie unter [Drop-in Gateway einrichten](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    Die Seite IGMP Snooping ermöglicht es Ihnen, Einstellungen zu konfigurieren, die das Multicast-Verkehrsmanagement in Ihrem Netzwerk optimieren. IGMP Snooping lauscht auf IGMP-Protokollpakete, extrahiert Informationen daraus und erstellt sowie pflegt Layer-2-Multicast-Weiterleitungstabellen. Dadurch werden Multicast-Gruppendaten nur an Hosts weitergeleitet, die der Multicast-Gruppe beigetreten sind, und unerwünschter Multicast-Verkehr erreicht keine anderen Hosts.

    Diese Einstellungen helfen, Netzwerkleistung und Effizienz zu optimieren, insbesondere in Umgebungen mit starkem Multicast-Verkehr wie Video-Streaming oder Online-Gaming.

    Informationen zur Einrichtung finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Systemeinstellungen

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der CPU Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um Ressourcen besser verwalten zu können.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, um sicherzustellen, dass genügend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * LED Control: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die optischen Anzeigen des Geräts anzupassen.
    * System Info: Rufen Sie detaillierte Systeminformationen Ihres Routers ab, darunter Firmware-Version, Laufzeit und Netzwerkstatus.
    
    Diese Funktionen bieten wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Die Seite Upgrade dient dazu, die Firmware Ihres Routers auf die neueste Version zu aktualisieren und so bessere Leistung, höhere Sicherheit und neue Funktionen bereitzustellen. Diese Seite bietet zwei Upgrade-Optionen:

    * Online Upgrade: Prüft automatisch auf die neueste Firmware-Version und installiert sie direkt vom Server des Herstellers, was den Aktualisierungsprozess vereinfacht.
    * Local Upgrade: Lädt eine Firmware-Datei manuell von Ihrem Computer hoch, damit Sie Version und Zeitpunkt des Upgrades selbst steuern können.

    Mit diesen Optionen halten Sie Ihren Router mit den neuesten Verbesserungen und Fehlerbehebungen auf dem aktuellen Stand.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Die Seite Scheduled Tasks ermöglicht es Ihnen, verschiedene Routerfunktionen auf Basis eines vordefinierten Zeitplans zu automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten die Lichtbelastung zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie den Router so, dass er in festgelegten Intervallen automatisch neu startet, um optimale Leistung und Stabilität zu erhalten.
    * 2.4GHz Wi-Fi Status Schedule: Legen Sie einen Zeitplan fest, um das 2,4-GHz-Wi-Fi-Band zu steuern und so Netzwerkverfügbarkeit sowie Stromverbrauch besser zu verwalten.
    
    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers und helfen dabei, ihn an Ihre Anforderungen und Vorlieben anzupassen.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche Ihres Routers festlegen oder ändern, damit nur autorisierte Benutzer auf die Routereinstellungen zugreifen und sie ändern können. Dieses Passwort ist entscheidend, um die Sicherheit und Integrität Ihres Netzwerks zu wahren und unbefugten Zugriff sowie Konfigurationsänderungen zu verhindern.

    Detaillierte Anweisungen finden Sie unter [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle geplanten Aufgaben, Protokolle und Systemereignisse mit Ihrer lokalen Zeit korrekt zeitgestempelt werden. Diese Einstellung ist entscheidend für präzise Aufzeichnungen und die ordnungsgemäße Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Auf der Seite Toggle Button Settings können Sie den physischen Kippschalter Ihres Routers konfigurieren und ihm bestimmte Funktionen für schnellen Zugriff und direkte Steuerung zuweisen. Diese Funktion bietet praktische Kurzbefehle für häufig verwendete Aufgaben und Einstellungen, verbessert die Benutzererfahrung und vereinfacht die Routerverwaltung.

    Detaillierte Anweisungen finden Sie unter [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Die Seite Log bietet Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und bei der Fehlerbehebung sowie der Leistungsüberwachung helfen. Diese Seite enthält:

    * System Log: Detaillierte Protokolle von Systemereignissen und Aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, nützlich zur Diagnose kritischer Probleme.
    * Cloud Log: Protokolle von Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern er vom Router verwendet wird, mit Details zum Webverkehr und Serverbetrieb.
    
    Zusätzlich verfügt die Seite über eine Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders wertvoll bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    Die Seite Reset Firmware ermöglicht es Ihnen, die aktuell installierte Firmware-Version Ihres Routers auf die Standardeinstellungen zurückzusetzen, wobei alle benutzerdefinierten Konfigurationen gelöscht werden. Dadurch wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Dies kann bei der Fehlerbehebung hartnäckiger Probleme hilfreich sein oder wenn Sie mit der Standardkonfiguration der aktuellen Firmware neu beginnen möchten.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche, sodass erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen können. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
