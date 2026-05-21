# Creta (GL-AR750) Benutzerhandbuch

## Produktübersicht

Creta (GL-AR750) ist ein Dual-Band-AC-Reiserouter. Das gleichzeitige Dual-Band unterstützt eine drahtlose Übertragungsrate von bis zu 733 Mbit/s (2.4 GHz: 300 Mbit/s + 5 GHz: 433 Mbit/s). Creta kann ein öffentliches Netzwerk in ein privates Wi-Fi für sicheres Surfen umwandeln. Der externe Speicher unterstützt MicroSD-Karten bis 128 GB. OpenWrt/LEDE und OpenVPN sind vorinstalliert. Dadurch bietet Creta datenschutzbewussten Benutzern ein schnelles und einfaches VPN mit moderner Kryptografie.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Technische Daten

[Technische Daten des GL-AR750](https://www.gl-inet.com/products/gl-ar750/#specs){target="\_blank"}

## So richten Sie Creta ein

Zum Einrichten von Creta verwenden Sie eine der vier unterstützten Internetverbindungsmethoden: Ethernet, Repeater, Tethering und Cellular. Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In diesem Video wird ein anderer GL.iNet-Router zur Demonstration verwendet, die Schritte sind jedoch für Creta und andere Routermodelle identisch.)</small>

### 1. Creta einschalten

Schließen Sie das Micro-USB-Stromkabel an den Stromanschluss des Routers an. Stellen Sie sicher, dass Sie ein Standard-Netzteil mit 5 V/2 A verwenden.

!!! Note

    Hot-Plugging für TF-Karten wird nicht unterstützt. Wenn Sie eine TF-Karte verwenden möchten, setzen Sie sie bitte ein, bevor Sie den Router einschalten.

### 2. Ihr Gerät mit Creta verbinden

Verbinden Sie Ihren Computer oder Ihr Mobilgerät per Wi-Fi oder Ethernet mit dem Router.

=== "Wi-Fi"

    Suchen Sie auf Ihrem Gerät in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett Ihres Routers.

=== "Ethernet"

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

### 3. Creta mit dem Internet verbinden

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das Web-Admin-Panel mit dem Internet verbinden. Wenn Sie statt des Web-Admin-Panels lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="\_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

#### 1. Im Web-Admin-Panel des Routers anmelden

Geben Sie in einem Webbrowser `192.168.8.1` in die Adressleiste ein. Wählen Sie Ihre Sprache aus und klicken Sie dann auf **Next**. Legen Sie Ihr Admin-Passwort fest und klicken Sie anschließend auf **Apply**.

#### 2. Ihre Internetverbindungsmethode(n) einrichten

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}

    Verbinden Sie den WAN-Port Ihres Routers per Ethernet-Kabel mit einem vorgelagerten Gerät, z. B. einem Modem. Wenn die Internetverbindung erfolgreich hergestellt wurde, erscheint neben „Ethernet“ ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. Suchen Sie auf der Hauptseite des Web-Admin-Panels den Bereich „Repeater“ und klicken Sie dann auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus.
    3. Geben Sie das Netzwerkpasswort ein und klicken Sie dann auf **Apply**.

    Wenn die Internetverbindung erfolgreich hergestellt wurde, erscheint neben dem Wi-Fi-Netzwerknamen ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Verbinden Sie Ihr Smartphone per USB-Kabel mit dem Router und aktivieren Sie in den Einstellungen des persönlichen Hotspots die Netzwerkfreigabe.
    2. Suchen Sie auf der Hauptseite des Web-Admin-Panels den Bereich „Tethering“ und klicken Sie dann auf **Connect**.
    3. Wenn die Internetverbindung erfolgreich hergestellt wurde, erscheint neben „Tethering“ ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Stecken Sie ein Mobilfunk-USB-Modem in den USB-Port des Routers.
    2. Suchen Sie auf der Hauptseite des Web-Admin-Panels den Bereich „Cellular“ und klicken Sie dann auf **Connect**.
    3. Wenn die Internetverbindung erfolgreich hergestellt wurde, erscheint neben „Cellular“ ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein USB-Modem eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md).

**Hinweis:** Wenn Sie die Multi-WAN-Funktion verwenden möchten, müssen Sie mehr als eine Internetverbindungsmethode einrichten.

---

## So richten Sie ein VPN ein

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Creta und andere GL.iNet-Router unterstützen OpenVPN und WireGuard.

=== "OpenVPN"

    Creta und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

---

## Weitere Anwendungen

=== "Plug-ins"

    Plug-ins sind Zusatzfunktionen, die den Funktionsumfang Ihres Routers erweitern. Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen. Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Der Cloud-Management-Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, per Fernzugriff auf GL.iNet-Router zuzugreifen und sie zu verwalten. Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

---

## Netzwerkeinstellungen

=== "Firewall"

    Die Seite Firewall bietet wichtige Sicherheitsfunktionen für Ihr Netzwerk. Dazu gehören Port Forwarding, Open Ports und DMZ. Mit diesen Werkzeugen können Sie den Datenverkehr Ihres Netzwerks verwalten und anpassen sowie dessen Sicherheit erhöhen.

    * Port Forwarding: Leiten Sie bestimmten Datenverkehr aus dem Internet an festgelegte Geräte in Ihrem Netzwerk weiter, um den Zugriff auf Dienste wie Spieleserver oder Webserver zu ermöglichen.
    * Open Ports: Überwachen und steuern Sie, welche Ports an Ihrem Router geöffnet sind, um unbefugten Zugriff und mögliche Sicherheitsbedrohungen zu verhindern.
    * DMZ (Demilitarized Zone): Platzieren Sie ein Gerät außerhalb der Haupt-Firewall, sodass es uneingeschränkten Zugriff auf das Internet erhält, während der Rest Ihres Netzwerks vor potenziellen Bedrohungen geschützt bleibt.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen einrichten können, z. B. Cellular, Repeater und Ethernet. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Auf der Seite LAN können Sie die Einstellungen des lokalen Netzwerks Ihres Routers verwalten und konfigurieren. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Router IP Address: Ändern Sie die IP-Adresse Ihres Routers, damit sie besser zu Ihrer Netzwerkkonfiguration passt.
    * Netmask: Legen Sie die Subnetzmaske für Ihr Netzwerk fest, die Größe und IP-Adressbereich des Netzwerks bestimmt.
    * DHCP: Aktivieren oder konfigurieren Sie das Dynamic Host Configuration Protocol, das Geräten in Ihrem Netzwerk automatisch IP-Adressen zuweist.
    * Address Reservation: Reservieren Sie bestimmte IP-Adressen für einzelne Geräte, damit diese immer dieselbe IP-Adresse vom DHCP-Server erhalten.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [LAN](../../interface_guide/lan.md).

---

=== "DNS"

    Die Seite DNS bietet Optionen zur Anpassung der Domain-Name-System-Einstellungen Ihres Routers und verbessert dadurch sowohl Sicherheit als auch Leistung. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Encrypted DNS: Konfigurieren Sie verschlüsseltes DNS, um Ihre Browserdaten vor Überwachung oder Manipulation zu schützen und so Datenschutz und Sicherheit zu gewährleisten.
    * Manual DNS: Legen Sie DNS-Server Ihrer Wahl manuell fest, um DNS-Anfragen gezielt zu steuern und unter Umständen schnellere Auflösungszeiten zu erreichen.
    * DNS Proxy: Aktivieren Sie den DNS-Proxy, um DNS-Anfragen Ihrer Geräte über einen bestimmten DNS-Server zu leiten und so eine zusätzliche Kontrolle über den DNS-Datenverkehr zu erhalten.

    Mit diesen Einstellungen können Sie die DNS-Leistung und Sicherheit Ihres Netzwerks an Ihre Anforderungen anpassen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Auf der Seite Network Mode können Sie Ihren Router für verschiedene Betriebsmodi konfigurieren und so flexibel auf unterschiedliche Netzwerkanforderungen reagieren. Verfügbare Modi sind:

    * Router: Arbeiten Sie als Standardrouter, der den Datenverkehr zwischen lokalem Netzwerk und Internet verwaltet und Funktionen wie NAT, Firewall und DHCP bereitstellt.
    * Access Point: Arbeiten Sie als Access Point und erweitern Sie Ihr bestehendes kabelgebundenes Netzwerk um drahtlose Konnektivität, ohne Datenverkehr zu routen.
    * Extender: Arbeiten Sie als Reichweitenverlängerer, verstärken Sie das Signal Ihres vorhandenen drahtlosen Netzwerks und decken Sie einen größeren Bereich ohne Funklöcher ab.
    * WDS (Wireless Distribution System): Ähnlich wie Extender. Wählen Sie WDS, wenn Ihr Hauptrouter den WDS-Modus unterstützt.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    Auf der Seite IPv6 können Sie IPv6-Einstellungen für Ihr Netzwerk konfigurieren und so Unterstützung für das neueste Internetprotokoll bereitstellen. Auf dieser Seite können Sie IPv6 aktivieren und aus vier verschiedenen Modi wählen, passend zu Ihren Netzwerkanforderungen:

    * Native: Beziehen Sie direkt von Ihrem ISP eine IPv6-Adresse, um eine einfache und effiziente native IPv6-Konnektivität zu erhalten.
    * Passthrough: Lassen Sie IPv6-Datenverkehr durch den Router zu den Geräten in Ihrem Netzwerk weiterleiten, sodass die Verbindung effektiv durchgereicht wird, ohne dass der Router selbst IPv6-Routing übernimmt.
    * NAT6: Nutzen Sie Network Address Translation für IPv6 (NAT6), um zwischen internen und externen IPv6-Adressen zu übersetzen, ähnlich wie NAT bei IPv4 funktioniert.
    * Static IPv6: Konfigurieren Sie manuell eine statische IPv6-Adresse für Ihren Router, um eine feste Adresse für konstante Konnektivität und einfachere Verwaltung von Netzwerkdiensten bereitzustellen.

    Mit diesen Einstellungen können Sie die Vorteile von IPv6 nutzen, darunter ein größerer Adressraum, erweiterte Sicherheitsfunktionen und eine bessere Leistung.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    Auf der Seite MAC Address können Sie die mit Ihrem Router verknüpften Media-Access-Control-Adressen (MAC-Adressen) anzeigen und verwalten. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * Factory Default: Zeigen Sie die Standard-MAC-Adressen für die Ethernet- und Repeater-Modi des Routers an, um eine Referenz für die ursprünglichen Hardware-Einstellungen zu haben.
    * Clone: Klonen Sie die MAC-Adresse eines bestimmten Client-Geräts. Das ist besonders nützlich in Szenarien, in denen der Netzwerkzugang auf bestimmte Geräte beschränkt ist.
    * Manual: Geben Sie manuell eine benutzerdefinierte MAC-Adresse für Ihren Router an. Zusätzlich können Sie mit der Schaltfläche Random eine zufällige MAC-Adresse erzeugen, was mehr Flexibilität und besseren Datenschutz bietet.

    Diese Funktionen ermöglichen es Ihnen, die MAC-Adressen Ihres Routers effektiv zu verwalten und so Kompatibilität und Flexibilität in unterschiedlichen Netzwerkumgebungen sicherzustellen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen, die er möglicherweise nicht besitzt, darunter AdGuard Home, verschlüsseltes DNS und VPN. Zum Einrichten von Drop-in Gateway lesen Sie bitte [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    Auf der Seite IGMP Snooping können Sie Einstellungen konfigurieren, die die Verwaltung von Multicast-Datenverkehr in Ihrem Netzwerk optimieren. IGMP Snooping überwacht IGMP-Protokollpakete, extrahiert Informationen daraus und erstellt sowie pflegt Layer-2-Multicast-Weiterleitungstabellen. Dadurch werden Multicast-Gruppendaten nur an Hosts weitergeleitet, die der Multicast-Gruppe beigetreten sind, sodass unerwünschter Multicast-Datenverkehr andere Hosts nicht erreicht.

    Diese Einstellungen helfen dabei, Netzwerkleistung und Effizienz zu optimieren, insbesondere in Umgebungen mit erheblichem Multicast-Datenverkehr, etwa bei Video-Streaming oder Online-Gaming.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Systemeinstellungen

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der Router-CPU, um die Leistung zu bewerten und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers aktuell genutzt wird, um Ressourcen besser zu verwalten.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten verfügbar bleibt.
    * LED Control: Schalten Sie die LED-Anzeigen des Routers ein oder aus, um die optischen Signale des Geräts anzupassen.
    * System Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, darunter Firmware-Version, Uptime und Netzwerkstatus.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    Auf der Seite Upgrade können Sie die Firmware Ihres Routers auf die neueste Version aktualisieren, um bessere Leistung, mehr Sicherheit und neue Funktionen zu erhalten. Diese Seite bietet zwei Upgrade-Optionen:

    * Online Upgrade: Prüfen Sie automatisch auf die neueste Firmware-Version und installieren Sie sie direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren, und behalten Sie dabei die Kontrolle über Version und Zeitpunkt des Upgrades.

    Mit diesen Optionen halten Sie Ihren Router auf dem neuesten Stand und profitieren von aktuellen Verbesserungen und Fehlerbehebungen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Routerfunktionen nach einem festgelegten Zeitplan automatisieren und so Komfort und Effizienz erhöhen. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Anzeigen des Routers zu bestimmten Zeiten automatisch ein- oder auszuschalten und so Lichtemissionen zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie den Router so, dass er in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität aufrechtzuerhalten.
    * 5GHz Wi-Fi Status Schedule: Erstellen Sie einen Zeitplan, um das 5-GHz-Wi-Fi-Band zu bestimmten Zeiten zu aktivieren oder zu deaktivieren und so Netzwerknutzung und Energieeffizienz zu optimieren.
    * 2.4GHz Wi-Fi Status Schedule: Legen Sie einen Zeitplan für das 2.4-GHz-Wi-Fi-Band fest, um Netzwerkverfügbarkeit und Stromverbrauch besser zu steuern.

    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers, sodass er Ihren Anforderungen und Vorlieben besser entspricht.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche Ihres Routers festlegen oder ändern, damit nur autorisierte Benutzer auf die Routereinstellungen zugreifen und diese ändern können. Dieses Passwort ist entscheidend, um die Sicherheit und Integrität Ihres Netzwerks zu wahren und unbefugten Zugriff sowie unerwünschte Konfigurationsänderungen zu verhindern.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle Zeitpläne, Protokolle und Systemereignisse präzise mit Ihrer Ortszeit versehen werden. Diese Einstellung ist wichtig für genaue Aufzeichnungen und die korrekte Ausführung zeitbasierter Konfigurationen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    Auf der Seite Toggle Button Settings können Sie den physischen Kippschalter Ihres Routers konfigurieren und ihm bestimmte Funktionen für schnellen Zugriff und einfache Steuerung zuweisen. Diese Funktion bietet praktische Kurzbefehle für häufig genutzte Aufgaben und Einstellungen, verbessert die Benutzererfahrung und vereinfacht die Routerverwaltung.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Auf der Seite Log erhalten Sie Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und so die Fehlerbehebung sowie Leistungsüberwachung unterstützen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle von Systemereignissen und -aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, die bei der Diagnose kritischer Probleme helfen.
    * Cloud Log: Protokolle zu Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern dieser vom Router genutzt wird, mit Informationen zu Webverkehr und Serverbetrieb.

    Zusätzlich verfügt die Seite über die Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders hilfreich bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen, wodurch alle benutzerdefinierten Konfigurationen gelöscht werden. Dabei wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Das ist hilfreich, um hartnäckige Probleme zu beheben oder mit der Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Auf der Seite Advanced Settings erhalten erfahrene Benutzer über die OpenWrt-LuCI-Oberfläche Zugriff auf erweiterte Konfigurationsoptionen, um Routereinstellungen und Funktionen über die grundlegenden Oberflächenoptionen hinaus fein abzustimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Einrichtungsanweisungen und weitere Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
