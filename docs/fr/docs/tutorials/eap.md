# Connecter les routeurs GL.iNet à un réseau EAP

Certains routeurs GL.iNet prennent en charge la connexion aux réseaux Wi-Fi EAP (Extensible Authentication Protocol).

EAP est un cadre d'authentification couramment utilisé avec l'**authentification 802.1X** pour les réseaux **WPA2‑Enterprise / WPA3‑Enterprise**. Un exemple typique est **eduroam**, un service mondial d'itinérance Wi-Fi pour l'enseignement et la recherche qui repose sur 802.1X et EAP.

Ce guide présente deux méthodes pour connecter les routeurs GL.iNet à un réseau Wi-Fi EAP : via le panneau d'administration et via LuCI.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-SFT1200 (Opal)

    **Remarque :** 
    
    1. Les GL-MT6000 (Flint 2) et GL-MT3000 (Beryl AX) ne prennent pas en charge la connexion aux réseaux EAP avec le firmware par défaut. Cependant, GL.iNet fournit un firmware OpenWrt 24 natif pour ces modèles, qui peut être installé afin de prendre en charge les réseaux EAP. Recherchez votre modèle dans le [Download Center](https://dl.gl-inet.com/){target="_blank"} puis ouvrez l'onglet OPENWRT 24 pour plus de détails.

    2. Le GL-SFT1200 (Opal) prend en charge la connexion aux réseaux EAP à partir du firmware v4.8.

??? "Modèles non pris en charge"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Se connecter via le panneau d'administration Web

1. Connectez-vous au panneau d'administration Web, allez dans **INTERNET** -> **Repeater**, puis cliquez sur **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Le routeur recherchera les réseaux disponibles. Trouvez et sélectionnez le SSID EAP auquel vous connecter.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Vous pouvez également cliquer sur **Join Other Network** en haut à droite pour rejoindre manuellement le réseau EAP.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Saisissez le **SSID**.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Sélectionnez **Security** sur WPA/WPA2/WPA3 Enterprise.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Saisissez le **Username** et le **Password**, puis cliquez sur **Apply** pour vous connecter.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Se connecter via LuCI

Le panneau d'administration Web GL.iNet ne prend en charge qu'un nombre limité de types EAP.

Si le réseau EAP cible ne peut pas être rejoint via le panneau d'administration Web, essayez de vous connecter via l'interface LuCI.

1. Connectez-vous au panneau d'administration Web, allez dans **SYSTEM** -> **Advanced Settings**. Installez LuCI puis cliquez sur **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Connectez-vous à l'interface LuCI avec le même mot de passe administrateur, puis allez dans Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Cliquez sur **Scan** dans la section 2.4G ou 5G.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Rejoignez le réseau souhaité.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Dépannage

Si le réseau EAP cible exige des paramètres supplémentaires, tels que le type EAP (par exemple PEAP, TTLS), la correspondance du suffixe de domaine, l'identité, l'identité anonyme, etc., la connexion EAP via le panneau d'administration Web peut échouer.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

Suivez les étapes ci-dessous pour connecter votre routeur GL.iNet à des réseaux EAP qui nécessitent des paramètres avancés via l'interface LuCI.

1. Obtenez la configuration.

    Préparez à l'avance les paramètres de configuration du réseau EAP cible. Par exemple : 

    - EAP Type (par exemple PEAP, TTLS, TLS)
    - Suffixe de domaine d'authentification (par exemple @company.com)
    - Identity (généralement le nom d'utilisateur complet)
    - Anonymous Identity (facultatif)
    - Type d'authentification interne (par exemple MSCHAPv2, PAP)
    - Certificat CA (si nécessaire, préparez un fichier au format .crt)

    Voici un exemple de configuration Xfinity Mobile Wi-Fi à titre de référence.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Connectez-vous à LuCI.

    Connectez-vous au panneau d'administration Web du routeur. Après la connexion, si vous avez déjà essayé de vous connecter au réseau EAP cible via la WebGUI et que cela a échoué, veuillez annuler la connexion.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

    Allez ensuite dans **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Connectez-vous à LuCI avec le même mot de passe administrateur.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Configurez Repeater dans LuCI.

    Dans l'interface LuCI, allez dans Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

    Cliquez sur le bouton **Scan** dans la section 5G ou 2.4G pour rechercher les réseaux Wi-Fi disponibles.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

    Recherchez le réseau EAP cible dans les résultats du scan puis cliquez sur **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

    Sur la page "Joining Network", saisissez la **WPA passphrase** puis cliquez sur **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

    Vous serez redirigé vers la configuration du client sans fil. 

4. Repérez **Interface Configuration** -> **Wireless Security**. 

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

    Sélectionnez/saisissez les paramètres de configuration corrects en fonction de votre réseau EAP cible, comme indiqué ci-dessous. **Ne cliquez pas encore sur Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

5. Basculez vers l'onglet **Advanced Settings**, indiquez un nom d'interface, par exemple **wlan0**. Cliquez ensuite sur **Save** en bas à droite.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

6. Vous reviendrez à la page Wireless, qui affichera les modifications en attente. Cliquez sur le bouton **Save & Apply** en bas à droite.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

    Votre routeur sera alors connecté avec succès au réseau EAP cible.

7. Vérifiez la connexion.

    ??? "Vérifier la connexion dans la WebGUI"

        Une fois le routeur connecté avec succès au réseau EAP cible, une icône de répéteur s'allumera dans la WebGUI, comme illustré ci-dessous.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

        **Remarque** : comme la configuration dans LuCI n'est pas synchronisée avec celle de la WebGUI, les détails de l'interface Repeater (par exemple l'adresse IP connectée, la passerelle, etc.) n'apparaîtront pas dans la WebGUI.
        
        Comme le montre l'image, la section Repeater en bas est vide. Cependant, le routeur est déjà connecté au réseau EAP cible en tant que répéteur, car l'icône de répéteur en haut est allumée.

    ??? "Vérifier la connexion via SSH"

        1. [Connectez-vous en SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} à votre routeur.

        2. Saisissez **ifconfig** puis appuyez sur Entrée.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

            Vous pourrez vérifier l'état de l'interface **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
