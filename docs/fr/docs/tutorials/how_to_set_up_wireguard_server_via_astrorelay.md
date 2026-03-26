# Comment configurer un serveur WireGuard via AstroRelay ?

Ce tutoriel présente les étapes pour configurer un serveur WireGuard via AstroRelay sur un routeur GL.iNet, idéal pour les utilisateurs qui ont besoin d'un accès à distance à leurs services locaux de domicile ou de bureau mais qui ne disposent pas d'une adresse IP publique de leur FAI.

[AstroRelay](https://www.astrorelay.com){target="_blank"} fournit un tunnel proxy inverse sécurisé, grâce auquel vous pouvez accéder en toute sécurité aux ressources derrière NAT et pare-feu.

1. Suivez [ce guide](../interface_guide/wireguard_server.md) pour configurer un serveur WireGuard sur votre routeur GL.iNet, même si vous ne disposez pas d'une adresse IP publique. 

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Cliquez ensuite sur **Profiles** pour exporter la configuration WireGuard. Voici un exemple de fichier de configuration.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. (Facultatif) Si vous devez accéder au LAN du serveur VPN à distance, activez **Allow Remote Access LAN**. Sinon, ignorez cette étape.

    ??? "Pour le firmware v4.7 et versions antérieures"

        Sur le panneau d'administration web du serveur, allez dans **VPN** -> **VPN Dashboard** -> section **VPN Server**. Cliquez sur l'icône d'engrenage à droite du serveur WireGuard.

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        Activez **Remote Access LAN**, puis cliquez sur **Apply**.

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **Lorsque cette option est activée, ce routeur et les périphériques du LAN sont accessibles à distance via le VPN.**

    ??? "Pour le firmware v4.8 et versions ultérieures"

        Sur le panneau d'administration web du serveur, allez dans **VPN** -> **WireGuard Server**. Cliquez sur **Options** dans le coin supérieur droit.

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        Activez **Allow Remote Access the LAN Subnet**, puis cliquez sur **Apply**.

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **Lorsque cette option est activée, ce routeur et les périphériques du LAN sont accessibles à distance via le VPN.**

3. Créez un compte AstroRelay et suivez ce [tutoriel](https://www.astrorelay.com/tutorial.html){target="_blank"} pour effectuer la configuration initiale.

    Lors de l'ajout d'un nouveau domaine, choisissez le serveur le plus proche de votre routeur.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Lors de l'ajout d'un nouveau lien, entrez l'**adresse IP LAN** de votre routeur dans le champ **Destination Host IP**, et entrez **51820** dans le champ **Destination Port**.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Vous obtiendrez alors un lien, tel que **wg_server_test.arlab1.cc:33331**. Cliquez dessus pour copier le lien.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. Ouvrez le fichier de configuration WireGuard, remplacez la valeur après **Endpoint** par le lien que vous avez obtenu à l'étape précédente, et appliquez les modifications.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. Installez l'[application WireGuard](https://www.wireguard.com/install/){target="_blank"} sur l'appareil que vous souhaitez utiliser comme client VPN WireGuard. Ensuite, téléchargez le fichier de configuration modifié dans l'application et démarrez la connexion. Alternativement, téléchargez-le sur un autre routeur GL.iNet afin de le configurer comme client VPN WireGuard.

    Une fois connecté, vous pourrez accéder à distance à vos services locaux de domicile ou de bureau.

---

Vous avez encore des questions ? Visitez notre [Forum Communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
