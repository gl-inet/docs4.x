# Spitz (GL-X750) Benutzerhandbuch

## Produktübersicht

Spitz is a 3G/4G dual-band wireless router, widely used for smart home and IoT area. Running OpenWRT OS, you can compile your own firmware to fit for different application scenarios. It has built-in mini PCIe 3G/4G module to support different operators and can be used all over the world.

Spitz V2 (GL-X750V2) is the advanced version of Spitz (GL-X750). It comes with the redesigned PCBA and optimized antennas to improve the 4G performance.

![gl-x750 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/x750v2_interface.jpg){class="glboxshadow"}

## Technische Daten

[GL-X750 specifications](https://www.gl-inet.com/products/gl-x750/#specs){target="_blank"}

---

## Erste Einrichtung

Alle GL.iNet-Router haben einen ähnlichen Einrichtungsprozess. [Klicken Sie hier, um mehr über die erste Einrichtung zu erfahren](../../faq/first_time_setup.md/).

---

## INTERNET

Melden Sie sich im Web-Admin-Panel des Routers an und wechseln Sie im linken Menü zu **INTERNET**.

Auf dieser Seite können Sie Ihre Internetverbindungsart auswählen, z. B. Ethernet, Repeater, Tethering und Cellular.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Klicken Sie hier, um zu erfahren, wie Sie über ein Ethernet-Kabel eine Internetverbindung herstellen](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_ethernet.png){class="glboxshadow"}

### Repeater

Set up your router as a repeater to extend the Wi-Fi coverage of an existing Wi-Fi network. As a repeater, it receives and retransmits wireless signals within its range, thereby extending its coverage. This method is useful when a single router cannot cover the entire usage area.

[Klicken Sie hier, um zu erfahren, wie Sie über ein vorhandenes Wi-Fi eine Internetverbindung herstellen](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_repeater.png){class="glboxshadow"}

### Tethering

Connect the router's USB port to a smartphone with active mobile data via a USB cable to access the Internet. This method enables multiple devices connected to the router to access the internet using the smartphone's mobile data.

[Klicken Sie hier, um zu erfahren, wie Sie über USB-Tethering eine Internetverbindung herstellen](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_tethering.png){class="glboxshadow"}

### Cellular
 
Insert a SIM card into the router's SIM card slot to connect it to the internet. This method is useful for sharing internet access from a single SIM card to all connected devices.

[Click here to learn how to connect to the internet via callular](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN is a networking feature that allows you to set up your router with multiple internet connections (e.g., Ethernet, Repeater, and Cellular) at the same time. If the top-priority internet connection fails, the router will automatically switch to another internet connection. This is also called Failover, ensuring smooth and uninterrupted internet access.

Wechseln Sie zu [Multi-WAN](../../interface_guide/multi-wan.md), um die Priorität jeder Internetverbindung festzulegen.

Alternativ können Sie den Multi-WAN-Modus von Failover auf Load Balance umstellen. Dadurch können Sie mehrere Netzwerkschnittstellen gleichzeitig nutzen, um die Gesamtbandbreite des Routers zu erhöhen.

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

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Detaillierte Schritt-für-Schritt-Anleitungen finden Sie unter den folgenden Links:

- [**OpenVPN-Client einrichten**](../../interface_guide/openvpn_client.md)
- [**OpenVPN-Server einrichten**](../../interface_guide/openvpn_server.md)

### WireGuard

Detaillierte Schritt-für-Schritt-Anleitungen finden Sie unter den folgenden Links:

- [**WireGuard-Client einrichten**](../../interface_guide/wireguard_client.md)
- [**WireGuard-Server einrichten**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

GL.iNet-Router bieten eine Vielzahl zusätzlicher Funktionen, die die Geräteverwaltung vereinfachen, das Interneterlebnis der Benutzer verbessern, Firmware-Updates automatisieren und vieles mehr.

### Plug-ins

Lesen Sie das Tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Lesen Sie das Tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Lesen Sie das Tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Parental Control

Lesen Sie das Tutorial [**Parental Control**](../../interface_guide/parental_control.md).

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

### Drop-in Gateway

Lesen Sie das Tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Lesen Sie das Tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Lesen Sie das Tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet stellt regelmäßig Updates für die Firmware unserer Router bereit, um die Leistung zu verbessern, Fehler zu beheben und Sicherheitslücken zu schließen.

Lesen Sie das Tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Lesen Sie das Tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Diese Funktion wurde seit v4.5 nach [**Security**](../../interface_guide/security.md) verschoben.

Lesen Sie das Tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Lesen Sie das Tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Lesen Sie das Tutorial [**Log**](../../interface_guide/log.md).

### Security

Diese Funktion ist seit v4.5 verfügbar.

Lesen Sie das Tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware

Lesen Sie das Tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Lesen Sie das Tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).

