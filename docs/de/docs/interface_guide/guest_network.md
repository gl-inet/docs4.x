# Gastnetzwerk

Die Einstellungen für das Gastnetzwerk wurden seit Firmware v4.5 von [LAN](lan.md) getrennt.

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **Guest Network**. 

Diese Seite enthält die Grundeinstellungen des Gastnetzwerks sowie die DHCP-Server-Einstellungen.

## Grundeinstellungen

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche festlegen: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

Sie können ein separates, isoliertes Netzwerk für temporäre Benutzer einrichten, das nur eingeschränkten Zugriff bietet und die Sicherheit erhöht, da es vom primären Netzwerk getrennt ist.

**Hinweis**: Einige Modelle (z. B. GL-MT5000, GL-MT2500/GL-MT2500A) unterstützen kein Wi-Fi. Daher sind die Einstellungen für das Gastnetzwerk in deren Web-Admin-Panel nicht verfügbar.

- **Gateway**

    Das **Standard-Gateway** des Gastnetzwerks ist **192.168.9.1**. Wenn dies mit Ihrem lokalen Netzwerk in Konflikt steht, ändern Sie es auf eine andere Adresse.

- **Netmask**
    
    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** auswählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **AP Isolation**

    Diese Funktion ist seit Firmware v4.5 verfügbar.

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

- **Block WAN Subnets**

    Diese Funktion ist seit Firmware v4.8 verfügbar.

    Wenn sie aktiviert ist, kann das Gastnetzwerk nicht auf das Upstream-Netzwerk und dessen Subnetz zugreifen.

## DHCP-Server

Wenn das Gastnetzwerk aktiviert ist, wird der DHCP-Server standardmäßig ebenfalls aktiviert.

Der DHCP-Server weist allen mit dem Gastnetzwerk verbundenen Client-Geräten automatisch IP-Adressen und andere Kommunikationsparameter zu. Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie manuell eine statische IP konfigurieren.

Sie können die Start- und End-IP-Adressen an Ihre Anforderungen anpassen – zum Beispiel, wenn Ihr Netzwerk wächst oder kleiner wird, IP-Adresskonflikte auftreten oder der Bereich der Subnetzmaske geändert wird.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Klicken Sie bei Bedarf auf **Advanced** für weitere Konfigurationen.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: Der Zeitraum, für den eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem Gastnetzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1**: Der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2**: Der sekundäre Server, der zur Domainnamenauflösung verwendet wird, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server**: (Line Printer Remote Server) Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckaufträge an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

---

Verwandte Artikel:

- [So richten Sie ein Gast-Wi-Fi-Netzwerk auf GL.iNet-Routern ein](../tutorials/how_to_set_up_a_guest_network.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
