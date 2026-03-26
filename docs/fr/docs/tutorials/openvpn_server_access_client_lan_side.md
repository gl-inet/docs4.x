# Comment accéder au LAN du client OpenVPN depuis le serveur

Ce tutoriel présente les étapes pour accéder au sous-réseau LAN du client OpenVPN (tel qu'un NAS, une caméra IP, etc.) depuis votre serveur OpenVPN.

## Topologie

Comme indiqué ci-dessous, le GL-AXT1800 est un serveur OpenVPN et le GL-MT2500 est un client OpenVPN connecté à celui-ci. Vous pouvez accéder aux appareils situés côté LAN du GL-MT2500 (tel qu'un NAS ou le GL-MT3000, un sous-routeur) depuis le côté serveur.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Ajouter une règle de routage sur le serveur

??? "Pour le firmware v4.7 et les versions antérieures"

    Connectez-vous au panneau d'administration web de <u>votre serveur OpenVPN</u>, puis accédez à **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Cliquez sur l'icône de routage à droite pour accéder à la règle de routage.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    Dans la fenêtre contextuelle, cliquez sur le bouton **Add Route Rule** à droite, puis saisissez le sous-réseau auquel vous souhaitez accéder.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Par exemple, le sous-réseau LAN du client OpenVPN GL-MT2500 est **192.168.48.0/24**, donc l'Adresse cible est **192.168.48.0/24**. 
    
    La Passerelle est l'IP client que votre serveur OpenVPN a générée pour ce client OpenVPN. Ici, nous définissons la Passerelle sur **10.8.0.1**, puis cliquons sur **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Remarque : Si vous avez plusieurs clients OpenVPN dont les sous-réseaux LAN doivent être accessibles, veuillez consulter [ce lien](reserve_fixed_IP_for_ovpn_client.md) pour réserver une IP client pour chaque client OpenVPN avant de définir les règles de routage.

??? "Pour le firmware v4.8 et les versions ultérieures"

    Connectez-vous au panneau d'administration web de <u>votre serveur OpenVPN</u>, puis accédez à **VPN** -> **OpenVPN Server**.

    Cliquez sur l'onglet **Route Rules**, puis sur le bouton **Add Route Rule** à droite.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, saisissez le sous-réseau auquel vous souhaitez accéder.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Par exemple, le sous-réseau LAN du client OpenVPN GL-MT2500 est **192.168.48.0/24**, donc l'Adresse cible est **192.168.48.0/24**. 
    
    La Passerelle est l'IP client que votre serveur OpenVPN a générée pour ce client OpenVPN. Ici, nous définissons la Passerelle sur **10.8.0.2**, puis cliquons sur **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Remarque : Si vous avez plusieurs clients OpenVPN dont les sous-réseaux LAN doivent être accessibles, veuillez consulter [ce lien](reserve_fixed_IP_for_ovpn_client.md) pour réserver une IP client pour chaque client OpenVPN avant de définir les règles de routage.

## 2. Autoriser l'accès à distance au LAN du client

??? "Pour le firmware v4.7 et les versions antérieures"

    Connectez-vous au panneau d'administration web de <u>votre client OpenVPN</u>, puis accédez à **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Cliquez sur l'icône d'engrenage pour accéder aux options du client.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez **Remote Access LAN**, puis cliquez sur **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Pour le firmware v4.8 et les versions ultérieures"

    Connectez-vous au panneau d'administration web de <u>votre client OpenVPN</u>, puis accédez à **VPN** -> **VPN Dashboard**.

    Dans l'angle supérieur gauche de votre tunnel VPN, cliquez sur l'icône d'engrenage pour accéder aux options du tunnel.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez **Allow Remote Access the LAN Subnet**, puis cliquez sur **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Tester la connexion

Voici un exemple d'accès au GL-MT3000 (un appareil dans le LAN du client OpenVPN) avec l'IP **192.168.48.211**.

Sur un appareil connecté à votre serveur OpenVPN, envoyez un ping à l'adresse IP **192.168.48.211** du GL-MT3000. Il s'agit de l'adresse IP que le client OpenVPN (GL-MT2500) attribue au GL-MT3000 dans son LAN.

Si vous pouvez effectuer le ping avec succès, cela signifie que les paramètres sont corrects. Vous pourrez accéder à tous les autres appareils du sous-réseau LAN du client OpenVPN via leurs adresses IP.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
