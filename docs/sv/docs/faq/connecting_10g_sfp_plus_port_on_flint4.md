# Ansluta 10G SFP+-porten på Flint 4 {#connecting-the-10g-sfp-port-on-flint-4}

Flint 4 (GL-BE14000) har en 10G SFP+-port som kan användas i WAN- eller LAN-läge. Porten stöder flera typer av SFP+-moduler och kablar för fiberoptiska Ethernet-anslutningar och Ethernet-anslutningar med koppar, bland annat fiberlänkar över långa avstånd, vanliga kablar med tvinnade par och avancerad PON-fiberterminering.

Artikeln beskriver tre anslutningsalternativ för SFP+-porten på Flint 4 (GL-BE14000), inklusive användningsområden, anslutningstopologier, fördelar och nackdelar, försiktighetsåtgärder och kompatibla modeller.

## Lösning 1. Optisk transceiver + fiberkabel {#solution-1-optical-transceiver-fiber-cable}

### 1.1 Scenarier {#11-scenarios}

Lösningen är avsedd för tillförlitliga 10G Ethernet-anslutningar över långa avstånd. Vanliga användningsområden är:

- Anslutning till internetleverantörens 10G Ethernet-upplänk via fiber för bredbandsåtkomst med hög hastighet i bostäder eller företag.
- Nätverkslänkar över långa avstånd inomhus eller utomhus, till exempel anslutning av Flint 4 till en avlägsen 10G-switch, kabeldragning mellan våningar i en bostad eller installation av ett stamnät på ett mindre kontor.

### 1.2 Topologi {#12-topology}

Flint 4 10G SFP+-port → Standardmässig optisk 10G SFP+-transceiver (SR/MR/LR) → Fiberoptisk kabel → Avlägsen 10G-nätverksswitch/internetleverantörens fiber-Ethernet-terminal

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Fördelar och nackdelar {#13-pros-and-cons}

Tabellen nedan bedömer viktiga prestanda- och användbarhetsaspekter för alternativet med optisk transceiver och fiberkabel. Stjärnbetyg och detaljerade anmärkningar anges som referens:

|Mått|Stjärnbetyg|Anmärkningar|
|---|---|---|
|Överföringsavstånd|★★★★★|Stöder avstånd upp till 300 m via multimodefiber eller mer än 10 km via singlemodefiber, vilket lämpar sig för anslutningar över långa avstånd.|
|Störningstålighet|★★★★★|Fiberoptisk överföring påverkas inte av elektromagnetiska störningar, statisk elektricitet eller överhörning och ger stabil drift i komplicerade miljöer.|
|Energieffektivitet|★★★★★|Har låg strömförbrukning och värmeutveckling. Den väl beprövade kretsdesignen ger stabil långvarig drift med full belastning utan överhettning.|
|Kompatibilitet|★★★★★|Stöds officiellt och följer standardprotokollen för 10G Ethernet. Ingen anpassning av firmware krävs.|
|Enkel installation|★★★☆☆|Kräver kunskap om grundläggande krav för fiberanslutningar. Felaktig hantering kan dämpa signalen, så installationen är mer komplicerad än med kopparkabel.|
|Kostnad|★★★☆☆|Kräver ytterligare optiska transceivrar och fiberkablar, vilket ger en högre totalkostnad än traditionella lösningar med tvinnade par.|

### 1.4 Försiktighetsåtgärder {#14-precautions}

- PON-moduler kan inte användas med det här alternativet.

- Välj lämpliga optiska singlemode- eller multimodemoduler och fiberkablar för det nödvändiga överföringsavståndet så att nätverkshastigheten inte sjunker och länken inte slutar fungera.

- Alternativet stöder endast internetleverantörers 10G Ethernet-tjänster via fiber och kan inte anslutas direkt till traditionella GPON-/XGS-PON-fiberledningar för bostäder.

### 1.5 Kompatibla modeller {#15-compatible-models}

Följande optiska standardtransceivrar har testats av GL.iNet eller communitymedlemmar och konstaterats vara kompatibla med Flint 4. Listan är endast avsedd som referens.

|Modell|Testare|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Communitymedlem|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Communitymedlem|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Communitymedlem|
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
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Communitymedlem|

## Lösning 2. SFP+-till-RJ45-modul (SFP-10G-T) {#solution-2-sfp-to-rj45-module-sfp-10g-t}

### 2.1 Scenarier {#21-scenarios}

SFP-10G-T-modulen omvandlar SFP+-platsen till ett vanligt RJ45-gränssnitt för tvinnade par och lämpar sig därför för 10G-nätverk över korta avstånd som använder vanliga Ethernet-kablar. Vanliga användningsområden är anslutning av Flint 4 till en närliggande 10G-switch eller NAS, tillägg av en 10G RJ45-port utan installation av fiber och uppbyggnad av ett snabbt hem- eller SOHO-LAN med befintliga kablar med tvinnade par. Alternativet passar användare som behöver 10G Ethernet men saknar fiberkablage.

### 2.2 Topologi {#22-topology}

Flint 4 10G SFP+-port → SFP+-till-RJ45-modul (SFP-10G-T) → CAT6A-/CAT7-kabel med tvinnade par → 10G-switch/trådbunden 10G-slutenhet

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Fördelar och nackdelar {#23-pros-and-cons}

Tabellen nedan bedömer viktiga prestanda- och användbarhetsaspekter för alternativet med en SFP+-till-RJ45-modul (SFP-10G-T). Stjärnbetyg och detaljerade anmärkningar anges som referens:

|Mått|Stjärnbetyg|Anmärkningar|
|---|---|---|
|Överföringsavstånd|★★☆☆☆|PHY begränsar det stabila överföringsavståndet till 30 m, vilket gör modulen olämplig för kabeldragning över långa avstånd.|
|Störningstålighet|★★★☆☆|Anslutningar med tvinnade par kan påverkas av elektromagnetiska störningar och överhörning i komplicerade kabelmiljöer.|
|Energieffektivitet|★★☆☆☆|Förbrukar mer ström och utvecklar mycket värme vid långvarig hög belastning. Tillräcklig kylning krävs för långvarig drift.|
|Kompatibilitet|★★★★☆|Kompatibel med vanliga 10G RJ45-enheter. CAT6A- eller CAT7-kablage krävs för stabil 10G-överföring.|
|Enkel installation|★★★★★|Kan installeras med plug-and-play utan konfiguration av en optisk väg och fungerar med vanligt Ethernet-kablage.|
|Kostnad|★★★★☆|Befintligt RJ45-kablage kan återanvändas utan installation av fiber, men en separat 10GBASE-T-modul krävs.|

### 2.4 Försiktighetsåtgärder {#24-precautions}

- Använd Ethernet-kablar av typen CAT6A eller högre för stabil 10G-överföring. Kablar av lägre kategori kan sänka hastigheten eller orsaka paketförlust.

- Håll kabellängden inom 30 m. Längre kablar kan göra länken instabil, sänka hastigheten eller orsaka frånkopplingar.

- Se till att luftflödet runt SFP-10G-T-modulen är tillräckligt för att förhindra fel som orsakas av överhettning.

### 2.5 Kompatibla modeller {#25-compatible-models}

Följande SFP+-till-RJ45-moduler har testats av GL.iNet eller communitymedlemmar och konstaterats vara kompatibla med Flint 4. Listan är endast avsedd som referens.

|Modell|Testare|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Communitymedlem|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Communitymedlem|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Communitymedlem|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Communitymedlem|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|

## Lösning 3. PON-ONU SFP+-sticka {#solution-3-pon-onu-sfp-stick}

### 3.1 Scenarier {#31-scenarios}

En PON-ONU SFP+-sticka har funktionerna hos ett optiskt ONU-modem och gör att SFP+-porten på Flint 4 kan terminera traditionella GPON-/XGS-PON-fiberledningar för bostäder direkt. Alternativet eliminerar behovet av ett separat externt optiskt modem genom att kombinera fiberåtkomst och routning i en enhet. Det är avsett för avancerade installationer på entusiastnivå, särskilt för användare som vill minska antalet enheter i hemnätverket och ansluta routern direkt till internetleverantörens PON-fiberledning.

### 3.2 Topologi {#32-topology}

Flint 4 10G SFP+-port → PON-ONU SFP+-sticka → Internetleverantörens GPON-/XGS-PON-fiberledning (inklusive anslutningskabel, PON-splitter och internetleverantörens OLT)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Fördelar och nackdelar {#33-pros-and-cons}

Tabellen nedan bedömer viktiga prestanda- och användbarhetsaspekter för alternativet med en PON-ONU SFP+-sticka. Stjärnbetyg och detaljerade anmärkningar anges som referens:

|Mått|Stjärnbetyg|Anmärkningar|
|---|---|---|
|Överföringsavstånd|★★★★★|Stöder vanliga PON-överföringsavstånd för fiberåtkomst i bostäder och vanliga företagsmiljöer.|
|Störningstålighet|★★★★★|Fiberoptisk överföring ger god störningstålighet och signalstabilitet i enlighet med vanliga standarder för PON-fiberåtkomst.|
|Energieffektivitet|★★☆☆☆|Utvecklar mycket värme vid drift med hög hastighet. Extra kylning krävs för att undvika försämrade prestanda och frånkopplingar.|
|Kompatibilitet|★★☆☆☆|Detta är en inofficiell lösning för entusiaster. Kompatibiliteten beror på internetleverantörens tillåtelselista och stickans modell, och långvarig drift kan vara instabil.|
|Enkel installation|★★☆☆☆|Kräver förhandsbekräftelse från internetleverantören, konfiguration av SN-/PLOAM-autentisering och tillräcklig kylning. Installationen är relativt komplicerad.|
|Kostnad|★★★☆☆|Eliminerar kostnaden för ett separat optiskt modem men kan påverka tjänster som IPTV och telefoni och omfattas inte av officiell teknisk support.|

### 3.4 Försiktighetsåtgärder {#34-precautions}

- **Bekräfta internetleverantörens tillstånd i förväg**: Fråga internetleverantören om egen ONU-maskinvara från tredje part är tillåten i PON-nätverket och hämta de autentiseringsparametrar som krävs, inklusive SN-registreringskoden och PLOAM-lösenordet.

- **Värmeavledning är obligatorisk**: Ge PON-ONU-stickan extra kylning för att förhindra försämrade prestanda, paketförlust och frånkopplingar som orsakas av höga temperaturer.

- **Ingen tjänstegaranti**: GL.iNet ger ingen teknisk support för det här alternativet. Problem som instabilt nätverk, hastighetsvariationer eller problem med tilläggstjänster omfattas inte av officiell firmware eller kundsupport.

- Reglerna för tillåtelselistor varierar mellan internetleverantörer. Kontrollera vilka PON-stickmodeller internetleverantören stöder före köpet.

### 3.5 Kompatibla modeller {#35-compatible-models}

Följande PON-ONU SFP+-stickor har testats av GL.iNet eller communitymedlemmar och konstaterats vara kompatibla med Flint 4. Listan är endast avsedd som referens.

|Modell|Testare|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Communitymedlem|

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
