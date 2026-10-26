# Firmware v4.9 {#firmware-v49}

Den här versionen ger mer exakt nätverksstyrning, förbättrad trafikhantering, högre nätverkssäkerhet och ett omarbetat användargränssnitt. Allt detta är utformat för att ge en bättre helhetsupplevelse.

Hämta den senaste firmwareversionen från [nedladdningscentret för firmware](https://dl.gl-inet.com/){target="_blank"}.

## Trafikstyrning {#flow-control}

Flow Control är en central nätverkshanteringsmodul för exakt identifiering, övervakning, reglering och filtrering av nätverkstrafik. Den optimerar tilldelningen av nätverksresurser, motverkar överbelastning av bandbredden och standardiserar nätverksåtkomsten för en smidigare, säkrare och mer kontrollerbar nätverksupplevelse. I firmware v4.9 integreras modulen med flera praktiska funktioner för heltäckande trafikhantering.

Modulen Flow Control innehåller DPI Engine, Data Statistics, Content Filter, QoS, SQM och Parental Control.

### DPI Engine {#dpi-engine}

Till skillnad från traditionella routrar, som endast identifierar käll- och destinationsadresser, analyserar DPI (Deep Packet Inspection) paketens nyttolast på djupet. Med hjälp av ett bibliotek för funktionsmatchning identifierar DPI program och webbplatser exakt, vilket möjliggör detaljerad klassificering och styrning av trafiken.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

GL.iNet DPI är integrerat med [Netify](https://www.netify.ai/){target="_blank"} och använder ett resurssnålt inbäddat insticksprogram för effektiv distribution. Netifys signaturdatabas uppdateras online och möjliggör tillförlitlig hantering, vilket gör nätverksstyrningen mer exakt och effektiv.

### Datastatistik {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) ger en intuitiv trafikinstrumentpanel som visar nätverksanvändningen efter program och protokoll. Den stöder historiska trender för 1 timme, 1 dag och 7 dagar, visar användningsrankning, övervakar trafik per enhet och gör det möjligt att blockera oönskade program med ett klick.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Innehållsfilter {#content-filter}

[Content Filter](../interface_guide/content_filter.md) är en intelligent funktion för säkerhet online som bygger på DPI-klassificering. Den blockerar automatiskt skadliga webbplatser för att hålla nätverket rent och säkert och stöder även anpassade regler för att blockera vissa program, domäner eller IP-adresser.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) optimerar bandbreddstilldelningen genom att prioritera viktiga aktiviteter (t.ex. videosamtal och spel) när nätverket är överbelastat. Det minskar latensen och förbättrar nätverkets övergripande prestanda.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) hanterar routerns nätverkstrafik intelligent för att minimera latens och ”bufferbloat”, vilket ger smidigare spel och röstsamtal.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Föräldrakontroll {#parental-control}

[Parental Control](../interface_guide/parental_control_v4.9.md) fanns tidigare på menyn **Applications**. I firmware v4.9 har funktionen flyttats till menyn **Flow Control**, eftersom den använder den uppgraderade DPI-motorn för att exakt identifiera och blockera olämpliga program och olämpligt nätverksinnehåll. Det ger mer avancerade och exakta trafikbaserade åtkomstbegränsningar.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN {#vpn}

Firmware v4.9 förbättrar VPN-modulens underliggande routningslogik och interaktiva gränssnitt. Versionen åtgärdar möjliga routningskonflikter, förenklar konfigurationslogiken och gör användningen mer intuitiv.

De detaljerade ändringarna är följande.

### Isolerad VPN-tunnel {#isolated-vpn-tunnel}

Varje VPN-tunnel fungerar som en oberoende grupp utan redundansväxling mellan grupper. När nätverkstrafiken matchar en viss VPN-grupp växlar den inte automatiskt till andra VPN-grupper om den aktuella tunneln slutar fungera. Detta ger en stabil och förutsägbar routning av trafiken.

**Obs!** Den tidigare principen "Not Use VPN" har tagits bort i firmware v4.9. Det eliminerar överflödig konfiguration och motverkar routningskonflikter som orsakas av flera komplicerade tunnelregler.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Redundansväxling för VPN-profiler {#vpn-profile-failover}

En VPN-tunnelgrupp kan innehålla flera konfigurationsprofiler. Du kan anpassa prioriteten för varje profil inom samma grupp. Det möjliggör automatisk intern redundansväxling som upprätthåller VPN-anslutningen när en enskild profil slutar fungera.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Omdesignad instrumentpanel {#redesigned-dashboard}

[VPN Dashboard](../interface_guide/vpn_dashboard.md) i firmware v4.9 har fått en fullständig omdesign med en mer intuitiv layout. Tunnelstatus, anslutningsinformation och konfigurationsposter visas tydligare, vilket gör den dagliga användningen och hanteringen betydligt effektivare. Dessutom är Kill Switch aktiverad som standard för alla VPN-tunnlar i den nya arkitekturen, så att trafiken alltid är skyddad.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0 {#amneziawg-20}

Firmware v4.9 introducerar officiellt protokollet AmneziaWG 2.0 med flera nya parametrar för trafikobfuskering. Det uppgraderade protokollet undgår effektivt identifiering av DPI och andra system för trafikidentifiering, vilket avsevärt förbättrar möjligheten att dölja anslutningen och motstå störningar. Detta gör det möjligt att upprätta stabila och tillförlitliga VPN-anslutningar i regioner med nätverksbegränsningar och i komplicerade nätverksmiljöer.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## IoT-nätverk {#iot-network}

Med [IoT Network](../interface_guide/iot_network.md) i firmware v4.9 kan du skapa ett separat Wi-Fi-nätverk för smarta IoT-enheter. Nätverket är fysiskt och logiskt isolerat från det primära nätverket och förhindrar att IoT-enheter belastar huvudnätverkets resurser eller medför säkerhetsrisker där. Optimeringen ger bredare enhetskompatibilitet för olika smarta IoT-klienter och förbättrar säkerheten i hemnätverket som helhet.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL {#acl}

[ACL](../interface_guide/acl.md), en förkortning av Access Control List, är en central funktion för hantering av nätverkssäkerhet. Med den kan du skapa anpassade åtkomstregler för att hantera intern och extern nätverkstrafik utifrån anslutningsprotokoll, enheternas IP-adresser och portar. Funktionen stöder exakt behörighetsstyrning för att tillåta eller blockera specifika typer av nätverksåtkomst. Om flera ACL-regler står i konflikt med varandra tillämpar systemet automatiskt regeln med högst prioritet för att säkerställa korrekt tillämpning av principerna.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL skiljer sig i sin grundläggande funktion från Port Forwarding. ACL styr enheters och trafiks åtkomstbehörigheter och fokuserar på hantering av nätverkssäkerhet. Port Forwarding används i stället för omdirigering av nätverksresurser. Funktionen vidarebefordrar extern nätverkstrafik till angivna lokala slutenheter för fjärråtkomst till lokala nätverkstjänster.

## Trådlöst {#wireless}

Användargränssnittet för [Wireless](../interface_guide/wireless.md) har fått en helt ny, förenklad layout och enhetlig visuell stil. Det minskar användningens komplexitet och gör gränssnittet betydligt enklare och mer användarvänligt.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## Krypterad DNS {#encrypted-dns}

[Encrypted DNS](../interface_guide/dns.md#encrypted-dns) har utökats med fler krypteringsprotokoll, däribland DoH, DoT och DoQ. Samtidigt har fler officiella DNS-tjänsteleverantörer integrerats, och manuell konfiguration av anpassade krypterade DNS-servrar har lagts till för att tillgodose olika behov av säker domännamnsupplösning.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale-utgångsnod {#tailscale-exit-node}

GL.iNet-routrar kan nu köras som Tailscale-utgångsnoder. All utgående internettrafik från enheter i Tailnet kan dirigeras via routerns offentliga IP-adress. Det ger enhetlig och säker hantering av nätverksutgången för hela Tailscale-nätverket. Mer information finns [här](../interface_guide/tailscale.md#run-exit-node).

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
