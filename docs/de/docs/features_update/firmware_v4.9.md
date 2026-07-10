# Firmware v4.9

Diese Version konzentriert sich auf präzisere Netzwerksteuerung, verbessertes Datenverkehrsmanagement, höhere Netzwerksicherheit und eine überarbeitete Benutzeroberfläche, um die allgemeine Benutzererfahrung zu verbessern. [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}

## Flow Control

Flow Control ist ein zentrales Modul für das Netzwerkmanagement. Es ermöglicht die genaue Erkennung, Überwachung, Regulierung und Filterung von Netzwerkdatenverkehr, optimiert die Zuweisung von Netzwerkressourcen, reduziert Bandbreitenengpässe und standardisiert das Netzwerkzugriffsverhalten. Dadurch entsteht eine flüssigere, sicherere und besser kontrollierbare Netzwerkerfahrung. In Firmware v4.9 ist dieses Modul mit mehreren praktischen Funktionen für ein umfassendes Datenverkehrsmanagement integriert.

Das Flow Control-Modul umfasst die folgenden Funktionen:

!!! note "DPI Engine"
    
    Deep Packet Inspection-Technologie zur genauen Erkennung von Anwendungsprotokollen, Datenverkehrstypen und Netzwerkverhalten.

!!! note "Datenstatistik"
    
    Erfassung, Analyse und Visualisierung von Netzwerkdaten in Echtzeit und aus Verlaufsdaten zur intuitiven Überwachung des Netzwerkstatus.

!!! note "Inhaltsfilterung"
    
    Intelligente Sperrung und Filterung ungeeigneter Netzwerkinhalte zur Standardisierung des Netzwerkzugriffs.

!!! note "QoS (Quality of Service)"
    
    Bandbreitenzuweisung und Priorisierung des Datenverkehrs, um die Netzwerkqualität für wichtige Anwendungen sicherzustellen.

!!! note "SQM (Smart Queue Management)"
    
    Optimiert die Warteschlangenplanung im Netzwerk, um Latenz und Paketverlust zu reduzieren und eine reibungslosere Netzwerkübertragung zu ermöglichen.

!!! note "Kindersicherung"
    
    Diese Funktion war bisher im Menü **Applications** eingeordnet und wurde in v4.9 in das Menü **Flow Control** verschoben. Sie nutzt die aktualisierte DPI Engine, um ungeeignete Anwendungen und Netzwerkinhalte präzise zu erkennen und zu blockieren. Dadurch werden professionellere und genauere datenverkehrsbasierte Zugriffsbeschränkungen ermöglicht.

## VPN

Firmware v4.9 verbessert die zugrunde liegende Routing-Logik und die interaktive Oberfläche des VPN-Moduls umfassend. Potenzielle Routing-Konflikte werden behoben, die Konfigurationslogik wird vereinfacht und die Bedienung wird intuitiver.
    
Die wichtigsten Anpassungen sind:

!!! note "Unabhängige VPN-Gruppierung"

    Jeder VPN-Tunnel arbeitet als eigenständige Gruppe ohne gruppenübergreifendes Failover. Wenn Netzwerkdatenverkehr einer bestimmten VPN-Gruppe zugeordnet wird, wechselt er auch bei Ausfall des aktuellen Tunnels nicht automatisch zu anderen VPN-Gruppen. Dadurch bleibt das Routing stabil und vorhersehbar.

!!! note "Profil-Failover innerhalb einer Gruppe"
    
    Eine einzelne VPN-Tunnelgruppe kann mehrere Konfigurationsprofile enthalten. Benutzer können die Priorität der einzelnen Profile innerhalb derselben Gruppe anpassen, sodass bei Ausfall eines einzelnen Profils ein automatisches internes Failover die VPN-Verbindung aufrechterhält.
    
!!! note "Richtlinie \"Not Use VPN\" entfernt"
    
    Die bisherige Option "Not Use VPN" für die VPN-Richtlinieneinrichtung wurde in v4.9 entfernt. Dadurch werden redundante Konfigurationseinträge beseitigt und komplexe Routing-Konflikte durch mehrere Richtlinieneinstellungen vermieden.
    
!!! note "VPN Dashboard neu gestaltet"
        
    Das VPN Dashboard wurde vollständig mit einem intuitiveren Layout überarbeitet. Tunnelstatus, Verbindungsinformationen und Konfigurationseinträge werden klarer angezeigt, was die tägliche Bedienung und Verwaltung deutlich erleichtert.

## AmneziaWG 2.0-Protokoll

Firmware v4.9 führt offiziell das AmneziaWG 2.0-Protokoll mit mehreren neuen Parametern zur Verschleierung des Datenverkehrs ein. Das aktualisierte Protokoll kann Erkennung durch DPI und andere Systeme zur Datenverkehrsidentifikation wirksam umgehen und verbessert damit die Verbindungsverschleierung und Störfestigkeit deutlich. So können stabile und zuverlässige VPN-Verbindungen in eingeschränkten Regionen und komplexen Netzwerkumgebungen aufgebaut werden.

## IoT-Netzwerk

Die neu entwickelte IoT-Netzwerkfunktion unterstützt die Erstellung eines unabhängigen, dedizierten WLAN-Netzwerks für smarte IoT-Geräte. Da es physisch und logisch vom primären Netzwerk isoliert ist, vermeidet es die Belegung von Netzwerkressourcen und Sicherheitsrisiken, die durch den Zugriff von IoT-Geräten auf das Hauptnetzwerk entstehen können. Diese Optimierung bietet eine breitere Gerätekompatibilität für verschiedene smarte IoT-Clients und erhöht insgesamt die Sicherheit des Heimnetzwerks.

## ACL (Access Control List)

ACL steht für Access Control List und ist eine zentrale Funktion für das Netzwerksicherheitsmanagement. Sie ermöglicht benutzerdefinierte Zugriffsregeln zur Verwaltung des internen und externen Netzwerkdatenverkehrs anhand von Verbindungsprotokollen, Geräte-IP-Adressen und Ports. Sie unterstützt präzise Berechtigungssteuerung, um bestimmte Netzwerkzugriffe zu erlauben oder zu blockieren. Wenn mehrere ACL-Regeln Konflikte verursachen, führt das System automatisch die Regel mit höherer Priorität aus, um die korrekte Umsetzung der Richtlinie sicherzustellen.

ACL unterscheidet sich in der Kernfunktion von Port Forwarding: ACL konzentriert sich auf das Netzwerksicherheitsmanagement durch Steuerung von Geräte- und Datenverkehrsberechtigungen. Port Forwarding dient dagegen der Umleitung von Netzwerkressourcen, indem externer Netzwerkdatenverkehr an bestimmte lokale Endgeräte weitergeleitet wird, um Fernzugriff auf lokale Netzwerkdienste zu ermöglichen.

## Weitere Verbesserungen

!!! note "Neugestaltung der Wireless-Benutzeroberfläche"
    
    Die Wireless-Einstellungsoberfläche wurde vollständig mit einem übersichtlicheren Layout und einem einheitlichen visuellen Stil überarbeitet. Dadurch sinkt die Bedienkomplexität und die Oberfläche wird insgesamt einfacher und benutzerfreundlicher.

!!! note "Aktualisiertes verschlüsseltes DNS"
    
    Verschlüsseltes DNS wurde um weitere Verschlüsselungsprotokolle einschließlich DoH, DoT und DoQ erweitert. Gleichzeitig wurden weitere offizielle DNS-Anbieter integriert und die manuelle Konfiguration benutzerdefinierter verschlüsselter DNS-Server hinzugefügt, um unterschiedliche Anforderungen an sichere Domainauflösung zu erfüllen.
    
!!! note "Unterstützung für Tailscale Exit Node"
    
    GL.iNet-Router unterstützen nun den Betrieb als Tailscale Exit Node. Der gesamte ausgehende Internetdatenverkehr von Geräten im Tailnet kann über die öffentliche IP-Adresse des Routers geleitet werden, um einen einheitlichen und sicheren Netzwerkausgang für das gesamte Tailscale-Netzwerk bereitzustellen.
    
!!! note "AstroWarp-Integration"
    
    AstroWarp ist in v4.9 offiziell in das GL.iNet Router SDK integriert. Auf Basis des AmneziaWG-Protokolls mit nativer Datenverkehrsverschleierung bietet es stabilen, verschlüsselten und sicheren Fernzugriff. Benutzer können die Gerätekopplung und Verbindungseinrichtung schnell über einen dynamischen Zugriffscode im webbasierten Admin Panel abschließen. Es unterstützt eine sichere Verbindung per Klick zwischen Reiseroutern und Heimnetzwerken innerhalb weniger Sekunden, ohne dass eine Kontoregistrierung oder Anmeldung erforderlich ist.
