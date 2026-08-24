# Configurer le serveur OpenVPN sur les routeurs GL.iNet

OpenVPN est un protocole VPN open source qui utilise des techniques de réseau privé virtuel pour établir des connexions sécurisées site à site ou point à point.

Pour configurer le serveur OpenVPN sur un routeur GL.iNet, regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Assurez-vous d'avoir une adresse IP publique {#make-sure-you-have-a-public-ip-address}

Veuillez cliquer [ici](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) pour vérifier si votre fournisseur d'accès Internet vous attribue une adresse IP publique.

**Sinon, votre routeur ne peut pas être configuré en tant que serveur OpenVPN.**

Méthodes alternatives :

1. Si vous disposez d'un routeur principal, connectez-vous à celui-ci et vérifiez s'il reçoit une adresse IP publique de votre FAI.
2. Demandez une adresse IP publique à votre FAI. Cela peut entraîner des frais supplémentaires.
3. Si les deux méthodes ci-dessus ne fonctionnent pas (par exemple si votre réseau est derrière un CGNAT), vous pouvez essayer notre solution SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}. 

## Vérifiez si la redirection de port est nécessaire {#confirm-if-port-forwarding-is-required}

**Topologie réseau**

??? "GL.iNet est le routeur principal"
    
    * Si le routeur GL.iNet est le routeur principal de votre réseau, aucune redirection de port n'est nécessaire. Passez à l'[étape suivante](#setup-openvpn-server).

??? " GL.iNet est le sous-routeur"

    * Si un routeur principal est déjà utilisé et que le routeur GL.iNet est configuré comme routeur secondaire, vous devez configurer la [redirection de port](../tutorials/how_to_set_up_port_forwarding.md) sur le routeur principal.
    
    * Si un routeur principal est déjà utilisé et que le routeur GL.iNet se trouve à plusieurs niveaux sous le routeur principal, configurez la [redirection de port](../tutorials/how_to_set_up_port_forwarding.md) à chaque niveau intermédiaire.

## Configurer le serveur OpenVPN {#setup-openvpn-server}

Connectez-vous au panneau d'administration web, puis accédez à **VPN** -> **OpenVPN Server**.

1. Cliquez sur **Generate Configuration** (uniquement lors de la configuration initiale du serveur VPN).

    ![ovpnserver generate config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_generate.png){class="glboxshadow"}

2. Appliquez la configuration.

    La configuration par défaut convient à la plupart des cas.
    
    Si vous n'avez pas besoin de la modifier, cliquez sur **Export Client Configuration** en bas de la page et passez à l'étape 3. 
    
    Si vous avez modifié la configuration, cliquez sur **Apply** avant d'exporter la configuration du client.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S ou Tun. Cliquez [ici](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode) pour voir les différences.

    * **Protocol:** UDP ou TCP. Cliquez [ici](../faq/openvpn_tcp_udp.md) pour voir les différences.

    * **Authentication Mode:** ce paramètre détermine la méthode d'authentification utilisée lorsque le client se connecte au serveur. Trois options sont disponibles.

        - **Certificate Only** : si cette option est sélectionnée, le routeur génère automatiquement les clés de certificat du serveur et du client, puis les intègre au fichier de configuration du client. Lorsque vous chargez la configuration sur le client, aucun identifiant supplémentaire n'est requis.

        - **Username/Password Only** : si cette option est sélectionnée, le routeur génère une configuration client sans clés de certificat. Vous devez d'abord ajouter un nom d'utilisateur et un mot de passe dans l'onglet Users avant d'exporter la configuration du client. Lors du chargement de la configuration sur le client, vous devrez saisir ces identifiants pour l'authentification.

        - **Username/Password and Certificate** : si cette option est sélectionnée, vous devez d'abord ajouter un nom d'utilisateur et un mot de passe dans l'onglet Users avant d'exporter la configuration du client ; ensuite, le routeur génère automatiquement les clés de certificat du serveur et du client et les intègre au fichier de configuration. Lors du chargement de la configuration sur le client, la clé de certificat est d'abord vérifiée, puis l'authentification par nom d'utilisateur et mot de passe est effectuée pour fournir une sécurité à deux facteurs.
    
        Voici un exemple de création d'un utilisateur.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration** : vous pouvez modifier d'autres paramètres du serveur si nécessaire.
    
        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Exportez la configuration du client.

    Cliquez sur **Export Client Configuration** en bas de l'onglet Configuration (ou appliquez la configuration modifiée), puis une fenêtre s'affichera comme ci-dessous.

    ![openvpn export config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_export_config.png){class="glboxshadow"}

    - Si l'adresse IP publique de votre réseau change fréquemment, vous pouvez activer [DDNS](ddns.md) afin d'utiliser le domaine DDNS comme adresse du serveur.

    - Depuis le firmware v4.8, vous pouvez choisir l'adresse du serveur parmi l'IP publique, le domaine DDNS et l'IP WAN actuelle. Une fois cette option modifiée, l'adresse du serveur dans le fichier de configuration est mise à jour simultanément. 
    
    Cliquez ensuite sur **Download** pour exporter la configuration.

4. Démarrez le serveur OpenVPN.

    Cliquez sur le bouton **Start** dans l'angle supérieur droit de la page OpenVPN Server pour démarrer le serveur. Accédez ensuite à la page VPN Dashboard pour vérifier son état et les autres paramètres.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Vérifier que le serveur OpenVPN fonctionne correctement

### Vérifier l'état du serveur

Depuis le firmware v4.8, vous pouvez vérifier l'état de la connexion du serveur sur la page **OpenVPN Server**. 

S'il affiche des statistiques de trafic montant/descendant, cela signifie que le serveur OpenVPN est en cours d'exécution.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

Pour le firmware v4.7 et les versions antérieures, veuillez vérifier l'état de la connexion du serveur sur la page **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Vérifier l'IP du client

Pour vérifier que la connexion au serveur a réussi, importez la configuration OpenVPN précédemment exportée sur un appareil connecté à un autre réseau (et non au même réseau local que le serveur). Ouvrez ensuite un navigateur web et recherchez votre adresse IP et votre localisation. Si elles correspondent à l'adresse IP du serveur VPN (et non à celle de votre fournisseur d'accès Internet) ainsi qu'à sa localisation, la connexion VPN a réussi.

La méthode la plus simple consiste à utiliser un smartphone sur lequel l'[OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"} officielle est installée. Commencez par désactiver le Wi-Fi du smartphone et connectez-le à Internet uniquement via les données cellulaires (4G/5G). Ouvrez ensuite l'application OpenVPN, importez le fichier de configuration et lancez la connexion. Vérifiez que le smartphone peut accéder à Internet et que son adresse IP correspond à celle du serveur OpenVPN.

Lors de l'importation du fichier de configuration dans l'application OpenVPN, un message peut apparaître comme illustré ci-dessous. Cliquez sur **CONTINUE** pour poursuivre, car le certificat est déjà intégré au fichier de configuration.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Si la connexion échoue, voici plusieurs causes fréquentes :

* Le fournisseur d'accès Internet ne vous attribue pas d'adresse IP publique. Veuillez vérifier [ici](#make-sure-you-have-a-public-ip-address).
* Vous devrez peut-être configurer la redirection de port. Veuillez vérifier [ici](#confirm-if-port-forwarding-is-required).
* Le port utilisé par le serveur OpenVPN est bloqué par votre fournisseur d'accès Internet. Changez de port ou contactez votre fournisseur d'accès Internet pour obtenir de l'aide.
* Certains pays/régions peuvent bloquer la connexion VPN.

## Server Options

Server Options regroupe des paramètres avancés côté serveur, notamment l’accès à distance au LAN du serveur et le masquage d’adresse IP. Configurez-les selon vos besoins.

Avec le micrologiciel v4.8 ou une version ultérieure, accédez à **OpenVPN Server**, puis cliquez sur **Options** dans l’angle supérieur droit.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options1.png){class="glboxshadow"}

Avec le micrologiciel v4.7 ou une version antérieure, accédez à **VPN Dashboard** -> **VPN Server**, puis cliquez sur l’icône en forme d’engrenage pour ouvrir OpenVPN Options.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options2.jpg){class="glboxshadow"}

La fenêtre contextuelle présente les fonctions suivantes.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet** : lorsque cette option est activée, les ressources du sous-réseau LAN du serveur sont accessibles via le tunnel VPN.

- **IP Masquerading** : lorsque cette option est activée, les adresses IP source des clients LAN sont remplacées par l’adresse IP du tunnel VPN du routeur. Désactivez-la uniquement dans les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

- **MTU** : abréviation de Maximum Transmission Unit. La valeur MTU définie pour le tunnel remplace celle du fichier de configuration.

## Client to Client

Client to Client est une fonction VPN côté serveur. Lorsqu’elle est activée, les clients VPN connectés peuvent communiquer entre eux au moyen de leurs adresses IP de tunnel VPN respectives.

La topologie réseau est la suivante.

![client-to-client topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Si nécessaire, procédez comme suit pour activer Client to Client sur votre serveur OpenVPN.

1. Sur la page **OpenVPN Server**, cliquez sur **Advanced Configuration** dans l’angle inférieur droit.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_config_advanced.png){class="glboxshadow"}

2. Activez **Client to Client**, puis cliquez sur **Apply**. Exportez ensuite une nouvelle configuration et importez-la sur vos clients OpenVPN.

    ![client to client](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/client-to-client.png){class="glboxshadow"}

**Conseil** : Client to Client annonce uniquement l’adresse IP de tunnel de chaque client. Les sous-réseaux LAN locaux situés derrière les différents clients VPN ne deviennent pas automatiquement accessibles. Pour permettre aux clients d’accéder aux sous-réseaux LAN des autres clients, ajoutez sur le serveur VPN des règles de routage qui annoncent ces sous-réseaux LAN distants.

## Installation de l'application OpenVPN

Veuillez télécharger l'OpenVPN App depuis le [site officiel d'OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
