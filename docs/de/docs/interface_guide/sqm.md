# SQM (Smart Queue Management)

SQM (Smart Queue Management) verwaltet den Netzwerkverkehr Ihres Routers intelligent, um Latenzen und „Bufferbloat“ zu minimieren und so ein flüssigeres Gaming sowie bessere Sprachanrufe zu ermöglichen.

**Hinweis**:

1. Diese Funktion ist derzeit nur auf **GL-MT5000 (Brume 3)** verfügbar.

2. Diese Funktion beeinflusst den Datenverkehr, der den Router als Gateway durchläuft (einschließlich lokalem Client-Datenverkehr und VPN-Client-Datenverkehr), jedoch nicht den eingehenden Datenverkehr, wenn der Router als VPN-Server arbeitet.

3. Da SQM ressourcenintensiv ist, eignet es sich am besten für Netzwerke mit geringer Bandbreite oder starker Auslastung. Auf Hochgeschwindigkeitsverbindungen kann die Aktivierung den maximalen Durchsatz verringern.

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** > > **SQM**.

Legen Sie zuerst Ihre maximale Upload- und Download-Geschwindigkeit fest (Eingabebereich: 1 - 10000), damit der Datenverkehr geplant werden kann. Stimmen Sie die Werte für optimale Ergebnisse auf Ihre tatsächliche Internetbandbreite ab.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Für **Queue Rule** stehen zwei Optionen zur Verfügung:

- **cake**: Intelligentes, automatisches Traffic Shaping mit überlegener allgemeiner Latenzkontrolle (empfohlen).

- **fq_codel**: Einfaches, effizientes Fair Queueing mit grundlegender Latenzreduzierung.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
