# GL-S200 Benutzerhandbuch

## Produktübersicht

GL-S200 is a miniaturized Thread gateway supporting BLE protocol that runs on a highly customizable OpenWrt operating system and supports cloud device management. It has a versatile design for connecting to various smart home devices, or mass device connectivity for smart buildings.

![gl-s200 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

## Lieferumfang

Bitte beachten Sie, dass der im Lieferumfang enthaltene Adapter vom Zielland abhängt.

Der Lieferumfang umfasst:

- 1 x Benutzerhandbuch
- 1 x GL-S200
- 1 x Ethernet-Kabel
- 1 x Dankeskarte
- 1 x Garantiekarte
- 1 x Netzadapter (ausgewählter Steckertyp)

![gl-s200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

Sehen Sie sich das [Unboxing-Video](../../video_library/unboxing_first_set_up.md#gl-s200) von GL-S200 an.

## Technische Daten

[GL-S200 specifications](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

## PCB-Pinbelegung

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="gl-s200 pinout" loading="lazy" />
    </a>
  </figure>
</div>

## GL Thread Dev Board Pinbelegung

![gl thread dev board pinout](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## Erste Einrichtung

Alle GL.iNet-Router haben einen ähnlichen Einrichtungsprozess. [Klicken Sie hier, um mehr über die erste Einrichtung zu erfahren](../../faq/first_time_setup.md/).

---

## INTERNET

Melden Sie sich im Web-Admin-Panel des Routers an und wechseln Sie im linken Menü zu **INTERNET**.

Auf dieser Seite können Sie je nach Modell Ihre Internetverbindungsart auswählen, z. B. Ethernet, Repeater, Tethering und Cellular.

Beim GL-S200 werden zwei Verbindungsarten unterstützt: Ethernet und Repeater.

### Ethernet

Connect your router to an active modem or an active network device via an Ethernet cable to access the Internet. This method usually provides the fastest and most reliable Internet connection.

[Klicken Sie hier, um zu erfahren, wie Sie über ein Ethernet-Kabel eine Internetverbindung herstellen](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### Repeater

Set up your router as a repeater to extend the Wi-Fi coverage of an existing Wi-Fi network. As a repeater, it receives and retransmits wireless signals within its range, thereby extending its coverage. This method is useful when a single router cannot cover the entire usage area.

[Klicken Sie hier, um zu erfahren, wie Sie über ein vorhandenes Wi-Fi eine Internetverbindung herstellen](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen (z. B. Ethernet und Repeater) konfigurieren können. Wenn die Internetverbindung mit der höchsten Priorität ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. Dies wird auch als Failover bezeichnet und sorgt für einen reibungslosen und unterbrechungsfreien Internetzugang.

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

## Thread Mesh

Informationen zu [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) finden Sie in den IoT-Dokumenten.

---

## GL Dev Board

Informationen zu [GL Dev Board](https://docs.gl-inet.com/iot/en/iot_dev_board/) finden Sie in den IoT-Dokumenten.

---

## Bluetooth

Informationen zu [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) finden Sie in den IoT-Dokumenten.

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
