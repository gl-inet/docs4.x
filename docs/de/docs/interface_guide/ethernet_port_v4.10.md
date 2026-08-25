# Ethernet-Port (Firmware v4.10)

**Hinweis**: Der Inhalt dieser Seite ist derzeit für Flint 4 (GL-BE14000) verfügbar und wird mit Firmware v4.10 für weitere Modelle bereitgestellt.

Wenn auf Ihrem Gerät eine andere Firmwareversion ausgeführt wird, verwenden Sie die nachfolgende Auswahl, um zur entsprechenden Anleitung zu wechseln.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Firmware v4.9 und älter](ethernet_port.md)

</div>

---

Navigieren Sie auf der linken Seite des webbasierten Admin Panels zu **NETWORK** -> **Ethernet Port**.

Auf dieser Seite werden alle Schnittstellen des Routers angezeigt. Sie können den Verbindungsstatus jeder Schnittstelle prüfen, die Rollen der Ethernet-Ports (WAN oder LAN) verwalten und Portdetails wie MAC-Adresse, ausgehandelte Geschwindigkeit und aktuellen Verbindungsstatus anzeigen. Darüber hinaus können Sie die physischen Schnittstellen beliebigen von Ihnen erstellten Subnetzen zuweisen.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: Wenn das Portsymbol blau hervorgehoben ist, ist die physische Verbindung aktiv.

- **Link Down**: Wenn das Portsymbol grau dargestellt wird, ist die physische Verbindung inaktiv.

- **Speed**: Ausgehandelte Übertragungsrate des Ethernet-Ports.

- **MAC**: MAC-Adresse des Ports.

- **VLAN Mode**: Der Betriebsmodus von LAN-Ports kann auf Standard oder Multiple VLANs eingestellt werden.

- **Native Network**: Das dem LAN-Port standardmäßig zugewiesene ungetaggte Subnetz.

- **Allowed VLANs**: Gibt die getaggten VLANs an, die diesen Port im Modus Multiple VLANs passieren dürfen.

- **Settings**: Klicken Sie hier, um die Konfigurationsseite des jeweiligen Ports aufzurufen.

## WAN

In diesem Abschnitt werden der Portmodus (WAN oder LAN), die MAC-Adresse und die ausgehandelte Geschwindigkeit angezeigt.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: Der aktuelle Betriebsmodus des physischen WAN-Ports. Sie können ihn bei Bedarf auf LAN einstellen.

- **MAC Mode**: Standardmäßig ist Factory Mode eingestellt. Sie können zu Clone Mode oder Random Mode wechseln.

- **MAC Address**: Die MAC-Adresse der WAN-Schnittstelle.

- **Negotiated Network Port Rate**: Die ausgehandelte Verbindungsgeschwindigkeit der WAN-Schnittstelle. Sie wird nur angezeigt, wenn eine gültige Verbindung erkannt wurde.

## LAN

In diesem Abschnitt wird die Konfiguration der LAN-Ports angezeigt. Sie können den Ethernet Mode je nach Bedarf auf **Standard** oder **Multiple VLANs** einstellen.

### Standardmodus

Im Standardmodus ist nur ein VLAN (Untagged) zulässig. Dieser Modus dient zum Anschließen von Endgeräten.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: Die ausgehandelte Verbindungsgeschwindigkeit der LAN-Schnittstelle. Sie wird nur angezeigt, wenn eine gültige Verbindung erkannt wurde.

- **Ethernet Mode**: Standardmäßig ist Standard Mode eingestellt.

- **Access Network**: Mit Access Network können Sie eine Netzwerkisolierung umsetzen, indem Sie LAN-Ports verschiedenen Subnetzen zuweisen.

Nach Abschluss der Konfiguration können Sie zur Seite Ethernet Port zurückkehren und die Einstellungen überprüfen.

### Modus Multiple VLANs

Der Modus Multiple VLANs erlaubt mehrere VLANs (Tagged) an einem Port und wird in der Regel zum Anschließen von APs oder weiteren Switches verwendet.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: Die ausgehandelte Verbindungsgeschwindigkeit der LAN-Schnittstelle. Sie wird nur angezeigt, wenn eine gültige Verbindung erkannt wurde.

- **VLAN Mode**: Klicken Sie auf die Registerkarte Multiple VLANs, um in den Modus Multiple VLANs zu wechseln.

- **Untagged Traffic Handling**: Legen Sie fest, wie der Port ungetaggte Pakete verarbeitet. Sie können diese Pakete entweder direkt verwerfen oder sie an ein anderes Subnetz als natives PVID-Netzwerk weiterleiten.

- **Allowed Tagged Networks**: Gibt an, welche VLANs diesen Port im getaggten Modus passieren dürfen. Sie können VLAN-Netzwerke aus der Liste auswählen; nur der entsprechende Datenverkehr wird weitergeleitet.

Nach Abschluss der Konfiguration können Sie zur Seite Ethernet Port zurückkehren und die Einstellungen überprüfen.

Einige Modelle unterstützen für Dual-Ethernet-WAN-Szenarien das Umschalten von LAN 1 auf einen WAN-Port. Weitere Informationen finden Sie unter [Dual-Ethernet WAN](#dual-ethernet-wan).

## Dual-Ethernet WAN

Mit der Funktion Dual-Ethernet WAN kann ein standardmäßiger LAN-Ethernet-Port in einen zweiten WAN-Port für Dual-Ethernet-Internetzugang umgeschaltet werden. Das sorgt für eine zuverlässige Backup-Verbindung und unterstützt, sofern kompatibel, die Bandbreitenbündelung für bandbreitenintensive Anwendungen. Außerdem können Sie gleichzeitig zwei unabhängige Netzwerke, beispielsweise ein berufliches und ein privates Netzwerk, verwenden, ohne zusätzliche Hardware zu benötigen.

??? "Unterstützte Modelle"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Hinweis**: GL-E5800 (Mudi 7) verfügt über einen Ethernet-Port (standardmäßig LAN, auf WAN umschaltbar) und einen **OTG-fähigen USB-C-Port**. Um einen zweiten Ethernet-Port für Dual-Ethernet WAN hinzuzufügen, schließen Sie einen separat erhältlichen USB-C-zu-Ethernet-Adapter an den USB-C-Port an.

??? "Nicht unterstützte Modelle"

    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Führen Sie die folgenden Schritte aus, um einen LAN-Port in einen WAN-Port umzuschalten. Als Beispiel wird Flint 3 (GL-BE9300) verwendet.

1. Klicken Sie auf der Seite **Ethernet Port** auf die Einstellung **LAN1**, um die Konfigurationsseite aufzurufen. Ändern Sie anschließend die Portrolle in WAN und klicken Sie auf **Apply**.

    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Sie können zur Seite Ethernet Port zurückkehren und überprüfen, ob die Portrolle zu WAN gewechselt wurde.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. Der ausgewählte Port arbeitet nun als WAN-Port. Anschließend können Sie [hier](multi-wan.md) Multi-WAN konfigurieren.

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
