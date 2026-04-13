# Tailscale

Tailscale est un service VPN qui permet d'accéder à vos appareils et applications partout dans le monde, de manière sécurisée et simple. Pour plus d'informations sur Tailscale, veuillez consulter le [site officiel de Tailscale](https://tailscale.com/).

La fonctionnalité Tailscale des routeurs GL.iNet, disponible depuis le firmware V4.2, permet au routeur de rejoindre un réseau virtuel Tailscale. Une fois connecté, vous pouvez accéder au routeur à distance, y compris à ses ressources WAN et LAN.

**Remarque** :

1. Comme Tailscale est basé sur WireGuard, il n'est pas recommandé d'utiliser Tailscale en même temps que l'une des fonctionnalités ou services suivants, car cela peut provoquer des conflits de routage : OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp.

2. Cette fonctionnalité est actuellement en version bêta et peut comporter certains bugs.

3. Les routeurs GL.iNet ne peuvent **pas encore être utilisés comme nœuds de sortie**.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Modèles non pris en charge"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Configurer un réseau Tailscale

L'exemple ci-dessous utilise le GL-MT2500.

1. Associez vos appareils.

    Veuillez d'abord créer un compte Tailscale, puis associer un ou deux appareils (par exemple un smartphone ou un ordinateur portable) à votre compte Tailscale à des fins de test.

    Après l'association, vous pourrez voir vos appareils et leur état dans la console d'administration Tailscale.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Activez Tailscale sur le routeur GL.iNet.

    Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Activez Tailscale, puis cliquez sur **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Après un court instant, l'interface affichera un **Device Bind Link**. Cliquez dessus.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    Un lien Tailscale s'affichera dans la fenêtre contextuelle. Cliquez dessus pour être redirigé vers le site Tailscale et vous connecter.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Une fois connecté, il vous sera demandé de confirmer l'appareil à connecter. Cliquez sur **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Lorsque la connexion est établie avec succès, vous serez automatiquement redirigé vers la console d'administration Tailscale. Vous pourrez constater que l'adresse IP du GL-MT2500 est `100.88.54.21`. Vous pouvez désormais utiliser cette adresse IP pour accéder au routeur.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

4. Testez la connectivité.

    Sur les appareils connectés au même réseau Tailscale, vous pouvez tester la connectivité des trois manières suivantes.

    * Utiliser la commande ping

        ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

    * Se connecter au routeur en SSH

        ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

    * Accéder au panneau d'administration web

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Autoriser l'accès à distance au WAN

Si cette option est activée, les ressources du côté WAN de l'appareil peuvent être accessibles via le réseau virtuel Tailscale.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez accéder au `GL-AXT1800` via son adresse IP (`192.168.29.1`) depuis `leo-phone`. Cela est possible car le GL-AXT1800 est l'appareil de niveau supérieur du `GL-MT2500`, et ce dernier est connecté au même réseau Tailscale que leo-phone.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Les étapes sont les suivantes.

1. Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    Activez **Allow Remote Access WAN**, puis cliquez sur **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Accédez à la console d'administration Tailscale ; une alerte indiquera que le GL-MT2500 possède des sous-réseaux.

    Cliquez sur l'icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Activez les routes de sous-réseau.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Vous pouvez maintenant accéder au GL-AXT1800 via son adresse IP (`192.168.29.1`) depuis d'autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.29.0/24`.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Autoriser l'accès à distance au LAN

Si cette option est activée, les ressources du côté LAN de l'appareil peuvent être accessibles via le réseau virtuel Tailscale.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez vous connecter en SSH à `Ubuntu` via son adresse IP (`192.168.8.110`) depuis `leo-phone`. Cela est possible car `Ubuntu` est l'appareil de niveau inférieur du `GL-MT2500`, et ce dernier est connecté au même réseau Tailscale que leo-phone.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Les étapes sont les suivantes.

1. Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    Activez **Allow Remote Access LAN**, puis cliquez sur **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Accédez à la console d'administration Tailscale ; une alerte indiquera que le GL-MT2500 possède des sous-réseaux.

    Cliquez sur l'icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Activez les routes de sous-réseau.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Vous pouvez maintenant envoyer un ping à Ubuntu ou vous y connecter en SSH via son adresse IP (`192.168.8.110`) depuis d'autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.8.0/24`.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Nœuds de sortie personnalisés

Par défaut, Tailscale fonctionne comme un réseau superposé : il achemine uniquement le trafic entre les appareils exécutant Tailscale et ne traite pas votre trafic Internet public, par exemple lorsque vous consultez des sites web comme Google.

Cependant, il peut arriver que vous souhaitiez utiliser Tailscale pour acheminer votre trafic Internet public. Par exemple, lorsque vous êtes loin de chez vous ou en voyage à l’étranger, si vous devez accéder à des services en ligne (comme votre banque) disponibles uniquement dans votre pays d’origine, vous pouvez définir votre ordinateur de bureau domestique disposant d’une IP publique comme nœud de sortie, puis configurer d’autres appareils sur le même Tailnet — comme le GL-AXT1800 et le GL-MT3000 montrés dans l’image ci-dessous — pour envoyer leur trafic via celui-ci. Tout votre trafic Internet public sera alors transféré par ce nœud de sortie.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Lorsque tout le trafic est acheminé via un nœud de sortie, vous utilisez en pratique les routes par défaut (`0.0.0.0/0`, `::/0`), ce qui fonctionne de façon similaire à une connexion VPN classique.

En résumé, un nœud de sortie achemine le trafic Internet sortant des appareils de votre Tailnet et agit ainsi comme un serveur VPN. Lorsque vous êtes connecté à un nœud de sortie, tout votre trafic Internet non Tailscale semble provenir de son emplacement, ce qui peut vous aider à accéder à des contenus géographiquement restreints et à renforcer votre confidentialité en ligne. L’appareil qui effectue ce transfert de trafic est appelé « nœud de sortie ».

**Remarque** : si le serveur DNS du routeur utilise une adresse IP privée accessible uniquement sur le réseau local, vous pouvez perdre l’accès à Internet lorsque vous utilisez un nœud de sortie. Pour résoudre ce problème, connectez-vous au routeur, accédez à **NETWORK** -> **DNS**, puis définissez manuellement un serveur DNS public tel que `8.8.8.8`.

---

Dans l’exemple suivant, un routeur GL.iNet **GL-MT2500** et un **Leo-Desktop** appartiennent au même Tailnet. Voici les étapes pour configurer Leo-Desktop comme nœud de sortie.

1. Activez les routes de sous-réseau du GL-MT2500 dans la console d’administration Tailscale.

    Accédez à la console d’administration Tailscale, cliquez sur l’icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez les routes de sous-réseau.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Sur l’appareil que vous souhaitez utiliser comme nœud de sortie, par exemple Leo-Desktop dans cet exemple, sélectionnez **Run exit node**. Voici un exemple sous Windows.

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Cliquez ensuite sur **Yes**.

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Dans la console d’administration Tailscale, configurez Leo-Desktop comme nœud de sortie.

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Connectez-vous au panneau d’administration web du GL-MT2500, accédez à **APPLICATIONS** -> **Tailscale** et activez **Custom Exit Nodes**. Cliquez sur le bouton d’actualisation, sélectionnez l’adresse IP de Leo-Desktop dans la liste déroulante, puis cliquez sur **Apply**.

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Les appareils connectés au routeur achemineront alors leur trafic via le nœud de sortie pour accéder à Internet, et tout votre trafic Internet semblera provenir de l’emplacement du nœud de sortie.

Référence : [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
