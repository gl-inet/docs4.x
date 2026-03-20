# Wie greift man vom Client per Domainnamen auf LAN-Geräte des OpenVPN-Servers zu?

Dieses Tutorial erklärt, wie Sie vom Client aus per Domainnamen auf Heimgeräte (z. B. NAS, IP-Kamera usw.) im LAN des OpenVPN-Servers zugreifen.

## Topologie

Wie unten dargestellt, können Sie von einem PC im LAN des Clients aus per jeweiligem Domainnamen auf Geräte wie NAS oder IP-Kamera im LAN des OpenVPN-Servers zugreifen.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Einrichtungsschritte

### 1. Hosts auf dem Server bearbeiten (optional)

Dieser Schritt gilt, wenn Ihr VPN-Server lokale Domainnamen nicht korrekt auflösen kann. Wenn Sie sich nicht sicher sind, überspringen Sie diesen Schritt.

Melden Sie sich am webbasierten Admin Panel Ihres VPN-Server-Routers an und navigieren Sie zu **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Geben Sie die IP-Adresse und den Domainnamen der Heimgeräte ein, auf die Sie zugreifen möchten, und klicken Sie anschließend auf **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Fernzugriff auf das LAN auf dem Server erlauben

Navigieren Sie im webbasierten Admin Panel des Servers zu **VPN** -> **OpenVPN Server**. Klicken Sie oben rechts auf **Options**.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Aktivieren Sie **Allow Remote Access the LAN Subnet** und klicken Sie auf **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Wenn diese Option aktiviert ist, kann per VPN aus der Ferne auf den Router und die LAN-Geräte zugegriffen werden.

### 3. VPN-Konfiguration exportieren

Navigieren Sie im Admin Panel des Servers zu **VPN** -> **OpenVPN Server** -> Registerkarte **Configuration** und klicken Sie unten auf **Export Client Configuration**.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

Klicken Sie im Pop-up-Fenster auf **Export**.

**Hinweis**: Wenn die öffentliche IP-Adresse Ihres Servers dynamisch ist und sich gelegentlich ändert, aktivieren Sie bitte vor dem Export der Client-Konfiguration unter **APPLICATIONS** -> **Dynamic DNS** die Funktion **DDNS**.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Anschließend erhalten Sie eine **.ovpn**-Datei, wie unten gezeigt.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Wenn auf Ihrem Server-Router Firmware v4.8 oder neuer läuft, müssen Sie die Konfigurationsdatei nicht bearbeiten und können mit dem nächsten Schritt fortfahren.

Wenn auf Ihrem Server-Router Firmware v4.7 oder älter läuft, öffnen Sie diese Datei, fügen Sie die folgende Zeile hinzu, um den DNS-Server auf die Tunnel-IP Ihres OpenVPN-Servers zu setzen, und speichern Sie anschließend die Änderungen.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Tipp: Das IPv4-Tunnel-Subnetz des OpenVPN-Servers finden Sie wie unten dargestellt auf der Registerkarte **Configuration** der Seite OpenVPN Server. Es variiert je nach Firmware-Version. Prüfen Sie bitte die Tunnel-IP Ihres OpenVPN-Servers.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. VPN-Server aktivieren

Klicken Sie auf der Seite **OpenVPN Server** oben rechts auf die Schaltfläche **Start**, um den Server zu starten.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. VPN-Konfiguration hochladen

Melden Sie sich am webbasierten Admin Panel Ihres VPN-Client-Routers an, navigieren Sie zu **VPN** -> **OpenVPN Client** und klicken Sie dann auf **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Erstellen Sie einen Namen für diese Gruppe und laden Sie die Konfigurationsdatei hoch.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Der Upload war erfolgreich. Klicken Sie auf **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Die Konfigurationsdatei wird nun hier aufgelistet.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. VPN-Client-Verbindung starten

Klicken Sie auf das Drei-Punkte-Symbol, um die VPN-Verbindung zu starten.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Wenn der graue Punkt grün wird, hat sich der OpenVPN-Client erfolgreich mit dem Server verbunden.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Jetzt können Sie von einem PC im LAN des Clients per Domainnamen auf Ihre Heimgeräte (z. B. NAS) im LAN des Servers zugreifen.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
