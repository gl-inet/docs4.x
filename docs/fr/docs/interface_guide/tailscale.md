# Tailscale

Tailscale est un service VPN qui permet d'accéder à vos appareils et applications partout dans le monde, de manière sécurisée et simple. Pour plus d'informations sur Tailscale, veuillez consulter le [site officiel de Tailscale](https://tailscale.com/).

La fonctionnalité Tailscale des routeurs GL.iNet, disponible depuis le firmware V4.2, permet au routeur de rejoindre un réseau virtuel Tailscale. Une fois connecté, vous pouvez accéder au routeur à distance, y compris à ses ressources WAN et LAN.

**Remarque** :

1. Comme Tailscale est basé sur WireGuard, il n'est pas recommandé d'utiliser Tailscale en même temps que l'une des fonctionnalités ou services suivants, car cela peut provoquer des conflits de routage : OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp.

2. Cette fonctionnalité est actuellement en version bêta et peut comporter certains bugs.

3. Certains modèles, bien qu'ils exécutent le firmware v4.2 ou une version ultérieure, ne prennent pas en charge Tailscale en raison d'une mémoire insuffisante.

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

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Activez Tailscale sur le routeur GL.iNet.

    Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Activez Tailscale, puis cliquez sur **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Après un court instant, l'interface affichera un **Device Bind Link**. Cliquez dessus.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    Un lien Tailscale s'affichera dans la fenêtre contextuelle. Cliquez dessus pour être redirigé vers le site Tailscale et vous connecter.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Une fois connecté, il vous sera demandé de confirmer l'appareil à connecter. Cliquez sur **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Lorsque la connexion est établie avec succès, vous serez automatiquement redirigé vers la console d'administration Tailscale. Vous pourrez constater que l'adresse IP du GL-MT2500 est `100.88.54.21`. Vous pouvez désormais utiliser cette adresse IP pour accéder au routeur.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

4. Testez la connectivité.

    Sur les appareils connectés au même réseau Tailscale, vous pouvez tester la connectivité des trois manières suivantes.

    * Utiliser la commande ping

        ![ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * Se connecter au routeur en SSH

        ![ssh](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Accéder au panneau d'administration web

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Autoriser l'accès à distance au WAN

> Cette fonction a été renommée **Advertise WAN Subnets** dans le firmware v4.9 et les versions ultérieures.

Lorsque cette option est activée, les ressources côté WAN de l’appareil sont accessibles via le réseau virtuel Tailscale. Les routes ne prennent effet qu’après approbation dans la Tailscale Admin Console.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez accéder au `GL-AXT1800` via son adresse IP (`192.168.29.1`) depuis `leo-phone`. Cela est possible car le GL-AXT1800 est l'appareil de niveau supérieur du `GL-MT2500`, et ce dernier est connecté au même réseau Tailscale que leo-phone.

![topologie d'accès à distance au WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Les étapes sont les suivantes.

1. Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    Activez **Allow Remote Access WAN**, puis cliquez sur **Apply**.

    ![activer l'accès à distance au WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Accédez à la console d'administration Tailscale ; une alerte indiquera que le GL-MT2500 possède des sous-réseaux.

    Cliquez sur l'icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Activez les routes de sous-réseau.

    ![activer la route de sous-réseau Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Vous pouvez maintenant accéder au GL-AXT1800 via son adresse IP (`192.168.29.1`) depuis d'autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.29.0/24`.

    ![accès à l'AXT1800 via Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Autoriser l'accès à distance au LAN

> Cette fonction a été renommée **Advertise LAN Subnets** dans le firmware v4.9 et les versions ultérieures.

Lorsque cette option est activée, les ressources côté LAN de l’appareil sont accessibles via le réseau virtuel Tailscale. Les routes ne prennent effet qu’après approbation dans la Tailscale Admin Console.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez vous connecter en SSH à `Ubuntu` via son adresse IP (`192.168.8.110`) depuis `leo-phone`. Cela est possible car `Ubuntu` est l'appareil de niveau inférieur du `GL-MT2500`, et ce dernier est connecté au même réseau Tailscale que leo-phone.

![topologie d'accès à distance au LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Les étapes sont les suivantes.

1. Connectez-vous au panneau d'administration web de votre routeur, puis accédez à **APPLICATIONS** -> **Tailscale**.

    Activez **Allow Remote Access LAN**, puis cliquez sur **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Accédez à la console d'administration Tailscale ; une alerte indiquera que le GL-MT2500 possède des sous-réseaux.

    Cliquez sur l'icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Activez les routes de sous-réseau.

    ![activer la route de sous-réseau Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Vous pouvez maintenant envoyer un ping à Ubuntu ou vous y connecter en SSH via son adresse IP (`192.168.8.110`) depuis d'autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.8.0/24`.

    ![accès à Ubuntu via Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Nœuds de sortie personnalisés

Par défaut, Tailscale fonctionne comme un réseau superposé : il achemine uniquement le trafic entre les appareils exécutant Tailscale et ne traite pas votre trafic Internet public, par exemple lorsque vous consultez des sites web comme Google.

Cependant, il peut arriver que vous souhaitiez utiliser Tailscale pour acheminer votre trafic Internet public. Par exemple, lorsque vous êtes loin de chez vous ou en voyage à l’étranger, si vous devez accéder à des services en ligne (comme votre banque) disponibles uniquement dans votre pays d’origine, vous pouvez définir votre ordinateur de bureau domestique disposant d’une IP publique comme nœud de sortie, puis configurer d’autres appareils sur le même Tailnet — comme le GL-AXT1800 et le GL-MT3000 montrés dans l’image ci-dessous — pour envoyer leur trafic via celui-ci. Tout votre trafic Internet public sera alors transféré par ce nœud de sortie.

![exitnode](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Lorsque tout le trafic est acheminé via un nœud de sortie, vous utilisez en pratique les routes par défaut (`0.0.0.0/0`, `::/0`), ce qui fonctionne de façon similaire à une connexion VPN classique.

En résumé, un nœud de sortie achemine le trafic Internet sortant des appareils de votre Tailnet et agit ainsi comme un serveur VPN. Lorsque vous êtes connecté à un nœud de sortie, tout votre trafic Internet non Tailscale semble provenir de son emplacement, ce qui peut vous aider à accéder à des contenus géographiquement restreints et à renforcer votre confidentialité en ligne. L’appareil qui effectue ce transfert de trafic est appelé « nœud de sortie ».

**Remarque** : si le serveur DNS du routeur utilise une adresse IP privée accessible uniquement sur le réseau local, vous pouvez perdre l’accès à Internet lorsque vous utilisez un nœud de sortie. Pour résoudre ce problème, connectez-vous au routeur, accédez à **NETWORK** -> **DNS**, puis définissez manuellement un serveur DNS public tel que `8.8.8.8`.

---

Dans l’exemple suivant, un routeur GL.iNet **GL-MT2500** et un **Leo-Desktop** appartiennent au même Tailnet. Voici les étapes pour configurer Leo-Desktop comme nœud de sortie.

1. Activez les routes de sous-réseau du GL-MT2500 dans la console d’administration Tailscale.

    Accédez à la console d’administration Tailscale, cliquez sur l’icône à trois points à droite du GL-MT2500, puis sélectionnez **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, activez les routes de sous-réseau.

    ![activer la route de sous-réseau Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Sur l’appareil que vous souhaitez utiliser comme nœud de sortie, par exemple Leo-Desktop dans cet exemple, sélectionnez **Run exit node**. Voici un exemple sous Windows.

    ![Tailscale Windows exécuter un nœud de sortie](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Cliquez ensuite sur **Yes**.

    ![Tailscale Windows confirmation du nœud de sortie](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Dans la console d’administration Tailscale, configurez Leo-Desktop comme nœud de sortie.

    ![paramètres de route Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Connectez-vous au panneau d’administration web du GL-MT2500, accédez à **APPLICATIONS** -> **Tailscale** et activez **Custom Exit Nodes**. Cliquez sur le bouton d’actualisation, sélectionnez l’adresse IP de Leo-Desktop dans la liste déroulante, puis cliquez sur **Apply**.

    ![nœud de sortie personnalisé GL.iNet Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Les appareils connectés au routeur achemineront alors leur trafic via le nœud de sortie pour accéder à Internet, et tout votre trafic Internet semblera provenir de l’emplacement du nœud de sortie.

5. **Dépannage** : après avoir activé **Custom Exit Nodes**, si les appareils connectés au routeur GL.iNet ne peuvent pas accéder à Internet, vérifiez si les routes de sous-réseau du routeur sont activées dans la console d’administration Tailscale.

    Une invite correspondante peut apparaître dans le panneau d’administration web du routeur, comme illustré ci-dessous.

    ![dépannage du nœud de sortie](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Pour résoudre ce problème, activez les routes de sous-réseau du routeur dans la console d’administration Tailscale comme indiqué à l’**étape 1** ci-dessus.

## Run Exit Node

> Cette fonction est introduite avec le firmware v4.9.

Exécuter un nœud de sortie sur le routeur permet aux autres appareils du tailnet de faire passer tout leur trafic Internet sortant par l’adresse IP publique de ce routeur.

Dans la topologie ci-dessous, un ordinateur portable se trouve à Boston et le routeur GL-BE9300 est installé à Hong Kong. Les deux ont été ajoutés au même tailnet Tailscale. Si vous définissez le GL-BE9300 comme nœud de sortie, tout le trafic sortant de l’ordinateur portable sortira vers Internet par ce routeur à Hong Kong, et l’adresse IP publique externe de l’ordinateur portable sera reconnue comme une IP de Hong Kong au lieu d’une IP de Boston.

![topology run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Conseil** : nous recommandons de désactiver l’expiration de la clé du nœud de sortie afin d’éviter les interruptions lorsque la clé d’authentification expire.*

Suivez ces étapes pour configurer le GL-BE9300 comme Exit Node.

1. Ajoutez le GL-BE9300 et l’ordinateur portable de voyage au même tailnet Tailscale.

    ![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. Dans le Web Admin Panel du GL-BE9300, activez **Run Exit Node** et cliquez sur **Apply**.

    ![run exit node1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. Dans la Tailscale Admin Console, l’étiquette "Exit Node" apparaît sous le GL-BE9300.

    ![run exit node2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Cliquez sur l’icône à trois points à côté du GL-BE9300 et sélectionnez **Edit route settings**.

    ![run exit node3](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. Cochez **Use as exit node** et cliquez sur **Save**.

    ![run exit node4](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Désactivez l’expiration de la clé.

    Par sécurité, les utilisateurs doivent se réauthentifier périodiquement sur chacun de leurs appareils. Pour éviter les interruptions de connexion lorsque la clé d’authentification du nœud de sortie expire, nous recommandons de désactiver l’expiration de la clé pour votre nœud de sortie. Cliquez [ici](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"} pour plus de détails sur l’expiration des clés.

    Cliquez sur l’icône à trois points à droite du GL-BE9300 et sélectionnez **Disable key expiry**.

    ![disable key expiry1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    L’étiquette "Expiry disabled" apparaît ensuite.

    ![disable key expiry2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Sélectionnez GL-BE9300 comme nœud de sortie pour votre ordinateur portable de voyage.

    Lancez Tailscale sur l’ordinateur portable de voyage. L’icône Tailscale apparaît dans la zone de notification en bas à droite.

    Faites un clic droit sur l’icône, cliquez sur **Exit nodes**, puis sélectionnez **gl-be9300**.

    ![run exit node5](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    Désormais, tout le trafic sortant de cet ordinateur portable de voyage passera par GL-BE9300 pour accéder à Internet.

8. Testez la connectivité.

    1. Sur l’ordinateur portable de voyage, ouvrez un navigateur web et consultez [ipcheck.ing](https://ipcheck.ing/){target="_blank"} ou un autre site de vérification d’IP. La page affichera l’adresse IP publique appartenant à votre nœud de sortie Tailscale, confirmant que l’ordinateur portable accède à Internet via ce nœud de sortie, ici le GL-BE9300 situé à Hong Kong.

        ![ip hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Appuyez sur `Win+R`, saisissez `cmd` pour ouvrir l’invite de commandes, puis exécutez `tracert google.com` afin de tracer les routes du trafic sortant. La sortie de commande liste tous les sauts de routage de votre trafic Internet. Si la configuration est correcte, le premier saut externe passe par le nœud de sortie, comme ci-dessous.

        ![tracert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Déconnectez le nœud de sortie pour effectuer un test comparatif.

        Faites un clic droit sur l’icône Tailscale dans la zone de notification en bas à droite, cliquez sur **Exit nodes**, puis sélectionnez **None** pour arrêter d’utiliser le nœud de sortie.

        ![comparative test](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Ouvrez un nouvel onglet de navigateur et consultez [ipcheck.ing](https://ipcheck.ing/){target="_blank"} ou un autre service de vérification d’IP. L’adresse IP publique native de l’ordinateur portable s’affiche alors, ce qui prouve que l’appareil utilise à nouveau sa connexion Internet locale, Boston dans cet exemple.

        ![ip boston](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}

---

Référence : [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
