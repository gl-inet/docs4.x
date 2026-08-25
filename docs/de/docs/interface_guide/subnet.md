# Subnetz

**Hinweis**: Diese Seite ist derzeit auf Flint 4 (GL-BE14000) verfügbar und wird mit Firmware v4.10 auf weitere Modelle ausgerollt.

---

Gehen Sie auf der linken Seite des webbasierten Admin Panels zu **NETWORK** -> **Subnet**.

Diese Seite fasst die Konfiguration von **LAN**, **Guest Network**, **IoT Network** und benutzerdefinierten **VLAN Networks** in einer gemeinsamen Ansicht zusammen. Sie bietet eine zentrale Verwaltungsoberfläche für alle subnetzbezogenen Einstellungen, sodass Sie mehrere Subnetze erstellen und verwalten können, um verschiedene Gerätetypen oder Datenverkehr voneinander zu trennen.

## Hauptnetzwerk

**Main Network** ist das Netzwerk, mit dem Ihr Gerät über das Haupt-Wi-Fi oder per Ethernet-Kabel verbunden ist.

Im Main Network können Sie direkt alle Schnittstellenstatus, die VLAN ID, die Router-IP-Adresse und den DHCP-Bereich anzeigen.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**, um das Main Network zu konfigurieren.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

Die Konfigurationsseite enthält Basic settings, DHCP server settings und Address Reservation.

### Basic Settings

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Dies ist die Adresse, die Sie in die Adresszeile Ihres Browsers eingeben, um die Administrationsseite des Routers aufzurufen.

    Standardmäßig lautet sie **192.168.8.1**. Sie können sie ändern, wenn sie mit Ihrem Netzwerk in Konflikt steht.

- **Netmask**

    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** auswählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **VLAN ID**

    Die Standard-VLAN ID des Main Network ist **1** und kann nicht geändert werden.

- **AP Isolation**

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

### DHCP Server

Der **DHCP Server** ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch IP-Adressen und andere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie eine statische IP manuell konfigurieren.

Sie können die Start- und End-IP-Adresse an Ihre Anforderungen anpassen, zum Beispiel wenn Ihr Netzwerk wächst oder kleiner wird, wenn IP-Adresskonflikte auftreten oder wenn sich der Bereich der Subnetzmaske ändert.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Der Zeitraum, für den eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server**: Zwei DNS-Server-Felder stehen zur Konfiguration des primären und sekundären Resolvers zur Verfügung.

    **Hinweis**: Der primäre DNS wird im oberen Feld und der sekundäre DNS im unteren Feld eingegeben. Wenn der primäre Server nicht verfügbar ist, wechseln Client-Geräte automatisch zum sekundären Resolver, sodass die Domainnamenauflösung weiter funktioniert.

- **LPR Server** (Line Printer Remote Server): Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckanforderungen an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

### Address Reservation

Wenn Sie für einen Client im LAN eine reservierte IP-Adresse festlegen, erhält der Client jedes Mal dieselbe IP-Adresse, wenn er auf den DHCP-Server des Routers zugreift. Sie können reservierte IP-Adressen Computern oder Servern zuweisen, die dauerhafte IP-Einstellungen benötigen.

**Hinweis:** Konfigurierte Clients müssen die Verbindung zum Router neu herstellen, damit die Einstellung wirksam wird.

Klicken Sie auf **Add**, um eine IP zu reservieren.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Es erscheint ein Pop-up-Fenster.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Wählen Sie **MAC** aus der Dropdown-Liste aus. Die passende verfügbare **IP** wird automatisch eingetragen. Optional können Sie einen **hostname** und einen benutzerdefinierten **name** zur leichteren Identifizierung eingeben. Klicken Sie anschließend auf **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Nach dem Hinzufügen einer neuen IP-Adressreservierung wird die unten gezeigte Seite angezeigt. Das bedeutet, dass die Einrichtung erfolgreich war.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Gastnetzwerk

Das **Guest Network** stellt ein dediziertes Wi-Fi-Netzwerk für Besucher bereit. Es ist vom primären Netzwerk getrennt, erhöht dadurch die Sicherheit und bietet gleichzeitig bequemen Internetzugang.

**Hinweis**: Einige Modelle (z. B. GL-MT5000, GL-MT2500/GL-MT2500A) verfügen über keine Wi-Fi-Funktion. Daher sind die Guest Network-Einstellungen in deren webbasiertem Admin Panel nicht verfügbar.

Im Guest Network können Sie direkt den Schnittstellenstatus, die VLAN ID, das Gateway und den DHCP-Bereich anzeigen.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Das Konfigurationspanel für Guest Network wird rechts auf der Seite geöffnet.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

Die Konfigurationsseite enthält Basic settings und DHCP server settings.

### Basic Settings

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    Das **Standard-Gateway** des Guest Network ist **192.168.9.1**. Wenn dies mit Ihrem lokalen Netzwerk in Konflikt steht, ändern Sie es auf eine andere Adresse.

- **Netmask**

    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** auswählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **VLAN ID**

    Die Standard-VLAN ID des Guest Network ist **9** und kann bei Bedarf geändert werden.

- **AP Isolation**

    Diese Funktion ist seit Firmware v4.5 verfügbar.

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

- **WAN Access Control**

    WAN Access Control verwaltet den Zugriff des lokalen Subnetzes auf WAN-seitige Netzwerke, einschließlich Internet und anderer WAN-Subnetze.

    Drei WAN-Zugriffssteuerungsmodi sind verfügbar:

    - **Unrestricted**: Erlaubt diesem Subnetz den Zugriff auf das Internet und andere WAN-seitige Subnetze ohne Einschränkungen.

    - **Block WAN Subnet**: Blockiert den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access**: Blockiert sämtlichen ausgehenden Zugriff, einschließlich Internet und WAN-seitiger Subnetze.

### DHCP Server

Der **DHCP Server** ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch IP-Adressen und andere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie eine statische IP manuell konfigurieren.

Sie können die Start- und End-IP-Adresse an Ihre Anforderungen anpassen, zum Beispiel wenn Ihr Netzwerk wächst oder kleiner wird, wenn IP-Adresskonflikte auftreten oder wenn sich der Bereich der Subnetzmaske ändert.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Der Zeitraum, für den eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server**: Zwei DNS-Server-Felder stehen zur Konfiguration des primären und sekundären Resolvers zur Verfügung.

    **Hinweis**: Der primäre DNS wird im oberen Feld und der sekundäre DNS im unteren Feld eingegeben. Wenn der primäre Server nicht verfügbar ist, wechseln Client-Geräte automatisch zum sekundären Resolver, sodass die Domainnamenauflösung weiter funktioniert.

- **LPR Server** (Line Printer Remote Server): Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckanforderungen an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

## IoT Network

IoT Network erstellt ein dediziertes Wi-Fi-Netzwerk für IoT-Geräte. Es ist vom primären Netzwerk getrennt und bietet bessere Kompatibilität sowie höhere Sicherheit.

**Hinweis**: Einige Modelle (z. B. GL-MT5000, GL-MT2500/GL-MT2500A) verfügen über keine Wi-Fi-Funktion. Daher sind die IoT Network-Einstellungen in deren webbasiertem Admin Panel nicht verfügbar.

Im IoT Network können Sie direkt den Schnittstellenstatus, die VLAN ID, das Gateway und den DHCP-Bereich anzeigen.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Das Konfigurationspanel für IoT Network wird rechts auf der Seite geöffnet. In diesem Panel können Sie Basic Settings und DHCP Server Settings konfigurieren.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Basic Settings

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    Das **Standard-Gateway** des IoT Network ist **192.168.10.1**. Wenn dies mit Ihrem lokalen Netzwerk in Konflikt steht, ändern Sie es auf eine andere Adresse.

- **Netmask**

    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** auswählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **VLAN ID**

    Die Standard-VLAN ID des IoT Network ist **10** und kann bei Bedarf geändert werden.

- **AP Isolation**

    Diese Funktion ist seit Firmware v4.5 verfügbar.

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

- **WAN Access Control**

    WAN Access Control verwaltet den Zugriff des lokalen Subnetzes auf WAN-seitige Netzwerke, einschließlich Internet und anderer WAN-Subnetze.

    Drei WAN-Zugriffssteuerungsmodi sind verfügbar:

    - **Unrestricted**: Erlaubt diesem Subnetz den Zugriff auf das Internet und andere WAN-seitige Subnetze ohne Einschränkungen.

    - **Block WAN Subnet**: Blockiert den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access**: Blockiert sämtlichen ausgehenden Zugriff, einschließlich Internet und WAN-seitiger Subnetze.

### DHCP Server

Der **DHCP Server** ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch IP-Adressen und andere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie eine statische IP manuell konfigurieren.

Sie können die Start- und End-IP-Adresse an Ihre Anforderungen anpassen, zum Beispiel wenn Ihr Netzwerk wächst oder kleiner wird, wenn IP-Adresskonflikte auftreten oder wenn sich der Bereich der Subnetzmaske ändert.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Der Zeitraum, für den eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server**: Zwei DNS-Server-Felder stehen zur Konfiguration des primären und sekundären Resolvers zur Verfügung.

    **Hinweis**: Der primäre DNS wird im oberen Feld und der sekundäre DNS im unteren Feld eingegeben. Wenn der primäre Server nicht verfügbar ist, wechseln Client-Geräte automatisch zum sekundären Resolver, sodass die Domainnamenauflösung weiter funktioniert.

- **LPR Server** (Line Printer Remote Server): Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckanforderungen an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

## VLAN Networks

Oben auf der Hauptseite können Sie bei Bedarf zusätzliche **VLAN networks** erstellen, um verschiedene Gerätetypen oder Besucherdatenverkehr voneinander zu trennen.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Klicken Sie rechts auf der Seite auf **+ Add**, um ein neues Netzwerk zu konfigurieren.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Basic Settings

Auf dieser Seite können Sie die grundlegenden Informationen für **VLAN Networks** konfigurieren.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Legen Sie einen Namen für das neu erstellte Subnetz fest, um es leichter zu identifizieren.

- **Gateway**

    Konfigurieren Sie das Gateway für das neue Subnetz manuell. Ändern Sie dieses Gateway, wenn es mit Ihrem vorhandenen LAN-Segment in Konflikt steht.

- **Netmask**

    Standardmäßig ist **255.255.255.0** eingestellt. Sie können auch **255.255.0.0** auswählen, wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen.

- **VLAN ID**

    Beim Erstellen eines Subnetzes müssen Sie eine VLAN ID zwischen **9** und **4000** zuweisen. Verwenden Sie keine bereits belegte VLAN ID, um Netzwerkkonflikte zu vermeiden.

- **AP Isolation**

    Diese Funktion ist seit Firmware v4.5 verfügbar.

    Sie können Client-Geräte in ein separates Netzwerksegment isolieren. Diese Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

- **WAN Access Control**

    WAN Access Control verwaltet den Zugriff des lokalen Subnetzes auf WAN-seitige Netzwerke, einschließlich Internet und anderer WAN-Subnetze.

    Drei WAN-Zugriffssteuerungsmodi sind verfügbar:

    - **Unrestricted**: Erlaubt diesem Subnetz den Zugriff auf das Internet und andere WAN-seitige Subnetze ohne Einschränkungen.

    - **Block WAN Subnet**: Blockiert den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access**: Blockiert sämtlichen ausgehenden Zugriff, einschließlich Internet und WAN-seitiger Subnetze.

### DHCP Server

Der **DHCP Server** ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch IP-Adressen und andere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen für Client-Geräte manuell konfigurieren. Klicken Sie [hier](../tutorials/manually_configure_static_ip.md), um zu erfahren, wie Sie eine statische IP manuell konfigurieren.

Sie können die Start- und End-IP-Adresse an Ihre Anforderungen anpassen, zum Beispiel wenn Ihr Netzwerk wächst oder kleiner wird, wenn IP-Adresskonflikte auftreten oder wenn sich der Bereich der Subnetzmaske ändert.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Der Zeitraum, für den eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway**: Das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server**: Zwei DNS-Server-Felder stehen zur Konfiguration des primären und sekundären Resolvers zur Verfügung.

    **Hinweis**: Der primäre DNS wird im oberen Feld und der sekundäre DNS im unteren Feld eingegeben. Wenn der primäre Server nicht verfügbar ist, wechseln Client-Geräte automatisch zum sekundären Resolver, sodass die Domainnamenauflösung weiter funktioniert.

- **LPR Server** (Line Printer Remote Server): Ein Dienst, der Druckaufträge verwaltet und es Netzwerkgeräten ermöglicht, Druckanforderungen an entfernte Drucker zu senden. Es können mehrere LPR-Druckerports konfiguriert werden.

Nach der Konfiguration wird das neue VLAN-Netzwerk auf der aktuellen Seite mit den Subnetzinformationen angezeigt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

