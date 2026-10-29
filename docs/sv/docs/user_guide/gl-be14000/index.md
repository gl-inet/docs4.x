# Användarhandbok för Flint 4 (GL-BE14000) {#flint-4-gl-be14000-user-guide}

## Produktöversikt {#product-overview}

Flint 4 (GL-BE14000) omdefinierar vad en hemrouter kan vara. Den har Wi-Fi 7 med tre band och MLO och levererar topphastigheter på 688 Mbps (2.4 GHz) + 4323 Mbps (5 GHz) + 8646 Mbps (6 GHz). För kabelanslutningar har den en fullständig multigigabit-infrastruktur med en 10G SFP+ WAN/LAN-port, en 10GE WAN/LAN-port, en 2.5GE WAN/LAN-port, tre 2.5GE LAN-portar och fyra 1GE LAN-portar. Den stöder högpresterande VPN och når en kapacitet på upp till 1.5 Gbps för både WireGuard® och OpenVPN DCO. Den inbyggda pekskärmen på 2.4 tum möjliggör övervakning av nätverksstatus i realtid och visar viktiga nätverksmätvärden direkt på enheten.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Flint 4 (GL-BE14000)
- 1 x nätadapter
- 1 x Ethernet-kabel
- 1 x användarhandbok
- 1 x tackkort
- 1 x adapter (beroende på leveransland)

Titta på uppackningsvideon för Flint 4 nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfigurera Flint 4 {#how-to-set-up-flint-4}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk på enheten och ange lösenordet för att ansluta. Standardnamnet (SSID) och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Ange administratörslösenordet och Wi-Fi-uppgifterna och klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

Konfigurera Flint 4 med någon av de internetanslutningsmetoder som stöds: Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering eller Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutning.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}

    Flint 4 har en 10G SFP+ WAN/LAN-port för fiberupplänkar, höghastighets-backhaul till switchar och högpresterande nätverksutbyggnad. Porten är inställd på WAN som standard och kan ändras till LAN vid behov.

    Nedan visas ett exempel på hur 10G SFP+-porten på Flint 4 ansluts till internetleverantörens fiberupplänk via en optisk transceiver och fiberkabel för internetåtkomst. Fler lösningar finns i [Anslut 10G SFP+-porten på Flint 4](../../faq/connecting_10g_sfp_plus_port_on_flint4.md).

    1. Sätt in en kompatibel 10G SFP+-transceiver i SFP+-porten på Flint 4 och anslut den sedan till internetleverantörens fiberupplänk.
    2. Flint 4 försöker automatiskt hämta nätverksparametrar (IP-adress, gateway och DNS) via DHCP. Om internetleverantören kräver PPPoE eller statisk IP-adressering ändrar du WAN-anslutningsinställningarna i webbadministrationspanelen.
    3. När internetanslutningen har upprättats blir avsnittet Ethernet på pekskärmens startsida blått (aktivt). Tryck på Ethernet på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}

    1. Anslut WAN-porten på Flint 4 till en uppströms enhet (t.ex. ett modem från internetleverantören, en nätverksswitch eller ett Ethernet-uttag i väggen) med en Ethernet-kabel.
    2. Flint 4 försöker automatiskt hämta nätverksparametrar (IP-adress, gateway och DNS) via DHCP. Om internetleverantören kräver PPPoE eller statisk IP-adressering ändrar du WAN-anslutningsinställningarna i webbadministrationspanelen.
    3. När internetanslutningen har upprättats blir avsnittet Ethernet på pekskärmens startsida blått (aktivt). Tryck på Ethernet på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Tryck på **Repeater** på pekskärmen. Enheten börjar söka efter tillgängliga Wi-Fi-nätverk.
    2. Välj det Wi-Fi-nätverk som du vill utöka med Flint 4.
    3. Ange lösenordet och tryck på **Apply**.
    4. När internetanslutningen har upprättats blir avsnittet Repeater på pekskärmens startsida blått (aktivt). Tryck på Repeater på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Anslut en mobil enhet (t.ex. en smartphone) till USB-porten på Flint 4 med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera **USB Tethering** eller **Personal Hotspot**. På iPhone trycker du på **Trust This Device** om du uppmanas att göra det.
    3. Välj **Tethering** på pekskärmen på Flint 4 och tryck på **Connect**. Routern ansluter sedan till enheten.
    4. När internetanslutningen har upprättats blir avsnittet Tethering på pekskärmens startsida blått (aktivt). Tryck på Tethering på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

    **Obs!** Om anslutningen misslyckas kontrollerar du att du använder en nätadapter på 12V/4A, eftersom otillräcklig effekt kan hindra USB-porten från att strömförsörja den anslutna enheten korrekt. Upprepa sedan stegen ovan eller logga in på webbadministrationspanelen för att kontrollera statusen för Tethering-anslutningen.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Anslut ett mobilmodem eller en USB-dongel till USB-porten på Flint 4. På så sätt kan internetanslutningen från ett USB-modem delas med alla anslutna enheter.
    2. När internetanslutningen har upprättats blir avsnittet Cellular på pekskärmens startsida blått (aktivt). Tryck på Cellular på pekskärmen eller logga in på webbadministrationspanelen för att kontrollera anslutningsinformationen.

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Flint 4.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera olika Wi-Fi-nätverk för Flint 4, däribland MLO Wi-Fi, Main Network, Guest Network och IoT Network.

Mer information finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Mer information finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Mer information finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksfunktion som är integrerad i GL.iNet-routrar. Den ger smidig fjärråtkomst till hemnätverket utan registrering eller inloggning. Genom att använda AmneziaWG-protokollet med inbyggd trafikobfuskering hålls anslutningen stabil och säker, vilket passar för tillförlitlig fjärråtkomst var du än befinner dig. Du kan konfigurera ett AstroWarp-nätverk direkt i GL.iNet-routerns administratörspanel. Parkoppla routrarna med en åtkomstkod för att ansluta reseroutern säkert till hemnätverket på några sekunder.

    Mer information finns i [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Flint 4 stöder protokollen OpenVPN och WireGuard.

=== "OpenVPN"

    Flint 4 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Mer information finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    På den här sidan kan du konfigurera och hantera **Main Network**, **Guest Network**, **IoT Network** och egna **VLAN Networks** centralt. Du kan skapa och hantera flera subnät för att isolera olika typer av enheter eller trafik.

    Mer information finns i [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du hantera Ethernet-portarnas roller (WAN/LAN) och VLAN-segmentering samt visa portinformation som MAC-adress och förhandlad hastighet.

    Mer information finns i [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Mer information finns i [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Mer information finns i [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Mer information finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Nätverksläge avser de olika driftroller och funktioner som en router kan använda för att uppfylla olika behov vid nätverksdistribution. Vanliga nätverkslägen är routerläge, extenderläge och åtkomstpunktsläge.

    Mer information finns i [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway är en flexibel funktion som utökar funktionerna hos en befintlig huvudrouter utan att den behöver bytas ut eller konfigureras om. Genom att ange en GL.iNet-router som Drop-in Gateway kan du lägga till avancerade funktioner i den befintliga nätverksinfrastrukturen, till exempel AdGuard Home, VPN och krypterad DNS.

    Använd länkarna nedan för att konfigurera en drop-in-gateway.

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Nätverksacceleration kan minska processorbelastningen och påskynda vidarebefordran av trafikpaket.

    Mer information finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

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

    Mer information finns i [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Security {#security}

=== "Port Forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Mer information finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

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

---

=== "AdGuard Home"

    AdGuard Home är en lösning som blockerar annonser och spårare i hela nätverket. Den fungerar som en DNS-server som filtrerar oönskat innehåll på alla enheter som är anslutna till hemnätverket.

    Mer information finns i [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Bark-tjänsten som är integrerad i Flint 4 kan skydda ditt barns digitala miljö och ge heltäckande skydd online. Den kräver vanligtvis en betalprenumeration. Genom vårt samarbete med Bark erbjuder GL.iNet dock abonnemanget Bark Home utan kostnad på utvalda routermodeller, däribland Flint 4. Det ger avancerad övervakning och varningar utan extra kostnad.

    Mer information finns i [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.

    Mer information finns i [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.

    Mer information finns i [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, en förkortning av The Onion Router, är ett integritetsfokuserat nätverk som möjliggör anonym kommunikation över internet. Internettrafiken dirigeras genom flera servrar (noder) som drivs av frivilliga för att dölja användarens plats och aktivitet. Det gör det svårt att spåra aktiviteter online.

    Mer information finns i [Tor](../../interface_guide/tor.md).

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
