# Användarhandbok för Slate 7 Pro (GL-BE10000) {#slate-7-pro-gl-be10000-user-guide}

## Produktöversikt {#product-overview}

Slate 7 Pro (GL-BE10000) är en bärbar Wi‑Fi 7-reserouter med tre band. Som uppgraderad version av Slate 7 (GL-BE3600) har den en större pekskärm på ovansidan, 1GB DDR4 RAM och 512MB NAND-flashlagring för stabil prestanda och kompatibilitet med insticksprogram. Den levererar VPN-hastigheter på upp till 1,100 Mbps för WireGuard® och 1,000 Mbps för OpenVPN-DCO. Med 2× 2.5G Ethernet-portar (1 WAN + 1 LAN), 1× USB-C 3.0-port och stöd för PD-ström ger den god anslutning och smidig användning på resan.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

Förpackningen innehåller:

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x användarhandbok
- 1 x tackkort
- 1 x Ethernet-kabel
- 1 x strömkabel
- 1 x nätadapter
- 4 x adaptrar (US-, EU-, UK- och AU-kontakter)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/unboxing.png){class="glboxshadow"}

Titta på uppackningsvideon för Slate 7 Pro nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zNxb5gl2tfg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Touchscreen {#touchscreen}

| Screen Display                    | Description         |
| :-------------------------------- | :------------------ |
| ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){width="500"} | Starting up |
| ![set up admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){width="400"} | Set admin password |
| ![set up wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){width="400"} | Set Wi-Fi |
| ![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){width="400"} | Home screen<br>**Left**: System time, network speed, and shortcuts for Wi-Fi, Clients, VPN, and other functions.<br>**Right**: Four connection modes: Ethernet, Repeater, Tethering, and Cellular |
| ![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){width="400"} | Network status<br>**Blue**: Active / Connected to Internet<br>**Yellow**: Connecting / Network Failure<br>**White**: Inactive connection

## Konfigurera Slate 7 Pro {#how-to-set-up-slate-7-pro}

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk på enheten och ange lösenordet för att ansluta. Standardnamnet (SSID) och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

Konfigurera Slate 7 Pro med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}

    1. Anslut WAN-porten på Slate 7 Pro till en uppströms enhet (t.ex. ett modem från internetleverantören, en nätverksswitch eller ett Ethernet-uttag i väggen) med en Ethernet-kabel.
    2. Slate 7 Pro försöker automatiskt hämta nätverksparametrar som IP-adress, gateway och DNS-server för att upprätta en Ethernet-anslutning.
    3. När internetanslutningen har upprättats blir avsnittet Ethernet på pekskärmens startsida blått (aktivt). Tryck på Ethernet på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Tryck på **Repeater** på pekskärmen. Enheten börjar söka efter tillgängliga Wi-Fi-nätverk.
    2. Välj det Wi-Fi-nätverk som du vill utöka med Slate 7 Pro.
    3. Ange lösenordet och tryck på **Apply**.
    4. När internetanslutningen har upprättats blir avsnittet Repeater på pekskärmens startsida blått (aktivt). Tryck på Repeater på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera **USB Tethering** eller **Personal Hotspot**. På iPhone trycker du på **Trust This Device** om du uppmanas att göra det.
    3. Välj **Tethering** på pekskärmen på Slate 7 Pro och tryck på **Connect**. Routern ansluter sedan till enheten.
    4. När internetanslutningen har upprättats blir avsnittet Tethering på pekskärmens startsida blått (aktivt). Tryck på Tethering på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

    **Obs!** Om anslutningen misslyckas kontrollerar du att strömförsörjningen är högre än 9V 3A, eftersom för låg effekt kan hindra USB-porten från att strömsättas. Upprepa stegen ovan eller logga in på webbadministrationspanelen för att kontrollera statusen för Tethering-anslutningen.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Anslut ett USB-modem för mobilnät till USB-porten på Slate 7 Pro. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.
    2. När internetanslutningen har upprättats blir avsnittet Cellular på pekskärmens startsida blått (aktivt). Tryck på Cellular på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Slate 7 Pro.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningarna för Wi-Fi-nätverk på 6GHz, 5 GHz och 2.4 GHz. Du kan bland annat aktivera Wi-Fi, ange sändningseffekt och Wi-Fi-namn (SSID), aktivera slumpmässig BSSID, välja Wi-Fi-säkerhetsläge och lösenord, konfigurera SSID-synlighet samt välja Wi-Fi-läge, bandbredd och kanal.

Dessutom stöder Slate 7 Pro MLO Wi-Fi, dvs. Multi-Link Operation, som kombinerar flera trådlösa nätverk samtidigt för högre bandbredd och tillförlitligare anslutningar.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksfunktion som är integrerad i GL.iNet-routrar. Den ger smidig fjärråtkomst till hemnätverket utan registrering eller inloggning. Genom att använda AmneziaWG-protokollet med inbyggd trafikobfuskering hålls anslutningen stabil och säker, vilket passar för tillförlitlig fjärråtkomst var du än befinner dig. Du kan konfigurera ett AstroWarp-nätverk direkt i GL.iNet-routerns administratörspanel. Parkoppla routrarna med en åtkomstkod för att ansluta reseroutern säkert till hemnätverket på några sekunder.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Slate 7 Pro stöder protokollen OpenVPN och WireGuard.

=== "OpenVPN"

    Slate 7 Pro och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate 7 Pro och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.

    Information om hur du konfigurerar LAN finns i [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Du kan ange ett subnät inom de privata IPv4-adressintervallen 192.168.0.0/16, 172.16.0.0/12 eller 10.0.0.0/8, ange IP-adresserna för gateway och nätmask samt konfigurera säkerhetsinställningar som AP-isolering för gästnätverket.

    Information om hur du konfigurerar gästnätverket finns i [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker och åsidosätta DNS-inställningarna för alla klienter. Du kan även tillåta att anpassad DNS åsidosätter VPN DNS samt ställa in DNS-serverläget på automatiskt eller manuellt ange DNS-servrar från Ethernet-anslutningen.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du hantera Ethernet-portens roll (WAN/LAN), ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

    Information om hur du hanterar Ethernet-portar finns i [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

---

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Nätverksläge avser de olika driftroller och funktioner som en router kan använda för att uppfylla olika behov vid nätverksdistribution. Vanliga nätverkslägen är routerläge, extenderläge och åtkomstpunktsläge.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway är en flexibel funktion som utökar funktionerna hos en befintlig huvudrouter utan att den behöver bytas ut eller konfigureras om. Genom att ange en GL.iNet-router som Drop-in Gateway kan du lägga till avancerade funktioner i den befintliga nätverksinfrastrukturen, till exempel AdGuard Home, VPN och krypterad DNS.

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

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionen kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Mer information finns i [Parental Control](../../interface_guide/parental_control.md).

=== "QoS"

    QoS (Quality of Service) optimerar bandbreddstilldelningen genom att prioritera viktiga aktiviteter (t.ex. videosamtal och spel) när nätverket är överbelastat. Det minskar latensen och förbättrar nätverkets övergripande prestanda. Observera att detta gäller lokal klienttrafik och tunneltrafik från VPN Client, men inte trafik som tas emot när routern fungerar som VPN Server.

    Mer information finns i [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) hanterar routerns nätverkstrafik intelligent för att minimera latens och ”bufferbloat”, vilket ger smidigare spel och röstsamtal.

    Mer information finns i [SQM](../../interface_guide/sqm.md).

## Security {#security}

=== "Port Forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Mer information finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Med Admin Access kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller följande alternativ:

    * Local Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.
    * Open Ports on Router: Styr vilka portar som är öppna på routern för att begränsa möjliga sårbarheter och obehörig åtkomst.

    Mer information finns i [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    På sidan NAT Mode kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG (Application Layer Gateway).

    Mer information finns i [NAT Mode](../../interface_guide/nat_settings.md).

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
    * Flash Usage: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
    * Device Info: Visa detaljerad information om routersystemet, däribland drifttid, värdnamn, modell, arkitektur, OpenWrt-version, kärnversion, enhets-ID, enhetens MAC-adress och enhetens serienummer.
    * External Storage: Kontrollera statusen för externa lagringsenheter som är anslutna till routern, till exempel USB-enheter och TF-kort.

    Dessa funktioner ger viktig information och viktiga kontroller som hjälper dig att effektivt hantera och övervaka routern.

    Mer information finns i [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    På sidan Admin Password kan du hantera lösenordet för routerns administratörsgränssnitt, så att endast behöriga användare kan ändra inställningarna.

    Mer information finns i [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Mer information finns i [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LCD Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LCD-skärm och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-banden 6GHz/5GHz/2.4GHz/MLO, hanterar nätverkets tillgänglighet och minskar strömförbrukningen.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Mer information finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    Sidan Display Management innehåller en komplett uppsättning funktioner för att hantera pekskärmen och tillhörande inställningar.

    ‒ Wallpaper: Anpassa bakgrundsbilden och skärmens stil när den aktiveras.
    ‒ Brightness: Justera pekskärmens ljusstyrka med reglaget eller ange en procentsats efter ljusförhållandena.
    ‒ Auto Lock: Ange hur lång tid utan aktivitet som ska gå innan skärmen låses automatiskt. Intervallet är 1 minut till 30 minuter.
    ‒ Screen Always On: Växla alternativet för att ange om pekskärmen ska vara på hela tiden eller stängas av efter inaktivitet.
    ‒ Enable Screen Passcode: Ange en kod för pekskärmen som ett extra säkerhetslager.

    Mer information finns i [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Mer information finns i [Time Zone](../../interface_guide/time_zone.md).

---

=== "Toggle Button Settings"

    På sidan Toggle Button Settings kan du konfigurera routerns fysiska växlingsknapp och tilldela den särskilda funktioner för snabb åtkomst och styrning. Funktionen ger praktiska genvägar till vanliga uppgifter och inställningar och förenklar routerhanteringen.

    Mer information finns i [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Mer information finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Mer information finns i [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Mer information finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
