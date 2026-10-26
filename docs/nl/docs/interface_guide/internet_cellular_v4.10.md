# Via een mobiel netwerk verbinding maken met internet (v4.10) {#connect-to-the-internet-via-cellular-v410}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.10 en hoger. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.10 en hoger" markdown="1">

- [Firmware v4.8-v4.9](internet_cellular.md)
- [Firmware v4.7 en ouder](internet_cellular_v4.7.md)

</div>

---

De meeste GL.iNet-routers ondersteunen mobiele verbindingen. Deze handleiding beschrijft de mobiele verbinding voor twee soorten routers:

1. **Routers voor mobiele netwerken**

    GL.iNet-routers voor mobiele netwerken, zoals Spitz AX (GL-X3000) en Mudi 7 (GL-E5800), hebben een ingebouwde 4G/5G-module en één of twee simkaartsleuven. De Cellular-instellingen in het webbeheerpaneel kunnen per model en firmwareversie enigszins verschillen. Raadpleeg [Routers voor mobiele netwerken](#cellular-routers) om de verbinding in te stellen.

2. **Routers zonder ingebouwde mobiele modem**

    Routers zonder ingebouwde mobiele modem zijn bijvoorbeeld thuis-, reis- en minirouters en beveiligingsgateways. Ze hebben gewoonlijk een USB-poort waarop je een niet-meegeleverde USB-dongle voor mobiele connectiviteit kunt aansluiten. Raadpleeg [Routers zonder ingebouwde mobiele modem](#non-cellular-routers) om de verbinding in te stellen.

**Opmerking:** sommige simkaarten moeten vóór het eerste gebruik worden geactiveerd. Activeer de simkaart in een smartphone voordat je deze in de router plaatst om compatibiliteit te waarborgen.

## Routers voor mobiele netwerken {#cellular-routers}

In dit gedeelte wordt **Mudi 7 (GL-E5800)** als voorbeeld gebruikt om de installatie van de mobiele verbinding en bijbehorende functies te beschrijven.

Mudi 7 heeft een ingebouwde eSIM en twee nano‑simkaartsleuven met Dual SIM Dual Standby. Het webbeheerpaneel kan daardoor enigszins afwijken van andere mobiele routers, vooral modellen met één simkaartsleuf.

### Netwerk instellen {#network-setup}

Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**.

1. Wanneer geen simkaart is geplaatst, toont de pagina "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Plaats een simkaart. De router maakt automatisch verbinding. Daarna toont de pagina je provider, signaalsterkte, band, dataverbruik en meer opties.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Als de simkaart niet wordt gedetecteerd, plaats je deze opnieuw of start je de router opnieuw op.

3. Klik op **Details & Configuration** om de netwerkgegevens te bekijken.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Onder **Network Information** staan SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address en IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Wat is Max Bit Rate (AMBR)?"

        Max Bit Rate (AMBR) betekent Aggregate Maximum Bit Rate. Dit bepaalt de gezamenlijke maximale bitsnelheid voor alle non‑GBR-bearers van je provider. Je mobiele provider stelt deze parameter in.

4. Klik op **Details & Configuration** om het netwerk handmatig te configureren.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Onder **Network Settings** kun je netwerkparameters, zoals APN, configureren.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: APN-instellingen worden gewoonlijk automatisch van de simkaart opgehaald. Sommige simkaarten vereisen een specifieke APN. Vraag je provider om de juiste APN als je deze niet kent.

    - **IP Type**: wordt automatisch gedetecteerd. Je kunt IPv4, IPv6 of beide instellen. Controleer of de geselecteerde optie overeenkomt met het IP-type dat je simkaart ondersteunt. Een niet-ondersteund type of geselecteerd IPv6 terwijl IPv6 op de router is uitgeschakeld, kan verbindingsproblemen veroorzaken.

    - **International Data Roaming**: standaard ingeschakeld voor datagebruik tijdens internationale reizen. Schakel de functie uit als deze niet nodig is of om hoge roamingkosten te voorkomen.

    - **TTL**: sommige providers bepalen aan de TTL-waarde of de simkaart in een router wordt gebruikt. Als je simkaart niet in de router werkt, kun je een andere TTL dan 64 of 128 proberen, bijvoorbeeld 65.

    - **HL**: bij IPv6 beperkt HL (Hop Limit) het aantal overdrachtshops van gegevenspakketten in het netwerk en is het gelijkwaardig aan TTL bij IPv4.

    - **MTU**: stel de MTU in voor je gebruikssituatie. Onjuiste instellingen kunnen de internetverbinding verbreken. Start het apparaat opnieuw op nadat je MTU hebt gewijzigd.

    - **Authentication**: staat gewoonlijk op NONE als geen aanmeldingsgegevens vereist zijn. Je kunt PAP, CHAP of PAP/CHAP instellen.

### Verkeersstatistieken {#traffic-statistics}

Klik op **Data Usage** om de verkeersstatistieken te bekijken.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Schakel **SIM Limit Settings** in om Data Cap Amount voor je simkaart in te stellen of een schema voor het periodiek resetten van simdata te maken.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Stel Data Cap Amount, Data Reset Period, Start Day en Start Hour in en klik op **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Note**:

1. Wijzig Data Cap Amount of Data Used als Data Used de limiet overschrijdt. Anders kan de netwerkverbinding worden verbroken of kan de router naar een andere simkaart overschakelen wanneer [SIM Failover](#sim-failover) is ingeschakeld.

2. Als SIM 1 Data Cap Amount is ingesteld en SIM Auto Switch is ingeschakeld, schakelt SIM 1 automatisch naar SIM 2 wanneer de limiet wordt overschreden en wordt SIM 1 uitgeschakeld.

3. Start Day: het maximale aantal dagen is gelijk aan het werkelijke aantal dagen in de huidige maand.

### Gegevens van het mobiele netwerk {#cellular-details}

Klik op **Details & Configuration** om de gegevens van het mobiele netwerk te bekijken.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Onder **Cellular Information** staan Network Type, TAC, Cell ID, Band en Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: wordt automatisch gedetecteerd. Open het tabblad **Cellular Settings** en selecteer het netwerktype in de vervolgkeuzelijst om het zelf in te stellen.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Selecteer 5G voor hogere snelheid, waarvoor een 5G-signaal vereist is, of 4G voor stabiliteit.

    Als je de zendmast vergrendelt, staat het netwerktype vast en kan het niet worden gewijzigd.

- **TAC**: afkorting van Tracking Area Code, een door het netwerk toegewezen id voor een trackinggebied bij mobiliteitsbeheer in het mobiele netwerk. Dit wordt automatisch van het basisstation gedetecteerd.

- **Cell ID**: een unieke id om een afzonderlijke cel van een mobiel basisstation te onderscheiden. Dit wordt ook automatisch van het basisstation gedetecteerd.

- **Band Information**: klik hierop om meer parameters van je mobiele band te bekijken.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: klik hierop om de geschiedenis van de signaalsterkte te bekijken en de kwaliteit van je mobiele verbinding te bewaken.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Band Masking {#band-masking}

Met Band Masking kun je specifieke mobiele banden gebruiken om het signaal te verbeteren.

Klik op **Details & Configuration** om Band Masking in te schakelen.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Schakel onder **Cellular Settings** **Band Masking** in, selecteer de gewenste banden en klik op **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Provider vergrendelen {#lock-operator}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) ondersteunt deze functie in firmware v4.8 en hoger.

Door een specifieke mobiele provider te vergrendelen, gebruikt de router alleen het netwerk van die provider. Dit zorgt voor een stabiele verbinding en voorkomt onbedoelde roamingkosten, vooral in grensgebieden waar het apparaat anders met buitenlandse netwerken kan verbinden.

Klik op **Details & Configuration** om een provider te vergrendelen.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Klik onder **Cellular Settings** op **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Selecteer eventueel **Lock Mode** voordat je naar netwerken scant.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: vergrendelt handmatig een specifieke provider.

- **Manual-Auto**: schakelt automatisch naar een beschikbaar providernetwerk als handmatig vergrendelen mislukt.

Klik vervolgens op **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Wacht een minuut totdat de beschikbare providers verschijnen. Selecteer een provider en klik op **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Het mobiele signaal wordt aan de geselecteerde provider gekoppeld.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Zendmast vergrendelen {#lock-tower}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) ondersteunt deze functie in firmware v4.7 en hoger.

Vergrendel een zendmast voor een hoogwaardig signaal en stabiele mobiele verbinding. De zendmast moet overeenkomen met de frequentiebanden die je provider en apparaat ondersteunen. Anders kan de verbinding mislukken.

Klik op **Details & Configuration** om een zendmast te vergrendelen.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Klik onder **Cellular Settings** op **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

Klik in het pop-upvenster op **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Wacht een minuut totdat de beschikbare zendmasten verschijnen.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Selecteer een zendmast om de gegevens te bekijken en klik op **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Het mobiele signaal wordt aan de geselecteerde zendmast gekoppeld.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Note**:

1. Wanneer de Cellular-interface is ingeschakeld, kan het apparaat mogelijk niet alle zendmasten scannen.

2. Als de vergrendelde zendmast niet overeenkomt met Band Masking, indien ingeschakeld, of de APN-parameters, kan de router geen verbinding maken met het mobiele netwerk.

3. Nadat je een zendmast hebt vergrendeld, probeert de router na een herstart opnieuw verbinding te maken met die mast, ook als je de router hebt verplaatst. Hierdoor kan de router op de nieuwe locatie mogelijk niet automatisch verbinding maken met het mobiele netwerk. Ontgrendel in dat geval de huidige zendmast of vergrendel handmatig een nieuwe mast.

### SMS {#sms}

Raadpleeg [SMS](../tutorials/sms.md).

### SMS Forwarding {#sms-forwarding}

Raadpleeg [SMS doorsturen](../tutorials/sms_forwarding.md).

### Vliegtuigmodus {#airplane-mode}

Klik rechtsboven op het tandwielpictogram en schakel **Airplane Mode** in.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Modemgegevens {#modem-information}

Klik rechtsboven op het tandwielpictogram en selecteer **Modem Information** om de modemgegevens te bekijken.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Simkaartfailover {#sim-failover}

Deze functie is alleen beschikbaar op mobiele routers die dual-sim ondersteunen.

Met SIM Failover schakelt de router automatisch tussen SIM 1 en SIM 2. Als het dataverbruik van de simkaart met de hoogste prioriteit Data Cap Amount overschrijdt of internettoegang mislukt, schakelt de router naar de back-upkaart.

Klik rechtsboven op het tandwielpictogram en selecteer **SIM Failover** om de functie in te schakelen.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

Schakel in het pop-upvenster **Auto Switch** in. Sleep de knop rechts om de simkaartprioriteit aan te passen.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Schakel **Scheduled Switch to Preferred SIM** in als de router dagelijks op een bepaald tijdstip naar de voorkeurssimkaart moet terugschakelen. Stel **Daily Execution Time** in en klik op **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### AT-opdracht {#at-command}

AT-opdrachten zijn standaardinstructies voor communicatie met de mobiele modem. Hiermee kun je opdrachten verzenden en de modemstatus controleren.

Klik rechtsboven op het tandwielpictogram en selecteer **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: wanneer Shortcut op **Manual command** staat, voer je de gewenste opdracht in het veld **AT Command** in en klik je onderaan op **Send**. Het resultaat verschijnt in het uitvoervak.

    Je kunt ook op het vak klikken en in de vervolgkeuzelijst een **vooraf ingestelde opdracht** selecteren.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Als je bijvoorbeeld "Request SIM card status" en SIM1 selecteert, klik je op "Send" voor het onderstaande resultaat.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: kies of de opdracht op SIM1 of SIM2 wordt toegepast. De beschikbare opties hangen af van het aantal simkaartsleuven.

- **AT Command**: voer in dit veld de gewenste opdracht in wanneer Shortcut op "Manual command" staat.

## Routers zonder ingebouwde mobiele modem {#non-cellular-routers}

Routers zonder ingebouwde mobiele modem kunnen via een externe, niet-meegeleverde USB-dongle op een USB-poort toch een mobiel netwerk gebruiken.

USB-dongles en modems kunnen in Standard USB modem mode of Host-less mode werken.

- **Standard USB modem mode**: de router werkt als USB-host en de dongle als USB-slavemodem. De dongle biedt opdrachtinterfaces (AT/QMI/MBIM) en een virtuele USB-Ethernet-poort en kan via de native Cellular WAN van de router worden beheerd. De router kan gegevens zoals ICCID, signaalsterkte en band uitlezen; je configureert simkaartinstellingen rechtstreeks via de webinterface van de router.

- **Host-less mode**: de dongle brengt intern de mobiele verbinding tot stand en biedt de router een virtuele USB-Ethernet-interface. De router herkent deze als tethered WAN en niet als bestuurbare modem. De verbinding wordt daarom via Tethering in plaats van Cellular tot stand gebracht. Gegevens op laag niveau zijn niet op de router beschikbaar; alle APN- en simkaartconfiguraties moeten via de ingebouwde webinterface van de dongle worden uitgevoerd.

Raadpleeg het gedeelte dat bij de bedrijfsmodus van je USB-dongle hoort.

### Standaard-USB-modem {#standard-usb-modem}

In dit gedeelte worden **Mango 2 (GL-MG1300)** en het 5G-ontwikkelbord [GL-M2](https://www.gl-inet.com/products/gl-m2){target="_blank"} met 5G NR-module RM520N-GL als voorbeeld gebruikt.

1. Plaats een simkaart in GL-M2 en sluit GL-M2 aan op de USB-poort van je router.

2. Meld je aan bij het webbeheerpaneel en ga naar **INTERNET** -> **Cellular**.

    De router probeert automatisch verbinding met internet te maken. Daarna toont de pagina de netwerkgegevens en een groene stip.

    ![m2 sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_active.png){class="glboxshadow"}

3. SIM Card Settings.

    Klik op **SIM Card Settings** om de simkaartconfiguratie te bekijken.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings1.png){class="glboxshadow"}

    Je ziet automatisch gedetecteerde configuraties, zoals APN, IP-type en netwerktype. Wijzigingen zorgen ervoor dat opnieuw verbinding wordt gemaakt.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings2.png){class="glboxshadow"}

4. SIM Information.

    Klik op **SIM Information** om de simkaartgegevens te bekijken.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info1.png){class="glboxshadow"}

    Je ziet netwerkgegevens van de simkaart, zoals ICCID, IP-adres, DNS, mobiele band en signaalsterkte.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info2.png){class="glboxshadow gl-80-desktop"}

5. SMS en SMS Forwarding.

    Raadpleeg [SMS](../tutorials/sms.md) en [SMS Forwarding](../tutorials/sms_forwarding.md) om deze functies te gebruiken.

6. Mobiele profielen beheren.

    Klik rechtsboven op het tandwielpictogram en selecteer **Manage Cellular Profiles** om simkaartprofielen te beheren.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    Het huidige profiel wordt weergegeven.

    ![m2 manage profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_manage_profiles.png){class="glboxshadow"}

    Klik op **Add a New Profile** om zo nodig meer profielen toe te voegen.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile1.png){class="glboxshadow"}

    Voer de vereiste parameters in en klik op **Apply**.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile2.png){class="glboxshadow"}

7. AT-opdracht voor de modem.

    AT-opdrachten zijn standaardinstructies voor communicatie met de mobiele modem. Hiermee kun je opdrachten verzenden en de modemstatus controleren.

    Klik rechtsboven op het tandwielpictogram en selecteer **Modem AT Command** om een AT-opdracht uit te voeren.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    ![m2 atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_atcommand.png){class="glboxshadow"}

    - **Shortcut**: wanneer Shortcut op **Manual command** staat, voer je de gewenste opdracht in het veld **AT Command** in en klik je onderaan op **Send**. Het resultaat verschijnt in het uitvoervak.

        Je kunt ook op het vak klikken en in de vervolgkeuzelijst een **vooraf ingestelde opdracht** selecteren.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

        Als je bijvoorbeeld "Request SIM card status" en SIM1 selecteert, klik je op "Send" voor het onderstaande resultaat.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

    - **SIM Slot**: kies of de opdracht op SIM1 of SIM2 wordt toegepast. De beschikbare opties hangen af van de simkaartsleuven van de externe USB-modem.

    - **AT Command**: voer in dit veld de gewenste opdracht in wanneer Shortcut op "Manual command" staat.

### Host‑less dongle {#hostless-dongle}

In dit gedeelte worden **Flint 3 (GL-BE9300)** en de externe USB-dongle [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} als voorbeeld gebruikt.

1. Sluit de USB-dongle aan op de USB-poort van de router.

2. Meld je aan bij het webbeheerpaneel, ga naar **INTERNET** -> **Tethering** en klik op **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Klik op **Advanced** om geavanceerde instellingen, zoals TTL, HL en MTU, aan te passen voordat je op **Connect** klikt.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Nadat de verbinding tot stand is gebracht, toont de pagina de netwerkgegevens en een groene stip.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

4. Raadpleeg [SIMPoYo uFi beheren](../user_guide/simpoyo-4g-ufi/index.md#manage-simpoyo-ufi) om APN- en simkaartinstellingen voor de kaart in SIMPoYo uFi te configureren.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
