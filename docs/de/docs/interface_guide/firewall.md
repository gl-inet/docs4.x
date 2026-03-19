# Firewall

Diese Anleitung gilt für Firmware v4.5 und früher.

Seit v4.6 wurde die Firewall-Seite aufgeteilt. Die Funktionen Port Forwarding und DMZ wurden auf die Seite [Portweiterleitung](port_forwarding.md) verschoben. Die Funktion Open Ports wurde auf die Seite [Sicherheit](security.md) verschoben.

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **Firewall**.

Auf der Firewall-Seite können Sie Firewall-Regeln wie **Port Forwarding**, **Open Ports on Router** und **DMZ** festlegen.

## Port Forwards

Mit Port Forwarding können entfernte Computer eine Verbindung zu einem lokalen Computer oder Server hinter der Firewall des Routers im LAN herstellen, z. B. zu Webservern oder FTP-Servern.

Um Portweiterleitungen einzurichten, klicken Sie auf die Registerkarte **Port Forwards** und dann auf **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

Fügen Sie im Pop-up-Fenster eine neue Portweiterleitungsregel hinzu und klicken Sie auf **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Der Name der Regel.

**Protocol:** Das verwendete Protokoll. Sie können TCP, UDP oder sowohl TCP als auch UDP auswählen.

**External Zone:** Die Optionen für die externe Zone sind `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** Die Nummern der externen Ports. Sie können hier eine bestimmte Portnummer eingeben.

**Internal Zone:** Die Optionen für die interne Zone sind `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** Die vom Router zugewiesene IP-Adresse des Geräts, auf das remote zugegriffen werden soll.

**Internal Port:** Die interne Portnummer des Geräts. Sie können eine bestimmte Portnummer eingeben. Lassen Sie das Feld leer, wenn sie identisch mit dem externen Port ist.

**Enable:** Aktiviert oder deaktiviert die Regel.

## Open Ports on Router

Dienste des Routers, z. B. Web und FTP, erfordern, dass ihre jeweiligen Ports auf dem Router geöffnet werden, damit sie öffentlich erreichbar sind.

Um einen Port zu öffnen, wechseln Sie zur Registerkarte **Open Ports on Router** und klicken Sie dann auf **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

Öffnen Sie im Pop-up-Fenster einen neuen Port und klicken Sie auf **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** Der Name der Regel, der vom Benutzer festgelegt werden kann.

**Protocol:** Das verwendete Protokoll. Sie können TCP, UDP oder sowohl TCP als auch UDP auswählen.

**Port:** Die Portnummer, die Sie öffnen möchten.

**Enable:** Aktiviert oder deaktiviert die Regel.

## DMZ

Mit DMZ können Sie einen Computer dem Internet direkt aussetzen, sodass alle eingehenden Pakete an diesen Computer weitergeleitet werden.

Aktivieren Sie **Enable DMZ**. Wählen Sie die interne IP-Adresse Ihres Host-Geräts aus, das alle eingehenden Pakete empfangen soll.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
