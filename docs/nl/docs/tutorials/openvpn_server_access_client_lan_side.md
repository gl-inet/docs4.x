# Vanaf de server toegang krijgen tot de LAN-zijde van de OpenVPN-client {#how-to-access-openvpn-client-lan-side-from-server}

In deze handleiding lees je hoe je vanaf de OpenVPN-serverzijde toegang krijgt tot het LAN-subnet van de OpenVPN-client, bijvoorbeeld een NAS of IP-camera.

## Topologie {#topology}

Zoals hieronder weergegeven, is de GL-AXT1800 een OpenVPN-server en de GL-MT2500 een OpenVPN-client die ermee is verbonden. Vanaf de serverzijde heb je toegang tot apparaten aan de LAN-zijde van de GL-MT2500, zoals een NAS of GL-MT3000 als subrouter.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Een routeringsregel toevoegen op de server {#1-add-route-rule-on-server}

??? "Voor firmware v4.7 en ouder"

    Meld je aan bij het webbeheerpaneel van <u>je OpenVPN-server</u> en ga naar **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Klik rechts op het routepictogram om de routeringsregel te openen.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    Klik in het pop-upvenster rechts op **Add Route Rule** en voer het subnet in waartoe je toegang wilt.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Het LAN-subnet van OpenVPN-client GL-MT2500 is bijvoorbeeld **192.168.48.0/24**, zodat Target Address **192.168.48.0/24** is.

    Gateway is het Client IP dat je OpenVPN-server voor deze OpenVPN-client heeft gegenereerd. In dit voorbeeld stellen we Gateway in op **10.8.0.1**. Klik vervolgens op **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Opmerking: als je meerdere OpenVPN-clients hebt waarvan de LAN-subnetten toegankelijk moeten zijn, volg je [deze handleiding](reserve_fixed_IP_for_ovpn_client.md) om voor elke OpenVPN-client een Client IP te reserveren voordat je de routeringsregels instelt.

??? "Voor firmware v4.8 en nieuwer"

    Meld je aan bij het webbeheerpaneel van <u>je OpenVPN-server</u> en ga naar **VPN** -> **OpenVPN Server**.

    Klik op het tabblad **Route Rules** en klik vervolgens rechts op **Add Route Rule**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    Voer in het pop-upvenster het subnet in waartoe je toegang wilt.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Het LAN-subnet van OpenVPN-client GL-MT2500 is bijvoorbeeld **192.168.48.0/24**, zodat Target Address **192.168.48.0/24** is.

    Gateway is het Client IP dat je OpenVPN-server voor deze OpenVPN-client heeft gegenereerd. In dit voorbeeld stellen we Gateway in op **10.8.0.2**. Klik vervolgens op **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Opmerking: als je meerdere OpenVPN-clients hebt waarvan de LAN-subnetten toegankelijk moeten zijn, volg je [deze handleiding](reserve_fixed_IP_for_ovpn_client.md) om voor elke OpenVPN-client een Client IP te reserveren voordat je de routeringsregels instelt.

## 2. Externe toegang tot het client-LAN toestaan {#2-allow-remote-access-to-client-lan}

??? "Voor firmware v4.7 en ouder"

    Meld je aan bij het webbeheerpaneel van <u>je OpenVPN-client</u> en ga naar **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Klik op het tandwielpictogram om de clientopties te openen.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Remote Access LAN** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Voor firmware v4.8"

    Meld je aan bij het webbeheerpaneel van <u>je OpenVPN-client</u> en ga naar **VPN** -> **VPN Dashboard**.

    Klik linksboven in je VPN-tunnel op het tandwielpictogram om de tunnelopties te openen.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "Voor firmware v4.9 en nieuwer"

    Meld je aan bij het webbeheerpaneel van <u>je OpenVPN-client</u> en ga naar **VPN** -> **VPN Dashboard**.

    Klik in een tunnelgroep op het tandwielpictogram en selecteer **Options**.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}


## 3. De verbinding testen {#3-test-connection}

Hier volgt een voorbeeld van toegang tot de GL-MT3000, een apparaat in het LAN van de OpenVPN-client, met IP-adres **192.168.48.211**.

Ping op een apparaat dat met je OpenVPN-server is verbonden het IP-adres **192.168.48.211** van de GL-MT3000. Dit is het IP-adres dat OpenVPN-client GL-MT2500 in zijn LAN aan de GL-MT3000 toewijst.

Als de ping slaagt, zijn de instellingen correct. Toegang tot diensten op dit apparaat of andere apparaten in het LAN-subnet van de OpenVPN-client hangt echter ook af van de firewallinstellingen en de configuratie van diensten op elk apparaat.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
