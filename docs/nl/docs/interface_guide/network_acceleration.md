# Network Acceleration {#network-acceleration}

Netwerkversnelling verlaagt de CPU-belasting en versnelt het doorsturen van verkeerspakketten, maar kan met bepaalde functies conflicteren.

Wanneer Network Acceleration is ingeschakeld, werken Client Speed and Traffic Statistics en Client Speed Limit niet goed.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Niet-ondersteunde modellen"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Instellen {#setup}

Ga links in het webbeheerpaneel naar **NETWORK** -> **Network Acceleration**.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_acceleration/network_acceleration.png){class="glboxshadow"}

Er zijn drie modi.

- **Auto**

    Auto schakelt op basis van het werkelijke gebruik automatisch tussen de twee versnellingsmodi.

- **Hardware Acceleration**

    Hardwareversnelling werkt voor <u>Ethernet</u> en <u>Repeater</u>.

    Hardwareversnelling verplaatst veelvoorkomende netwerktaken, zoals NAT, pakketdoorsturing en checksumcontrole, naar speciale hardware zoals NPU's of HWNAT-chips. De functie werkt voor Ethernet- en Repeater-verbindingen en levert bij vaste paden en eenvoudige regels hoge doorvoer, lage latentie en minimale CPU-belasting.

- **Software Acceleration**

    Softwareversnelling werkt voor <u>Cellular</u>.

    Softwareversnelling gebruikt de algemene CPU van de router met geoptimaliseerde kernels of stuurprogramma's, zoals SWNAT. De functie werkt voor Cellular-toegang (4G/5G), waar hardwareversnelling gewoonlijk niet beschikbaar is, en biedt brede compatibiliteit en ondersteuning voor complexe protocollen. Bij hoge bandbreedte kan de CPU een knelpunt worden, vooral met functies zoals DPI, QoS of port forwarding.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
