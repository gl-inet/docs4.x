# Användarhandbok för Mango 2 (GL-MG1300) {#mango-2-gl-mg1300-user-guide}

## Produktöversikt {#product-overview}

Mango 2 (GL-MG1300) är GL.iNets första Wi‑Fi 5-minireserouter med dubbla band och en mycket tunn, bärbar design. Den levererar teoretiska hastigheter på 400 Mbps (2.4 GHz) och 866 Mbps (5 GHz) med en 2×2 MIMO-konfiguration. OpenVPN och WireGuard är förinstallerade. Routern stöder över 30 VPN-tjänster som krypterar nätverkstrafiken när VPN-klienten är aktiverad och möjliggör fjärrhantering via GoodCloud, vilket ger en god balans mellan prestanda, praktisk användning och säkerhet.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Mango 2 (GL-MG1300)
- 1 x användarhandbok
- 1 x USB-C-till-USB-C-strömkabel
- 1 x tackkort

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/unboxing.png){class="glboxshadow"}

Titta på uppackningsvideon för Mango 2 nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xwHgLdWPwPc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Konfigurera Mango 2 {#how-to-set-up-mango-2}

Konfigurera Mango 2 med någon av de fyra internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering eller Cellular. Följ stegen nedan.

### 1. Slå på {#1-power-on}

Anslut USB Type-C-strömkabeln till routerns strömport. Anslut den andra änden till en 5V/2A-nätadapter (medföljer inte) och anslut adaptern till ett eluttag.

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

Konfigurera Mango 2 med någon av de internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering och Cellular. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du fler än en internetanslutningar.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Anslut WAN-porten på Mango 2 till en uppströms enhet (t.ex. ett modem) med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange lösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Anslut den mobila enheten (t.ex. en smartphone eller USB-dongel) till routerns USB-port med en USB-kabel.
    2. Öppna Settings på den mobila enheten och aktivera **USB Tethering** eller **Personal Hotspot**. På iPhone trycker du på **Trust This Device** om du uppmanas att göra det.
    3. Klicka på **Connect** i avsnittet Tethering på sidan INTERNET i webbadministrationspanelen.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Tethering på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

     ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Till Mango 2 kan du ansluta ett USB-C-modem direkt eller använda en USB-C-till-USB-A-adapter för att ansluta ett USB-A-modem.

    Anslut ett USB-modem för mobilnät till USB-porten på Mango 2. På så sätt kan internetanslutningen från USB-modemet delas med alla anslutna enheter.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Cellular på sidan INTERNET.

    Detaljerade anvisningar finns i [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

---

Nedan finns en översikt över funktionerna i webbadministrationspanelen för Mango 2.

## Wireless {#wireless}

På sidan Wireless kan du konfigurera olika Wi-Fi-nätverk, däribland Main Network, Guest Network och IoT Network. För varje nätverkstyp kan banden 5 GHz och 2.4 GHz konfigureras oberoende. Du kan även aktivera och konfigurera grundläggande inställningar för varje band, till exempel Wi-Fi SSID, säkerhetsläge, lösenord och slumpmässig BSSID.

Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

På sidan Clients visas information om anslutna enheter. För varje klient visas namn, IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GL.iNet Account"

    Med GL.iNet Account kan du ansluta och hantera enheter och molntjänster. Du får smidig åtkomst till både GoodCloud och glinet App för en säkrare och bättre upplevelse. Det gör det enklare att hantera nätverket när och var som helst.

    Information om hur du konfigurerar GL.iNet Account finns i [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

=== "GoodPAS"

    GoodPAS är en avancerad nätverksfunktion för smidig fjärråtkomst och enhetshantering. GoodPAS är särskilt utvecklat för integrering med GL.iNet-routrar och använder AmneziaWG-protokollet med inbyggd trafikobfuskering för säkra och stabila anslutningar. Med GoodPAS kan du fjärransluta till hemnätverket. När hemroutern fungerar som GoodPAS-utgångsnod använder internettrafik som skickas via GoodPAS routerns offentliga WAN-IP-adress.

    Information om hur du konfigurerar GoodPAS finns i [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Mango 2 stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Mango 2 och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2 och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

## Network {#network}

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).


=== "Subnet"

    Subnet samlar hanteringen av LAN, Guest Network, IoT Network och anpassade VLAN Networks. Där kan du skapa och hantera flera subnät för att isolera olika typer av enheter eller trafik.

    Information om hur du konfigurerar subnet finns i [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    På sidan Ethernet Port kan du konfigurera WAN- och LAN-portarna, ange Ethernet för WAN/LAN-gränssnittet, ange MAC-läge och MAC-adress för WAN-gränssnittet samt visa nätverksportens förhandlade hastighet.

    Information om hur du konfigurerar ethernet Port finns i [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).
---

=== "DNS"

    På sidan DNS kan du ange anpassade DNS-servrar, aktivera skydd mot DNS-rebinding-attacker, åsidosätta DNS-inställningarna för alla klienter och tillåta att anpassad DNS åsidosätter VPN-DNS. Du kan använda DNS-servrar som hämtas automatiskt från uppströmsenheter eller ange anpassade DNS-servrar manuellt.

    Information om hur du konfigurerar DNS finns i [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, eller Internet Protocol version 6, är den senaste versionen av internetprotokollet och är avsett att ersätta IPv4. Det erbjuder ett mycket större adressutrymme med ett praktiskt taget obegränsat antal unika IP-adresser, vilket är viktigt för att hantera det växande antalet enheter som är anslutna till internet.

    Information om hur du konfigurerar IPV6 finns i [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping är en teknik för nätverksoptimering som används i Ethernet-switchar för att hantera och styra multicast-trafik.

    Information om hur du konfigurerar IGMP snooping finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    På sidan Network Mode kan du konfigurera routerns driftroll för olika nätverksbehov. Du kan välja mellan lägen för allt från Wi-Fi-täckning i hemmet till multilänknätverk på företagsnivå. Varje läge aktiverar eller inaktiverar särskilda routerfunktioner för att optimera prestandan.

    Information om hur du konfigurerar nätverksläget finns i [Network Mode](../../interface_guide/network_mode.md).

=== "Network Acceleration"

    Nätverksacceleration kan minska processorbelastningen och påskynda vidarebefordran av trafikpaket.

    Information om hur du konfigurerar nätverksacceleration finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control {#flow-control}

=== "Parental Control"

    Parental Control hjälper dig att hantera och styra dina barns enheter. Funktionen kan bland annat begränsa deras skärmtid och åtkomst till visst innehåll.

    Information om hur du konfigurerar parental control finns i [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Security {#security}

=== "Port Forwarding"

    Portvidarebefordran gör det möjligt för fjärrservrar och enheter på internet att få åtkomst till enheter i ett privat nätverk.

    Information om hur du konfigurerar port forwarding finns i [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Med Admin Access kan du konfigurera olika säkerhetsinställningar som skyddar nätverket och routern mot obehörig åtkomst.

    Information om hur du konfigurerar admin access finns i [Admin Access](../../interface_guide/admin_access.md).

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

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger dig åtkomst till dina enheter och program oavsett var du befinner dig.

    Information om hur du konfigurerar Tailscale finns i [Tailscale](../../interface_guide/tailscale.md).

## System {#system}

=== "Overview"

    Sidan Overview ger en heltäckande översikt över routerns aktuella status och prestandamätvärden. På sidan kan du visa:

    * CPU Average Load: Övervaka den genomsnittliga belastningen på routerns processor för att bedöma prestandan och identifiera möjliga flaskhalsar.
    * Memory Usage: Kontrollera hur mycket av routerns minne som används för att underlätta resurshanteringen.
    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.
    * Flash: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
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

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * Wi-Fi Status Schedule: Ange ett schema som styr banden 5GHz/2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade anvisningar finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade anvisningar finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    På sidan Toggle Button Settings kan du konfigurera routerns fysiska växlingsknapp och tilldela den särskilda funktioner för snabb åtkomst och styrning. Funktionen ger praktiska genvägar till vanliga uppgifter och inställningar och förenklar routerhanteringen.

    Detaljerade anvisningar finns i [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

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
