# Configuration initiale

La configuration initiale d'un routeur GL.iNet est très similaire d'un modèle à l'autre. La plupart des modèles disposent d'un module Wi-Fi, mais certains n'en ont pas.

Les instructions ci-dessous sont donc divisées en deux cas, selon la présence ou non d'un module Wi-Fi.

* [Pour les modèles avec Wi-Fi](#pour-les-modeles-avec-wi-fi)
* [Pour les modèles sans Wi-Fi](#pour-les-modeles-sans-wi-fi)

## Pour les modèles avec Wi-Fi

Les étapes suivantes utilisent le GL-MT3000 (Beryl AX) comme exemple.

Veuillez préparer les éléments suivants, inclus dans l'emballage.

- Un routeur GL-MT3000 (Beryl AX)
- Un adaptateur secteur
- Un câble Ethernet

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. **Mise sous tension**

    Branchez une extrémité de l'adaptateur secteur au routeur et l'autre à une prise électrique. Il s'allumera automatiquement.
    
    Certains modèles (comme le Slate AX) sont équipés d'un emplacement pour carte TF. Si vous devez utiliser une carte TF, insérez-la avant de mettre le routeur sous tension. Le remplacement à chaud des cartes TF n'est pas pris en charge.

2. **Connexion au routeur**

    Connectez un appareil (par exemple un smartphone, un ordinateur portable ou un ordinateur) au routeur à l'aide d'un câble Ethernet ou en Wi-Fi.

    * Connexion via Ethernet : Connectez un appareil au port LAN du routeur à l'aide d'un câble Ethernet.

    * Connexion via Wi-Fi : Repérez le SSID Wi-Fi et la Wi-Fi Key sur l'étiquette située sous le routeur. Recherchez le SSID du routeur sur votre appareil, puis saisissez la Wi-Fi Key.

        !!! tip
        
            1. Le code QR figurant sur l'étiquette inférieure contient les informations Wi-Fi par défaut. Vous pouvez vous connecter rapidement en le scannant avec un lecteur de QR code.
            2. Sur certains anciens modèles, si la Wi-Fi Key n'est pas indiquée sur l'étiquette, essayez "goodlife".
        
    Après la connexion au Wi-Fi, l'accès à Internet peut ne pas être immédiatement disponible. Suivez l'étape suivante pour configurer d'abord votre réseau avant d'accéder à Internet.

3. **Connexion au panneau d'administration web**

    Ouvrez un navigateur web (Chrome, Edge et Safari sont recommandés pour une meilleure compatibilité) et accédez à [http://192.168.8.1](http://192.168.8.1). Vous serez redirigé vers la page de connexion GL.iNet. Si vous ne pouvez pas accéder au panneau d'administration web, cliquez [ici](cannot_access_web_admin_panel.md) pour le dépannage.

    Définissez votre mot de passe administrateur, puis cliquez sur **Next**.

    ![mt3000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_password.png){class="glboxshadow"}

    Configurez votre Wi-Fi. Si vous modifiez les informations Wi-Fi, assurez-vous de vous reconnecter au réseau mis à jour, puis cliquez sur **Next**

    ![mt3000 set up wifi](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_set_up_wifi.png){class="glboxshadow"}

    Attendez que le routeur termine son initialisation.

    ![mt3000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_initializing.png){class="glboxshadow"}

    Vous accéderez ensuite au panneau d'administration web de votre routeur.

    ![mt3000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_panel.png){class="glboxshadow"}

4. **Connexion à Internet**

    * [Se connecter à Internet avec un câble Ethernet](../interface_guide/internet_ethernet.md)
    * [Se connecter à Internet via un réseau Wi-Fi existant](../interface_guide/internet_repeater.md)
    * [Se connecter à Internet via le partage de connexion USB](../interface_guide/internet_tethering.md)
    * [Se connecter à Internet via un modem USB](../interface_guide/internet_cellular.md)

## Pour les modèles sans Wi-Fi

Les étapes suivantes utilisent le GL-MT5000 (Brume 3) comme exemple.

1. **Mise sous tension**

    Branchez une extrémité de l'adaptateur secteur au routeur et l'autre à une prise électrique. Le routeur se mettra automatiquement sous tension.

2. **Connexion au routeur**

    Connectez un appareil (par exemple un ordinateur portable ou un ordinateur) au port LAN du routeur à l'aide d'un câble Ethernet.

3. **Connexion au panneau d'administration web**

    Ouvrez un navigateur web (Chrome, Edge et Safari sont recommandés pour une meilleure compatibilité) et accédez à [http://192.168.8.1](http://192.168.8.1). Vous serez redirigé vers la page de connexion GL.iNet. Si vous ne pouvez pas accéder au panneau d'administration web, cliquez [ici](cannot_access_web_admin_panel.md) pour le dépannage.

    Définissez votre mot de passe administrateur, puis cliquez sur **Next**.

    ![mt5000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_password.png){class="glboxshadow"}

    Attendez que le routeur termine son initialisation.

    ![mt5000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_initializing.png){class="glboxshadow"}

    Vous accéderez ensuite au panneau d'administration web de votre routeur.

    ![mt5000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_panel.png){class="glboxshadow"}

4. **Connexion à Internet**

    * [Se connecter à Internet avec un câble Ethernet](../interface_guide/internet_ethernet.md)
    * [Se connecter à Internet via le partage de connexion USB](../interface_guide/internet_tethering.md)
    * [Se connecter à Internet via un modem USB](../interface_guide/internet_cellular.md)

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
