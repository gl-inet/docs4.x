# Wie greift man vom Server auf das Client-LAN von WireGuard zu?

Dieses Tutorial beschreibt die Schritte, mit denen Sie von der WireGuard-Serverseite aus auf das LAN-Subnetz eines WireGuard-Clients (z. B. IP-Kamera, NAS usw.) zugreifen.

## Topologie

Wie unten dargestellt, ist der GL-MT2500 ein WireGuard-Server und der GL-AXT1800 ein damit verbundener WireGuard-Client. Sie können von der Serverseite aus auf die Geräte im LAN des GL-AXT1800 zugreifen (z. B. IP-Kamera oder NAS).

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Routing-Regel auf dem Server hinzufügen

??? "Für Firmware v4.7 und früher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres WireGuard-Servers</u> an und gehen Sie zu **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Klicken Sie rechts auf das Routing-Symbol, um die Routing-Regeln zu öffnen.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Klicken Sie oben rechts auf **Add Route Rule** und geben Sie das Subnetz ein, auf das Sie zugreifen möchten.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Das LAN-Subnetz des WireGuard-Clients GL-AXT1800 ist zum Beispiel **192.168.8.0/24**, daher ist die Target Address **192.168.8.0/24**.

    Gateway ist die Client-IP, die Ihr WireGuard-Server für diesen WireGuard-Client erzeugt hat. Sie finden sie unter der Registerkarte **Profiles** auf der Seite **WireGuard Server**. Wie unten gezeigt, lautet die Client-IP für den WireGuard-Client GL-AXT1800 **10.0.0.4**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Setzen Sie Gateway daher auf **10.0.0.4** und Scope auf **global** und klicken Sie anschließend auf **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Für Firmware v4.8 und höher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres WireGuard-Servers</u> an und gehen Sie zu **VPN** -> **WireGuard Server**.

    Klicken Sie auf die Registerkarte **Route Rules** und anschließend rechts auf **Add Route Rule**.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    Geben Sie im Pop-up-Fenster das Subnetz ein, auf das Sie zugreifen möchten.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Das LAN-Subnetz des WireGuard-Clients GL-AXT1800 ist zum Beispiel **192.168.8.0/24**, daher ist die Target Address **192.168.8.0/24**.

    Gateway ist die Client-IP, die Ihr WireGuard-Server für diesen WireGuard-Client erzeugt hat. Sie finden sie unter der Registerkarte **Profiles** auf derselben Seite. Wie unten gezeigt, lautet die Client-IP für den WireGuard-Client GL-AXT1800 **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Setzen Sie Gateway daher auf **10.1.0.2** und klicken Sie anschließend auf **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Fernzugriff auf das Client-LAN erlauben

??? "Für Firmware v4.7 und früher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres WireGuard-Clients</u> an und gehen Sie zu **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Klicken Sie rechts neben WireGuard auf das Zahnradsymbol.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    Aktivieren Sie im Pop-up-Fenster **Remote Access LAN** und klicken Sie anschließend auf **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Für Firmware v4.8 und höher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres WireGuard-Clients</u> an und gehen Sie zu **VPN** -> **VPN Dashboard**.

    Klicken Sie oben links an Ihrem VPN-Tunnel auf das Zahnradsymbol, um die Tunnel-Optionen zu öffnen.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    Aktivieren Sie im Pop-up-Fenster **Allow Remote Access the LAN Subnet** und klicken Sie anschließend auf **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Verbindung testen

Prüfen Sie, ob Sie von der Serverseite aus auf die LAN-Geräte Ihres WireGuard-Clients zugreifen können.

Sie können die Verbindung mit `ping` testen. Pingen Sie zum Beispiel auf einem Gerät, das mit dem WireGuard-Server (GL-MT2500) verbunden ist, die IP-Adresse eines Geräts im LAN Ihres WireGuard-Clients (GL-AXT1800) an und prüfen Sie, ob der Ping erfolgreich ist.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
