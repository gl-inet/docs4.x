# Via een mobiel netwerk verbinding maken met internet (v4.8-v4.9) {#connect-to-the-internet-via-cellular-v48-v49}

De inhoud van deze pagina is gebaseerd op firmwareversies v4.8 tot v4.9. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.8 - v4.9" markdown="1">

- [Firmware v4.10 en hoger](internet_cellular_v4.10.md)
- [Firmware v4.7 en ouder](internet_cellular_v4.7.md)

</div>

---

De meeste GL.iNet-routers ondersteunen verbindingen met mobiele netwerken. Deze handleiding behandelt drie soorten modellen:

1. **Modellen met ingebouwd 4G en één simkaart**

    Sommige modellen, zoals GL-E750 (Mudi), hebben een ingebouwde 4G-module met één simkaartsleuf. Raadpleeg [Modellen met één simkaart instellen](#setup-for-single-sim-models).

2. **Modellen met ingebouwd 5G en dual-sim**

    Sommige modellen, zoals GL-X3000 (Spitz AX), hebben een ingebouwde 5G-module met twee simkaartsleuven. De Cellular-instellingen in het webbeheerpaneel kunnen enigszins verschillen. Raadpleeg [Dual-simmodellen instellen](#setup-for-dual-sim-models).

3. **Modellen die compatibel zijn met een USB-modem**

    Sommige modellen, zoals GL-MT3000 (Beryl AX), hebben geen ingebouwde simkaartsleuf maar wel een USB-poort en ondersteunen een mobiel netwerk via een USB-modem. Raadpleeg [Een USB-modem instellen](#setup-for-usb-modem).

**Opmerking:** sommige simkaarten moeten vóór het eerste gebruik worden geactiveerd. Activeer de simkaart in een smartphone voordat je deze in de router plaatst om compatibiliteit te waarborgen.

## Modellen met één simkaart instellen {#setup-for-single-sim-models}

De volgende stappen gelden voor modellen met een ingebouwde modem voor mobiele netwerken en één simkaartsleuf.

In dit voorbeeld gebruiken we **GL-E750 (Mudi)**.

We raden aan de router eerst uit te schakelen, een vooraf geactiveerde simkaart in de sleuf te plaatsen en de router daarna in te schakelen. Als je de simkaart plaatst nadat de router is opgestart, wordt het webbeheerpaneel mogelijk niet automatisch bijgewerkt. Vernieuw in dat geval de pagina of start de router opnieuw op.

### Auto Setup {#auto-setup}

Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**.

1. Wanneer geen simkaart is geplaatst, toont de pagina de melding "Your SIM card has not been detected".

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Plaats een simkaart. Het apparaat begint verbinding te maken, zoals hieronder.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Klik op **Connect** als het apparaat niet automatisch verbinding maakt en de knop beschikbaar is.

    Als de simkaart niet wordt gedetecteerd, start je de router opnieuw op.

3. Zodra de verbinding met het mobiele netwerk tot stand is gebracht, toont de pagina de netwerkgegevens met een groene stip.

    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Als Auto Setup mislukt, probeer je [Manual Setup](#manual-setup-single-sim).

### Manual Setup {#manual-setup-single-sim}

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** en klik op **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Je kunt de instellingen voor het mobiele netwerk van de huidige simkaart bekijken of wijzigen.

**Opmerking**: voor sommige simkaarten is een specifieke APN vereist. Neem contact op met je provider om mogelijke beperkingen te controleren als je simkaart niet kan worden geregistreerd. Configureer zo nodig de juiste APN op je router.

Door de wijzigingen toe te passen, wordt opnieuw verbinding gemaakt.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) is een gatewayparameter die voor een verbinding met een mobiel netwerk vereist is. Hiermee maakt de router verbinding met het internet van je mobiele provider. Je kunt de standaard-APN of een aangepaste APN van je provider gebruiken.

- **Protocol**: het communicatieprotocol voor het mobiele netwerk, zoals 3G, QMI of QCM. Dit wordt gewoonlijk automatisch gedetecteerd en kan aan de vereisten van je modem en provider worden aangepast.

- **Port**: de seriële poort voor communicatie met de mobiele modem. Deze wordt gewoonlijk automatisch gedetecteerd en hoeft niet handmatig te worden aangepast.

- **TTL**: TTL (Time To Live) bepaalt hoe lang pakketten maximaal in het netwerk kunnen blijven. De router verlaagt standaard de TTL van inkomende pakketten van clientapparaten met 1 voordat hij ze doorstuurt. De TTL-instelling geldt alleen voor IPv4.

    **Opmerking**: stel hier een vaste waarde in als je de TTL wilt overschrijven of spoofen. Voer voor de meeste modellen de gewenste effectieve TTL plus 1 in om de automatische verlaging te compenseren. Mudi 7 (GL‑E5800) past de ingevoerde waarde ongewijzigd toe.

- **HL**: bij IPv6 beperkt HL (Hop Limit) het aantal overdrachtshops voor gegevenspakketten in het netwerk en is het gelijkwaardig aan TTL bij IPv4.

- **MTU**: de standaard-MTU is 1500 bytes.

- **Authentication**: kies de verificatiemethode die je provider vereist, zoals NONE, PAP of CHAP. Dit staat gewoonlijk op NONE als geen aanmeldingsgegevens nodig zijn.

- **Band Masking**: schakel Band Masking in als de router bepaalde banden moet blokkeren of alleen specifieke mobiele banden mag gebruiken. Klik [hier](#band-masking) voor meer informatie.

## Dual-simmodellen instellen {#setup-for-dual-sim-models}

De volgende stappen gelden voor modellen met een ingebouwde modem voor mobiele netwerken die twee simkaarten ondersteunt. De pagina's kunnen enigszins afwijken van modellen met één simkaart.

In dit voorbeeld gebruiken we **GL-X3000 (Spitz AX)**. Het ondersteunt Dual SIM, Single Standby: er kunnen twee simkaarten voor mobiele toegang worden geplaatst, maar er is telkens slechts één kaart actief. Je kunt handmatig tussen de kaarten wisselen.

We raden aan de router eerst uit te schakelen, de vooraf geactiveerde simkaart(en) te plaatsen en de router daarna in te schakelen. Als je een simkaart plaatst nadat de router is opgestart, wordt het webbeheerpaneel mogelijk niet automatisch bijgewerkt. Vernieuw in dat geval de pagina of start de router opnieuw op.

### Auto Setup {#auto-setup_1}

Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**.

1. Wanneer geen simkaart is geplaatst, toont de pagina de melding "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Wanneer een simkaart is geplaatst, wordt de pagina als volgt weergegeven. Klik op **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Als de simkaart niet wordt gedetecteerd, start je de router opnieuw op.

3. Zodra de verbinding met het mobiele netwerk tot stand is gebracht, toont de pagina de netwerkgegevens met een groene stip.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Klik op **View More Information** om meer informatie te tonen, waaronder modemgegevens, simkaartgegevens, internetgegevens en het mobiele signaal.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Als Auto Setup mislukt, probeer je [Manual Setup](#manual-setup-dual-sim).

### Manual Setup {#manual-setup-dual-sim}

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** en klik op **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Je kunt de instellingen voor het mobiele netwerk van de huidige simkaart bekijken of wijzigen.

**Opmerking**: voor sommige simkaarten is een specifieke APN vereist. Neem contact op met je provider om mogelijke beperkingen te controleren als je simkaart niet kan worden geregistreerd. Configureer zo nodig de juiste APN op je router.

Door de wijzigingen toe te passen, wordt opnieuw verbinding gemaakt.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) is een gatewayparameter die voor een verbinding met een mobiel netwerk vereist is. Hiermee maakt de router verbinding met het internet van je mobiele provider. Je kunt de standaard-APN of een aangepaste APN van je provider gebruiken.

- **Protocol**: het communicatieprotocol voor het mobiele netwerk, zoals QMI of QCM, dat automatisch op basis van je modem en provider wordt gedetecteerd.

- **Port**: de automatisch gedetecteerde seriële poort voor communicatie met de mobiele modem.

- **TTL**: TTL (Time To Live) bepaalt hoe lang pakketten maximaal in het netwerk kunnen blijven. De router verlaagt standaard de TTL van inkomende pakketten van clientapparaten met 1 voordat hij ze doorstuurt. De TTL-instelling geldt alleen voor IPv4.

    **Opmerking**: stel hier een vaste waarde in als je de TTL wilt overschrijven of spoofen. Voer voor de meeste modellen de gewenste effectieve TTL plus 1 in om de automatische verlaging te compenseren. Mudi 7 (GL‑E5800) past de ingevoerde waarde ongewijzigd toe.

- **HL**: bij IPv6 beperkt HL (Hop Limit) het aantal overdrachtshops voor gegevenspakketten in het netwerk en is het gelijkwaardig aan TTL bij IPv4.

- **MTU**: de standaard-MTU is 1500 bytes.

- **Authentication**: kies de verificatiemethode die je provider vereist, zoals NONE, PAP of CHAP. Dit staat gewoonlijk op NONE als geen aanmeldingsgegevens nodig zijn.

- **Band Masking**: schakel Band Masking in als de router bepaalde banden moet blokkeren of alleen specifieke mobiele banden mag gebruiken. Klik [hier](#band-masking) voor meer informatie.

### Instellingen voor simkaartsleuven {#sim-card-slot-settings}

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** en klik op **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

De knop voor automatisch wisselen, de actieve simkaart, ICCID en Network Operator worden weergegeven.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Als twee simkaarten zijn geplaatst, kun je **Auto Switch** inschakelen.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: schakelt automatisch tussen SIM 1 en SIM 2. De netwerkdetectiemethode voor SIM Auto Switch is gelijk aan de configuratie op de pagina Multi-WAN.

- **Preferred SIM Card Slot**: stel SIM 1 of SIM 2 als voorkeurssimkaart in.

- **Failover Interval**: beschikbare waarden lopen van 5 minuten tot 24 uur.

    Als internet na failover nog niet beschikbaar is, schakelt het apparaat terug naar de voorkeurssleuf en wacht het dit interval voordat failover opnieuw wordt geprobeerd.

    Deze optie geldt wanneer zowel de voorkeurssimkaart als de back-upkaart geen signaal heeft. Het apparaat wisselt tussen de kaarten totdat een geldig signaal wordt verkregen.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Wanneer dit is ingeschakeld, controleert het apparaat dagelijks op het ingestelde tijdstip de voorkeurssleuf en probeert het terug te schakelen als de voorkeurssimkaart weer internettoegang heeft.

    Dit voorkomt overmatig dataverbruik door de back-upkaart. Als de voorkeurssimkaart nog steeds geen signaal heeft, blijft het apparaat de back-upkaart gebruiken.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Opmerking**: Auto Switch schakelt niet onmiddellijk naar een andere simkaart. Het apparaat heeft eerst tijd nodig om vast te stellen dat de huidige kaart geen internettoegang heeft. De andere kaart staat bovendien niet in stand-by en heeft tijd nodig om te activeren.

## Een USB-modem instellen {#setup-for-usb-modem}

De volgende stappen gelden voor modellen zonder ingebouwde simkaartsleuf maar met een USB-poort voor een externe USB-modem.

In dit voorbeeld gebruiken we **GL-MT3000 (Beryl AX)** met de externe USB-modem **SIMPoYo uFi**.

We raden aan de router eerst uit te schakelen, een vooraf geactiveerde simkaart in de USB-modem te plaatsen, de modem op de USB-poort aan te sluiten en de router daarna in te schakelen. Als je de USB-modem aansluit nadat de router is opgestart, wordt het webbeheerpaneel mogelijk niet automatisch bijgewerkt. Vernieuw in dat geval de pagina of start de router opnieuw op.

### Snelle installatie {#quick-setup}

1. Schakel de router uit. Plaats een simkaart in de USB-modem, sluit de modem aan op de USB-poort van de router en schakel de router in.

2. Meld je aan bij het webbeheerpaneel, ga naar **INTERNET** -> **Tethering** en klik op **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Klik op **Advanced** als je geavanceerde instellingen, zoals TTL, HL en MTU, wilt aanpassen en klik vervolgens op **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    De verbinding wordt tot stand gebracht.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Nadat de verbinding tot stand is gebracht, toont de pagina de netwerkgegevens met een groene stip.

    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Opmerking:** na de eerste installatie wordt de USB-modem automatisch herkend wanneer je de router opnieuw opstart terwijl de modem is aangesloten of de modem opnieuw aansluit. De netwerkverbinding wordt tot stand gebracht zonder opnieuw op Connect te klikken.

### Compatibele modems {#compatible-modems}

Hieronder staat een lijst met ondersteunde modems die door ons zijn getest.

**SIMPoYo uFi** is een compacte Plug & Play-USB-dongle met Wi-Fi-hotspot voor snelle, betrouwbare verbindingen op elke locatie. De dongle werkt naadloos met de meeste GL.iNet-routers, laptops, powerbanks, USB-poorten in auto's en andere USB-voedingsbronnen. Je ontvangt 10GB gratis data voor 30 dagen, geldig in het Verenigd Koninkrijk en 34 Europese landen.

| Model                                  | Mobiel netwerk | Type       | Getest door       | Opmerkingen* |
| -------------------------------------- | -------- | ---------- | --------------- | --------- |
| [SIMPoYo SP-N150C4](https://www.gl-inet.com/campaign/simpoyo-ufi/)  | 4G    | USB Dongle | GL.iNet |           |
| Quectel RM520N-GL                      | 5G       | Module     | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | Module     | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | Module     | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | Module     | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | Module     | anonymous       |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | Module     | anonymous       |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | Module     | anonymous       |           |
| Huawei E3276                           | 4G       | USB Dongle | GL.iNet         |           |
| Huawei E3372h-153                      | 4G       | USB Dongle | GL.iNet         | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G       | USB Dongle | anonymous       | Host-less |
| Huawei E3372h-607                      | 4G       | USB Dongle | GL.iNet         |           |
| Huawei K5161h                          | 4G       | USB Dongle | anonymous       |           |
| ZTE MF833U1                            | 4G       | USB Dongle | anonymous       | Host-less |
| ZTE MF79U                              | 4G       | USB Dongle | GL.iNet         | Host-less |
| ZTE M823                               | 4G       | USB Dongle | Arnas Risqianto |           |
| MeiG O4H13 (Qualcomm MDM9207)          | 4G       | USB Dongle | GL.iNet         | Host-less |
| XTRONS 4G LTE USB Dongle               | 4G       | USB Dongle | GL.iNet         | Host-less |

- **QMI**: deze modem ondersteunt de QMI-modus. Selecteer QMI als mobiel communicatieprotocol en **/dev/cdc-wdm0** als seriële poort in de simkaartinstellingen.

- **Host-less**: deze modem ondersteunt Tethering. Beheer de verbinding via de Tethering-interface van de router in plaats van de Cellular-interface.

## Verkeersstatistieken {#traffic-statistics}

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** en klik op **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

De pagina Traffic Statistics wordt geopend. Deze toont het dataverbruik van de simkaart(en) en biedt instellingen voor datalimieten.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Als Data Used hoger is dan Data Cap Amount, wijzig je **Data Cap Amount** of **Data Used** handmatig. Anders kan de netwerkverbinding worden verbroken of kan Auto Switch van de simkaart worden geactiveerd bij dual-simmodellen.

- **Data Used wijzigen**

    Klik rechts van SIM 1/2 Data Used op **Modify**.

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Je kunt vervolgens het dataverbruik wijzigen of resetten.

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Datalimiet voor de simkaart instellen**

    Schakel eerst **Save data when power off** in om een datalimiet voor de simkaart in te stellen. Hierdoor blijven de gegevens bewaard nadat het apparaat is uitgeschakeld.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Schakel vervolgens SIM 1 of SIM 2 Limit Settings in.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Voor dual-simmodellen raden we aan tegelijk **SIM Card Slot Auto Switch** in te schakelen. Als SIM 1 Data Cap Amount is ingesteld en SIM Card Slot Auto Switch is ingeschakeld, schakelt SIM 1 automatisch naar SIM 2 wanneer de limiet wordt overschreden en wordt SIM 1 uitgeschakeld.

## Historisch signaaloverzicht {#historical-signal-record}

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** en klik op **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Hier kun je de kwaliteit van de mobiele verbinding controleren. Probeer bij een zwak signaal naar een andere zendmast over te schakelen.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Bekijk de geschiedenis van de signaalsterkte door rechtsboven een andere periode te selecteren.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Band Masking {#band-masking}

Met Band Masking kun je bepaalde banden blokkeren of alleen voorkeursbanden gebruiken om een zwak mobiel signaal te verbeteren.

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular** -> **SIM Card Settings** en schakel **Enable Band Masking** in.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Selecteer **Masking Mode** (Block of Open) en vervolgens LTE Bands, 5G NSA Bands en 5G SA Bands.

## SMS {#sms}

Raadpleeg [SMS](../tutorials/sms.md).

## SMS Forwarding {#sms-forwarding}

Raadpleeg [SMS doorsturen](../tutorials/sms_forwarding.md).

## Zendmast vergrendelen {#lock-tower}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) ondersteunt deze functie in firmware v4.7 en hoger.

Je kunt een zendmast vergrendelen om een hoogwaardig signaal en een stabiele mobiele verbinding te verkrijgen.

**Opmerking:** de vergrendelde zendmast moet overeenkomen met de frequentiebanden die je provider en apparaat ondersteunen. Anders kan de verbinding mislukken.

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular**. Klik rechtsboven op het pictogram met drie stippen en selecteer **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Klik op **Scan** om naar zendmasten te scannen. Dit duurt enkele minuten. Vernieuw de pagina niet tijdens het scannen.

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

De beschikbare zendmasten worden weergegeven.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Klik op een zendmast om de gegevens te bekijken en deze te vergrendelen.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Note**:

1. Wanneer de Cellular-interface is ingeschakeld, kan het apparaat mogelijk niet alle zendmasten scannen.

2. Als de vergrendelde zendmast niet overeenkomt met de Band Masking- of APN-parameters in de mobiele instellingen, kan de router geen verbinding maken met het mobiele netwerk.

3. Nadat je een zendmast hebt vergrendeld, probeert de router na een herstart opnieuw verbinding te maken met die mast, ook als je de router hebt verplaatst. Hierdoor kan de router op de nieuwe locatie mogelijk niet automatisch verbinding maken met het mobiele netwerk. Ontgrendel in dat geval de huidige zendmast of vergrendel handmatig een nieuwe mast.

## Provider vergrendelen {#lock-operator}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) ondersteunt deze functie in firmware v4.8 en hoger.

Door een specifieke mobiele provider te vergrendelen, gebruikt de router alleen het netwerk van die provider. Dit zorgt voor een stabiele verbinding en voorkomt onbedoelde roamingkosten, vooral in grensgebieden waar het apparaat anders met buitenlandse netwerken kan verbinden.

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular**. Klik rechtsboven op het pictogram met drie stippen en selecteer **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Er zijn drie vergrendelingsmodi:

- **Auto**: maakt automatisch verbinding met een beschikbaar providernetwerk.
- **Manual**: vergrendelt handmatig een specifieke provider.
- **Manual-Auto**: schakelt automatisch naar een beschikbaar providernetwerk als handmatig vergrendelen mislukt.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## AT-opdrachten voor de modem {#modem-at-command}

AT-opdrachten zijn standaardinstructies voor communicatie met de mobiele modem. Met deze functie kun je opdrachten verzenden en de modemstatus controleren.

Ga in het webbeheerpaneel naar **INTERNET** -> **Cellular**. Klik rechtsboven op het pictogram met drie stippen en selecteer **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

De pagina AT Command wordt geopend.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Wanneer Shortcut op **Manual command** staat, kun je de gewenste opdracht in het veld AT Command invoeren.

Je kunt ook in de vervolgkeuzelijst Shortcut een van de **vooraf ingestelde opdrachten** selecteren.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

De volgende opdrachten zijn vooraf ingesteld:

* IMEI opvragen
* QCCID opvragen
* IMSI opvragen
* Signaalkwaliteit controleren
* Modem resetten
* Providernamen
* Simkaartstatus opvragen

In dit voorbeeld is de snelkoppeling "Request IMEI" geselecteerd. Klik op "Send" om het onderstaande resultaat te ontvangen.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

Klik rechtsonder op **Export Debug Info** om een .json-bestand te downloaden.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Probleemoplossing {#troubleshooting}

Als geen mobiele verbinding tot stand kan worden gebracht, klik je op de onderstaande foutmelding voor oplossingen.

??? note "Geen simkaart/Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Hieronder staan enkele suggesties voor probleemoplossing.

    1. Vernieuw de pagina en wacht enkele minuten om te controleren of de simkaart wordt gedetecteerd.

    2. Controleer of de simkaart correct is geplaatst. Lijn de inkeping op de kaart uit met de markering op de sleuf.

    3. Schakel de router uit, verwijder de simkaart, plaats deze opnieuw en schakel de router weer in.

    4. Probeer indien beschikbaar een andere simkaart.

    Als het probleem aanhoudt, download je de logboeken en stuur je deze naar [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Simkaart niet geregistreerd/de interface is verbonden, maar internet is niet toegankelijk"

    Dit probleem heeft twee soorten foutmeldingen:

    - Simkaart niet geregistreerd

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - De interface is verbonden, maar internet is niet toegankelijk

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Hieronder staan enkele suggesties voor probleemoplossing.

    1. Vernieuw de pagina en wacht enkele minuten om te controleren of de fout verdwijnt.

    2. Klik op **Disconnect**/**Abort** en vervolgens op **Connect** om opnieuw verbinding te maken.

    3. Start de router opnieuw op.

    4. Controleer de status en activering van de simkaart. Plaats de kaart in een smartphone om met een actieve databundel de internettoegang te testen of neem contact op met je provider.

    5. Sommige providers vereisen een 3G-protocol. Ga naar **SIM Card Settings** -> **Protocol**, selecteer **3G** en klik op **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Het apparaat maakt automatisch opnieuw verbinding. Wacht enkele minuten en controleer of de verbinding tot stand komt.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Als de verbinding tot stand is gebracht, wordt de pagina als volgt weergegeven.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Sommige simkaarten hebben gebruiksbeperkingen, zoals een specifieke APN. Neem contact op met je provider om beperkingen te controleren als de simkaart niet wordt geregistreerd.

        Ga zo nodig naar **SIM Card Settings** -> **APN**, configureer de juiste APN en klik op **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Klik op **View More Information** om de mobiele signaalsterkte te controleren. Controleer bij een zwak signaal of de antenne correct is geïnstalleerd en plaats de router op een open locatie zonder obstakels.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. Controleer of **Band Masking** of **Lock Tower** is ingeschakeld. Schakel de functie uit en probeer opnieuw verbinding te maken.

    Als het probleem aanhoudt, download je de logboeken en stuur je deze naar [support@gl-inet.com](mailto:support@gl-inet.com).

## IoT-certificering {#iot-certification}

### AT&T-certificering {#att-certification}

Open [att device certification](https://iotdevices.att.com/certified-devices.aspx#) en voer de apparaatnaam in om het apparaat te vinden.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile-certificering {#t-mobile-certification}

Open [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification){target="_blank"} en kies 5G onder **Filter** om het apparaat te vinden.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Gerelateerde artikelen

- [Internetpagina](internet.md)
- [Hoe stel je de prioriteit van elke methode voor internettoegang in?](multi-wan.md)
- [Hoe stel je load balancing in wanneer meerdere methoden voor internettoegang tegelijk worden gebruikt?](multi-wan.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
