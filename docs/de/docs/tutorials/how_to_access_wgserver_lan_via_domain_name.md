# Wie greift man vom Client per Domainnamen auf LAN-Geräte des WireGuard-Servers zu?

Dieses Tutorial erklärt, wie Sie vom Client aus per Domainnamen auf Heimgeräte (z. B. NAS, IP-Kamera usw.) im LAN des WireGuard-Servers zugreifen.

## Topologie

Wie unten dargestellt, können Sie von einem PC im LAN des Clients aus per jeweiligem Domainnamen auf Geräte wie NAS oder IP-Kamera im LAN des WireGuard-Servers zugreifen.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Einrichtungsschritte

### 1. Hosts auf dem Server bearbeiten (optional)

Dieser Schritt gilt, wenn Ihr VPN-Server lokale Domainnamen nicht korrekt auflösen kann. Wenn Sie sich nicht sicher sind, überspringen Sie diesen Schritt.

Melden Sie sich am webbasierten Admin Panel Ihres VPN-Server-Routers an und navigieren Sie zu **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Geben Sie die IP-Adresse und den Domainnamen der Heimgeräte ein, auf die Sie zugreifen möchten, und klicken Sie anschließend auf **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Fernzugriff auf das LAN auf dem Server erlauben

??? "Für Server-Router mit Firmware v4.8"

    Navigieren Sie im webbasierten Admin Panel des Servers zu **VPN** -> **WireGuard Server**. Klicken Sie oben rechts auf **Options**.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Aktivieren Sie **Allow Remote Access the LAN Subnet** und klicken Sie auf **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Wenn diese Option aktiviert ist, kann per VPN aus der Ferne auf diesen Router und die LAN-Geräte zugegriffen werden.**
 
??? "Für Server-Router mit Firmware v4.7 und früher"

    Navigieren Sie im webbasierten Admin Panel des Servers zu **VPN** -> **VPN Dashboard** -> Abschnitt **VPN Server**. Klicken Sie auf der rechten Seite des WireGuard-Servers auf das Zahnradsymbol.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Aktivieren Sie **Remote Access LAN** und klicken Sie auf **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Wenn diese Option aktiviert ist, kann per VPN aus der Ferne auf diesen Router und die LAN-Geräte zugegriffen werden.**

### 3. VPN-Konfiguration exportieren

Navigieren Sie im Admin Panel des Servers zu **VPN** -> **WireGuard Server** -> Registerkarte **Profiles** und klicken Sie auf **Add**, um ein Konfigurationsprofil zu exportieren.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Anschließend erhalten Sie eine **.conf**-Datei, wie unten gezeigt.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Öffnen Sie diese Datei. Stellen Sie sicher, dass das DNS-Feld in der Datei auf die Tunnel-IP des Servers verweist, die wie unten gezeigt auf der Registerkarte **Configuration** der Seite WireGuard Server angezeigt wird. Löschen Sie außerdem gegebenenfalls `64.6.64.6` aus dem DNS-Feld, um Fehler bei der DNS-Auflösung zu vermeiden.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Hinweis**: Die Tunnel-IP des WireGuard-Servers unterscheidet sich je nach Firmware-Version. Prüfen Sie bitte die Tunnel-IP Ihres Servers.

### 4. VPN-Server aktivieren

Klicken Sie auf der Seite **WireGuard Server** oben rechts auf die Schaltfläche **Start**, um den Server zu starten.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. VPN-Konfiguration hochladen

Melden Sie sich am webbasierten Admin Panel Ihres VPN-Client-Routers an, navigieren Sie zu **VPN** -> **WireGuard Client** und klicken Sie dann auf **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Erstellen Sie einen Namen für diese Gruppe und laden Sie die Konfigurationsdatei hoch.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Der Upload war erfolgreich. Klicken Sie auf **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Die Konfigurationsdatei wird nun hier aufgelistet.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. VPN-Client-Verbindung starten

Klicken Sie auf das Drei-Punkte-Symbol, um die VPN-Verbindung zu starten.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Wenn der graue Punkt grün wird, hat sich der WireGuard-Client erfolgreich mit dem Server verbunden.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Jetzt können Sie von einem PC im LAN des Clients per Domainnamen auf Ihre Heimgeräte (z. B. NAS) im LAN des Servers zugreifen.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
