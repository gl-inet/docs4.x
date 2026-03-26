# Drop-in Gateway

Dans le panneau d'administration web, accédez à **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway est une fonction d'extension qui permet d'ajouter des capacités à un routeur principal existant sans le remplacer ni le reconfigurer. En connectant le routeur GL.iNet au routeur principal à l'aide d'un câble Ethernet, vous pouvez ajouter des fonctions réseau avancées à l'infrastructure existante, par exemple :

- Filtrer les publicités via AdGuard Home
- Activer un client VPN
- Utiliser un DNS chiffré

Il est recommandé d'utiliser un routeur ou une passerelle de sécurité plus performant, avec suffisamment de mémoire (par exemple GL-MT2500, GL-MT5000), et d'installer si nécessaire des outils supplémentaires de transfert et de contrôle du trafic.

## Topologie réseau

Drop-in Gateway fonctionne comme un système réseau intermédiaire : le trafic des appareils clients est redirigé vers le routeur GL.iNet pour y être traité, puis renvoyé via le routeur principal. Ce fonctionnement permet non seulement de conserver les paramètres réseau existants (par exemple le SSID et le mot de passe) afin d'assurer une connectivité ininterrompue pour tous les appareils connectés, mais aussi de gérer le trafic réseau de tous les appareils clients ou de certains d'entre eux selon les besoins.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Le schéma ci-dessus comporte deux types de lignes : des lignes grises et des lignes vertes marquées de trois flèches, chacune portant un numéro correspondant.

1. Les **lignes grises** illustrent la topologie des connexions physiques : les appareils clients (par exemple un ordinateur de bureau ou portable) se connectent au routeur principal, et le port LAN du routeur principal est relié au port WAN du routeur GL.iNet (avec Drop-in Gateway activé) à l'aide d'un câble Ethernet.

2. Les **lignes vertes** représentent le chemin séquentiel de transmission des données lorsque Drop-in Gateway est actif, les flèches numérotées indiquant l'ordre de circulation du trafic :

    1. Le trafic des appareils clients est d'abord envoyé vers le routeur principal ;
    
    2. Le routeur principal transmet ensuite ce trafic au routeur GL.iNet pour traitement (par exemple filtrage des publicités ou chiffrement VPN) ;
    
    3. Une fois traité, le trafic est renvoyé au routeur principal, qui transmet soit les données finales aux appareils clients d'origine, soit le trafic vers Internet.

## Configuration

Deux modes de déploiement sont disponibles selon le scénario d'utilisation : tous les appareils clients utilisent Drop-in Gateway, ou seuls certains appareils clients l'utilisent.

Dans l'exemple suivant, l'adresse de passerelle du routeur principal est `192.168.1.1`.

### Tous les appareils utilisent Drop-in Gateway {all-devices-managed-by-the-drop-in-gateway}

1. Reliez le port LAN du routeur principal au port WAN du routeur GL.iNet à l'aide d'un câble Ethernet.

2. Connectez-vous au panneau d'administration web de votre routeur GL.iNet, activez Drop-in Gateway, puis le système générera automatiquement les paramètres de configuration correspondants.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** correspond à l'adresse IP WAN de votre routeur GL.iNet, attribuée dynamiquement par le routeur principal. Cette adresse IP WAN peut être consultée dans la section Ethernet de la page [INTERNET](internet_ethernet.md). 
    
    - Les champs **Gateway** et **DNS Server 1** sont automatiquement renseignés avec l'adresse IP du routeur principal par défaut. Si ces paramètres sont incorrects, vous pouvez les ajuster manuellement selon vos besoins.

    Notez cette adresse IP, car elle sera utilisée dans les étapes suivantes.

    Sélectionnez la première méthode de configuration, puis cliquez sur **Apply**.

3. Connectez-vous au panneau d'administration web de votre routeur principal.

    ??? "GL.iNet"

        Si votre routeur principal est un GL.iNet et qu'il exécute le firmware v4.2 ou supérieur, suivez les étapes ci-dessous.

        Connectez-vous au panneau d'administration web -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Renseignez **DHCP Gateway** avec l'**IP Address** obtenue à l'étape 2, par exemple `192.168.1.23`, puis cliquez sur **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Si votre routeur principal est un TP-Link, suivez les étapes ci-dessous (exemple basé sur un TP-LINK Archer C3150).

        Connectez-vous à la page d'administration TP-Link, accédez à **Advanced** -> **Network** -> **DHCP Server**, puis désactivez **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Cliquez ensuite sur **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Si votre routeur principal est un Linksys, suivez les étapes ci-dessous (exemple basé sur un Linksys WHW01).

        Connectez-vous à la page d'administration Linksys, puis accédez à **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Cliquez sur l'onglet **Local Network**, désactivez **DHCP Server**, puis cliquez sur **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Un avertissement s'affiche. Cliquez sur **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Autres"

        Connectez-vous au panneau d'administration du routeur principal pour désactiver son serveur DHCP. Vous pouvez consulter le manuel utilisateur du fabricant concerné ou contacter son support.

4. Revenez sur le routeur GL.iNet et configurez les fonctions souhaitées, comme [AdGuard Home](adguardhome.md), le [DNS chiffré](dns.md), [WireGuard Client](wireguard_client.md) et [OpenVPN Client](openvpn_client.md).

### Seuls certains appareils utilisent Drop-in Gateway {some-devices-managed-by-the-drop-in-gateway}

1. Reliez le port LAN du routeur principal au port WAN du routeur GL.iNet à l'aide d'un câble Ethernet.

2. Connectez-vous au panneau d'administration web de votre routeur GL.iNet, activez Drop-in Gateway, puis le système générera automatiquement les paramètres de configuration correspondants.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** correspond à l'adresse IP WAN de votre routeur GL.iNet, attribuée dynamiquement par le routeur principal. Cette adresse IP WAN peut être consultée dans la section Ethernet de la page [INTERNET](internet_ethernet.md). 
    
    - Les champs **Gateway** et **DNS Server 1** sont automatiquement renseignés avec l'adresse IP du routeur principal par défaut. Si ces paramètres sont incorrects, vous pouvez les ajuster manuellement selon vos besoins.

    Notez cette adresse IP, car elle sera utilisée dans les étapes suivantes.

    Sélectionnez la deuxième méthode de configuration, puis cliquez sur **Apply**.

3. Sur l'appareil qui doit utiliser Drop-in Gateway, définissez la passerelle et le DNS sur l'adresse IP affichée sur la page Drop-in Gateway.

    ??? "Windows"

        Voici un exemple sous Windows 11 ; Windows 10 est similaire. Assurez-vous que votre PC est connecté au routeur principal. Dans cet exemple, l'ordinateur est connecté au routeur principal via un câble réseau, mais la configuration est similaire en Wi-Fi.

        1. Ouvrez **Settings**.

        2. Cliquez sur **Network & Internet**.

        3. Cliquez sur l'onglet **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Repérez l'adresse IP de ce PC. Dans la section "IP assignment", cliquez sur le bouton **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Sélectionnez l'option **Manual**. Activez ensuite le bouton **IPv4**.

        6. Définissez **IP address** sur l'adresse IP relevée à l'étape 4, **Subnet mask** sur `255.255.255.0`, et **Gateway** ainsi que **Preferred DNS** sur l'adresse IP affichée sur la page Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Cliquez sur le bouton **Save**.

    ??? "Android"

        Voici un exemple avec un Samsung S21. Assurez-vous que votre smartphone est connecté au routeur principal.

        1. Ouvrez **Settings**, puis appuyez sur **Connections**.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Appuyez sur **Wi-Fi**.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Appuyez sur l'icône en forme d'engrenage du SSID actuel.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Appuyez sur **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Appuyez sur **IP settings**, puis choisissez **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Définissez **Gateway** et **DNS 1** sur l'adresse IP affichée sur la page Drop-in Gateway, puis cliquez sur **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Voici un exemple avec iOS 16.3 sur iPhone 8. Assurez-vous que votre smartphone est connecté au routeur principal.

        1. Ouvrez **Settings**, puis appuyez sur **Wi-Fi**.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Appuyez sur le SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Faites défiler la page jusqu'à voir **Configure IP** sur **Automatic**. Notez **IP Address** et **Subnet Mask** pour l'étape suivante.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Remplacez **Configure IP** par **Manual**, définissez **IP Address** et **Subnet Mask** avec les mêmes valeurs que celles relevées à l'étape précédente, puis définissez **Router** sur l'adresse IP affichée sur la page Drop-in Gateway. Cliquez ensuite sur **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Appuyez sur **Configure DNS** et remplacez-le par **Manual**. Appuyez sur **Add Server**, définissez l'adresse IP du serveur DNS sur celle affichée sur la page Drop-in Gateway, puis cliquez sur **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Revenez au panneau d'administration web du routeur GL.iNet et configurez les fonctions nécessaires, par exemple [AdGuard Home](adguardhome.md), le [DNS chiffré](dns.md), [WireGuard Client](wireguard_client.md) et [OpenVPN Client](openvpn_client.md).

## Précautions

1. L'activation de Drop-in Gateway augmente la latence réseau.

2. Lorsque Drop-in Gateway est activé, la transmission des données entre les appareils LAN sélectionnés transite également par cette passerelle intermédiaire. La bande passante entre le routeur principal et Drop-in Gateway influe donc sur la bande passante globale du LAN.

---

Article connexe :

- [Comment configurer Drop-in Gateway sur un routeur GL.iNet](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
