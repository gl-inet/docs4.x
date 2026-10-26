# Anslut till internet via mobilnät (v4.10) {#connect-to-the-internet-via-cellular-v410}

Innehållet bygger på firmware v4.10 och senare. Om enheten kör en annan version använder du väljaren nedan för att byta guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10 and above" markdown="1">

- [Firmware v4.8 - v4.9](internet_cellular.md)
- [Firmware v4.7 and earlier](internet_cellular_v4.7.md)

</div>

---

De flesta GL.iNet-routrar stöder mobilnätsanslutning. Guiden beskriver två routertyper:

1. **Cellular routers**

    GL.iNet-mobilnätsroutrar som Spitz AX (GL-X3000) och Mudi 7 (GL-E5800) har en inbyggd 4G/5G-modul och en eller två SIM-kortplatser. Inställningarna kan skilja sig efter modell och firmware. Se [Mobilnätsroutrar](#cellular-routers).

2. **Non-cellular routers**

    Övriga routrar är hem-, rese- och miniroutrar samt säkerhetsgatewayer. De har vanligtvis en USB-port för en USB-dongel (medföljer inte) med mobilnätsanslutning. Se [Routrar utan inbyggt mobilmodem](#non-cellular-routers).

**Obs!** Vissa SIM-kort måste aktiveras före första användningen. Aktivera kortet i en smartphone innan det sätts i routern.

## Cellular Routers {#cellular-routers}

Avsnittet använder **Mudi 7 (GL-E5800)** som exempel för mobilnätskonfiguration och relaterade funktioner.

Mudi 7 har inbyggt eSIM, dubbla Nano‑SIM-kortplatser och Dual SIM Dual Standby. Webbadministrationspanelen kan därför skilja sig från andra mobilnätsroutrar, särskilt modeller med en kortplats.

### Network Setup {#network-setup}

Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

1. När inget SIM-kort är isatt visas "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Sätt in ett SIM-kort. Routern börjar ansluta automatiskt. Efter anslutning visas operatör, signalstyrka, band, dataanvändning och fler alternativ.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Om SIM-kortet inte identifieras sätter du in det igen eller startar om routern.

3. Klicka på **Details & Configuration** för nätverksinformation.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Under **Network Information** visas SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address och IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "What is Max Bit Rate (AMBR)?"

        Max Bit Rate (AMBR): Aggregate Maximum Bit Rate. Anger den sammanlagda övre bithastighetsgränsen för alla icke-GBR-bärare och tillhandahålls av mobiloperatören.

4. Klicka på **Details & Configuration** för manuell nätverkskonfiguration.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Under **Network Settings** kan du konfigurera nätverksparametrar som APN.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: APN-inställningar hämtas vanligtvis automatiskt från SIM-kortet. Fråga operatören om rätt APN om kortet kräver ett särskilt värde.

    - **IP Type**: Identifieras automatiskt men kan anges till IPv4, IPv6 eller båda. Valet måste matcha SIM-kortets stöd. Annars, eller om IPv6 väljs men är inaktiverat på routern, kan anslutningsproblem uppstå.

    - **International Data Roaming**: Aktiverat som standard för dataanvändning utomlands. Inaktivera om funktionen inte behövs eller för att undvika höga roamingavgifter.

    - **TTL**: Vissa operatörer avgör via TTL om SIM-kortet används i en router. Om kortet inte fungerar kan du prova ett annat värde än 64 och 128, till exempel 65.

    - **HL**: I IPv6 begränsar HL (Hop Limit) antalet överföringshopp och motsvarar TTL i IPv4.

    - **MTU**: Ange MTU efter användningsscenario. Fel värde kan bryta internetanslutningen. Starta om enheten efter en ändring.

    - **Authentication**: NONE används vanligtvis utan inloggningsuppgifter. Du kan välja PAP, CHAP eller PAP/CHAP.

### Traffic Statistics {#traffic-statistics}

Klicka på **Data Usage** för trafikstatistik.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Aktivera **SIM Limit Settings** för Data Cap Amount eller ett schema som återställer SIM-data regelbundet.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Ange Data Cap Amount, Data Reset Period, Start Day och Start Hour och klicka på **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Note**:

1. Om Data Used överstiger Data Cap Amount ändrar du Data Cap Amount eller Data Used. Annars kan nätverket kopplas från eller routern växla SIM-kort om [SIM Failover](#sim-failover) är aktiverat.

2. Om SIM 1 Data Cap Amount är angivet och SIM Auto Switch aktiverat växlar SIM 1 till SIM 2 när gränsen överskrids och SIM 1 inaktiveras.

3. Start Day: Högsta antal dagar motsvarar antalet dagar i aktuell månad.

### Cellular Details {#cellular-details}

Klicka på **Details & Configuration** för mobilnätsinformation.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Under **Cellular Information** visas Network Type, TAC, Cell ID, Band och Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: Identifieras automatiskt. Välj vid behov nätverkstyp i listrutan på fliken **Cellular Settings**.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Select 5G for faster speed (5G signal required) or 4G for stability.

    När en mast låses blir nätverkstypen fast och kan inte ändras.

- **TAC**: Tracking Area Code, en nätverkstilldelad identifierare för ett spårningsområde inom mobilnätet. Identifieras automatiskt från basstationen.

- **Cell ID**: Unik identifierare för en cell i mobilbasstationen. Identifieras automatiskt från basstationen.

- **Band Information**: Klicka för fler parametrar om mobilbandet.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: Klicka för historisk signalstyrka och övervakning av anslutningskvaliteten.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Band Masking {#band-masking}

Band Masking allows you to use specific cellular bands to improve cellular signal.

To enable Band Masking, click **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Aktivera **Band Masking** under **Cellular Settings**, välj band och klicka på **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Lock Operator {#lock-operator}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) stöder funktionen i firmware v4.8 eller senare.

Genom att låsa en mobiloperatör använder routern endast dennes nätverk. Det ger stabil anslutning och undviker oavsiktliga roamingavgifter, särskilt nära landsgränser.

To lock operator, click **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In the **Cellular Settings**, click **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Välj vid behov **Lock Mode** före nätverkssökningen.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: Lock to a specific operator manually.

- **Manual-Auto**: Switch to an available operator network automatically when manual locking fails.

Then click **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Vänta en minut, välj en tillgänglig operatör och klicka på **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Mobilsignalen låses till vald operatör.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Lock Tower {#lock-tower}

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) stöder funktionen i firmware v4.7 eller senare.

Lås en mast för hög signal och stabil anslutning. Masten måste matcha frekvensbanden som operatören och enheten stöder, annars kan anslutningen misslyckas.

To lock a tower, click **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In the **Cellular Settings**, click **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

Klicka på **Scan Networks** i popup-fönstret.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Vänta en minut tills tillgängliga master visas.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Välj en mast för information och klicka på **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Mobilsignalen låses till vald mast.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Note**:

1. Enheten kanske inte kan söka efter alla master när Cellular-gränssnittet är aktiverat.

2. Om den låsta masten inte matchar bandmaskering eller APN-parametrar kan routern inte ansluta till mobilnätet.

3. Om routern flyttas försöker den fortfarande ansluta till den låsta masten efter omstart. Det kan hindra automatisk anslutning på den nya platsen. Lås upp masten eller lås manuellt en ny.

### SMS {#sms}

Please refer to [SMS](../tutorials/sms.md).

### SMS Forwarding {#sms-forwarding}

Please refer to [SMS Forwarding](../tutorials/sms_forwarding.md).

### Airplane Mode {#airplane-mode}

Aktivera Airplane Mode genom att klicka på kugghjulet uppe till höger och aktivera **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Modem Information {#modem-information}

Visa modeminformation genom att klicka på kugghjulet uppe till höger och välja **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### SIM Failover {#sim-failover}

Funktionen är endast tillgänglig på mobilnätsroutrar med Dual-SIM.

SIM Failover låter routern växla automatiskt mellan SIM 1 och SIM 2. När prioriterat SIM överskrider Data Cap Amount eller saknar internet växlar routern till reservkortet.

Aktivera SIM Failover genom att klicka på kugghjulet uppe till höger och välja **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

Aktivera **Auto Switch** i popup-fönstret. Dra knappen till höger för att ändra SIM-prioritet.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Aktivera **Scheduled Switch to Preferred SIM**, ange **Daily Execution Time** och klicka på **Apply** om routern ska växla tillbaka vid en viss tid.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### AT Command {#at-command}

AT-kommandon är standardinstruktioner för kommunikation med mobilmodemet. Du kan skicka kommandon och kontrollera modemstatus.

Klicka på kugghjulet uppe till höger och välj **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: När Shortcut är **Manual command** anger du kommandot i **AT Command** och klickar på **Send**. Resultatet visas nedan.

    Du kan även välja ett **förinställt kommando** i listrutan.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Om du till exempel väljer "Request SIM card status" och SIM1 klickar du på "Send" för att visa resultatet.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: Välj SIM1 eller SIM2. Alternativen beror på antalet kortplatser.

- **AT Command**: Ange kommandot här när Shortcut är "Manual command".

## Non-cellular Routers {#non-cellular-routers}

Routrar utan inbyggt mobilmodem kan anslutas till mobilnät med en extern USB-dongel (medföljer inte).

Different USB dongles/modems may work in different modes: Standard USB modem mode or Host-less mode.

- **Standard USB modem mode**: Routern fungerar som USB-värd och dongeln som USB-slavmodem. Dongeln exponerar kommandogränssnitt (AT/QMI/MBIM) och en virtuell USB Ethernet-port och hanteras via routerns Cellular WAN. Routern kan läsa ICCID, signalstyrka och band, och SIM-inställningar konfigureras i webbgränssnittet.

- **Host-less mode**: Dongeln utför mobilanslutningen internt och exponerar ett virtuellt USB Ethernet-gränssnitt. Routern identifierar den som Tethering WAN, så anslutningen upprättas via Tethering i stället för Cellular. Mobilmätvärden visas inte på routern, och APN- och SIM-inställningar görs i dongelns webbgränssnitt.

Se avsnittet som motsvarar USB-dongelns driftläge.

### Standard USB modem {#standard-usb-modem}

Avsnittet använder **Mango 2 (GL-MG1300)** och 5G-utvecklingskortet [GL-M2](https://www.gl-inet.com/products/gl-m2){target="_blank"} (5G NR-modul: RM520N-GL) som exempel.

1. Sätt ett SIM-kort i GL-M2 och anslut kortet till routerns USB-port.

2. Logga in på routerns webbadministrationspanel och öppna **INTERNET** -> **Cellular**.

    Routern försöker ansluta automatiskt. När anslutningen är klar visas nätverksinformationen med en grön punkt.

    ![m2 sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_active.png){class="glboxshadow"}

3. SIM Card Settings.

    Klicka på **SIM Card Settings** för SIM-konfigurationen.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings1.png){class="glboxshadow"}

    Automatiskt identifierade inställningar som APN, IP-typ och nätverkstyp visas. Ändringar medför ny uppringning.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings2.png){class="glboxshadow"}

4. SIM Information.

    Klicka på **SIM Information** för SIM-information.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info1.png){class="glboxshadow"}

    Nätverksinformation som ICCID, IP-adress, DNS, mobilband och signalstyrka visas.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info2.png){class="glboxshadow gl-80-desktop"}

5. SMS & SMS Forwarding.

    Information om SMS och vidarebefordran finns i [SMS](../tutorials/sms.md) och [SMS Forwarding](../tutorials/sms_forwarding.md).

6. Manage Cellular Profiles.

    Hantera SIM-profiler genom att klicka på kugghjulet uppe till höger och välja **Manage Cellular Profiles**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    Aktuell profil visas.

    ![m2 manage profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_manage_profiles.png){class="glboxshadow"}

    Klicka på **Add a New Profile** för fler profiler.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile1.png){class="glboxshadow"}

    Ange parametrarna och klicka på **Apply**.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile2.png){class="glboxshadow"}

7. Modem AT Command.

    AT-kommandon är standardinstruktioner för kommunikation med mobilmodemet. Du kan skicka kommandon och kontrollera modemstatus.

    Kör AT-kommandon genom att klicka på kugghjulet uppe till höger och välja **Modem AT Command**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    ![m2 atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_atcommand.png){class="glboxshadow"}

    - **Shortcut**: När Shortcut är **Manual command** anger du kommandot i **AT Command** och klickar på **Send**. Resultatet visas nedan.

        Du kan även välja ett **förinställt kommando** i listrutan.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

        Om du till exempel väljer "Request SIM card status" och SIM1 klickar du på "Send" för att visa resultatet.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

    - **SIM Slot**: Välj SIM1 eller SIM2. Alternativen beror på USB-modemets kortplatser.

    - **AT Command**: Ange kommandot här när Shortcut är "Manual command".

### Host‑less dongle {#hostless-dongle}

Avsnittet använder **Flint 3 (GL-BE9300)** och USB-dongeln [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} som exempel.

1. Anslut USB-dongeln till routerns USB-port.

2. Log in to your router's web Admin Panel, navigate to **INTERNET** -> **Tethering**, then click **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Klicka vid behov på **Advanced** för TTL, HL och MTU innan du klickar på **Connect**.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. När anslutningen är klar visas nätverksinformationen med en grön punkt.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

4. Information om APN- och SIM-inställningar för SIMPoYo uFi finns i [Hantera SIMPoYo uFi](../user_guide/simpoyo-4g-ufi/index.md#manage-simpoyo-ufi).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
