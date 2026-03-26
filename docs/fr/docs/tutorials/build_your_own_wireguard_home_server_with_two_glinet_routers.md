# Créez votre propre serveur domestique WireGuard avec deux routeurs GL.iNet

Cet article explique comment configurer votre routeur domestique comme serveur VPN WireGuard et votre routeur de voyage comme client VPN WireGuard afin qu'ils se connectent à distance. Vous pourrez ainsi utiliser l'adresse IP de votre domicile avec le routeur de voyage, où que vous soyez.

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise les modèles GL-MT5000 (Brume 3) et GL-MT3600BE (Beryl 7) pour présenter la configuration VPN.)</small>

Dans les étapes suivantes, nous prenons les modèles GL-MT6000 (Flint 2) et GL-MT3000 (Beryl AX) comme exemples :

- Le GL-MT6000, un routeur domestique, sera configuré comme serveur VPN WireGuard. Si la connectivité sans fil n'est pas nécessaire, notre passerelle de sécurité GL-MT2500 ou d'autres modèles peuvent également convenir.

- Le GL-MT3000, un routeur de voyage, sera configuré comme client VPN WireGuard pour se connecter à distance au serveur VPN situé à votre domicile.

## Pourquoi créer votre propre serveur domestique WireGuard

1. Utilisez l'adresse IP de votre domicile comme adresse Internet, comme si vous étiez chez vous.
2. Aucuns frais mensuels à payer, contrairement à un service VPN tiers.
3. Faites passer tout le trafic Internet par votre réseau domestique via un tunnel VPN chiffré et protégez votre confidentialité.
4. Accédez facilement à vos ressources internes et à votre streaming local.

## Préparatifs

### Vérifier si vous disposez d'une adresse IP publique

Tout d'abord, assurez-vous que le GL-MT6000 dispose d'une adresse IP publique sur son interface WAN, afin qu'il soit accessible depuis Internet. Sinon, votre routeur de voyage ne pourra pas établir de connexion VPN avec lui pendant vos déplacements.

Pour vérifier si vous avez une adresse IP publique, ouvrez un navigateur Web et saisissez [what is my ip](https://whatismyipaddress.com/){target="_blank"} dans la barre d'adresse.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Votre adresse IP publique s'affichera. Si elle correspond à l'adresse IP WAN fournie par votre FAI au GL-MT6000, vous disposez bien d'une adresse IP publique.

Si vous ne disposez pas d'une adresse IP publique, voici quelques méthodes possibles.

1. Si vous avez un routeur principal, connectez-vous-y et vérifiez s'il reçoit l'adresse IP publique de votre FAI.
2. Demandez une adresse IP publique à votre FAI. Cela peut entraîner des frais supplémentaires.
3. Si les deux solutions ci-dessus ne fonctionnent pas, par exemple si vous êtes derrière un CGNAT, vous pouvez utiliser une méthode de proxy inverse comme [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md). Vous pouvez également essayer une solution SDWAN : [AstroWarp](https://www.astrowarp.net/).

### Vérifier si une redirection de port est nécessaire

??? "GL.iNet comme routeur principal" 

    Si votre routeur GL.iNet est directement connecté à un modem de FAI via un câble Ethernet, le routeur GL.iNet est alors le routeur principal.

    **Comment vérifier si votre routeur GL.iNet est directement connecté au modem du FAI ?**

    Étapes :
    
    1. Connectez-vous au panneau d'administration GL.iNet. 

    2. Sélectionnez **INTERNET** dans la barre latérale gauche. Vérifiez la topologie et les détails de connexion :

        S'il est connecté directement via Ethernet, vous verrez une section nommée "Ethernet" avec des informations comme Protocol, IP address, Gateway, etc.

        En prenant l'image suivante comme exemple, l'adresse IP mise en évidence correspond à l'adresse IP WAN fournie par le FAI pour ce routeur GL.iNet. 

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Cette adresse IP WAN est une adresse IP publique ; ce routeur GL.iNet, utilisé comme routeur principal, dispose donc d'une adresse IP publique et **il n'est pas nécessaire de configurer une redirection de port**.

        Il vous suffit de configurer ce routeur GL.iNet comme serveur WireGuard, puis un routeur de voyage comme client VPN WireGuard connecté au serveur. Un tunnel VPN sera alors établi entre eux.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}
    
??? "GL.iNet comme sous-routeur"

    Configurez la redirection de port (**Port Forwarding**) sur votre routeur principal pour le routeur GL.iNet si ce dernier est derrière un NAT.

    Topologie

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

## Configurer le serveur WireGuard

### Activer DDNS (facultatif)

Activez la fonction DDNS si vous n'avez pas d'adresse IP publique statique mais uniquement une adresse IP publique dynamique.

Connectez-vous au panneau d'administration Web du GL-MT6000 et allez dans **APPLICATIONS** -> **Dynamic DNS**. Activez l'interrupteur **Enable DDNS**.

Cochez **Terms of Service & Privacy Policy** puis cliquez sur **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Allez ensuite dans l'onglet **Configuration** de **WireGuard Server**, assurez-vous que le port d’écoute est 51820, puis cliquez sur **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Générer la configuration

Sur la même page, cliquez sur l'onglet **Profiles** à côté de l'onglet **Configuration**, puis cliquez sur **Add** (repéré par le numéro 1 dans l'image ci-dessous).

Une configuration client sera générée automatiquement. Cliquez sur l'**icône de transfert** (repérée par le numéro 2).

Dans la fenêtre contextuelle, activez **DDNS Domain** (repéré par le numéro 3, option facultative à activer uniquement si vous avez une adresse IP publique dynamique).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Vous pouvez ensuite scanner le code QR à l'aide de l'[application mobile](https://www.wireguard.com/install/) WireGuard pour tester le serveur. Pour plus de détails, cliquez [ici](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

Vous pouvez aussi exporter une configuration au format texte pour la connexion du client VPN.

Basculez la configuration du code QR vers le format texte en cliquant sur l'onglet **Configuration File**. 

Copiez le texte destiné au client, ou cliquez sur le bouton Download et enregistrez-le pour une utilisation ultérieure.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Configurer le client VPN WireGuard

### Changer l'adresse IP LAN

Dans ce tutoriel, nous utilisons les GL-MT6000 et GL-MT3000 comme exemples. Leur adresse IP LAN par défaut est **192.168.8.1** pour les deux, nous devons donc modifier l'une d'elles afin d'éviter un conflit. 

Voici les étapes pour modifier l'adresse IP LAN du GL-MT3000 (le client VPN WireGuard).

Connectez-vous au panneau d'administration Web du GL-MT3000, puis allez dans **NETWORK** -> **LAN** pour modifier l'adresse IP LAN. Par exemple, vous pouvez remplacer l'adresse IP LAN par défaut 192.168.8.1 par `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Pour plus de détails sur l'interface LAN, cliquez [ici](../interface_guide/lan.md).

### Ajouter la configuration

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

### Démarrer la connexion

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

## Préparer le dépannage VPN à distance

En cas de problème imprévu pendant vos déplacements, associez à l'avance les deux routeurs à votre compte GoodCloud afin de faciliter le dépannage VPN à distance.

Votre serveur peut parfois être indisponible à cause d'une coupure de courant ou d'autres raisons. Pour préserver son accessibilité, veuillez l'associer à GL.iNet GoodCloud. 

---

Articles associés

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
