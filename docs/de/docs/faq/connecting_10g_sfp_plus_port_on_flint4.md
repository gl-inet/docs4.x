# 10G-SFP+-Port am Flint 4 anschließen

Flint 4 (GL‑BE14000) verfügt über einen 10G-SFP+-Port, der zwischen WAN- und LAN-Modus umgeschaltet werden kann. Dieser Port ist mit verschiedenen SFP+-Modulen und Kabeln für optische und kupferbasierte Ethernet-Verbindungen kompatibel. Dadurch eignet er sich für unterschiedliche Netzwerkanforderungen, darunter Glasfaserverbindungen über große Entfernungen, herkömmliche Twisted-Pair-Verkabelung und moderne PON-Glasfaserabschlüsse.

Nachfolgend werden die drei Verbindungslösungen für den SFP+-Port des Flint 4 (GL-BE14000) ausführlich beschrieben. Die Angaben zu Anwendungsszenarien, Verbindungstopologien, Vor- und Nachteilen, Vorsichtsmaßnahmen und kompatiblen Modellen dienen lediglich als Referenz.

## Lösung 1: Optischer Transceiver und Glasfaserkabel

### 1.1 Anwendungsszenarien

Diese Lösung eignet sich für stabile 10G-Ethernet-Netzwerke über große Entfernungen. Sie wird hauptsächlich in zwei Szenarien eingesetzt:

- Verbindung mit einem reinen 10G-Glasfaser-Ethernet-Uplink des Internetanbieters für besonders schnelle private und gewerbliche Breitbandzugänge;
- Einrichtung weitreichender Netzwerkverbindungen im Innen- und Außenbereich, beispielsweise zwischen Flint 4 und einem entfernten 10G-Switch, zur Verkabelung eines Heimnetzwerks über mehrere Etagen oder zum Aufbau des Backbone-Netzwerks eines kleinen Büros.

### 1.2 Topologie

10G-SFP+-Port des Flint 4 → Standardmäßiger optischer 10G-SFP+-Transceiver (SR/MR/LR) → Glasfaserkabel → Entfernter 10G-Netzwerk-Switch/Glasfaser-Ethernet-Terminal des Internetanbieters

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Vor- und Nachteile

Die folgende Tabelle bewertet wichtige Leistungs- und Benutzerfreundlichkeitsmerkmale der Lösung mit optischem Transceiver und Glasfaserkabel. Die Sternebewertungen und Hinweise dienen als Referenz:

|Kriterium|Sternebewertung|Anmerkungen|
|---|---|---|
|Übertragungsentfernung|★★★★★|Unterstützt bis zu 300 m (Multimode) bzw. mehr als 10 km (Singlemode), überwindet damit die Entfernungsgrenzen von Kupferkabeln und eignet sich für weitreichende Netzwerke.|
|Störfestigkeit|★★★★★|Die optische Signalübertragung ist unempfindlich gegenüber elektromagnetischen Störungen, statischer Elektrizität und Übersprechen und gewährleistet einen stabilen Betrieb in komplexen Umgebungen.|
|Energieeffizienz|★★★★★|Geringer Stromverbrauch und geringe Wärmeentwicklung; das ausgereifte Chipdesign ermöglicht einen stabilen Dauerbetrieb unter Volllast ohne Überhitzungsrisiko.|
|Kompatibilität|★★★★★|Wird offiziell vollständig unterstützt, entspricht den standardmäßigen 10G-Ethernet-Protokollen und birgt kein Risiko hinsichtlich der Firmwareanpassung.|
|Einfache Bereitstellung|★★★☆☆|Grundkenntnisse zu den Glasfaser-Anschlussspezifikationen sind erforderlich. Unsachgemäße Handhabung kann zu Signaldämpfung führen, weshalb die Anforderungen etwas höher als bei Kupferverkabelung sind.|
|Wirtschaftlichkeit|★★★☆☆|Zusätzliche optische Transceiver und Glasfaserkabel sind erforderlich; die Gesamtkosten liegen über denen herkömmlicher Twisted-Pair-Lösungen.|

### 1.4 Vorsichtsmaßnahmen

- Es werden nur standardmäßige optische 10G-Ethernet-Transceiver unterstützt. Optische Module mit PON-Protokoll sind für diese Lösung nicht geeignet.

- Wählen Sie anhand der tatsächlichen Übertragungsentfernung zueinander passende Singlemode-/Multimode-Module und Glasfaserkabel, um eine Verringerung der Netzwerkgeschwindigkeit oder einen Verbindungsfehler zu vermeiden.

- Diese Lösung unterstützt ausschließlich 10G-Ethernet-over-Fiber-Dienste des Internetanbieters. Eine direkte Verbindung mit herkömmlichen GPON-/XGS-PON-Glasfaseranschlüssen für Privathaushalte ist nicht möglich.

### 1.5 Kompatible Modelle

Die folgenden standardmäßigen optischen Transceiver wurden von GL.iNet und Community-Nutzern getestet und sind mit Flint 4 kompatibel. Die Liste dient lediglich als Referenz.

|Modell|Tester|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Community-Nutzer|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Community-Nutzer|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Community-Nutzer|
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
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Community-Nutzer|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Community-Nutzer|

## Lösung 2: SFP+-zu-RJ45-Modul (SFP‑10G‑T)

### 2.1 Anwendungsszenarien

Das SFP‑10G‑T-Modul wandelt den optischen SFP+-Steckplatz in eine standardmäßige RJ45-Twisted-Pair-Schnittstelle um. Es eignet sich für 10G-Netzwerke über kurze Entfernungen mit herkömmlichen Netzwerkkabeln. Typische Anwendungen sind kurze Verbindungen zwischen Flint 4 und 10G-Switches oder NAS-Geräten, die schnelle Erweiterung um 10G-RJ45-Netzwerkports ohne neue Glasfaserverkabelung sowie schnelle Heim- und SOHO-Netzwerke, die weiterhin eine herkömmliche Twisted-Pair-Verkabelung verwenden. Für Benutzer, die 10G-Ethernet benötigen, aber keine Glasfaserverkabelung nutzen können, ist dies die beste Alternative.

### 2.2 Topologie

10G-SFP+-Port des Flint 4 → SFP+-zu-RJ45-Modul (SFP‑10G‑T) → CAT6A-/CAT7-Twisted-Pair-Kabel → 10G-Switch/10G-Endgerät mit Kabelverbindung

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Vor- und Nachteile

Die folgende Tabelle bewertet wichtige Leistungs- und Benutzerfreundlichkeitsmerkmale der Lösung mit einem SFP+-zu-RJ45-Modul (SFP‑10G‑T). Die Sternebewertungen und Hinweise dienen als Referenz:

|Kriterium|Sternebewertung|Anmerkungen|
|---|---|---|
|Übertragungsentfernung|★★☆☆☆|Aufgrund der PHY-Chip-Hardware ist die stabile Übertragungsentfernung auf höchstens 30 Meter begrenzt. Die Lösung eignet sich nicht für weitreichende Verkabelungen.|
|Störfestigkeit|★★★☆☆|Die herkömmliche Twisted-Pair-Übertragung ist bei komplexen Verkabelungen anfällig für elektromagnetische Störungen und Übersprechen.|
|Energieeffizienz|★★☆☆☆|Hoher Stromverbrauch und deutliche Wärmeentwicklung bei anhaltend hoher Last; für den Dauerbetrieb ist ein Wärmemanagement erforderlich.|
|Kompatibilität|★★★★☆|Mit allen standardmäßigen 10G-RJ45-Endgeräten kompatibel; nur CAT6A-/CAT7-Kabel unterstützen eine stabile 10G-Übertragung.|
|Einfache Bereitstellung|★★★★★|Plug-and-play, keine Einrichtung des optischen Pfads erforderlich und mit den üblichen Verfahren zur Netzwerkkabelverlegung kompatibel; besonders einfache Handhabung.|
|Wirtschaftlichkeit|★★★★☆|Die vorhandene RJ45-Verkabelung kann weiterverwendet werden und muss nicht durch Glasfaser ersetzt werden. Lediglich ein 10G-T-Modul muss separat erworben werden.|

### 2.4 Vorsichtsmaßnahmen

- Für eine stabile 10G-Übertragung müssen Netzwerkkabel der Kategorie CAT6A oder höher verwendet werden. CAT6-Kabel und niedrigere Kategorien führen zu Geschwindigkeitseinbußen und Paketverlusten.

- Begrenzen Sie die Kabellänge auf 30 Meter. Bei Überschreitung dieses Grenzwerts kann die Verbindung instabil werden, langsamer werden oder abbrechen.

- Lassen Sie um das SFP‑10G‑T-Modul ausreichend Raum zur Wärmeableitung, um einen Geräteausfall durch Überhitzung zu vermeiden.

### 2.5 Kompatible Modelle

Die folgenden SFP+-zu-RJ45-Module wurden von GL.iNet und Community-Nutzern getestet und sind mit Flint 4 kompatibel. Die Liste dient lediglich als Referenz.

|Modell|Tester|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Community-Nutzer|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Community-Nutzer|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Community-Nutzer|

## Lösung 3: PON‑ONU-SFP+-Stick

### 3.1 Anwendungsszenarien

Der PON‑ONU-SFP+-Stick integriert die vollständigen ONU-Funktionen eines optischen Modems. Dadurch kann der SFP+-Port des Flint 4 herkömmliche GPON-/XGS-PON-Glasfaseranschlüsse für Privathaushalte direkt abschließen. Ein separates externes optisches Modem ist nicht mehr erforderlich, sodass ein einziges Gerät sowohl den Glasfaserzugang als auch das Routing übernehmen kann. Diese Lösung richtet sich an erfahrene Netzwerknutzer, insbesondere wenn weniger Geräte im Heimnetzwerk eingesetzt und PON-Glasfaserleitungen des Anbieters direkt über den Router verwendet werden sollen.

### 3.2 Topologie

10G-SFP+-Port des Flint 4 → PON‑ONU-SFP+-Stick → GPON-/XGS-PON-Glasfaserleitung des Internetanbieters (einschließlich Teilnehmeranschlusskabel, PON-Splitter und OLT des Internetanbieters)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Vor- und Nachteile

Die folgende Tabelle bewertet wichtige Leistungs- und Benutzerfreundlichkeitsmerkmale der Lösung mit einem PON‑ONU-SFP+-Stick. Die Sternebewertungen und Hinweise dienen als Referenz:

|Kriterium|Sternebewertung|Anmerkungen|
|---|---|---|
|Übertragungsentfernung|★★★★★|Unterstützt die standardmäßigen PON-Glasfaser-Übertragungsentfernungen und damit alle üblichen privaten und gewerblichen Glasfaserzugänge.|
|Störfestigkeit|★★★★★|Die optische Übertragung über Glasfaser ist besonders störfest und signalstabil und entspricht den gängigen Standards für PON-Glasfaserzugänge.|
|Energieeffizienz|★★☆☆☆|Hohe Wärmeentwicklung bei hohen Geschwindigkeiten; eine zusätzliche Kühlung ist zwingend erforderlich, um Leistungseinbußen und Verbindungsabbrüche zu vermeiden.|
|Kompatibilität|★★☆☆☆|Inoffiziell geprüfte Lösung für erfahrene Nutzer; die Kompatibilität hängt von der Freigabeliste des Internetanbieters und vom Stick-Modell ab. Der langfristig stabile Betrieb ist nicht gewährleistet.|
|Einfache Bereitstellung|★★☆☆☆|Erfordert eine vorherige Bestätigung durch den Internetanbieter, die Konfiguration der SN-/PLOAM-Authentifizierung und eine optimierte Wärmeableitung. Die Anforderungen an die Bereitstellung sind insgesamt hoch.|
|Wirtschaftlichkeit|★★★☆☆|Ein separates optisches Modem entfällt. Es bestehen jedoch mögliche Dienstrisiken, beispielsweise nicht verfügbare IPTV-/Sprachdienste und fehlender offizieller technischer Support.|

### 3.4 Vorsichtsmaßnahmen

- **Erlaubnis des Internetanbieters vorab bestätigen**: Klären Sie mit dem Anbieter, ob kundeneigene ONU-Hardware eines Drittanbieters auf das PON-Netzwerk zugreifen darf, und fordern Sie die erforderlichen Authentifizierungsparameter an, darunter den SN-Registrierungscode und das PLOAM-Passwort.

- **Wärmeableitung ist zwingend erforderlich**: Statten Sie den PON‑ONU-Stick mit zusätzlichen Maßnahmen zur Wärmeableitung aus, um eine Taktreduzierung, Paketverluste und Verbindungsabbrüche durch hohe Temperaturen zu vermeiden.

- **Keine Dienstgarantie**: GL.iNet bietet für diese Lösung keinen technischen Support. Probleme wie ein instabiles Netzwerk, Geschwindigkeitsschwankungen und fehlerhafte Mehrwertdienste können nicht durch offizielle Firmware oder den Kundendienst behoben werden.

- Die Freigaberegeln für Modulmodelle unterscheiden sich je nach Anbieter. Erkundigen Sie sich vor dem Kauf, welche PON-Stick-Modelle Ihr Anbieter unterstützt.

### 3.5 Kompatible Modelle

Die folgenden PON-ONU-SFP+-Sticks wurden von GL.iNet und Community-Nutzern getestet und sind mit Flint 4 kompatibel. Die Liste dient lediglich als Referenz.

|Modell|Tester|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Community-Nutzer|

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
