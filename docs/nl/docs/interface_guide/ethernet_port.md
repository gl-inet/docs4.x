# Ethernet Port {#ethernet-port}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.7-4.9. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.9 en ouder" markdown="1">

- [Firmware v4.10 en hoger](ethernet_port_v4.10.md)

</div>

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **Ethernet Port** of **Port Management**.

Je kunt de rollen van Ethernet-poorten (WAN/LAN) beheren en poortgegevens, zoals het MAC-adres en de onderhandelde snelheid, bekijken.

## WAN {#wan}

Dit gedeelte toont de poortrol (WAN of LAN), het MAC-adres en de onderhandelde snelheid.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

- **WAN/LAN**: de huidige bedrijfsmodus van de fysieke WAN-poort. Je kunt deze zo nodig op LAN instellen.

- **MAC Mode**: standaard Factory Mode. Je kunt overschakelen naar Clone Mode of Random Mode.

- **MAC Address**: het MAC-adres van de WAN-interface.

- **Negotiated Network Port Rate**: de onderhandelde linksnelheid van de WAN-interface. Deze wordt alleen weergegeven wanneer een geldige link wordt gedetecteerd.

## LAN {#lan}

Dit gedeelte toont de onderhandelde snelheid van de LAN-poort. Deze wordt alleen weergegeven wanneer een geldige link wordt gedetecteerd.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Bij sommige modellen kun je LAN 1 voor een dual-Ethernet WAN-configuratie naar een WAN-poort omschakelen. Klik op [Dual-Ethernet WAN](#dual-ethernet-wan) voor meer informatie.

## Dual-Ethernet WAN {#dual-ethernet-wan}

Met Dual-Ethernet WAN kun je een standaard LAN-Ethernet-poort omschakelen naar een secundaire WAN-poort voor internettoegang via twee Ethernet-verbindingen. Dit biedt een betrouwbare back-upverbinding en ondersteunt, indien compatibel, bandbreedteaggregatie voor toepassingen met veel bandbreedte. Je kunt ook tegelijk verbinding maken met twee onafhankelijke netwerken, bijvoorbeeld voor werk en privé, zonder extra hardware.

??? "Ondersteunde modellen"

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
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Opmerking**: GL-E5800 (Mudi 7) heeft één Ethernet-poort, standaard LAN maar omschakelbaar naar WAN, en een **USB-C-poort met OTG-ondersteuning**. Sluit een afzonderlijk verkrijgbare USB‑C-naar-Ethernet-adapter aan op de USB‑C-poort om een tweede Ethernet-poort voor Dual-Ethernet WAN toe te voegen.

??? "Niet-ondersteunde modellen"
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

Volg de onderstaande stappen om een LAN-poort naar een WAN-poort om te schakelen.

1. Klik op de pagina **Port Management** of **Ethernet Port** op het tabblad **LAN**, wijzig de poortrol in WAN en klik op **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. Klik in het pop-upvenster op **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. De geselecteerde poort werkt nu als WAN-poort. Je kunt [hier](multi-wan.md) verdergaan met de configuratie van Multi-WAN.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
