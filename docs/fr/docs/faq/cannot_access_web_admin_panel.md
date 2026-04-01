# Impossible d'accéder au panneau d'administration web

Il arrive que vous ne puissiez pas accéder à [http://192.168.8.1](http://192.168.8.1) et donc que vous ne puissiez pas vous connecter au panneau d'administration web. Plusieurs raisons sont possibles.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Causes possibles

* Votre ordinateur ou votre téléphone mobile n'est pas connecté au routeur.
* `192.168.8.1` est l'adresse IP par défaut du routeur. Il est possible que vous l'ayez modifiée.
* Le cache du navigateur ou une extension peut empêcher l'accès au panneau d'administration.
* Un logiciel VPN ou proxy peut prendre en charge votre trafic et empêcher l'accès au panneau d'administration.
* Le routeur est brické.

## Vérifier les étapes générales d'accès au panneau d'administration web

1. Mettez le routeur sous tension sans le connecter à un autre appareil.
2. Connectez votre téléphone ou votre ordinateur portable au Wi-Fi du routeur et saisissez la clé Wi-Fi imprimée sur l'étiquette du routeur.
3. Si l'étape 2 échoue, désactivez le Wi-Fi sur votre ordinateur portable et connectez-le à la place au port LAN du routeur à l'aide d'un câble Ethernet.
4. Ouvrez un navigateur, saisissez `192.168.8.1` dans la barre d'adresse et appuyez sur Entrée. Vous devriez pouvoir accéder au panneau d'administration web GL.iNet.

Vous pouvez également utiliser [l'application](mobile_app.md) pour accéder au routeur.

## Autres étapes pour résoudre ce problème

1. [Vérifier la connexion](#verifier-la-connexion)
2. [Vérifier l'adresse IP du routeur](#verifier-ladresse-ip-du-routeur)
3. [Accéder à l'adresse IP du routeur](#acceder-a-ladresse-ip-du-routeur)

---

### Vérifier la connexion

Si vous êtes connecté par câble Ethernet, vérifiez que la connexion WAN/LAN du routeur est correcte :

- Le port WAN est connecté à une source Internet, comme un modem ou un routeur principal.
- Le port LAN est connecté à l'appareil terminal, par exemple votre ordinateur portable.

Si vous êtes connecté en Wi-Fi, assurez-vous d'avoir sélectionné le bon SSID sur votre appareil et d'avoir saisi le bon mot de passe.

### Vérifier l'adresse IP du routeur

Suivez les étapes ci-dessous pour vérifier l'adresse IP du routeur.

=== "Windows 10 / Windows 11"

    Accédez au Control Panel et assurez-vous que le coin supérieur droit est réglé sur View by Large icons ou Small icons.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    Control Panel -> Network and Share Center -> cliquez sur la connexion. Vous pouvez avoir plusieurs connexions ; choisissez celle qui correspond au routeur que vous souhaitez vérifier.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Une boîte de dialogue affichant l'état de la connexion s'ouvrira. Cliquez sur le bouton Detail.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    Une boîte de dialogue affichant les détails de la connexion réseau s'ouvrira. L'adresse IP du routeur correspond à **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings

    Cliquez avec le bouton droit sur le réseau -> Status -> Details
    
    L'adresse IP du routeur correspond à **IPv4 Default Gateway**.
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. System Preferences -> Network

    2. Dans la colonne de gauche, cliquez sur la connexion réseau. Pour une connexion Ethernet, l'adresse IP du routeur s'affichera.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Pour une connexion Wi-Fi, cliquez sur le bouton "Advanced...", puis sur l'onglet "TCP/IP" en haut de la fenêtre. L'adresse IP du routeur s'affichera.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Settings -> Wi-Fi
    2. Appuyez sur l'icône d'information (un i bleu dans un cercle) du réseau Wi-Fi actuellement connecté. L'adresse IP du routeur s'affichera.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Cela varie selon les appareils Android.

    1. Settings -> Network & internet
    2. Appuyez sur Wi-Fi et trouvez le réseau auquel vous êtes connecté, puis cliquez sur l'icône des paramètres pour gérer sa configuration.
    3. Appuyez sur le menu déroulant Advanced. Si des options Static ou Dynamic IP sont proposées, sélectionnez Static.
    4. Dans tous les cas, vous devriez voir l'adresse IP de votre routeur sous Gateway.

### Accéder à l'adresse IP du routeur

1. Utilisez Chrome/Edge/Safari pour accéder au panneau d'administration de votre routeur afin d'obtenir une meilleure compatibilité.

2. Afin d'éviter les problèmes causés par le cache du navigateur et les extensions, ouvrez une fenêtre de navigation privée, puis essayez d'accéder de nouveau à l'adresse IP du routeur.

3. Désactivez tout logiciel VPN ou proxy, y compris Tailscale et ZeroTier.

4. Si vous utilisez un téléphone mobile, désactivez les données mobiles.

    Certains smartphones se déconnectent du Wi-Fi du routeur et utilisent les données mobiles lorsqu'ils détectent que le routeur n'a pas accès à Internet. Or, cette déconnexion du routeur empêche l'accès au panneau d'administration web.

5. Si les étapes ci-dessus échouent, essayez de [réinitialiser](repair_network_or_reset_firmware.md#reset-to-factory) le routeur à sa configuration d'usine.

6. Si la réinitialisation ne fonctionne pas, essayez la [récupération via U-Boot](debrick.md).

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

