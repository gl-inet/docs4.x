# Multi-WAN {#multi-wan}

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Öppna **NETWORK** -> **Multi-WAN**.

Du kan konfigurera flera internetanslutningar så att routern snabbt växlar när en anslutning saknas eller använder flera samtidigt enligt ett angivet förhållande.

GL.iNet-routrar kan anslutas via [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md) och [Cellular](internet_cellular.md).

!!! Note

    1. Models lacking Wi-Fi functionality (e.g., GL-MT2500/GL-MT2500A) only support Ethernet, Tethering, and Cellular network access.

    2. Models lacking USB port (e.g., GL-B3000) only support Ethernet and Repeater network access.

    3. Vissa modeller stöder [Dual-Ethernet WAN](ethernet_port.md#dual-ethernet-wan), vilket ger ett extra Ethernet-gränssnitt på Multi-WAN.

## Interface Status Track {#interface-status-track}

GL.iNet-routrar stöder upp till 5 virtuella nätverksgränssnitt beroende på modell. GL-MT6000 har exempelvis **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** och **Cellular**.

Routern använder **ping** eller **httping** (endast v4.3 och tidigare) mot destinations-IP för att avgöra om gränssnittet är tillgängligt.

Ett tillgängligt gränssnitt visas med grön punkt, annars grå.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Status Track Settings {#status-track-settings}

Klicka på kugghjulet för statusövervakning av respektive gränssnitt.

Exemplet visar Ethernet; samma gäller andra gränssnitt.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: Aktiverat som standard. Om det inaktiveras avgör routern status utifrån fysisk anslutning, till exempel nätverkskabeln.

- **Detection Mode**: Introducerades som Low Data Mode i v4.5 och bytte namn i v4.7. Lägena är Normal Mode, Low Data Mode och Strict Mode.

    Normal Mode används som standard. Low Data Mode testar endast vid nätverksfel, och Strict Mode avgör status enbart från ett test mot en offentlig IP.

    Low Data Mode passar begränsade dataplaner men kan ge långsammare återanslutning. Endast Cellular aktiveras som standard.

- **Track Command**: ping testar destinations-IP. I firmware v4.3 och tidigare finns även httping.

- **IPv4 Track IP**: Ange en egen IPv4-testadress.

!!! Note

    Äldre firmware som v4.3 har **Track Interval**, **Change to Failure Condition** och **Change to Available Condition**. Från v4.5 ersätts de av Detection Mode och Sensitivity Options.

### Sensitivity Options {#sensitivity-options}

This feature is available since v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Känsligheten avgör intervallet för internetstatuskontroll.

- Vid stabilt nätverk, video eller spel rekommenderas hög känslighet för snabb växling.
- Vid instabilt nätverk och filhämtning rekommenderas låg känslighet för att undvika ständig växling.

**Tips!** Hög känslighet kan orsaka frånkoppling. Ändra försiktigt.

## Multi-WAN Mode {#multi-wan-mode}

Multi-WAN har **Failover** och **Load Balance**. Endast ett kan användas åt gången.

### Failover {#failover}

Failover är standard med flera WAN-anslutningar. Om den aktiva länken slutar fungera växlar routern automatiskt.

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Ange prioritet för varje gränssnitt. Vid fel används nästa tillgängliga med högst prioritet, och routern växlar tillbaka när en högre prioritet återställs.

### Load Balance {#load-balance}

Load Balance enables multiple network links to be used simultaneously, increasing bandwidth and improving total throughput.

**Load Ratio** avgör hur nya anslutningar fördelas mellan gränssnitt.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

Två belastningsförhållanden kan konfigureras:

- **Default Load Ratio**

    Med fyra aktiva gränssnitt och förhållandet 1:1:1:1 fördelas nya anslutningar jämnt mellan Ethernet, Repeater, Tethering och Cellular.

- **Customize Load Ratio**

    Med Ethernet 200 Mbps och Repeater 100 Mbps kan förhållandet anges till 2:1:0:0. Ethernet hanterar då ungefär dubbelt så många nya anslutningar som Repeater.

**Obs!** Befintliga anslutningar följer inte garanterat förhållandet; det närmas efter längre användning.

## Usage Scenarios {#usage-scenarios}

* Ett kassasystem använder kabelanslutning och Repeater eller Cellular som reserv för att undvika avbrott i betalningar.

* Om offentligt Wi-Fi via Repeater är långsamt kan Mobile Tethering användas samtidigt med Load Balance.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
