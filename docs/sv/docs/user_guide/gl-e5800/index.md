# Användarhandbok för Mudi 7 (GL-E5800) {#mudi-7-gl-e5800-user-guide}

## Produktöversikt {#product-overview}

Mudi 7 är en bärbar 5G NR Wi-Fi 7-reserouter för mobila användare och affärsresenärer. Den ger tillförlitliga privata nätverk som skyddar data mot cyberhot. Den har 5G-hyperhastighet, automatisk växling mellan dubbla SIM-kort (failover) och Wi-Fi 7 (320MHz-kanaler och 4K QAM) för stabil och snabb anslutning, snabba nedladdningar, 4K-strömning och videokonferenser utan fördröjning även i trånga miljöer.

Med pekskärmen på Mudi 7 kan du övervaka dataanvändning i realtid, signalstyrka, anslutna enheter och klienthastighet samt ändra inställningar med enkla tryck för intuitiv och smidig styrning.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Mudi 7 (GL-E5800)
- 1 x batteripaket
- 1 x 10Gbps USB-C-kabel
- 1 x resefodral
- 1 x användarhandbok

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Titta på uppackningsvideon för Mudi 7 nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfigurera Mudi 7 {#how-to-set-up-mudi-7}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Installera SIM-kort {#1-install-sim-card}

Installera Nano-SIM-kort i Mudi 7. Om du föredrar eSIM hoppar du över detta och fortsätter till steg 2.

Använd först den lilla skåran i det nedre högra hörnet på enhetens bakstycke som hävpunkt. Bänd längs skarven så att en öppning bildas. Öppna sedan bakstycket och ta ut batteriet ur Mudi 7.

!!! Warning

    Om batteriet är svullet, läcker, är ovanligt varmt, skadat eller svårt att ta ut ska du sluta använda enheten och inte försöka ta ut batteriet. Se [Batterisäkerhet](#battery-safety).

![small notch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/notch.png){class="glboxshadow"}

![remove battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery1.png){class="glboxshadow"}

Sätt därefter in Nano-SIM-kortet eller Nano-SIM-korten. Om du bara använder ett kort bör du använda SIM 1.

![sim slots](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/sim-slots.png){class="glboxshadow"}

Sätt slutligen tillbaka batteriet och bakstycket.

![restore battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery2.png){class="glboxshadow"}

### 2. Slå på {#2-power-on}

Håll Power-knappen intryckt i **3 sekunder** eller anslut en nätadapter.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power-button.png){class="glboxshadow"}

### 3. Grundläggande inställningar {#3-basic-settings}

Följ anvisningarna på skärmen för att konfigurera grundläggande inställningar, däribland **screen passcode**, **admin password**, **Wi-Fi name**, **Wi-Fi password** och **frequency bands**.

**Tips!** Standardlösenordet för administratören är de sista 9 tecknen i enhetens S/N följt av tecknet #. Du kan använda standardlösenordet eller ange ett eget.

### 4. Konfigurera internet {#4-internet-setup}

Konfigurera Mudi 7 med någon av de internetanslutningsmetoder som stöds: Cellular, Ethernet, Repeater, Tethering eller USB Ethernet. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutning.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Mudi 7 har ett **inbyggt eSIM** och **dubbla Nano‑SIM-kortplatser**. Du kan ansluta till internet genom att köpa ett eSIM-paket utan ett fysiskt SIM-kort eller sätta in Nano-SIM-kort för åtkomst till 5G-mobilnätet.

    **Konfigurera eSIM**:

    1. Öppna **Cellular** -> **SIM Card Switch** på pekskärmen och växla reglaget för att **aktivera eSIM**.

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. Logga in på [webbadministrationspanelen](./index.md#log-in-to-web-admin-panel) och öppna **INTERNET** -> **Cellular** -> **eSIM Management**.

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. Klicka på **Add eSIM Profile** längst ned i popup-fönstret.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        **Obs!** Kontrollera att enheten är ansluten till internet innan du laddar upp. Ett nätverksfel gör att eSIM-konfigurationsfilen inte kan laddas upp.

        Ladda upp eSIM-profilen via en QR-kod eller aktiveringskod och klicka på **Install**. Observera att de flesta eSIM-profiler bara kan hämtas och läggas till en gång.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Tips!** Om du inte har köpt någon eSIM-profil kan du köpa en i eSIM Profile Recommended Store.

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. När uppladdningen är klar öppnar du **Cellular** och klickar på **SIM Card Switch**.

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        Välj **eSIM** som aktivt SIM-kort i popup-fönstret och klicka sedan på **Apply**.

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. Routern börjar ansluta via eSIM-profilen. Vänta och kontrollera att anslutningen upprättas.

    **Konfigurera Nano‑SIM**:

    6. Ta bort bakstycket, ta ut batteriet, sätt in Nano-SIM-kortet i kortplatsen och sätt sedan tillbaka batteriet.

    7. Routern börjar automatiskt ansluta via Nano‑SIM-kortet. Vänta och kontrollera att anslutningen upprättas.

    När internetanslutningen har upprättats visas signalstaplarna och mobilnätsstatusen i pekskärmens övre högra hörn. Du kan också kontrollera anslutningsinformationen i webbadministrationspanelen.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

    !!! Note

        1. Det inbyggda eSIM-kortet och SIM 2 utesluter varandra och kan inte aktiveras samtidigt. eSIM är inaktiverat som standard. Om du aktiverar eSIM fungerar SIM 2 inte, även om ett SIM-kort är isatt.
        2. Eftersom Mudi 7 har ett inbyggt eSIM identifieras ett fysiskt SIMPoYo eSIM-kort som ett vanligt SIM-kort utan eSIM-funktioner på Mudi 7.

=== "Ethernet"

    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Anslut Ethernet-porten på Mudi 7 till en uppströms nätverkskälla (t.ex. ett modem från internetleverantören, en nätverksswitch eller ett Ethernet-uttag i väggen) med en Ethernet-kabel.
    2. Öppna **Network** -> **Ethernet Ports** på pekskärmen eller i webbadministrationspanelen, ange portrollen **WAN** och klicka på **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. När internetanslutningen har upprättats visas en Ethernet-portikon i pekskärmens övre högra hörn. Du kan också kontrollera anslutningsinformationen i webbadministrationspanelen.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Öppna **Internet** -> **Repeater** på pekskärmen eller i webbadministrationspanelen och klicka på **Connect**. Mudi 7 börjar söka efter tillgängliga Wi-Fi-nätverk.
    2. Välj det Wi-Fi-nätverk som du vill utöka med Mudi 7.
    3. Ange lösenordet och klicka på **Apply**.
    4. När internetanslutningen har upprättats visas en Wi-Fi-ikon i pekskärmens övre högra hörn. Du kan också kontrollera anslutningsinformationen i webbadministrationspanelen.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till USB-C-porten på Mudi 7 med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera **USB Tethering**. På iPhone trycker du på **Trust This Device** om du uppmanas att göra det.
    3. När du uppmanas att välja USB-läge på pekskärmen väljer du **Host (USB OTG) mode**. Mudi 7 ansluter sedan automatiskt till enheten. Om anslutningen inte upprättas upprepar du stegen ovan eller loggar in på webbadministrationspanelen och kontrollerar Tethering-anslutningen på sidan INTERNET.

        Klicka [här](../../tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg.md) för att läsa mer om skillnaderna mellan USB-lägena.

    4. När internetanslutningen har upprättats visas en kedjelänksikon i pekskärmens övre högra hörn. Du kan också kontrollera anslutningsinformationen i webbadministrationspanelen.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 har en **OTG-aktiverad** USB-C-port som gör att du kan lägga till en andra Ethernet-port för Dual-Ethernet WAN. Detta kräver en **USB‑C-till-Ethernet-adapter som säljs separat**.

    <small>*USB OTG (On-The-Go) är en USB-standard som gör att kompatibla enheter, till exempel routrar, kan växla mellan värd- och periferienhetsroller. Det möjliggör direkt dataöverföring och ströminteraktion utan en separat värdenhet.</small>

    1. Anslut en uppströms nätverkskälla (t.ex. ett modem från internetleverantören, en nätverksswitch eller ett Ethernet-uttag i väggen) till USB-C-porten på Mudi 7 via en USB C-till-Ethernet-adapter.
    2. Öppna **Network** -> **Ethernet Ports** -> **USB Ethernet Port** på pekskärmen eller i webbadministrationspanelen, ange portrollen **WAN** och klicka på **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 ansluter sedan automatiskt till enheten. Om anslutningen inte upprättas upprepar du stegen ovan eller loggar in på webbadministrationspanelen och kontrollerar USB Ethernet-anslutningen på sidan INTERNET.
    4. När internetanslutningen har upprättats visas en USB-ikon och en Ethernet-portikon i pekskärmens övre högra hörn. Du kan också kontrollera anslutningsinformationen i webbadministrationspanelen.

    Klicka [här](../../tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg.md) för mer information om USB-C OTG på Mudi 7.

## Firmwareuppgradering {#firmware-upgrade}

!!! Note "Observera följande före uppgradering:"

    1. Välj **Keep Settings** på uppgraderingssidan om du vill behålla konfigurationerna för Mudi 7.
    2. Välj inte Keep Settings vid nedgradering eftersom kompatibilitetsproblem kan uppstå.
    3. En firmwareuppgradering förbrukar en viss mängd data. Om SIM-kortets dataplan är begränsad rekommenderas att du ansluter routern till internet på något annat sätt (t.ex. Repeater eller USB Tethering) för att undvika ytterligare dataförbrukning.

Du kan uppgradera firmware för Mudi 7 via pekskärmen eller webbadministrationspanelen.

### Uppgradera via pekskärmen {#upgrade-via-touchscreen}

1. Anslut Mudi 7 till internet.

2. När anslutningen har upprättats söker systemet automatiskt efter tillgängliga firmwareuppdateringar. Om ny firmware är tillgänglig visas ett meddelande på skärmen. Klicka på **Go to Upgrade** i popup-fönstret för att fortsätta.

    ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. Om popup-fönstret inte visas klickar du på **More** på startskärmen -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade** och följer sedan anvisningarna på skärmen för att uppgradera firmware.

    ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Uppgradera via webben {#upgrade-via-web}

Logga in på webbadministrationspanelen och öppna **SYSTEM** -> **Upgrade**. Du kan uppgradera routerns firmware online eller lokalt.

Mer information finns i [here](../../interface_guide/upgrade.md).

## Fabriksåterställning {#factory-reset}

Du kan återställa Mudi 7 på tre sätt: direkt på pekskärmen, med Reset-knappen eller via webbadministrationspanelen.

**Obs!** Kontrollera att Mudi 7 har startat helt innan du återställer den. Tryck INTE på återställningsknappen omedelbart efter start eftersom detta kan utlösa U-Boot-felsäkert läge.

Titta på videon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Återställ via pekskärmen {#reset-via-touchscreen}

1. Tryck på **More** på startsidan.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset1.png){class="glboxshadow" width="300"}

2. Bläddra längst ned på sidan More och tryck på **Reset**.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset2.png){class="glboxshadow" width="300"}

3. Tryck på Reset igen för att bekräfta. Routern återställs och startas sedan om.

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset3.png){class="glboxshadow" width="300"}

### Återställ med knappen {#reset-via-button}

1. Ta bort bakstycket. Återställningsknappen sitter enligt bilden nedan.

    ![reset button](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

2. Utför en mjuk återställning eller fabriksåterställning efter behov.

    - **Soft Reset**: Om du vill starta om nätverksanslutningen utan att radera data håller du återställningsknappen intryckt i **4 sekunder** och släpper den sedan för att reparera nätverket. Följ meddelandena på skärmen medan du håller knappen intryckt. Nätverksgränssnittet startas om, men Wi-Fi-inställningar, VPN-konfigurationer (inaktiverade), systeminställningar med mera bevaras. Om Wi-Fi har inaktiverats återställer en mjuk återställning Wi-Fi till standardläget aktiverat. En mjuk återställning kan också användas för att snabbt växla enheten från ett annat läge till routerläge.

    - **Factory Reset**: Håll återställningsknappen intryckt i **10 sekunder** och släpp den sedan för att utföra en fullständig återställning. Följ meddelandena på skärmen medan du håller knappen intryckt. Alla inställningar raderas. Fortsätt försiktigt.

### Återställ via webben {#reset-via-web}

1. Logga in på webbadministrationspanelen och öppna **SYSTEM** -> **Reset Firmware**.

2. Klicka på **Delete All and Reboot**. Routern återställs och startas sedan om.

    ![web reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/web_reset.png){class="glboxshadow"}

## Logga in på webbadministrationspanelen {#log-in-to-web-admin-panel}

Du kan logga in på webbadministrationspanelen för Mudi 7 för att konfigurera eller kontrollera fler inställningar.

Anslut först en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till Mudi 7 via Wi-Fi, en Ethernet-kabel eller en USB-kabel.

- **Wi-Fi**

    - <u>QR code</u>: Skanna QR-koden på skärmen på Mudi 7 med enheten. Klicka sedan på "Join" på enheten för att ansluta.
    - <u>Manual Connect</u>: Öppna Settings -> WLAN på enheten, leta reda på Wi-Fi-nätverksnamnet för Mudi 7 i listan över tillgängliga nätverk och ange lösenordet för att ansluta. Standardnamnet och standardlösenordet för nätverket finns på etiketten.

- **Ethernet**

    Anslut enheten till Ethernet-porten (LAN som standard) på Mudi 7 med en Ethernet-kabel.

- **USB**

    Anslut enheten till USB-C-porten på Mudi 7 med en USB-kabel. Den OTG-aktiverade USB-C-porten gör att du kan öppna WebGUI för Mudi 7 i nästa steg.

Öppna sedan en webbläsare och ange `192.168.8.1` i adressfältet för att öppna inloggningssidan. Välj språk, ange administratörslösenordet och klicka på **Apply**.

Du loggas sedan in på webbadministrationspanelen för Mudi 7.

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Mudi 7.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningarna för Wi-Fi-nätverk på 6 GHz, 5 GHz och 2.4 GHz. Du kan bland annat aktivera Wi-Fi, ange sändningseffekt och Wi-Fi-namn (SSID), aktivera slumpmässig BSSID, välja Wi-Fi-säkerhetsläge och lösenord, konfigurera SSID-synlighet samt välja Wi-Fi-läge, bandbredd och kanal.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

**Obs!** De trådlösa inställningarna för Mudi 7 skiljer sig på vissa punkter från andra GL.iNet Wi-Fi 7-routrar.

1. På grund av maskinvarubegränsningar i chipsetet kan Wi-Fi på 5 GHz och 6 GHz inte aktiveras samtidigt.
2. När Repeater är aktiverat inaktiveras Guest Network automatiskt.
3. Enligt gällande bestämmelser ska Wi-Fi ställas in på Outdoor-läge när det används utomhus. Det kan minska täckningsområdet. Du kan växla Usage Environment (Indoor eller Outdoor) högst upp på sidan Wireless.

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GL.iNet Account"

    Med GL.iNet Account kan du ansluta och hantera dina enheter och molntjänster. Med ett enda GL.iNet Account får du smidig åtkomst till både GoodCloud och glinet App för en säker och förbättrad upplevelse. Det gör det enklare att hantera nätverket var du än är och när som helst.

    Information om hur du konfigurerar GL.iNet Account finns i [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNets molnhanteringstjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.
    
    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

    Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Mudi 7 stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Mudi 7 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ dessa guider för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi 7 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ dessa guider för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet, repeater, internetdelning, mobilnät och USB Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    På den här sidan kan du konfigurera och hantera **Main Network**, **Guest Network**, **IoT Network** och egna **VLAN Networks** centralt. Du kan skapa och hantera flera subnät för att isolera olika typer av enheter eller trafik.

    Information om hur du konfigurerar subnet finns i [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du ange Ethernet-portens roll (dvs. använda den som WAN/LAN), ändra MAC-läge och MAC-adress för WAN-gränssnittet samt visa den förhandlade porthastigheten.

    Mudi 7 har en Ethernet-port som är inställd på LAN som standard. Vid behov kan du ändra den till en WAN-port på pekskärmen eller i webbadministrationspanelen.

    Information om hur du konfigurerar ethernet Port finns i [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, en förkortning av Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.
    
    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.
    
    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Nätverksläge avser den konfiguration som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.
    
    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

    **Obs!** Mudi 7 stöder lägena Router, Access Point och Extender. WDS-läge stöds inte.

=== "Drop-in gateway"

    En drop-in-gateway utökar huvudrouterns funktioner med bland annat AdGuard Home, krypterad DNS och VPN-klient.
    
    Använd följande länkar för att konfigurera en drop-in-gateway:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Nätverksacceleration kan minska processorbelastningen och påskynda vidarebefordran av trafikpaket.
    
    Information om hur du konfigurerar nätverksacceleration finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control {#flow-control}

=== "DPI Engine"

    DPI (Deep Packet Inspection) är en central funktion för intelligent nätverkshantering. Den övervinner begränsningen hos traditionella routrar, som endast identifierar käll- eller destinationsadresser, genom att analysera datapaketens nyttolast på djupet och exakt identifiera program och webbplatser som användaren öppnar genom jämförelse med ett funktionsbibliotek. Det möjliggör detaljerad klassificering och styrning av trafiken.
    
    GL.iNets DPI-funktion är integrerad med [Netify](https://www.netify.ai/){target="_blank"} och använder ett resurssnålt inbäddat insticksprogram för effektiv distribution. Netifys signaturdatabas uppdateras online och möjliggör tillförlitlig hantering, vilket gör nätverksstyrningen mer exakt och effektiv.

    Mer information finns i [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics erbjuder en intelligent instrumentpanel för trafikinformation som kategoriserar och visualiserar nätverksanvändningen efter program. Den hjälper dig att övervaka trafik i realtid och historisk trafik för bättre insyn och kontroll över nätverket.

    Mer information finns i [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter ger intelligent säkerhet online med DPI-baserad klassificering. Funktionen blockerar automatiskt skadliga webbplatser för att hålla nätverket rent och säkert.

    Mer information finns i [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) optimerar bandbreddstilldelningen genom att prioritera viktiga aktiviteter (t.ex. videosamtal och spel) när nätverket är överbelastat. Det minskar latensen och förbättrar nätverkets övergripande prestanda. Observera att detta gäller lokal klienttrafik och tunneltrafik från VPN Client, men inte trafik som tas emot när routern fungerar som VPN Server.

    Mer information finns i [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) hanterar routerns nätverkstrafik intelligent för att minimera latens och ”bufferbloat”, vilket ger smidigare spel och röstsamtal.

    Mer information finns i [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionen kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Information om hur du konfigurerar parental control finns i [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Security {#security}

=== "Port Forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Information om hur du konfigurerar port forwarding finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, en förkortning av Access Control List, låter dig skapa regler för att hantera nätverkstrafik utifrån anslutningsprotokoll, enhetsadresser och portar. Funktionen styr om nätverksåtkomst ska tillåtas eller blockeras. Om flera ACL-regler står i konflikt tillämpar systemet regeln med högst prioritet.

    Mer information finns i [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Med Admin Access kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller följande alternativ:

    * Local Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.
    * Open Ports on Router: Styr vilka portar som är öppna på routern för att begränsa möjliga sårbarheter och obehörig åtkomst.

    Mer information finns i [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    På sidan NAT Mode kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG.

    Information om hur du konfigurerar NAT settings finns i [NAT Mode](../../interface_guide/nat_settings.md).

## Program {#applications}

=== "Plug-ins"

    Ett insticksprogram är en programvarukomponent som lägger till särskilda funktioner i ett befintligt datorprogram. På så sätt kan programmets funktioner anpassas och utökas.

    Information om hur du konfigurerar insticksprogram finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress.

    Information om hur du konfigurerar Dynamic DNS finns i [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Nätverkslagring är en central lösning för datalagring där flera användare och enheter kan komma åt och dela filer via ett nätverk.

    Information om hur du konfigurerar nätverkslagring finns i [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home är en lösning som blockerar annonser och spårare i hela nätverket. Den fungerar som en DNS-server som filtrerar oönskat innehåll på alla enheter som är anslutna till hemnätverket.

    Information om hur du konfigurerar AdGuard Home finns i [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.
    
    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.
    
    Information om hur du konfigurerar ZeroTier finns i [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, en förkortning av The Onion Router, är ett integritetsfokuserat nätverk som möjliggör anonym kommunikation över internet. Internettrafiken dirigeras genom flera servrar (noder) som drivs av frivilliga för att dölja användarens plats och aktivitet. Det gör det svårt att spåra aktiviteter online.

    Information om hur du konfigurerar Tor finns i [Tor](../../interface_guide/tor.md).

## System {#system}

=== "Overview"

    Sidan Overview ger en heltäckande översikt över routerns aktuella status och prestandamätvärden. På sidan kan du visa:

    * CPU Average Load: Övervaka den genomsnittliga belastningen på routerns processor för att bedöma prestandan och identifiera möjliga flaskhalsar.
    * Memory Usage: Kontrollera hur mycket av routerns minne som används för att underlätta resurshanteringen.
    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.
    * Flash Usage: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
    * Device Info: Visa detaljerad information om routersystemet, däribland drifttid, värdnamn, modell, arkitektur, OpenWrt-version, kärnversion, enhets-ID, enhetens MAC-adress och enhetens serienummer.
    * External Storage: Kontrollera statusen för externa lagringsenheter som är anslutna till routern, till exempel USB-enheter och TF-kort.

    Dessa funktioner ger viktig information och viktiga kontroller som hjälper dig att effektivt hantera och övervaka routern.

    Detaljerade anvisningar finns i [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    På sidan Admin Password kan du ange eller ändra lösenordet för routerns administratörsgränssnitt.

    Administratörslösenordet måste uppfylla följande krav:

    * Minst 10 och högst 63 tecken.
    * Bokstäver (skiftlägeskänsliga), siffror och symbolerna `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` tillåts.
    * Minst två av följande teckentyper krävs: versaler, gemener, siffror och symboler.

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade anvisningar finns i [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Obs!** Mudi 7 stöder inte scheman för LED-visning eller Wi-Fi-status.

=== "Display Management"

    På sidan Display Management kan du hantera pekskärmen och tillhörande inställningar.

    - Wallpaper: Anpassa bakgrundsbilden och skärmens stil när den aktiveras.
    - Brightness: Justera pekskärmens ljusstyrka med reglaget eller ange en procentsats efter ljusförhållandena.
    - Personalised Signature: Lägg till egen text på pekskärmen för en personlig stil eller snabb identifiering.
    - Auto Lock: Ange hur lång tid utan aktivitet som ska gå innan skärmen låses automatiskt. Intervallet är 15 sekunder till 5 minuter.
    - Passcode: Ange en kod för pekskärmen som ett extra säkerhetslager.

    Detaljerade anvisningar finns i [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    På sidan USB & Power kan du konfigurera USB-relaterade inställningar och strömhantering för routern, till exempel USB-protokoll, strömriktning, tidsgränser för inaktivitet och väntelägesfunktion.

    Detaljerade anvisningar finns i [USB & Power](../../interface_guide/usb_power.md).

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade anvisningar finns i [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade anvisningar finns i [Advanced Settings](../../interface_guide/advanced_settings.md).

## Batterisäkerhet {#battery-safety}

Sluta använda och ladda Mudi 7 om batteriet är svullet, läcker, är ovanligt varmt eller skadat eller avger en ovanlig lukt.

- Tryck inte på, böj inte, punktera inte och krossa inte batteriet och utsätt det inte för tryck.
- Använd inte verktyg för att bända mot ett svullet eller skadat batteri.
- Försök inte ta ut ett batteri som är svullet, sitter fast, läcker, är varmt eller på annat sätt är osäkert att hantera.
- Lägg inte ett skadat litiumjonbatteri i hushållsavfall eller vanlig återvinning.
- Skicka inte ett svullet eller skadat batteri med vanlig post eller pakettjänst.
- Kontakta [GL.iNet Support](https://www.gl-inet.com/contacts/) för garantiassistans och nästa steg.

Om det skadade batteriet redan har tagits ut ska du inte sätta tillbaka det. Kontakta en lämplig lokal återvinningscentral för batterier eller anläggning för farligt hushållsavfall som tar emot skadade litiumjonbatterier.

Om batteriet ryker, snabbt blir varmt, väser, brinner eller på annat sätt utgör en omedelbar fara ska du avlägsna dig från enheten och kontakta den lokala räddningstjänsten.
