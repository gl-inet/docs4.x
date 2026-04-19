# Tableau de bord VPN (firmware v4.9)

Dans la partie gauche du panneau d’administration web, accédez à **VPN** -> **VPN Dashboard**.

Le tableau de bord VPN affiche les détails de connexion VPN, comme les règles de routage, le serveur connecté, les statistiques de trafic, l’IP virtuelle du client et le journal de connexion. Il permet également de configurer des paramètres avancés comme le Kill Switch VPN, le masquage IP et le MTU.

Par rapport au firmware v4.8, la version v4.9 apporte les améliorations suivantes au tableau de bord VPN :

1. **Les utilisateurs peuvent sélectionner plusieurs profils dans un groupe de tunnels et définir leur priorité**. Le tunnel tentera de se connecter en utilisant chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion soit établie avec succès.

2. **Chaque groupe de tunnels fonctionne indépendamment et n’effectue pas de basculement entre groupes**. Si tous les profils d’un même tunnel ne parviennent pas à se connecter, le système déterminera s’il doit basculer vers le WAN local selon l’état du Tunnel Kill Switch et du tunnel All Other Traffic.

## Premiers pas

### Importer un profil VPN

Lors de votre première visite sur cette page, si aucun tunnel n’a encore été créé, la page s’affichera comme ci-dessous. Cliquez sur **Add VPN Tunnel** pour commencer.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

Vous serez redirigé vers la page **VPN Client Profile**. Sélectionnez un fournisseur VPN et connectez-vous.

Les fournisseurs VPN listés sont intégrés au panneau d’administration web des routeurs GL.iNet. Avec un abonnement actif, les utilisateurs n’ont qu’à saisir leurs identifiants pour se connecter immédiatement et obtenir les fichiers de configuration nécessaires aux connexions VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

Si vous êtes abonné à d’autres fournisseurs VPN, ou si vous souhaitez téléverser vos propres configurations VPN, cliquez sur **Add Manually** et téléversez vos configurations.

Prenons **PureVPN** comme exemple. Cliquez sur PureVPN et connectez-vous avec des identifiants valides.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Vous obtiendrez une liste de profils VPN. Pour certains fournisseurs de services VPN, vous devrez peut-être d’abord sélectionner un protocole VPN ou des serveurs/villes préférés avant que la liste des profils n’apparaisse.

Cliquez ensuite sur **Go to Dashboard** en bas de la page. Vous serez redirigé vers le tableau de bord VPN afin d’ajouter votre tunnel VPN et de configurer la politique VPN.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

### Configurer la politique VPN

!!! note "Qu’est-ce qu’une politique VPN ?"

    Une politique VPN définit la manière dont le trafic réseau est acheminé via les tunnels VPN, en déterminant quel trafic va vers des destinations cibles via le VPN et quel trafic accède directement à Internet via le WAN local.

    Elle permet à tous les clients ou à des appareils spécifiques d’accéder à des sites désignés ou à l’ensemble d’Internet via une connexion VPN, ce qui autorise une gestion réseau souple et sécurisée.

Dans le tableau de bord VPN, suivez l’assistant de configuration pour définir votre politique VPN, notamment en sélectionnant le profil VPN, la source du trafic et la destination du trafic.

1. **Sélectionnez le profil VPN.**

    Si vous vous êtes déjà connecté avec les identifiants d’un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser un fichier de configuration manuellement.

    Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion réussisse. Si tous les profils d’un même tunnel échouent, le système déterminera s’il doit basculer vers le WAN local en fonction de l’état du Tunnel Kill Switch et de la politique [All Other Traffic](#all-other-traffic).

2. **Sélectionnez la source cliente.**

    Quatre options sont disponibles :

    - **All Clients** : si cette option est sélectionnée, le trafic de tous les appareils correspondra à cette règle.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types** : si cette option est sélectionnée, le trafic des types de connexion spécifiés (par ex. sous-réseau LAN, Drop-in Gateway, Guest Network) correspondra à cette règle.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) correspondra à cette règle.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) ne correspondra pas à cette règle.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **Sélectionnez la destination cible**.

    Trois options sont disponibles :

    - **All Targets** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers toutes les cibles.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle ne sera pas acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}


### Kill Switch

!!! note "Qu’est-ce que le Kill Switch ?"

    Le Kill Switch est une fonction de sécurité pour les connexions VPN. Il coupe automatiquement tout accès à Internet sur votre réseau local si la connexion VPN se déconnecte de manière inattendue, afin d’empêcher l’exposition de votre véritable adresse IP et de vos données en ligne, et de garantir une confidentialité et une sécurité continues. Cette fonction est particulièrement utile pour conserver un accès Internet sécurisé et anonyme, par exemple lors de l’utilisation de réseaux publics, du traitement de données sensibles ou lorsque vous souhaitez masquer votre véritable adresse IP.

    Lorsqu’il est activé, il bloque tout trafic client qui tente de contourner le tunnel VPN, ce qui empêche efficacement les fuites VPN causées par des problèmes de configuration DNS, des déconnexions inattendues, des requêtes IP directes et d’autres scénarios similaires.

Depuis le firmware v4.8, les routeurs GL.iNet prennent en charge la configuration d’un Kill Switch pour chaque tunnel VPN individuel, ainsi que pour la connexion VPN globale.

- Pour configurer le Kill Switch de chaque tunnel VPN individuel, consultez [cette section](#tunnel-options).

- Pour configurer le Kill Switch de la connexion VPN globale (c’est-à-dire **Enhanced Kill Switch**), consultez [cette section](#all-other-traffic).

## Scénarios d’utilisation

Voici deux scénarios avec instructions de configuration pas à pas à titre de référence.

### Scénario 1

**Objectifs** :

1. Seuls certains appareils connectés à ce routeur accèdent à Internet via le VPN. Tous les autres appareils accèdent à Internet via le WAN local.

2. Les appareils sélectionnés doivent utiliser uniquement la connexion VPN. Si le VPN se déconnecte de manière inattendue, l’accès Internet de ces appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

**Suivez les étapes ci-dessous pour configurer la politique VPN.**

1. Sélectionnez le profil VPN.

    Si vous vous êtes connecté avec les identifiants d’un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser un fichier de configuration manuellement.

    Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![scenario 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion réussisse. Si tous les profils d’un même tunnel échouent, le système déterminera s’il doit basculer vers le WAN local en fonction de l’état du Tunnel Kill Switch et de la politique [All Other Traffic](#all-other-traffic).

2. Sélectionnez la source cliente.

    Cliquez sur l’onglet **Specified Devices**, sélectionnez les appareils qui utiliseront le VPN, puis cliquez sur **Apply**.

    ![scenario 1 select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. Sélectionnez la destination cible.

    Cliquez sur l’onglet **All Targets**, définissez-le comme destination du trafic, puis cliquez sur **Apply**.

    ![scenario 1 select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

4. Vous serez redirigé vers le tableau de bord VPN, où un tunnel VPN aura été ajouté.

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. Assurez-vous que le **Kill Switch** de ce tunnel est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

6. Assurez-vous que **Allow Non-VPN Traffic** est activé. Cette option est activée par défaut afin de garantir que le trafic ne correspondant pas au tunnel VPN puisse toujours accéder à Internet via le WAN local.

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. Cliquez sur le bouton central pour activer ce tunnel.

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. Une fois connecté, la page affichera les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l’adresse du serveur, le port d’écoute et l’adresse IP virtuelle.

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    Désormais, seuls les deux appareils spécifiés accèdent à Internet via le VPN. Si le VPN se déconnecte de manière inattendue, l’accès Internet de ces appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP. Tous les autres appareils accéderont à Internet via le WAN local.

### Scénario 2

**Objectifs** :

1. Tous les appareils utilisent **VPN Tunnel 1** lorsqu’ils accèdent aux domaines de certains réseaux sociaux et services de streaming, et utilisent **VPN Tunnel 2** pour tous les autres accès Internet.

2. Si les tunnels VPN se déconnectent de manière inattendue, l’accès Internet de tous les appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

**Suivez les étapes ci-dessous pour configurer la politique VPN.**

1. Sélectionnez le profil VPN pour le Tunnel 1.

    Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![scenario 2 select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion réussisse. Si tous les profils d’un même tunnel échouent, le système déterminera s’il doit basculer vers le WAN local en fonction de l’état du Tunnel Kill Switch et de la politique [All Other Traffic](#all-other-traffic).

2. Sélectionnez la source cliente.

    Cliquez sur l’onglet **All Clients**, définissez-le comme source cliente pour le Tunnel 1, puis cliquez sur **Apply**.

    ![scenario 2 select source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

3. Sélectionnez la destination cible.

    Cliquez sur l’onglet **Specified Domain / IP List**, saisissez les domaines de certains réseaux sociaux et services de streaming courants, comme illustré ci-dessous, puis cliquez sur **Apply**.

    ![scenario 2 select target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. Vous serez redirigé vers le tableau de bord VPN, où le Tunnel 1 aura été ajouté.

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Assurez-vous que le **Kill Switch** du Tunnel 1 est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

6. Cliquez sur **Add New Tunnel** pour ajouter le Tunnel 2.

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Sélectionnez le profil VPN pour le Tunnel 2.

    Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![scenario 2 select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l’ordre de priorité jusqu’à ce qu’une connexion réussisse. Si tous les profils d’un même tunnel échouent, le système déterminera s’il doit basculer vers le WAN local en fonction de l’état du Tunnel Kill Switch et de la politique [All Other Traffic](#all-other-traffic).

8. Sélectionnez la source cliente.

    Cliquez sur l’onglet **All Clients**, définissez-le comme source cliente pour le Tunnel 2, puis cliquez sur **Apply**.

    ![scenario 2 select source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Sélectionnez la destination cible.

    Cliquez sur l’onglet **All Targets**, définissez-le comme destination du trafic pour le Tunnel 2, puis cliquez sur **Apply**.

    ![scenario 2 select target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. Vous serez redirigé vers le tableau de bord VPN, où le Tunnel 2 aura été ajouté.

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Assurez-vous que le **Kill Switch** du Tunnel 2 est activé. Si le VPN se déconnecte de manière inattendue, l’accès Internet du trafic correspondant à ce tunnel sera bloqué afin d’éviter les fuites DNS et le suivi IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. Cliquez sur l’icône d’engrenage en haut à droite et activez **Enhanced Kill Switch**. Cela garantit que tout le trafic doit accéder à Internet via le VPN.

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. Cliquez sur le bouton central pour activer le Tunnel 1 et le Tunnel 2.

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. Une fois connecté, la page affichera les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l’adresse du serveur, le port d’écoute et l’adresse IP virtuelle.

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    Désormais, tous les appareils utiliseront **VPN Tunnel 1** lorsqu’ils accèdent aux domaines spécifiés, et **VPN Tunnel 2** pour tous les autres accès Internet. Si les tunnels VPN se déconnectent de manière inattendue, l’accès Internet de tous les appareils sera bloqué afin d’éviter les fuites DNS et le suivi IP.

## Tout le reste du trafic {#all-other-traffic}

Cliquez sur l’icône d’engrenage en haut à droite pour définir la politique du trafic qui ne correspond à aucun tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Cette politique contrôle si le trafic qui ne correspond à aucun de vos groupes de tunnels VPN peut accéder à Internet ou non. Elle comporte deux options : **Allow Non-VPN Traffic** et **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic** : activé par défaut afin de garantir un accès Internet normal au trafic hors VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch** : force tous les appareils à accéder à Internet via un VPN. Tout trafic ne correspondant pas à un tunnel VPN sera bloqué. Ce paramètre global ne remplace pas le Kill Switch configuré pour chaque tunnel VPN individuellement.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Priorité du tunnel

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

## Options du tunnel

Vous pouvez configurer des paramètres avancés pour chaque tunnel VPN, tels que le Kill Switch VPN, le masquage IP et le MTU.

Cliquez sur l’icône d’engrenage dans un groupe de tunnels, puis sélectionnez **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch** : s’il est activé, le trafic correspondant à ce tunnel VPN sera bloqué si la connexion VPN échoue de manière inattendue. S’il est désactivé, ce trafic basculera vers le tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN** : si cette option est activée, les services GoodCloud, DDNS et rtty transmettront leurs paquets via les tunnels VPN. Cette option est désactivée par défaut, car ces services ont normalement besoin de la véritable adresse IP de l’appareil pour fonctionner correctement.

- **Allow Remote Access to the LAN Subnet** : si cette option est activée, l’accès à distance à ce routeur et à ses appareils LAN via le VPN sera autorisé. Cela nécessite que le serveur VPN annonce une route de retour vers son sous-réseau LAN.

- **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l’adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

- **MTU** : la valeur MTU que vous définissez pour le tunnel remplacera les paramètres MTU du fichier de configuration.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
