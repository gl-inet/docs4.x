# Configurer le client WireGuard sur les routeurs GL.iNet

**Remarque** : ce guide s'applique au firmware v4.7 et aux versions ultérieures. Pour les versions antérieures, veuillez consulter [cette page](wireguard_client_v4.6.md).

---

WireGuard® est un VPN extrêmement simple, rapide et moderne qui utilise une cryptographie de pointe. Il vise à être plus rapide, plus simple, plus léger et plus pratique qu'IPsec, tout en évitant sa complexité. Il offre également de meilleures performances qu'OpenVPN.

Pour configurer un client WireGuard sur un routeur GL.iNet, regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Avant de commencer, assurez-vous de disposer d'un abonnement actif auprès d'un fournisseur VPN prenant en charge la configuration manuelle WireGuard. Cliquez [ici](https://www.gl-inet.com/solutions/vpn/){target="_blank"} pour consulter la liste des fournisseurs WireGuard compatibles avec GL.iNet.

En général, vous devez d'abord vous rendre sur le site officiel du fournisseur VPN auquel vous avez souscrit, obtenir le fichier de configuration puis le téléverser sur le routeur pour l'utiliser comme client WireGuard. Si vous ne savez pas comment obtenir le fichier de configuration, consultez [ce guide](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) ou contactez son assistance.

Vous pouvez configurer un client WireGuard via le panneau d'administration web ou l'[application mobile](../faq/mobile_app.md). 

- **L'application mobile** intègre certains fournisseurs WireGuard, comme AzireVPN, Mullvad VPN, OVPN, StrongVPN ou PIA VPN. Vous pouvez donc effectuer la configuration simplement en saisissant les identifiants du service WireGuard auquel vous êtes abonné. Ouvrez l'application et suivez les instructions à l'écran.

- **Le panneau d'administration web** intègre non seulement certains fournisseurs WireGuard, mais propose aussi une entrée pour la configuration manuelle. Vous pouvez soit saisir les identifiants de votre service WireGuard pour une configuration rapide, soit téléverser manuellement un fichier de configuration.

Vous trouverez ci-dessous les étapes de configuration via le panneau d'administration web. Sélectionnez le fournisseur WireGuard correspondant pour accéder rapidement aux instructions détaillées.

* [Configurer AzireVPN](#set-up-azirevpn)
* [Configurer Hide.me](#set-up-hideme)
* [Configurer IPVanish](#set-up-ipvanish)
* [Configurer Mullvad](#set-up-mullvad)
* [Configurer NordVPN](#set-up-nordvpn)
* [Configurer PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Configurer PureVPN](#set-up-purevpn)
* [Configurer Surfshark](#set-up-surfshark)
* [Configurer manuellement le client WireGuard (autres fournisseurs)](#set-up-wireguard-client-manually-for-other-providers)

## Configurer AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

Regardez cette vidéo pour configurer AzireVPN sur les routeurs GL.iNet via le panneau d'administration web ou l'application mobile.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ou suivez les étapes ci-dessous pour configurer AzireVPN via le panneau d'administration web.

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}
    
    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Renouveler l'abonnement.

    Si vous cliquez sur **Go Renew**, vous serez redirigé vers le site officiel afin de renouveler votre abonnement.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Configurer Hide.me {#set-up-hideme}

[Site officiel](https://www.hideipvpn.com/){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Configurer IPVanish {#set-up-ipvanish}

[Site officiel](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Sélectionner les serveurs.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Configurer Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} is a VPN service that helps keep your online activity, identity, and location private.

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Saisissez **Account**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Sélectionner les serveurs.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}
    
    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Renouveler l'abonnement.

    Si vous cliquez sur **Go Renew**, vous serez redirigé vers le site officiel afin de renouveler votre abonnement.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Configurer NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is an online VPN service that combines speed and security.

1. Cliquez [ici](https://my.nordaccount.com/){target="_blank"} pour vous connecter à votre compte web NordVPN.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}
    
    Après vous être connecté au Nord Dashboard, cliquez sur **NordVPN** dans le menu de gauche, repérez la section **Access Token**, puis cliquez sur **Get Access token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

    Sur la page suivante, cliquez sur **Generate new token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

    Dans la fenêtre pop-up, sélectionnez la date d'expiration du token, puis cliquez sur **Generate token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

    Le token d'accès s'affichera alors. Copiez-le pour l'utiliser plus tard.

    **Remarque** : le token d'accès ne s'affiche qu'une seule fois. Assurez-vous de le copier et de l'utiliser maintenant. Après avoir fermé cette fenêtre, il ne sera plus visible. Si vous ne l'enregistrez pas, vous devrez générer un nouveau token.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Connectez-vous au panneau d'administration web du routeur, puis accédez à **VPN** -> **WireGuard Client** -> **NordVPN**. 

    Saisissez **Token**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Select servers.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Configurer PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Site officiel](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **PIA**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Sélectionner les serveurs.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Configurer PureVPN {#set-up-purevpn}

[Site officiel](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **PureVPN**.

1. Input **Username** and **Password**, then click **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Le système générera tous les fichiers de configuration disponibles.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Configurer Surfshark {#set-up-surfshark}

[Site officiel](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Sélectionner les serveurs.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Actualiser.

    Vous pouvez cliquer sur **Refresh** pour mettre à jour la clé publique lorsqu'il est impossible de se connecter au serveur VPN.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Configurer Windscribe {#set-up-windscribe}

[Site officiel](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

Dans le panneau d'administration web, accédez à **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Saisissez **Username** et **Password**, puis cliquez sur **Save and Continue**. Le système générera des fichiers de configuration pour chaque serveur.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Sélectionner les serveurs.

    Sélectionnez le ou les serveurs auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Vous obtiendrez ensuite une liste de fichiers de configuration correspondant au serveur sélectionné.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Démarrer une connexion.

    Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Les détails de la connexion VPN s'afficheront alors dans **VPN Dashboard**.

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour obtenir la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à une maintenance ou à l'arrêt de certains serveurs.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Modifier les identifiants ou se déconnecter.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion ou vous déconnecter.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Actualiser.

    Vous pouvez cliquer sur **Refresh** pour mettre à jour la clé publique lorsqu'il est impossible de se connecter au serveur VPN.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Tout supprimer.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un clic, et choisir si vous souhaitez également supprimer simultanément les clés privée et publique.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Configurer manuellement le client WireGuard (autres fournisseurs) {#set-up-wireguard-client-manually-for-other-providers}

Si vous utilisez un autre fournisseur de service WireGuard, vous pouvez télécharger les fichiers de configuration WireGuard puis suivre les étapes ci-dessous pour configurer le client WireGuard. Si vous ne savez pas comment télécharger les fichiers de configuration, consultez [ce guide](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) ou contactez son assistance.

In the web Admin Panel, go to **VPN** -> **WireGuard Client**.

1. Cliquez sur **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Le système créera un groupe dans la barre latérale gauche.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Donnez au groupe un nom explicite (par ex. `azirevpn`). Téléversez ensuite un fichier de configuration (formats pris en charge : zip, tar, gz, conf, txt) ou ajoutez manuellement les détails de configuration sous forme de texte.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Téléverser un fichier de configuration**.

        Cliquez dans la zone de téléversement pour importer votre fichier de configuration WireGuard, puis cliquez sur **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Ajouter manuellement une configuration**.
    
        Cliquez sur **Manually Add Configuration** en bas de la zone de téléversement.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Donnez un nom explicite, puis collez la configuration dans la zone de texte. Cliquez ensuite sur **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Mode texte)</small>

        Si vous souhaitez vérifier chaque élément, vous pouvez passer en mode Item et vérifier les détails de la configuration. Cliquez ensuite sur **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Mode Item)</small>

4. Cliquez sur l'icône à trois points située à droite pour démarrer la connexion.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Une fois connecté, vous pouvez vérifier l'état de la connexion sur la page **VPN Dashboard**.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Configurer un serveur WireGuard sur un routeur GL.iNet

Vous ne souhaitez pas vous abonner à un service VPN tiers ? Vous pouvez acheter deux routeurs GL.iNet : configurer l'un comme serveur WireGuard et l'autre comme client WireGuard.

Cette configuration est particulièrement adaptée si votre FAI domestique fournit une IP publique et que vous souhaitez vous connecter à votre réseau domestique via VPN lorsque vous êtes absent, afin d'assurer la sécurité et l'accès aux ressources du réseau interne. Cela évite le coût et les contraintes d'un abonnement continu à des services VPN commerciaux.

Pour la configuration du serveur WireGuard, veuillez consulter [ce guide](wireguard_server.md).

---

WireGuard® est une marque déposée de Jason A. Donenfeld.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
