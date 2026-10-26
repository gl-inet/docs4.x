# Användarhandbok för Marble (GL-B3000) {#marble-gl-b3000-user-guide}

## Produktöversikt {#product-overview}

Routern Marble (GL-B3000) är ett konstverk i sig, utformad som en fotoram för ditt favoritmotiv och för att lyfta bostaden. Marble (GL-B3000) är både visuellt tilltalande och högpresterande med Wi-Fi 6 och VPN-stöd.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

- 1 x Marble (GL-B3000)
- 1 x användarhandbok
- 1 x tackkort
- 1 x Ethernet-kabel
- 1 x väggmonteringssats
- 1 x självhäftande dyna
- 1 x routerstativ
- 1 x fotoram (tillval)
- 1 x nätadapter
- 1 x adapter (beroende på leveransland)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Konfigurera Marble {#how-to-set-up-marble}

Titta på installations- och konfigurationsvideorna eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Slå på {#1-power-on}

Sätt ihop nätadapterns två delar. Anslut den till routern och till ett eluttag. Routern startar automatiskt.

### 2. Anslut en enhet {#2-connect-device}

Anslut en enhet (t.ex. en stationär eller bärbar dator eller en smartphone) till routern via Wi-Fi eller Ethernet-kabel.

- Ethernet

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

- Wi-Fi

    Öppna Settings -> WLAN på enheten, leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk och ange lösenordet. Standardnamnet och standardlösenordet för nätverket finns på routerns etikett.

### 3. Logga in på webbadministrationspanelen {#3-log-in-to-web-admin-panel}

Öppna en webbläsare, ange `192.168.8.1` i adressfältet och logga in. Välj språk och ange administratörslösenordet. Klicka sedan på **Apply**.

### 4. Konfigurera internet {#4-internet-setup}

**Obs!** Följande anvisningar gäller när du konfigurerar routern via GL.iNet Web Admin Panel. Om du föredrar att använda GL.iNet-appen kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

Konfigurera Marble med någon av de internetanslutningsmetoder som stöds: Ethernet och Repeater. Om du vill använda funktionen [Multi-WAN](../../interface_guide/multi-wan.md) konfigurerar du två internetanslutningar.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}

    Anslut routerns WAN-port till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Ethernet på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Leta reda på avsnittet Repeater på sidan INTERNET i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk bland de tillgängliga nätverken.
    3. Ange nätverkslösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt i avsnittet Repeater på sidan INTERNET.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

---

## Konfigurera ett VPN {#how-to-set-up-a-vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Marble och andra GL.iNet-routrar stöder OpenVPN och WireGuard. Marble stöder även Tor.

=== "OpenVPN"

    Marble och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ guiderna nedan för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ guiderna nedan för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor är en integritetsfokuserad tjänst för anonym internetåtkomst. Följ dessa guider för att konfigurera Tor:

    * [How to set up Tor](../../interface_guide/tor.md)

---

## Trådlöst nätverk och klienter {#wireless-and-clients}

=== "Wireless"

    På sidan Wireless kan du konfigurera inställningarna för Wi-Fi-nätverk på både 5 GHz och 2.4 GHz. Du kan bland annat aktivera eller inaktivera Wi-Fi, ange sändningseffekt, Wi-Fi-namn (SSID) och Wi-Fi-lösenord, aktivera eller inaktivera slumpmässig BSSID, välja Wi-Fi-säkerhetsläge, konfigurera SSID-synlighet samt välja Wi-Fi-läge, bandbredd och kanal.

    Information om hur du konfigurerar Wireless finns i [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    På sidan Clients visas information om anslutna enheter. För varje klient visas enhetsnamn, anslutningstyp (Ethernet eller Wi-Fi), IP- och MAC-adresser, nedladdnings- och uppladdningshastighet samt total trafik. Du kan även blockera klienten eller utföra andra åtgärder.

    Information om hur du konfigurerar Clients finns i [Clients](../../interface_guide/clients.md).

## Molntjänster {#cloud-services}

=== "GoodCloud"

    GL.iNets tjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar.

    Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Funktionen är tillgänglig från firmware v4.7.

    AstroWarp är en avancerad nätverksplattform för smidiga fjärrnätverk och fjärrhantering av enheter. AstroWarp är särskilt utvecklat för integrering med GL.iNet-routrar och stöder heltäckande enhetshantering i hela nätverk, med styrning av både överordnade och underordnade enheter. Genom att fokusera på nätverksomfattande hantering och framtida stöd för styrning på maskinvarunivå erbjuder AstroWarp en robust och tillförlitlig lösning för enhetshantering och säkra, stabila nätverk.

## Program {#applications}

=== "Plug-ins"

    Insticksprogram är tilläggsfunktioner som utökar routerns funktionalitet. Information om hur du konfigurerar insticksprogram finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress. Information om hur du konfigurerar Dynamic DNS finns i [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home är ett verktyg från tredje part som blockerar annonser och spårning för att skydda dig.

    Information om hur du aktiverar AdGuard Home finns i [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Föräldrakontroll är en grupp inställningar som hjälper dig att hantera och styra dina barns enheter. De kan bland annat begränsa skärmtiden och åtkomsten till visst innehåll. Marble erbjuder två alternativ: en lokal version från GL.iNet och en integrerad version från föräldrakontrollappen Bark.

    Information om hur du konfigurerar föräldrakontroll finns i [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Tailscale är en VPN-tjänst som ger åtkomst till dina enheter och program var som helst. Information om konfiguration finns i [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier är en VPN-tjänst som låter dig ansluta enheter till ett virtuellt nätverk. Information om konfiguration finns i [ZeroTier](../../interface_guide/zerotier.md).

---

## Nätverksinställningar {#network-settings}

=== "Firewall"

    Sidan Firewall innehåller viktiga säkerhetsförbättringar för nätverket. Den har funktioner som Port Forwarding, Open Ports och DMZ. Med dessa verktyg kan du hantera och anpassa nätverkets trafikflöde och förbättra säkerheten.

    * Port Forwarding: Omdirigera viss trafik från internet till angivna enheter i nätverket och ge åtkomst till tjänster som spelservrar och webbservrar.
    * Open Ports: Övervaka och styr vilka portar som är öppna på routern för att förhindra obehörig åtkomst och möjliga säkerhetshot.
    * DMZ (Demilitarized Zone): Exponera en enhet mot internet genom att vidarebefordra all inkommande trafik till den.

    Detaljerade konfigurationsanvisningar och mer information finns i [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. Ethernet och repeater) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    På sidan LAN kan du hantera och konfigurera inställningarna för routerns lokala nätverk. Sidan innehåller bland annat följande funktioner:

    * Router IP Address: Ändra routerns IP-adress så att den passar nätverkskonfigurationen bättre.
    * Netmask: Ange nätmasken för nätverket. Den bestämmer nätverkets storlek och intervall av IP-adresser.
    * DHCP: Aktivera eller konfigurera Dynamic Host Configuration Protocol, som automatiskt tilldelar IP-adresser till enheter i nätverket.
    * Address Reservation: Reservera särskilda IP-adresser för vissa enheter så att de alltid får samma IP-adress från DHCP-servern.

    Detaljerade konfigurationsanvisningar och mer information finns i [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    På sidan Guest Network kan du skapa och hantera ett separat nätverk för gäster. De får internetåtkomst samtidigt som huvudnätverket förblir säkert. Sidan innehåller bland annat följande funktioner:

    * Gateway: Ange ett särskilt IP-adressintervall för gästnätverket för att skilja det från huvudnätverket.
    * DHCP: Konfigurera Dynamic Host Configuration Protocol för gästnätverket så att IP-adresser automatiskt tilldelas anslutna enheter.

    Funktionerna ger gäster internetåtkomst utan att äventyra huvudnätverkets säkerhet och prestanda.

    Detaljerade konfigurationsanvisningar och mer information finns i [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    Sidan DNS innehåller alternativ för att anpassa routerns Domain Name System-inställningar och förbättra både säkerhet och prestanda. Sidan innehåller bland annat följande funktioner:

    * Encrypted DNS: Konfigurera krypterad DNS för att skydda webbläsardata mot övervakning och manipulering och på så sätt säkerställa integritet och säkerhet.
    * Manual DNS: Ange valfria DNS-servrar manuellt för anpassad kontroll över DNS-frågor och eventuellt snabbare uppslagning.
    * DNS Proxy: Aktivera DNS-proxy för att dirigera DNS-förfrågningar från enheterna via en angiven DNS-server och få ytterligare kontroll över DNS-trafiken.

    Med dessa inställningar kan du optimera nätverkets DNS-prestanda och säkerhet efter dina behov.

    Detaljerade konfigurationsanvisningar och mer information finns i [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    På sidan Network Mode kan du konfigurera routern för olika driftlägen och på så sätt uppfylla olika nätverksbehov. Följande lägen är tillgängliga:

    * Router: Fungerar som en standardrouter, hanterar trafik mellan det lokala nätverket och internet och tillhandahåller funktioner som NAT, brandvägg och DHCP.
    * Access Point: Fungerar som en åtkomstpunkt och utökar det befintliga kabelanslutna nätverket med trådlös anslutning utan att dirigera trafik.
    * Extender: Fungerar som räckviddsförlängare och förstärker signalen från det befintliga trådlösa nätverket för att täcka ett större område och eliminera döda zoner.
    * WDS (Wireless Distribution System): Liknar Extender. Välj WDS om huvudroutern stöder WDS-läge.

    Detaljerade konfigurationsanvisningar och mer information finns i [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    På sidan IPv6 kan du konfigurera IPv6-inställningar för nätverket och få stöd för det senaste internetprotokollet. Du kan aktivera IPv6 och välja mellan fyra lägen efter nätverkets behov:

    * Native: Hämta en IPv6-adress direkt från internetleverantören för enkel och effektiv inbyggd IPv6-anslutning.
    * Passthrough: Låt IPv6-trafik passera genom routern till enheterna i nätverket. Anslutningen bryggas utan att routern själv hanterar IPv6-routningen.
    * NAT6: Använd Network Address Translation för IPv6 (NAT6) för att översätta mellan interna och externa IPv6-adresser på ett sätt som liknar NAT för IPv4.
    * Static IPv6: Konfigurera en statisk IPv6-adress för routern manuellt. En fast adress ger en konsekvent anslutning och enklare hantering av nätverkstjänster.

    Med dessa inställningar kan du dra nytta av IPv6-fördelar som större adressutrymme, förbättrade säkerhetsfunktioner och bättre prestanda.

    Detaljerade konfigurationsanvisningar och mer information finns i [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    På sidan MAC Address kan du visa och hantera de Media Access Control-adresser (MAC-adresser) som är kopplade till routern. Sidan innehåller bland annat följande funktioner:

    * Factory Default: Visa standard-MAC-adresserna för routerns Ethernet- och Repeater-lägen som referens för de ursprungliga maskinvaruinställningarna.
    * Clone: Klona MAC-adressen för en viss klientenhet. Detta är särskilt användbart när nätverksåtkomsten är begränsad till vissa enheter.
    * Manual: Ange en anpassad MAC-adress för routern manuellt. Du kan även använda knappen Random för att generera en slumpmässig MAC-adress, vilket ger flexibilitet och förbättrad integritet.

    Med dessa funktioner kan du hantera routerns MAC-adresser effektivt och säkerställa kompatibilitet och flexibilitet i olika nätverksmiljöer.

    Detaljerade konfigurationsanvisningar och mer information finns i [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN. Information om hur du konfigurerar Drop-in Gateway finns i [Konfigurera Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    På sidan IGMP Snooping kan du konfigurera inställningar som optimerar hanteringen av multicast-trafik i nätverket. IGMP Snooping lyssnar på och hämtar information från IGMP-protokollpaket och upprättar och underhåller vidarebefordringstabeller för multicast på lager 2. Det säkerställer att multicast-gruppdata endast vidarebefordras till värdar som har anslutit till multicast-gruppen och förhindrar att oönskad multicast-trafik når andra värdar.

    Inställningarna optimerar nätverkets prestanda och effektivitet, särskilt i miljöer med omfattande multicast-trafik, till exempel videoströmning och onlinespel.

    Detaljerade konfigurationsanvisningar och mer information finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    På sidan Network Acceleration kan du aktivera funktioner som minskar processorbelastningen och påskyndar vidarebefordran av trafikpaket, vilket förbättrar nätverkets övergripande prestanda. Nätverksacceleration kan dock stå i konflikt med vissa funktioner.

    Detaljerade konfigurationsanvisningar och mer information finns i [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    På sidan NAT Settings kan du konfigurera alternativ för Network Address Translation (NAT) för att optimera vissa program och förbättra nätverkets prestanda. Sidan innehåller bland annat följande inställningar:

    * Enable Full Cone NAT: Full Cone NAT kan minska latensen i spel genom att ge nätverkstrafiken en mer direkt och mindre begränsad väg. Funktionen kan dock försämra säkerheten eftersom externa värdar lättare kan initiera anslutningar till interna enheter.
    * Enable SIP ALG: Session Initiation Protocol Application Layer Gateway (SIP ALG) kan minska problem som orsakas av flera NAT och påverkar VoIP-tjänster. I de flesta fall är SIP ALG dock inte till nytta och kan orsaka envägsljud, telefoner som inte ringer, avbrutna anslutningar och samtal som går direkt till röstbrevlådan.

    Med inställningarna kan du anpassa routerns NAT-funktion efter nätverkets behov och balansera prestandaförbättringar mot möjliga säkerhets- och funktionsaspekter.

    Detaljerade konfigurationsanvisningar och mer information finns i [NAT Settings](../../interface_guide/nat_settings.md).

---

## Systeminställningar {#system-settings}

=== "Overview"

    Sidan Overview ger en heltäckande översikt över routerns aktuella status och prestandamätvärden. På sidan kan du visa:

    * CPU Average Load: Övervaka den genomsnittliga belastningen på routerns processor för att bedöma prestandan och identifiera möjliga flaskhalsar.
    * Memory Usage: Kontrollera hur mycket av routerns minne som används för att underlätta resurshanteringen.
    * Flash Usage: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
    * System Info: Visa detaljerad information om routersystemet, däribland firmwareversion, drifttid och nätverksstatus.
    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.

    Dessa funktioner ger viktig information och viktiga kontroller som hjälper dig att effektivt hantera och övervaka routern.

    Detaljerade konfigurationsanvisningar och mer information finns i [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    På sidan Upgrade kan du uppdatera routerns firmware till den senaste versionen för att få bättre prestanda, högre säkerhet och nya funktioner. Sidan erbjuder två uppgraderingsalternativ:

    * Online Upgrade: Sök automatiskt efter den senaste firmwareversionen på tillverkarens server. Du kan installera den senaste versionen om den är tillgänglig online.
    * Local Upgrade: Ladda upp en firmwarefil manuellt från datorn för att uppdatera routern. På så sätt styr du uppgraderingsversionen och tidpunkten.

    Med dessa alternativ kan du hålla routern uppdaterad med de senaste förbättringarna och korrigeringarna.

    Detaljerade konfigurationsanvisningar och mer information finns i [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    På sidan Scheduled Tasks kan du automatisera olika routerfunktioner enligt ett fördefinierat schema för enklare och effektivare användning. Sidan innehåller bland annat följande funktioner:

    * LED Display Schedule: Ange ett schema som automatiskt slår på eller av routerns LED-lampor och minskar ljusstörningar under vissa tider.
    * Schedule Reboot: Konfigurera routern så att den startas om automatiskt med angivna intervall för att upprätthålla optimal prestanda och stabilitet.
    * 5GHz Wi-Fi Status Schedule: Skapa ett schema som aktiverar eller inaktiverar Wi-Fi-bandet 5GHz vid vissa tider för att optimera nätverksanvändning och energieffektivitet.
    * 2.4GHz Wi-Fi Status Schedule: Ange ett schema som styr Wi-Fi-bandet 2.4GHz för bättre hantering av nätverkets tillgänglighet och strömförbrukning.

    Dessa schemaläggningsalternativ ger dig större kontroll över routerns funktioner, så att den kan uppfylla dina särskilda behov och önskemål.

    Detaljerade konfigurationsanvisningar och mer information finns i [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade konfigurationsanvisningar och mer information finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade konfigurationsanvisningar och mer information finns i [Log](../../interface_guide/log.md).

=== "Security"

    På sidan Security kan du konfigurera olika säkerhetsinställningar för att skydda nätverket och routern mot obehörig åtkomst. Sidan innehåller alternativ för:

    * Admin Password: Ange eller ändra lösenordet för routerns administratörsgränssnitt så att endast behöriga användare kan ändra inställningarna.
    * Local Access Control: Hantera och begränsa åtkomsten till routerns gränssnitt från enheter som är anslutna till det lokala nätverket.
    * Remote Access Control: Konfigurera och begränsa åtkomsten till routerns gränssnitt från fjärrplatser via internet för att förbättra skyddet mot externa hot.

    Dessa inställningar hjälper dig att upprätthålla en säker nätverksmiljö som skyddar både routern och anslutna enheter.

    Detaljerade konfigurationsanvisningar och mer information finns i [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade konfigurationsanvisningar och mer information finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade konfigurationsanvisningar och mer information finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
