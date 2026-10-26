# Ethernet Port (Firmware v4.10) {#ethernet-port-firmware-v410}

**Opmerking**: de inhoud van deze pagina is voor het eerst geïntroduceerd op Flint 4 (GL-BE14000) en wordt met firmware v4.10 voor andere modellen uitgerold.

Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Firmware v4.9 en ouder](ethernet_port.md)

</div>

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **Ethernet Port**.

Deze pagina toont alle interfaces van de router. Je kunt de verbindingsstatus van elke interface bekijken, de rollen van Ethernet-poorten (WAN of LAN) beheren en poortgegevens, zoals het MAC-adres, de onderhandelde snelheid en de huidige linkstatus, bekijken. Daarnaast kun je fysieke interfaces aan gemaakte subnets toewijzen.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: wanneer het poortpictogram blauw is gemarkeerd, is de fysieke link actief.

- **Link Down**: wanneer het poortpictogram grijs is, is de fysieke link inactief.

- **Speed**: onderhandelde overdrachtssnelheid van de Ethernet-poort.

- **MAC**: MAC-adres van de poort.

- **VLAN Mode**: de bedrijfsmodus van LAN-poorten kan worden ingesteld op Standard of Multiple VLANs.

- **Native Network**: het standaard niet-getagde subnet dat aan de LAN-poort is toegewezen.

- **Allowed VLANs**: bepaalt welke getagde VLAN's in de modus Multiple VLANs via deze poort mogen worden doorgestuurd.

- **Settings**: klik om de configuratiepagina van een afzonderlijke poort te openen.

## WAN {#wan}

Dit gedeelte toont Port Mode (WAN of LAN), het MAC-adres en de onderhandelde snelheid.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: de huidige bedrijfsmodus van de fysieke WAN-poort. Je kunt deze zo nodig op LAN instellen.

- **MAC Mode**: standaard Factory Mode. Je kunt overschakelen naar Clone Mode of Random Mode.

- **MAC Address**: het MAC-adres van de WAN-interface.

- **Negotiated Network Port Rate**: de onderhandelde linksnelheid van de WAN-interface. Deze wordt alleen weergegeven wanneer een geldige link wordt gedetecteerd.

## LAN {#lan}

Dit gedeelte toont de configuratie van de LAN-poort. Je kunt Ethernet Mode naar behoefte instellen op **Standard** of **Multiple VLANs**.

### Standard Mode {#standard-mode}

Standard Mode staat slechts één VLAN (Untagged) toe en wordt gebruikt om eindapparaten aan te sluiten.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: de onderhandelde linksnelheid van de LAN-interface. Deze wordt alleen weergegeven wanneer een geldige link wordt gedetecteerd.

- **Ethernet Mode**: standaard Standard Mode.

- **Access Network**: met Access Network kun je netwerkisolatie bereiken door LAN-poorten aan verschillende subnets toe te wijzen.

Na de configuratie kun je naar de pagina Ethernet Port terugkeren om de instellingen te controleren.

### Multiple VLANs Mode {#multiple-vlans-mode}

De modus Multiple VLANs staat meerdere VLAN's (Tagged) op één poort toe, doorgaans om access points of andere switches aan te sluiten.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: de onderhandelde linksnelheid van de LAN-interface. Deze wordt alleen weergegeven wanneer een geldige link wordt gedetecteerd.

- **VLAN Mode**: klik op het tabblad Multiple VLANs om naar de modus Multiple VLANs over te schakelen.

- **Untagged Traffic Handling**: configureer hoe de poort niet-getagde pakketten verwerkt. Je kunt deze pakketten direct laten verwijderen of naar een ander subnet doorsturen als het native PVID-netwerk.

- **Allowed Tagged Networks**: bepaalt welke VLAN's in tagged-modus via deze poort mogen worden doorgestuurd. Selecteer VLAN-netwerken uit de lijst; alleen overeenkomend verkeer wordt doorgestuurd.

Na de configuratie kun je naar de pagina Ethernet Port terugkeren om de instellingen te controleren.

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

Volg de onderstaande stappen om een LAN-poort naar een WAN-poort om te schakelen. Flint 3 (GL-BE9300) wordt als voorbeeld gebruikt.

1. Klik op de pagina **Ethernet Port** op de instelling **LAN1** om de pagina Configuration te openen. Wijzig vervolgens de poortrol in WAN en klik op **Apply**.

    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Je kunt naar de pagina Ethernet Port terugkeren om te controleren of de poortrol naar WAN is gewijzigd.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. De geselecteerde poort werkt nu als WAN-poort. Je kunt [hier](multi-wan.md) verdergaan met de configuratie van Multi-WAN.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
