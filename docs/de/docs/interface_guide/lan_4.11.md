# LAN {#lan}

**Hinweis:** Diese Anleitung gilt ab Firmware v4.11. Wenn auf Ihrem Gerät eine andere Firmware-Version installiert ist, wählen Sie unten die passende Anleitung aus.

<div class="gl-link-select" data-label="Firmware-Version" data-placeholder="Ab Firmware v4.11" markdown="1">

- [Firmware v4.9 und älter](lan.md)

</div>

---

Gehen Sie im linken Menü des webbasierten Admin Panels zu **NETWORK** -> **LAN**.

Auf dieser Seite konfigurieren und verwalten Sie zentral das Hauptnetzwerk (**Main Network**), das Gastnetzwerk (**Guest Network**), das IoT-Netzwerk (**IoT Network**) und benutzerdefinierte VLAN-Netzwerke (**VLAN Networks**). Sie können mehrere Subnetze erstellen und verwalten, um verschiedene Gerätetypen oder den jeweiligen Datenverkehr voneinander zu trennen.

## Hauptnetzwerk {#main-network}

Ihr Gerät stellt über das Haupt-WLAN oder ein Ethernet-Kabel eine Verbindung zum Hauptnetzwerk her.

Die Übersicht des Hauptnetzwerks zeigt den Status aller Schnittstellen, die VLAN-ID, die IP-Adresse des Routers und den DHCP-Adressbereich.

![Hauptnetzwerk 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**, um das Hauptnetzwerk zu konfigurieren.

![Hauptnetzwerk 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

Auf der Konfigurationsseite finden Sie die Grundeinstellungen, die Einstellungen des DHCP-Servers und die Adressreservierung.

### Grundeinstellungen {#basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![Hauptnetzwerk – Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Geben Sie diese Adresse in die Adresszeile Ihres Browsers ein, um die Administrationsseite des Routers zu öffnen.

    Die Standardadresse lautet **192.168.8.1**. Sie können sie ändern, falls sie einen Konflikt mit Ihrem Netzwerk verursacht.

- **Netmask**

    Die voreingestellte Netzmaske ist **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die VLAN-ID des Hauptnetzwerks ist fest auf **1** eingestellt.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Danach können diese Geräte nicht mehr mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis:** Die AP-Isolierung gilt ausschließlich für WLAN-Clients.

### DHCP-Server {#dhcp-server}

Der DHCP-Server ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch eine IP-Adresse und weitere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen auf den Client-Geräten manuell konfigurieren. Befolgen Sie dazu die [Anleitung zur manuellen Konfiguration einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Bereichs anpassen, etwa wenn sich die Größe Ihres Netzwerks ändert, IP-Adresskonflikte auftreten oder sich der durch die Subnetzmaske festgelegte Adressbereich ändert.

![Hauptnetzwerk – DHCP-Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![Hauptnetzwerk – erweiterte DHCP-Einstellungen 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Hauptnetzwerk – erweiterte DHCP-Einstellungen 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** übernimmt die Auflösung von Domainnamen, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Druckaufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

### Adressreservierung {#address-reservation}

Wenn Sie eine IP-Adresse für einen Client im LAN reservieren, erhält er bei jeder Anfrage an den DHCP-Server des Routers dieselbe IP-Adresse. Sie können IP-Adressen für Computer oder Server reservieren, die dauerhaft feste IP-Einstellungen benötigen.

**Hinweis:** Die Clients müssen die Verbindung zum Router neu herstellen, damit die Reservierung wirksam wird.

Klicken Sie auf **Add**, um eine IP-Adresse zu reservieren.

![Hauptnetzwerk – Adressreservierung 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Ein Dialogfenster öffnet sich.

![Hauptnetzwerk – Adressreservierung 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Wählen Sie unter **MAC** die MAC-Adresse aus der Dropdown-Liste aus. Die passende verfügbare IP-Adresse wird automatisch in das Feld **IP** eingetragen. Zur leichteren Identifizierung können Sie optional einen Hostnamen (**hostname**) und einen benutzerdefinierten Namen (**name**) eingeben. Klicken Sie anschließend auf **Submit**.

![Hauptnetzwerk – Adressreservierung 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Nach erfolgreicher Einrichtung erscheint die neue IP-Adressreservierung wie unten abgebildet.

![Hauptnetzwerk – Adressreservierung 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Gastnetzwerk {#guest-network}

Das Gastnetzwerk stellt Besuchern ein eigenes WLAN mit Internetzugang bereit. Die Trennung vom Hauptnetzwerk erhöht die Sicherheit.

**Hinweis:** Einige Modelle (z. B. GL-MT5000, GL-MT2500/GL-MT2500A) verfügen über kein WLAN. Daher bietet ihr webbasiertes Admin Panel keine Einstellungen für das Gastnetzwerk.

Die Übersicht des Gastnetzwerks zeigt den Schnittstellenstatus, die VLAN-ID, das Gateway und den DHCP-Adressbereich.

![Gastnetzwerk 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Die Einstellungen des Gastnetzwerks öffnen sich am rechten Seitenrand.

![Gastnetzwerk 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

Auf der Konfigurationsseite finden Sie die Grundeinstellungen und die Einstellungen des DHCP-Servers.

### Grundeinstellungen {#guest-network-basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![Gastnetzwerk – Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Das Standard-Gateway des Gastnetzwerks lautet **192.168.9.1**. Wählen Sie eine andere Adresse, falls sie einen Konflikt mit Ihrem lokalen Netzwerk verursacht.

- **Netmask**

    Die voreingestellte Netzmaske ist **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die Standard-VLAN-ID des Gastnetzwerks ist **9**. Sie können sie bei Bedarf ändern.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die per Kabel an diesen Ports angeschlossen sind, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Danach können diese Geräte nicht mehr mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis:** Die AP-Isolierung gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Die WAN-Zugriffssteuerung regelt den Zugriff des lokalen Subnetzes auf das Internet und auf andere WAN-seitige Subnetze.

    Für die WAN-Zugriffssteuerung stehen drei Modi zur Auswahl.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und auf andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt den gesamten ausgehenden Zugriff, einschließlich des Zugriffs auf das Internet und auf WAN-seitige Subnetze.

### DHCP-Server {#guest-network-dhcp-server}

Der DHCP-Server ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch eine IP-Adresse und weitere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen auf den Client-Geräten manuell konfigurieren. Befolgen Sie dazu die [Anleitung zur manuellen Konfiguration einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Bereichs anpassen, etwa wenn sich die Größe Ihres Netzwerks ändert, IP-Adresskonflikte auftreten oder sich der durch die Subnetzmaske festgelegte Adressbereich ändert.

![Gastnetzwerk – DHCP-Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![Gastnetzwerk – erweiterte DHCP-Einstellungen 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Gastnetzwerk – erweiterte DHCP-Einstellungen 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** übernimmt die Auflösung von Domainnamen, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Druckaufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

## IoT-Netzwerk {#iot-network}

Das IoT-Netzwerk stellt IoT-Geräten ein eigenes WLAN bereit. Es ist vom Hauptnetzwerk getrennt und bietet eine bessere Kompatibilität und höhere Sicherheit.

**Hinweis:** Einige Modelle (z. B. GL-MT5000, GL-MT2500/GL-MT2500A) verfügen über kein WLAN. Daher bietet ihr webbasiertes Admin Panel keine Einstellungen für das IoT-Netzwerk.

Die Übersicht des IoT-Netzwerks zeigt den Schnittstellenstatus, die VLAN-ID, das Gateway und den DHCP-Adressbereich.

![IoT-Netzwerk 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Edit**. Die Einstellungen des IoT-Netzwerks öffnen sich am rechten Seitenrand. Dort können Sie die Grundeinstellungen und die Einstellungen des DHCP-Servers ändern.

![IoT-Netzwerk 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Grundeinstellungen {#iot-network-basic-settings}

Sie können das Subnetz innerhalb der privaten IPv4-Adressbereiche `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` festlegen.

![IoT-Netzwerk – Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Das Standard-Gateway des IoT-Netzwerks lautet **192.168.10.1**. Wählen Sie eine andere Adresse, falls sie einen Konflikt mit Ihrem lokalen Netzwerk verursacht.

- **Netmask**

    Die voreingestellte Netzmaske ist **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Die Standard-VLAN-ID des IoT-Netzwerks ist **10**. Sie können sie bei Bedarf ändern.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die per Kabel an diesen Ports angeschlossen sind, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Danach können diese Geräte nicht mehr mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis:** Die AP-Isolierung gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Die WAN-Zugriffssteuerung regelt den Zugriff des lokalen Subnetzes auf das Internet und auf andere WAN-seitige Subnetze.

    Für die WAN-Zugriffssteuerung stehen drei Modi zur Auswahl.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und auf andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt den gesamten ausgehenden Zugriff, einschließlich des Zugriffs auf das Internet und auf WAN-seitige Subnetze.

### DHCP-Server {#iot-network-dhcp-server}

Der DHCP-Server ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch eine IP-Adresse und weitere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen auf den Client-Geräten manuell konfigurieren. Befolgen Sie dazu die [Anleitung zur manuellen Konfiguration einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Bereichs anpassen, etwa wenn sich die Größe Ihres Netzwerks ändert, IP-Adresskonflikte auftreten oder sich der durch die Subnetzmaske festgelegte Adressbereich ändert.

![IoT-Netzwerk – DHCP-Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![IoT-Netzwerk – erweiterte DHCP-Einstellungen 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![IoT-Netzwerk – erweiterte DHCP-Einstellungen 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** übernimmt die Auflösung von Domainnamen, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Druckaufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

## VLAN-Netzwerke {#vlan-networks}

Oben auf der Hauptseite können Sie bei Bedarf weitere VLAN-Netzwerke erstellen, um verschiedene Gerätetypen oder den Datenverkehr von Gästen zu isolieren.

![VLAN-Netzwerke 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Klicken Sie rechts auf der Seite auf **+ Add**, um ein neues Netzwerk zu konfigurieren.

![VLAN-Netzwerke 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Grundeinstellungen {#vlan-networks-basic-settings}

Auf dieser Seite können Sie die Grundeinstellungen für VLAN-Netzwerke festlegen.

![VLAN-Netzwerke – Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Vergeben Sie einen Namen, an dem Sie das neue Subnetz erkennen können.

- **Gateway**

    Konfigurieren Sie das Gateway für das neue Subnetz manuell. Wählen Sie ein anderes Gateway, falls es einen Konflikt mit Ihrem bestehenden LAN-Segment verursacht.

- **Netmask**

    Die voreingestellte Netzmaske ist **255.255.255.0**. Wenn Sie ein größeres Subnetz mit mehr IP-Adressen benötigen, können Sie **255.255.0.0** auswählen.

- **VLAN ID**

    Beim Erstellen eines Subnetzes müssen Sie eine VLAN-ID zwischen **9** und **4000** zuweisen. Wählen Sie eine freie VLAN-ID, um Netzwerkkonflikte zu vermeiden.

- **Associated LAN Ports**

    Wählen Sie die LAN-Ports aus, die Sie diesem Subnetz zuweisen möchten. Geräte, die per Kabel an diesen Ports angeschlossen sind, werden Teil dieses Netzwerks.

- **AP Isolation**

    Sie können Client-Geräte in einem separaten Netzwerksegment isolieren. Danach können diese Geräte nicht mehr mit anderen Geräten im selben Netzwerk kommunizieren.

    **Hinweis:** Die AP-Isolierung gilt ausschließlich für WLAN-Clients.

- **WAN Access Control**

    Die WAN-Zugriffssteuerung regelt den Zugriff des lokalen Subnetzes auf das Internet und auf andere WAN-seitige Subnetze.

    Für die WAN-Zugriffssteuerung stehen drei Modi zur Auswahl.

    - **Unrestricted** erlaubt diesem Subnetz uneingeschränkten Zugriff auf das Internet und auf andere WAN-seitige Subnetze.

    - **Block WAN Subnet** sperrt den Zugriff auf andere WAN-seitige Subnetze. Der Internetzugang bleibt verfügbar.

    - **Block Internet Access** sperrt den gesamten ausgehenden Zugriff, einschließlich des Zugriffs auf das Internet und auf WAN-seitige Subnetze.

### DHCP-Server {#vlan-networks-dhcp-server}

Der DHCP-Server ist standardmäßig aktiviert. Er weist jedem Client-Gerät automatisch eine IP-Adresse und weitere Kommunikationsparameter zu.

Wenn der DHCP-Server deaktiviert ist, müssen Sie die Netzwerkeinstellungen auf den Client-Geräten manuell konfigurieren. Befolgen Sie dazu die [Anleitung zur manuellen Konfiguration einer statischen IP-Adresse](../tutorials/manually_configure_static_ip.md).

Sie können die erste und letzte IP-Adresse des DHCP-Bereichs anpassen, etwa wenn sich die Größe Ihres Netzwerks ändert, IP-Adresskonflikte auftreten oder sich der durch die Subnetzmaske festgelegte Adressbereich ändert.

![VLAN-Netzwerke – DHCP-Grundeinstellungen](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Klicken Sie bei Bedarf auf **Advanced**, um weitere Einstellungen vorzunehmen.

![VLAN-Netzwerke – erweiterte DHCP-Einstellungen 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![VLAN-Netzwerke – erweiterte DHCP-Einstellungen 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** gibt an, wie lange eine per DHCP zugewiesene IP-Adresse für ein Gerät gültig ist.

- **Gateway** bezeichnet das Gerät, das den Datenverkehr zwischen dem lokalen Netzwerk und externen Netzwerken wie dem Internet weiterleitet.

- **DNS Server 1** ist der primäre Server, der Domainnamen in IP-Adressen auflöst.

- **DNS Server 2** übernimmt die Auflösung von Domainnamen, wenn der primäre DNS-Server nicht verfügbar ist.

- **LPR Server** (Line Printer Remote Server) verwaltet Druckaufträge und ermöglicht es Netzwerkgeräten, Druckaufträge an entfernte Drucker zu senden. Sie können mehrere LPR-Druckerports konfigurieren.

Nach der Konfiguration erscheint das neue VLAN-Netzwerk mit den Subnetzinformationen auf derselben Seite.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
