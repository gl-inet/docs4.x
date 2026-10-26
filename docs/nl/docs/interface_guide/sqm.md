# SQM (Smart Queue Management) {#sqm-smart-queue-management}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Sommige modellen, zoals Mango 2 (GL-MG1300), ondersteunen SQM wegens onvoldoende geheugen niet, ook niet met firmware v4.9 of hoger.

---

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) beheert het netwerkverkeer intelligent om latentie en bufferbloat te beperken, voor soepelere games en spraakoproepen.

**Note**:

1. Deze functie beïnvloedt alleen verkeer dat door de router loopt wanneer deze als gateway werkt, waaronder lokaal clientverkeer en VPN-clientverkeer. De functie geldt niet voor inkomend verkeer wanneer de router als VPN-server werkt.
2. SQM gebruikt veel systeembronnen en werkt het best bij lage bandbreedte of congestie. Op snelle verbindingen kan de piekdoorvoer dalen.
3. SQM werkt niet in de modus Drop-in Gateway.
4. SQM en QoS kunnen niet tegelijk worden ingeschakeld.
5. SQM kan niet samen met Network Acceleration worden gebruikt. Bij inschakeling wordt Network Acceleration automatisch uitgeschakeld.

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

Zet de schakelaar om om SQM in te schakelen en volg de onderstaande stappen.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Voer de WAN-upload- en downloadsnelheid van 1-10000 handmatig in of klik op **Run Speedtest** om deze te meten en de velden automatisch in te vullen. Hiervoor is een internetverbinding vereist.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Opmerking**: ingevoerde waarden zijn in **Mbps**. De equivalente waarde in **MB/s** wordt ter referentie weergegeven.

2. **Queue Discipline**

    Selecteer een wachtrijregel om verkeer te beheren en latentie onder belasting te verlagen.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: slimme automatische verkeersregeling met uitstekende algemene latentiebeheersing (aanbevolen).

        Wanneer **cake** als wachtrijdiscipline is geselecteerd, is **Cake Autorate** optioneel beschikbaar.

        Cake Autorate past de CAKE-bandbreedte in realtime aan op basis van probe RTT. Er worden geen actieve snelheidstests uitgevoerd, alleen lichte pings. Aanbevolen bij wisselende WAN-bandbreedte en niet nodig bij stabiele links.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Opmerking**: Cake Autorate genereert voortdurend testverkeer op de achtergrond. Houd rekening met dit dataverbruik bij een verbinding met datalimiet.

        De standaardinstellingen zijn geschikt voor de meeste verbindingen. Wijzig de volgende parameters alleen als je het effect op Cake Autorate begrijpt. Klik zo nodig op **Reset to Default**.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: een door komma's gescheiden lijst met IP-adressen voor netwerkkwaliteitstests.

        - **Probe Interval**: kortere intervallen reageren sneller maar gebruiken meer CPU-bronnen.

        - **Concurrent Probes**: het aantal gelijktijdige tests mag niet hoger zijn dan het aantal testservers; hogere waarden verhogen de CPU-belasting.

        - **Idle Detection Threshold**: onder deze overdrachtssnelheid wordt de verbinding als inactief beschouwd. De waarde mag niet hoger zijn dan 25% van de ingestelde snelheidslimiet.

        - **Download Latency Threshold**: als de downloadlatentie deze drempel overschrijdt, wordt de bandbreedte verlaagd.

        - **Upload Latency Threshold**: als de uploadlatentie deze drempel overschrijdt, wordt de bandbreedte verlaagd.

    - **fq_codel**: eenvoudige, efficiënte fair queueing met basisverlaging van de latentie.

## Voor firmware v4.9 tot v4.10 {#for-firmware-v49-to-v410}

Zet de schakelaar om om SQM in te schakelen en stel voor verkeersplanning de maximale upload- en downloadsnelheid van 1-10000 in. Stem deze af op de werkelijke internetbandbreedte.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Opmerking**: ingevoerde waarden zijn in **Mbps**. De equivalente waarde in **MB/s** wordt ter referentie weergegeven.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Voor Queue Rule zijn twee opties beschikbaar:

- **cake**: slimme automatische verkeersregeling met uitstekende algemene latentiebeheersing (aanbevolen).

- **fq_codel**: eenvoudige, efficiënte fair queueing met basisverlaging van de latentie.

!!! Tip

    Bij QoS stel je toepassingsprioriteiten in en wijst de router bandbreedte dienovereenkomstig toe. Bij SQM selecteer je een wachtrijregel.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
