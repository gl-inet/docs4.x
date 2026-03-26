# Comment accéder à l’interface LuCI via GoodCloud

[GoodCloud](https://www.goodcloud.xyz/){target="_blank"} de GL.iNet permet de s’affranchir des limitations géographiques et offre un moyen pratique de gérer le routeur à distance. Grâce à GoodCloud, vous pouvez accéder à l’interface LuCI du routeur à tout moment et où que vous soyez, effectuer divers réglages sur le routeur et gérer facilement le réseau.

## Préparation

- Équipement matériel : un routeur GL.iNet configuré avec un accès Internet et fonctionnant normalement.
- Environnement réseau : le réseau auquel le routeur est connecté est stable et peut accéder normalement à Internet.
- Association de l’appareil : vous devez [associer votre routeur GL.iNet à votre compte GoodCloud](../interface_guide/cloud.md/#setup-your-goodcloud-account). Si vous n’avez pas de compte GoodCloud, veuillez en [créer un](https://www.goodcloud.xyz/){target="_blank"}.

## Étapes pour accéder à l’interface LuCI via GoodCloud

### Pour la version de firmware 4.7 ou supérieure

À partir de la v4.7, les utilisateurs peuvent accéder directement à la page LuCI depuis la plateforme GoodCloud sans passer par le panneau d’administration web du routeur.

1. Connectez-vous à votre compte GoodCloud [ici](https://www.goodcloud.xyz/){target="_blank"}.

2. Sur la gauche -> **Devices** -> **Bound Devices**, cliquez sur le nom de l’appareil auquel vous souhaitez accéder ; vous verrez alors les icônes de Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    La fenêtre contextuelle affiche le port 80. Remplacez-le par **8080**, puis cliquez sur **Apply**.

    ![change port](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Vous serez redirigé vers la page de connexion LuCI. Saisissez votre mot de passe administrateur pour vous connecter.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Vous êtes maintenant connecté à LuCI avec succès.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}    

### Pour la version de firmware 4.6 ou inférieure

1. Connectez-vous à votre compte GoodCloud [ici](https://www.goodcloud.xyz/){target="_blank"}.

2. Sur la gauche -> **Devices** -> **Bound Devices**, cliquez sur le nom de l’appareil auquel vous souhaitez accéder ; vous verrez alors les icônes de Remote Web Access.

    ![remote gui](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    La fenêtre contextuelle affiche le port 80 ; cliquez sur **Apply**.

    ![vist web apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Vous serez alors redirigé vers la page de connexion du GL.iNet Admin Panel. Saisissez votre mot de passe administrateur pour vous connecter.

    ![admin panel login](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Après la connexion, sur la gauche -> SYSTEM -> Advanced Settings, cliquez sur le lien pour accéder à l’interface LuCI.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Vous serez redirigé vers la page de connexion LuCI. Saisissez le même mot de passe administrateur pour vous connecter.

    ![log in luci](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Vous êtes maintenant connecté à LuCI avec succès.

    ![luci interface](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
