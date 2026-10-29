# Användarhandbok för Mango (GL-MT300N-V2) {#mango-gl-mt300n-v2-user-guide}

## Produktöversikt {#product-overview}

Mango (GL-MT300N-V2) är en kompakt minirouter i fickformat som är bärbar och enkel att ta med på resor. Den stöder trådlösa överföringshastigheter på upp till 300Mbps. Mango erbjuder avancerade säkerhetsfunktioner med stöd för OpenVPN, WireGuard® och en DNS-server. Du kan både omvandla ett offentligt nätverk till ett privat Wi-Fi-nätverk för säker surfning och ladda upp VPN-konfigurationsfiler från över 30 VPN-tjänsteleverantörer. Routern kan användas som VPN-klient och skapar krypterad trafik mellan din enhet och VPN-servern för ytterligare integritet och säkerhet.

![mt300n-v2 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## Konfigurera Mango {#how-to-set-up-mango}

Konfigurera Mango med någon av de fyra internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering eller Cellular. Följ stegen nedan.

### 1. Slå på {#1-power-on}

Anslut Micro USB-strömkabeln till routerns strömport. Anslut den andra änden till en 5V/2A-nätadapter (medföljer inte) och anslut adaptern till ett eluttag.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Öppna Settings -> WLAN på enheten, leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk och ange lösenordet. Standardnamnet och standardlösenordet för nätverket finns på etiketten på routerns undersida.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

Observera att enheten måste anslutas till routerns Wi-Fi igen med de uppdaterade inloggningsuppgifterna om du ändrar Wi-Fi-informationen.

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel. Om du föredrar att använda GL.iNet-appen kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

Konfigurera Mango med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/ethernet.png){class="glboxshadow"}

    Anslut routerns WAN-port till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/repeater.png){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/tethering.png){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera USB Tethering.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/usb_modem.png){class="glboxshadow"}

    Metoden är användbar för att dela internetanslutningen från ett USB-modem med alla anslutna enheter.

    1. Sätt in ett USB-modem för mobilnät i routerns USB-port.
    2. Leta reda på avsnittet Cellular på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    3. När internetanslutningen har upprättats visas en grön punkt i avsnittet Cellular på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett USB-modem](../../interface_guide/internet_cellular.md).

---

## Wireless {#wireless}

På sidan Wireless kan du konfigurera inställningar för Wi-Fi-nätverken på 2.4 GHz, bland annat aktivering av Wi-Fi, sändareffekt, Wi-Fi-namn (SSID), säkerhetsläge och lösenord för Wi-Fi, SSID-synlighet, Wi-Fi-läge, bandbredd och kanal.

Mer information finns i [Wireless](../../interface_guide/wireless_v4.8.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Mango och andra GL.iNet-routrar stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Mango och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Program {#applications}

=== "Plug-ins"

    Insticksprogram är tilläggsfunktioner som utökar routerns funktionalitet.

    Information om hur du konfigurerar insticksprogram finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress.

    Information om hur du konfigurerar Dynamic DNS finns i [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    GL.iNets molnhanteringstjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

## Network {#network}

=== "Firewall"

    Sidan Firewall innehåller viktiga säkerhetsförbättringar för nätverket. Den har funktioner som Port Forwarding, Open Ports och DMZ. Med dessa verktyg kan du hantera och anpassa nätverkets trafikflöde och förbättra säkerheten.

    * Port Forwarding: Omdirigera viss trafik från internet till angivna enheter i nätverket och ge åtkomst till tjänster som spelservrar och webbservrar.
    * Open Ports: Övervaka och styr vilka portar som är öppna på routern för att förhindra obehörig åtkomst och möjliga säkerhetshot.
    * DMZ (Demilitarized Zone): Exponera en enhet mot internet genom att vidarebefordra all inkommande trafik till den.

    Information om hur du konfigurerar brandväggsrelaterade inställningar finns i [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    På sidan LAN kan du hantera och konfigurera inställningarna för routerns lokala nätverk. Sidan innehåller bland annat följande funktioner:

    * Router IP Address: Ändra routerns IP-adress så att den passar nätverkskonfigurationen bättre.
    * Netmask: Ange nätmasken för nätverket. Den bestämmer nätverkets storlek och intervall av IP-adresser.
    * DHCP: Aktivera eller konfigurera Dynamic Host Configuration Protocol, som automatiskt tilldelar IP-adresser till enheter i nätverket.
    * Address Reservation: Reservera särskilda IP-adresser för vissa enheter så att de alltid får samma IP-adress från DHCP-servern.

    Information om hur du konfigurerar LAN finns i [Lan](../../interface_guide/lan.md).

---

=== "DNS"

    Sidan DNS innehåller alternativ för att anpassa routerns Domain Name System-inställningar och förbättra både säkerhet och prestanda. Sidan innehåller bland annat följande funktioner:

    * Encrypted DNS: Konfigurera krypterad DNS för att skydda webbläsardata mot övervakning och manipulering och på så sätt säkerställa integritet och säkerhet.
    * Manual DNS: Ange valfria DNS-servrar manuellt för anpassad kontroll över DNS-frågor och eventuellt snabbare uppslagning.
    * DNS Proxy: Aktivera DNS-proxy för att dirigera DNS-förfrågningar från enheterna via en angiven DNS-server och få ytterligare kontroll över DNS-trafiken.

    Med dessa inställningar kan du optimera nätverkets DNS-prestanda och säkerhet efter dina behov.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    På sidan Network Mode kan du konfigurera routern för olika driftlägen och på så sätt uppfylla olika nätverksbehov. Följande lägen är tillgängliga:

    * Router: Fungerar som en standardrouter, hanterar trafik mellan det lokala nätverket och internet och tillhandahåller funktioner som NAT, brandvägg och DHCP.
    * Access Point: Fungerar som en åtkomstpunkt och utökar det befintliga kabelanslutna nätverket med trådlös anslutning utan att dirigera trafik.
    * Extender: Fungerar som räckviddsförlängare och förstärker signalen från det befintliga trådlösa nätverket för att täcka ett större område och eliminera döda zoner.
    * WDS (Wireless Distribution System): Liknar Extender. Välj WDS om huvudroutern stöder WDS-läge.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    På sidan IPv6 kan du konfigurera IPv6-inställningar för nätverket och få stöd för det senaste internetprotokollet. Du kan aktivera IPv6 och välja mellan fyra lägen efter nätverkets behov:

    * Native: Hämta en IPv6-adress direkt från internetleverantören för enkel och effektiv inbyggd IPv6-anslutning.
    * Passthrough: Låt IPv6-trafik passera genom routern till enheterna i nätverket. Anslutningen bryggas utan att routern själv hanterar IPv6-routningen.
    * NAT6: Använd Network Address Translation för IPv6 (NAT6) för att översätta mellan interna och externa IPv6-adresser på ett sätt som liknar NAT för IPv4.
    * Static IPv6: Konfigurera en statisk IPv6-adress för routern manuellt. En fast adress ger en konsekvent anslutning och enklare hantering av nätverkstjänster.

    Dessa lägen ger flexibla konfigurationsalternativ för IPv6 som passar olika nätverksmiljöer.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    På sidan MAC Address kan du visa och hantera MAC-adresserna som är kopplade till routern. Sidan innehåller bland annat följande funktioner:

    * Factory Default: Visa standard-MAC-adresserna för routerns Ethernet- och Repeater-lägen som referens för de ursprungliga maskinvaruinställningarna.
    * Clone: Klona MAC-adressen för en viss klientenhet. Detta är särskilt användbart när nätverksåtkomsten är begränsad till vissa enheter.
    * Manual: Ange en anpassad MAC-adress för routern manuellt. Du kan även använda knappen Random för att generera en slumpmässig MAC-adress, vilket ger flexibilitet och förbättrad integritet.

    Med dessa funktioner kan du hantera routerns MAC-adresser effektivt och säkerställa kompatibilitet och flexibilitet i olika nätverksmiljöer.

    Information om hur du hanterar MAC-adresser finns i [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN.

    Information om hur du konfigurerar Drop-in Gateway finns i [Konfigurera Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    På sidan IGMP Snooping kan du konfigurera inställningar som optimerar hanteringen av multicast-trafik i nätverket. IGMP Snooping lyssnar på och hämtar information från IGMP-protokollpaket och upprättar och underhåller vidarebefordringstabeller för multicast på lager 2. Det säkerställer att multicast-gruppdata endast vidarebefordras till värdar som har anslutit till multicast-gruppen och förhindrar att oönskad multicast-trafik når andra värdar.

    Inställningarna optimerar nätverkets prestanda och effektivitet, särskilt i miljöer med omfattande multicast-trafik, till exempel videoströmning och onlinespel.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## System {#system}

=== "Overview"

    Sidan Overview ger en heltäckande översikt över routerns aktuella status och prestandamätvärden. På sidan kan du visa:

    * CPU Average Load: Övervaka den genomsnittliga belastningen på routerns processor för att bedöma prestandan och identifiera möjliga flaskhalsar.
    * Memory Usage: Kontrollera hur mycket av routerns minne som används för att underlätta resurshanteringen.
    * Flash Usage: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.
    * System Info: Visa detaljerad information om routersystemet, däribland firmwareversion, drifttid och nätverksstatus.

    Dessa funktioner ger viktig information och viktiga kontroller som hjälper dig att effektivt hantera och övervaka routern.

    Detaljerade anvisningar finns i [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade anvisningar finns i [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * 2.4GHz Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-bandet 2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    På sidan Admin Password kan du ange eller ändra lösenordet för routerns administratörsgränssnitt, så att endast behöriga användare kan öppna och ändra routerns inställningar. Lösenordet är avgörande för nätverkets säkerhet och integritet och skyddar mot obehörig åtkomst och konfigurationsändringar.

    Detaljerade anvisningar finns i [Admin Password](../../interface_guide/admin_password.md).

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

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade anvisningar finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade anvisningar finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
