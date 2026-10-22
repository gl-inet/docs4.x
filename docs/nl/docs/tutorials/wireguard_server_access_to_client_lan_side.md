# Vanaf de server toegang krijgen tot de LAN-zijde van de WireGuard-client {#how-to-access-wireguard-client-lan-side-from-server}

In deze handleiding lees je hoe je vanaf de WireGuard-serverzijde toegang krijgt tot het LAN-subnet van de WireGuard-client, bijvoorbeeld een IP-camera of NAS.

## Topologie {#topology}

Zoals hieronder weergegeven, is de GL-MT2500 een WireGuard-server en de GL-AXT1800 een WireGuard-client die ermee is verbonden. Vanaf de serverzijde heb je toegang tot apparaten aan de LAN-zijde van de GL-AXT1800, zoals een IP-camera of NAS.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Een routeringsregel toevoegen op de server {#1-add-route-rule-on-server}

??? "Voor firmware v4.7 en ouder"

    Meld je aan bij het webbeheerpaneel van <u>je WireGuard-server</u> en ga naar **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Klik rechts op het routepictogram om de routeringsregel te openen.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Klik rechtsboven op **Add Route Rule** en voer het subnet in waartoe je toegang wilt.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Het LAN-subnet van WireGuard-client GL-AXT1800 is bijvoorbeeld **192.168.8.0/24**, zodat Target Address **192.168.8.0/24** is.

    Gateway is het client-IP-adres dat je WireGuard-server voor deze WireGuard-client heeft gegenereerd. Je vindt dit op het tabblad **Profiles** van de pagina **WireGuard Server**. Zoals hieronder weergegeven, is het client-IP-adres voor WireGuard-client GL-AXT1800 **10.0.0.4**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Stel Gateway daarom in op **10.0.0.4** en Scope op **global**. Klik vervolgens op **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Voor firmware v4.8 en nieuwer"

    Meld je aan bij het webbeheerpaneel van <u>je WireGuard-server</u> en ga naar **VPN** -> **WireGuard Server**.

    Klik op het tabblad **Route Rules** en klik vervolgens rechts op **Add Route Rule**.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    Voer in het pop-upvenster het subnet in waartoe je toegang wilt.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Het LAN-subnet van WireGuard-client GL-AXT1800 is bijvoorbeeld **192.168.8.0/24**, zodat Target Address **192.168.8.0/24** is.

    Gateway is het client-IP-adres dat je WireGuard-server voor deze WireGuard-client heeft gegenereerd. Je vindt dit op het tabblad **Profiles** van dezelfde pagina. Zoals hieronder weergegeven, is het client-IP-adres voor WireGuard-client GL-AXT1800 **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Stel Gateway daarom in op **10.1.0.2** en klik op **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Externe toegang tot het client-LAN toestaan {#2-allow-remote-access-to-client-lan}

??? "Voor firmware v4.7 en ouder"

    Meld je aan bij het webbeheerpaneel van <u>je WireGuard-client</u> en ga naar **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Klik rechts van WireGuard op het tandwielpictogram.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Remote Access LAN** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Voor firmware v4.8"

    Meld je aan bij het webbeheerpaneel van <u>je WireGuard-client</u> en ga naar **VPN** -> **VPN Dashboard**.

    Klik linksboven in je VPN-tunnel op het tandwielpictogram om de tunnelopties te openen.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "Voor firmware v4.9 en nieuwer"

    Meld je aan bij het webbeheerpaneel van <u>je WireGuard-client</u> en ga naar **VPN** -> **VPN Dashboard**.

    Klik in een tunnelgroep op het tandwielpictogram en selecteer **Options**.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    Schakel in het pop-upvenster **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}

## 3. De verbinding testen {#3-test-connection}

Controleer of je vanaf de serverzijde toegang hebt tot de LAN-apparaten van je WireGuard-client.

Je kunt de verbinding met ping testen. Ping bijvoorbeeld op een apparaat dat met de WireGuard-server (GL-MT2500) is verbonden het IP-adres van een apparaat in het LAN van je WireGuard-client (GL-AXT1800) en controleer of de ping slaagt.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
