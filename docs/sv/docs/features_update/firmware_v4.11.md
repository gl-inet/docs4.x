# Firmware v4.11 {#firmware-v411}

Den här versionen förbättrar övervakningen av nätverkskvalitet och säkerhetsbedömningen, så att du lättare kan identifiera anslutningsproblem och möjliga säkerhetsrisker. Den förbättrar även DNS, QoS, SQM och datastatistik för flexiblare nätverkshantering och trafikstyrning.

Hämta den senaste firmwareversionen från [nedladdningscentret för firmware](https://dl.gl-inet.com/){target="_blank"}.

## Nätverkskvalitet {#network-quality}

[Network Quality](../interface_guide/network_quality.md) är en ny funktion som övervakar internetanslutningen i realtid. Den bedömer svarstid, latens och DNS-prestanda samt upptäcker anslutningsavbrott och paketförluster. Det hjälper dig att identifiera instabila nätverk och anslutningsproblem som inte alltid upptäcks med enbart bandbreddstester.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Säkerhetskontroll {#security-scan}

[Security Scan](../interface_guide/security_scan.md) är en ny funktion som utvärderar routerns säkerhetsinställningar och visar en säkerhetspoäng, riskvarningar och optimeringsförslag. Den kontrollerar bland annat Wi-Fi-säkerhet, WAN-ping, SSH-fjärråtkomst, portvidarebefordran och DPI-innehållsskydd, så att du kan identifiera och åtgärda möjliga säkerhetsrisker. En kontroll startar automatiskt när du öppnar sidan. Du kan även klicka på poängikonen för att återställa och köra kontrollen igen.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## DNS {#dns}

Den här versionen förbättrar [DNS](../interface_guide/dns_v4.11.md)-konfigurationen genom att samla WAN DNS, VPN DNS och Manual DNS på en sida. Du kan enkelt visa DNS-status för varje anslutningstyp, konfigurera anpassade DNS-servrar och välja om manuella DNS-inställningar ska gälla för VPN-tunnlar eller själva routern.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) har alternativet **Run Speedtest** för WAN-bandbredd. Det mäter nedladdnings- och uppladdningshastigheten och fyller automatiskt i relevanta fält. För schemaläggningsprinciper lägger den här versionen till två alternativ utöver Application Priority: **Device Priority** och **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Valda lokala klienter får högre nätverksprioritet vid överbelastning av WAN.

- **Application Priority**: Ange egna prioriteter för olika program. Routern fördelar bandbredden efter dessa.

- **Advanced QoS**: Skapa avancerade QoS-regler för högprioriterad trafik.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) har alternativet **Run Speedtest** för WAN-bandbredd. Det mäter nedladdnings- och uppladdningshastigheten och fyller automatiskt i relevanta fält. Två ködiscipliner är tillgängliga: **cake** och **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: Smart, automatisk trafikformning med bäst övergripande latenskontroll (rekommenderas).

    För den här ködisciplinen justerar den nya funktionen **Cake Autorate** den konfigurerade bandbredden dynamiskt utifrån mätt RTT. Den använder resurssnåla pingförfrågningar i stället för aktiva hastighetstester och rekommenderas för WAN-anslutningar med varierande bandbredd.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: Enkel och effektiv rättvis köhantering med grundläggande latensminskning.

## Datastatistik {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) stöder nu trafikfiltrering efter klient och nya diagramvyer, däribland stapel- och cirkeldiagram. När du visar App Traffic Statistics kan du välja en viss klient och växla mellan diagramvyer för en tydligare analys av trafikanvändningen.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
