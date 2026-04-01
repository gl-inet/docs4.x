# Comment autoriser l’accès au WAN lorsque le client VPN est activé ?

Lorsque le client VPN est activé sur les routeurs GL.iNet, en mode global par défaut, les appareils LAN ne peuvent pas accéder aux appareils ou services du WAN local, car tout le trafic provenant du LAN est acheminé par le tunnel VPN plutôt que par son réseau amont (WAN), afin d’éviter les fuites DNS.

Ce tutoriel présente les étapes permettant de rendre les services WAN locaux (par ex. imprimante, NAS, etc.) accessibles aux appareils du LAN du client VPN.

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Pour le firmware v4.7 et les versions antérieures

Connectez-vous au panneau d’administration web de votre client VPN, puis accédez à **VPN** -> **VPN Dashboard** -> **VPN Client**. Cliquez sur **Global Options** dans l’angle supérieur droit.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Activez **Allow Access WAN** et cliquez sur **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Si cette option est activée, lorsque le VPN est connecté, les appareils clients peuvent toujours accéder aux services WAN du sous-réseau supérieur, par exemple votre imprimante, votre NAS, etc.

## Pour le firmware v4.8 et les versions ultérieures

L’option **Allow Access WAN** a été supprimée du VPN Dashboard dans le firmware v4.8. Vous pouvez toutefois obtenir l’accès au WAN local à l’aide d’une politique VPN.

Suivez les étapes ci-dessous.

1. Connectez-vous au panneau d’administration web de votre client VPN, puis accédez à **VPN** -> **VPN Dashboard**. 

    Cliquez sur le mode dans l’angle supérieur droit.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Passez en **Policy Mode** (mode de stratégie), puis cliquez sur **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    La page sera actualisée et s’affichera comme ci-dessous.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Cliquez sur la case centrale pour définir la destination du tunnel.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Sélectionnez **Exclude Speficied Domain / IP**, saisissez le sous-réseau WAN de votre routeur, puis cliquez sur **Apply**.

    Cela garantit que tout le trafic vers le sous-réseau WAN est acheminé via le WAN local plutôt que via le tunnel VPN.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    Nous prenons ici le sous-réseau 192.168.0.1/24 comme exemple. Saisissez ce sous-réseau et appliquez les paramètres ; le tunnel VPN s’affichera alors comme ci-dessous.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Comment connaître le sous-réseau WAN de mon routeur GL.iNet ?"

        Le sous-réseau WAN du routeur GL.iNet se trouve généralement sur la page INTERNET. Il est déterminé par l’appareil amont auquel l’interface WAN du routeur est connectée (par ex. un modem FAI ou une passerelle amont).

        Par exemple, si votre routeur fonctionne comme routeur secondaire (c’est-à-dire que son port WAN est connecté à un autre réseau local, tel qu’un modem FAI ou le port LAN d’un routeur principal), et que l’adresse IP WAN du routeur est 192.168.1.165, la Gateway est 192.168.1.1 et le Subnet Mask est 255.255.255.0 (un masque courant pour les petits réseaux), alors le sous-réseau WAN correspondant est 192.168.1.0/24. Il s’agit également du sous-réseau LAN de l’appareil amont.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Remarque** : la longueur de préfixe de 192.168.1.0/24 est 24, ce qui correspond au masque de sous-réseau 255.255.255.0. Si le WAN Subnet Mask de votre routeur n’est pas 255.255.255.0, alors la longueur de préfixe de votre sous-réseau WAN n’est pas "/24". Veuillez confirmer le sous-réseau WAN selon la configuration WAN réelle. 

3. Cliquez sur la case de droite pour définir l’action du tunnel (c.-à-d. utiliser ou non le VPN).

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Sélectionnez **Use VPN** et choisissez un fichier de configuration VPN. Cliquez ensuite sur **Apply**.

    S’il n’existe aucune configuration disponible, importez-en d’abord une afin de configurer votre routeur comme client VPN. Revenez ensuite sur cette page, sélectionnez **Use VPN**, choisissez un fichier de configuration VPN, puis cliquez sur **Apply**.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Basculez l’interrupteur situé dans l’angle supérieur droit pour activer ce tunnel VPN. La connexion va démarrer.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Attendez quelques minutes. Une fois la connexion établie avec succès, l’indicateur devient vert.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Vérifiez votre IP publique pour tester la connexion VPN. Par exemple, ouvrez un navigateur et accédez à [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Le site affichera votre adresse IP publique et votre emplacement, comme ci-dessous. 

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Accédez aux appareils ou services du sous-réseau WAN et vérifiez que l’accès fonctionne correctement.

    Vous pouvez utiliser la commande ping pour tester la connectivité. 

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
