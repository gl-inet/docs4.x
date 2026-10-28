# UPnP {#upnp}

**Opmerking**: Deze functie is geïntroduceerd in firmware v4.11.

---

Ga links in het webbeheerpaneel naar **SECURITY** -> **UPnP**.

Met UPnP (Universal Plug and Play) kunnen compatibele LAN-apparaten en toepassingen automatisch poorttoewijzingen aanvragen op GL.iNet-routers. Deze toewijzingen sturen inkomend WAN-verkeer door naar opgegeven LAN-IP-adressen en poorten, zodat externe clients verbinding kunnen maken met lokale diensten zonder handmatig ingestelde regels voor port forwarding.

UPnP verschilt van [port forwarding](./port_forwarding.md) en [DMZ](./port_forwarding.md#dmz): UPnP maakt automatisch toewijzingen op verzoek van apparaten. Port forwarding stelt geselecteerde poorten open, terwijl DMZ alle poorten van een LAN-host openstelt. Port forwarding en DMZ vereisen beide handmatige configuratie. Zorg dat je de werking en de bijbehorende beveiligingsrisico’s begrijpt voordat je deze functies inschakelt.

**Opmerking**: 

1. Als UPnP is ingeschakeld, kunnen compatibele LAN-apparaten en toepassingen poorttoewijzingen aanvragen zonder goedkeuring per verzoek.

2. Een gecompromitteerd apparaat of schadelijke toepassing kan UPnP gebruiken om lokale diensten via internet bereikbaar te maken. Schakel UPnP alleen in op vertrouwde netwerken en schakel het uit wanneer het niet nodig is.

3. UPnP vereist een openbaar IP-adres op de WAN-interface van de router om inkomende verbindingen van internet te accepteren. Het werkt niet als je internetprovider CGNAT gebruikt.

Veelgebruikte toepassingen van UPnP zijn:

- **Online gaming**: compatibele games en consoles (bijvoorbeeld Steam-multiplayergames, Xbox Series X|S, PlayStation 5, Nintendo Switch) kunnen automatisch poorttoewijzingen maken om verbindingen met andere spelers te helpen opzetten.

- **Peer-to-peerbestandsdeling**: BitTorrent-clients en andere compatibele P2P-toepassingen kunnen automatisch luisterpoorten toewijzen om inkomende verbindingen van peers te accepteren.

- **Externe toegang**: apparaten en toepassingen die UPnP-poorttoewijzing ondersteunen, zoals bepaalde NAS-apparaten, IP-camera’s en mediaservers, kunnen automatisch toewijzingen instellen voor toegang van buiten het lokale netwerk.

## Snelle installatie {#quick-setup}

Schakel UPnP in met de schakelaar. Compatibele apparaten en toepassingen kunnen daarna naar behoefte poorttoewijzingen aanvragen, zoals in het onderstaande voorbeeld.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- Client / Application: de beschrijving van de client of toepassing en het LAN-IP-adres van het aanvragende apparaat.

- Protocol: het transportprotocol van de toewijzing, bijvoorbeeld TCP of UDP.

- External Port: de WAN-poort voor inkomende verbindingen.

- Internal Target: het doel-IP-adres en de poort in het LAN.

- Lease: de resterende tijd voordat de toewijzing verloopt. De standaardleaseduur is 7 dagen.

- Action: klik op het prullenbakpictogram om de toewijzing te verwijderen. De client of toepassing kan deze opnieuw aanvragen als deze nog actief is.

Actieve poorttoewijzingen worden verwijderd wanneer de client ze vrijgeeft of de lease verloopt. Klik op **Refresh** om de nieuwste poorttoewijzingen te bekijken.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
