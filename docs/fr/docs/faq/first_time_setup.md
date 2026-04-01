# Configuration initiale

La configuration initiale d'un routeur GL.iNet est très similaire d'un modèle à l'autre. La plupart des modèles disposent d'un module Wi-Fi, mais certains n'en ont pas.

Les instructions ci-dessous sont donc divisées en deux cas, selon la présence ou non d'un module Wi-Fi.

* [Pour les modèles avec Wi-Fi](#pour-les-modeles-avec-wi-fi)
* [Pour les modèles sans Wi-Fi](#pour-les-modeles-sans-wi-fi)

## Pour les modèles avec Wi-Fi

Prenons ici l'exemple du GL-AXT1800 (Slate AX).

Veuillez préparer les éléments suivants, inclus dans l'emballage.

- GL-AXT1800
- Un adaptateur secteur
- Un câble Ethernet

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise un autre routeur GL.iNet pour illustrer la configuration, car les étapes sont identiques pour la plupart des modèles.)</small>

1. Mise sous tension

    Si vous souhaitez utiliser une carte TF, insérez-la avant de mettre le routeur sous tension. Le remplacement à chaud des cartes TF n'est pas pris en charge.

    Branchez une extrémité de l'adaptateur secteur au routeur et l'autre à une prise électrique. Il s'allumera automatiquement.

2. Connexion au routeur

    Vous pouvez vous connecter au routeur à l'aide d'un câble Ethernet ou en Wi-Fi.

    * Connexion par câble

        Connectez votre ordinateur au port LAN du routeur à l'aide d'un câble Ethernet.

    * Connexion en Wi-Fi

        Le SSID Wi-Fi est imprimé sur l'étiquette située sous le routeur, au format suivant :

        **GL-AXT1800-XXX** ou **GL-AXT1800-XXX-5G**

        La clé Wi-Fi par défaut se trouve sous le SSID.

        Recherchez le SSID du routeur sur votre ordinateur, votre téléphone ou votre tablette, puis saisissez la clé Wi-Fi. Sur certains modèles, si le mot de passe Wi-Fi n'est pas indiqué sur l'étiquette, essayez **"goodlife"**.

        **Conseil :** Le code QR figurant sur l'étiquette inférieure contient les informations Wi-Fi par défaut. Vous pouvez vous connecter rapidement en le scannant avec le lecteur de QR code de votre téléphone.

        **Remarque :** Après la connexion au Wi-Fi, l'accès à Internet peut ne pas être immédiatement disponible. Suivez l'étape suivante pour configurer d'abord votre réseau avant d'accéder à Internet.

3. Connexion au panneau d'administration web

    Ouvrez un navigateur web (nous recommandons Chrome, Edge ou Safari) et accédez à [http://192.168.8.1](http://192.168.8.1). Vous serez redirigé vers la configuration initiale du panneau d'administration web.
    
    Si vous ne pouvez pas accéder au panneau d'administration web, veuillez consulter [cette page](cannot_access_web_admin_panel.md).

    Choisissez une langue, puis cliquez sur **Next** pour continuer.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Définissez le mot de passe administrateur. Nous vous recommandons d'utiliser un mot de passe robuste. Cliquez sur **Apply** pour continuer.

    **Remarque :** Le Wi-Fi peut se désactiver pendant l'initialisation ; assurez-vous de vous reconnecter au routeur.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Une fois la configuration initiale terminée, vous accéderez au panneau d'administration web du routeur.

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Connexion à Internet

    * [Se connecter à Internet avec un câble Ethernet](../interface_guide/internet_ethernet.md)
    * [Se connecter à Internet via un réseau Wi-Fi existant](../interface_guide/internet_repeater.md)
    * [Se connecter à Internet via le partage de connexion USB](../interface_guide/internet_tethering.md)
    * [Se connecter à Internet via un modem USB](../interface_guide/internet_cellular.md)

## Pour les modèles sans Wi-Fi

Prenons ici l'exemple du GL-MT2500A (Brume 2).

1. Mise sous tension

    Branchez une extrémité de l'adaptateur secteur au routeur et l'autre à une prise électrique. Le routeur se mettra automatiquement sous tension.

2. Connexion au routeur

    Vous pouvez vous connecter au routeur à l'aide d'un câble Ethernet ou du Wi-Fi d'un autre routeur.

    * Connexion directe via un câble Ethernet

        Connectez votre ordinateur au port LAN du routeur à l'aide d'un câble Ethernet. C'est la méthode de configuration recommandée, car elle est simple et directe.

    * Connexion via le Wi-Fi d'un autre routeur

        Comme le GL-MT2500A ne dispose pas de module Wi-Fi intégré, vous pouvez utiliser un autre routeur doté d'une fonction Wi-Fi pour initialiser le GL-MT2500A.

        * Méthode 1 : Réglez le second routeur en mode AP (Access Point), puis connectez le port LAN du GL-MT2500A au port WAN du second routeur.

        * Méthode 2 : Laissez le second routeur dans son mode routeur par défaut, mais avec une adresse IP de routeur différente et non en conflit avec 192.168.8.1/24, par exemple 192.168.10.1. Connectez ensuite le port LAN du GL-MT2500A au port WAN du second routeur.

        Utilisez votre ordinateur ou votre smartphone pour vous connecter au Wi-Fi du second routeur.

        !!! Note
        
            Le second routeur mentionné ici est un routeur classique, par exemple un GL.iNet GL-AXT1800, un TP-LINK ou un Netgear. Les modems, terminaux de réseau optique ou appareils fournis par les FAI peuvent ne pas fonctionner dans ce scénario.

3. Accès au panneau d'administration web

    Ouvrez un navigateur web (nous recommandons Chrome, Edge ou Safari) et accédez à [http://192.168.8.1](http://192.168.8.1). Vous serez redirigé vers la configuration initiale du panneau d'administration web. Si vous ne pouvez pas accéder au panneau d'administration web, veuillez consulter [cette page](cannot_access_web_admin_panel.md).

    Choisissez une langue, puis cliquez sur **Next** pour continuer.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Définissez le mot de passe administrateur. Nous vous recommandons d'utiliser un mot de passe robuste. Cliquez sur **Submit** pour continuer.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Une fois la configuration initiale terminée, vous accéderez au panneau d'administration web du routeur.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Connexion à Internet

    * [Se connecter à Internet avec un câble Ethernet](../interface_guide/internet_ethernet.md)
    * [Se connecter à Internet via le partage de connexion USB](../interface_guide/internet_tethering.md)
    * [Se connecter à Internet via un modem USB](../interface_guide/internet_cellular.md)

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

