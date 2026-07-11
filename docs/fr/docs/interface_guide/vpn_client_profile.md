# Profil client VPN

> Ce guide s'applique au firmware v4.9 et aux versions ultérieures.

Sur la partie gauche du panneau d'administration web, accédez à **VPN** -> **VPN Client Profile**.

Depuis le firmware v4.9, [OpenVPN Client](openvpn_client.md) et [WireGuard Client](wireguard_client.md) ont été fusionnés dans une seule page **VPN Client Profile** pour une gestion plus fluide. La présentation a été légèrement ajustée, mais les fonctionnalités principales restent inchangées. Vous pouvez toujours consulter les guides séparés si nécessaire.

Cette page vous permet de vous connecter à certains services VPN intégrés et de télécharger facilement leurs profils pour établir une connexion VPN, ou de téléverser manuellement vos fichiers de configuration exportés depuis le site web d'un autre fournisseur VPN. Vous pouvez changer de protocole VPN dans l'angle supérieur droit si nécessaire.

## WireGuard

WireGuard® est un VPN moderne, léger et haute performance, conçu avec une cryptographie de pointe. Il offre une vitesse, une simplicité et une efficacité supérieures à IPsec, tout en surpassant nettement OpenVPN.

Les routeurs GL.iNet offrent une prise en charge WireGuard intégrée pour les fournisseurs VPN suivants. Si vous disposez d'un abonnement actif, saisissez simplement vos identifiants de service sur la page **VPN Client Profile** pour terminer rapidement la configuration.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

Si vous êtes abonné à un autre fournisseur de services WireGuard, téléchargez un fichier de configuration depuis son site web, puis cliquez sur **Add Manually** pour l'importer dans votre routeur et établir la connexion VPN. Si vous ne savez pas comment télécharger les fichiers de configuration, reportez-vous [ici](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) ou contactez leur assistance.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Prenons [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} comme exemple.

1. Cliquez sur **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Saisissez votre **Username** et votre **Password**, puis cliquez sur **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    Le système générera des fichiers de configuration pour tous les serveurs disponibles.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Suivez ensuite les instructions correspondant à votre besoin réel.

    !!! note "Cas 1. Si vous voulez que tous les clients connectés utilisent le VPN pour accéder à Internet, suivez ces étapes."
    
        1. Sélectionnez votre serveur préféré, puis cliquez sur l'icône à trois points à droite pour démarrer la connexion.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Une fois connecté, un point vert apparaîtra à côté du fichier de configuration.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            La connexion VPN est alors activée, et tous les clients connectés à ce routeur devraient utiliser le VPN pour accéder à Internet de manière sécurisée.

        3. (Facultatif) Si vous souhaitez que le système coupe automatiquement tout accès Internet pour votre réseau local en cas d'échec inattendu de la connexion VPN, empêchant ainsi l'exposition de votre véritable adresse IP et de vos données en ligne, et garantissant une confidentialité et une sécurité continues, accédez à **VPN Dashboard** pour activer le **Kill Switch**.

            * Pour configurer le Kill Switch pour chaque tunnel VPN individuel, référez-vous à [cette section](vpn_dashboard.md#tunnel-options).

            * Pour configurer le Kill Switch pour la connexion VPN globale (c'est-à-dire le Kill Switch amélioré), référez-vous à [cette section](vpn_dashboard.md#all-other-traffic).

    !!! note "Cas 2. Si vous préférez personnaliser la politique VPN, suivez ces étapes."
    
        1. Cliquez sur **Go to Dashboard** en bas de la page.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Vous serez alors redirigé vers **VPN Dashboard** pour configurer la politique VPN. Cliquez [ici](vpn_dashboard.md#set-up-vpn-policy) pour plus de détails.

## OpenVPN

OpenVPN est un protocole VPN open source qui utilise des techniques de réseau privé virtuel pour établir des connexions sécurisées site à site ou point à point.

Les routeurs GL.iNet offrent une prise en charge OpenVPN intégrée pour [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Si vous disposez d'un abonnement actif, saisissez simplement vos identifiants de service sur la page **VPN Client Profile** pour terminer rapidement la configuration.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Si vous êtes abonné à un autre fournisseur de services OpenVPN, téléchargez un fichier de configuration depuis son site web, puis cliquez sur **Add Manually** pour l'importer dans votre routeur et établir la connexion VPN. Si vous ne savez pas comment télécharger les fichiers de configuration, reportez-vous [ici](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) ou contactez leur assistance.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Articles connexes

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [Configurer le client WireGuard sur les routeurs GL.iNet](wireguard_client.md)
- [Configurer le client OpenVPN sur les routeurs GL.iNet](openvpn_client.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
