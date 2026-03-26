# Comment configurer un serveur OpenVPN via AstroRelay ?

Ce tutoriel présente les étapes pour configurer un serveur OpenVPN via AstroRelay sur un routeur GL.iNet. Cette solution est idéale pour les utilisateurs qui ont besoin d'un accès à distance à leurs services locaux à domicile ou au bureau, mais qui ne disposent pas d'une adresse IP publique fournie par leur FAI.

[AstroRelay](https://www.astrorelay.com){target="_blank"} fournit un tunnel proxy inverse sécurisé, qui permet d'accéder en toute sécurité aux ressources derrière un NAT et des pare-feu.

1. Suivez [ce guide](../interface_guide/openvpn_server.md) pour configurer un serveur OpenVPN sur votre routeur GL.iNet, même si vous ne disposez pas d'une adresse IP publique.

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Exportez ensuite la configuration OpenVPN. Voici un exemple de fichier de configuration.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. (Facultatif) Si vous devez accéder à distance au réseau local du serveur VPN, activez l'option **Allow Remote Access LAN**. Sinon, ignorez cette étape.

    ??? "Pour le firmware v4.7 et versions antérieures"

        1. Dans la barre latérale gauche, cliquez sur **VPN** > **VPN Dashboard**.
        2. Cliquez sur l'icône Options.
        3. Activez **Remote Access LAN**.
        4. Cliquez sur **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "Pour le firmware v4.8 et versions ultérieures"

        1. Dans la barre latérale gauche, cliquez sur **VPN** > **OpenVPN Server**.
        2. Cliquez sur **Options** en haut à droite.
        3. Activez **Allow Remote Access the LAN Subnet**.
        4. Cliquez sur **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. Créez un compte AstroRelay et suivez ce [tutoriel](https://www.astrorelay.com/tutorial.html){target="_blank"} pour terminer la configuration initiale.

    Lors de l'ajout d'un nouveau domaine, choisissez le serveur le plus proche de votre routeur.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Lors de l'ajout d'un nouveau lien, saisissez l'**adresse IP LAN** de votre routeur dans le champ **Destination Host IP**, puis saisissez **1194** dans le champ **Destination Port**.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Vous obtiendrez ensuite un lien, par exemple **testforx3000.arlab1.cc:37202**. Cliquez dessus pour le copier.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. Ouvrez le fichier de configuration OpenVPN et remplacez la valeur située après **Remote** par le lien obtenu à l'étape précédente. Dans l'exemple ci-dessous, "42.200.00.00 1194" est remplacé par le lien "testforx3000.arlab1.cc:37202". Remplacez ensuite le signe deux-points ":" par un espace et appliquez les modifications.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. Installez l'application [OpenVPN Connect](https://openvpn.net/client/){target="_blank"} sur l'appareil que vous souhaitez utiliser comme client OpenVPN. Téléversez ensuite le fichier de configuration modifié dans l'application et démarrez la connexion. Vous pouvez également le téléverser sur un autre routeur GL.iNet afin de le configurer comme client OpenVPN.

    Une fois connecté, vous pourrez accéder à distance à vos services locaux à domicile ou au bureau.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

