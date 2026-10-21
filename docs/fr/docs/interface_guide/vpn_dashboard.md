# VPN Dashboard {#vpn-dashboard}

Le contenu de cette page est basé sur la version de firmware v4.9.x et versions ultérieures. Si votre appareil utilise une autre version de firmware, utilisez le sélecteur ci-dessous pour passer au guide correspondant.

<div class="gl-link-select" data-label="Version du firmware" data-placeholder="Firmware v4.9 et versions ultérieures" markdown="1">

- [Firmware v4.7 et versions antérieures](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

Dans la partie gauche du panneau d’administration web, accédez à **VPN** -> **VPN Dashboard**.

Le tableau de bord VPN affiche les détails de connexion VPN, comme les règles de routage, le serveur connecté, les statistiques de trafic, l’IP virtuelle du client et le journal de connexion. Il permet également de configurer des paramètres avancés comme le Kill Switch VPN, le masquage IP et le MTU.

Par rapport au firmware v4.8, la version v4.9 apporte les améliorations suivantes au tableau de bord VPN :

1. **Les utilisateurs peuvent sélectionner plusieurs profils dans un groupe de tunnels et définir leur priorité**. Le tunnel tentera de se connecter en utilisant chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion soit établie avec succès.

2. **Chaque groupe de tunnels fonctionne indépendamment et n’effectue pas de basculement entre groupes**. Si tous les profils d’un même tunnel ne parviennent pas à se connecter, le système déterminera s’il doit basculer vers le WAN local selon l’état du Kill Switch du tunnel et du tunnel All Other Traffic.

## Importer un profil VPN {#upload-vpn-profile}

Lors de votre première visite sur cette page, si aucun tunnel n’a encore été créé, la page s’affiche comme ci-dessous. Cliquez sur **Add VPN Tunnel** pour commencer.

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Vous serez redirigé vers la page **VPN Client Profile**. Sélectionnez un fournisseur VPN et connectez-vous.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. Les fournisseurs VPN présentés dans l’image ci-dessus sont intégrés au panneau d’administration web des routeurs GL.iNet. Avec un abonnement actif, les utilisateurs n’ont qu’à saisir leurs identifiants pour se connecter immédiatement et obtenir les fichiers de configuration nécessaires aux connexions VPN.
    
    2. Si vous êtes abonné à d’autres fournisseurs VPN, ou si vous souhaitez téléverser vos propres configurations VPN, cliquez sur **Add Manually** et téléversez vos configurations.

Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Cliquez sur PureVPN et connectez-vous avec des identifiants valides.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Vous obtiendrez une liste de profils VPN. Pour certains fournisseurs de services VPN, vous devrez peut-être d’abord sélectionner un protocole VPN ou des serveurs/villes préférés avant que la liste des profils n’apparaisse.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Cliquez sur **Go to Dashboard** en bas de la page. Vous serez redirigé vers le tableau de bord VPN afin d’ajouter votre tunnel VPN et de configurer les politiques VPN.

## Ajouter un tunnel VPN {#add-vpn-tunnel}

### Étapes générales {#general-steps}

Suivez les étapes ci-dessous pour ajouter votre tunnel VPN et configurer les politiques VPN. Consultez au besoin la section [Cas de référence](#case-reference).

1. Dans le tableau de bord VPN, cliquez sur **Add VPN Tunnel**. Un assistant de configuration VPN s’ouvre à droite.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Sélectionnez le profil VPN.

    Sélectionnez un ou plusieurs profils, ajustez leur priorité à droite selon vos besoins, puis cliquez sur **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion soit établie avec succès. Si tous les profils d’un même tunnel ne parviennent pas à se connecter, le système déterminera s’il doit basculer vers le WAN local du routeur en fonction de l’état du Kill Switch dans les paramètres [Options du tunnel](#tunnel-options) et [All Other Traffic](#all-other-traffic).

3. Sélectionnez la source cliente, puis cliquez sur **Next**.

    Quatre options sont disponibles :

    - **All Clients** : si cette option est sélectionnée, le trafic de tous les appareils correspondra à cette règle.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types** : si cette option est sélectionnée, le trafic des types de connexion spécifiés (par ex. sous-réseau LAN, Drop-in Gateway, Guest Network) correspondra à cette règle.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) correspondra à cette règle.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) ne correspondra pas à cette règle.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Sélectionnez la destination cible, puis cliquez sur **Apply**.

    Trois options sont disponibles :

    - **All Targets** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers toutes les cibles.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle ne sera pas acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Le tunnel VPN a été ajouté avec succès. Vous serez redirigé vers le **VPN Dashboard**. Ajoutez d’autres tunnels VPN si nécessaire.

    Pour des raisons de sécurité, consultez les sections [All Other Traffic](#all-other-traffic) et [Options du tunnel](#tunnel-options) afin de vérifier l’état du **Kill Switch** avant d’activer votre tunnel VPN.

### Cas de référence {#case-reference}

Voici deux cas typiques de configuration de politiques VPN, avec des instructions pas à pas à titre de référence.

??? note "Cas 1 : acheminer uniquement certains appareils via le VPN."

    **Exigences :**

    1. Seuls certains appareils connectés à ce routeur accèdent à Internet via le VPN. Tous les autres appareils accèdent à Internet via le WAN local.

    2. Les appareils sélectionnés doivent utiliser uniquement la connexion VPN. Si le VPN se déconnecte de manière inattendue, l’accès Internet de ces appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

    **Étapes de configuration :**

    1. Sélectionnez le profil VPN.

        Si vous vous êtes connecté avec les identifiants d’un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser un fichier de configuration manuellement.

        Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Sélectionnez la source cliente.

        Cliquez sur l’onglet **Specified Devices**, sélectionnez les appareils qui utiliseront le VPN, puis cliquez sur **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Sélectionnez la destination cible.

        Cliquez sur l’onglet **All Targets**, définissez-le comme destination du trafic, puis cliquez sur **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Vous serez redirigé vers le tableau de bord VPN. Un tunnel VPN a maintenant été ajouté avec succès, comme illustré ci-dessous.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Assurez-vous que le **Kill Switch** de ce tunnel est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}
        
    6. Assurez-vous que **Allow Non-VPN Traffic** est activé. Cette option est activée par défaut afin de garantir que le trafic ne correspondant pas au tunnel VPN puisse toujours accéder à Internet via le WAN local.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Cliquez sur le bouton central pour activer ce tunnel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Une fois la connexion établie, la page affiche les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l’adresse du serveur, le port d’écoute et l’adresse IP virtuelle.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Désormais, seuls les deux appareils spécifiés accèdent à Internet via le VPN. Si le VPN se déconnecte de manière inattendue, l’accès Internet de ces appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP. Tous les autres appareils accéderont à Internet via le WAN local.

??? note "Cas 2 : acheminer tous les appareils via le VPN 1 pour certains sites web, et tout le reste du trafic via le VPN 2."

    **Exigences :**

    1. Tous les appareils utilisent **VPN Tunnel 1** lorsqu’ils accèdent aux domaines de certains réseaux sociaux et services de streaming, et utilisent **VPN Tunnel 2** pour tous les autres accès Internet.

    2. Si les tunnels VPN se déconnectent de manière inattendue, l’accès Internet de tous les appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

    **Étapes de configuration :**

    1. Sélectionnez le profil VPN pour le Tunnel 1.

        Si vous vous êtes connecté avec les identifiants d’un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser un fichier de configuration manuellement.
        
        Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, ajustez leur priorité à droite selon vos besoins, puis cliquez sur **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Sélectionnez la source cliente.

        Cliquez sur l’onglet **All Clients**, définissez-le comme source cliente pour le Tunnel 1, puis cliquez sur **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Sélectionnez la destination cible.

        Cliquez sur l’onglet **Specified Domain / IP List**, saisissez les domaines de certains réseaux sociaux et services de streaming courants, comme illustré ci-dessous, puis cliquez sur **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Vous serez redirigé vers le tableau de bord VPN. Le tunnel VPN 1 a maintenant été ajouté avec succès.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Assurez-vous que le **Kill Switch** du Tunnel 1 est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}
        
    6. Cliquez sur **Add New Tunnel** pour ajouter le Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Sélectionnez le profil VPN pour le Tunnel 2.

        Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Sélectionnez la source cliente.

        Cliquez sur l’onglet **All Clients**, définissez-le comme source cliente pour le Tunnel 2, puis cliquez sur **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Sélectionnez la destination cible.

        Cliquez sur l’onglet **All Targets**, définissez-le comme destination du trafic pour le Tunnel 2, puis cliquez sur **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Vous serez redirigé vers le tableau de bord VPN. Le tunnel VPN 2 a maintenant été ajouté avec succès.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Assurez-vous que le **Kill Switch** du Tunnel 2 est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Cliquez sur l’icône d’engrenage en haut à droite et activez **Enhanced Kill Switch**. Cela garantit que tout le trafic doit accéder à Internet via le VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Cliquez sur le bouton central pour activer le Tunnel 1 et le Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Une fois la connexion établie, la page affiche les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l’adresse du serveur, le port d’écoute et l’adresse IP virtuelle.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Désormais, tous les appareils utiliseront **VPN Tunnel 1** lorsqu’ils accèdent aux domaines spécifiés, et **VPN Tunnel 2** pour tous les autres accès Internet. Si les tunnels VPN se déconnectent de manière inattendue, l’accès Internet de tous les appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

## Kill Switch {#kill-switch}

!!! Tip "Qu’est-ce que le Kill Switch ?"

    Le Kill Switch VPN aide à empêcher le trafic de basculer vers une connexion Internet non chiffrée lorsque la connexion VPN échoue.

    Pour un tunnel individuel, l’activation de **Kill Switch** bloque l’accès à Internet du trafic affecté à ce tunnel si sa connexion échoue. Le reste du trafic suit les paramètres **All Other Traffic**.

    **Enhanced Kill Switch** bloque le trafic Internet qui ne correspond à aucun tunnel VPN. Il ne remplace pas le paramètre **Kill Switch** propre à chaque tunnel.

Depuis le firmware v4.8, les routeurs GL.iNet prennent en charge la configuration d’un Kill Switch pour la connexion VPN globale, ainsi que pour chaque tunnel VPN individuel.

- Pour configurer le Kill Switch de la connexion VPN globale (c’est-à-dire **Enhanced Kill Switch**), consultez la section [Tout le reste du trafic](#all-other-traffic).

- Pour configurer le Kill Switch de chaque tunnel VPN individuel, consultez la section [Options du tunnel](#tunnel-options).

## Tout le reste du trafic {#all-other-traffic}

Cliquez sur l’icône d’engrenage en haut à droite pour définir la politique du trafic qui ne correspond à aucun tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Cette politique contrôle si le trafic qui ne correspond à aucun de vos groupes de tunnels VPN peut accéder à Internet ou non. Elle comporte deux options : **Allow Non-VPN Traffic** et **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic** : activé par défaut afin de garantir un accès Internet normal au trafic hors VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch** : force tous les appareils à accéder à Internet via un VPN. Tout trafic ne correspondant pas à un tunnel VPN sera bloqué. Ce paramètre global ne remplace pas le Kill Switch configuré pour chaque tunnel VPN individuellement.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Options du tunnel {#tunnel-options}

Vous pouvez configurer des paramètres avancés pour chaque tunnel VPN, tels que le Kill Switch VPN, le masquage IP et le MTU.

Cliquez sur l’icône d’engrenage dans un groupe de tunnels, puis sélectionnez **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch** : s’il est activé, le trafic correspondant à ce tunnel VPN sera bloqué si la connexion VPN échoue de manière inattendue. S’il est désactivé, ce trafic basculera vers le tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN** : si cette option est activée, les services GoodCloud, DDNS et rtty transmettront leurs paquets via les tunnels VPN. Cette option est désactivée par défaut, car ces services ont normalement besoin de la véritable adresse IP de l’appareil pour fonctionner correctement.

- **Allow Remote Access to the LAN Subnet** : si cette option est activée, l’accès à distance à ce routeur et à ses appareils LAN via le VPN sera autorisé. Cela nécessite que le serveur VPN annonce une route de retour vers son sous-réseau LAN.

- **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l’adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

    Comme illustré ci-dessous, lorsque le masquage IP est activé et que l’ordinateur portable (192.168.10.200) du LAN de voyage envoie du trafic à travers le tunnel vers le NAS domestique (192.168.8.100), le routeur de voyage remplace l’adresse IP source `192.168.10.200` par l’adresse du tunnel du client VPN, `10.1.0.2`. Le côté serveur voit ainsi le trafic comme provenant du client et non du LAN local du client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU** : la valeur MTU que vous définissez pour le tunnel remplacera les paramètres MTU du fichier de configuration.

## Priorité du tunnel {#tunnel-priority}

Pour ajuster la priorité des tunnels, cliquez sur l’icône d’engrenage d’un groupe de tunnels, puis sélectionnez **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Cliquez sur l’icône à trois lignes à droite et maintenez-la pour réorganiser les tunnels, puis cliquez sur **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Lorsque plusieurs tunnels sont activés, le routeur achemine le trafic selon les règles suivantes** :

1. Le trafic tente d’abord de correspondre à la règle du tunnel ayant la priorité la plus élevée. S’il correspond, il est acheminé via ce tunnel ; sinon, il essaie le tunnel de priorité suivante, et ainsi de suite.

2. Chaque groupe de tunnels fonctionne indépendamment. Une fois que le trafic correspond à une règle de tunnel, il est acheminé par ce tunnel et n’effectue pas de basculement entre groupes de tunnels.

3. Plusieurs profils peuvent être sélectionnés dans chaque groupe de tunnels afin d’activer un basculement interne au tunnel. Lorsque le profil de plus haute priorité d’un groupe devient indisponible, le tunnel se connecte automatiquement en utilisant le profil de priorité suivante, et ainsi de suite.

4. Si un tunnel VPN se déconnecte de manière inattendue, le système détermine si le trafic doit basculer vers le tunnel All Other Traffic selon que le **Kill Switch** de ce tunnel est activé ou non.

    - Si le Kill Switch est activé, le trafic sera bloqué et ne basculera pas vers le tunnel All Other Traffic.
    - Si le Kill Switch est désactivé, le trafic basculera vers le tunnel All Other Traffic.

5. Dans le tunnel **All Other Traffic**, différents modes déterminent si le trafic qui ne correspond pas à un tunnel VPN peut accéder à Internet.

    - **Allow Non-VPN Traffic** : activé par défaut afin de garantir que le trafic ne correspondant pas aux tunnels VPN puisse toujours accéder à Internet via le WAN local.

    - **Enhanced Kill Switch** : force tous les appareils à accéder à Internet via un VPN. Tout trafic ne correspondant pas à un tunnel VPN sera bloqué. Ce paramètre global ne remplace pas le Kill Switch configuré pour chaque tunnel VPN individuellement. En bref, il renforce le Kill Switch et bloque l’accès Internet classique afin d’éviter les fuites d’IP.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
