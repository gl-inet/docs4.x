# Användarhandbok för Slate 7 (GL-BE3600) {#slate-7-gl-be3600-user-guide}

## Produktöversikt {#product-overview}

Slate 7 (GL-BE3600) är GL.iNets första bärbara Wi-Fi 7-reserouter med dubbla band. Den bygger på avancerad Wi-Fi 7-teknik, däribland Multi-Link Operation och 4K QAM. De teoretiska hastigheterna är 688Mbps (2.4GHz) och 2882Mbps (5GHz), vilket möjliggör smidig 8K-strömning och mobilspel. Pekskärmen ger snabb överblick över nätverksstatus och intuitiv grundläggande styrning.

Routern har 2× 2.5G Ethernet-portar (1 WAN + 1 LAN) och 1× USB 3.0-port för snabba kabelanslutningar och flexibel lagringsutökning. Den stöder även Type-C PD-strömförsörjning (5V/3A, 9V/3A, 12V/2.5A) och har en kompakt, lätt design. AdGuard Home är förinstallerat och routern är kompatibel med över 30 VPN-tjänster, vilket ger robust nätverkssäkerhet. Slate 7 kombinerar mobil användning med professionell prestanda och passar för distansarbete och nätverksdelning på resan.

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Slate 7 (GL-BE3600)
- 1 x användarhandbok
- 1 x tackkort
- 1 x Ethernet-kabel
- 1 x strömkabel
- 1 x nätadapter för USA
- 3 x adaptrar (EU-, UK- och AU-kontakter)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Titta på uppackningsvideon för Slate 7 nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Touchscreen {#touchscreen}

| Screen Display                    | Description         |
| :-------------------------------- | :------------------ |
| ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){width="400"} | Starting up |
| ![network](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){width="400"} | Network connection types and status<br>**Green**: Active / Connected<br>**Yellow**: Connecting / Abnormal <br>**White**: Inactive connection |
| ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){width="400"} | Wi-Fi-information, däribland SSID, lösenord, QR-kod och på/av-knapp |
| ![vpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/vpn_client.png){width="400"} | VPN status. It requires initial setup in the web admin panel |
| ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){width="400"} | AdGuard Home |
| ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){width="400"} | Tor |
| ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){width="400"} | Trafikstatistik<br>Avser genomsnittshastigheten för all trafik genom routern, beräknad var 3:e sekund |
| ![system usage](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){width="400"} | System usage |
| ![time zone](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){width="400"} | Time zone |
| ![system menu](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){width="400"} | System menu<br>Swipe from top to bottom to access system menu |
| ![unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){width="400"} | Tryck på skärmen för att aktivera den och svep från vänster till höger för att låsa upp |
| ![reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){width="400"} | After clicking "Reboot", slide from left to right to confirm |

## Konfigurera Slate 7 {#how-to-set-up-slate-7}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(I videon visar vi konfigurationen genom att ställa in Slate 7 som Repeater. Följ stegen nedan om du vill konfigurera Slate 7 med andra internetanslutningsmetoder.)</small>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk på enheten och ange lösenordet för att ansluta. Standardnamnet och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel. Om du föredrar att använda GL.iNet-appen kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

Konfigurera Slate 7 med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}

    Anslut WAN-porten på Slate 7 till en uppströms enhet (t.ex. ett modem) med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera USB Tethering.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Anslut ett USB-modem för mobilnät till USB-porten på Slate 7. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Cellular på sidan INTERNET.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Slate 7.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningarna för Wi-Fi-nätverk på både 5 GHz och 2.4 GHz. Du kan bland annat aktivera Wi-Fi, ange sändningseffekt och Wi-Fi-namn (SSID), aktivera slumpmässig BSSID, välja Wi-Fi-säkerhetsläge och lösenord, konfigurera SSID-synlighet samt välja Wi-Fi-läge, bandbredd och kanal.

Dessutom stöder Slate 7 MLO Wi-Fi, dvs. Multi-Link Operation, som kombinerar flera trådlösa nätverk samtidigt för högre bandbredd och tillförlitligare anslutningar.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Slate 7 stöder OpenVPN, WireGuard och Tor.

=== "OpenVPN"

    Slate 7 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, en förkortning av The Onion Router, är ett integritetsfokuserat nätverk som möjliggör anonym kommunikation över internet. Internettrafiken dirigeras genom flera servrar (noder) som drivs av frivilliga för att dölja användarens plats och aktivitet. Det gör det svårt att spåra aktiviteter online.

    * [How to set up Tor](../../interface_guide/tor.md)

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

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionerna kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Information om hur du konfigurerar föräldrakontroll finns i [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.

    Information om hur du konfigurerar ZeroTier finns i [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.

    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

## Network {#network}

=== "Port forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Information om hur du konfigurerar port forwarding finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.

    Information om hur du konfigurerar LAN finns i [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Du kan ange ett subnät inom de privata IPv4-adressintervallen 192.168.0.0/16, 172.16.0.0/12 eller 10.0.0.0/8, ange IP-adresserna för gateway och nätmask samt konfigurera säkerhetsinställningar som AP-isolering för gästnätverket.

    Information om hur du konfigurerar gästnätverket finns i [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du konfigurera WAN- och LAN-portarna, ange Ethernet för WAN/LAN-gränssnittet, ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

    Information om hur du hanterar Ethernet-portar finns i [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    En drop-in-gateway utökar huvudrouterns funktioner med bland annat AdGuard Home, krypterad DNS och VPN-klient.

    Använd följande länkar för att konfigurera en drop-in-gateway:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Nätverksacceleration kan minska processorbelastningen och påskynda vidarebefordran av trafikpaket.

    Information om hur du konfigurerar nätverksacceleration finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    På sidan NAT Settings kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG (Application Layer Gateway).

    Information om hur du konfigurerar NAT-inställningar finns i [NAT Settings](../../interface_guide/nat_settings.md).

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

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade anvisningar finns i [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-banden 5GHz/2.4GHz/MLO för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Display Management"

    Sidan Display Management innehåller en komplett uppsättning funktioner för att hantera pekskärmen och tillhörande inställningar.

    - Function Management: Hantera vilka funktioner som visas på pekskärmen och anpassa skärmen efter dina behov.
    - Lock Screen: Anpassa inställningarna för låsskärmen. Du kan ange bakgrundsbild och skärmaktivering.
    - Brightness: Justera pekskärmens ljusstyrka med reglaget eller ange en nivå mellan 1 och 10 efter ljusförhållandena.
    - Auto Lock: Ange hur lång tid utan aktivitet som ska gå innan skärmen låses automatiskt. Intervallet är 1 till 30 minuter.
    - Screen Always On: Växla alternativet för att ange om pekskärmen ska vara på hela tiden eller stängas av efter inaktivitet.
    - Enable Screen Passcode: Aktivera en kod för pekskärmen som ett extra säkerhetslager.

    Detaljerade anvisningar finns i [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    På sidan Toggle Button Settings kan du konfigurera routerns fysiska växlingsknapp och tilldela den särskilda funktioner för snabb åtkomst och styrning. Funktionen ger praktiska genvägar till vanliga uppgifter och inställningar och förenklar routerhanteringen.

    Detaljerade anvisningar finns i [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade anvisningar finns i [Log](../../interface_guide/log.md).

=== "Security"

    På sidan Security kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller alternativ för:

    * Admin Password: Ange eller ändra lösenordet för routerns administratörsgränssnitt så att endast behöriga användare kan ändra inställningarna.
    * Local Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.
    * Open Ports on Router: Styr vilka portar som är öppna på routern för att begränsa möjliga sårbarheter och obehörig åtkomst.

    Dessa inställningar hjälper dig att upprätthålla en säker nätverksmiljö som skyddar både routern och anslutna enheter.

    Detaljerade anvisningar finns i [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade anvisningar finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
