# Användarhandbok för Brume 3 (GL-MT5000) {#brume-3-gl-mt5000-user-guide}

## Produktöversikt {#product-overview}

Brume 3 (GL-MT5000) är en högpresterande säkerhetsgateway med OpenWrt v21.02, en fyrkärnig MediaTek Cortex-A53-processor, 1GB RAM och 8GB eMMC-lagring för insticksprogram. Den kompakta designen passar installationer med begränsat utrymme. Den stöder VPN-server i hemmet, plats-till-plats-SD-WAN och över 30 VPN-tjänster för säker anslutning mellan platser. Dessutom ingår GL.iNets DPI-funktion, Parental Control och AdGuard Home för olika behov hos teknikentusiaster och företagsanvändare.

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Brume 3 (GL-MT5000)
- 1 x nätadapter
- 1 x Ethernet-kabel
- 1 x användarhandbok
- 1 x tackkort
- 1 x adapter (beroende på leveransland)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/unboxing.png){class="glboxshadow"}

Titta på uppackningsvideon för Brume 3 nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfigurera Brume 3 {#how-to-set-up-brume-3}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till Brume 3 och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en kabelansluten enhet (t.ex. en stationär eller bärbar dator) till LAN-porten på Brume 3 med en Ethernet-kabel.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel.

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

Konfigurera Brume 3 med någon av de internetanslutningsmetoder som stöds: Ethernet, Tethering och Cellular (optional). Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Anslut WAN-porten på Brume 3 till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.

    När Brume 3 har anslutits till internet visas en grön punkt bredvid "Ethernet" på sidan INTERNET i Web Admin Panel, och den fysiska LED-lampan på Brume 3 lyser med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. Anslut den mobila enheten till USB Type-C-porten på Brume 3 med en USB 3.0-datakabel.
    2. Aktivera USB-internetdelning i inställningarna på den mobila enheten.
    3. Klicka på **Connect** i avsnittet "Tethering" på sidan INTERNET i webbadministrationspanelen.

    När Brume 3 har anslutits till internet visas en grön punkt bredvid "Tethering" på sidan INTERNET i Web Admin Panel, och den fysiska LED-lampan på Brume 3 lyser med fast vitt sken.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    En extra USB-C-till-USB-A-adapterkabel krävs för den här anslutningsmetoden.

    Anslut ett USB-modem för mobilnät till USB Type-C-porten på Brume 3 med en extra USB-C-till-USB-A-adapterkabel. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna klientenheter.

    När Brume 3 har anslutits till internet visas en grön punkt bredvid "Cellular" på sidan INTERNET i Web Admin Panel, och den fysiska LED-lampan på Brume 3 lyser med fast vitt sken.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Brume 3.

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNets molnhanteringstjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Brume 3 stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Brume 3 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 3 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet, internetdelning och mobilnät) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.

    Information om hur du konfigurerar LAN finns i [Lan](../../interface_guide/lan.md).

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

---

=== "Ethernet Port"

    På sidan Ethernet Port kan du konfigurera WAN- och LAN-portarna, ange Ethernet för WAN/LAN-gränssnittet, ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

    Information om hur du hanterar Ethernet-portar finns i [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

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

    Detaljerade anvisningar finns i [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics erbjuder en intelligent instrumentpanel för trafikinformation som kategoriserar och visualiserar nätverksanvändningen efter program. Den hjälper dig att övervaka trafik i realtid och historisk trafik för bättre insyn och kontroll över nätverket.

    Detaljerade anvisningar finns i [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter ger intelligent säkerhet online med DPI-baserad klassificering. Funktionen blockerar automatiskt skadliga webbplatser för att hålla nätverket rent och säkert.

    Detaljerade anvisningar finns i [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) optimerar bandbreddstilldelningen genom att prioritera viktiga aktiviteter (t.ex. videosamtal och spel) när nätverket är överbelastat. Det minskar latensen och förbättrar nätverkets övergripande prestanda. Observera att detta gäller lokal klienttrafik och tunneltrafik från VPN Client, men inte trafik som tas emot när routern fungerar som VPN Server.

    Detaljerade anvisningar finns i [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) hanterar routerns nätverkstrafik intelligent för att minimera latens och ”bufferbloat”, vilket ger smidigare spel och röstsamtal.

    Detaljerade anvisningar finns i [SQM](../../interface_guide/sqm.md).

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

    På sidan NAT Mode kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG (Application Layer Gateway).

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

    * [How to set up Tor](../../interface_guide/tor.md)

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

    Detaljerade konfigurationsanvisningar och mer information finns i [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    På sidan Admin Password kan du ange eller ändra lösenordet för routerns administratörsgränssnitt, så att endast behöriga användare kan ändra inställningarna.

    Av säkerhetsskäl rekommenderar vi att du aktiverar **Prevent Weak Password**.

    När **Prevent Weak Password** är aktiverat gäller följande krav för nya lösenord.

    * Minst 5 och högst 63 tecken.
    * Bokstäver (skiftlägeskänsliga), siffror och symbolerna `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` tillåts.
    * Minst två av följande teckentyper krävs: versaler, gemener, siffror och symboler.

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade konfigurationsanvisningar och mer information finns i [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade konfigurationsanvisningar och mer information finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade konfigurationsanvisningar och mer information finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade konfigurationsanvisningar och mer information finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade konfigurationsanvisningar och mer information finns i [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade konfigurationsanvisningar och mer information finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
