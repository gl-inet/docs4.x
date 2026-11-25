# LAN {#lan}

**Hinweis**: Diese Anleitung gilt ab Firmware v4.11. Wenn auf Ihrem Gerät eine andere Firmware-Version installiert ist, wählen Sie unten die passende Anleitung aus.

<div class="gl-link-select" data-label="Firmwareversion" data-placeholder="Firmware v4.11 und höher" markdown="1">

- [Firmware v4.9 und früher](lan.md)

</div>

---

Öffnen Sie links im Web-Admin-Panel **NETWORK** -> **LAN**.

Auf dieser Seite können Sie das Hauptnetzwerk (**Main Network**), das Gastnetzwerk (**Guest Network**), das **IoT Network** und benutzerdefinierte VLANs (**VLAN Networks**) konfigurieren und verwalten. Erstellen und verwalten Sie mehrere Subnetze, um verschiedene Gerätetypen oder Arten von Datenverkehr voneinander zu trennen.

## Hauptnetzwerk {#main-network}

Mit dem Hauptnetzwerk verbinden Sie Ihr Gerät über das Haupt-WLAN oder ein Ethernet-Kabel.

Die Übersicht des Hauptnetzwerks zeigt den Status aller Schnittstellen, die VLAN-ID, die IP-Adresse des Routers und den DHCP-Adressbereich.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**, um das Hauptnetzwerk zu konfigurieren.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

Auf der Konfigurationsseite finden Sie die Grundeinstellungen, die DHCP-Server-Einstellungen und die Adressreservierung.

### Grundeinstellungen {#basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Geben Sie diese Adresse in die Adresszeile Ihres Browsers ein, um das Web-Admin-Panel des Routers zu öffnen.

    Die Standardadresse lautet **192.168.8.1**. Bei einem Konflikt mit Ihrem Netzwerk können Sie sie ändern.

- **Netmask**

    Die Standardnetzmaske lautet **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die VLAN-ID des Hauptnetzwerks ist fest auf **1** eingestellt.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Die isolierten Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis**: **AP Isolation** gilt ausschließlich für WLAN-Clients.

### DHCP-Server {#dhcp-server}

Der **DHCP Server** ist standardmäßig aktiviert und weist jedem Client automatisch eine IP-Adresse und weitere Netzwerkparameter zu.

Bei deaktiviertem DHCP-Server müssen Sie die Netzwerkeinstellungen der Clients manuell konfigurieren. Folgen Sie dazu der Anleitung zum [manuellen Einrichten einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Adressbereichs anpassen, etwa wenn sich die Netzwerkgröße oder die Subnetzmaske ändert oder IP-Adresskonflikte auftreten.

![main network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange die per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** löst Domainnamen auf, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Aufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

### Adressreservierung {#address-reservation}

Wenn Sie eine IP-Adresse für einen Client im LAN reservieren, weist ihm der DHCP-Server des Routers bei jeder Anfrage dieselbe Adresse zu. Sie können IP-Adressen für Computer oder Server reservieren, die dauerhaft feste IP-Einstellungen benötigen.

**Hinweis**: Die betreffenden Clients müssen die Verbindung zum Router neu herstellen, damit die Reservierung wirksam wird.

Klicken Sie auf **Add**, um eine IP-Adresse zu reservieren.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Ein Dialogfenster öffnet sich.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Wählen Sie unter **MAC** eine Adresse aus der Dropdown-Liste aus. Eine passende freie **IP** wird automatisch eingetragen. Zur leichteren Identifizierung können Sie optional einen Hostnamen (**hostname**) und einen eigenen Namen (**name**) eingeben. Klicken Sie anschließend auf **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Nach erfolgreicher Einrichtung erscheint die neue Adressreservierung wie unten gezeigt in der Übersicht.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Gastnetzwerk {#guest-network}

Das Gastnetzwerk stellt Besuchern ein eigenes WLAN mit Internetzugang zur Verfügung. Es ist aus Sicherheitsgründen vom Hauptnetzwerk getrennt.

**Hinweis**: Bei Modellen ohne WLAN, etwa GL-MT5000 und GL-MT2500/GL-MT2500A, sind die Einstellungen für das Gastnetzwerk im Web-Admin-Panel nicht verfügbar.

Die Übersicht des Gastnetzwerks zeigt den Status der Schnittstelle, die VLAN-ID, das Gateway und den DHCP-Adressbereich.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Die Einstellungen für das Gastnetzwerk öffnen sich auf der rechten Seite.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

Auf der Konfigurationsseite finden Sie die Grundeinstellungen und die DHCP-Server-Einstellungen.

### Grundeinstellungen {#guest-network-basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Das Standardgateway des Gastnetzwerks lautet **192.168.9.1**. Weisen Sie dem Gateway bei einem Konflikt mit Ihrem lokalen Netzwerk eine andere Adresse zu.

- **Netmask**

    Die Standardnetzmaske lautet **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die VLAN-ID des Gastnetzwerks ist standardmäßig **9**. Sie können sie bei Bedarf ändern.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die Sie per Kabel mit diesen Ports verbinden, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Die isolierten Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis**: **AP Isolation** gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Mit **WAN Access Control** legen Sie fest, ob das lokale Subnetz auf das Internet und andere WAN-seitige Subnetze zugreifen darf.

    Sie können zwischen drei Einstellungen wählen.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt sämtliche ausgehenden Verbindungen, einschließlich des Zugriffs auf das Internet und WAN-seitige Subnetze.

### DHCP-Server {#guest-network-dhcp-server}

Der **DHCP Server** ist standardmäßig aktiviert und weist jedem Client automatisch eine IP-Adresse und weitere Netzwerkparameter zu.

Bei deaktiviertem DHCP-Server müssen Sie die Netzwerkeinstellungen der Clients manuell konfigurieren. Folgen Sie dazu der Anleitung zum [manuellen Einrichten einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Adressbereichs anpassen, etwa wenn sich die Netzwerkgröße oder die Subnetzmaske ändert oder IP-Adresskonflikte auftreten.

![guest network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange die per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** löst Domainnamen auf, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Aufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

## IoT-Netzwerk {#iot-network}

Das IoT-Netzwerk stellt ein eigenes WLAN für IoT-Geräte bereit. Es ist vom Hauptnetzwerk getrennt und bietet bessere Kompatibilität und höhere Sicherheit.

**Hinweis**: Bei Modellen ohne WLAN, etwa GL-MT5000 und GL-MT2500/GL-MT2500A, sind die Einstellungen für das IoT-Netzwerk im Web-Admin-Panel nicht verfügbar.

Die Übersicht des IoT-Netzwerks zeigt den Status der Schnittstelle, die VLAN-ID, das Gateway und den DHCP-Adressbereich.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Auf der rechten Seite öffnen sich die Grundeinstellungen und die DHCP-Server-Einstellungen für das IoT-Netzwerk.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Grundeinstellungen {#iot-network-basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Das Standardgateway des IoT-Netzwerks lautet **192.168.10.1**. Weisen Sie dem Gateway bei einem Konflikt mit Ihrem lokalen Netzwerk eine andere Adresse zu.

- **Netmask**

    Die Standardnetzmaske lautet **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die VLAN-ID des IoT-Netzwerks ist standardmäßig **10**. Sie können sie bei Bedarf ändern.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die Sie per Kabel mit diesen Ports verbinden, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Die isolierten Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis**: **AP Isolation** gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Mit **WAN Access Control** legen Sie fest, ob das lokale Subnetz auf das Internet und andere WAN-seitige Subnetze zugreifen darf.

    Sie können zwischen drei Einstellungen wählen.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt sämtliche ausgehenden Verbindungen, einschließlich des Zugriffs auf das Internet und WAN-seitige Subnetze.

### DHCP-Server {#iot-network-dhcp-server}

Der **DHCP Server** ist standardmäßig aktiviert und weist jedem Client automatisch eine IP-Adresse und weitere Netzwerkparameter zu.

Bei deaktiviertem DHCP-Server müssen Sie die Netzwerkeinstellungen der Clients manuell konfigurieren. Folgen Sie dazu der Anleitung zum [manuellen Einrichten einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Adressbereichs anpassen, etwa wenn sich die Netzwerkgröße oder die Subnetzmaske ändert oder IP-Adresskonflikte auftreten.

![iot network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange die per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** löst Domainnamen auf, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Aufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

## VLAN-Netzwerke {#vlan-networks}

Oben auf der Seite können Sie bei Bedarf zusätzliche VLANs erstellen, um verschiedene Gerätetypen oder den Datenverkehr von Gästen getrennt zu halten.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Klicken Sie rechts auf **+ Add**, um ein neues Netzwerk zu konfigurieren.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Grundeinstellungen {#vlan-networks-basic-settings}

Auf dieser Seite können Sie die Grundeinstellungen des VLANs festlegen.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Vergeben Sie einen Namen, unter dem Sie das neue Subnetz leicht wiederfinden.

- **Gateway**

    Legen Sie das Gateway des neuen Subnetzes manuell fest. Wählen Sie bei einem Konflikt mit dem vorhandenen LAN-Segment eine andere Gateway-Adresse.

- **Netmask**

    Die Standardnetzmaske lautet **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Weisen Sie dem neuen Subnetz eine VLAN-ID zwischen **9** und **4000** zu. Wählen Sie eine freie ID, um Netzwerkkonflikte zu vermeiden.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die Sie per Kabel mit diesen Ports verbinden, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Die isolierten Geräte können dann nicht mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis**: **AP Isolation** gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Mit **WAN Access Control** legen Sie fest, ob das lokale Subnetz auf das Internet und andere WAN-seitige Subnetze zugreifen darf.

    Sie können zwischen drei Einstellungen wählen.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt sämtliche ausgehenden Verbindungen, einschließlich des Zugriffs auf das Internet und WAN-seitige Subnetze.

### DHCP-Server {#vlan-networks-dhcp-server}

Der **DHCP Server** ist standardmäßig aktiviert und weist jedem Client automatisch eine IP-Adresse und weitere Netzwerkparameter zu.

Bei deaktiviertem DHCP-Server müssen Sie die Netzwerkeinstellungen der Clients manuell konfigurieren. Folgen Sie dazu der Anleitung zum [manuellen Einrichten einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Adressbereichs anpassen, etwa wenn sich die Netzwerkgröße oder die Subnetzmaske ändert oder IP-Adresskonflikte auftreten.

![vlan networks dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange die per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** löst Domainnamen auf, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Aufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

Nach der Einrichtung erscheint das neue VLAN mit seinen Subnetzdaten in der Übersicht.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
