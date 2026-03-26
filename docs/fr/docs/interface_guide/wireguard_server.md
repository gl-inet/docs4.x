# Configurer un serveur WireGuard sur les routeurs GL.iNet

WireGuard® est un VPN extrêmement simple, rapide et moderne qui utilise une cryptographie de pointe. Il vise à être plus rapide, plus simple, plus léger et plus pratique qu'IPSec, tout en évitant sa complexité. Il offre également de meilleures performances qu'OpenVPN.

Pour configurer un serveur WireGuard sur un routeur GL.iNet, regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Vérifier que vous disposez d'une adresse IP publique

Cliquez [ici](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) pour vérifier si votre fournisseur d'accès à Internet vous attribue une adresse IP publique.

**Si ce n'est pas le cas, votre routeur ne peut pas être configuré comme serveur WireGuard.**

Méthodes alternatives :

1. Si vous avez un routeur principal, connectez-vous-y et vérifiez s'il reçoit une adresse IP publique de votre FAI.
2. Demandez une adresse IP publique à votre FAI. Cela peut entraîner des frais supplémentaires.
3. Si les deux méthodes ci-dessus ne fonctionnent pas (par exemple si votre réseau est derrière un CGNAT), vous pouvez essayer notre solution SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Vérifier si une redirection de ports est nécessaire

**Topologie réseau**

??? "GL.iNet est le routeur principal"

    * Si le routeur GL.iNet est le routeur principal de votre réseau, aucune redirection de ports n'est nécessaire. Passez directement à [l'étape suivante](#configurer-le-serveur-wireguard).

??? "GL.iNet est le sous-routeur"

    * Si un routeur principal est déjà utilisé et que le routeur GL.iNet est configuré comme routeur secondaire, vous devez configurer une [redirection de ports](../tutorials/how_to_set_up_port_forwarding.md) sur le routeur principal.

    * Si un routeur principal est déjà utilisé et que le routeur GL.iNet se trouve à plusieurs niveaux en dessous du routeur principal, configurez une [redirection de ports](../tutorials/how_to_set_up_port_forwarding.md) à chaque niveau intermédiaire.

## Configurer le serveur WireGuard {#configurer-le-serveur-wireguard}

Connectez-vous au panneau d'administration web, puis accédez à **VPN** -> **WireGuard Server**.

1. Cliquez sur **Generate Configuration** (uniquement pour la configuration initiale du serveur VPN).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Vérifiez la configuration.

    La configuration par défaut convient à la plupart des cas, comme ci-dessous. Il n'est pas nécessaire de modifier l'adresse IPv4 si elle n'entre pas en conflit avec la passerelle de votre routeur amont.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    (L'IPv6 est désactivé par défaut sur GL.iNet. Si vous souhaitez utiliser une adresse IPv6, activez d'abord IPv6 sur votre routeur.)

    Si vous constatez que l'adresse IPv4 entre en conflit avec la passerelle du routeur amont, remplacez-la par une autre, par exemple **10.1.0.1/24**, puis cliquez sur **Apply**. Veillez à conserver la notation CIDR `/24` afin d'éviter des problèmes de connectivité.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Par exemple, si un routeur Xfinity se trouve en amont du routeur GL.iNet, son adresse IP peut être `10.0.0.1`, ce qui entre en conflit avec l'adresse IP du tunnel WireGuard lorsque le routeur GL.iNet est configuré comme serveur WireGuard. Vous devez alors effectuer la modification ci-dessus.

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Ajoutez un profil.

    Passez à l'onglet **Profiles**, puis cliquez sur **Add** pour générer un profil pour votre appareil.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Définissez un nom explicite puis cliquez sur **Apply** pour continuer.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Si vous devez définir des paramètres avancés, cliquez sur **Set More**, puis sur **Apply** pour continuer.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Ajouter des règles de routage si nécessaire"

        Il n'est pas nécessaire d'ajouter des règles de routage dans la plupart des cas.

        Si vous souhaitez accéder depuis le serveur aux appareils LAN du client WireGuard, ouvrez l'onglet **Route Rules** de la page **WireGuard Server** pour configurer les règles de routage. Cliquez [ici](../tutorials/wireguard_server_access_to_client_lan_side.md) pour plus d'instructions.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        Sinon, passez à l'étape 4 pour télécharger la configuration client.

4. Téléchargez la configuration.

    Après avoir ajouté un profil et cliqué sur Apply, un fichier de configuration sera généré en trois formats : code QR, texte brut et fichier `.conf`. Choisissez la méthode qui vous convient.

    - **QR code** : adapté aux appareils terminaux (par ex. smartphone, tablette, ordinateur portable) sur lesquels l'application WireGuard est installée. Ouvrez simplement l'application WireGuard, scannez le code QR et la configuration sera importée automatiquement.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text** : ce format vous permet de consulter les détails de la configuration et de copier-coller facilement son contenu pour une configuration manuelle, par exemple dans l'application WireGuard ou sur un routeur GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file** : cliquez sur **Download** pour enregistrer le fichier `.conf` sur votre appareil local. Il peut ensuite être téléversé directement dans l'application WireGuard ou sur un routeur GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    Si nécessaire, vous pouvez choisir l'adresse du serveur parmi l'IP publique, le domaine DDNS et l'IP WAN actuelle. Cette fonctionnalité est disponible depuis le firmware v4.8. Une fois modifiée, l'adresse du serveur est mise à jour simultanément dans le fichier de configuration.

    Par exemple, il est recommandé d'activer [DDNS](ddns.md) et d'utiliser le domaine DDNS comme adresse de serveur si l'IP publique de votre réseau change fréquemment.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Démarrez le serveur WireGuard.

    Cliquez sur le bouton **Start** en haut à droite pour démarrer le serveur WireGuard.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    L'état de la connexion s'affichera sur la même page.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Vérifier que le serveur WireGuard fonctionne correctement

### Vérifier l'état du serveur

Depuis le firmware v4.8, vous pouvez vérifier l'état de connexion du serveur sur la page **WireGuard Server**.

Si des statistiques de trafic montant/descendant et des appareils connectés en ligne s'affichent, cela signifie que le serveur WireGuard fonctionne et que des clients WireGuard y sont connectés.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

S'il affiche 0 trafic et 0 client, cela signifie qu'aucun client WireGuard n'est connecté.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

Pour le firmware v4.7 et les versions antérieures, veuillez vérifier l'état de connexion du serveur sur la page **VPN Dashboard**.

### Vérifier l'IP du client

Pour vérifier qu'une connexion au serveur est établie avec succès, importez la configuration WireGuard précédemment exportée sur un appareil situé sur un autre réseau (et non sur le même réseau local que le serveur). Ouvrez ensuite un navigateur web et recherchez votre adresse IP et votre position. Si elles correspondent à l'IP et à l'emplacement du serveur VPN (et non à ceux de votre FAI), la connexion VPN est réussie.

La méthode la plus simple consiste à utiliser un smartphone avec l'[application officielle WireGuard](https://www.wireguard.com/install){target="_blank"}. Désactivez d'abord le Wi-Fi du smartphone et connectez-le uniquement via les données cellulaires (4G/5G). Ouvrez ensuite l'application WireGuard, importez le fichier de configuration et lancez la connexion. Vérifiez que le smartphone peut accéder à Internet et que son adresse IP correspond à celle du serveur WireGuard.

En cas d'échec de la connexion, voici quelques causes fréquentes :

* Votre fournisseur d'accès à Internet ne vous attribue pas d'adresse IP publique. Vérifiez [ici](#vérifier-que-vous-disposez-dune-adresse-ip-publique).
* Vous devez peut-être configurer une redirection de ports. Vérifiez [ici](#vérifier-si-une-redirection-de-ports-est-nécessaire).
* Le port utilisé par le serveur WireGuard est bloqué par votre fournisseur d'accès à Internet. Changez de port ou contactez-le pour plus d'assistance.
* Certains pays ou certaines régions peuvent bloquer la connexion VPN.

## Installation de l'application WireGuard

Téléchargez l'application WireGuard depuis le [site officiel de WireGuard](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® est une marque déposée de Jason A. Donenfeld.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
