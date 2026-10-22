# Network Quality {#network-quality}

**Note**: This feature was introduced in firmware v4.11.

---

Öppna **FLOW CONTROL** -> **Network Quality** på vänster sida i webbadministrationspanelen.

Network Quality övervakar anslutningskvaliteten i realtid och bedömer svarstid, latens och DNS-prestanda samt upptäcker avbrott och paketförlust.

På sidan bedömer du anslutningen med Network Quality Score och kör lokala hastighetstester.

**Note**:

1. The overall GL.iNet Network Quality Score is calculated by the weighted formula:

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest körs lokalt på routern och omfattas av hastighetsgränser från SQM och QoS.

## Network Quality Score {#network-quality-score}

Avsnittet visar Network Quality Score, beräknad från Response Score och Reliable Score. Det visar även latens, jitter, paketförlust samt nedladdning och uppladdning i KB/s. `google.com` används som standardmål.

Klicka på inställningsikonen för att konfigurera testmål.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Välj testmål för Internet Reachability och DNS Resolution, däribland Baidu, Tencent, Alibaba, Google, Microsoft och Cloudflare, eller ange en domän manuellt.

Målen används för anslutnings- och DNS-tester samt Network Quality Score.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: Used to probe internet connectivity and measure end-to-end latency (Hop2 ping target).

- **DNS Resolution Target**: Domänen som slås upp under DNS-tester. Både A(IPv4)- och AAAA(IPv6)-poster efterfrågas.

## Speedtest {#speedtest}

Det inbyggda testet använder Cloudflare Speed Test för nedladdning, uppladdning, pinglatens och bufferbloat och visar diagram i realtid.

Klicka på **Run Speedtest** för att starta.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

After the test is complete, the page will display the results.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
