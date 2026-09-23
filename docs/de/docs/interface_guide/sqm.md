# SQM (Smart Queue Management)

**Hinweis**: Diese Funktion wurde mit Firmware v4.9 eingeführt.

Einige Modelle, darunter Mango 2 (GL-MG1300), unterstützen SQM wegen unzureichenden Speichers auch mit Firmware v4.9 oder höher nicht.

---

Navigieren Sie im linken Menü des webbasierten Admin-Panels zu **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) verwaltet den Netzwerkverkehr Ihres Routers intelligent, um Latenzen und „Bufferbloat“ zu minimieren und so flüssigeres Gaming und bessere Sprachanrufe zu ermöglichen.

**Hinweis**:

1. Diese Funktion wirkt sich nur auf Datenverkehr aus, der den Router passiert, wenn er als Gateway arbeitet, einschließlich lokalem Client-Datenverkehr und VPN-Client-Datenverkehr. Auf eingehenden Datenverkehr wirkt sie nicht, wenn der Router als VPN-Server arbeitet.

2. Da SQM ressourcenintensiv ist, eignet es sich am besten für Netzwerke mit geringer Bandbreite oder starker Auslastung. Auf Hochgeschwindigkeitsverbindungen kann die Aktivierung den maximalen Durchsatz verringern.

3. SQM wirkt nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.

4. SQM und QoS können nicht gleichzeitig aktiviert werden.

5. SQM kann nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren von SQM wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle {#supported-models}

??? "Unterstützte Modelle"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Nicht unterstützte Modelle"
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


## Für Firmware v4.11 und höher

Aktivieren Sie SQM mit dem Schalter und führen Sie anschließend die folgenden Schritte aus.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Geben Sie die Upload- und Download-Geschwindigkeit des WAN manuell ein (Eingabebereich: 1–10000) oder klicken Sie auf **Run Speedtest**, um sie zu messen und die Felder automatisch auszufüllen. Für den Geschwindigkeitstest ist eine aktive Internetverbindung erforderlich.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Hinweis**: Die Werte werden in **Mbps** (Megabit pro Sekunde) eingegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

2. **Queue Discipline**

    Wählen Sie eine Warteschlangenregel aus, um den Datenverkehr zu verwalten und die Latenz unter Last zu reduzieren.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: Intelligentes, automatisches Traffic Shaping mit besonders guter allgemeiner Latenzkontrolle (empfohlen).

        Wenn **cake** als Queue Discipline ausgewählt ist, steht **Cake Autorate** optional zur Verfügung.

        Cake Autorate passt die CAKE-Bandbreite anhand der gemessenen RTT-Latenz in Echtzeit nach unten oder oben an. Es werden keine aktiven Geschwindigkeitstests, sondern nur schlanke Ping-Abfragen ausgeführt. Die Funktion wird bei schwankender WAN-Bandbreite empfohlen und ist bei stabilen Verbindungen nicht erforderlich.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Hinweis**: Cake Autorate erzeugt fortlaufenden Prüfverkehr im Hintergrund. Berücksichtigen Sie diesen zusätzlichen Datenverbrauch bei getakteten Verbindungen.

        Die Standardeinstellungen eignen sich für die meisten Verbindungen. Ändern Sie die folgenden Parameter nur, wenn Sie deren Auswirkungen verstehen. Klicken Sie bei Bedarf auf **Reset to Default**, um die Standardwerte wiederherzustellen.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: Durch Kommas getrennte Liste von IP-Adressen für die Prüfung der Netzwerkqualität.
        - **Probe Interval**: Kürzere Intervalle reagieren schneller, beanspruchen jedoch mehr CPU-Ressourcen.
        - **Concurrent Probes**: Die Anzahl gleichzeitiger Prüfungen darf die Anzahl der Prüfserver nicht überschreiten; höhere Werte erhöhen die CPU-Last.
        - **Idle Detection Threshold**: Liegt die Übertragungsrate unter diesem Wert, gilt die Verbindung als inaktiv. Der Wert darf 25 % des konfigurierten Geschwindigkeitslimits nicht überschreiten.
        - **Download Latency Threshold**: Wird dieser Schwellenwert überschritten, wird die Download-Bandbreite reduziert.
        - **Upload Latency Threshold**: Wird dieser Schwellenwert überschritten, wird die Upload-Bandbreite reduziert.

    - **fq_codel**: Einfaches, effizientes Fair Queueing mit grundlegender Latenzreduzierung.

## Für Firmware v4.9 bis v4.10

Schalten Sie den Schalter um, um SQM zu aktivieren, und legen Sie Ihre maximale Upload- und Download-Geschwindigkeit fest (Eingabebereich: 1 - 10000), damit der Datenverkehr geplant werden kann. Stimmen Sie die Werte für optimale Ergebnisse auf Ihre tatsächliche Internetbandbreite ab.

![sqm](https://static.gl-inet.com/docs/router/de/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Hinweis**: Die im Eingabefeld eingegebenen Werte sind in **Mbps** (Megabit pro Sekunde) angegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

![up down speed](https://static.gl-inet.com/docs/router/de/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Für **Queue Rule** stehen zwei Optionen zur Verfügung:

- **cake**: Intelligentes, automatisches Traffic Shaping mit besonders guter allgemeiner Latenzkontrolle (empfohlen).

- **fq_codel**: Einfaches, effizientes Fair Queueing mit grundlegender Latenzreduzierung.

!!! Tip

    Ein Unterschied zwischen QoS und SQM besteht darin, dass Sie mit QoS Anwendungsprioritäten festlegen und der Router die Bandbreite entsprechend zuweist, während Sie mit SQM eine Warteschlangenregel auswählen können.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
