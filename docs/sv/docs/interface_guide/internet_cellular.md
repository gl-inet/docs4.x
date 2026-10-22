# Anslut till internet via mobilnät (v4.8-v4.9) {#connect-to-the-internet-via-cellular-v48-v49}

Innehållet bygger på firmwareversionerna v4.8-v4.9. Om enheten kör en annan version använder du väljaren nedan för att byta guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.8 - v4.9" markdown="1">

- [Firmware v4.10 and above](internet_cellular_v4.10.md)
- [Firmware v4.7 and earlier](internet_cellular_v4.7.md)

</div>

---

De flesta GL.iNet-routrar stöder mobilnätsanslutning. Guiden omfattar tre modelltyper:

1. **Built-in 4G Single-SIM models**

    Vissa modeller, till exempel GL-E750 (Mudi), har en inbyggd 4G-modul och en SIM-kortplats. Se [Konfiguration för modeller med ett SIM-kort](#setup-for-single-sim-models).

2. **Built-in 5G Dual-SIM models**

    Vissa modeller, till exempel GL-X3000 (Spitz AX), har en inbyggd 5G-modul och dubbla SIM-kortplatser. Mobilnätsinställningarna kan skilja sig något. Se [Konfiguration för modeller med dubbla SIM-kort](#setup-for-dual-sim-models).

3. **USB Modem compatible models**

    Vissa modeller, till exempel GL-MT3000 (Beryl AX), saknar inbyggd SIM-kortplats men har USB-port och stöder mobilnät via USB-modem. Se [Konfiguration för USB-modem](#setup-for-usb-modem).

**Note:** Some SIM cards require activation before first use. To ensure compatibility, activate the SIM card in a smartphone before inserting it into the router.

## Setup for Single-SIM models {#setup-for-single-sim-models}

Följande steg gäller modeller med inbyggt mobilmodem och en SIM-kortplats.

Here we use the **GL-E750 (Mudi)** as an example.

Stäng först av routern, sätt in ett föraktiverat SIM-kort och slå sedan på routern. Om kortet sätts in efter start kanske webbadministrationspanelen inte uppdateras automatiskt. Uppdatera då sidan eller starta om routern.

### Auto Setup {#auto-setup}

Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

1. När inget SIM-kort är isatt visas "Your SIM card has not been detected".

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Insert a SIM card. The device will start connecting as shown below.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Om anslutningen inte upprättas automatiskt klickar du på **Connect** om knappen finns.

    Om SIM-kortet inte identifieras startar du om routern och kontrollerar igen.

3. När mobilnätet är anslutet visas nätverksinformationen med en grön punkt.

    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Om Auto Setup misslyckas provar du [Manual Setup](#manual-setup-single-sim).

### Manual Setup {#manual-setup-single-sim}

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular**, then click **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Du kan visa eller ändra mobilnätsinställningarna för aktuellt SIM-kort.

**Obs!** Vissa SIM-kort kräver ett visst APN. Kontakta operatören om kortet inte registreras och kontrollera begränsningar. Konfigurera rätt APN vid behov.

Applying the changes will trigger a reconnection.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) är en gatewayparameter som krävs för mobilnätsanslutning. Använd standard-APN eller ett eget APN från operatören.

- **Protocol**: Mobilkommunikationsprotokollet, till exempel 3G, QMI eller QCM. Det identifieras vanligtvis automatiskt men kan ändras efter modemets och operatörens krav.

- **Port**: Serieporten för kommunikation med mobilmodemet. Den identifieras vanligtvis automatiskt.

- **TTL**: TTL (Time To Live) anger maximal tid för paket i nätverket. Routern minskar som standard TTL för inkommande klientpaket med 1 före vidarebefordran. Gäller endast IPv4.

    **Obs!** Ange ett fast värde för att åsidosätta eller förfalska TTL. På de flesta modeller anger du önskad effektiv TTL plus 1. Mudi 7 (GL‑E5800) använder värdet utan ändring.

- **HL**: I IPv6 begränsar HL (Hop Limit) antalet överföringshopp och motsvarar TTL i IPv4.

- **MTU**: The default MTU value is 1500 bytes.

- **Authentication**: Välj operatörens autentiseringsmetod, till exempel NONE, PAP eller CHAP. NONE används vanligtvis utan inloggningsuppgifter.

- **Band Masking**: Aktivera för att blockera vissa band eller endast använda angivna mobilband. Mer information finns [här](#band-masking).

## Setup for Dual-SIM models {#setup-for-dual-sim-models}

Följande steg gäller modeller med inbyggt mobilmodem och dubbla SIM-kort. Sidorna kan skilja sig något från modeller med ett SIM-kort.

**GL-X3000 (Spitz AX)** används som exempel. Dual SIM, Single Standby innebär att två SIM-kort kan vara isatta men endast ett är aktivt åt gången. Du kan växla manuellt.

Stäng först av routern, sätt in föraktiverade SIM-kort och slå sedan på routern. Om kort sätts in efter start kanske webbadministrationspanelen inte uppdateras automatiskt. Uppdatera sidan eller starta om routern.

### Auto Setup {#auto-setup_1}

Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

1. När inget SIM-kort är isatt visas "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. När ett SIM-kort är isatt visas sidan nedan. Klicka på **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Om SIM-kortet inte identifieras startar du om routern och kontrollerar igen.

3. När mobilnätet är anslutet visas nätverksinformationen med en grön punkt.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Klicka på **View More Information** för modem-, SIM-, internet- och signalinformation.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Om Auto Setup misslyckas provar du [Manual Setup](#manual-setup-dual-sim).

### Manual Setup {#manual-setup-dual-sim}

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular**, then click **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Du kan visa eller ändra mobilnätsinställningarna för aktuellt SIM-kort.

**Obs!** Vissa SIM-kort kräver ett visst APN. Kontakta operatören om kortet inte registreras och kontrollera begränsningar. Konfigurera rätt APN vid behov.

Applying the changes will trigger a reconnection.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) är en gatewayparameter som krävs för mobilnätsanslutning. Använd standard-APN eller ett eget APN från operatören.

- **Protocol**: Mobilkommunikationsprotokollet, till exempel QMI eller QCM, som identifieras automatiskt utifrån modem och operatör.

- **Port**: Den automatiskt identifierade serieporten för kommunikation med mobilmodemet.

- **TTL**: TTL (Time To Live) anger maximal tid för paket i nätverket. Routern minskar som standard TTL för inkommande klientpaket med 1 före vidarebefordran. Gäller endast IPv4.

    **Obs!** Ange ett fast värde för att åsidosätta eller förfalska TTL. På de flesta modeller anger du önskad effektiv TTL plus 1. Mudi 7 (GL‑E5800) använder värdet utan ändring.

- **HL**: I IPv6 begränsar HL (Hop Limit) antalet överföringshopp och motsvarar TTL i IPv4.

- **MTU**: The default MTU value is 1500 bytes.

- **Authentication**: Välj operatörens autentiseringsmetod, till exempel NONE, PAP eller CHAP. NONE används vanligtvis utan inloggningsuppgifter.

- **Band Masking**: Aktivera för att blockera vissa band eller endast använda angivna mobilband. Mer information finns [här](#band-masking).

### SIM Card Slot Settings {#sim-card-slot-settings}

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular**, then click **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Sidan visar knappen för automatisk växling, aktivt SIM-kort, ICCID och Network Operator.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Om två SIM-kort är isatta kan du aktivera **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: Aktiverar automatisk växling mellan SIM 1 och SIM 2. Nätverksidentifieringen är samma som på sidan Multi-WAN.

- **Preferred SIM Card Slot**: Ange SIM 1 eller SIM 2 som föredraget SIM-kort.

- **Failover Interval**: Available values range from 5 minutes to 24 hours.

    Om internet fortfarande saknas efter failover växlar enheten tillbaka till den föredragna kortplatsen och väntar detta intervall före nytt försök.

    Alternativet gäller när både föredraget och reservkort saknar signal. Enheten växlar tills ett kort får giltig signal.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Enheten kontrollerar den föredragna kortplatsen dagligen vid angiven tid och försöker växla tillbaka om internetåtkomst återfås.

    Det förhindrar hög dataförbrukning på reservkortet. Om föredraget kort saknar signal fortsätter reservkortet att användas.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Obs!** Auto Switch växlar inte omedelbart. Enheten måste först bekräfta att aktuellt SIM saknar internet, och det andra kortet måste aktiveras eftersom det inte är i vänteläge.

## Setup for USB modem {#setup-for-usb-modem}

Följande steg gäller modeller utan inbyggd SIM-kortplats men med USB-port för externt USB-modem.

**GL-MT3000 (Beryl AX)** med det externa USB-modemet **SIMPoYo uFi** används som exempel.

Stäng av routern, sätt ett föraktiverat SIM-kort i USB-modemet, anslut modemet till USB-porten och slå på routern. Om modemet ansluts efter start kanske webbadministrationspanelen inte uppdateras automatiskt. Uppdatera sidan eller starta om routern.

### Quick Setup {#quick-setup}

1. Stäng av routern, sätt ett SIM-kort i USB-modemet, anslut modemet till routerns USB-port och slå på routern.

2. Log in to the router's web Admin Panel, navigate to **INTERNET** -> **Tethering**, then click **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Klicka vid behov på **Advanced** för TTL, HL och MTU och klicka sedan på **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    It will start connecting.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. När anslutningen är klar visas nätverksinformationen med en grön punkt.

    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Obs!** Efter första konfigurationen identifieras modemet automatiskt efter omstart eller återanslutning och nätverket ansluts utan att Connect behöver klickas igen.

### Compatible Modems {#compatible-modems}

Nedan visas testade modem som stöds.

**SIMPoYo uFi** är en kompakt plug-and-play-USB-dongel med Wi-Fi-hotspot för snabb och tillförlitlig anslutning. Den fungerar med de flesta GL.iNet-routrar, bärbara datorer, powerbanker, bilars USB-portar och andra USB-strömkällor. Den innehåller 10GB kostnadsfri data i 30 dagar i Storbritannien och 34 europeiska länder.

| Model                                  | Cellular | Type       | Tested by       | Comments* |
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

- **QMI**: Modemet stöder QMI. Välj QMI som mobilkommunikationsprotokoll och **/dev/cdc-wdm0** som serieport i SIM-kortsinställningarna.

- **Host-less**: Modemet stöder Tethering. Hantera anslutningen via Tethering-gränssnittet i stället för Cellular.

## Traffic Statistics {#traffic-statistics}

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular**, then click **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Sidan Traffic Statistics öppnas. Den visar SIM-kortens dataanvändning och inställningar för datagränser.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Om Data Used överstiger Data Cap Amount ändrar du **Data Cap Amount** eller **Data Used** manuellt. Annars kan nätverket kopplas från eller SIM-kortet växlas med Auto Switch på modeller med dubbla SIM-kort.

- **Modify the Data Used**

    Klicka på **Modify** till höger om SIM 1/2 Data Used.

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Ändra eller återställ sedan dataanvändningen.

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Set up SIM data limit**

    Aktivera först **Save data when power off** för att ange en datagräns. Då sparas data även när enheten stängs av.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Aktivera sedan SIM 1 eller SIM 2 Limit Settings.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

På modeller med dubbla SIM-kort rekommenderas samtidig aktivering av **SIM Card Slot Auto Switch**. När SIM 1 Data Cap Amount har angetts växlar SIM 1 automatiskt till SIM 2 när gränsen överskrids och SIM 1 inaktiveras.

## Historical Signal Record {#historical-signal-record}

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular**, then click **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Här kan du kontrollera mobilanslutningens kvalitet. Vid svag signal kan du prova en annan mast.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

View the signal strength history by selecting different time frames in the upper-right corner.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Band Masking {#band-masking}

Band Masking allows you to block specific bands or use only preferred cellular bands to improve weak cellular signal.

In the router's web Admin Panel, navigate to **INTERNET** -> **Cellular** -> **SIM Card Settings**, toggle on **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Välj **Masking Mode** (Block eller Open) och välj sedan LTE Bands, 5G NSA Bands och 5G SA Bands.

## SMS {#sms}

Please refer to [SMS](../tutorials/sms.md).

## SMS Forwarding {#sms-forwarding}

Please refer to [SMS Forwarding](../tutorials/sms_forwarding.md).

## Lock Tower {#lock-tower}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) stöder funktionen i firmware v4.7 eller senare.

Lås en mobilmast för att försöka få en stark och stabil signal.

**Obs!** Den låsta masten måste matcha frekvensbanden som operatören och enheten stöder, annars kan anslutningen misslyckas.

Öppna **INTERNET** -> **Cellular** i webbadministrationspanelen. Klicka på ikonen med tre punkter uppe till höger och välj **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Klicka på **Scan** för att söka efter mobilmaster. Det tar några minuter. Uppdatera inte sidan under sökningen.

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

It will display the available towers.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Klicka på en mast för att visa information och låsa den.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Note**:

1. Enheten kanske inte kan söka efter alla master när Cellular-gränssnittet är aktiverat.

2. Om den låsta masten inte matchar bandmaskering eller APN-parametrar kan routern inte ansluta till mobilnätet.

3. Om routern flyttas försöker den fortfarande ansluta till den låsta masten efter omstart. Det kan hindra automatisk anslutning på den nya platsen. Lås upp masten eller lås manuellt en ny.

## Lock Operator {#lock-operator}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) stöder funktionen i firmware v4.8 eller senare.

Genom att låsa en mobiloperatör använder routern endast dennes nätverk. Det ger stabil anslutning och undviker oavsiktliga roamingavgifter, särskilt nära landsgränser.

Öppna **INTERNET** -> **Cellular**, klicka på ikonen med tre punkter uppe till höger och välj **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

There are three locking modes:

- **Auto**: Automatically connect to an available operator network.
- **Manual**: Manually lock onto a specific operator.
- **Manual-Auto**: Växlar automatiskt till ett tillgängligt operatörsnätverk om manuell låsning misslyckas.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Modem AT Command {#modem-at-command}

Modemets AT-kommandon är standardinstruktioner för kommunikation med mobilmodemet. Du kan skicka kommandon och kontrollera modemstatus.

Öppna **INTERNET** -> **Cellular**, klicka på ikonen med tre punkter uppe till höger och välj **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Sidan AT Command öppnas.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

När Shortcut är **Manual command** kan du skriva kommandot i fältet AT Command.

Du kan även välja bland **förinställda kommandon** i listrutan Shortcut.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Följande kommandon är förinställda:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

I exemplet väljs "Request IMEI". Klicka på "Send" för att visa resultatet.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

Klicka på **Export Debug Info** nere till höger för att hämta en .json-fil.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Troubleshooting {#troubleshooting}

Om mobilanslutningen misslyckas klickar du på felmeddelandet nedan för lösningar.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Here are some suggestions for troubleshooting.

    1. Uppdatera sidan, vänta några minuter och kontrollera om SIM-kortet identifieras.

    2. Kontrollera att SIM-kortet är rätt installerat. Rikta kortets skåra mot markeringen på kortplatsen.

    3. Stäng av routern, ta ut och sätt tillbaka SIM-kortet och slå på routern.

    4. Try using another SIM card if available.

    Om problemet kvarstår hämtar du loggarna och skickar dem till [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Problemet har två typer av felmeddelanden:

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Here are some suggestions for troubleshooting.

    1. Uppdatera sidan och vänta några minuter för att se om felet försvinner.

    2. Klicka på **Disconnect**/**Abort** och sedan på **Connect** för att återansluta.

    3. Restart the router.

    4. Kontrollera SIM-kortets status och att det är aktiverat. Prova kortet i en smartphone med aktiv dataplan eller kontakta operatören.

    5. Some network carriers may require a 3G protocol for network connection. Please go to **SIM Card Settings** -> **Protocol**, select **3G**, then click **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Enheten återansluter automatiskt. Vänta några minuter och kontrollera anslutningen.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Vid lyckad anslutning visas sidan enligt följande.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Vissa SIM-kort har särskilda begränsningar, till exempel ett visst APN. Kontakta operatören om kortet inte registreras.

        Öppna vid behov **SIM Card Settings** -> **APN**, konfigurera rätt APN och klicka på **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Klicka på **View More Information** för att kontrollera signalstyrkan. Kontrollera antennen och flytta routern till en öppen plats vid svag signal.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. Kontrollera om **Band Masking** eller **Lock Tower** är aktiverat. Inaktivera och återanslut.

    Om problemet kvarstår hämtar du loggarna och skickar dem till [support@gl-inet.com](mailto:support@gl-inet.com).

## IoT Certification {#iot-certification}

### AT&T Certification {#att-certification}

Öppna [AT&T-enhetscertifiering](https://iotdevices.att.com/certified-devices.aspx#) och ange enhetsnamnet.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile Certification {#t-mobile-certification}

Öppna [T-Mobile-enhetscertifiering](https://www.t-mobile.com/business/solutions/iot/device-certification){target="_blank"} och välj 5G under **Filter**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Related Articles

- [Internet page](internet.md)
- [Ange prioriteten för varje internetanslutningsmetod](multi-wan.md)
- [Ange lastbalansering när flera internetanslutningsmetoder används samtidigt](multi-wan.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
