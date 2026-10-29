# Användarhandbok för Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Produktöversikt {#product-overview}

Slate Plus (GL-A1300) är en reserouter i fickformat med en kraftfull processor som är optimerad för stabila nätverk och effektiv bearbetning av VPN-kryptering. Den innehåller våra senaste säkerhetsfunktioner och kör det senaste operativsystemet OpenWrt. Routern är utformad för dig som reser ofta och använder VPN-nätverk i stor omfattning.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

Observera att adaptern i förpackningen beror på leveranslandet.

Förpackningen innehåller:

- 1 x användarhandbok
- 1 x Slate Plus (GL-A1300)
- 1 x Ethernet-kabel
- 1 x tackkort
- 1 x garantikort
- 1 x nätadapter
- 1 x adapter (beroende på leveransland)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Konfigurera Slate Plus {#how-to-set-up-slate-plus}

Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Se [Första installationen](../../faq/first_time_setup.md) om du behöver mer vägledning.

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Öppna Settings -> WLAN på enheten, leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk och ange lösenordet. Standardnamnet och standardlösenordet för nätverket finns på etiketten på routerns undersida.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

När du bekräftar Wi-Fi-uppgifterna bör du tänka på att enheten måste anslutas till routerns Wi-Fi igen med de uppdaterade inloggningsuppgifterna om du ändrar Wi-Fi-informationen.

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel. Om du föredrar att använda GL.iNet-appen kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

Konfigurera Slate Plus med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

    Anslut routerns WAN-port till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.
    
    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.
    
    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera USB Tethering.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.
    
    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

    Anslut ett USB-modem för mobilnät till routerns USB-port. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Cellular på sidan INTERNET.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningar för Wi-Fi-nätverken på 5 GHz och 2.4 GHz, bland annat aktivering av Wi-Fi, sändareffekt, Wi-Fi-namn (SSID), säkerhetsläge och lösenord för Wi-Fi, SSID-synlighet, Wi-Fi-läge, bandbredd och kanal.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless_v4.8.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Slate Plus och andra GL.iNet-routrar stöder OpenVPN och WireGuard. Slate Plus stöder även Tor.

=== "OpenVPN"

    Slate Plus och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate Plus och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, en förkortning av The Onion Router, är ett integritetsfokuserat nätverk som möjliggör anonym kommunikation över internet. Internettrafiken dirigeras genom flera servrar (noder) som drivs av frivilliga för att dölja användarens plats och aktivitet. Det gör det svårt att spåra aktiviteter online.
    
    * [Konfigurera Tor](../../interface_guide/tor.md).

## Program {#applications}

=== "Plug-ins"

    Ett insticksprogram är en programvarukomponent som lägger till särskilda funktioner i ett befintligt datorprogram. På så sätt kan programmets funktioner anpassas och utökas.
    
    Information om hur du konfigurerar insticksprogram finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress.
    
    Information om hur du konfigurerar Dynamic DNS finns i [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    GL.iNets molnhanteringstjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.
    
    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    Nätverkslagring är en central lösning för datalagring där flera användare och enheter kan komma åt och dela filer via ett nätverk.
    
    Information om hur du konfigurerar nätverkslagring finns i [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home är en lösning som blockerar annonser och spårare i hela nätverket. Den fungerar som en DNS-server som filtrerar oönskat innehåll på alla enheter som är anslutna till hemnätverket.
    
    Information om hur du konfigurerar AdGuard Home finns i [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionen kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Information om hur du konfigurerar parental control finns i [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier är en programvarudefinierad nätverkslösning som låter dig skapa säkra virtuella nätverk över internet och ansluta enheter som om de fanns i samma lokala nätverk.
    
    Information om hur du konfigurerar ZeroTier finns i [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.
    
    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

## Network {#network}

=== "Firewall"

    Sidan Firewall innehåller viktiga säkerhetsförbättringar för nätverket. Den har funktioner som Port Forwarding, Open Ports och DMZ. Med dessa verktyg kan du hantera och anpassa nätverkets trafikflöde och förbättra säkerheten.

    * Port Forwarding: Omdirigera viss trafik från internet till angivna enheter i nätverket och ge åtkomst till tjänster som spelservrar och webbservrar.
    * Open Ports: Övervaka och styr vilka portar som är öppna på routern för att förhindra obehörig åtkomst och möjliga säkerhetshot.
    * DMZ (Demilitarized Zone): Exponera en enhet mot internet genom att vidarebefordra all inkommande trafik till den.

    Information om hur du konfigurerar brandväggsrelaterade inställningar finns i [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet, repeater och internetdelning) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.
    
    Information om hur du konfigurerar LAN finns i [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Du kan ange ett subnät inom de privata IPv4-adressintervallen 192.168.0.0/16, 172.16.0.0/12 eller 10.0.0.0/8, ange IP-adresserna för gateway och nätmask samt konfigurera säkerhetsinställningar som AP-isolering för gästnätverket.

    Information om hur du konfigurerar gästnätverket finns i [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.
    
    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.
    
    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "MAC Address"

    På sidan MAC Address kan du visa och hantera de Media Access Control-adresser (MAC-adresser) som är kopplade till routern. Sidan innehåller bland annat följande funktioner:

    * Factory Default: Visa standard-MAC-adresserna för routerns Ethernet- och Repeater-lägen som referens för de ursprungliga maskinvaruinställningarna.
    * Clone: Klona MAC-adressen för en viss klientenhet. Detta är särskilt användbart när nätverksåtkomsten är begränsad till vissa enheter.
    * Manual: Ange en anpassad MAC-adress för routern manuellt. Du kan även använda knappen Random för att generera en slumpmässig MAC-adress, vilket ger flexibilitet och förbättrad integritet.

    Med dessa funktioner kan du hantera routerns MAC-adresser effektivt och säkerställa kompatibilitet och flexibilitet i olika nätverksmiljöer.

    Information om hur du hanterar MAC-adresser finns i [MAC Address](../../interface_guide/mac_address.md).

---

=== "Drop-in Gateway"

    En drop-in-gateway utökar huvudrouterns funktioner med bland annat AdGuard Home, krypterad DNS och VPN-klient.
    
    Använd följande länkar för att konfigurera en drop-in-gateway:
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.
    
    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

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
    * Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-banden 5GHz/2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.
    
    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    På sidan Toggle Button Settings kan du konfigurera routerns fysiska växlingsknapp och tilldela den särskilda funktioner för snabb åtkomst och styrning. Funktionen ger praktiska genvägar till vanliga uppgifter och inställningar och förenklar routerhanteringen.

    Detaljerade anvisningar finns i [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.
    
    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade anvisningar finns i [Log](../../interface_guide/log.md).

---

=== "Security"

    **Obs**: Funktionen är tillgänglig från och med v4.5.

    På sidan Security kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller alternativ för:

    * Admin Password: Ange eller ändra lösenordet för routerns administratörsgränssnitt så att endast behöriga användare kan ändra inställningarna.
    * Local Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.

    Dessa inställningar hjälper dig att upprätthålla en säker nätverksmiljö som skyddar både routern och anslutna enheter.
    
    Detaljerade anvisningar finns i [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade anvisningar finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
