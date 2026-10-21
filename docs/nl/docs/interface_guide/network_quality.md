# Network Quality {#network-quality}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.11.

---

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **Network Quality**.

Het dashboard Network Quality bewaakt de kwaliteit van je internetverbinding in realtime. Het beoordeelt reactiesnelheid, latentie en DNS-prestaties en detecteert verbindingsuitval en pakketverlies. Zo kun je instabiliteit en problemen vinden die bandbreedtetests alleen niet tonen.

Op deze pagina kun je de internetverbinding met Network Quality Score beoordelen en lokale snelheidstests uitvoeren.

**Note**:

1. De algemene GL.iNet Network Quality Score wordt met de volgende gewogen formule berekend:

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest is een lokale snelheidstest op de router en volgt snelheidsbeperkingen van functies zoals SQM en QoS.

## Network Quality Score {#network-quality-score}

Dit gedeelte toont de algemene Network Quality Score, berekend uit Response Score en Reliable Score. Je kunt elke score afzonderlijk bekijken. Het paneel toont ook latentie, jitter, pakketverlies en realtime download- en uploadsnelheden in KB/s. Het dashboard gebruikt standaard `google.com` voor controles van internetverbinding en DNS-omzetting.

Klik op het instellingenpictogram om de testdoelen te configureren.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Je kunt testdoelen voor Internet Reachability en DNS Resolution selecteren, waaronder Baidu, Tencent, Alibaba, Google, Microsoft en Cloudflare, of handmatig een aangepast domein invoeren.

De ingestelde doelen worden gebruikt voor verbindings- en DNS-tests en de berekening van Network Quality Score.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: controleert de internetverbinding en meet end-to-endlatentie (Hop2-pingdoel).

- **DNS Resolution Target**: het domein dat tijdens DNS-tests wordt omgezet. Zowel A(IPv4)- als AAAA(IPv6)-records worden opgevraagd.

## Speedtest {#speedtest}

Deze ingebouwde snelheidstest gebruikt Cloudflare Speed Test om download- en uploadsnelheden, pinglatentie en bufferbloat te meten. Tijdens de test worden realtime grafieken weergegeven.

Klik op **Run Speedtest** om de snelheidstest te starten.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Na de test toont de pagina de resultaten.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
