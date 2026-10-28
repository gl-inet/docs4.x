# Användarhandbok för Spitz Plus (GL-X2000) {#spitz-plus-gl-x2000-user-guide}

## Produktöversikt {#product-overview}

Spitz Plus (GL-X2000) är en 4G LTE Wi-Fi 6-mobilnätsgateway med dubbla SIM-kort, utformad för snabba och tillförlitliga anslutningar, särskilt i avlägsna områden och under bilresor. Med aggregering av tre bärvågor (3CA) kan routern ge upp till tre gånger den teoretiska kanalbandbredden hos en Cat 4-anslutning med en enda bärvåg, beroende på de aggregerade bärvågornas bandbredder och stöd för LTE 3CA hos din operatör och lokala basstationer. Den erbjuder fyra internetanslutningsmetoder: Cellular (SIM-kort), Ethernet, repeater och internetdelning. Den stöder Multi-WAN (failover och lastbalansering), VPN (OpenVPN och WireGuard), föräldrakontroll, AdGuard Home, portvidarebefordran, Tailscale med mera.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Spitz Plus (GL-X2000)
- 1 x användarhandbok
- 4 x externa antenner
- 1 x tackkort
- 1 x RJ45 Ethernet-kabel
- 1 x väggmonteringssats
- 1 x självhäftande dyna
- 1 x nätadapter
- 1 x adapter (beroende på leveransland)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_package.png){class="glboxshadow"}

## LED-indikatorer {#led-indicators}

Nedan beskrivs LED-lägena för olika händelser. Alla lägen för varje LED finns i [LED-indikatorstatus för GL-X2000](../../faq/led.md#gl-x2000){target="_blank"}.

| Device status                         | Power                     | Internet            | 2.4GHz | 5GHz  | Cellular |
| ------------------------------------- | ------------------------- | ------------------- | ------ | ----- | -------- |
| Internet connected                    | Green                     | Green               | Green  | Green | Green    |
| No internet                           | Green                     | Off                 | Green  | Green | Green    |
| Firmware updating                     | Green                     | Blinking every 0.5s | Blinking every 0.5s | Blinking every 0.5s | Green    |
| Network reset (press "reset" for 5s)  | Blinking every 1s         | Green               | Green  | Green | Green    |
| Factory reset (press "reset" for 10s) | Fast blinking every 0.25s | Green               | Green  | Green | Green    |

## Konfigurera Spitz Plus {#how-to-set-up-spitz-plus}

Konfigurera Spitz Plus med någon av de fyra internetanslutningsmetoder som stöds: Cellular (SIM krävs), Ethernet, Repeater eller Tethering. Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Videon visar Cellular-konfigurationen av Spitz Plus. Följ stegen nedan om du vill konfigurera Spitz Plus med andra internetanslutningsmetoder.)</small>

!!! note "Innan du börjar följer du dessa steg (vid anslutning via mobilnät):"

    Minst ett nano-SIM-kort krävs för att ansluta till internet via mobilnätet. Följ dessa steg när nano-SIM-korten är klara:

    1. Aktivera SIM-kortet eller SIM-korten om mobiloperatören kräver det.
    2. Stäng av routern.
    3. Sätt in SIM-korten i SIM-kortplatserna. (**Obs!** Endast ett SIM-kort är aktivt åt gången. Det andra fungerar endast som reserv.)

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Öppna Settings -> WLAN på enheten, leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk och ange lösenordet. Standardnamnet och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare och ange `192.168.8.1` i adressfältet för att öppna GL.iNet Web Admin Panel. Välj språk, ange administratörslösenordet och klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel. Om du föredrar att använda GL.iNet-appen kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

Konfigurera Spitz Plus med någon av de internetanslutningsmetoder som stöds: Cellular, Ethernet, Repeater och Tethering. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Om SIM-kortet sitter i routern bör internetanslutningen upprättas automatiskt. Namnet på mobiloperatören och en grön punkt ska visas i avsnittet Cellular.

    Om anslutningen inte fungerar stänger du av routern, sätter in SIM-kortet igen och slår på routern.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md#setup-for-dual-sim-models).

    **Obs!** eSIM-funktionen på Spitz Plus är tillgänglig i firmware v4.7 och senare. Läs [här](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md) om hur du använder det fysiska eSIM-kortet på en GL.iNet-router.

    Om du stöter på problem kan du läsa [felsökningsguiden för mobilnät](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}

    Anslut WAN-porten på Spitz Plus till en uppströms enhet (t.ex. ett modem) med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i administratörspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera USB Tethering.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Spitz Plus.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningarna för Wi-Fi-nätverk på både 5 GHz och 2.4 GHz. Du kan bland annat aktivera eller inaktivera Wi-Fi, ange sändningseffekt, Wi-Fi-namn (SSID) och Wi-Fi-lösenord, aktivera eller inaktivera slumpmässig BSSID, välja Wi-Fi-säkerhetsläge, konfigurera SSID-synlighet samt välja Wi-Fi-läge, bandbredd och kanal.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas enhetsnamn, anslutningstyp (Ethernet eller Wi-Fi), IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även reservera en IP-adress, blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

    Information om hur du konfigurerar AstroWarp finns i [AstroWarp](../../interface_guide/astrowarp.md).

    **Obs!** Uppgradera Spitz Plus till firmware v4.8 eller senare för att använda AstroWarp.

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Spitz Plus stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Spitz Plus och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz Plus och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

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

    AdGuard Home är ett verktyg från tredje part som blockerar annonser och spårning för att skydda dig. Information om hur du aktiverar funktionen finns i [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Föräldrakontroll är en grupp inställningar som hjälper dig att hantera och styra dina barns enheter. De kan bland annat begränsa skärmtiden och åtkomsten till visst innehåll.

    Information om hur du konfigurerar parental control finns i [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Spitz Plus stöder Tailscale i firmware v4.7 och senare.

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.

    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM"

    Spitz Plus stöder eSIM-funktioner i firmware v4.7 och senare.

    Information om hur du konfigurerar och hanterar eSIM på enheten finns i [den här guiden](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Network {#network}

=== "Port forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk. Information om konfiguration finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, eller Local Area Network, är ett nätverk som ansluter datorer och enheter inom ett begränsat geografiskt område, till exempel ett hem eller ett kontor. Det möjliggör snabb dataöverföring och resursdelning, så att enheterna kan kommunicera effektivt med varandra.

    Information om hur du konfigurerar LAN finns i [Lan Tutorial](../../interface_guide/lan.md).

---

=== "Guest Network"

    Du kan ange ett subnät inom de privata IPv4-adressintervallen 192.168.0.0/16, 172.16.0.0/12 eller 10.0.0.0/8, ange IP-adresserna för gateway och nätmask samt konfigurera säkerhetsinställningar som AP-isolering för gästnätverket.

    Information om hur du konfigurerar gästnätverket finns i [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Port Management"

    På sidan Port Management kan du konfigurera WAN- och LAN-portarna, ange Ethernet för WAN/LAN-gränssnittet, ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

    Information om hur du hanterar Ethernet ports finns i [Port Management](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Nätverksläge avser de konfigurationsinställningar som avgör hur en enhet ansluter till ett nätverk och kommunicerar med andra enheter.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN. Information om hur du konfigurerar Drop-in Gateway finns i [Konfigurera Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

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

    Detaljerade konfigurationsanvisningar finns i [Overview](../../interface_guide/system_overview.md){target="_blank"}.

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder fyra uppgraderingsalternativ:

    * Firmware Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Firmware Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.
    * Module Online Upgrade: Sök automatiskt efter den senaste versionen av 4G/5G-modulen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Module Local Upgrade: Ladda upp en modulfil manuellt från datorn för att uppdatera 4G/5G-modulen.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade anvisningar finns i [Upgrade](../../interface_guide/upgrade.md){target="_blank"}.

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-banden 5GHz/2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade anvisningar finns i [Log](../../interface_guide/log.md){target="_blank"}.

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

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}.

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade konfigurationsanvisningar och mer information finns i [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.
