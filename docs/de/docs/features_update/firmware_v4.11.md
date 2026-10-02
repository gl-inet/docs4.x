# Firmware v4.11

Diese Version konzentriert sich auf Verbesserungen bei der Überwachung der Netzwerkqualität und der Sicherheitsbewertung, damit Sie Verbindungsprobleme und potenzielle Sicherheitsrisiken erkennen können. Sie führt außerdem neue Funktionen für Mesh, GL.iNet Account und VLAN ein und enthält umfangreiche Verbesserungen für DNS, SQM, QoS und Datenverkehrsstatistiken.

Laden Sie die neueste Firmware im [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"} herunter.

## Netzwerkqualität

[Network Quality](../interface_guide/network_quality.md) ist eine neue Funktion, die Ihre Internetverbindung in Echtzeit überwacht. Sie bewertet Reaktionsfähigkeit, Latenz und DNS-Leistung und erkennt Verbindungsabbrüche und Paketverluste. So lassen sich Netzwerkinstabilität und Verbindungsprobleme erkennen, die reine Bandbreitentests möglicherweise nicht aufzeigen.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Sicherheitsprüfung

[Security Scan](../interface_guide/security_scan.md) ist eine neue Funktion, die die Sicherheitseinstellungen Ihres Routers bewertet und einen Sicherheitswert, Risikowarnungen sowie Optimierungsvorschläge bereitstellt. Sie prüft unter anderem Wi-Fi-Sicherheit, WAN-Ping, Remote SSH, Portweiterleitung und DPI-Inhaltsschutz, damit Sie potenzielle Sicherheitsrisiken erkennen und beheben können. Beim Öffnen der Seite startet automatisch eine Prüfung. Sie können auch auf das Symbol mit dem Sicherheitswert klicken, um die Prüfung zurückzusetzen und erneut auszuführen.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md) basiert auf dem Standard Wi-Fi EasyMesh™ und erweitert die Wi-Fi-Abdeckung im gesamten Zuhause. Die Funktion ermöglicht nahtloses Roaming. Wenn Sie mehrere GL.iNet-Router besitzen, richten Sie einen als Hauptrouter und die übrigen als Mesh-Knoten ein, um nahtloses Wi-Fi-Roaming in Ihrem Zuhause zu nutzen.

**Hinweis**: Diese Funktion wurde zunächst für bestimmte Modelle veröffentlicht und mit Firmwareversion 4.11 auf weitere Modelle ausgeweitet.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## GL.iNet-Konto

Ein [GL.iNet Account](../interface_guide/glinet_account.md) bietet einen einheitlichen Zugang zu Ihren Geräten und Cloud-Diensten. Mit einem einzigen GL.iNet-Konto können Sie auf GoodCloud und die GL.iNet App zugreifen, um Netzwerke und Geräte komfortabler zu verwalten. Darüber hinaus können Sie mit GoodPAS schnell eine sichere Verbindung zwischen Ihrem Reiserouter und Ihrem Heimnetzwerk herstellen und so auch unterwegs nahtlos auf Ihr Heimnetzwerk zugreifen.

**Hinweis**: Diese Funktion wurde zunächst für bestimmte Modelle veröffentlicht und mit Firmwareversion 4.11 auf weitere Modelle ausgeweitet.

![GL.iNet Account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md) ist eine Fernzugriffslösung auf Basis des AmneziaWG-Protokolls mit integrierter Datenverkehrsverschleierung. Sie können Ihren Reiserouter über einen dynamischen Zugriffscode sicher mit Ihrem Heimnetzwerk verbinden, ohne sich registrieren oder anmelden zu müssen.

**Hinweis**: Diese Funktion wurde zunächst für bestimmte Modelle veröffentlicht und mit Firmwareversion 4.11 auf weitere Modelle ausgeweitet.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md) ermöglicht Fernzugriff und die zentrale Verwaltung von GL.iNet-Routern. Sie können mehrere Geräte gleichzeitig verwalten, Netzwerkkonfigurationen bereitstellen, Firmware-Upgrades durchführen und aus der Ferne auf das Web-Admin-Panel oder das SSH-Terminal des Routers zugreifen.

**Hinweis**: Diese Funktion wurde zunächst für bestimmte Modelle veröffentlicht und mit Firmwareversion 4.11 auf weitere Modelle ausgeweitet.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Ethernet-Port

Die Seite [Ethernet Port](../interface_guide/ethernet_port_v4.10.md) zeigt alle Schnittstellen des Routers an. Sie können den Verbindungsstatus jeder Schnittstelle anzeigen, die Ethernet-Portrollen (WAN oder LAN) verwalten und Portdetails wie MAC-Adresse, ausgehandelte Geschwindigkeit und aktuellen Verbindungsstatus einsehen. Außerdem können Sie physische Schnittstellen beliebigen von Ihnen erstellten Subnetzen zuweisen.

**Hinweis**: Diese Funktion wurde zunächst für bestimmte Modelle veröffentlicht und mit Firmwareversion 4.11 auf weitere Modelle ausgeweitet.

Die folgende Abbildung zeigt Ethernet Port auf dem Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

Diese Version verbessert die [DNS](../interface_guide/dns_v4.11.md)-Konfiguration, indem WAN DNS, VPN DNS und Manual DNS auf einer einzigen Seite zusammengeführt werden. Sie können den DNS-Status für jeden Verbindungstyp anzeigen, benutzerdefinierte DNS-Server konfigurieren und festlegen, ob manuelle DNS-Einstellungen für VPN-Tunnel oder den Router selbst gelten.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

[QoS](../interface_guide/qos.md) (Quality of Service) wurde in dieser Firmware erweitert. Die neue Option **Run Speedtest** misst die WAN-Download- und Upload-Bandbreite und füllt die entsprechenden Felder automatisch aus. Es stehen drei Scheduling-Richtlinien zur Verfügung, darunter die neu eingeführten Optionen **Device Priority** und **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Ausgewählte lokale Clients erhalten bei einer Überlastung der WAN-Verbindung eine höhere Netzwerkpriorität.

- **Application Priority**: Legen Sie benutzerdefinierte Prioritäten für verschiedene Anwendungen fest. Der Router weist die Bandbreite entsprechend zu.

- **Advanced QoS**: Erstellen Sie erweiterte QoS-Regeln für Datenverkehr mit hoher Priorität.

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) bietet die Option **Run Speedtest** für die WAN-Bandbreite. Sie misst Download- und Upload-Geschwindigkeiten und füllt die entsprechenden Felder automatisch aus. Für die Warteschlangendisziplin **cake** passt die neue Funktion **Cake Autorate** die konfigurierte Bandbreite dynamisch anhand der RTT von Testpaketen an. Sie verwendet ressourcenschonende Ping-Abfragen statt aktiver Geschwindigkeitstests und wird für WAN-Verbindungen mit schwankender Bandbreite empfohlen.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## Datenstatistiken

[Data Statistics](../interface_guide/data_statistics.md) unterstützt jetzt das Filtern des Datenverkehrs nach Client und bietet neue Diagrammansichten, darunter Balken- und Kreisdiagramme. In App Traffic Statistics können Sie einen bestimmten Client auswählen und zwischen Diagrammansichten wechseln, um die Datennutzung übersichtlicher zu analysieren.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
