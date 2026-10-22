# Via een mobiel netwerk verbinding maken met internet (v4.7 en ouder) {#connect-to-the-internet-via-cellular-v47-and-earlier}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.7 en ouder. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.7 en ouder" markdown="1">

- [Firmware v4.10 en hoger](internet_cellular_v4.10.md)
- [Firmware v4.8-v4.9](internet_cellular.md)

</div>

---

De meeste GL.iNet-routers ondersteunen verbindingen met mobiele netwerken. Deze handleiding behandelt drie soorten modellen:

1. **Modellen met ingebouwd 4G en één simkaart**

    Sommige modellen, zoals GL-XE300 (Puli), hebben een ingebouwde 4G-module met één simkaartsleuf. Raadpleeg [Modellen met één simkaart instellen](#setup-for-single-sim-models).

2. **Modellen die compatibel zijn met een USB-modem**

    Sommige modellen, zoals GL-AXT1800 (Slate AX), hebben een USB-poort en ondersteunen een mobiel netwerk via een USB-modem. De stappen zijn vergelijkbaar met modellen met ingebouwd 4G en één simkaart. Raadpleeg [Modellen met één simkaart instellen](#setup-for-single-sim-models).

3. **Modellen met ingebouwd 5G en dual-sim**

    Sommige modellen, zoals GL-X3000 (Spitz AX), hebben een ingebouwde 5G-module met twee simkaartsleuven. De Cellular-instellingen in het webbeheerpaneel kunnen enigszins verschillen. Raadpleeg [Dual-simmodellen instellen](#setup-for-dual-sim-models).

**Opmerking:** sommige simkaarten moeten vóór het eerste gebruik worden geactiveerd. Activeer de simkaart in een smartphone voordat je deze in de router plaatst om compatibiliteit te waarborgen.

## Modellen met één simkaart instellen {#setup-for-single-sim-models}

De volgende stappen gelden voor modellen met een ingebouwde mobiele modem en één simkaartsleuf, zoals GL-XE300 Puli, of een USB-poort voor een externe USB-modem, zoals GL-AXT1800 Slate AX.

In dit voorbeeld gebruiken we **GL-AXT1800 (Slate AX)** met een externe USB-modem.

We raden aan de router eerst uit te schakelen. Plaats een vooraf geactiveerde simkaart in de USB-modem, sluit de modem op de USB-poort aan en schakel de router daarna in.

Als je de USB-modem aansluit nadat de router is opgestart, wordt het webbeheerpaneel mogelijk niet automatisch bijgewerkt. Vernieuw in dat geval de pagina of start de router opnieuw op.

### Auto Setup {#auto-setup}

Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**.

1. Bij de eerste toegang wordt mogelijk niet automatisch verbinding gemaakt, maar linksboven moeten de naam van je provider en de IMEI worden weergegeven. Klik op **Auto Setup**.

    Negeer de waarschuwing *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. De verbinding wordt tot stand gebracht.

    **Opmerking:** sommige simkaarten hebben gebruiksbeperkingen, zoals een specifieke APN. Neem contact op met je provider om beperkingen te controleren als de simkaart niet wordt geregistreerd.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Nadat de verbinding tot stand is gebracht, toont de pagina de netwerkgegevens met een groene stip.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Opmerking:** na de eerste installatie wordt de USB-modem automatisch herkend wanneer je de router opnieuw opstart terwijl de modem is aangesloten of de modem opnieuw aansluit. De netwerkverbinding wordt tot stand gebracht zonder opnieuw op Auto Setup te klikken.

Als Auto Setup mislukt, probeer je [Manual Setup](#manual-setup).

### Manual Setup {#manual-setup}

Klik in het gedeelte Cellular op **Manual Setup** om de mobiele instellingen van de huidige simkaart te bekijken of wijzigen.

**Opmerking**: voor sommige simkaarten is een specifieke APN vereist. Neem contact op met je provider om mogelijke beperkingen te controleren als je simkaart niet kan worden geregistreerd. Configureer zo nodig de juiste APN op je router.

Door de wijzigingen toe te passen, wordt opnieuw verbinding gemaakt.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: het communicatieprotocol voor het mobiele netwerk, zoals 3G, QMI of QCM. Dit wordt gewoonlijk automatisch gedetecteerd en kan aan de vereisten van je modem en provider worden aangepast.

- **Port**: de seriële poort voor communicatie met de mobiele modem. Deze wordt gewoonlijk automatisch gedetecteerd en hoeft niet handmatig te worden aangepast.

- **APN**: APN (Access Point Name) is een gatewayparameter die voor een verbinding met een mobiel netwerk vereist is. Hiermee maakt de router verbinding met het internet van je mobiele provider. Je kunt de standaard-APN of een aangepaste APN van je provider gebruiken.

- **PIN**: voer hier de pincode in als je simkaart ermee is beveiligd. Dit veld is optioneel als geen pincode is ingesteld.

- **TTL**: TTL (Time To Live) bepaalt hoe lang pakketten maximaal in het netwerk kunnen blijven. De router verlaagt standaard de TTL van inkomende pakketten van clientapparaten met 1 voordat hij ze doorstuurt. De TTL-instelling geldt alleen voor IPv4.

    **Opmerking**: stel hier een vaste waarde in als je de TTL wilt overschrijven of spoofen. Voer voor de meeste modellen de gewenste effectieve TTL plus 1 in om de automatische verlaging te compenseren. Mudi 7 (GL‑E5800) past de ingevoerde waarde ongewijzigd toe.

- **Service**: selecteer het type mobiele dienst om te bepalen welke netwerktechnologieën de modem gebruikt.

- **Dial Number**: voer het inbelnummer van je provider in. Dit is vaak vooraf geconfigureerd en kan bij de meeste moderne netwerken leeg blijven.

- **Authentication**: kies de verificatiemethode die je provider vereist, zoals NONE, PAP of CHAP. Dit staat gewoonlijk op NONE als geen aanmeldingsgegevens nodig zijn.

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

- **QMI**: deze modem ondersteunt de QMI-modus. Selecteer QMI als protocol en **/dev/cdc-wdm0** als seriële poort.

- **Host-less**: deze modem ondersteunt Tethering. Beheer de verbinding via de Tethering-interface van de router in plaats van de Cellular-interface.

## Dual-simmodellen instellen {#setup-for-dual-sim-models}

De volgende stappen gelden voor modellen met een ingebouwde mobiele modem die twee simkaarten ondersteunt. Het webbeheerpaneel kan enigszins afwijken van modellen met één simkaart.

In dit voorbeeld gebruiken we **GL-X3000 (Spitz AX)**. Het ondersteunt Dual SIM, Single Standby: er kunnen twee simkaarten voor mobiele toegang worden geplaatst, maar er is telkens slechts één kaart actief. Je kunt handmatig tussen de kaarten wisselen.

We raden aan de router eerst uit te schakelen, de vooraf geactiveerde simkaart(en) te plaatsen en de router daarna in te schakelen. Als je een simkaart plaatst nadat de router is opgestart, wordt het webbeheerpaneel mogelijk niet automatisch bijgewerkt. Vernieuw in dat geval de pagina of start de router opnieuw op.

### Auto Setup {#auto-setup_1}

Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**.

1. Wanneer geen simkaart is geplaatst, wordt de pagina als volgt weergegeven.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Wanneer een simkaart is geplaatst, maakt de router automatisch verbinding.

    Als de verbinding tot stand is gebracht, wordt de pagina als volgt weergegeven.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Als geen automatische verbinding wordt gemaakt, klik je op **Auto Setup** en wacht je of probeer je **Manual Setup**.

### Manual Setup {#manual-setup_1}

Klik in het gedeelte Cellular op **Manual Setup** om Cellular Settings te openen.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Je kunt de mobiele instellingen van de huidige simkaart bekijken of wijzigen. Er zijn ook vooraf geconfigureerde profielen opgeslagen en je kunt handmatig configuraties aan "Saved Settings" toevoegen.

### Instellingen voor simkaartsleuven {#sim-card-slot-settings}

Klik in het gedeelte Cellular op **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

De pagina **SIM Card Slot Settings** wordt geopend.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Als twee simkaarten zijn geplaatst, kun je **Auto Switch** inschakelen.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

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

## Verkeersstatistieken {#traffic-statistics}

Klik in het gedeelte Cellular op **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

De pagina Traffic Statistics wordt geopend.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS {#sms}

Raadpleeg [SMS](../tutorials/sms.md).

## SMS Forwarding {#sms-forwarding}

Raadpleeg [SMS doorsturen](../tutorials/sms_forwarding.md).

## Modembeheer {#modem-management}

Klik in het gedeelte Cellular rechtsboven op **Tool** om de pagina Modem Management te openen.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

De pagina bevat **Modem Info** en **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

AT-opdrachten zijn standaardinstructies voor communicatie met de mobiele modem.

Wanneer Shortcut op **Manual command** staat, voer je de gewenste opdracht in het veld AT Command in om de modemstatus te controleren.

Je kunt ook in de vervolgkeuzelijst Shortcut een van de **vooraf ingestelde opdrachten** selecteren.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

De volgende opdrachten zijn vooraf ingesteld:

* IMEI opvragen
* QCCID opvragen
* IMSI opvragen
* Signaalkwaliteit controleren
* Modem resetten
* Providernamen
* Simkaartstatus opvragen

In dit voorbeeld is "Request IMEI" geselecteerd. Klik op "Send" om het onderstaande resultaat te ontvangen.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Providerprofiel {#carrier-profile}

Je kunt verschillende profielen voor dezelfde of verschillende providers opslaan.

Klik in het gedeelte Cellular rechtsboven op **Profile** om profielen te beheren.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Voeg een nieuw profiel toe of sla het huidige profiel op.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Maak je eigen profiel op basis van de vereisten van je provider.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Je kunt de volgende keer een opgeslagen profiel selecteren.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Kies de benodigde profielen.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Zendmast vergrendelen {#lock-tower}

Deze functie is alleen beschikbaar op bepaalde modellen, zoals GL-X3000, GL-XE3000 en GL-X2000 met firmware v4.7 of hoger.

Je kunt een zendmast vergrendelen om een hoogwaardig signaal en een stabiele mobiele verbinding te verkrijgen.

**Opmerking:** de vergrendelde zendmast moet overeenkomen met de frequentiebanden die je provider en apparaat ondersteunen. Anders kan de verbinding mislukken.

Klik in het gedeelte Cellular rechtsboven op het pictogram **Tower**.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

De beschikbare zendmasten worden weergegeven.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Klik op een zendmast om de gegevens te bekijken en deze te vergrendelen.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

Bovenaan wordt de status van de zendmast weergegeven, zoals Locked of Unlocked.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Note**:

1. Wanneer de Cellular-interface is ingeschakeld, kan het apparaat mogelijk niet alle zendmasten scannen.

2. Als de vergrendelde zendmast niet overeenkomt met de Band Masking- of APN-parameters in de mobiele instellingen, kan de router geen verbinding maken met het mobiele netwerk.

3. Nadat je een zendmast hebt vergrendeld, probeert de router na een herstart opnieuw verbinding te maken met die mast, ook als je de router hebt verplaatst. Hierdoor kan de router op de nieuwe locatie mogelijk niet automatisch verbinding maken met het mobiele netwerk. Ontgrendel in dat geval de huidige zendmast of vergrendel handmatig een nieuwe mast.

## Historisch signaaloverzicht {#historical-signal-record}

Klik in het gedeelte Cellular rechtsboven op **Signal** om de historische signaalsterkte te controleren.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Hiermee kun je de kwaliteit van de mobiele verbinding bepalen. Probeer bij een zwak signaal naar een andere zendmast over te schakelen.

Je kunt de geschiedenis van de mobiele signaalsterkte bekijken door verschillende perioden te selecteren.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking {#band-masking}

Klik in het gedeelte Cellular op **View More** en selecteer **Cells Info** om de celgegevens te bekijken.

De gebruikte banden en hun signaalstatus worden weergegeven.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Bij een zwak signaal kun je Band Masking inschakelen om bepaalde banden te blokkeren. Bij een goed signaal kun je de router alleen specifieke mobiele banden laten gebruiken.

Klik op **Manual Setup** om Cellular Settings te openen en schakel **Band Masking** in.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Selecteer **Masking Mode** (Block of Open) en vervolgens LTE Bands, 5G NSA Bands en 5G SA Bands.

## Probleemoplossing {#troubleshooting}

Als geen mobiele verbinding tot stand kan worden gebracht, klik je op de onderstaande foutmelding voor oplossingen.

??? note "Geen simkaart/Your SIM card has not been detected"

    1. Vernieuw de pagina en wacht enkele minuten om te controleren of de simkaart wordt gedetecteerd.

    2. Controleer of de simkaart correct is geplaatst. Lijn de inkeping op de kaart uit met de markering op de sleuf.

    3. Schakel de router uit, verwijder de simkaart, plaats deze opnieuw en schakel de router weer in.

    4. Probeer indien beschikbaar een andere simkaart.

    Als het probleem aanhoudt, download je de logboeken en stuur je deze naar [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Simkaart niet geregistreerd/de interface is verbonden, maar internet is niet toegankelijk"

    1. Vernieuw de pagina en wacht enkele minuten om te controleren of de fout verdwijnt.

    2. Klik op **Disconnect**/**Abort** en vervolgens op **Connect** om opnieuw verbinding te maken.

    3. Start de router opnieuw op.

    4. Controleer de status en activering van de simkaart. Plaats de kaart in een smartphone om met een actieve databundel de internettoegang te testen of neem contact op met je provider.

    5. Sommige providers vereisen een 3G-protocol. Ga naar **Manual Setup** -> **Cellular Settings** -> **Protocol**, selecteer **3G** en klik op **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Het apparaat maakt automatisch opnieuw verbinding. Wacht enkele minuten en controleer of de verbinding tot stand komt.

    6. Sommige simkaarten hebben gebruiksbeperkingen, zoals een specifieke APN. Neem contact op met je provider om beperkingen te controleren als de simkaart niet wordt geregistreerd.

        Ga zo nodig naar **Manual Setup** -> **Cellular Settings** -> **APN**, configureer de juiste APN en klik op **Apply**.

    7. Klik op **View More** en selecteer **Cells Info** om de mobiele signaalsterkte te controleren. Controleer bij een zwak signaal of de antenne correct is geïnstalleerd en plaats de router op een open locatie zonder obstakels.

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
