# Portweiterleitung

Diese Seite ist seit Firmware v4.6 verfügbar. Für frühere Versionen lesen Sie bitte [Firewall](firewall.md).

---

Gehen Sie in der Web-Adminoberfläche auf der linken Seite zu **NETWORK** -> **Port Forwarding**. In Firmware v4.9 finden Sie dies unter **SECURITY** -> **Port Forwarding**.

Auf dieser Seite können Sie Firewall-Regeln konfigurieren, darunter **DMZ** und **Port Forwarding**.

Hinweis: Wenn Sie Ports auf Ihrem Router öffnen möchten, gehen Sie bitte zu **SYSTEM** -> **Security** oder zu **SECURITY** -> **Admin Access**.

## DMZ

Mit DMZ können Sie einen Computer direkt für das Internet freigeben, sodass alle eingehenden Pakete an diesen Computer weitergeleitet werden.

Aktivieren Sie **Enable DMZ**. Wählen Sie die interne IP-Adresse Ihres Host-Geräts aus, das alle eingehenden Pakete empfangen soll.

Sie können die Priorität für DMZ festlegen. Wenn die DMZ-Priorität höher ist als die Regeln für die Portweiterleitung, werden alle Regeln für die Portweiterleitung ungültig. Andernfalls werden Anfragen nur dann an das DMZ-Host-Gerät weitergeleitet, wenn für den aufgerufenen Port keine entsprechende Regel für die Portweiterleitung vorhanden ist.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Portweiterleitung

Mit der Portweiterleitung können entfernte Computer eine Verbindung zu einem lokalen Computer oder Server hinter der Firewall des Routers im LAN herstellen (z. B. Webserver, FTP-Server usw.).

Um eine Portweiterleitung einzurichten, klicken Sie im Abschnitt **Port Forwarding** auf **Add**.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Fügen Sie im Pop-up-Fenster eine neue Regel für die Portweiterleitung hinzu und klicken Sie auf **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** Wählen Sie für diese Regel `TCP`, `UDP` oder `TCP and UDP`.

- **External Zone:** Für die externe Zone stehen `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` und `Guest` zur Verfügung.

- **External Port:** Die Nummern der externen Ports. Sie können hier eine bestimmte Portnummer eingeben. Der Portbereich reicht von 1 bis 65535. Sie können einen einzelnen Port festlegen oder einen Portbereich angeben, indem Sie die erste und die letzte Portnummer mit dem Symbol `-` verbinden, z. B. `501-510`.

- **Internal Zone:** Für die interne Zone stehen `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` und `WAN` zur Verfügung.

- **Internal IP:** Die vom Router dem Gerät zugewiesene IP-Adresse, auf das per Fernzugriff zugegriffen werden soll. Wenn Sie unter **External Port** einen einzelnen Port festlegen, sollten Sie hier den einzelnen Port angeben. Wenn Sie unter **External Port** einen Portbereich festlegen, sollten Sie hier den entsprechenden Portbereich angeben.

- **Internal Port:** Die interne Portnummer des Geräts. Sie können eine bestimmte Portnummer eingeben. Lassen Sie das Feld leer, wenn sie mit dem externen Port identisch ist.

- **Description:** Legen Sie einen benutzerdefinierten Namen fest oder fügen Sie eine Beschreibung für diese Regel hinzu (optional).

- **Enable:** Aktivieren oder deaktivieren Sie diese Regel.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
