# Firmware v4.9

Diese Version konzentriert sich auf präzisere Netzwerksteuerung, verbessertes Datenverkehrsmanagement, höhere Netzwerksicherheit und eine überarbeitete Benutzeroberfläche, um die allgemeine Benutzererfahrung zu verbessern.

Die neueste Firmware erhalten Sie im [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control ist ein zentrales Modul für das Netzwerkmanagement. Es ermöglicht die genaue Erkennung, Überwachung, Regulierung und Filterung des Netzwerkdatenverkehrs, optimiert die Zuweisung von Netzwerkressourcen, beseitigt Bandbreitenengpässe und standardisiert das Netzwerkzugriffsverhalten. Dadurch entsteht eine flüssigere, sicherere und besser kontrollierbare Netzwerkerfahrung. In Firmware v4.9 umfasst dieses Modul mehrere praktische Funktionen für ein umfassendes Datenverkehrsmanagement.

Das Flow-Control-Modul umfasst DPI Engine, Data Statistics, Content Filter, QoS, SQM und Parental Control.

### DPI Engine

Während herkömmliche Router nur Quell- und Zieladressen erkennen, analysiert DPI (Deep Packet Inspection) die Nutzdaten von Paketen eingehend. Mithilfe einer Bibliothek zum Abgleich charakteristischer Merkmale werden Anwendungen und Websites genau erkannt, sodass der Datenverkehr differenziert klassifiziert und gesteuert werden kann.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics bietet ein übersichtliches Datenverkehrs-Dashboard, das die Netzwerknutzung nach Anwendung und Protokoll aufschlüsselt. Es zeigt historische Trends für 1 Stunde, 1 Tag und 7 Tage sowie Nutzungsranglisten an, überwacht den Datenverkehr einzelner Geräte und ermöglicht das Blockieren unerwünschter Apps mit einem Klick.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter ist eine intelligente, auf der DPI-Klassifizierung basierende Funktion für die Online-Sicherheit. Sie blockiert automatisch schädliche und bösartige Websites, um das Netzwerk sauber und sicher zu halten. Außerdem unterstützt sie benutzerdefinierte Regeln zum Blockieren bestimmter Apps, Domains oder IP-Adressen.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS (Quality of Service) optimiert die Bandbreitenzuweisung, indem bei Netzwerküberlastung wichtigen Aktivitäten wie Videoanrufen oder Gaming Priorität eingeräumt wird. Dies reduziert die Latenz und verbessert die gesamte Netzwerkleistung.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) verwaltet den Netzwerkdatenverkehr des Routers intelligent, um Latenz und „Bufferbloat“ zu minimieren und so flüssigeres Gaming und störungsfreiere Sprachanrufe zu ermöglichen.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

Diese Funktion war bisher im Menü **Applications** eingeordnet und wurde in Firmware v4.9 in das Menü **Flow Control** verschoben. Sie nutzt die aktualisierte DPI Engine, um ungeeignete Anwendungen und Netzwerkinhalte präzise zu erkennen und zu blockieren. Dadurch werden professionellere und genauere datenverkehrsbasierte Zugriffsbeschränkungen ermöglicht.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

Firmware v4.9 verbessert die zugrunde liegende Routing-Logik und die interaktive Oberfläche des VPN-Moduls umfassend. Potenzielle Routing-Konflikte werden behoben, die Konfigurationslogik wird vereinfacht und die Bedienung wird intuitiver.

Die wichtigsten Anpassungen sind nachfolgend beschrieben.

### Isolierter VPN-Tunnel

Jeder VPN-Tunnel arbeitet als eigenständige Gruppe ohne gruppenübergreifendes Failover. Sobald Netzwerkdatenverkehr einer bestimmten VPN-Gruppe zugeordnet wurde, wechselt er auch bei Ausfall des aktuellen Tunnels nicht automatisch zu anderen VPN-Gruppen. Dadurch bleibt das Routing stabil und vorhersehbar.

**Hinweis**: Die bisherige Richtlinie „Not Use VPN“ wurde in Firmware v4.9 entfernt. Dadurch entfallen redundante Konfigurationen und Routing-Konflikte durch mehrere komplexe Tunnelregeln werden vermieden.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### VPN-Profil-Failover

Eine einzelne VPN-Tunnelgruppe kann mehrere Konfigurationsprofile enthalten. Benutzer können die Priorität der einzelnen Profile innerhalb derselben Gruppe anpassen, sodass bei Ausfall eines einzelnen Profils ein automatisches internes Failover die VPN-Verbindung aufrechterhält.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Neu gestaltetes Dashboard

Das VPN Dashboard wurde vollständig überarbeitet und bietet nun ein intuitiveres Layout. Tunnelstatus, Verbindungsdetails und Konfigurationseinträge werden übersichtlicher dargestellt, wodurch die tägliche Bedienung und Verwaltung deutlich effizienter wird. In der neuen Architektur ist der Kill Switch außerdem standardmäßig für alle VPN-Tunnel aktiviert, damit Ihr Datenverkehr jederzeit geschützt bleibt.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

Firmware v4.9 führt offiziell das AmneziaWG 2.0-Protokoll mit mehreren neuen Parametern zur Verschleierung des Datenverkehrs ein. Das aktualisierte Protokoll kann die Erkennung durch DPI und andere Systeme zur Datenverkehrsidentifikation wirksam umgehen und verbessert damit die Verbindungsverschleierung und Störfestigkeit deutlich. So können stabile und zuverlässige VPN-Verbindungen in Regionen mit Netzwerkeinschränkungen und in komplexen Netzwerkumgebungen aufgebaut werden.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## IoT-Netzwerk

In Firmware v4.9 können Sie ein unabhängiges, dediziertes WLAN-Netzwerk für intelligente IoT-Geräte erstellen. Da es physisch und logisch vom primären Netzwerk isoliert ist, werden die Belegung von Netzwerkressourcen und Sicherheitsrisiken vermieden, die durch den Zugriff von IoT-Geräten auf das Hauptnetzwerk entstehen können. Diese Optimierung bietet eine breitere Gerätekompatibilität für verschiedene intelligente IoT-Clients und erhöht insgesamt die Sicherheit des Heimnetzwerks.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL steht für Access Control List und ist eine zentrale Funktion für das Netzwerksicherheitsmanagement. Sie ermöglicht benutzerdefinierte Zugriffsregeln zur Verwaltung des internen und externen Netzwerkdatenverkehrs anhand von Verbindungsprotokollen, Geräte-IP-Adressen und Ports. Mit einer präzisen Berechtigungssteuerung können bestimmte Netzwerkzugriffe erlaubt oder blockiert werden. Wenn mehrere ACL-Regeln in Konflikt stehen, führt das System automatisch die Regel mit der höheren Priorität aus, um die Richtlinie korrekt umzusetzen.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL unterscheidet sich in der Kernfunktion von Port Forwarding: ACL konzentriert sich auf das Netzwerksicherheitsmanagement durch Steuerung von Geräte- und Datenverkehrsberechtigungen. Port Forwarding dient dagegen der Umleitung von Netzwerkressourcen, indem externer Netzwerkdatenverkehr an bestimmte lokale Endgeräte weitergeleitet wird, um Fernzugriff auf lokale Netzwerkdienste zu ermöglichen.

## Wireless-Benutzeroberfläche

Die Wireless-Benutzeroberfläche wurde vollständig mit einem übersichtlicheren Layout und einem einheitlichen visuellen Stil überarbeitet. Dadurch sinkt die Bedienkomplexität und die Oberfläche wird insgesamt einfacher und benutzerfreundlicher.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## Verschlüsseltes DNS

Verschlüsseltes DNS wurde um weitere Verschlüsselungsprotokolle einschließlich DoH, DoT und DoQ erweitert. Gleichzeitig wurden weitere offizielle DNS-Anbieter integriert und die manuelle Konfiguration benutzerdefinierter verschlüsselter DNS-Server hinzugefügt, um unterschiedliche Anforderungen an eine sichere Domainauflösung zu erfüllen.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

GL.iNet-Router unterstützen nun den Betrieb als Tailscale Exit Node. Der gesamte ausgehende Internetdatenverkehr von Geräten im Tailnet kann über die öffentliche IP-Adresse des Routers geleitet werden, um einen einheitlichen und sicheren Netzwerkausgang für das gesamte Tailscale-Netzwerk bereitzustellen. Weitere Informationen finden Sie [hier](../interface_guide/tailscale.md#run-exit-node).

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
