# Collegare la porta 10G SFP+ di Flint 4

Flint 4 (GL‑BE14000) è dotato di una porta 10G SFP+ che può essere commutata tra le modalità WAN e LAN. La porta è compatibile con diversi tipi di moduli e cavi SFP+ per connessioni Ethernet ottiche e in rame, rispondendo a varie esigenze di rete, tra cui collegamenti in fibra a lunga distanza, cablaggio tradizionale a doppino intrecciato e terminazione avanzata della fibra PON.

Di seguito sono descritte in dettaglio le tre soluzioni di collegamento per la porta SFP+ di Flint 4 (GL-BE14000), con scenari applicativi, topologie di connessione, vantaggi e svantaggi, precauzioni e modelli compatibili riportati esclusivamente come riferimento.

## Soluzione 1. Ricetrasmettitore ottico + cavo in fibra

### 1.1 Scenari

Questa soluzione è adatta a reti Ethernet 10G a lunga distanza e ad alta stabilità. Viene utilizzata principalmente nei seguenti scenari:

- collegamento a uplink Ethernet 10G in fibra pura dell'ISP, per accesso a banda larga domestico o commerciale ad altissima velocità;  
- realizzazione di collegamenti di rete a lunga distanza, interni o esterni, ad esempio tra Flint 4 e uno switch 10G remoto, tra piani diversi di un'abitazione oppure per la dorsale di rete di un piccolo ufficio.

### 1.2 Topologia

Porta 10G SFP+ di Flint 4 → Ricetrasmettitore ottico 10G SFP+ standard (SR/MR/LR) → Cavo in fibra ottica → Switch di rete 10G remoto / terminale fibra-Ethernet dell'ISP

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Vantaggi e svantaggi

La tabella seguente valuta i principali aspetti relativi a prestazioni e facilità d'uso della soluzione con ricetrasmettitore ottico e cavo in fibra. Le valutazioni a stelle e le note dettagliate sono fornite come riferimento:

|Parametro|Valutazione|Note|
|---|---|---|
|Distanza di trasmissione|★★★★★|Supporta fino a 300 m (multimodale) o oltre 10 km (monomodale), superando i limiti di distanza dei cavi in rame ed è quindi adatta alle reti a lungo raggio.|
|Resistenza alle interferenze|★★★★★|La trasmissione del segnale ottico è immune da interferenze elettromagnetiche, elettricità statica e diafonia, garantendo un funzionamento stabile in ambienti complessi.|
|Risparmio energetico|★★★★★|Consumo energetico e produzione di calore ridotti; il design consolidato del chipset consente un funzionamento stabile a pieno carico per lunghi periodi senza rischi di surriscaldamento.|
|Compatibilità|★★★★★|Pieno supporto ufficiale e conformità ai protocolli Ethernet 10G standard, senza rischi di adattamento del firmware.|
|Facilità di installazione|★★★☆☆|Richiede conoscenze di base sulle specifiche di accoppiamento della fibra; un'installazione non corretta può causare attenuazione del segnale e richiede competenze leggermente superiori rispetto al cablaggio in rame.|
|Costo|★★★☆☆|Sono necessari ricetrasmettitori ottici e cavi in fibra aggiuntivi, con un costo complessivo superiore rispetto alle tradizionali soluzioni a doppino intrecciato.|

### 1.4 Precauzioni

- Sono supportati solo ricetrasmettitori ottici Ethernet 10G standard; i moduli ottici con protocollo PON non sono adatti a questa soluzione.

- Selezionare moduli ottici monomodali o multimodali e cavi in fibra adeguati alla distanza di trasmissione effettiva, per evitare riduzioni della velocità o interruzioni del collegamento.

- Questa soluzione supporta esclusivamente servizi ISP Ethernet 10G su fibra e non può essere collegata direttamente alle tradizionali linee in fibra residenziali GPON/XGS-PON.

### 1.5 Modelli compatibili

Di seguito sono elencati alcuni ricetrasmettitori ottici standard verificati da GL.iNet e dagli utenti come compatibili con Flint 4. L'elenco è fornito esclusivamente come riferimento.

|Modello|Tester|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Utente|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Utente|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Utente|
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
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Utente|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Utente|

## Soluzione 2. Modulo da SFP+ a RJ45 (SFP‑10G‑T)

### 2.1 Scenari

Il modulo SFP‑10G‑T converte lo slot ottico SFP+ in un'interfaccia RJ45 standard a doppino intrecciato ed è adatto a reti 10G a breve distanza basate su cavi di rete tradizionali. Tra gli impieghi tipici figurano il collegamento a breve distanza tra Flint 4 e switch 10G o dispositivi NAS, la rapida aggiunta di porte di rete 10G RJ45 senza installare nuovamente la fibra e il cablaggio LAN ad alta velocità domestico o SOHO che mantiene il tradizionale doppino intrecciato. È l'alternativa ideale per chi necessita di Ethernet 10G ma non dispone di un cablaggio in fibra.

### 2.2 Topologia

Porta 10G SFP+ di Flint 4 → Modulo da SFP+ a RJ45 (SFP‑10G‑T) → Cavo a doppino intrecciato CAT6A/CAT7 → Switch 10G / dispositivo terminale cablato 10G

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Vantaggi e svantaggi

La tabella seguente valuta i principali aspetti relativi a prestazioni e facilità d'uso della soluzione con modulo da SFP+ a RJ45 (SFP‑10G‑T). Le valutazioni a stelle e le note dettagliate sono fornite come riferimento:

|Parametro|Valutazione|Note|
|---|---|---|
|Distanza di trasmissione|★★☆☆☆|A causa dei limiti hardware del chip PHY, la distanza massima di trasmissione stabile è di soli 30 metri; la soluzione non è adatta al cablaggio a lunga distanza.|
|Resistenza alle interferenze|★★★☆☆|La tradizionale trasmissione su doppino intrecciato è soggetta a interferenze elettromagnetiche e diafonia negli scenari di cablaggio complessi.|
|Risparmio energetico|★★☆☆☆|Consumo energetico elevato e notevole produzione di calore con carichi elevati continui; per il funzionamento a lungo termine è necessario gestire la dissipazione del calore.|
|Compatibilità|★★★★☆|Compatibile con tutti i terminali RJ45 10G standard; solo i cavi CAT6A/CAT7 supportano una trasmissione 10G stabile.|
|Facilità di installazione|★★★★★|Plug-and-play, non richiede la diagnostica del percorso ottico ed è compatibile con le consuete modalità di installazione dei cavi di rete, risultando estremamente semplice da utilizzare.|
|Costo|★★★★☆|Riutilizza il cablaggio RJ45 esistente senza costi di conversione alla fibra; è sufficiente acquistare separatamente un modulo 10G-T.|

### 2.4 Precauzioni

- Per una trasmissione 10G stabile è necessario utilizzare cavi CAT6A o di categoria superiore; i cavi CAT6 o inferiori causano riduzioni della velocità e perdita di pacchetti.

- Mantenere la distanza del cablaggio entro 30 metri. Il superamento del limite può causare instabilità del collegamento, riduzione della velocità o disconnessioni.

- Lasciare spazio sufficiente per la dissipazione del calore del modulo SFP‑10G‑T, per evitare guasti dovuti al surriscaldamento.

### 2.5 Modelli compatibili

Di seguito sono elencati alcuni moduli da SFP+ a RJ45 verificati da GL.iNet e dagli utenti come compatibili con Flint 4. L'elenco è fornito esclusivamente come riferimento.

|Modello|Tester|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Utente|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Utente|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Utente|

## Soluzione 3. Modulo PON‑ONU SFP+

### 3.1 Scenari

Il modulo PON‑ONU SFP+ integra tutte le funzioni di un modem ottico ONU, consentendo alla porta SFP+ di Flint 4 di terminare direttamente le tradizionali linee in fibra residenziali GPON/XGS-PON. Questa soluzione elimina la necessità di un modem ottico esterno indipendente e riunisce in un solo dispositivo l'accesso in fibra e l'uscita instradata. È indicata per scenari di rete avanzati destinati agli utenti più esperti, in particolare per chi desidera ridurre il numero di dispositivi nella rete domestica e collegare direttamente al router le linee in fibra PON dell'operatore.

### 3.2 Topologia

Porta 10G SFP+ di Flint 4 → Modulo PON‑ONU SFP+ → Linea in fibra GPON/XGS-PON dell'ISP (inclusi cavo di derivazione, splitter PON e OLT dell'ISP)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Vantaggi e svantaggi

La tabella seguente valuta i principali aspetti relativi a prestazioni e facilità d'uso della soluzione con modulo PON‑ONU SFP+. Le valutazioni a stelle e le note dettagliate sono fornite come riferimento:

|Parametro|Valutazione|Note|
|---|---|---|
|Distanza di trasmissione|★★★★★|Supporta le distanze di trasmissione standard della fibra PON e soddisfa tutti i comuni scenari di accesso in fibra domestici e commerciali.|
|Resistenza alle interferenze|★★★★★|La trasmissione in fibra ottica offre un'elevata resistenza alle interferenze e un segnale stabile, in linea con i principali standard di accesso in fibra PON.|
|Risparmio energetico|★★☆☆☆|Durante il funzionamento ad alta velocità viene generato molto calore; è obbligatoria una dissipazione ausiliaria per evitare riduzioni delle prestazioni e disconnessioni.|
|Compatibilità|★★☆☆☆|Soluzione per utenti esperti verificata in modo non ufficiale; la compatibilità dipende dalla whitelist dell'ISP e dal modello del modulo, mentre il funzionamento a lungo termine potrebbe non essere stabile.|
|Facilità di installazione|★★☆☆☆|Richiede la conferma preventiva dell'ISP, la configurazione dell'autenticazione SN/PLOAM e l'ottimizzazione della dissipazione del calore; la complessità complessiva dell'installazione è elevata.|
|Costo|★★★☆☆|Elimina il costo di un modem ottico indipendente, ma comporta potenziali rischi per i servizi, ad esempio l'indisponibilità di IPTV o telefonia e l'assenza di assistenza tecnica ufficiale.|

### 3.4 Precauzioni

- **Verificare preventivamente l'autorizzazione dell'ISP**: chiedere all'operatore se è consentito collegare alla rete PON hardware ONU di terze parti di proprietà dell'utente e ottenere i parametri di autenticazione obbligatori, inclusi il codice di registrazione SN e la password PLOAM.

- **La dissipazione del calore è obbligatoria**: dotare il modulo PON‑ONU di sistemi ausiliari di dissipazione per evitare riduzioni della frequenza, perdita di pacchetti e disconnessioni dovute alle alte temperature.

- **Nessuna garanzia del servizio**: GL.iNet non fornisce assistenza tecnica per questa soluzione. Problemi quali instabilità della rete, variazioni della velocità e anomalie dei servizi a valore aggiunto non possono essere risolti tramite firmware ufficiale o assistenza post-vendita.

- Ogni operatore applica regole diverse per la whitelist dei modelli. Prima dell'acquisto, verificare quali moduli PON sono supportati dall'operatore.

### 3.5 Modelli compatibili

Di seguito sono elencati alcuni moduli PON-ONU SFP+ verificati da GL.iNet e dagli utenti come compatibili con Flint 4. L'elenco è fornito esclusivamente come riferimento.

|Modello|Tester|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Utente|

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
