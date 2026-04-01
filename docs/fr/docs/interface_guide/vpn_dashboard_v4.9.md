# Tableau de bord VPN (firmware v4.9)

**Remarque** : ce guide est basé sur le firmware v4.9. Pour les versions antérieures, veuillez consulter [cette page](vpn_dashboard.md).

---

Dans la partie gauche du panneau d'administration web, accédez à **VPN** -> **VPN Dashboard**.

Le tableau de bord VPN affiche les détails de connexion VPN, comme les règles de routage, le serveur connecté, les statistiques de trafic, l'IP virtuelle du client et le journal de connexion. Il permet également de configurer des paramètres avancés comme le Kill Switch VPN, le masquage IP et le MTU.

Par rapport au firmware v4.8, la version v4.9 apporte les améliorations suivantes au tableau de bord VPN :

1. **Permet aux utilisateurs de sélectionner plusieurs profils dans un groupe de tunnels et d'en définir la priorité**. Le tunnel tentera de se connecter en utilisant chaque profil selon l'ordre de priorité jusqu'à ce qu'une connexion soit établie avec succès.

2. **Chaque groupe de tunnels fonctionne indépendamment et n'effectue pas de basculement entre groupes**. Si tous les profils d'un même tunnel ne parviennent pas à se connecter, le système déterminera s'il doit basculer vers le WAN local selon l'état du Tunnel Kill Switch et du tunnel All Other Traffic.

## Premiers pas

Lors de votre première visite sur cette page, si aucun tunnel n'a encore été créé, elle s'affichera comme ci-dessous. Cliquez sur **Add VPN Tunnel** pour commencer.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Sélectionnez un fournisseur VPN**. Les fournisseurs VPN listés sont intégrés au panneau d'administration web des routeurs GL.iNet. Avec un abonnement actif, les utilisateurs n'ont qu'à saisir leurs identifiants pour se connecter immédiatement et obtenir les fichiers de configuration nécessaires aux connexions VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

Si vous êtes abonné à d'autres fournisseurs VPN, ou si vous souhaitez téléverser vos propres configurations VPN, accédez à **VPN Client Profile** pour effectuer une configuration manuelle.

Voici un exemple avec **Hide.me**. Connectez-vous avec vos identifiants Hide.me.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Sélectionnez un serveur VPN**. Il s'agit du serveur auquel vous vous connecterez via ce tunnel VPN, et votre adresse IP publique semblera provenir de l'emplacement du serveur sélectionné. Cliquez sur **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

La connexion s'établira automatiquement. Cliquez sur **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

Vous serez redirigé vers le tableau de bord VPN, où le VPN Tunnel 1 aura été activé et connecté.

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**Dans cet exemple, tous les clients connectés à ce routeur accéderont à Internet via ce tunnel VPN.**

Si vous souhaitez configurer une politique VPN, veuillez consulter [Politique VPN](#vpn-policy).

Le tunnel **All Other Traffic** est un tunnel préactivé affiché en bas du tableau de bord VPN. Cliquez [ici](#all-other-traffic) pour plus de détails.

## Détails du tunnel

Dans le tableau de bord VPN, chaque tunnel VPN individuel s'affiche comme ci-dessous, avec des informations détaillées telles que les règles de routage, le serveur connecté, les statistiques de trafic, l'adresse du serveur, le port d'écoute, l'IP virtuelle du client et le journal de connexion. Vous pouvez activer ou désactiver le tunnel VPN et configurer ses paramètres en haut du groupe de tunnels.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## Politique VPN {#vpn-policy}

Une politique VPN définit la manière dont le trafic réseau est acheminé via les tunnels VPN, en déterminant quel trafic va vers des destinations cibles via le VPN et quel trafic accède directement à Internet via le WAN local.

Elle permet à tous les clients ou à des appareils spécifiques d'accéder à des sites désignés ou à l'ensemble d'Internet via une connexion VPN, ce qui autorise une gestion réseau souple et sécurisée.

### Configuration rapide

Dans le tableau de bord VPN, cliquez sur **Add New Tunnel** ou sur la zone centrale d'un tunnel VPN existant.

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Suivez ensuite l'assistant de configuration pour définir votre politique VPN, notamment en sélectionnant le profil VPN, la source du trafic et la destination du trafic.

1. **Sélectionnez le profil VPN.**

    Si vous vous êtes connecté avec les identifiants d'un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser manuellement un fichier de configuration.

    Prenons [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} comme exemple. Connectez-vous avec vos identifiants de service ; vous verrez alors une liste de profils VPN. Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l'ordre de priorité jusqu'à ce qu'une connexion réussisse. Si tous les profils d'un même tunnel échouent, le système déterminera s'il doit basculer vers le WAN local en fonction de l'état du Tunnel Kill Switch et du tunnel [All Other Traffic](#all-other-traffic).

2. **Sélectionnez la source cliente.**

    Quatre options sont disponibles :

    - **All Clients** : si cette option est sélectionnée, le trafic de tous les appareils correspondra à cette règle.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types** : si cette option est sélectionnée, le trafic des types de connexion spécifiés (par ex. sous-réseau LAN, Drop-in Gateway, Guest Network) correspondra à cette règle.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) correspondra à cette règle.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par adresse MAC) ne correspondra pas à cette règle.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Sélectionnez la destination cible**.

    Trois options sont disponibles :

    - **All Targets** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers toutes les cibles.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle ne sera pas acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Scénarios d'utilisation

Voici deux scénarios illustrés étape par étape à titre de référence.

**Scénario 1**

**Objectifs** :

1. Seuls certains appareils connectés à ce routeur accèdent à Internet via le VPN. Tous les autres appareils accèdent à Internet via le WAN local.

2. Les appareils sélectionnés doivent utiliser uniquement la connexion VPN. Si le VPN se déconnecte de manière inattendue, l'accès Internet de ces appareils sera bloqué pour éviter les fuites DNS et le suivi IP.

**Suivez les étapes ci-dessous pour configurer la politique VPN.**

1. Sélectionnez le profil VPN.

    Si vous vous êtes connecté avec les identifiants d'un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser manuellement un fichier de configuration.

    Prenons [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} comme exemple. Connectez-vous avec vos identifiants de service ; vous verrez alors une liste de profils VPN.

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l'ordre de priorité jusqu'à ce qu'une connexion réussisse. Si tous les profils d'un même tunnel échouent, le système déterminera s'il doit basculer vers le WAN local en fonction de l'état du Tunnel Kill Switch et du tunnel [All Other Traffic](#all-other-traffic).

2. Sélectionnez **Specified Devices** comme source cliente, puis choisissez les appareils qui utiliseront le VPN et cliquez sur **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Sélectionnez **All Targets** comme destination cible, puis cliquez sur **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Vous serez redirigé vers le tableau de bord VPN, où un tunnel VPN aura été ajouté.

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Assurez-vous que le **Kill Switch** de ce tunnel est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet du trafic correspondant à ce tunnel sera bloqué afin d'éviter les fuites DNS et le suivi IP.

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}

6. Assurez-vous que **All Other Traffic** est activé et que le mode est défini sur **Allow Non-VPN Traffic**. Cela garantit que le trafic qui ne correspond pas aux tunnels VPN ci-dessus peut toujours accéder à Internet via le WAN local.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Activez l'interrupteur pour mettre ce tunnel en service.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Une fois connecté, la page affichera les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l'adresse du serveur, le port d'écoute et l'adresse IP virtuelle.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    Désormais, seuls les deux appareils spécifiés accèdent à Internet via le VPN. Si le VPN se déconnecte de manière inattendue, l'accès Internet de ces appareils sera bloqué afin d'éviter les fuites DNS et le suivi IP. Tous les autres appareils accéderont à Internet via le WAN local.

**Scénario 2**

**Objectifs** :

1. Tous les appareils utilisent **VPN Tunnel 1** lorsqu'ils accèdent à des domaines de certains réseaux sociaux et services de streaming, et utilisent **VPN Tunnel 2** pour tous les autres accès Internet.

2. Si les tunnels VPN se déconnectent de manière inattendue, l'accès Internet de tous les appareils sera bloqué afin d'éviter les fuites DNS et le suivi IP.

**Suivez les étapes ci-dessous pour configurer la politique VPN.**

1. Sélectionnez le profil VPN pour le Tunnel 1.

    Si vous vous êtes connecté avec les identifiants d'un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser manuellement un fichier de configuration.

    Prenons [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} comme exemple. Connectez-vous avec vos identifiants de service ; vous verrez alors une liste de profils VPN.

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}

    Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l'ordre de priorité jusqu'à ce qu'une connexion réussisse. Si tous les profils d'un même tunnel échouent, le système déterminera s'il doit basculer vers le WAN local en fonction de l'état du Tunnel Kill Switch et du tunnel [All Other Traffic](#all-other-traffic).

2. Sélectionnez **All Clients** comme source cliente pour le Tunnel 1, puis cliquez sur **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Sélectionnez **Specified Domain / IP List** comme destination cible pour le Tunnel 1. Saisissez les domaines de certains réseaux sociaux et services de streaming courants, comme illustré ci-dessous, puis cliquez sur **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. Vous serez redirigé vers le tableau de bord VPN, où le Tunnel 1 aura été ajouté.

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Assurez-vous que le **Kill Switch** du Tunnel 1 est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet du trafic correspondant à ce tunnel sera bloqué afin d'éviter les fuites DNS et le suivi IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}

6. Cliquez sur **Add New Tunnel** pour ajouter le Tunnel 2.

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Sélectionnez le profil VPN pour le Tunnel 2.

    Si vous vous êtes connecté avec les identifiants d'un service VPN intégré ou si vous avez téléversé un fichier de configuration, les profils disponibles seront listés ici. Sinon, accédez à **VPN Client Profile** pour vous connecter avec vos identifiants ou téléverser manuellement un fichier de configuration.

    Prenons [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} comme exemple. Connectez-vous avec vos identifiants de service ; vous verrez alors une liste de profils VPN.

    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}

    Sélectionnez un ou plusieurs profils, puis ajustez leur priorité à droite selon vos besoins.

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

    **Remarque** : lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter avec chaque profil selon l'ordre de priorité jusqu'à ce qu'une connexion réussisse. Si tous les profils d'un même tunnel échouent, le système déterminera s'il doit basculer vers le WAN local en fonction de l'état du Tunnel Kill Switch et du tunnel [All Other Traffic](#all-other-traffic).

8. Sélectionnez **All Clients** comme source cliente pour le Tunnel 2, puis cliquez sur **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Sélectionnez **All Targets** comme destination cible pour le Tunnel 2, puis cliquez sur **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. Vous serez redirigé vers le tableau de bord VPN, où le Tunnel 2 aura été ajouté.

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Assurez-vous que le **Kill Switch** du Tunnel 2 est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet du trafic correspondant à ce tunnel sera bloqué afin d'éviter les fuites DNS et le suivi IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Désactivez **All Other Traffic**. Assurez-vous que le mode est défini sur **Enhanced Kill Switch**. Cela garantit que tout le trafic doit accéder à Internet via le VPN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Activez l'interrupteur pour mettre en service le Tunnel 1 et le Tunnel 2.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Une fois connecté, la page affichera les détails de connexion VPN, notamment la politique VPN, les statistiques de trafic, l'adresse du serveur, le port d'écoute et l'adresse IP virtuelle.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Désormais, tous les appareils utiliseront **VPN Tunnel 1** lors de l'accès aux domaines spécifiés, et **VPN Tunnel 2** pour tous les autres accès Internet. Si les tunnels VPN se déconnectent de manière inattendue, l'accès Internet de tous les appareils sera bloqué afin d'éviter les fuites DNS et le suivi IP.

## Tout le reste du trafic {#all-other-traffic}

Cette option contrôle si le trafic qui ne correspond à aucun des groupes de tunnels VPN ci-dessus peut accéder à Internet. Elle est activée par défaut afin de garantir un accès Internet normal au trafic qui n'est pas acheminé via le VPN.

Lorsqu'elle est activée, le trafic non correspondant peut toujours accéder à Internet.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

Lorsqu'elle est désactivée, seul le trafic acheminé via le VPN est autorisé à accéder à Internet. Tout le trafic hors VPN, ainsi que le trafic basculé depuis des connexions VPN, sera bloqué. Cette option ne remplace pas le Kill Switch individuel de chaque tunnel VPN.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Priorité du tunnel

Pour ajuster la priorité du tunnel, cliquez sur l'icône d'engrenage dans un groupe de tunnels et sélectionnez **Sort**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Cliquez sur l'icône à trois lignes à droite et maintenez-la pour réorganiser les tunnels, puis cliquez sur **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Lorsque plusieurs tunnels sont activés, le routeur achemine le trafic selon les règles suivantes** :

1. Le trafic tente d'abord de correspondre à la règle du tunnel ayant la plus haute priorité. S'il correspond, il est acheminé via ce tunnel ; sinon, il essaie le tunnel de priorité suivante, et ainsi de suite.

2. Chaque groupe de tunnels fonctionne indépendamment. Une fois que le trafic correspond à une règle de tunnel, il est acheminé par ce tunnel et n'effectue pas de basculement entre groupes de tunnels.

3. Plusieurs profils peuvent être sélectionnés dans chaque groupe de tunnels afin d'activer un basculement interne au tunnel. Lorsque le profil de plus haute priorité d'un groupe devient indisponible, le tunnel se connecte automatiquement en utilisant le profil de priorité suivante, et ainsi de suite.

4. Si un tunnel VPN se déconnecte de manière inattendue, le système détermine si le trafic doit basculer vers le tunnel All Other Traffic selon que le **Kill Switch** de ce tunnel est activé ou non.

    - Si le Kill Switch est activé, le trafic sera bloqué et ne basculera pas vers le tunnel All Other Traffic.
    - Si le Kill Switch est désactivé, le trafic basculera vers le tunnel All Other Traffic.

5. Le tunnel **All Other Traffic** est activé par défaut pour garantir que le trafic qui ne correspond pas aux tunnels VPN puisse toujours accéder à Internet.

    - S'il est activé, il achemine le trafic non correspondant ou basculé via le WAN local.
    - S'il est désactivé, il renforce le Kill Switch et bloque l'accès Internet classique afin d'éviter les fuites d'IP.

## Options du tunnel

Vous pouvez configurer des paramètres avancés pour chaque tunnel VPN, tels que le Kill Switch VPN, le masquage IP et le MTU.

Cliquez sur l'icône d'engrenage dans un groupe de tunnels, puis sélectionnez **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch** : s'il est activé, le trafic correspondant à ce tunnel VPN sera bloqué si la connexion VPN échoue de manière inattendue. S'il est désactivé, ce trafic basculera vers le tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN** : si cette option est activée, les services GoodCloud, DDNS et rtty transmettront leurs paquets via les tunnels VPN. Cette option est désactivée par défaut, car ces services ont normalement besoin de la véritable adresse IP de l'appareil pour fonctionner correctement.

- **Allow Remote Access to the LAN Subnet** : si cette option est activée, l'accès à distance à ce routeur et à ses appareils LAN via le VPN sera autorisé. Cela nécessite que le serveur VPN annonce une route de retour vers son sous-réseau LAN.

- **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l'adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

- **MTU** : la valeur MTU que vous définissez pour le tunnel remplacera les paramètres MTU du fichier de configuration.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
