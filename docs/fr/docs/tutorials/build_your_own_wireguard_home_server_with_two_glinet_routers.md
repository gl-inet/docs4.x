# Créez votre propre serveur domestique WireGuard avec deux routeurs GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Cet article explique comment configurer votre routeur domestique comme serveur VPN WireGuard et votre routeur de voyage comme client VPN WireGuard afin qu'ils se connectent à distance. Vous pourrez ainsi utiliser l'adresse IP de votre domicile avec le routeur de voyage, où que vous soyez.

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise les modèles GL-MT5000 (Brume 3) et GL-MT3600BE (Beryl 7) pour présenter la configuration VPN.)</small>

Dans les étapes suivantes, nous prenons les modèles GL-MT6000 (Flint 2) et GL-MT3000 (Beryl AX) comme exemples :

- Le GL-MT6000, un routeur domestique, sera configuré comme serveur VPN WireGuard. Si la connectivité sans fil n'est pas nécessaire, notre passerelle de sécurité GL-MT2500 ou d'autres modèles peuvent également convenir.

- Le GL-MT3000, un routeur de voyage, sera configuré comme client VPN WireGuard pour se connecter à distance au serveur VPN situé à votre domicile.

## Pourquoi créer votre propre serveur domestique WireGuard {#why-build-your-own-wireguard-home-server}

1. Utilisez l’adresse IP publique de votre connexion à domicile pour que votre trafic semble en provenir.
2. Évitez les frais mensuels des services VPN tiers.
3. Chiffrez tout votre trafic Internet en le faisant transiter par un tunnel jusqu’à votre réseau domestique afin de protéger votre vie privée.
4. Accédez de n’importe où à vos appareils domestiques et à vos services de streaming locaux.

## Préparatifs {#preparations}

### Vérifier si vous disposez d'une adresse IP publique {#check-if-you-have-a-public-ip}

Tout d'abord, assurez-vous que le GL-MT6000 dispose d'une adresse IP publique sur son interface WAN, afin qu'il soit accessible depuis Internet. Sinon, votre routeur de voyage ne pourra pas établir de connexion VPN avec lui pendant vos déplacements.

Pour vérifier si vous avez une adresse IP publique, ouvrez un navigateur Web et saisissez [what is my ip](https://whatismyipaddress.com/){target="_blank"} dans la barre d'adresse.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Votre adresse IP publique s'affichera. Si elle correspond à l'adresse IP WAN fournie par votre FAI au GL-MT6000, vous disposez bien d'une adresse IP publique.

Si vous ne disposez pas d'une adresse IP publique, voici quelques méthodes possibles.

1. Si vous avez un routeur principal, connectez-vous-y et vérifiez s'il reçoit l'adresse IP publique de votre FAI.
2. Demandez une adresse IP publique à votre FAI. Cela peut entraîner des frais supplémentaires.
3. Si les deux méthodes ci-dessus ne fonctionnent pas (par exemple si votre réseau est derrière un CGNAT), vous pouvez essayer notre solution SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Vérifier si une redirection de port est nécessaire {#check-if-port-forwarding-is-required}

??? "GL.iNet comme routeur principal" 

    Si votre routeur GL.iNet est directement connecté à un modem de FAI via un câble Ethernet, le routeur GL.iNet est alors le routeur principal.

    **Comment vérifier si votre routeur GL.iNet est directement connecté au modem du FAI ?**

    Connectez-vous au panneau d’administration GL.iNet. Sélectionnez **INTERNET** dans la barre latérale gauche et vérifiez la topologie du réseau et les détails de la connexion.

    S'il est connecté directement via Ethernet, vous verrez une section nommée "Ethernet" avec des informations comme le protocole, l’adresse IP et la passerelle, etc.

    En prenant l'image suivante comme exemple, l'adresse IP mise en évidence correspond à l'adresse IP WAN fournie par le FAI pour ce routeur GL.iNet.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Cette adresse IP WAN est publique. Le routeur GL.iNet sert donc de routeur principal et **aucune redirection de port n’est nécessaire**.

    Il vous suffit de configurer ce routeur GL.iNet comme serveur WireGuard, puis un routeur de voyage comme client VPN WireGuard connecté au serveur. Un tunnel VPN sera alors établi entre eux.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet comme sous-routeur"

    Configurez la redirection de port (**Port Forwarding**) sur votre routeur principal pour le routeur GL.iNet si ce dernier est derrière un NAT.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Exemple : un routeur TP-Link comme routeur principal de votre domicile.

    Connectez-vous au Wi-Fi ou au LAN de votre routeur domestique. Connectez-vous ensuite au panneau d'administration Web. Vérifiez l'adresse IP WAN qu'il reçoit de votre FAI. Dans l'image ci-dessous, vous pouvez voir que votre adresse IP publique est **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Avant de configurer la redirection de port, nous recommandons de réserver une adresse IP pour le routeur GL.iNet sur votre routeur principal, afin qu'une adresse IP fixe lui soit attribuée.** Sinon, si le routeur principal ou le routeur GL.iNet redémarre, le routeur principal peut attribuer une autre adresse IP au routeur GL.iNet, ce qui fera échouer la règle de redirection de port.

    Configurez ensuite la redirection de port (**Port Forwarding**) sur votre routeur principal pour le routeur GL.iNet.

    1. Allez dans “Advanced”, cliquez sur “virtual Server”, puis sur “Add”.
    
    2. Internal IP (Device IP) : il s'agit de l'adresse IP attribuée au routeur GL.iNet ; vous pouvez la trouver dans la liste des clients TP-Link.
    
    3. External/Internal port : renseignez "51820" pour les deux champs.
    
    4. Protocol : vous pouvez choisir "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Autres exemples de [Port Forward](how_to_set_up_port_forwarding.md)**

## Configurer le serveur WireGuard {#set-up-wireguard-server}

1. Connectez-vous au panneau d’administration Web et accédez à **VPN** -> **WireGuard Server**. Cliquez sur **Generate Configuration** lors de la configuration initiale du serveur VPN.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Vérifiez la configuration.

    La configuration par défaut illustrée ci-dessous convient dans la plupart des cas.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** correspond à l’adresse IP du tunnel du serveur WireGuard. Conservez cette adresse si elle n’entre pas en conflit avec la passerelle de votre routeur en amont.

        En cas de conflit, remplacez l’adresse, par exemple par **10.1.0.1/24**, puis cliquez sur **Apply**. Incluez le préfixe CIDR « /24 » pour éviter des problèmes de connexion.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Par exemple, un routeur Xfinity en amont peut avoir l’adresse IP 10.0.0.1. Sur certains routeurs GL.iNet configurés comme serveurs WireGuard, cette adresse peut entrer en conflit avec l’adresse IP du tunnel. Modifiez l’adresse IP du tunnel uniquement en cas de conflit.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 est désactivé par défaut sur les routeurs GL.iNet. Pour utiliser une adresse IPv6, activez [IPv6](../interface_guide/ipv6.md) sur votre routeur.

    - **Listen Port**. Le serveur WireGuard écoute par défaut sur le port UDP `51820`. Si vous modifiez ce port et utilisez une redirection de port, adaptez la règle en amont pour qu’elle redirige le trafic vers le nouveau port d’écoute du serveur. Indiquez le port externe de la redirection dans le champ `Endpoint` de chaque profil client. Si le serveur est directement accessible, utilisez son port d’écoute.

    - **Enable Obfuscation**. Lorsque cette option est activée, le serveur VPN utilise le protocole AmneziaWG pour masquer le trafic VPN. Nous recommandons de conserver les réglages par défaut et de les modifier uniquement si vous connaissez ces paramètres.

        - [Obfuscation AmneziaWG sur les routeurs GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Configurer l’obfuscation VPN sur les routeurs GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Ajoutez un profil.

    Dans l’onglet **Profiles**, cliquez sur **Add** pour créer un profil pour votre appareil.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Donnez-lui un nom explicite, puis cliquez sur **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Si nécessaire, cliquez sur **Set More** pour accéder aux paramètres avancés. Cliquez ensuite sur **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Ajouter des règles de routage si nécessaire"

        Dans la plupart des cas, les règles de routage sont facultatives.

        Pour accéder depuis le serveur aux appareils du réseau local du client WireGuard, ouvrez l’onglet **Route Rules** de la page **WireGuard Server** et configurez les règles. Consultez la [procédure d’accès au réseau local du client](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Sinon, passez à l’étape 4 pour télécharger une configuration client.

4. Téléchargez la configuration.

    Après avoir ajouté un profil et cliqué sur **Apply**, vous pouvez récupérer la configuration sous forme de code QR, de texte brut ou de fichier `.conf` téléchargeable.

    - **Code QR**. Scannez le code dans l’application WireGuard pour importer un profil WireGuard standard. Si vous avez activé l’obfuscation, utilisez l’application AmneziaWG ou un autre client compatible avec l’obfuscation AmneziaWG.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Texte brut**. Consultez les paramètres de configuration et copiez-les pour les appliquer manuellement, par exemple dans l’application WireGuard ou sur un routeur GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **Fichier .conf**. Cliquez sur **Download** pour enregistrer le fichier sur votre appareil. Vous pouvez l’importer directement dans l’application WireGuard ou sur un routeur GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    Depuis la version v4.8 du micrologiciel, vous pouvez choisir comme adresse du serveur l’adresse IP publique, le domaine DDNS ou l’adresse IP WAN actuelle. Si vous modifiez ce choix, l’adresse du serveur dans le fichier de configuration est mise à jour en même temps.

    Par exemple, si l’adresse IP publique de votre réseau change régulièrement, activez le [DDNS](../interface_guide/ddns.md) et utilisez le domaine DDNS comme adresse du serveur.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Cliquez sur **Start** dans le coin supérieur droit pour démarrer le serveur WireGuard. L’état de la connexion s’affiche sur la même page.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Configurer le client VPN WireGuard {#set-up-wireguard-client}

### Changer l'adresse IP LAN {#change-the-lan-ip}

Dans ce tutoriel, nous utilisons les GL-MT6000 et GL-MT3000 comme exemples. Leur adresse IP LAN par défaut est **192.168.8.1** pour les deux, nous devons donc modifier l'une d'elles afin d'éviter un conflit. 

Modifiez l’adresse IP LAN du GL-MT3000, qui sert de client WireGuard.

Connectez-vous au panneau d’administration Web du GL-MT3000 et accédez à **NETWORK** -> **LAN**. Remplacez l’adresse IP LAN par défaut 192.168.8.1, par exemple par `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Ajouter la configuration {#add-the-configuration}

Dans le panneau d'administration Web du GL-MT3000, allez dans **VPN** -> **WireGuard Client**, puis cliquez sur **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Créez un groupe à gauche et définissez un nom, puis sélectionnez le fichier de configuration à téléverser ou faites-le glisser dans la zone d'import à droite.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Après validation du fichier, cliquez sur **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Vous pouvez également cliquer sur **Manually Add Configuration**, coller le texte de configuration, puis cliquer sur **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Le fichier de configuration s'affichera sur la page **WireGuard Client** une fois le téléversement réussi.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Démarrer la connexion {#start-the-connection}

Cliquez sur l'icône à trois points puis sur **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Patientez quelques minutes. Une fois la connexion établie, un point vert s'allumera.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Accédez à **VPN Dashboard** ; vous verrez que votre client se connecte au serveur avec l'adresse IP publique de votre domicile. La page peut varier légèrement selon la version du firmware.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Reconnectez-vous au panneau d'administration web du GL-MT6000 (le serveur WireGuard), allez dans **VPN** -> **WireGuard Server** (ou dans **VPN** -> **VPN Dashboard** si vous utilisez le firmware v.4.7 ou une version antérieure) ; vous verrez également l'état de la connexion, indiquant que le client est bien connecté.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Page WireGuard Server dans le firmware v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Page VPN Dashboard dans le firmware v4.7 et antérieur)</small>

## Préparer le dépannage VPN à distance {#prep-for-remote-vpn-fixes-ahead}

Associez les deux routeurs à votre compte GoodCloud avant de partir. Vous pourrez ainsi effectuer un dépannage à distance si votre connexion VPN échoue en raison de problèmes de configuration ou de réseau. L’accès à distance ne fonctionne que si les routeurs restent allumés et connectés à Internet.

---

Articles associés

- [Configurer un serveur WireGuard sur les routeurs GL.iNet](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
