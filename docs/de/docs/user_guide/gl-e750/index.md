# Mudi V2 (GL-E750V2) Benutzerhandbuch

**Hinweis:** Mudi V2 (GL-E750V2) und Mudi (GL-E750) verwenden dieselbe Firmware. Wenn Sie Mudi (GL-E750) nutzen, [aktualisieren Sie Ihre Firmware](https://dl.gl-inet.com/?model=e750), um die neuesten Funktionen und Verbesserungen zu verwenden.

## Produktübersicht

Mudi V2 (GL-E750V2) ist ein tragbarer 4G-LTE-Reiserouter, der mit Netzbetreibern weltweit kompatibel ist. Er läuft vollständig Open Source auf OpenWrt und GL.iNet SDK 4.0 und bietet dadurch umfassende Anpassungsmöglichkeiten sowie eine Vielzahl an Funktionen. Mudi V2 (GL-E750V2) unterstützt Wi-Fi-Geschwindigkeiten von 300 Mbit/s (2.4GHz) und 433 Mbit/s (5GHz) sowie MicroSD-Karten mit bis zu 1 TB. Er verfügt über einen integrierten 7000-mAh-Akku. Außerdem unterstützt er Multi-WAN (Failover und Load Balance), um für all Ihre Geräte eine stabile Verbindung sicherzustellen.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Taste

- Drücken Sie die Einschalttaste **3 Sekunden lang**: Das Gerät wird eingeschaltet.

- Drücken Sie die Einschalttaste **3 bis 5 Sekunden lang**: Das Gerät wechselt in den Standby-Modus.

- Drücken Sie die Einschalttaste **länger als 5 Sekunden**: Das Gerät wird ausgeschaltet.

  (Wenn Sie die Taste 3 Sekunden lang drücken, zeigt der OLED-Bildschirm zunächst „Standby Mode On“ an. HALTEN SIE die Einschalttaste weiter gedrückt, bis unter „Standby Mode On“ der Hinweis „Shut Down“ erscheint. Anschließend wird 3 Sekunden heruntergezählt und das Gerät ausgeschaltet.)

## Standby-Modus

Im Standby-Modus schaltet Mudi V2 (GL-E750V2) Wi-Fi und 4G aus, um Strom zu sparen. In diesem Modus können Sie keine Verbindung zu Mudi V2 (GL-E750V2) herstellen.

Um den Standby-Modus ein- oder auszuschalten, drücken Sie die Einschalttaste 3 Sekunden lang. Auf dem OLED-Bildschirm wird dann „Standby Mode On“ oder „Standby Mode Off“ angezeigt.

## Lieferumfang

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x tragbarer 4G-LTE-Router Mudi V2 (GL-E750V2)
- 1 x tragbarer 4G-LTE-Router Mudi V2 (GL-E750V2)
- 1 x Netzadapter
- 4 x Adapter (US-, EU-, UK- und AU-Stecker)
- 1 x Benutzerhandbuch
- 1 x Garantiekarte
- 1 x Ethernet-Kabel
- 1 x USB-C-Port-Replikator
- 1 x USB-C-auf-USB-C-Kabel
- 1 x USB-A-auf-USB-C-Kabel
- 1 x Transportbeutel
- 1 x Dankeskarte

---

## Ersteinrichtung

Sehen Sie sich dieses Video an oder folgen Sie den Schritten, um Mudi V2 einzurichten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. SIM-Karte einsetzen

Setzen Sie eine SIM-Karte und optional eine MicroSD-Karte in Mudi V2 (GL-E750V2) ein.

Hinweis: Wenn Sie eine SIM-Karte verwenden, müssen Sie diese vor dem Einschalten in das Gerät einsetzen.

1. Drehen Sie Mudi V2 (GL-E750V2) auf die Rückseite.
2. Stecken Sie Ihren Finger in die Öffnung nahe am Rand der Abdeckung.
3. Fahren Sie entlang des Randes.
4. Wenn sich die Abdeckung leicht anhebt (auf etwa 25 bis 30 Grad), ziehen Sie sie zum Öffnen nach oben.
5. Setzen Sie die Karte entsprechend dem Symbol in der Ecke in den Kartenslot ein.
6. Drücken Sie die Abdeckung nach unten, um sie wieder zu schließen.

### 2. Einschalten

Drücken Sie die Einschalttaste, um das Gerät einzuschalten.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_power-on.png){class="glboxshadow"}

Wenn Mudi V2 (GL-E750V2) ausgeschaltet ist, können Sie den Akkustand trotzdem überprüfen, indem Sie die Einschalttaste drücken. Der LED-Bildschirm zeigt den Akkustatus an, wenn Sie die Taste drücken.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_battery.png){class="glboxshadow"}

Stellen Sie sicher, dass Sie einen Standard-5V/2A-Netzadapter verwenden. Andernfalls kann es zu Fehlfunktionen kommen.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET

Melden Sie sich im Web-Admin-Panel des Routers an und wechseln Sie im linken Menü zu **INTERNET**.

Auf dieser Seite können Sie Ihre Internetverbindungsart auswählen, z. B. Ethernet, Repeater, Tethering und Cellular.

### Ethernet

Verbinden Sie Ihren Router per Ethernet-Kabel mit einem aktiven Modem oder einem aktiven Netzwerkgerät, um auf das Internet zuzugreifen. Diese Methode bietet in der Regel die schnellste und zuverlässigste Internetverbindung.

[Klicken Sie hier, um zu erfahren, wie Sie über ein Ethernet-Kabel eine Internetverbindung herstellen](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Richten Sie Ihren Router als Repeater ein, um die Wi-Fi-Abdeckung eines vorhandenen Wi-Fi-Netzwerks zu erweitern. Als Repeater empfängt und sendet er Funksignale innerhalb seiner Reichweite erneut und vergrößert so die Abdeckung. Diese Methode ist nützlich, wenn ein einzelner Router den gesamten Einsatzbereich nicht abdecken kann.

[Klicken Sie hier, um zu erfahren, wie Sie über ein vorhandenes Wi-Fi eine Internetverbindung herstellen](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Verbinden Sie den USB-Port des Routers per USB-Kabel mit einem Smartphone mit aktiver mobiler Datenverbindung, um auf das Internet zuzugreifen. Mit dieser Methode können mehrere mit dem Router verbundene Geräte über die mobile Datenverbindung des Smartphones auf das Internet zugreifen.

[Klicken Sie hier, um zu erfahren, wie Sie über USB-Tethering eine Internetverbindung herstellen](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular

Entfernen Sie die rückseitige Abdeckung von Mudi V2 und setzen Sie eine SIM-Karte in den SIM-Kartenslot ein, um eine Verbindung zum Internet herzustellen. Diese Methode ist nützlich, um den Internetzugang einer einzelnen SIM-Karte mit allen verbundenen Geräten zu teilen.

[Klicken Sie hier, um zu erfahren, wie Sie über Cellular eine Internetverbindung herstellen](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750/internet/e750v2_cellular.png){class="glboxshadow"}

Wenn Sie eine physische eSIM-Karte auf Ihrem GL.iNet-Router verwenden möchten, klicken Sie bitte hier: [Wie verwendet man die physische eSIM-Karte mit GL.iNet-Routern?](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## WIRELESS

Über die Wireless-Einstellungen können Benutzer die Netzwerksicherheit des primären Wi-Fi und des Gast-Wi-Fi verwalten. Sie sind über **WIRELESS** im Seitenmenü erreichbar.

[Klicken Sie hier, um mehr über die Wireless-Konfiguration zu erfahren](../../interface_guide/wireless.md)

---

## CLIENTS

Clients sind Geräte, die mit dem Router verbunden sind. Sie können Clients blockieren oder ihre Netzwerkgeschwindigkeit begrenzen. Die Oberfläche ist über **CLIENTS** im Seitenmenü des Admin-Panels des Routers erreichbar.

[Klicken Sie hier, um mehr über die Verwaltung Ihrer Geräte-Clients zu erfahren.](../../interface_guide/clients.md)

---

## VPN

GL.iNet-Router sind mit OpenVPN und WireGuard® vorinstalliert und unterstützen mehr als 30 VPN-Dienste. Dadurch wird der gesamte Netzwerkverkehr im verbundenen Netzwerk automatisch verschlüsselt, einschließlich Gastgeräten und Client-Geräten, die selbst keine VPN-Verschlüsselung ausführen können. Unsere Router können außerdem als VPN-Server fungieren und den Verkehr von Client-Geräten an entfernten Standorten über einen VPN-Tunnel zum VPN-Server umleiten, bevor auf das öffentliche Internet zugegriffen wird.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Detaillierte Schritt-für-Schritt-Anleitungen finden Sie unter den folgenden Links:

- [**OpenVPN-Client einrichten**](../../interface_guide/openvpn_client.md)
- [**OpenVPN-Server einrichten**](../../interface_guide/openvpn_server.md)

### WireGuard

Detaillierte Schritt-für-Schritt-Anleitungen finden Sie unter den folgenden Links:

- [**WireGuard-Client einrichten**](../../interface_guide/wireguard_client.md)
- [**WireGuard-Server einrichten**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

GL.iNet-Router bieten eine Vielzahl zusätzlicher Funktionen, die die Geräteverwaltung vereinfachen, das Interneterlebnis der Benutzer verbessern, Firmware-Updates automatisieren und vieles mehr.

### Plug-ins

Lesen Sie das Tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Lesen Sie das Tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Lesen Sie das Tutorial [**GoodCloud**](../../interface_guide/cloud.md).

---

## NETWORK

### Firewall

Die Router von GL.iNet bieten mehrere Firewall-Funktionen, um eine sichere Verbindung und vollständige Kontrolle für Benutzer zu gewährleisten. Damit können Firewall-Regeln wie Port Forwarding, Open Ports und DMZ konfiguriert werden.

[Klicken Sie hier, um mehr über die Firewall der GL.iNet-Router zu erfahren](../../interface_guide/firewall.md)

### Multi-WAN

Lesen Sie das Tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Lesen Sie das Tutorial [**LAN**](../../interface_guide/lan.md).

### DNS

Lesen Sie das Tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode

Lesen Sie das Tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Lesen Sie das Tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

Die Seite Mac Address hieß früher Mac Clone und wurde seit v4.2 in Mac Address umbenannt.

Lesen Sie das Tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### IGMP Snooping

Lesen Sie das Tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Lesen Sie das Tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet stellt regelmäßig Updates für die Firmware unserer Router bereit, um die Leistung zu verbessern, Fehler zu beheben und Sicherheitslücken zu schließen.

Lesen Sie das Tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### OLED-Bildschirmeinstellungen

Auf dieser Seite können Sie festlegen, welche Informationen auf dem OLED-Bildschirm Ihres Mudi V2 (GL-E750V2) angezeigt werden.

### Scheduled Tasks

Lesen Sie das Tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Diese Funktion wurde seit v4.5 nach [**Security**](../../interface_guide/security.md) verschoben.

Lesen Sie das Tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Lesen Sie das Tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings

Lesen Sie das Tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Lesen Sie das Tutorial [**Log**](../../interface_guide/log.md).

### Reset Firmware

Lesen Sie das Tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Lesen Sie das Tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
