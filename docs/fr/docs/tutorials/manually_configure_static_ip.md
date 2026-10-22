# Comment configurer manuellement une IP statique sur les appareils clients ? {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    Sous Windows 11, vous pouvez définir une adresse IP statique pour les adaptateurs sans fil et filaires.

    **Définir une adresse IP statique sur l’adaptateur Wi-Fi**

    1. Sur un PC Windows 11, accédez à **Settings** -> **Network & internet** -> **Wi-Fi** et sélectionnez la connexion Wi-Fi actuelle.

    2. Recherchez **IP assignment** et cliquez sur le bouton **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Dans la fenêtre contextuelle, sélectionnez **Manual** et activez **IPv4**.

        ![Configuration IP manuelle](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Suivez les étapes ci-dessous pour modifier les paramètres IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address : définissez une adresse IP statique, par exemple `10.1.4.119`.

        - Subnet mask : spécifiez un masque de sous-réseau, par exemple `255.255.255.0`.

        - Gateway : saisissez l’adresse de la passerelle, généralement l’adresse IP LAN de votre routeur sur le même sous-réseau. Par exemple, si votre adresse IP est `10.1.4.119`, la passerelle est généralement `10.1.4.1`.

        - Preferred DNS : spécifiez une adresse DNS préférée (obligatoire). Vous pouvez utiliser un serveur DNS public, comme le serveur DNS de Google `8.8.8.8`.

        - Alternate DNS : spécifiez une adresse DNS secondaire (facultatif).

        - DNS over HTTPS : sélectionnez "Off". Trois options sont disponibles :

            - Off : transmet tout le trafic DNS sans chiffrement.

            - On (automatic template) : envoie tout le trafic DNS avec chiffrement.

            - On (manual template) : permet de spécifier un modèle particulier. Cela n’est nécessaire que si le service DNS ne fonctionne pas automatiquement ou possède un modèle qui fonctionne comme prévu.

        - Désactivez le bouton bascule "Fallback to plaintext" si vous activez DNS over HTTPS.

            **Conseil** : si vous activez cette fonctionnalité, le système chiffrera le trafic DNS, mais autorisera l’envoi de requêtes sans chiffrement.

    5. Cliquez sur **Save** pour appliquer les paramètres.

        Une fois les étapes terminées, la configuration réseau statique sera appliquée à l’ordinateur. Vous pouvez tester les nouveaux paramètres en ouvrant le navigateur web et en chargeant un site web.

    ---

    **Définir une adresse IP statique sur l’adaptateur Ethernet**

    1. Sur un PC Windows 11, accédez à **Settings** -> **Network & internet** -> **Ethernet**.

    2. Recherchez **IP assignment** et cliquez sur le bouton **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Dans la fenêtre contextuelle, sélectionnez **Manual** et activez **IPv4**.

        ![Configuration IP manuelle](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Suivez les étapes ci-dessous pour modifier les paramètres IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address : définissez une adresse IP statique, par exemple `10.1.4.119`.

        - Subnet mask : spécifiez un masque de sous-réseau, par exemple `255.255.255.0`.

        - Gateway : saisissez l’adresse de la passerelle, généralement l’adresse IP LAN de votre routeur sur le même sous-réseau. Par exemple, si votre adresse IP est `10.1.4.119`, la passerelle est généralement `10.1.4.1`.

        - Preferred DNS : spécifiez une adresse DNS préférée (obligatoire). Vous pouvez utiliser un serveur DNS public, comme le serveur DNS de Google `8.8.8.8`.

        - Alternate DNS : spécifiez une adresse DNS secondaire (facultatif).

        - DNS over HTTPS : sélectionnez "Off". Trois options sont disponibles :

            - Off : transmet tout le trafic DNS sans chiffrement.

            - On (automatic template) : envoie tout le trafic DNS avec chiffrement.

            - On (manual template) : permet de spécifier un modèle particulier. Cela n’est nécessaire que si le service DNS ne fonctionne pas automatiquement ou possède un modèle qui fonctionne comme prévu.

        - Désactivez le bouton bascule "Fallback to plaintext" si vous activez DNS over HTTPS.

            **Conseil** : si vous activez cette fonctionnalité, le système chiffrera le trafic DNS, mais autorisera l’envoi de requêtes sans chiffrement.

    5. Cliquez sur **Save** pour appliquer les paramètres.

        Une fois les étapes terminées, la configuration réseau statique sera appliquée à l’ordinateur. Vous pouvez tester les nouveaux paramètres en ouvrant le navigateur web et en chargeant un site web.

=== "macOS"

    Voici comment définir une adresse IP statique sous macOS.

    Dans le menu Apple, sélectionnez **System Preferences**.

    Sélectionnez **Network** pour afficher la page suivante. Dans la barre latérale, sélectionnez une interface réseau active, telle que **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Notez l’adresse IP actuelle attribuée à votre Mac. Vous devrez sélectionner une nouvelle adresse IP dans la plage d’adresses IP privées indiquée.

    Cliquez sur **Advanced** dans le coin inférieur droit.

    Sélectionnez ensuite **TCP/IP** pour afficher la page suivante.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4 : sélectionnez "Manually".

    - IPv4 Address : saisissez une adresse IP statique. Conservez les trois premiers octets de votre adresse IP actuelle et remplacez le dernier par une valeur inutilisée. Par exemple, sur le réseau `192.168.7.0/24`, choisissez une adresse de `192.168.7.2` à `192.168.7.254` qui n’est pas déjà utilisée (évitez `.1`, qui correspond au routeur). N’utilisez ni `192.168.7.0` ni `192.168.7.255`.

    - Subnet Mask : saisissez `255.255.255.0` (ou le masque de sous-réseau fourni par votre administrateur réseau).

    - Router : saisissez l’adresse IP LAN de votre routeur, par exemple `192.168.7.1`.

    Cliquez sur **OK**, puis sur **Apply**.

=== "iOS"

    Les étapes peuvent varier selon la version d’iOS. Les étapes suivantes sont basées sur iOS 26.2.2.

    1. Accédez à **Settings** -> **WLAN**. Appuyez sur l’icône d’information bleue (i) à côté du réseau Wi-Fi actuellement connecté.

        ![Adresse IP statique sous iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Faites défiler l’écran jusqu’à **IPv4 Address** et définissez **Configure IP** sur **Manual**.

        ![Adresse IP statique sous iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Spécifiez les valeurs **IP Address**, **Subnet Mask** et **Router IP** à utiliser sur votre iPhone/iPad, puis appuyez sur **Save** dans le coin supérieur droit.

        ![Adresse IP statique sous iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Les étapes peuvent varier selon la version d’Android. Les étapes suivantes sont basées sur Android 11.

    1. Accédez à **Settings** -> **Network & Internet** -> **Wi-Fi**. Appuyez sur le réseau actuellement connecté pour ouvrir le menu des paramètres.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Appuyez sur l’icône en forme de crayon dans le coin supérieur droit pour accéder aux paramètres réseau.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Appuyez sur **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Appuyez sur **IP Settings** et sélectionnez **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Saisissez l’**IP address**. Le champ **Gateway** devrait se renseigner automatiquement en fonction de l’adresse IP. Sinon, saisissez la passerelle de votre réseau. Il s’agit généralement de l’adresse IP LAN de votre routeur sur le même sous-réseau.

        **Conseil** : lorsque vous utilisez des adresses IP statiques sur des réseaux domestiques ou d’autres réseaux privés, choisissez une adresse d’hôte inutilisée dans votre sous-réseau actuel. Les plages d’adresses IP privées standard sont :

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Appuyez sur **Save** et attendez que le réseau se reconnecte.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
