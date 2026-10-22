# De 10G SFP+-poort op Flint 4 aansluiten {#connecting-the-10g-sfp-port-on-flint-4}

Flint 4 (GL-BE14000) heeft een 10G SFP+-poort die als WAN of LAN kan werken. De poort ondersteunt verschillende SFP+-modules en kabels voor glasvezel- en koperen Ethernetverbindingen, waaronder lange glasvezelverbindingen, twisted-pairbekabeling en geavanceerde PON-glasvezelterminatie.

Dit artikel beschrijft drie aansluitmogelijkheden voor de SFP+-poort van Flint 4 (GL-BE14000), met toepassingen, topologieën, voor- en nadelen, voorzorgsmaatregelen en compatibele modellen.

## Solution 1. Optical Transceiver + Fiber Cable {#solution-1-optical-transceiver-fiber-cable}

### 1.1 Scenarios {#11-scenarios}

Deze oplossing is bedoeld voor betrouwbare 10G-Ethernetverbindingen over lange afstanden. Typische toepassingen zijn:

- Connecting to an ISP's 10G fiber Ethernet uplink for high-speed residential or commercial broadband access.
- Deploying long-distance indoor or outdoor network links, such as connecting Flint 4 to a remote 10G switch, cabling between floors in a home, or deploying a small-office backbone network.

### 1.2 Topology {#12-topology}

Flint 4 10G SFP+ port → Standard 10G SFP+ optical transceiver (SR/MR/LR) → Fiber-optic cable → Remote 10G network switch / ISP fiber Ethernet terminal

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Voor- en nadelen {#13-pros-and-cons}

De onderstaande tabel beoordeelt prestaties en gebruiksgemak van de optische transceiver met glasvezelkabel aan de hand van sterren en opmerkingen:

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmission Distance|★★★★★|Supports distances of up to 300 m over multimode fiber or more than 10 km over single-mode fiber, making it suitable for long-range connections.|
|Interference Resistance|★★★★★|Fiber-optic transmission is immune to electromagnetic interference, static electricity, and crosstalk, ensuring stable operation in complex environments.|
|Energy Efficiency|★★★★★|Offers low power consumption and heat output. Its mature chipset design supports stable, long-term operation under full load without overheating.|
|Compatibiliteit|★★★★★|Officieel ondersteund en compatibel met standaard 10G-Ethernetprotocollen; geen firmwareaanpassing nodig.|
|Ease of Deployment|★★★☆☆|Requires knowledge of basic fiber connection requirements. Improper handling may cause signal attenuation, so deployment is more complex than with copper cabling.|
|Cost|★★★☆☆|Requires additional optical transceivers and fiber cables, resulting in a higher overall cost than traditional twisted-pair solutions.|

### 1.4 Precautions {#14-precautions}

- PON-modules kunnen niet met deze optie worden gebruikt.

- Kies singlemode- of multimode-optische modules en glasvezelkabels die bij de vereiste afstand passen om lagere snelheden of verbindingsuitval te voorkomen.

- Deze optie ondersteunt alleen 10G Ethernet-over-fiber van de internetprovider en kan niet rechtstreeks met traditionele GPON/XGS-PON-thuisverbindingen worden verbonden.

### 1.5 Compatible Models {#15-compatible-models}

De volgende standaard optische transceivers zijn door GL.iNet of communityleden getest en compatibel bevonden met Flint 4. De lijst is alleen bedoeld als referentie.

|Model|Tester|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Community member|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Community member|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Community member|
|XZSNET SFP10G-SR|GL.iNet|
|10Gtek AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|10Gtek AZS85-192-M1 25G SFP28-SR 850nm 100m|GL.iNet|
|10Gtek ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|10Gtek ASF85-24-X2-D 1.25G SFP-SX 850nm 550m|GL.iNet|
|FS Cisco SFP-10G-SR Compatible 10GBASE-SR|GL.iNet|
|FS Juniper EX-SFP-10GE-SR 10GBASE-SR SFP+|GL.iNet|
|FS Arista SFP-10G-SR 10GBASE-SR SFP+|GL.iNet|
|FS Brocade 10G-SFPP-SR 10GBASE-SR SFP+|GL.iNet|
|HUAWEI 6G-850nm-120m-MM-SFP+ MTRS-6A11-01|GL.iNet|
|HUAWEI 2.5G-1310nm-SM-ESFP MXPD-483II|GL.iNet|
|netLINK 10G/850nm/300m/DDM HTB-10G-SR|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Community member|

## Solution 2. SFP+ to RJ45 Module (SFP-10G-T) {#solution-2-sfp-to-rj45-module-sfp-10g-t}

### 2.1 Scenarios {#21-scenarios}

De SFP-10G-T-module zet de SFP+-sleuf om in een standaard RJ45-interface voor twisted pair. Dit is geschikt voor korte 10G-netwerken met gewone Ethernetkabels, bijvoorbeeld voor een nabijgelegen 10G-switch of NAS, een extra 10G-RJ45-poort zonder glasvezel of een snel thuis- of SOHO-LAN met bestaande bekabeling. Deze optie is geschikt als je 10G Ethernet nodig hebt maar geen glasvezelbekabeling hebt.

### 2.2 Topology {#22-topology}

Flint 4 10G SFP+ port → SFP+ to RJ45 module (SFP-10G-T) → CAT6A/CAT7 twisted-pair cable → 10G switch / 10G wired terminal device

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Voor- en nadelen {#23-pros-and-cons}

De onderstaande tabel beoordeelt prestaties en gebruiksgemak van de SFP+-naar-RJ45-module (SFP-10G-T):

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmissieafstand|★★☆☆☆|De PHY beperkt de stabiele afstand tot 30 m; de module is niet geschikt voor lange kabeltrajecten.|
|Storingsbestendigheid|★★★☆☆|Twisted-pairverbindingen kunnen in complexe bekabelingsomgevingen gevoelig zijn voor elektromagnetische interferentie en overspraak.|
|Energie-efficiëntie|★★☆☆☆|Gebruikt meer stroom en produceert bij langdurige hoge belasting veel warmte. Voor langdurig gebruik is goede koeling vereist.|
|Compatibiliteit|★★★★☆|Compatibel met standaard 10G-RJ45-apparaten. CAT6A- of CAT7-bekabeling is vereist voor stabiele 10G-transmissie.|
|Implementatiegemak|★★★★★|Plug-and-play zonder configuratie van een optisch pad en geschikt voor gewone Ethernetbekabeling.|
|Cost|★★★★☆|Can reuse existing RJ45 cabling without installing fiber, although a separate 10GBASE-T module is required.|

### 2.4 Precautions {#24-precautions}

- Use CAT6A or higher-category Ethernet cables for stable 10G transmission. Lower-category cables may reduce speeds or cause packet loss.

- Keep the cable length within 30 m. Longer cables may cause link instability, reduced speeds, or disconnections.

- Provide adequate airflow around the SFP-10G-T module to prevent failures caused by overheating.

### 2.5 Compatible Models {#25-compatible-models}

De volgende SFP+-naar-RJ45-modules zijn door GL.iNet of communityleden getest en compatibel bevonden met Flint 4. De lijst is alleen bedoeld als referentie.

|Model|Tester|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Community member|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Community member|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Community member|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Community member|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|

## Solution 3. PON-ONU SFP+ Stick {#solution-3-pon-onu-sfp-stick}

### 3.1 Scenarios {#31-scenarios}

De PON-ONU SFP+-stick werkt als optische ONU-modem, zodat de SFP+-poort van Flint 4 traditionele GPON/XGS-PON-thuisverbindingen rechtstreeks kan termineren. Glasvezeltoegang en routering worden in één apparaat gecombineerd, zonder externe optische modem. Deze geavanceerde optie is bedoeld voor ervaren gebruikers die minder apparaten willen gebruiken en de router rechtstreeks met de PON-lijn van hun provider willen verbinden.

### 3.2 Topology {#32-topology}

Flint 4 10G SFP+ port → PON-ONU SFP+ stick → ISP GPON/XGS-PON fiber line (including drop cable, PON splitter, and ISP OLT)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Voor- en nadelen {#33-pros-and-cons}

De onderstaande tabel beoordeelt prestaties en gebruiksgemak van de PON-ONU SFP+-stick:

|Metric|Star Rating|Remarks|
|---|---|---|
|Transmissieafstand|★★★★★|Ondersteunt standaard PON-afstanden voor thuis- en normale zakelijke glasvezeltoegang.|
|Storingsbestendigheid|★★★★★|Glasvezel biedt sterke storingsbestendigheid en signaalstabiliteit volgens gangbare PON-standaarden.|
|Energy Efficiency|★★☆☆☆|Generates significant heat during high-speed operation. Auxiliary cooling is required to avoid performance degradation and disconnections.|
|Compatibiliteit|★★☆☆☆|Dit is een onofficiële oplossing voor gevorderden. Compatibiliteit hangt af van de acceptatielijst van de provider en het stickmodel; langdurig gebruik kan instabiel zijn.|
|Implementatiegemak|★★☆☆☆|Vereist voorafgaande bevestiging van de provider, SN/PLOAM-verificatie en voldoende koeling. De implementatie is relatief complex.|
|Kosten|★★★☆☆|Bespaart een aparte optische modem, maar kan IPTV en telefonie beïnvloeden en omvat geen officiële technische ondersteuning.|

### 3.4 Precautions {#34-precautions}

- **Vraag vooraf toestemming aan de provider**: vraag of eigen ONU-hardware van derden op het PON-netwerk is toegestaan en verkrijg de vereiste verificatieparameters, waaronder de SN-registratiecode en het PLOAM-wachtwoord.

- **Koeling is verplicht**: koel de PON-ONU-stick om prestatieverlies, pakketverlies en verbroken verbindingen door hoge temperaturen te voorkomen.

- **Geen servicegarantie**: GL.iNet biedt geen technische ondersteuning voor deze optie. Netwerkinstabiliteit, snelheidsvariaties en problemen met aanvullende diensten vallen niet onder officiële firmware- of aftersalesondersteuning.

- Regels voor acceptatielijsten verschillen per provider. Controleer vóór aankoop welke PON-stickmodellen worden ondersteund.

### 3.5 Compatible Models {#35-compatible-models}

De volgende PON-ONU SFP+-sticks zijn door GL.iNet of communityleden getest en compatibel bevonden met Flint 4. De lijst is alleen bedoeld als referentie.

|Model|Tester|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Community member|

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
