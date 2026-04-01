# Comment acheminer les requêtes DNS du client VPN vers le DNS amont du serveur VPN ?

Ce tutoriel présente les étapes permettant de rediriger toutes les requêtes DNS des clients VPN vers votre serveur DNS auto-hébergé sur le côté LAN de votre routeur principal, en amont du serveur VPN.

## Topologie

Dans ce tutoriel, nous utilisons **Flint 3 (GL-BE9300)** et **Slate 7 (GL-BE3600)** comme exemples. 

Flint 3 est le serveur VPN, qui a un routeur principal sur son réseau amont, et Slate 7 est le client VPN qui se connecte à Flint 3.

Lorsqu'un tunnel VPN est établi entre le serveur et le client VPN, par défaut, les requêtes DNS du client VPN sont d'abord envoyées au serveur VPN, puis transférées au routeur principal, et enfin résolues par les serveurs DNS attribués par le fournisseur d'accès Internet configurés sur le WAN du routeur principal.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Cependant, si vous avez déployé un serveur DNS auto-hébergé (adresse IP `192.168.1.13`) sur le routeur principal, des configurations supplémentaires sont nécessaires pour acheminer les requêtes DNS vers ce serveur DNS auto-hébergé.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Configuration

1. Connectez-vous au panneau d'administration web du Flint 3, accédez à **NETWORK** -> **DNS**. Basculez le mode serveur DNS (**DNS Server Mode**) sur **Manual DNS**, puis saisissez l'adresse IP de votre serveur DNS.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Accédez à **VPN** -> **WireGuard Server** -> onglet **Configuration**, puis notez l'adresse IPv4 (**IPv4 Address**), qui est généralement `10.0.0.1/24` ou `10.1.0.1/24`, selon les modèles et les versions du firmware.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Passez à l'onglet **Profiles**, ajoutez une configuration client et exportez un profil pour Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Ouvrez le profil, puis assurez-vous que le DNS correspond à l'adresse IP du serveur VPN obtenue à l'étape 2. 

    Pour éviter un échec de résolution DNS, veuillez supprimer "64.6.64.6" s'il apparaît, puis enregistrez les modifications.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Dans le panneau d'administration web du Flint 3, cliquez sur le bouton **Start** en haut de la page **WireGuard Server** pour démarrer le serveur.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Connectez-vous au panneau d'administration web du Slate 7, puis accédez à **VPN** -> **WireGuard Client**. 

    Cliquez sur **Add Manually** et chargez le profil modifié. 

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Cliquez sur l'icône à trois points pour démarrer la connexion VPN. Si l'indicateur d'état devient vert, cela signifie que la connexion VPN a réussi.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Vérifier la résolution DNS

Exécutez la commande suivante pour capturer le trafic DNS sur le client VPN. Elle montrera que tout le trafic DNS du client VPN est envoyé vers le serveur VPN (c'est-à-dire `10.0.0.1` dans cet exemple).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Exécutez la commande suivante pour capturer le trafic DNS sur le serveur VPN. Elle montrera que tout le trafic DNS du client VPN est finalement envoyé vers le serveur DNS auto-hébergé (c'est-à-dire `192.168.1.13` dans cet exemple).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
