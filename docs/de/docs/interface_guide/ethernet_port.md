# Ethernet-Port

**Hinweis**: Diese Seite ist seit Firmware v4.7 als **Port Management** verfügbar und wurde in Firmware v4.8.3 in **Ethernet-Port** umbenannt.

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **Port Management** oder **Ethernet-Port**.

Hier können Sie Ethernet-Portrollen (WAN/LAN) verwalten und Portdetails wie MAC-Adresse und ausgehandelte Geschwindigkeit anzeigen.

## WAN

In diesem Abschnitt werden die Portrolle (WAN oder LAN), die MAC-Adresse und die ausgehandelte Geschwindigkeit angezeigt. 

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN**: Der aktuelle Betriebsmodus des physischen WAN-Ports. Sie können ihn bei Bedarf auf LAN einstellen.

- **MAC Mode**: Standardmäßig ist Factory Mode eingestellt. Sie können zu Clone Mode oder Random Mode wechseln.

- **Mac Address**: Die MAC-Adresse der WAN-Schnittstelle.

- **Negotiated Network Port Rate**: Die ausgehandelte Verbindungsgeschwindigkeit der WAN-Schnittstelle. Sie wird nur angezeigt, wenn eine gültige Verbindung erkannt wurde.

## LAN

In diesem Abschnitt wird die ausgehandelte Geschwindigkeit des LAN-Ports angezeigt. Sie wird nur eingeblendet, wenn eine gültige Verbindung erkannt wurde.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Einige Modelle unterstützen das Umschalten von LAN 1 auf einen WAN-Port für Dual-Ethernet-WAN-Szenarien. Klicken Sie für Details auf [Dual-Ethernet WAN](#dual-ethernet-wan).

## Dual-Ethernet WAN

Mit der Funktion Dual-Ethernet WAN kann ein standardmäßiger LAN-Ethernet-Port in einen zweiten WAN-Port für Dual-Ethernet-Internetzugang umgeschaltet werden. Das sorgt für zuverlässige Backup-Konnektivität und unterstützt, sofern kompatibel, die Bandbreitenbündelung für bandbreitenintensive Workloads. Außerdem können Sie gleichzeitig zwei unabhängige Netzwerke, z. B. beruflich und privat, verwenden, ohne zusätzliche Hardware zu benötigen.

??? "Unterstützte Modelle"
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

    **Hinweis**: GL-E5800 (Mudi 7) ist mit einem Ethernet-Port ausgestattet (standardmäßig LAN, auf WAN umschaltbar) sowie mit einem **OTG-fähigen USB-C-Port**. Um einen zweiten Ethernet-Port für Dual-Ethernet WAN hinzuzufügen, schließen Sie bitte einen separat erhältlichen USB-C-zu-Ethernet-Adapter an den USB-C-Port an.

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

Führen Sie die folgenden Schritte aus, um einen LAN-Port in einen WAN-Port umzuschalten.

1. Klicken Sie auf der Seite **Port Management** oder **Ethernet Port** auf die Registerkarte **LAN**, ändern Sie die Portrolle in WAN und klicken Sie dann auf **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. Klicken Sie im Pop-up-Fenster auf **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. Der ausgewählte Port arbeitet nun als WAN-Port. Sie können anschließend [hier](multi-wan.md) Multi-WAN konfigurieren.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
