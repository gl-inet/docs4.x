# LAN

Gehen Sie auf der linken Seite des webbasierten Admin Panels zu **NETWORK** -> **LAN**.

Das LAN ist das Netzwerk, mit dem Ihr Gerät verbunden ist, wenn es über das Haupt-WLAN oder per Ethernet-Kabel angeschlossen ist.

Es umfasst die Basic Settings, die DHCP-Server-Einstellungen und die Address Reservation.

## Basic Settings

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    Dies ist die Adresse, die Sie in die Adresszeile Ihres Browsers eingeben, um die Administrationsseite des Routers aufzurufen.

    Standardmäßig lautet sie **192.168.8.1**. Sie können sie ändern, wenn sie mit Ihrem Netzwerk in Konflikt steht.

- **Netmask**
    
    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** wählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **AP Isolation**

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

## DHCP Server

Der **DHCP Server** ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch IP-Adressen und andere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie eine statische IP manuell konfigurieren.

Sie können die Start- und End-IP-Adresse an Ihre Anforderungen anpassen, zum Beispiel wenn Ihr Netzwerk wächst oder kleiner wird, wenn IP-Adresskonflikte auftreten oder wenn sich der Bereich der Subnetzmaske ändert.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: Der Zeitraum, für den eine vom DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1**: Der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2**: Der sekundäre Server, der zur Domainauflösung verwendet wird, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server**: (Line Printer Remote Server) Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckanforderungen an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

## Address Reservation

Wenn Sie für einen Client im LAN eine reservierte IP-Adresse festlegen, erhält der Client jedes Mal dieselbe IP-Adresse, wenn er den DHCP-Server des Routers nutzt. Sie können reservierte IP-Adressen an Computer oder Server vergeben, die dauerhaft feste IP-Einstellungen benötigen.

**Hinweis:** Konfigurierte Clients müssen die Verbindung zum Router neu herstellen, damit die Einstellung wirksam wird.

Klicken Sie auf **Add**, um eine IP zu reservieren.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Es erscheint ein Pop-up-Fenster.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Wählen Sie die **MAC** aus der Dropdown-Liste aus; die zur ausgewählten MAC gehörende **IP** wird automatisch eingetragen. Vergeben Sie einen aussagekräftigen Namen und klicken Sie dann auf **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Nach dem Hinzufügen einer neuen IP-Adressreservierung wird die unten gezeigte Seite angezeigt. Das bedeutet, dass die Einrichtung erfolgreich war.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
