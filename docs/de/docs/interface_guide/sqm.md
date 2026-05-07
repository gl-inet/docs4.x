# SQM (Smart Queue Management)

SQM (Smart Queue Management) verwaltet den Netzwerkverkehr Ihres Routers intelligent, um Latenzen und „Bufferbloat“ zu minimieren und so flüssigeres Gaming und bessere Sprachanrufe zu ermöglichen.

**Hinweis**:

1. Diese Funktion wirkt sich nur auf Datenverkehr aus, der den Router passiert, wenn er als Gateway arbeitet, einschließlich lokalem Client-Datenverkehr und VPN-Client-Datenverkehr. Auf eingehenden Datenverkehr wirkt sie nicht, wenn der Router als VPN-Server arbeitet.

2. Da SQM ressourcenintensiv ist, eignet es sich am besten für Netzwerke mit geringer Bandbreite oder starker Auslastung. Auf Hochgeschwindigkeitsverbindungen kann die Aktivierung den maximalen Durchsatz verringern.

3. SQM wirkt nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.

4. SQM und QoS können nicht gleichzeitig aktiviert werden.

5. SQM kann nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren von SQM wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle

!!! note "Unterstützte Modelle"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Hinweis: Mit ※ gekennzeichnete Modelle unterstützen SQM ab Firmware v4.9.

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **SQM**.

Schalten Sie den Schalter um, um SQM zu aktivieren, und legen Sie Ihre maximale Upload- und Download-Geschwindigkeit fest (Eingabebereich: 1 - 10000), damit der Datenverkehr geplant werden kann. Stimmen Sie die Werte für optimale Ergebnisse auf Ihre tatsächliche Internetbandbreite ab.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Hinweis**: Die im Eingabefeld eingegebenen Werte sind in **Mbps** (Megabit pro Sekunde) angegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Für **Queue Rule** stehen zwei Optionen zur Verfügung:

- **cake**: Intelligentes, automatisches Traffic Shaping mit besonders guter allgemeiner Latenzkontrolle (empfohlen).

- **fq_codel**: Einfaches, effizientes Fair Queueing mit grundlegender Latenzreduzierung.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
