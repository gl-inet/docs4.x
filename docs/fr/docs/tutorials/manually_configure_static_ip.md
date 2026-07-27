# Comment configurer manuellement une IP statique sur les appareils clients ?

=== "Windows 11"

    Sous Windows 11, vous pouvez définir une configuration d'adresse IP statique à partir de l'application Paramètres pour les adaptateurs sans fil et filaires.

    **Définir une adresse IP statique sur l'adaptateur Wi-Fi**

    Pour attribuer une configuration d'adresse IP statique à un adaptateur Wi-Fi, procédez comme suit :

    1. Ouvrez les Paramètres sous Windows 11 -> Réseau et Internet -> l'onglet Wi-Fi -> sélectionnez la connexion réseau actuelle.

    2. Dans la section « Paramètres IP », cliquez sur le bouton Modifier.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Suivez les étapes ci-dessous pour le configurer :

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - Sélectionnez l'option Manuel et activez le bouton bascule IPv4.

        - Définissez une adresse IP statique pour Windows 11 – par exemple, 10.1.4.119.

        - Spécifiez un Masque de sous-réseau – par exemple, 255.255.255.0.

        - Spécifiez une adresse Passerelle par défaut.

        - Spécifiez une adresse DNS préférée (obligatoire).

        - (Facultatif) Spécifiez une adresse « DNS secondaire ».

        - Utilisez le menu déroulant « DNS sur HTTPS » et sélectionnez l'option Désactivé pour les adresses préférée et secondaire, mais vous pouvez activer DoH avec ces options :

            - Désactivé : transmet tout le trafic DNS sans chiffrement.

            - Activé (modèle automatique) : envoie tout le trafic DNS avec chiffrement.

            - Activé (modèle manuel) : permet de spécifier un modèle particulier. Cela n'est nécessaire que si le service DNS ne fonctionne pas automatiquement ou possède un modèle qui fonctionne comme prévu.

        - Désactivez le bouton bascule « Basculer vers texte en clair » (si vous activez DoH).

            - Conseil : si vous activez cette fonctionnalité, le système chiffrera le trafic DNS, mais autorisera l'envoi de requêtes sans chiffrement.

    4. Cliquez sur le bouton Enregistrer.

        Une fois les étapes terminées, la configuration réseau statique sera appliquée à l'ordinateur. Vous pouvez tester les nouveaux paramètres en ouvrant le navigateur web et en chargeant un site web.


    ## **Définir une adresse IP statique sur l'adaptateur Ethernet**

    Pour attribuer une adresse IP statique à un adaptateur Ethernet (filaire) sous Windows 11, procédez comme suit :

    1. Ouvrez les Paramètres -> Réseau et Internet -> l'onglet Ethernet.
    
    2. Dans la section « Paramètres IP », cliquez sur le bouton Modifier.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Suivez les étapes ci-dessous pour le configurer :

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}
        
        - Sélectionnez l'option Manuel.

        - Activez le bouton bascule IPv4.

        - Définissez une adresse IP statique pour Windows 11 – par exemple, 10.1.4.119.

        - Spécifiez un Masque de sous-réseau – par exemple, 255.255.255.0.

        - Spécifiez une adresse Passerelle par défaut.

        - Spécifiez une adresse DNS préférée (obligatoire).

        - (Facultatif) Spécifiez une adresse « DNS secondaire ».

        - Utilisez le menu déroulant « DNS sur HTTPS » et sélectionnez l'option Désactivé pour les adresses préférée et secondaire, mais vous pouvez activer DoH avec ces options :

            * Désactivé : transmet tout le trafic DNS sans chiffrement.

            * Activé (modèle automatique) : envoie tout le trafic DNS avec chiffrement.

            * Activé (modèle manuel) : permet de spécifier un modèle particulier. Cela n'est nécessaire que si le service DNS ne fonctionne pas automatiquement ou possède un modèle qui fonctionne comme prévu.
            
        - Désactivez le bouton bascule « Basculer vers texte en clair » (si vous activez DoH).

    4. Cliquez sur le bouton Enregistrer.

        Une fois les étapes terminées, vous pouvez tester vos paramètres en ouvrant un site web dans votre navigateur.


=== "macOS"

    Voici comment définir une adresse IP statique sous macOS :

    Si vous possédez un MacBook, vous souhaiterez peut-être créer un nouvel emplacement réseau. Cela vous permettra d'utiliser l'adresse IP statique pour certains réseaux seulement. 

    Dans le menu Apple, sélectionnez Préférences Système.

    Sélectionnez Réseau. La fenêtre ci-dessous s'affiche.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Dans la barre latérale, sélectionnez une interface réseau active. Dans cet exemple, connecté à un réseau sans fil, sélectionnez Wi-Fi.

    Notez l'adresse IP actuelle attribuée à votre Mac. Vous devrez sélectionner une nouvelle adresse IP dans la plage d'adresses IP privées listée. Plus d'informations à ce sujet dans un instant.

    Cliquez sur Avancé.

    Sélectionnez TCP/IP. La fenêtre ci-dessous s'affiche.
    
    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    Dans le menu Configurer IPv4, sélectionnez Manuellement.

    Saisissez une adresse IP statique dans le champ Adresse IPv4. Quel numéro faut-il saisir ? Une méthode consiste à prendre votre adresse IP actuelle et à modifier la dernière partie du numéro. Dans cet exemple, vous pouvez choisir n'importe quelle adresse entre 192.168.7.0 et 192.168.7.255, à condition que l'adresse ne soit pas déjà attribuée à un autre appareil.

    Cliquez sur OK -> Cliquez sur Appliquer.
   

=== "Android"

    Les étapes varient selon les versions d'Android. Cette documentation est basée sur Android version 11.

    1. Accédez aux Paramètres -> sélectionnez Réseau et Internet, puis Wi-Fi -> appuyez sur le réseau actuellement connecté pour ouvrir le menu des paramètres.
    
    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. Pour définir une adresse IP statique, procédez comme suit :

    - Sélectionnez l'icône en forme de crayon en haut à droite pour accéder aux paramètres réseau.
        
        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Sélectionnez Options avancées.
        
        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Sélectionnez Paramètres IP.
        
    - Changez le paramètre de DHCP à Statique.
        
        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Lors de l'utilisation d'adresses IP statiques sur les réseaux domestiques et autres réseaux privés, elles doivent être choisies dans les plages d'adresses IP privées standard listées : 10.0.0.0 à 10.255.255.255, 172.16.0.0 à 172.31.255.255, 192.168.0.0 à 192.168.255.255

    - Saisissez maintenant l'adresse IP.
        - Cette étape est spécifique à chaque réseau. Exemple : 192.168.1.128
        
    - La Passerelle devrait se remplir automatiquement en fonction de l'adresse IP. Sinon, copiez l'adresse IP et remplacez le dernier chiffre par 1. 
        - Exemple : d'après l'exemple précédent : 192.168.1.1

    3. Appuyez sur Enregistrer et laissez le réseau se reconnecter.

=== "iOS"

    Lors de l'utilisation d'adresses IP statiques sur les réseaux domestiques et autres réseaux privés, elles doivent être choisies dans les plages d'adresses IP privées standard listées :

    10.0.0.0 à 10.255.255.255
    172.16.0.0 à 172.31.255.255
    192.168.0.0 à 192.168.255.255

    Pour définir une adresse IP statique, procédez comme suit :

    - Appuyez sur l'icône Réglages.

    - Accédez à Wi-Fi.

    - Appuyez sur l'icône d'information bleue (i) à côté du nom du réseau Wi-Fi
         - Il peut s'agir d'une erreur bleue si vous utilisez une version antérieure à iOS 7.

    - Accédez à l'onglet Statique, illustré ci-dessous.

        
    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - Appuyez sur le champ Adresse IP.

    - Saisissez l'adresse IP statique que vous souhaitez utiliser sur votre iPhone/iPad.

    - Appuyez sur le champ Routeur.

    - Saisissez l'adresse IP du routeur.
        
    - Appuyez sur Masque de sous-réseau et saisissez vos informations

        - Habituellement, ce sera 255.255.0.0.

    - Appuyez sur le bouton Wi-Fi dans l'angle supérieur gauche de l'écran pour enregistrer les paramètres.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
