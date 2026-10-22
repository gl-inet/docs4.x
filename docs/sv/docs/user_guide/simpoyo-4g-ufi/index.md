# Användarhandbok för SIMPoYo 4G uFi {#simpoyo-4g-ufi-user-guide}

SIMPoYo 4G uFi är vår kompakta serie Plug & Play-USB-donglar med Wi-Fi-hotspot, utformad för snabb och tillförlitlig anslutning överallt. Den fungerar smidigt med de flesta GL.iNet-routrar samt bärbara datorer, powerbanker, USB-portar i bilar och andra USB-strömkällor. Den levereras med 10GB kostnadsfri data i 30 dagar, giltig i Storbritannien och 34 andra europeiska länder.
<br><small>*Available Only: [EU](https://store-eu.gl-inet.com/) & [UK Stores](https://store-uk.gl-inet.com/)</small>

Den här guiden visar hur du använder USB-dongeln SIMPoYo uFi (SP-N150C4), däribland LED-indikering, aktivering av det inbyggda SIM-kortet, användning av dongeln med olika enheter, datapåfyllning och hantering av uFi-inställningar.

![SIMPoYo uFi](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/sp-n150c4.jpg){class="glboxshadow"}

## LED-indikering {#led-indication}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LED Indication</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            vertical-align: middle;
        }
        th {
            background-color: #f2f2f2;
            text-align: left;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>LED Type</th>
                <th>Color</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3">4G LED</td>
                <td>Green</td>
                <td>LTE Connected</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>WCDMA Connected</td>
            </tr>
            <tr>
                <td>Red Blinking</td>
                <td>No Signal / No SIM Card / Out of Service</td>
            </tr>
            <tr>
                <td rowspan="3">Wi-Fi LED</td>
                <td>Green</td>
                <td>Device(s) connected to Wi-Fi</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>No device connected to Wi-Fi</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>Wi-Fi is Disabled</td>
            </tr>
            <tr>
                <td rowspan="2">4G LED + Wi-Fi LED</td>
                <td>White</td>
                <td>Device Powered On</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>Device Powered Off</td>
            </tr>
        </tbody>
    </table>
</body>
</html>

## Aktivera SIM-kort {#activate-sim-card}

SIMPoYo uFi levereras med ett förinstallerat SIM-kort som måste aktiveras före användning.

Titta på videon eller följ stegen nedan för att aktivera SIM-kortet i SIMPoYo uFi.

<iframe width="560" height="315" src="https://www.youtube.com/embed/0UokDjzp7Ek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Steg 1**. Leta reda på ICCID-numret på informationsetiketten på baksidan av SIMPoYo uFi.

**Steg 2**. Skanna QR-koden eller besök [https://w.simpoyo.com/activate/](https://w.simpoyo.com/activate/){target="_blank"} och ange ICCID-numret för att registrera dig.

**Steg 3**. Använd 10GB kostnadsfri data. Som ny användare får du omedelbart 10GB kostnadsfri 4G-data som är giltig i 30 dagar i Storbritannien och 34 andra europeiska länder.

## Internetkonfiguration {#internet-setup}

### Anslut till en GL.iNet-router {#connect-to-a-glinet-router}

SIMPoYo uFi fungerar smidigt med de flesta rese- och hemroutrar från GL.iNet. Anslut den till routern för omedelbar 4G LTE-åtkomst när och var du vill.

Titta på videon eller följ stegen nedan för att ansluta SIMPoYo uFi till en GL.iNet-router.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sU2u4En04so" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Steg 1**. Anslut SIMPoYo uFi till USB-porten på GL.iNet-routern.

![setup1](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/setup1.png){class="glboxshadow"}

**Steg 2**. Anslut en enhet till routern, öppna en webbläsare och besök `192.168.8.1` för att logga in på routerns webbadministrationspanel. Om du har ändrat routerns IP-adress loggar du in med den nya adressen.

![setup2](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/setup2.png){class="glboxshadow"}

**Steg 3**. Öppna **INTERNET** -> **Tethering** i administratörspanelen och klicka på **Connect**.

![setup3](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/setup3.png){class="glboxshadow"}

**Steg 4**. När anslutningen har upprättats visas nätverksinformationen med en blå punkt i det övre vänstra hörnet.

![setup4](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/setup4.png){class="glboxshadow"}

Nu kan du ansluta enheter till routern via kabel eller Wi-Fi eller ansluta direkt till Wi-Fi-nätverket från SIMPoYo uFi för att få internetåtkomst.

- Anslut till routern via kabel: Anslut en Ethernet-kabel till routerns LAN-port och enheten. Detta passar enheter som endast har kabelanslutning eller när du behöver en stabil anslutning utan störningar.

- Anslut till routern via Wi-Fi: Leta reda på Wi-Fi SSID och Key på etiketten på routerns undersida och anslut sedan enheten. Detta passar flera enheter (2.4 GHz och 5 GHz), behov av större täckning eller personliga nätverksinställningar på routern.

- Anslut till SIMPoYo uFi via Wi-Fi: Leta reda på Wi-Fi SSID och Key på enhetsetiketten på SIMPoYo uFi och anslut sedan dina enheter (upp till 8). Den fungerar som en fristående 2.4 GHz-hotspot för extra flexibilitet när det behövs.

!!! note "Felsökning"

    Om en GL.iNet-router inte identifierar uFi-enheten provar du stegen nedan:

    1. Använd routerns ursprungliga nätadapter. **Otillräcklig spänning eller ström kan göra att USB-porten inte fungerar korrekt och att uFi-enheten inte identifieras.**

    2. Prova en annan nätadapter med samma specifikationer som originalet.

### Anslut till en dator {#connect-to-a-computer}

**Steg 1**. Anslut SIMPoYo uFi till datorns USB-port (t.ex. en stationär eller bärbar dator). Den identifieras automatiskt som en USB Ethernet-enhet och ansluter genast datorn till internet.

**Steg 2**. Andra enheter (t.ex. smartphones och surfplattor) kan samtidigt ansluta till Wi-Fi-nätverket på 2.4 GHz från SIMPoYo uFi för internetåtkomst.

![multi-device](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/multi-device.jpg){class="glboxshadow"}

### Anslut till en USB-strömkälla {#connect-to-a-usb-power-source}

**Steg 1**. Anslut SIMPoYo uFi till valfri USB-strömkälla, till exempel en väggladdare, powerbank eller billaddare.

**Steg 2**. När SIMPoYo uFi har slagits på sänder den ut ett Wi-Fi-nätverk med SSID **SIMPoYo-XXX**.

**Steg 3**. Leta reda på Wi-Fi-lösenordet (Key) på enhetsetiketten. Använd lösenordet för att ansluta en smartphone, surfplatta, bärbar dator eller andra enheter till Wi-Fi-nätverket från SIMPoYo uFi för internetåtkomst.

## Fyll på SIMPoYo-abonnemang {#top-up-simpoyo-plans}

När data tar slut eller går ut skannar du QR-koden på SIMPoYo uFi eller besöker [https://w.simpoyo.com](https://w.simpoyo.com){target="_blank"} för att fylla på dataplanen.

!!! note "Länder och regioner som stöds"

    - **Storbritannien**

    - **Europa**

        Andorra, Österrike, Belgien, Bulgarien, Kroatien, Cypern, Tjeckien, Danmark, Estland, Finland, Frankrike, Tyskland, Gibraltar (Storbritannien), Grekland, Ungern, Island, Irland, Italien, Lettland, Liechtenstein, Litauen, Luxemburg, Malta, Nederländerna, Norge, Polen, Portugal, Réunion (Frankrike), Rumänien, Slovakien, Slovenien, Spanien, Sverige, Schweiz.

    - **Mellanöstern och Nordafrika**

        Egypten, Iran, Israel, Kuwait, Qatar, Saudiarabien, Förenade Arabemiraten.

    - **Asien**

        Indonesien, Japan, Pakistan, Filippinerna, Singapore, Sydkorea, Turkiet, Vietnam, Fastlandskina, Hongkong (Kina), Taiwan (Kina).

## Hantera SIMPoYo uFi {#manage-simpoyo-ufi}

Du kan logga in på administratörspanelen för SIMPoYo uFi och hantera nätverksinställningarna.

### Logga in på administratörspanelen {#log-in-admin-panel}

1. Anslut en enhet till Wi-Fi-nätverket från SIMPoYo uFi.

2. Öppna en webbläsare och ange `192.168.1.1` för att öppna administratörspanelen för SIMPoYo uFi.

3. Logga in med Admin Password (som standard är det samma som Wi-Fi-lösenordet för SIMPoYo uFi).

    ![log in](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/0-simpoyo-login.png){class="glboxshadow"}

**Tips!** Om du har glömt administratörslösenordet för SIMPoYo uFi följer du stegen nedan för att återställa det:

1. Anslut SIMPoYo uFi till USB-porten på en stationär eller bärbar dator eller någon annan USB-strömkälla. Den slås på automatiskt.
2. För in ett stift i Reset-hålet i cirka 2 sekunder och släpp det sedan.
3. Vänta i 8-10 sekunder. LED-indikatorn släcks först och därefter tänds två vita lampor, vilket visar att återställningen har slutförts.

### Kontrollera nätverksinformation {#check-network-details}

1. Välj **Status** på den övre menyn och öppna **Device & Network**. Startsidan med enhetens nätverksstatus visas.

    ![network status](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/1.1-device-network.png){class="glboxshadow"}

2. Välj **Cellular Network** på sidofältet till vänster. Där kan du kontrollera information om mobilnätet, till exempel signalstyrkan.

    ![cellular network](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/1.2-cellular-network.png){class="glboxshadow"}

### Kontrollera dataanvändning {#check-data-usage}

1. Välj **Data Usage** på den övre menyn för att visa nedladdning, uppladdning, total dataförbrukning och varaktighet.

    ![data usage](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/2-data-usage.png){class="glboxshadow"}

    Obs! Uppgifterna är endast avsedda som referens. Se fakturan för exakta uppgifter.

2. Om du vill återställa dataanvändningen klickar du på knappen **Clear History**.

### Ändra Wi-Fi-inställningar {#change-wi-fi-settings}

1. Välj **Settings** på den övre menyn och öppna **Wi-Fi Settings**.

    ![wifi settings](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.1-wifi-settings.png){class="glboxshadow"}

2. Anpassa Wi-Fi-nätverksnamnet och lösenordet för SIMPoYo uFi och klicka sedan på **Apply**.

### Ange APN {#set-apn}

Om SIM-kortet kräver manuell APN-konfiguration följer du stegen nedan.

1. Välj **Settings** på den övre menyn och öppna **Cellular Settings**.

    ![cellular settings](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.2-cellular-settings.png){class="glboxshadow"}

2. Ändra **APN Mode** till **Manual**.

3. Fyll i informationen från mobiloperatören och klicka sedan på **Apply**.

### Aktivera roaming {#enable-roaming}

Med roaming kan SIM-kortet användas med lokala operatörer i andra regioner eller länder, så att du förblir ansluten utanför hemnätverket.

Följ stegen nedan för att aktivera roaming.

1. Välj **Settings** på den övre menyn och öppna **Roaming**.

    ![roaming](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.3-roaming.png){class="glboxshadow"}

2. Välj **Enable** och klicka på **Apply**.

### Aktivera PIN-kod {#enable-pin-code}

En PIN-kod är ett kort säkerhetslösenord för SIM-kortet (vanligtvis 4-8 siffror) som låser kortet och förhindrar obehörig användning. Om SIM-kortet stjäls eller sätts in i en annan enhet kan det inte aktiveras eller användas utan PIN-koden.

Följ stegen nedan för att aktivera PIN-koden.

1. Välj **Settings** på den övre menyn och öppna **PIN Settings**.

    ![pin settings](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.4-pin-settings.png){class="glboxshadow"}

2. Välj **Enable**, ange PIN-koden och klicka på **Apply**.

### Ändra administratörslösenord {#change-admin-password}

Administratörens standardlösenord är samma som Wi-Fi-lösenordet. Av säkerhetsskäl bör du ändra det under den första konfigurationen.

1. Välj **Settings** på den övre menyn och öppna **Admin Settings**.

    ![admin settings](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.5-admin-settings.png){class="glboxshadow"}

2. Anpassa Admin Password och Login Timeout och klicka sedan på **Apply**.

3. Om du vill återställa SIMPoYo uFi till standardinställningarna klickar du på knappen **Factory Default Setting**.

### Återställ administratörslösenordet {#reset-admin-password}

Om du har glömt administratörslösenordet för SIMPoYo uFi följer du stegen nedan för att återställa det:

1. Anslut SIMPoYo uFi till USB-porten på en stationär eller bärbar dator eller någon annan USB-strömkälla. Den slås på automatiskt.
2. För in ett stift i Reset-hålet i cirka 2 sekunder och släpp det sedan.
3. Vänta i 8-10 sekunder. LED-indikatorn släcks först och därefter tänds två vita lampor, vilket visar att återställningen har slutförts.

### DHCP-inställningar {#dhcp-settings}

Som standard är IP-adressen för SIMPoYo uFi `192.168.1.1`, och DHCP-servern är aktiverad för att tilldela IP-adresser till anslutna enheter.

Om du vill ändra IP-adressen eller anpassa DHCP-inställningarna följer du stegen nedan.

1. Välj **Settings** på den övre menyn och öppna **Advanced** -> **DHCP**.

    ![dhcp](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.6-dhcp.jpg){class="glboxshadow"}

2. Här kan du ändra enhetens IP-adress, aktivera eller inaktivera DHCP-servern samt ange IP-intervall och lånetid. Konfigurera DHCP-inställningarna och klicka på **Apply**.

### MAC-filter {#mac-filter}

Med MAC Filter kan du styra vilka enheter som får åtkomst till WLAN genom att hantera deras MAC-adresser, vilket förbättrar nätverkets säkerhet.

MAC Filter är inaktiverat som standard. Följ stegen nedan om du vill aktivera det.

1. Välj **Settings** på den övre menyn och öppna **Advanced** -> **MAC Filter**.

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.6-mac-filter-1.png){class="glboxshadow"}

    **User list** högst upp visar information om anslutna enheter. Kontrollera att enheten som du vill styra finns i listan. Om den saknas ansluter du den till Wi-Fi-nätverket från SIMPoYo uFi igen.

2. Ändra **MAC Filter Mode** till **Black List** / **White List**.

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/3.6-mac-filter-2.png){class="glboxshadow"}

3. Kopiera MAC-adressen för enheten som du vill blockera eller tillåta till listan och klicka på **Apply**.

### Upgrade {#upgrade}

1. Välj **Upgrade** på den övre menyn och öppna **Device Info**. Där visas enhetsinformationen för SIMPoYo uFi, däribland:

    - Maskinvaruinformation (t.ex. maskinvaruversion, MAC-adress, IMEI och ICCID)
    - Programvaruinformation (t.ex. programvaruversion)
    - WebUI-information (t.ex. WebUI-version)

    ![upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/4.1-upgrade.jpg){class="glboxshadow"}

2. Du kan uppgradera programvaruversionen om en uppdatering är tillgänglig.

    Välj **Online Update** på sidofältet till vänster och klicka på knappen **Check New Update** för att kontrollera om en ny version är tillgänglig.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/4.2-online-update.png){class="glboxshadow"}

    Du kan också välja **Local Update** på sidofältet till vänster, ladda upp en fil och klicka på **Apply** för att uppgradera manuellt.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/simpoyo-4g-ufi/4.3-local-update.png){class="glboxshadow"}

## Tillbehörsguide {#accessories-guide}

Följande tillbehör ingår i förpackningen:

- **1 USB-C-till-USB-A-adapterkabel**: Lämplig för att ansluta SIMPoYo uFi till enheter som endast har ett USB Type-C-gränssnitt (t.ex. bärbara datorer).

- **1 USB-A-till-USB-A-adapterkabel**: Gör det möjligt att flexibelt ansluta SIMPoYo uFi till en USB-port (t.ex. på en dator eller USB-strömkälla) utan direkt kontakt mellan den inbyggda porten på SIMPoYo uFi och målporten. Det motverkar skador på metallgränssnittet vid plötsliga stötar.

- **1 SIM-utmatningsverktyg (ett stift)**: Använd det för att mata ut SIM-kort från enheter (t.ex. smartphones) inför installation i SIMPoYo uFi eller för att trycka in återställningshålet på uFi-enheten vid behov.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
