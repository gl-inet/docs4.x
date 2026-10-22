# Förstå externa mobilantenner {#understanding-external-cellular-antennas}

Externa mobilantenner kan förbättra mobilanslutningens kvalitet i vissa situationer, men de garanterar inte högre nedladdnings- eller uppladdningshastighet.

Den här guiden förklarar när en extern antenn kan hjälpa, hur du väljer en kompatibel antenn och vilka faktorer som påverkar mobilnätets prestanda.

## När bör jag använda en extern antenn? {#when-should-i-use-an-external-antenna}

En extern antenn kan förbättra anslutningen om routern finns på en plats där mobilsignalen försvagas innan den når enheten, till exempel i husbilar, fordon, källare, byggnader med betong-, tegel- eller metallväggar, teknikrum, nätverksskåp eller glesbygdsområden med svag täckning.

Innan du köper en antenn bör du prova att flytta routern närmare ett fönster eller högre upp. Enbart en bättre placering kan ofta förbättra signalkvaliteten avsevärt.

## När hjälper inte en extern antenn? {#when-wont-an-external-antenna-help}

En extern antenn löser inte alla problem med mobilanslutningar. Förbättringen kan bli liten eller utebli om routern redan har stark signal, mobilmasten är överbelastad, operatören begränsar hastigheten, antennen inte stöder operatörens frekvensband, långa kablar orsakar stor signalförlust eller antennen placeras nästan på samma plats som routerns interna antenner.

En starkare signal innebär inte alltid högre internethastighet.

## Välja rätt antenn {#choosing-the-right-antenna}

Kontrollera före köpet att kontakttypen passar routern, att antennen stöder operatörens mobilfrekvensband, att den är avsedd för LTE, 5G eller båda beroende på router och att den passar installationsmiljön, till exempel inomhus, i fordon eller utomhus. Rätt kontakttyp anges i routerns produktdokumentation.

## Förstå MIMO {#understanding-mimo}

De flesta moderna LTE- och 5G-nät använder **Multiple Input Multiple Output (MIMO)** för högre kapacitet och tillförlitligare anslutning. Många GL.iNet-mobilroutrar har flera mobilantennportar för MIMO.

Anslut alla nödvändiga antennkablar, använd en kompatibel MIMO-antenn när det är möjligt och följ tillverkarens rekommendationer om avstånd och riktning. Om du bara använder en antenn på en router som är avsedd för flera antenner kan prestandan försämras.

## Antennförstärkning och kabelförlust {#antenna-gain-and-cable-loss}

Antennförstärkning mäts vanligtvis i **dBi**. Högre förstärkning ger inte alltid bättre prestanda. Antenner med högre förstärkning är ofta mer riktade och passar fasta installationer där mobilmastens position är känd.

Varje antennkabel dämpar signalen innan den når routern. Använd därför kortast praktiska kabel, undvik onödiga adaptrar och använd koaxialkabel med låg förlust för längre sträckor.

## Rundstrålande och riktade antenner {#omnidirectional-vs-directional-antennas}

### Rundstrålande antenner {#omnidirectional-antennas}

Rundstrålande antenner tar emot signaler från alla riktningar. De rekommenderas vanligtvis för fordon, husbilar, mobila installationer och områden med flera närliggande master.

### Riktade antenner {#directional-antennas}

Riktade antenner koncentrerar mottagningen åt ett visst håll. De rekommenderas när routern står kvar på samma plats, mobilmasten är känd, täckningen är svag eller högsta möjliga signalkvalitet krävs. De måste riktas in noggrant.

## Mäta förbättringen {#measuring-improvement}

Förlita dig inte enbart på signalstaplarna i routerns gränssnitt. Jämför RSRP (signalstyrka), RSRQ (signalkvalitet), SINR (signal-brus- och störningsförhållande), anslutet LTE- eller 5G-band och status för operatörsaggregering före och efter installationen.

Kör flera hastighetstester under liknande förhållanden eftersom mobilnätets prestanda varierar naturligt under dagen.

## Vanliga frågor {#frequently-asked-questions}

### Kan jag använda vilken mobilantenn som helst? {#can-i-use-any-cellular-antenna}

Nej. Antennen måste ha rätt kontakttyp och stödja de mobilfrekvensband som routern och operatören använder.

### Bör jag köpa antennen med högst förstärkning? {#should-i-buy-the-highest-gain-antenna-available}

Inte nödvändigtvis. Välj en antenn som passar installationen och bedöm den inte enbart efter angiven förstärkning.

### Ökar en extern antenn alltid internethastigheten? {#will-an-external-antenna-always-increase-my-internet-speed}

Nej. Prestandan beror bland annat på signalkvalitet, operatörsaggregering, belastning på masten, nätverksförhållanden och operatören.

### Används de interna mobilantennerna fortfarande när externa antenner är anslutna? {#will-the-internal-cellular-antennas-still-be-used-when-external-antennas-are-connected}

Nej. När kompatibla externa antenner ansluts till en GL.iNet-mobilrouters externa mobilantennportar inaktiveras motsvarande interna mobilantenner.

Anslut alla nödvändiga externa antennkablar. Om bara en kabel ansluts till en router som är avsedd för flera mobilantenner kan MIMO-prestandan och anslutningens kvalitet försämras.

### Kan jag ansluta en Wi-Fi-antenn till en mobilantennport? {#can-i-connect-a-wi-fi-antenna-to-a-cellular-antenna-port}

Nej. Wi-Fi- och mobilantenner är konstruerade för olika radiosystem och kan inte användas i stället för varandra.

---

## Relaterade guider {#related-tutorials}

- [Installera eller byt externa antenner](how_to_install_or_change_antennas.md)
- [Kontrollera status för operatörsaggregering](how_to_check_carrier_aggregation.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com) eller [kontakta oss](https://www.gl-inet.com/contact-us).
