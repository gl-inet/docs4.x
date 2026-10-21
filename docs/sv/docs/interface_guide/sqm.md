# SQM (Smart Queue Management) {#sqm-smart-queue-management}

**Note**: This feature was introduced in firmware v4.9.

Vissa modeller, till exempel Mango 2 (GL-MG1300), stöder inte SQM på grund av otillräckligt minne, även med firmware v4.9 eller senare.

---

Öppna **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) hanterar trafiken för att minimera latens och ”bufferbloat” och ge smidigare spel och röstsamtal.

**Note**:

1. Funktionen påverkar endast trafik genom routern när den fungerar som gateway, inklusive lokal klient- och VPN-klienttrafik. Inkommande trafik till en VPN-server påverkas inte.
2. Since SQM is resource-intensive, it works best for low-bandwidth or congested networks. Enabling it on high-speed connections may reduce peak throughput.
3. SQM får ingen effekt i Drop-in Gateway-läge.
4. SQM and QoS cannot be enabled simultaneously.
5. SQM cannot work with Network Acceleration. Enabling SQM will automatically disable Network Acceleration to ensure stable performance.

## Supported Models {#supported-models}

??? "Supported Models"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Unsupported Models"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## För firmware v4.11 och senare {#for-firmware-v411-and-above}

Aktivera SQM och följ stegen nedan.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Ange WAN-uppladdning och nedladdning (1-10000) eller klicka på **Run Speedtest** för automatisk mätning. Internetanslutning krävs.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Obs!** Värden anges i **Mbps**. Motsvarande **MB/s** visas som referens.

2. **Queue Discipline**

    Select a queueing rule to manage traffic and reduce latency under load.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended).

        När **cake** väljs som ködisciplin är **Cake Autorate** tillgängligt.

        Cake Autorate justerar CAKE-bandbredden i realtid utifrån test-RTT med resurssnåla pingförfrågningar. Rekommenderas för varierande WAN-bandbredd men behövs inte på stabila länkar.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Obs!** Cake Autorate genererar kontinuerlig testtrafik i bakgrunden. Beakta dataanvändningen på mätade anslutningar.

        Standardinställningarna passar de flesta anslutningar. Ändra endast parametrarna om du förstår effekten. **Reset to Default** återställer standardvärden.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: A list of IP addresses separated by commas, used for network quality probing.

        - **Probe Interval**: Shorter intervals enable faster response but consume more CPU resources.

        - **Concurrent Probes**: Antalet samtidiga tester får inte överstiga antalet testservrar; högre värden ökar processorbelastningen.

        - **Idle Detection Threshold**: Under detta värde betraktas anslutningen som inaktiv. Värdet får inte överstiga 25% av hastighetsgränsen.

        - **Download Latency Threshold**: Överskriden nedladdningslatens utlöser bandbreddsminskning.

        - **Upload Latency Threshold**: Överskriden uppladdningslatens utlöser bandbreddsminskning.

    - **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

## For firmware v4.9 to v4.10 {#for-firmware-v49-to-v410}

Aktivera SQM och ange maximal uppladdnings- och nedladdningshastighet (1-10000) efter faktisk internetbandbredd.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Obs!** Värden anges i **Mbps**. Motsvarande **MB/s** visas som referens.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

For Queue Rule, two options are available:

- **cake**: Smart, automatic traffic shaping with superior overall latency control (recommended).

- **fq_codel**: Simple, efficient fair queueing with basic latency reduction.

!!! Tip

    QoS anger programprioriteter och fördelar bandbredd därefter, medan SQM låter dig välja köregel.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
