# UPnP {#upnp}

**Hinweis**: Diese Funktion wurde in Firmware v4.11 eingeführt.

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **SECURITY** -> **UPnP**.

UPnP (Universal Plug and Play) ermöglicht kompatiblen LAN-Geräten und Anwendungen, automatisch Portzuordnungen auf GL.iNet-Routern anzufordern. Diese Zuordnungen leiten eingehenden WAN-Datenverkehr an bestimmte LAN-IP-Adressen und Ports weiter. So können sich externe Clients ohne manuell konfigurierte Portweiterleitungsregeln mit lokalen Diensten verbinden.

UPnP unterscheidet sich von [Portweiterleitung](./port_forwarding.md) und [DMZ](./port_forwarding.md#dmz): UPnP erstellt Zuordnungen automatisch auf Geräteanfrage. Portweiterleitung gibt ausgewählte Ports frei, während DMZ alle Ports eines LAN-Hosts freigibt. Sowohl Portweiterleitung als auch DMZ erfordern eine manuelle Konfiguration. Stellen Sie vor dem Aktivieren dieser Funktionen sicher, dass Sie deren Funktionsweise und die damit verbundenen Sicherheitsrisiken verstehen.

**Hinweis**: 

1. Wenn UPnP aktiviert ist, können kompatible LAN-Geräte und Anwendungen Portzuordnungen ohne Genehmigung jeder einzelnen Anfrage anfordern.

2. Ein kompromittiertes Gerät oder eine schädliche Anwendung kann UPnP nutzen, um lokale Dienste im Internet verfügbar zu machen. Aktivieren Sie UPnP nur in vertrauenswürdigen Netzwerken und deaktivieren Sie es, wenn es nicht benötigt wird.

3. UPnP benötigt eine öffentliche IP-Adresse an der WAN-Schnittstelle des Routers, um eingehende Verbindungen aus dem Internet anzunehmen. Es funktioniert nicht, wenn Ihr Internetanbieter CGNAT verwendet.

Typische Anwendungsfälle für UPnP sind:

- **Online-Spiele**: Kompatible Spiele und Konsolen (z. B. Steam-Multiplayer-Spiele, Xbox Series X|S, PlayStation 5, Nintendo Switch) können automatisch Portzuordnungen erstellen, um Verbindungen mit anderen Spielern herzustellen.

- **Peer-to-Peer-Dateifreigabe**: BitTorrent-Clients und andere kompatible P2P-Anwendungen können Listening-Ports automatisch zuordnen, um eingehende Verbindungen von Peers anzunehmen.

- **Fernzugriff**: Geräte und Anwendungen, die UPnP-Portzuordnungen unterstützen, etwa bestimmte NAS-Geräte, IP-Kameras und Medienserver, können automatisch Zuordnungen für den Zugriff von außerhalb des lokalen Netzwerks konfigurieren.

## Schnelleinrichtung {#quick-setup}

Aktivieren Sie UPnP mit dem Schalter. Kompatible Geräte und Anwendungen können anschließend bei Bedarf Portzuordnungen anfordern, wie im folgenden Beispiel gezeigt.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- Client / Application: Beschreibung des Clients bzw. der Anwendung und LAN-IP-Adresse des anfragenden Geräts.

- Protocol: Transportprotokoll der Zuordnung, z. B. TCP oder UDP.

- External Port: WAN-Port für eingehende Verbindungen.

- Internal Target: Ziel-IP-Adresse und Port im LAN.

- Lease: Verbleibende Zeit bis zum Ablauf der Zuordnung. Die standardmäßige Lease-Dauer beträgt 7 Tage.

- Action: Klicken Sie auf das Papierkorbsymbol, um die Zuordnung zu löschen. Der Client bzw. die Anwendung kann sie erneut anfordern, wenn er bzw. sie noch ausgeführt wird.

Aktive Portzuordnungen werden entfernt, wenn der Client sie freigibt oder ihre Lease abläuft. Klicken Sie auf **Refresh**, um die aktuellen Portzuordnungen anzuzeigen.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
