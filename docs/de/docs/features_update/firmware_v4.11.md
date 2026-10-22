# Firmware v4.11 {#firmware-v411}

Diese Version verbessert die Überwachung der Netzwerkqualität und die Sicherheitsbewertung, damit Sie Verbindungsprobleme und mögliche Sicherheitsrisiken erkennen können. Außerdem verbessert sie DNS, QoS, SQM und Datenstatistiken für eine flexiblere Netzwerkverwaltung und Datenverkehrssteuerung.

Laden Sie die neueste Firmware im [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"} herunter.

## Netzwerkqualität {#network-quality}

[Network Quality](../interface_guide/network_quality.md) ist eine neue Funktion, die Ihre Internetverbindung in Echtzeit überwacht. Sie bewertet Reaktionsfähigkeit, Latenz und DNS-Leistung und erkennt Verbindungsabbrüche und Paketverluste. So lassen sich Netzwerkinstabilität und Verbindungsprobleme erkennen, die reine Bandbreitentests möglicherweise nicht aufzeigen.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Sicherheitsprüfung {#security-scan}

[Security Scan](../interface_guide/security_scan.md) ist eine neue Funktion, die die Sicherheitseinstellungen Ihres Routers bewertet und einen Sicherheitswert, Risikowarnungen sowie Optimierungsvorschläge bereitstellt. Sie prüft unter anderem Wi-Fi-Sicherheit, WAN-Ping, Remote SSH, Portweiterleitung und DPI-Inhaltsschutz, damit Sie potenzielle Sicherheitsrisiken erkennen und beheben können. Beim Öffnen der Seite startet automatisch eine Prüfung. Sie können auch auf das Symbol mit dem Sicherheitswert klicken, um die Prüfung zurückzusetzen und erneut auszuführen.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## DNS {#dns}

Diese Version verbessert die [DNS](../interface_guide/dns_v4.11.md)-Konfiguration, indem WAN DNS, VPN DNS und Manual DNS auf einer einzigen Seite zusammengeführt werden. Sie können den DNS-Status für jeden Verbindungstyp anzeigen, benutzerdefinierte DNS-Server konfigurieren und festlegen, ob manuelle DNS-Einstellungen für VPN-Tunnel oder den Router selbst gelten.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) bietet die Option **Run Speedtest** für die WAN-Bandbreite. Sie misst die Download- und Upload-Geschwindigkeiten und füllt die entsprechenden Felder automatisch aus. Zusätzlich zu Application Priority enthält diese Version zwei weitere Scheduling-Richtlinien: **Device Priority** und **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Ausgewählte lokale Clients erhalten bei einer Überlastung der WAN-Verbindung eine höhere Netzwerkpriorität.

- **Application Priority**: Legen Sie benutzerdefinierte Prioritäten für verschiedene Anwendungen fest. Der Router weist die Bandbreite entsprechend zu.

- **Advanced QoS**: Erstellen Sie erweiterte QoS-Regeln für Datenverkehr mit hoher Priorität.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) bietet die Option **Run Speedtest** für die WAN-Bandbreite. Sie misst die Download- und Upload-Geschwindigkeiten und füllt die entsprechenden Felder automatisch aus. Es stehen zwei Warteschlangendisziplinen zur Verfügung: **cake** und **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: Intelligente, automatische Datenverkehrsformung mit der insgesamt besten Latenzkontrolle (empfohlen).

    Für diese Warteschlangendisziplin passt die neue Funktion **Cake Autorate** die konfigurierte Bandbreite dynamisch anhand der RTT von Testpaketen an. Sie verwendet ressourcenschonende Ping-Abfragen statt aktiver Geschwindigkeitstests und wird für WAN-Verbindungen mit schwankender Bandbreite empfohlen.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: Einfaches und effizientes Fair-Queueing mit grundlegender Latenzreduzierung.

## Datenstatistiken {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) unterstützt jetzt das Filtern des Datenverkehrs nach Client und bietet neue Diagrammansichten, darunter Balken- und Kreisdiagramme. In App Traffic Statistics können Sie einen bestimmten Client auswählen und zwischen Diagrammansichten wechseln, um die Datennutzung übersichtlicher zu analysieren.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
