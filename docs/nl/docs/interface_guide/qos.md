# QoS (Quality of Service) {#qos-quality-of-service}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Sommige modellen, zoals Mango 2 (GL-MG1300), ondersteunen QoS wegens onvoldoende geheugen niet, ook niet met firmware v4.9 of hoger. Raadpleeg [Ondersteunde modellen](#supported-models) voor meer informatie.

---

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) optimaliseert bandbreedtetoewijzing door bij netwerkcongestie prioriteit te geven aan belangrijke activiteiten, zoals videogesprekken en gaming. Hierdoor daalt de latentie en verbeteren de prestaties.

**Note**:

1. Deze functie beïnvloedt alleen verkeer dat door de router loopt wanneer deze als gateway werkt, waaronder lokaal clientverkeer en VPN-clientverkeer. De functie geldt niet voor inkomend verkeer wanneer de router als VPN-server werkt.
2. QoS werkt niet in de modus Drop-in Gateway.
3. QoS en SQM kunnen niet tegelijk worden ingeschakeld.
4. QoS kan niet samen met Network Acceleration worden gebruikt. Bij inschakeling wordt Network Acceleration automatisch uitgeschakeld.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Niet-ondersteunde modellen"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Voor firmware v4.11 en hoger {#for-firmware-v411-and-above}

Zet de schakelaar om om QoS in te schakelen en volg de onderstaande stappen.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Voer de WAN-upload- en downloadsnelheid van 1-10000 handmatig in of klik op **Run Speedtest** om deze te meten en de velden automatisch in te vullen. Hiervoor is een internetverbinding vereist.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Opmerking**: ingevoerde waarden zijn in **Mbps**. De equivalente waarde in **MB/s** wordt ter referentie weergegeven.

2. **Scheduling Policy**

    Je kunt één beleidsmodus selecteren. Geavanceerde regels overschrijven het basisbeleid voor overeenkomend verkeer.

    - **Device Priority**

        In deze modus krijgen geselecteerde lokale clients bij WAN-congestie een hogere netwerkprioriteit. Klik op **Add Device** en selecteer apparaten die bij zware belasting bandbreedteprioriteit krijgen.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Zoek op clientnaam, MAC- of IP-adres. Selecteer de doelapparaten en klik op **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        In deze modus stel je prioriteiten voor toepassingen in. De router wijst de bandbreedte dienovereenkomstig toe.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Selecteer **Customize** en klik op **Pre-Set up** om toepassingsprioriteiten aan te passen.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        In het pop-upvenster staan alle categorieën standaard op Medium Priority.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Sleep de categorieën om de prioriteit aan te passen en klik op **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        In deze modus maak je geavanceerde QoS-regels voor verkeer met hoge prioriteit. Klik op **Add Rule** voor regels op basis van protocol, poort en bron-IP.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Geef Name, Protocol, Source Address en Destination Port op en klik op **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Voor firmware v4.9 tot v4.10 {#for-firmware-v49-to-v410}

Zet de schakelaar om om QoS in te schakelen. De pagina ziet er als volgt uit.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Stel voor verkeersplanning de maximale upload- en downloadsnelheid van 1-10000 in. Stem deze voor het beste resultaat af op de werkelijke internetbandbreedte.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Opmerking**: ingevoerde waarden zijn in **Mbps**. De equivalente waarde in **MB/s** wordt ter referentie weergegeven.

Stel vervolgens prioriteiten voor toepassingen in. De router wijst de bandbreedte dienovereenkomstig toe.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Selecteer **Customize** en klik op **Pre-Set up** om toepassingsprioriteiten aan te passen.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

In het pop-upvenster staan alle categorieën standaard op Medium Priority.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Sleep de categorieën om de prioriteit aan te passen en klik op **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
