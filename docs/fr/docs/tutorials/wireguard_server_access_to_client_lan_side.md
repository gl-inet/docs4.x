# Comment accéder au côté LAN du client WireGuard depuis le serveur

Ce tutoriel présente les étapes pour accéder au sous-réseau LAN d'un client WireGuard (caméra IP, NAS, etc.) depuis le côté serveur WireGuard.

## Topologie

Comme illustré ci-dessous, le GL-MT2500 est un serveur WireGuard et le GL-AXT1800 est un client WireGuard qui y est connecté. Vous pouvez accéder aux appareils du côté LAN du GL-AXT1800 (caméra IP ou NAS) depuis le côté serveur.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Ajouter une règle de routage sur le serveur

??? "Pour le firmware v4.7 et antérieur"

    Connectez-vous au panneau d'administration web de <u>votre serveur WireGuard</u>, puis accédez à **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Cliquez sur l'icône de routage à droite pour accéder à la règle de routage.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Cliquez sur **Add Route Rule** en haut à droite, puis saisissez le sous-réseau auquel vous souhaitez accéder.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Par exemple, le sous-réseau LAN du client WireGuard GL-AXT1800 est **192.168.8.0/24**, donc **Target Address** est **192.168.8.0/24**.
    
    **Gateway** correspond à l'IP virtuelle du client que votre serveur WireGuard a générée pour ce client WireGuard. Vous pouvez la trouver dans l'onglet **Profiles** de la page **WireGuard Server**. Comme indiqué ci-dessous, l'IP du client pour le client WireGuard GL-AXT1800 est **10.0.0.4**.
    
    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}
    
    Définissez donc **Gateway** sur **10.0.0.4** et **Scope** sur **global**, puis cliquez sur **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Pour le firmware v4.8 et supérieur"

    Connectez-vous au panneau d'administration web de <u>votre serveur WireGuard</u>, puis accédez à **VPN** -> **WireGuard Server**.

    Cliquez sur l'onglet **Route Rules**, puis sur **Add Route Rule** à droite.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, saisissez le sous-réseau auquel vous souhaitez accéder.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Par exemple, le sous-réseau LAN du client WireGuard GL-AXT1800 est **192.168.8.0/24**, donc **Target Address** est **192.168.8.0/24**.
    
    **Gateway** correspond à l'IP virtuelle du client que votre serveur WireGuard a générée pour ce client WireGuard. Vous pouvez la trouver dans l'onglet **Profiles** sur la même page. Comme indiqué ci-dessous, l'IP du client pour le client WireGuard GL-AXT1800 est **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Définissez donc **Gateway** sur **10.1.0.2**, puis cliquez sur **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Autoriser l'accès à distance au LAN du client

??? "Pour le firmware v4.7 et antérieur"

    Connectez-vous au panneau d'administration web de <u>votre client WireGuard</u>, puis accédez à **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Cliquez sur l'icône en forme d'engrenage à droite de WireGuard.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez **Remote Access LAN**, puis cliquez sur **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Pour le firmware v4.8 et supérieur"

    Connectez-vous au panneau d'administration web de <u>votre client WireGuard</u>, puis accédez à **VPN** -> **VPN Dashboard**.

    Dans l'angle supérieur gauche de votre tunnel VPN, cliquez sur l'icône en forme d'engrenage pour accéder aux options du tunnel.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez **Allow Remote Access the LAN Subnet**, puis cliquez sur **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Tester la connexion

Vérifiez si vous pouvez accéder aux appareils LAN de votre client WireGuard depuis le côté serveur.

Vous pouvez tester la connexion via ping. Par exemple, depuis un appareil connecté au serveur WireGuard (GL-MT2500), effectuez un ping vers l'adresse IP d'un appareil du LAN de votre client WireGuard (GL-AXT1800) et vérifiez si le ping réussit.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
