# Wie greift man vom Server auf das Client-LAN von OpenVPN zu?

Dieses Tutorial beschreibt die Schritte, mit denen Sie von der OpenVPN-Serverseite aus auf das LAN-Subnetz eines OpenVPN-Clients (z. B. NAS, IP-Kamera usw.) zugreifen.

## Topologie

Wie unten dargestellt, ist der GL-AXT1800 ein OpenVPN-Server und der GL-MT2500 ein damit verbundener OpenVPN-Client. Sie können von der Serverseite aus auf die Geräte im LAN des GL-MT2500 zugreifen (z. B. NAS oder GL-MT3000 als Unterrouter).

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Routing-Regel auf dem Server hinzufügen

??? "Für Firmware v4.7 und früher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres OpenVPN-Servers</u> an und gehen Sie zu **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Klicken Sie rechts auf das Routing-Symbol, um die Routing-Regeln zu öffnen.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    Klicken Sie im Pop-up-Fenster rechts auf **Add Route Rule** und geben Sie das Subnetz ein, auf das Sie zugreifen möchten.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Das LAN-Subnetz des OpenVPN-Clients GL-MT2500 ist zum Beispiel **192.168.48.0/24**, daher ist die Target Address **192.168.48.0/24**.

    Gateway ist die Client-IP, die Ihr OpenVPN-Server für diesen OpenVPN-Client erzeugt hat. Hier setzen wir das Gateway auf **10.8.0.1** und klicken anschließend auf **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Hinweis: Wenn Sie mehrere OpenVPN-Clients haben, deren LAN-Subnetze erreichbar sein sollen, lesen Sie bitte [diesen Artikel](reserve_fixed_IP_for_ovpn_client.md), um vor dem Setzen der Routing-Regeln für jeden OpenVPN-Client eine feste Client-IP zu reservieren.

??? "Für Firmware v4.8 und höher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres OpenVPN-Servers</u> an und gehen Sie zu **VPN** -> **OpenVPN Server**.

    Klicken Sie auf die Registerkarte **Route Rules** und anschließend rechts auf **Add Route Rule**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    Geben Sie im Pop-up-Fenster das Subnetz ein, auf das Sie zugreifen möchten.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Das LAN-Subnetz des OpenVPN-Clients GL-MT2500 ist zum Beispiel **192.168.48.0/24**, daher ist die Target Address **192.168.48.0/24**.

    Gateway ist die Client-IP, die Ihr OpenVPN-Server für diesen OpenVPN-Client erzeugt hat. Hier setzen wir das Gateway auf **10.8.0.2** und klicken anschließend auf **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Hinweis: Wenn Sie mehrere OpenVPN-Clients haben, deren LAN-Subnetze erreichbar sein sollen, lesen Sie bitte [diesen Artikel](reserve_fixed_IP_for_ovpn_client.md), um vor dem Setzen der Routing-Regeln für jeden OpenVPN-Client eine feste Client-IP zu reservieren.

## 2. Fernzugriff auf das Client-LAN erlauben

??? "Für Firmware v4.7 und früher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres OpenVPN-Clients</u> an und gehen Sie zu **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Klicken Sie auf das Zahnradsymbol, um die Client-Optionen zu öffnen.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    Aktivieren Sie im Pop-up-Fenster **Remote Access LAN** und klicken Sie anschließend auf **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Für Firmware v4.8 und höher"

    Melden Sie sich am webbasierten Admin Panel <u>Ihres OpenVPN-Clients</u> an und gehen Sie zu **VPN** -> **VPN Dashboard**.

    Klicken Sie oben links an Ihrem VPN-Tunnel auf das Zahnradsymbol, um die Tunnel-Optionen zu öffnen.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    Aktivieren Sie im Pop-up-Fenster **Allow Remote Access the LAN Subnet** und klicken Sie anschließend auf **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Verbindung testen

Hier sehen Sie ein Beispiel für den Zugriff auf den GL-MT3000 (ein Gerät im LAN des OpenVPN-Clients) mit der IP **192.168.48.211**.

Pingen Sie auf einem Gerät, das mit Ihrem OpenVPN-Server verbunden ist, die IP-Adresse des GL-MT3000 **192.168.48.211** an. Dies ist die IP-Adresse, die der OpenVPN-Client (GL-MT2500) dem GL-MT3000 in seinem LAN zuweist.

Wenn der Ping erfolgreich ist, sind die Einstellungen korrekt. Sie können dann über deren IP-Adressen auf alle weiteren Geräte im LAN-Subnetz des OpenVPN-Clients zugreifen.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
