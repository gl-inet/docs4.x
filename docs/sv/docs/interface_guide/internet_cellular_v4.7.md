# Anslut till internet via mobilnät (v4.7 och tidigare) {#connect-to-the-internet-via-cellular-v47-and-earlier}

Innehållet bygger på firmware v4.7 och tidigare. Om enheten kör en annan version använder du väljaren nedan för att byta guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.7 and earlier" markdown="1">

- [Firmware v4.10 and above](internet_cellular_v4.10.md)
- [Firmware v4.8 - v4.9](internet_cellular.md)

</div>

---

De flesta GL.iNet-routrar stöder mobilnätsanslutning. Guiden omfattar tre modelltyper:

1. **Built-in 4G Single-SIM models**

    Vissa modeller, till exempel GL-XE300 (Puli), har en inbyggd 4G-modul och en SIM-kortplats. Se [Konfiguration för modeller med ett SIM-kort](#setup-for-single-sim-models).

2. **USB Modem compatible models**

    Vissa modeller, till exempel GL-AXT1800 (Slate AX), har USB-port och stöder mobilnät via USB-modem. Stegen liknar modeller med inbyggd 4G och ett SIM-kort. Se [Konfiguration för modeller med ett SIM-kort](#setup-for-single-sim-models).

3. **Built-in 5G Dual-SIM models**

    Vissa modeller, till exempel GL-X3000 (Spitz AX), har en inbyggd 5G-modul och dubbla SIM-kortplatser. Mobilnätsinställningarna kan skilja sig något. Se [Konfiguration för modeller med dubbla SIM-kort](#setup-for-dual-sim-models).

**Note:** Some SIM cards require activation before first use. To ensure compatibility, activate the SIM card in a smartphone before inserting it into the router.

## Setup for Single-SIM models {#setup-for-single-sim-models}

Följande steg gäller modeller med inbyggt mobilmodem och en SIM-kortplats, till exempel GL-XE300 Puli, eller USB-port för externt modem, till exempel GL-AXT1800 Slate AX.

**GL-AXT1800 (Slate AX)** med externt USB-modem används som exempel.

Stäng först av routern. Sätt ett föraktiverat SIM-kort i USB-modemet, anslut modemet till routerns USB-port och slå på routern.

Om USB-modemet ansluts efter start kanske webbadministrationspanelen inte uppdateras automatiskt. Uppdatera sidan eller starta om routern.

### Auto Setup {#auto-setup}

Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

1. Vid första åtkomst kanske anslutningen inte upprättas automatiskt, men operatörens namn och IMEI ska visas uppe till vänster. Klicka på **Auto Setup**.

    Ignorera varningen *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. It will start connecting.

    **Obs!** Vissa SIM-kort har särskilda begränsningar, till exempel ett visst APN. Kontakta operatören om kortet inte registreras.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. När anslutningen är klar visas nätverksinformationen med en grön punkt.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Obs!** Efter första konfigurationen identifieras USB-modemet automatiskt efter omstart eller återanslutning och nätverket ansluts utan att Auto Setup behöver klickas igen.

Om Auto Setup misslyckas provar du [Manual Setup](#manual-setup).

### Manual Setup {#manual-setup}

Klicka på **Manual Setup** i avsnittet Cellular för att visa eller ändra aktuella SIM-kortsinställningar.

**Obs!** Vissa SIM-kort kräver ett visst APN. Kontakta operatören om kortet inte registreras och kontrollera begränsningar. Konfigurera rätt APN vid behov.

Applying the changes will trigger a reconnection.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: Mobilkommunikationsprotokollet, till exempel 3G, QMI eller QCM. Det identifieras vanligtvis automatiskt men kan ändras efter modemets och operatörens krav.

- **Port**: Serieporten för kommunikation med mobilmodemet. Den identifieras vanligtvis automatiskt.

- **APN**: APN (Access Point Name) är en gatewayparameter som krävs för mobilnätsanslutning. Använd standard-APN eller ett eget APN från operatören.

- **PIN**: Ange SIM-kortets PIN-kod om en sådan används. Fältet är valfritt utan PIN.

- **TTL**: TTL (Time To Live) anger maximal tid för paket i nätverket. Routern minskar som standard TTL för inkommande klientpaket med 1 före vidarebefordran. Gäller endast IPv4.

    **Obs!** Ange ett fast värde för att åsidosätta eller förfalska TTL. På de flesta modeller anger du önskad effektiv TTL plus 1. Mudi 7 (GL‑E5800) använder värdet utan ändring.

- **Service**: Select the cellular service type to define the network technologies the modem will use.

- **Dial Number**: Ange operatörens uppringningsnummer. Det är ofta förkonfigurerat och kan lämnas tomt på moderna nätverk.

- **Authentication**: Välj operatörens autentiseringsmetod, till exempel NONE, PAP eller CHAP. NONE används vanligtvis utan inloggningsuppgifter.

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

- **QMI**: Modemet stöder QMI. Välj QMI som protokoll och **/dev/cdc-wdm0** som serieport.

- **Host-less**: Modemet stöder Tethering. Hantera anslutningen via Tethering-gränssnittet i stället för Cellular.

## Setup for Dual-SIM models {#setup-for-dual-sim-models}

Följande steg gäller modeller med inbyggt mobilmodem och dubbla SIM-kort. Webbadministrationspanelen kan skilja sig något.

**GL-X3000 (Spitz AX)** används som exempel. Dual SIM, Single Standby innebär att två SIM-kort kan vara isatta men endast ett är aktivt åt gången. Du kan växla manuellt.

Stäng först av routern, sätt in föraktiverade SIM-kort och slå sedan på routern. Om kort sätts in efter start kanske webbadministrationspanelen inte uppdateras automatiskt. Uppdatera sidan eller starta om routern.

### Auto Setup {#auto-setup_1}

Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

1. När inget SIM-kort är isatt visas följande sida.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. När ett SIM-kort sätts in börjar routern ansluta automatiskt.

    Vid lyckad anslutning visas följande sida.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Om automatisk anslutning misslyckas klickar du på **Auto Setup** och väntar eller provar **Manual Setup**.

### Manual Setup {#manual-setup_1}

Klicka på **Manual Setup** i avsnittet Cellular för att öppna Cellular Settings.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Du kan visa eller ändra aktuella SIM-kortsinställningar. Förkonfigurerade profiler lagras, och konfigurationer kan läggas till manuellt i "Saved Settings".

### SIM Card Slot Settings {#sim-card-slot-settings}

Klicka på **Current SIM Card** i avsnittet Cellular.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Sidan **SIM Card Slot Settings** öppnas.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Om två SIM-kort är isatta kan du aktivera **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

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

## Traffic Statistics {#traffic-statistics}

Klicka på **Traffic Statistics** i avsnittet Cellular.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Sidan Traffic Statistics öppnas.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS {#sms}

Please refer to [SMS](../tutorials/sms.md).

## SMS Forwarding {#sms-forwarding}

Please refer to [SMS Forwarding](../tutorials/sms_forwarding.md).

## Modem Management {#modem-management}

Klicka på **Tool** uppe till höger i avsnittet Cellular för att öppna Modem Management.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

It includes two sections: **Modem Info** and **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

AT-kommandon är standardinstruktioner för kommunikation med mobilmodemet.

När Shortcut är **Manual command** skriver du önskat kommando i fältet AT Command för att kontrollera modemstatus.

Du kan även välja bland **förinställda kommandon** i listrutan Shortcut.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Följande kommandon är förinställda:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

I exemplet väljs "Request IMEI". Klicka på "Send" för att visa resultatet.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Carrier profile {#carrier-profile}

Du kan spara olika profiler för samma eller olika operatörer.

Klicka på **Profile** uppe till höger i avsnittet Cellular för att hantera profiler.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Add a new profile or save the current profile.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Create your own profile based on your carrier's requirements.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Du kan välja en sparad profil nästa gång.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Välj profilerna som behövs.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Lock Tower {#lock-tower}

Funktionen är endast tillgänglig på utvalda modeller, till exempel GL-X3000, GL-XE3000 och GL-X2000 med firmware v4.7 eller senare.

Lås en mobilmast för att försöka få en stark och stabil signal.

**Obs!** Den låsta masten måste matcha frekvensbanden som operatören och enheten stöder, annars kan anslutningen misslyckas.

Klicka på ikonen **Tower** uppe till höger i avsnittet Cellular.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

It will display the available towers.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Klicka på en mast för att visa information och låsa den.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

The tower status (e.g., Locked/Unlocked) will be displayed at the top.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Note**:

1. Enheten kanske inte kan söka efter alla master när Cellular-gränssnittet är aktiverat.

2. Om den låsta masten inte matchar bandmaskering eller APN-parametrar kan routern inte ansluta till mobilnätet.

3. Om routern flyttas försöker den fortfarande ansluta till den låsta masten efter omstart. Det kan hindra automatisk anslutning på den nya platsen. Lås upp masten eller lås manuellt en ny.

## Historical Signal Record {#historical-signal-record}

Klicka på ikonen **Signal** uppe till höger i avsnittet Cellular för historisk signalstyrka.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Det hjälper dig att bedöma mobilanslutningens kvalitet. Vid svag signal provar du en annan mast.

Visa signalhistoriken genom att välja olika tidsintervall.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking {#band-masking}

Klicka på **View More** i avsnittet Cellular och välj **Cells Info** för cellinformation.

Aktuella band och deras signalstatus visas.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Vid svag signal kan Band Masking blockera vissa band. Vid god signal kan routern begränsas till vissa mobilband.

Klicka på **Manual Setup** för att öppna Cellular Settings och aktivera **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Välj **Masking Mode** (Block eller Open) och välj sedan LTE Bands, 5G NSA Bands och 5G SA Bands.

## Troubleshooting {#troubleshooting}

Om mobilanslutningen misslyckas klickar du på felmeddelandet nedan för lösningar.

??? note "No SIM / Your SIM card has not been detected"

    1. Uppdatera sidan, vänta några minuter och kontrollera om SIM-kortet identifieras.

    2. Kontrollera att SIM-kortet är rätt installerat. Rikta kortets skåra mot markeringen på kortplatsen.

    3. Stäng av routern, ta ut och sätt tillbaka SIM-kortet och slå på routern.

    4. Try using another SIM card if available.

    Om problemet kvarstår hämtar du loggarna och skickar dem till [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Uppdatera sidan och vänta några minuter för att se om felet försvinner.

    2. Klicka på **Disconnect**/**Abort** och sedan på **Connect** för att återansluta.

    3. Restart the router.

    4. Kontrollera SIM-kortets status och att det är aktiverat. Prova kortet i en smartphone med aktiv dataplan eller kontakta operatören.

    5. Some network carriers may require a 3G protocol for network connection. Please go to **Manual Setup** -> **Cellular Settings** -> **Protocol**, select **3G**, then click **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Enheten återansluter automatiskt. Vänta några minuter och kontrollera anslutningen.

    6. Vissa SIM-kort har särskilda begränsningar, till exempel ett visst APN. Kontakta operatören om kortet inte registreras.

        Öppna vid behov **Manual Setup** -> **Cellular Settings** -> **APN**, konfigurera rätt APN och klicka på **Apply**.

    7. Klicka på **View More**, välj **Cells Info** och kontrollera signalstyrkan. Kontrollera antennen och flytta routern till en öppen plats vid svag signal.

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
