# Användarhandbok för Brume 2 (GL-MT2500/GL-MT2500A) {#brume-2-gl-mt2500gl-mt2500a-user-guide}

## Produktöversikt {#product-overview}

Brume 2 (GL-MT2500/GL-MT2500A) är en lätt och kraftfull VPN-gateway som kör operativsystemet OpenWrt v21.02. Den kompakta utformningen passar för en VPN-server i hemmet eller SD-WAN (Site-to-Site) för små och medelstora företag. Den finns i två varianter: GL-MT2500 med plasthölje och GL-MT2500A med aluminiumhölje.

![gl-mt2500 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/hardware_info/mt2500_interface.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Brume 2 (GL-MT2500/GL-MT2500A)
- 1 x användarhandbok
- 1 x Ethernet-kabel
- 1 x tackkort
- 1 x garantikort
- 1 x nätadapter
- 1 x adapter (beroende på leveransland)

Följande bild visar GL-MT2500A som exempel.

![gl-mt2500 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/first_time_setup/mt2500a_unboxing.jpg){class="glboxshadow"}

## Konfigurera Brume 2 {#how-to-set-up-brume-2}

Konfigurera Brume 2 med någon av de internetanslutningsmetoder som stöds: Ethernet, Tethering eller Cellular. Repeater stöds inte eftersom Brume 2 saknar Wi-Fi-modul. Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rpi_loOwUQM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut enheten (t.ex. en stationär eller bärbar dator) till routerns LAN-port med en Ethernet-kabel.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_ethernet.png){class="glboxshadow"}

    Anslut routerns WAN-port till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_tethering.png){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera USB Tethering.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt2500/internet/mt2500_cellular.png){class="glboxshadow"}

    Anslut ett USB-modem för mobilnät till routerns USB-port. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Cellular på sidan INTERNET.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

**Obs!** Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningsmetod.

## Konfigurera ett VPN {#how-to-set-up-a-vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Brume 2 och andra GL.iNet-routrar stöder OpenVPN och WireGuard. Brume 2 stöder även Tor.

=== "OpenVPN"

    Brume 2 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 2 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, en förkortning av The Onion Router, är ett integritetsfokuserat nätverk som möjliggör anonym kommunikation över internet. Internettrafiken dirigeras genom flera servrar (noder) som drivs av frivilliga för att dölja användarens plats och aktivitet. Det gör det svårt att spåra aktiviteter online.

    * [Konfigurera Tor](../../interface_guide/tor.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas enhetsnamn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även reservera en IP-adress, blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNets tjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

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

    Föräldrakontroll är en grupp inställningar som hjälper dig att hantera och styra dina barns enheter. De kan bland annat begränsa skärmtiden och åtkomsten till visst innehåll.

    Information om hur du konfigurerar föräldrakontroll finns i [Parental controls](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.

    Information om hur du konfigurerar ZeroTier finns i [ZeroTier](../../interface_guide/zerotier.md).

---

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.

    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

## Nätverksinställningar {#network-settings}

=== "Port forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk. Information om hur du konfigurerar portvidarebefordran finns i [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet, internetdelning och mobilnät) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.

    Information om hur du konfigurerar LAN finns i [Lan Tutorial](../../interface_guide/lan.md).

---


=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker och åsidosätta DNS-inställningarna för alla klienter. Du kan även tillåta att anpassad DNS åsidosätter VPN DNS samt ställa in DNS-serverläget på automatiskt eller manuellt ange DNS-servrar från Ethernet-anslutningen.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Network Port Management"

    På sidan Network Port Management kan du konfigurera WAN- och LAN-portarna, ange Ethernet för WAN/LAN-gränssnittet, ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

---

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN.

    Information om hur du konfigurerar en drop-in-gateway finns i [Konfigurera en drop-in-gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    Maskinvaruacceleration innebär att specialiserade maskinvarukomponenter utför vissa uppgifter effektivare än generella processorer.

    Information om hur du konfigurerar nätverksacceleration finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    På sidan NAT Settings kan du aktivera eller inaktivera funktionerna Full Cone NAT och SIP ALG (Application Layer Gateway).

    Information om hur du konfigurerar NAT-inställningar finns i [NAT Settings](../../interface_guide/nat_settings.md).

## Systeminställningar {#system-settings}

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

    På sidan Scheduled Tasks kan du automatisera routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md).

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

---

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade anvisningar finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
