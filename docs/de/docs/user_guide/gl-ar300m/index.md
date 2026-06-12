# Shadow (GL-AR300M Series) Benutzerhandbuch

## Produktübersicht

Shadow (GL-AR300M Series) ist ein Mini-Router im Taschenformat, der für den mobilen Einsatz und Reisen entwickelt wurde und drahtlose Übertragungsraten von bis zu 300 Mbit/s unterstützt. Shadow bietet erweiterte Sicherheitsfunktionen, darunter Unterstützung für OpenVPN, WireGuard® und einen DNS-Server. Sie können damit nicht nur ein öffentliches Netzwerk in ein privates Wi-Fi für sicheres Surfen umwandeln, sondern auch VPN-Konfigurationsdateien von mehr als 30 VPN-Dienstanbietern hochladen und den Router als VPN-Client verwenden, um eine zusätzliche Ebene für Datenschutz und Sicherheit durch verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server bereitzustellen.

![ar300m illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## So richten Sie Shadow ein

Um Shadow einzurichten, verwenden Sie eine der vier unterstützten Internetverbindungsmethoden: Ethernet, Repeater, Tethering und Cellular. Folgen Sie den untenstehenden Schritten.

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

Richten Sie Shadow mit einer der unterstützten Internetverbindungsmethoden ein: Ethernet, Repeater, Tethering und Cellular. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/ethernet.png){class="glboxshadow"}
    
    Verbinden Sie den WAN-Port Ihres Routers per Ethernet-Kabel mit einem vorgelagerten Gerät, beispielsweise einem Modem.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/repeater.png){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder einen USB-Dongle, per USB-Kabel mit dem USB-Port des Routers.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Abschnitt Tethering auf **Connect**.
    
    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Tethering-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar300m/internet_setup/usb_modem.png){class="glboxshadow"}

    Diese Methode eignet sich, um die Internetverbindung eines USB-Modems mit allen verbundenen Geräten zu teilen.

    1. Schließen Sie ein mobilfunkfähiges USB-Modem an den USB-Port des Routers an.
    2. Suchen Sie auf der Seite INTERNET des Web-Admin-Panels den Bereich Cellular und klicken Sie auf **Connect**.
    3. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Cellular-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein USB-Modem eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

## So richten Sie ein VPN ein

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Shadow und andere GL.iNet-Router unterstützen OpenVPN und WireGuard.

=== "OpenVPN" 

    Shadow und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Shadow und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

## Anwendungen

=== "Plug-ins"

    Plug-ins sind Zusatzfunktionen, die den Funktionsumfang Ihres Routers erweitern.
    
    Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.
    
    Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Der Cloud-Management-Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten.
    
    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

## Netzwerkeinstellungen

=== "Firewall"

    Die Seite Firewall bietet wichtige Sicherheitsfunktionen für Ihr Netzwerk. Sie enthält Funktionen wie Port Forwarding, Open Ports und DMZ. Mit diesen Werkzeugen können Sie den Datenverkehr Ihres Netzwerks steuern, anpassen und seine Sicherheit erhöhen.

    * Port Forwarding: Leiten Sie bestimmten Datenverkehr aus dem Internet an festgelegte Geräte in Ihrem Netzwerk weiter, um den Zugriff auf Dienste wie Spieleserver oder Webserver zu ermöglichen.
    * Open Ports: Überwachen und steuern Sie, welche Ports auf Ihrem Router offen sind, um unbefugten Zugriff und potenzielle Sicherheitsbedrohungen zu vermeiden.
    * DMZ (Demilitarized Zone): Platzieren Sie ein Gerät außerhalb der Haupt-Firewall, damit es uneingeschränkt auf das Internet zugreifen kann, während der Rest Ihres Netzwerks weiterhin geschützt bleibt.

    Zum Konfigurieren der Firewall-Einstellungen lesen Sie bitte [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen, z. B. Cellular, Repeater und Ethernet, konfigurieren können. Fällt Ihre aktuelle Internetverbindung aus, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt Ihr Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Auf der Seite LAN können Sie die Einstellungen des lokalen Netzwerks Ihres Routers verwalten und konfigurieren. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Router IP Address: Ändern Sie die IP-Adresse Ihres Routers, damit sie besser zu Ihrer Netzwerkkonfiguration passt.
    * Netmask: Legen Sie die Subnetzmaske Ihres Netzwerks fest, die Größe und Adressbereich des Netzwerks bestimmt.
    * DHCP: Aktivieren oder konfigurieren Sie das Dynamic Host Configuration Protocol, das Geräten in Ihrem Netzwerk automatisch IP-Adressen zuweist.
    * Address Reservation: Reservieren Sie bestimmte IP-Adressen für einzelne Geräte, damit diese vom DHCP-Server immer dieselbe IP-Adresse erhalten.

    Zum Einrichten von LAN lesen Sie bitte [Lan](../../interface_guide/lan.md).

---

=== "DNS"

    Die Seite DNS bietet Optionen zum Anpassen der Domain-Name-System-Einstellungen Ihres Routers und verbessert sowohl Sicherheit als auch Leistung. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Encrypted DNS: Konfigurieren Sie verschlüsseltes DNS, um Ihre Browserdaten vor Überwachung oder Manipulation zu schützen und so Privatsphäre und Sicherheit zu gewährleisten.
    * Manual DNS: Legen Sie DNS-Server Ihrer Wahl manuell fest, um DNS-Abfragen gezielt zu steuern und möglicherweise schnellere Auflösungszeiten zu erreichen.
    * DNS Proxy: Aktivieren Sie DNS Proxy, um DNS-Anfragen Ihrer Geräte über einen bestimmten DNS-Server zu leiten und so eine zusätzliche Kontrolle über den DNS-Datenverkehr zu erhalten.

    Mit diesen Einstellungen können Sie die DNS-Leistung und Sicherheit Ihres Netzwerks an Ihre Anforderungen anpassen.

    Zum Einrichten von DNS lesen Sie bitte [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Auf der Seite Network Mode können Sie Ihren Router für verschiedene Betriebsarten konfigurieren, um unterschiedliche Netzwerkanforderungen flexibel abzudecken. Verfügbare Modi sind:

    * Router: Arbeiten Sie als Standardrouter, verwalten Sie den Datenverkehr zwischen lokalem Netzwerk und Internet und nutzen Sie Funktionen wie NAT, Firewall und DHCP.
    * Access Point: Nutzen Sie den Router als Access Point, um Ihr bestehendes kabelgebundenes Netzwerk mit drahtloser Konnektivität zu erweitern, ohne Routing durchzuführen.
    * Extender: Verwenden Sie den Router als Reichweitenverlängerer, um das Signal Ihres bestehenden drahtlosen Netzwerks zu verstärken, größere Bereiche abzudecken und Funklöcher zu vermeiden.
    * WDS (Wireless Distribution System): Ähnlich wie Extender; wählen Sie WDS, wenn Ihr Hauptrouter den WDS-Modus unterstützt.

    Zum Einrichten des Network Mode lesen Sie bitte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    Auf der Seite IPv6 können Sie IPv6-Einstellungen für Ihr Netzwerk konfigurieren und Unterstützung für das neueste Internetprotokoll bereitstellen. Auf dieser Seite können Sie IPv6 aktivieren und aus vier verschiedenen Modi wählen, die zu Ihren Netzwerkanforderungen passen:

    * Native: Beziehen Sie eine IPv6-Adresse direkt von Ihrem ISP, um eine einfache und effiziente native IPv6-Konnektivität zu nutzen.
    * Passthrough: Lassen Sie IPv6-Datenverkehr durch den Router zu den Geräten in Ihrem Netzwerk weiterleiten, wobei die Verbindung effektiv durchgereicht wird, ohne dass der Router selbst IPv6-Routing übernimmt.
    * NAT6: Verwenden Sie Network Address Translation für IPv6 (NAT6), um zwischen internen und externen IPv6-Adressen zu übersetzen, ähnlich wie NAT bei IPv4 funktioniert.
    * Static IPv6: Konfigurieren Sie manuell eine statische IPv6-Adresse für Ihren Router, um eine feste Adresse für stabile Konnektivität und einfachere Verwaltung von Netzwerkdiensten bereitzustellen.

    Diese Einstellungen helfen Ihnen, die Vorteile von IPv6 zu nutzen, darunter ein größerer Adressraum, verbesserte Sicherheitsfunktionen und bessere Leistung.

    Zum Einrichten von IPv6 lesen Sie bitte [IPv6](../../interface_guide/network_mode.md).

---

=== "MAC Address"

    Auf der Seite MAC Address können Sie die mit Ihrem Router verbundenen Media-Access-Control-(MAC-)Adressen anzeigen und verwalten. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Factory Default: Zeigen Sie die Standard-MAC-Adressen für die Ethernet- und Repeater-Modi des Routers an, um die ursprünglichen Hardware-Einstellungen nachzuvollziehen.
    * Clone: Klonen Sie die MAC-Adresse eines bestimmten Client-Geräts. Dies ist besonders nützlich, wenn der Netzwerkzugang auf bestimmte Geräte beschränkt ist.
    * Manual: Legen Sie manuell eine benutzerdefinierte MAC-Adresse für Ihren Router fest. Zusätzlich können Sie mit der Schaltfläche Random eine zufällige MAC-Adresse erzeugen, was mehr Flexibilität und Privatsphäre bietet.

    Mit diesen Funktionen können Sie die MAC-Adressen Ihres Routers effektiv verwalten und so Kompatibilität und Flexibilität in unterschiedlichen Netzwerkumgebungen sicherstellen.

    Zum Verwalten der MAC-Adresse lesen Sie bitte [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen, die er möglicherweise nicht besitzt, darunter AdGuard Home, verschlüsseltes DNS und VPN.
    
    Zum Einrichten von Drop-in Gateway lesen Sie bitte [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    Auf der Seite IGMP Snooping können Sie Einstellungen konfigurieren, die das Multicast-Verkehrsmanagement in Ihrem Netzwerk optimieren. IGMP Snooping überwacht IGMP-Protokollpakete und extrahiert Informationen daraus, um Multicast-Weiterleitungstabellen auf Layer 2 aufzubauen und zu pflegen. So wird sichergestellt, dass Multicast-Gruppendaten nur an Hosts weitergeleitet werden, die der Multicast-Gruppe beigetreten sind, und unerwünschter Multicast-Verkehr andere Hosts nicht erreicht.

    Diese Einstellungen helfen, Netzwerkleistung und Effizienz zu optimieren, insbesondere in Umgebungen mit hohem Multicast-Aufkommen, etwa bei Video-Streaming oder Online-Gaming.

    Zum Einrichten von IGMP Snooping lesen Sie bitte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Systemeinstellungen

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungskennzahlen Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche CPU-Auslastung Ihres Routers, um die Leistung zu beurteilen und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers verwendet wird, um die Ressourcennutzung besser zu verwalten.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers des Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten vorhanden ist.
    * LED Control: Schalten Sie die LED-Leuchten des Routers ein oder aus, um die visuellen Anzeigen des Geräts anzupassen.
    * System Info: Greifen Sie auf detaillierte Informationen zum System Ihres Routers zu, einschließlich Firmware-Version, Uptime und Netzwerkstatus.
    
    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Die Seite Upgrade dient dazu, die Firmware Ihres Routers auf die neueste Version zu aktualisieren, um Leistung, Sicherheit und neue Funktionen bereitzustellen. Diese Seite bietet zwei Upgrade-Optionen:

    * Online Upgrade: Prüfen und installieren Sie automatisch die neueste Firmware-Version direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren und dabei Version und Zeitpunkt des Upgrades selbst zu bestimmen.

    Mit diesen Optionen halten Sie Ihren Router mit den neuesten Verbesserungen und Fehlerbehebungen aktuell.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Router-Funktionen anhand eines vordefinierten Zeitplans automatisieren, was Komfort und Effizienz erhöht. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Leuchten des Routers automatisch ein- oder auszuschalten und so zu bestimmten Zeiten Lichtemissionen zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um optimale Leistung und Stabilität zu erhalten.
    * 2.4GHz Wi-Fi Status Schedule: Legen Sie einen Zeitplan zur Steuerung des 2.4GHz-Wi-Fi-Bands fest, um Netzwerkverfügbarkeit und Stromverbrauch besser zu verwalten.
    
    Diese Planungsoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers, damit er Ihren Anforderungen und Vorlieben besser entspricht.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche Ihres Routers festlegen oder ändern. So wird sichergestellt, dass nur autorisierte Benutzer auf die Router-Einstellungen zugreifen und sie ändern können. Dieses Passwort ist entscheidend, um Sicherheit und Integrität Ihres Netzwerks zu wahren und unbefugten Zugriff sowie Konfigurationsänderungen zu verhindern.

    Detaillierte Anweisungen finden Sie unter [Admin Password](../../interface_guide/admin_password.md).

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

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf die Werkseinstellungen zurücksetzen, wobei alle benutzerdefinierten Konfigurationen gelöscht werden. Dieser Vorgang stellt die Standardeinstellungen der derzeit installierten Firmware-Version wieder her. Das kann hilfreich sein, um hartnäckige Probleme zu beheben oder mit einer sauberen Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Die Seite Advanced Settings bietet Zugriff auf erweiterte Konfigurationsoptionen über die OpenWrt-LuCI-Oberfläche. Damit können erfahrene Benutzer die Einstellungen und Funktionen ihres Routers über die grundlegenden Oberflächenoptionen hinaus fein abstimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
