# Användarhandbok för Fortify (GL-MT6000) {#fortify-gl-mt6000-user-guide}

## Produktöversikt {#product-overview}

Fortify (GL-MT6000) är en gemensamt varumärkesprofilerad Wi-Fi 6-router från GL.iNet och ExpressVPN. Varje enhet levereras med en kostnadsfri ettårsprenumeration på ExpressVPN. Du kan lösa in prenumerationen och ansluta kontot direkt i routerns webbadministrationspanel. När en ExpressVPN-tunnel är ansluten krypterar och dirigerar routern trafik genom tunneln enligt dina VPN-principer.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Fortify (GL-MT6000)
- 1 x användarhandbok
- 1 x aktiveringsguide för ExpressVPN
- 1 x Ethernet-kabel
- 1 x nätadapter
- 1 x tackkort
- 1 x adapter (beroende på leveransland)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/unboxing.png){class="glboxshadow"}

Titta på uppackningsvideon för Fortify nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IQEfj7Hff7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfigurera Fortify {#how-to-set-up-fortify}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/FymI3LCRMTA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till Fortify-routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Öppna Settings -> WLAN på enheten, leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk och ange lösenordet för att ansluta. Standardnamnet och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk i det övre högra hörnet, ange administratörslösenordet och klicka sedan på **Next**. Lösenordet måste innehålla 10–63 tecken och minst två av följande: versaler, gemener, siffror och specialtecken.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Konfigurera Wi-Fi. Observera att enheten måste anslutas till routerns Wi-Fi igen med de uppdaterade inloggningsuppgifterna om du ändrar Wi-Fi-informationen.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet web Admin Panel. Om du föredrar [GL.iNet-appen](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"} hämtar du den och följer anvisningarna på skärmen.

Konfigurera Fortify med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Anslut WAN-porten på Fortify-routern till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.

    När internetanslutningen har upprättats lyser routerns LED med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Öppna INTERNET -> avsnittet Repeater i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats lyser routerns LED med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Anslut smarttelefonen till routerns USB-port med en USB-kabel.
    2. Öppna Settings på smarttelefonen och aktivera USB Tethering. På iPhone godkänner du enheten och aktiverar Personal Hotspot.
    3. Öppna INTERNET -> avsnittet Tethering i webbadministrationspanelen och klicka på **Connect**.

    När internetanslutningen har upprättats lyser routerns LED med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Anslut ett USB-modem för mobilnät till routerns USB-port. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.

    När internetanslutningen har upprättats lyser routerns LED med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via mobilnät](../../interface_guide/internet_cellular.md).

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Fortify.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera Wi-Fi-nätverken på Fortify, däribland Main Network, Guest Network och IoT Network. Varje nätverk stöder både 2.4 GHz- och 5 GHz-banden.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter, däribland enhetsnamn, anslutningstyp, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt trafik. Du kan även blockera en viss klient med ett klick eller utföra andra åtgärder.

Mer information finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera dina GL.iNet-routrar.

    Mer information finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en funktion för smidiga fjärrnätverk på GL.iNet-routrar. Den använder AmneziaWG-protokollet med inbyggd trafikobfuskering och ger stabil och säker fjärråtkomst när och var som helst.

    Mer information finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) upprättar säkra, krypterade trafiktunnlar mellan den lokala enheten och VPN-servern. Det ger VPN-klienten ytterligare integritet och säkerhet och möjliggör åtkomst till VPN-serverns fjärrnätverk.

Fortify är integrerad med [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, så att du kan aktivera en ExpressVPN-anslutning på några minuter. Varje Fortify-enhet levereras med en kostnadsfri ettårsprenumeration på ExpressVPN. Du kan lösa in prenumerationen och ansluta ExpressVPN-kontot direkt i routerns webbadministrationspanel. När en ExpressVPN-tunnel är ansluten krypterar och dirigerar routern trafik genom tunneln enligt dina VPN-principer.

Information om hur du löser in den kostnadsfria prenumerationen och konfigurerar en VPN-tunnel finns i [ExpressVPN Activation Guide](../../interface_guide/expressvpn_activation_guide.md).

Information om hur du konfigurerar an OpenVPN server finns i [OpenVPN Server](../../interface_guide/openvpn_server.md).

Information om hur du konfigurerar a WireGuard server finns i [WireGuard Server](../../interface_guide/wireguard_server.md).

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Mer information finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Ett LAN, eller Local Area Network, ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller kontor. Det är det lokala nätverk som enheten ansluter till via huvudnätverkets Wi-Fi eller en Ethernet-kabel. Sidan LAN omfattar Basic Settings, DHCP Server Settings och Address Reservation.

    Mer information finns i [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    På sidan Guest Network kan du skapa ett särskilt Wi-Fi-nätverk för besökare. Det är isolerat från det primära nätverket och förbättrar säkerheten samtidigt som det ger smidig internetåtkomst. Du kan ange ett gästsubnät inom de privata IPv4-adressintervallen `192.168.0.0/16`, `172.16.0.0/12` eller `10.0.0.0/8` samt ange IP-adresserna för gateway och nätmask.

    Mer information finns i [Guest Network](../../interface_guide/guest_network.md).

=== "IoT Network"

    På sidan IoT Network kan du skapa ett särskilt Wi-Fi-nätverk för IoT-enheter. Det är isolerat från det primära nätverket och ger bättre kompatibilitet och säkerhet.

    Mer information finns i [IoT Network](../../interface_guide/iot_network.md).

<br>

=== "DNS"

    Routerns DNS-inställningar styr hur domännamn översätts till IP-adresser. På sidan kan du använda DNS-servrar som automatiskt hämtas från uppströms enheter eller ange egna och konfigurera DNS-prioriteter.

    Mer information finns i [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du hantera Ethernet-portarnas roller (WAN/LAN) och visa portinformation som MAC-adress och förhandlad hastighet.

    Mer information finns i [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Mer information finns i [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Mer information finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

<br>

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN.

    Information om hur du konfigurerar en drop-in-gateway finns i [Konfigurera en drop-in-gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

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

<br>

=== "QoS"

    QoS (Quality of Service) optimerar bandbreddstilldelningen genom att prioritera viktiga aktiviteter (t.ex. videosamtal och spel) när nätverket är överbelastat. Det minskar latensen och förbättrar nätverkets övergripande prestanda. Observera att detta gäller lokal klienttrafik och tunneltrafik från VPN Client, men inte trafik som tas emot när routern fungerar som VPN Server.

    Mer information finns i [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) hanterar routerns nätverkstrafik intelligent för att minimera latens och ”bufferbloat”, vilket ger smidigare spel och röstsamtal.

    Mer information finns i [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionen kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Mer information finns i [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Security {#security}

=== "Port forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Mer information finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, en förkortning av Access Control List, låter dig skapa regler för att hantera nätverkstrafik utifrån anslutningsprotokoll, enhetsadresser och portar. Funktionen styr om nätverksåtkomst ska tillåtas eller blockeras. Om flera ACL-regler står i konflikt tillämpar systemet regeln med högst prioritet.

    Mer information finns i [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Med Admin Access kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller följande alternativ:

    * Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.
    * Open Ports on Router: Styr vilka portar som är öppna på routern för att begränsa möjliga sårbarheter och obehörig åtkomst.

    Mer information finns i [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    På sidan NAT Mode kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG (Application Layer Gateway).

    Mer information finns i [NAT Mode](../../interface_guide/nat_settings.md).

## Program {#applications}

=== "Plug-ins"

    Ett insticksprogram är en programvarukomponent som lägger till särskilda funktioner i ett befintligt datorprogram. På så sätt kan programmets funktioner anpassas och utökas.

    Mer information finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress.

    Mer information finns i [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Nätverkslagring är en central lösning för datalagring där flera användare och enheter kan komma åt och dela filer via ett nätverk.

    Mer information finns i [Network Storage](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home är en lösning som blockerar annonser och spårare i hela nätverket. Den fungerar som en DNS-server som filtrerar oönskat innehåll på alla enheter som är anslutna till hemnätverket.

    Mer information finns i [AdGuard Home](../../interface_guide/adguardhome.md).

<br>

=== "Bark"

    Tjänsten [Bark](https://www.bark.us/){target="_blank"} kan skydda ditt barns digitala miljö och ge heltäckande skydd online. Den kräver vanligtvis en betalprenumeration. Genom GL.iNets samarbete med Bark erbjuds dock abonnemanget Bark Home utan kostnad på Fortify (GL-MT6000), med avancerad övervakning och varningar utan extra kostnad.

    Mer information finns i [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger säker och enkel åtkomst till dina enheter och program var som helst i världen.

    Fortify (GL-MT6000) är integrerad med Tailscale, så att routern kan anslutas till ett virtuellt Tailscale-nätverk. När den är ansluten kan du fjärransluta till den och dess WAN- och LAN-resurser.

    Mer information finns i [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.

    Mer information finns i [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor (från The Onion Router) är kostnadsfri programvara med öppen källkod för anonym kommunikation. Den hjälper användare att använda internet med skyddad integritet.

    Mer information finns i [Tor](../../interface_guide/tor.md).

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

    Mer information finns i [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    På sidan Admin Password kan du ange eller ändra lösenordet för routerns administratörsgränssnitt.

    Mer information finns i [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två alternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Mer information finns i [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * 5GHz / 2.4GHz Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-banden 5GHz/2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Mer information finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

<br>

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Mer information finns i [Time Zone](../../interface_guide/time_zone.md).

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
