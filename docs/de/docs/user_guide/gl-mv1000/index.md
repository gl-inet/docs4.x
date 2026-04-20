# Brume (GL-MV1000) Benutzerhandbuch

## Produktübersicht

Brume (GL-MV1000) and Brume-W (GL-MV1000W) are powerful and stable networking products designed to do cutting-edge computing. With the Marvell high-performance chipset, the Brume and Brume-W* can run state-of-the-art cryptography at impressive speeds for an excellent VPN routing experience. Pre-installed OpenWrt and supported Ubuntu, Brume and Brume-W* allows in-depth developments for commercial IoT projects.

Brume-W (GL-MV1000W) is the special edition of Brume (GL-MV1000) that comes with an embedded Wi-Fi module, which delivers high-speed Wi-Fi performance on 2.4GHz Wi-Fi with up to 300Mbps Wi-Fi speed.

## Technische Daten

[GL-MV1000 specifications](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## Erste Einrichtung

All GL.iNet routers have a similar setup process. [Click here to learn about the first time-setup](../../faq/first_time_setup.md/).

---

## INTERNET

Melden Sie sich im Web-Admin-Panel des Routers an und wechseln Sie im linken Menü zu **INTERNET**.

Auf dieser Seite können Sie je nach Modell Ihre Internetverbindungsart auswählen, z. B. Ethernet, Repeater, Tethering und Cellular.

For Brume (GL-MV1000), it supports three types of connection type: Ethernet, Tethering, and Cellular.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Klicken Sie hier, um zu erfahren, wie Sie über ein Ethernet-Kabel eine Internetverbindung herstellen](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering

Connect the router's USB port to a smartphone with active mobile data via a USB cable to access the Internet. This method enables multiple devices connected to the router to access the internet using the smartphone's mobile data.

[Klicken Sie hier, um zu erfahren, wie Sie über USB-Tethering eine Internetverbindung herstellen](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular
 
Connect the router to the internet by plugging a cellular-enabled USB modem into the router's USB port. This method is useful for sharing internet from a USB modem to all connected devices.

[Klicken Sie hier, um zu erfahren, wie Sie über ein USB-Modem eine Internetverbindung herstellen](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen (z. B. Ethernet und Repeater) konfigurieren können. Wenn die Internetverbindung mit der höchsten Priorität ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. Dies wird auch als Failover bezeichnet und sorgt für einen reibungslosen und unterbrechungsfreien Internetzugang.

Wechseln Sie zu [Multi-WAN](../../interface_guide/multi-wan.md), um die Priorität jeder Internetverbindung festzulegen.

Alternativ können Sie den Multi-WAN-Modus von Failover auf Load Balance umstellen. Dadurch können Sie mehrere Netzwerkschnittstellen gleichzeitig nutzen, um die Gesamtbandbreite des Routers zu erhöhen.

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

### Network Storage

Lesen Sie das Tutorial [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home

Lesen Sie das Tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control

Lesen Sie das Tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier

Lesen Sie das Tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale

Lesen Sie das Tutorial [**Tailscale**](../../interface_guide/tailscale.md).

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

### Toggle Button Settings

Lesen Sie das Tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Lesen Sie das Tutorial [**Log**](../../interface_guide/log.md).

### Security

Diese Funktion ist seit v4.5 verfügbar.

Lesen Sie das Tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware

Lesen Sie das Tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Lesen Sie das Tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
