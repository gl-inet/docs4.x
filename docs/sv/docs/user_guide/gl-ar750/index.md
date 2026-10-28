# Användarhandbok för Creta (GL-AR750) {#creta-gl-ar750-user-guide}

## Produktöversikt {#product-overview}

Creta (GL-AR750) är en AC-reserouter med dubbla band. Samtidig användning av båda banden stöder en trådlös överföringshastighet på upp till 733Mbps (2.4GHz: 300Mbps + 5GHz: 433Mbps). Creta kan omvandla ett offentligt nätverk till ett privat Wi-Fi-nätverk för säker surfning. Extern lagring stöder MicroSD på upp till 128GB. OpenWrt/LEDE och OpenVPN är förinstallerade. Creta ger integritetsmedvetna användare ett snabbt och enkelt VPN med modern kryptografi.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Specifikationer {#specifications}

[Specifikationer för GL-AR750](https://www.gl-inet.com/products/gl-ar750/#specs){target="_blank"}

## Konfigurera Creta {#how-to-set-up-creta}

Konfigurera Creta med någon av de fyra internetanslutningsmetoder som stöds: Ethernet, Repeater, Tethering eller Cellular. Titta på konfigurationsvideon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(I videon visas konfigurationen med en annan GL.iNet-router, men stegen är desamma för Creta och andra routermodeller.)</small>

### 1. Slå på Creta {#1-power-on-creta}

Anslut Micro USB-strömkabeln till routerns strömport. Använd en standardnätadapter på 5V/2A.

!!! Note

    Hot-plugging av TF-kort stöds inte. Sätt in TF-kortet innan routern slås på om du vill använda det.

### 2. Anslut enheten till Creta {#2-connect-your-device-to-creta}

Anslut datorn eller den mobila enheten till routern via Wi-Fi eller Ethernet.

=== "Wi-Fi"

    Leta reda på routerns Wi-Fi-nätverksnamn i listan över tillgängliga nätverk på enheten och ange lösenordet. Standardnamnet och standardlösenordet för nätverket finns på routerns etikett.

=== "Ethernet"

    Anslut enheten till routerns LAN-port med en Ethernet-kabel.

### 3. Anslut Creta till internet {#3-connect-creta-to-the-internet}

**Obs!** Följande anvisningar gäller när du ansluter routern till internet via webbadministrationspanelen. Om du vill använda GL.iNet-appen i stället kan du [hämta appen](https://www.gl-inet.com/app/){target="_blank"} och följa anvisningarna på skärmen.

#### 1. Logga in på routerns webbadministrationspanel {#1-log-in-to-the-router-web-admin-panel}

Ange `192.168.8.1` i webbläsarens adressfält. Välj språk och klicka sedan på **Next**. Ange administratörslösenordet och klicka på **Apply**.

#### 2. Konfigurera internetanslutningsmetoder {#2-set-up-your-internet-connection-methods}

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}

    Anslut routerns WAN-port till en uppströms enhet, till exempel ett modem, med en Ethernet-kabel. När internetanslutningen har upprättats visas en grön punkt bredvid "Ethernet".

    Detaljerade anvisningar finns i [Anslut till internet via en Ethernet-kabel](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. Leta reda på avsnittet "Repeater" på huvudskärmen i webbadministrationspanelen och klicka på **Connect**.
    2. Välj ett Wi-Fi-nätverk.
    3. Ange nätverkslösenordet och klicka sedan på **Apply**.

    När internetanslutningen har upprättats visas en grön punkt bredvid Wi-Fi-nätverksnamnet.

    Detaljerade anvisningar finns i [Anslut till internet via ett befintligt Wi-Fi-nätverk](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Anslut smarttelefonen till routern med en USB-kabel och aktivera nätverksdelning under Personal hotspot i inställningarna.
    2. Leta reda på avsnittet "Tethering" på huvudskärmen i webbadministrationspanelen och klicka på **Connect**.
    3. När internetanslutningen har upprättats visas en grön punkt bredvid "Tethering".

    Detaljerade anvisningar finns i [Anslut till internet via internetdelning med USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Sätt in ett USB-modem för mobilnät i routerns USB-port.
    2. Leta reda på avsnittet "Cellular" på huvudskärmen i webbadministrationspanelen och klicka på **Connect**.
    3. När internetanslutningen har upprättats visas en grön punkt bredvid "Cellular".

    Detaljerade anvisningar finns i [Anslut till internet via ett USB-modem](../../interface_guide/internet_cellular.md).

**Obs!** Om du vill använda Multi-WAN-funktionen måste du konfigurera fler än en internetanslutningsmetod.

---

## Konfigurera ett VPN {#how-to-set-up-a-vpn}

Ett VPN (virtuellt privat nätverk) skapar en säker, krypterad trafikförbindelse mellan din enhet och VPN-servern. Det ger ett extra lager av integritet och säkerhet (VPN-klient) och låter dig få åtkomst till ett fjärrnätverk (VPN-server). Creta och andra GL.iNet-routrar stöder OpenVPN och WireGuard.

=== "OpenVPN"

    Creta och andra GL.iNet-routrar stöder OpenVPN-protokollet, som erbjuder hög säkerhet. Följ dessa guider för att konfigurera OpenVPN:

    * [Konfigurera en OpenVPN-klient](../../interface_guide/openvpn_client.md)
    * [Konfigurera en OpenVPN-server](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta och andra GL.iNet-routrar stöder WireGuard-protokollet, som erbjuder hög hastighet och enkel användning. Följ dessa guider för att konfigurera WireGuard:

    * [Konfigurera en WireGuard-klient](../../interface_guide/wireguard_client.md)
    * [Konfigurera en WireGuard-server](../../interface_guide/wireguard_server.md)

---

## Fler program {#more-applications}

=== "Plug-ins"

    Insticksprogram är tilläggsfunktioner som utökar routerns funktionalitet. Information om hur du konfigurerar insticksprogram finns i [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) identifierar och uppdaterar automatiskt IP-adressen som är kopplad till en domän i realtid. Tjänsten kopplar ett domännamn till routerns dynamiska offentliga IP-adress, så att du kan fjärransluta till nätverket utan en statisk IP-adress. Information om hur du konfigurerar Dynamic DNS finns i [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    GL.iNets molnhanteringstjänst [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är ett enkelt sätt att fjärransluta till och hantera GL.iNet-routrar. Information om hur du konfigurerar GoodCloud finns i [GoodCloud](../../interface_guide/cloud.md).

---

## Nätverksinställningar {#network-settings}

=== "Firewall"

    Sidan Firewall innehåller viktiga säkerhetsförbättringar för nätverket. Den har funktioner som Port Forwarding, Open Ports och DMZ. Med dessa verktyg kan du hantera och anpassa nätverkets trafikflöde och förbättra säkerheten.

    * Port Forwarding: Omdirigera viss trafik från internet till angivna enheter i nätverket och ge åtkomst till tjänster som spelservrar och webbservrar.
    * Open Ports: Övervaka och styr vilka portar som är öppna på routern för att förhindra obehörig åtkomst och möjliga säkerhetshot.
    * DMZ (Demilitarized Zone): Exponera en enhet mot internet genom att vidarebefordra all inkommande trafik till den.

    Detaljerade konfigurationsanvisningar och mer information finns i [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN är en nätverksfunktion som gör att du kan konfigurera routern med flera internetanslutningar (t.ex. mobilnät, repeater och Ethernet) samtidigt. Om den aktuella internetanslutningen slutar fungera växlar routern automatiskt till en annan internetanslutning. Det ger en smidig och oavbruten internetåtkomst.

    Information om hur du konfigurerar Multi-WAN finns i [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    På sidan LAN kan du hantera och konfigurera inställningarna för routerns lokala nätverk. Sidan innehåller bland annat följande funktioner:

    * Router IP Address: Ändra routerns IP-adress så att den passar nätverkskonfigurationen bättre.
    * Netmask: Ange nätmasken för nätverket. Den bestämmer nätverkets storlek och intervall av IP-adresser.
    * DHCP: Aktivera eller konfigurera Dynamic Host Configuration Protocol, som automatiskt tilldelar IP-adresser till enheter i nätverket.
    * Address Reservation: Reservera särskilda IP-adresser för vissa enheter så att de alltid får samma IP-adress från DHCP-servern.

    Detaljerade konfigurationsanvisningar och mer information finns i [LAN](../../interface_guide/lan.md).

---

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

=== "IPv6"

    På sidan IPv6 kan du konfigurera IPv6-inställningar för nätverket och få stöd för det senaste internetprotokollet. Du kan aktivera IPv6 och välja mellan fyra lägen efter nätverkets behov:

    * Native: Hämta en IPv6-adress direkt från internetleverantören för enkel och effektiv inbyggd IPv6-anslutning.
    * Passthrough: Låt IPv6-trafik passera genom routern till enheterna i nätverket. Anslutningen bryggas utan att routern själv hanterar IPv6-routningen.
    * NAT6: Använd Network Address Translation för IPv6 (NAT6) för att översätta mellan interna och externa IPv6-adresser på ett sätt som liknar NAT för IPv4.
    * Static IPv6: Konfigurera en statisk IPv6-adress för routern manuellt. En fast adress ger en konsekvent anslutning och enklare hantering av nätverkstjänster.

    Dessa lägen ger flexibla konfigurationsalternativ för IPv6 som passar olika nätverksmiljöer.

    Detaljerade konfigurationsanvisningar och mer information finns i [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    På sidan MAC Address kan du visa och hantera de Media Access Control-adresser (MAC-adresser) som är kopplade till routern. Sidan innehåller bland annat följande funktioner:

    * Factory Default: Visa standard-MAC-adresserna för routerns Ethernet- och Repeater-lägen som referens för de ursprungliga maskinvaruinställningarna.
    * Clone: Klona MAC-adressen för en viss klientenhet. Detta är särskilt användbart när nätverksåtkomsten är begränsad till vissa enheter.
    * Manual: Ange en anpassad MAC-adress för routern manuellt. Du kan även använda knappen Random för att generera en slumpmässig MAC-adress, vilket ger flexibilitet och förbättrad integritet.

    Med dessa funktioner kan du hantera routerns MAC-adresser effektivt och säkerställa kompatibilitet och flexibilitet i olika nätverksmiljöer.

    Detaljerade konfigurationsanvisningar och mer information finns i [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway utökar huvudrouterns funktioner med funktioner som den kanske saknar, däribland AdGuard Home, krypterad DNS och VPN. Information om hur du konfigurerar Drop-in Gateway finns i [Konfigurera Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    På sidan IGMP Snooping kan du konfigurera inställningar som optimerar hanteringen av multicast-trafik i nätverket. IGMP Snooping lyssnar på och hämtar information från IGMP-protokollpaket och upprättar och underhåller vidarebefordringstabeller för multicast på lager 2. Det säkerställer att multicast-gruppdata endast vidarebefordras till värdar som har anslutit till multicast-gruppen och förhindrar att oönskad multicast-trafik når andra värdar.

    Inställningarna optimerar nätverkets prestanda och effektivitet, särskilt i miljöer med omfattande multicast-trafik, till exempel videoströmning och onlinespel.

    Detaljerade konfigurationsanvisningar och mer information finns i [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Systeminställningar {#system-settings}

=== "Overview"

    Sidan Overview ger en heltäckande översikt över routerns aktuella status och prestandamätvärden. På sidan kan du visa:

    * CPU Average Load: Övervaka den genomsnittliga belastningen på routerns processor för att bedöma prestandan och identifiera möjliga flaskhalsar.
    * Memory Usage: Kontrollera hur mycket av routerns minne som används för att underlätta resurshanteringen.
    * Flash Usage: Visa användningen av routerns flashlagring och kontrollera att det finns tillräckligt med utrymme för firmware och konfigurationsdata.
    * LED Control: Slå på eller av routerns LED-lampor för att anpassa enhetens visuella indikatorer.
    * System Info: Visa detaljerad information om routersystemet, däribland firmwareversion, drifttid och nätverksstatus.

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

=== "Admin Password"

    På sidan Admin Password kan du ange eller ändra lösenordet för routerns administratörsgränssnitt, så att endast behöriga användare kan öppna och ändra routerns inställningar. Lösenordet är avgörande för nätverkets säkerhet och integritet och skyddar mot obehörig åtkomst och konfigurationsändringar.

    Detaljerade konfigurationsanvisningar och mer information finns i [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    På sidan Time Zone kan du ange rätt tidszon för routern. Då tidsstämplas alla schemalagda uppgifter, loggar och systemhändelser korrekt enligt din lokala tid. Inställningen är viktig för korrekta register och för att tidsbaserade konfigurationer ska köras på rätt sätt.

    Detaljerade konfigurationsanvisningar och mer information finns i [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    På sidan Toggle Button Settings kan du konfigurera routerns fysiska växlingsknapp och tilldela den särskilda funktioner för snabb åtkomst och styrning. Funktionen ger praktiska genvägar till vanliga uppgifter och inställningar och förenklar routerhanteringen.

    Detaljerade konfigurationsanvisningar och mer information finns i [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    Sidan Log ger åtkomst till olika loggar som registrerar routerns aktiviteter och händelser. De hjälper till vid felsökning och prestandaövervakning. Sidan innehåller:

    * System Log: Detaljerade loggar över händelser och aktiviteter på systemnivå.
    * Kernel Log: Loggar som rör kärnans åtgärder och händelser.
    * Crash Log: Poster över systemkrascher och fel som är användbara vid diagnostisering av allvarliga problem.
    * Cloud Log: Loggar över interaktioner och aktiviteter som rör GoodCloud-tjänster som är integrerade med routern.
    * Nginx Log: Loggar från Nginx-webbservern, om den används av routern, med information om webbtrafik och serveråtgärder.

    Sidan har dessutom knappen Export Log, som låter dig exportera alla insamlade loggar för analys av den tekniska supporten. Funktionen är mycket användbar för diagnostisering av komplicerade problem och för att få professionell hjälp.

    Detaljerade konfigurationsanvisningar och mer information finns i [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    På sidan Reset Firmware kan du återställa routerns aktuella firmwareversion till standardinställningarna. Alla anpassade konfigurationer raderas. Processen återställer routern till standardinställningarna för den installerade firmwareversionen. Det kan vara användbart vid felsökning av återkommande problem eller om du vill börja om med standardkonfigurationen för aktuell firmware.

    Detaljerade konfigurationsanvisningar och mer information finns i [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    Sidan Advanced Settings ger åtkomst till avancerade konfigurationsalternativ via OpenWrt LuCI-gränssnittet. Erfarna användare kan finjustera routerns inställningar och funktioner utöver alternativen i det grundläggande gränssnittet. Det omfattar detaljerade nätverkskonfigurationer, brandväggsinställningar och andra avancerade systemanpassningar.

    Detaljerade konfigurationsanvisningar och mer information finns i [Advanced Settings](../../interface_guide/advanced_settings.md).
