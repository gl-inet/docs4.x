# Multi-WAN {#multi-wan}

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ga links in het webbeheerpaneel naar **NETWORK** -> **Multi-WAN**.

Je kunt meerdere methoden voor internettoegang configureren. Als één methode niet beschikbaar is, schakelt de router snel naar een andere. Je kunt ook meerdere methoden tegelijk gebruiken en nieuwe verbindingen volgens een ingestelde verhouding verdelen.

GL.iNet-routers kunnen op verschillende manieren met internet worden verbonden, zoals [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md) en [Cellular](internet_cellular.md).

!!! Note

    1. Modellen zonder Wi-Fi, zoals GL-MT2500/GL-MT2500A, ondersteunen alleen Ethernet, Tethering en Cellular.

    2. Modellen zonder USB-poort, zoals GL-B3000, ondersteunen alleen Ethernet en Repeater.

    3. Sommige modellen ondersteunen [Dual-Ethernet WAN](ethernet_port.md#dual-ethernet-wan). Dan verschijnt een extra Ethernet-interface op de pagina Multi-WAN.

## Interfacestatus bewaken {#interface-status-track}

GL.iNet-routers ondersteunen maximaal 5 virtuele netwerkinterfaces; het exacte aantal verschilt per model. GL-MT6000 heeft bijvoorbeeld **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** en **Cellular**, elk met een eigen netwerkfunctie.

De routers gebruiken **ping** of, alleen in v4.3 en ouder, **httping** om de verbinding met het doel-IP te bewaken en te bepalen of de interface beschikbaar is.

Als de interface beschikbaar is, staat links een groene stip; anders is deze grijs.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Instellingen voor statusbewaking {#status-track-settings}

Klik op het tandwielpictogram voor de instellingen voor statusbewaking van elke netwerkinterface.

Hieronder staan de instellingen voor de Ethernet-interface; hetzelfde geldt voor andere interfaces.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: standaard ingeschakeld. Als je statusbewaking uitschakelt, bepaalt de router de interfacestatus aan de hand van de fysieke status, zoals een aangesloten netwerkkabel.

- **Detection Mode**: geïntroduceerd als Low Data Mode in v4.5 en in v4.7 hernoemd naar Detection Mode. Beschikbare modi zijn Normal Mode, Low Data Mode en Strict Mode.

    Normal Mode wordt standaard gebruikt. Low Data Mode controleert alleen bij een netwerkfout op een interface. Strict Mode bepaalt de status uitsluitend op basis van een detectieopdracht naar een openbaar IP-adres.

    Gebruik Low Data Mode bij een beperkte databundel. Opnieuw verbinden kan na uitval iets langer duren dan in Normal Mode en standaard wordt alleen de Cellular-interface ingeschakeld.

- **Track Command**: gebruikt ping om de verbinding met het doel-IP te bewaken en de beschikbaarheid van de interface te bepalen. In firmware v4.3 en ouder is ook httping beschikbaar.

- **IPv4 Track IP**: hier kun je het IPv4 Track IP aanpassen.

!!! Note

    Oudere firmware, zoals v4.3, bevat instellingen zoals **Track Interval**, **Change to Failure Condition** en **Change to Available Condition**. Deze zijn sinds v4.5 vervangen door Detection Mode en Sensitivity Options.

### Gevoeligheidsopties {#sensitivity-options}

Deze functie is beschikbaar sinds v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

De gevoeligheid bepaalt het tijdsinterval voor detectie van de internetstatus.

- Gebruik bij een stabiel netwerk en toepassingen zoals video, livestreams of games een hoge gevoeligheid om bij uitval snel over te schakelen.
- Gebruik bij een instabiel netwerk en het downloaden van gecachte bestanden een lage gevoeligheid om voortdurend en onsuccesvol wisselen te voorkomen.

**Tip**: een hoge gevoeligheid kan de netwerkverbinding verbreken. Pas deze voorzichtig aan.

## Multi-WAN-modus {#multi-wan-mode}

Multi-WAN heeft twee elkaar uitsluitende modi: **Failover** en **Load Balance**.

### Failover {#failover}

Failover is de standaardmodus bij meerdere WAN-verbindingen. Als de actieve link uitvalt, schakelt de router automatisch naar een andere netwerkinterface.

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Je kunt de prioriteit van elke interface instellen. Als de gebruikte interface uitvalt, schakelt de router naar de beschikbare interface met de hoogste prioriteit. Zodra een verbinding met hogere prioriteit is hersteld, schakelt de router automatisch terug.

### Load Balance {#load-balance}

Load Balance gebruikt meerdere netwerklinks tegelijk om de bandbreedte en totale doorvoer te verhogen.

**Load Ratio** bepaalt de verdeling van nieuwe verbindingen over de interfaces volgens de ingestelde verhouding.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

Je kunt twee soorten laadverhoudingen configureren:

- **Default Load Ratio**

    Als de router tegelijk met Ethernet, Repeater, Tethering en Cellular is verbonden en alle interfaces internettoegang hebben, verdeelt Load Balance met 1:1:1:1 nieuwe verbindingen gelijkmatig over de vier interfaces.

- **Customize Load Ratio**

    Als Ethernet 200 Mbps en Repeater 100 Mbps biedt en Tethering en Cellular inactief zijn, stel je 2 in voor Ethernet, 1 voor Repeater en 0 voor Tethering/Cellular. Het systeem verdeelt nieuwe verbindingen volgens 2:1, zodat Ethernet ongeveer tweemaal zoveel verbindingen verwerkt. Dit optimaliseert de doorvoer ten opzichte van Failover.

**Opmerking:** bestaande verbindingen of verkeer volgen de verhouding niet gegarandeerd. Bij langer gebruik wordt de verdeling nauwkeuriger.

## Usage Scenarios {#usage-scenarios}

* Een kassasysteem gebruikt een bekabelde internetverbinding en Repeater naar Wi-Fi van een naburige winkel of Cellular via een simkaart als back-up, zodat mobiele betalingen bij kabeluitval doorgaan.

* Als Repeater naar openbare Wi-Fi onvoldoende snelheid biedt, kun je tegelijk Mobile Tethering met load balancing gebruiken om de totale bandbreedte te verhogen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
