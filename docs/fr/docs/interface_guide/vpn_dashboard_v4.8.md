# Tableau de bord VPN (firmware v4.8)

Dans la partie gauche du panneau d'administration web, accédez à **VPN** -> **VPN Dashboard**.

Le tableau de bord VPN affiche les détails de connexion VPN, tels que les règles de tunnel, l'adresse du serveur, les statistiques de trafic, l'IP virtuelle du client et le journal de connexion. Il permet également de configurer des paramètres avancés comme le Kill Switch VPN, le masquage IP et le MTU.

Vous pouvez également activer plusieurs connexions VPN pour les scénarios à tunnels multiples.

## Assistant de configuration {#vpn-setup-wizard}

Cliquez sur l'icône de livre en haut à gauche et suivez l'assistant de configuration VPN pour terminer rapidement la configuration.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Remarque** : l'assistant de configuration VPN est uniquement disponible pour les services VPN intégrés, notamment AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA et Surfshark. Pour les autres services VPN, ignorez l'assistant et accédez à [OpenVPN Client](openvpn_client.md){target="_blank"} ou [WireGuard Client](wireguard_client.md){target="_blank"} afin de configurer le VPN manuellement.

Voici un exemple avec **Hide.me**. Connectez-vous avec vos identifiants Hide.me.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Sélectionnez un serveur VPN et cliquez sur **Apply**. Il s'agit du serveur auquel vous vous connecterez via ce tunnel VPN, et votre adresse IP publique semblera provenir de l'emplacement du serveur sélectionné.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

La connexion s'établira automatiquement. Une fois connecté avec succès, accédez au tableau de bord VPN et vous verrez qu'un tunnel VPN a été activé.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Le tableau affiche le protocole VPN utilisé (par exemple WireGuard), le fichier de configuration, l'adresse du serveur, le port d'écoute du serveur, les statistiques de trafic et l'IP virtuelle du client. Les utilisateurs peuvent consulter le journal de connexion dans la partie inférieure droite.

Tous les clients connectés accéderont à Internet via ce tunnel VPN.

Si vous souhaitez configurer une politique VPN, veuillez consulter [Policy Mode](#policy-mode).

## Mode VPN

Dans le tableau de bord VPN, cliquez sur le bouton situé en haut à droite pour changer de mode VPN.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Deux modes sont disponibles : **Global Mode** et **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Mode global

Dans ce mode, tout le trafic est acheminé via le tunnel VPN, et une seule instance cliente VPN peut être activée.

Il est idéal pour les scénarios où tout le trafic client doit passer par un seul serveur VPN, par exemple pour une sécurité réseau unifiée ou l'accès à des contenus spécifiques à une région.

Dans l'exemple ci-dessous, le routeur se connecte à un serveur australien via le protocole WireGuard. Tout le trafic des clients connectés sera acheminé via ce tunnel VPN.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### Mode de stratégie {#policy-mode}

Dans ce mode, le routeur peut se connecter à plusieurs serveurs VPN, et vous pouvez personnaliser les règles de routage pour différents clients ou différentes destinations de trafic.

Il convient aux scénarios nécessitant une gestion flexible du trafic, par exemple lorsque différents flux doivent être envoyés vers différentes destinations via plusieurs serveurs VPN.

Basculez le mode VPN sur **Policy Mode**, puis cliquez sur **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Après le basculement, si le VPN n'est pas activé, la page s'affiche comme ci-dessous et comprend trois sections : Primary Tunnel, Add Tunnel et All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Cliquez sur la section correspondante pour en savoir plus.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Tunnel principal {#primary-tunnel}

Le tunnel principal est un tunnel <u>prédéfini</u> en mode de stratégie. Il a la priorité la plus élevée, et vous pouvez modifier la [priorité du tunnel](#tunnel-priority) s'il existe plusieurs tunnels.

Dans ce tunnel, vous pouvez personnaliser la règle de tunnel en définissant trois facteurs :

1. **From** : il s'agit de la source du trafic, c'est-à-dire du trafic qui doit être acheminé via ce tunnel.

    Cliquez sur la zone grisée pour sélectionner la source du trafic.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients** : si cette option est sélectionnée, le trafic de tous les appareils correspondra à cette règle.

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types** : si cette option est sélectionnée, le trafic des types de connexion spécifiés (par ex. sous-réseau LAN, Drop-in Gateway, Guest Network) correspondra à cette règle.

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Si vous avez activé le serveur OpenVPN ou le serveur WireGuard sur ce routeur, davantage d'options apparaîtront dans Specified Connection Types. C'est utile pour le [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par leur adresse MAC) correspondra à cette règle.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par leur adresse MAC) **ne** correspondra **pas** à cette règle.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To** : il s'agit des destinations du trafic.

    Cliquez sur la zone grisée pour sélectionner les destinations du trafic.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers toutes les cibles.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.

        Veuillez noter que si vous spécifiez un <u>domaine racine</u>, tous ses sous-domaines seront également inclus. Par exemple, si vous souhaitez spécifier `archive.ubuntu.com`, `security.ubuntu.com` et `old-releases.ubuntu.com` dans un tunnel, il suffit de spécifier le domaine racine `ubuntu.com`.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Ou basculez le **Input Mode** de Manual vers Subscription URL, puis saisissez l'URL.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - La spécification d’un domaine racine couvre tous ses sous-domaines.

            - Si vous sélectionnez Subscribe URL, le nom de domaine ou l'adresse IP contenus dans l'URL sont mis à jour automatiquement chaque jour.

            - Assurez-vous de saisir une URL correcte. La détection d'URL vérifiera la validité du nom de domaine ou de l'adresse IP. [En savoir plus](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle **ne** sera **pas** acheminé vers les noms de domaine ou adresses IP spécifiés. Vous devez les saisir manuellement.

        Veuillez noter que si vous spécifiez un <u>domaine racine</u>, tous ses sous-domaines seront également inclus. Par exemple, si vous souhaitez spécifier `archive.ubuntu.com`, `security.ubuntu.com` et `old-releases.ubuntu.com` dans un tunnel, il suffit de spécifier le domaine racine `ubuntu.com`.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Ou basculez le **Input Mode** de Manual vers Subscription URL, puis saisissez l'URL.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - La spécification d’un domaine racine couvre tous ses sous-domaines.

            - Si vous sélectionnez Subscribe URL, le nom de domaine ou l'adresse IP contenus dans l'URL sont mis à jour automatiquement chaque jour.

            - Assurez-vous de saisir une URL correcte. La détection d'URL vérifiera la validité du nom de domaine ou de l'adresse IP. [En savoir plus](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via** : il s'agit de la méthode de routage du trafic, c'est-à-dire de l'utilisation ou non du VPN.

    Cliquez sur la zone grisée pour sélectionner la méthode de routage.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les destinations sélectionnées via le VPN.

        Pour commencer, vous devez configurer votre routeur comme client VPN. Utilisez le [VPN Setup Wizard](#vpn-setup-wizard) pour terminer rapidement la configuration, ou accédez à OpenVPN Client / WireGuard Client dans la barre latérale gauche pour configurer manuellement.

        Une fois le routeur configuré comme client VPN, sélectionnez un fichier de configuration VPN pour ce tunnel, puis cliquez sur **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers les destinations sélectionnées via le WAN local au lieu du VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Après avoir sélectionné la source du trafic, la destination et la méthode de routage, la configuration de la règle du tunnel principal est terminée.

Dans l'exemple ci-dessous, la règle du tunnel principal est la suivante : tous les clients utilisent le VPN pour accéder à des domaines spécifiés. Leur trafic est acheminé via le serveur australien et sort vers les domaines Internet sélectionnés par ce tunnel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Remarque** : pour des raisons de sécurité, veuillez accéder à [All Other Traffic](#all-other-traffic) et [Tunnel Options](#tunnel-options) afin de vérifier les autres paramètres avant d'activer les tunnels.

#### Ajouter un tunnel {#add-tunnel}

Pour créer des tunnels supplémentaires pour plusieurs instances VPN, cliquez sur **Add Tunnel** sous le tunnel principal, puis configurez des règles personnalisées.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Donnez un nom au tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Un tunnel supplémentaire apparaîtra alors sur le tableau de bord VPN.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Vous pouvez ajouter davantage de tunnels si nécessaire. Jusqu'à 5 tunnels peuvent être créés (y compris le tunnel principal prédéfini).

Personnalisez les règles de tunnel en définissant la source du trafic, les destinations et la méthode de routage. Veuillez vous reporter à [Primary Tunnel](#primary-tunnel).

**Remarque** : pour des raisons de sécurité, veuillez accéder à [All Other Traffic](#all-other-traffic) et [Tunnel Options](#tunnel-options) afin de vérifier les autres paramètres avant d'activer les tunnels.

#### Tout le reste du trafic {#all-other-traffic}

En mode de stratégie, un tunnel <u>préactivé</u> s'affiche en bas du tableau de bord VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Ce tunnel contrôle si le trafic qui ne correspond à aucun des groupes de tunnels VPN ci-dessus peut accéder à Internet. Il est activé par défaut pour garantir un accès Internet normal au trafic qui n'est pas acheminé via le VPN.

- Lorsqu'il est activé, le trafic non correspondant peut toujours accéder à Internet.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Lorsqu'il est désactivé, seul le trafic acheminé via le VPN est autorisé à accéder à Internet. Tout le trafic hors VPN, ainsi que le trafic basculé depuis des connexions VPN, seront bloqués. Cette option ne remplace pas le Kill Switch individuel de chaque tunnel VPN.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Priorité du tunnel {#tunnel-priority}

Par défaut, le tunnel principal prédéfini a la priorité la plus élevée, suivi des autres tunnels ajoutés manuellement (le cas échéant), puis du tunnel All Other Traffic afin de garantir la connectivité réseau locale (via le WAN local).

Pour modifier la priorité du tunnel, cliquez sur **Modify Priority** dans la barre d'information supérieure, ou cliquez sur le **libellé de priorité** en haut à gauche d'un tunnel (par exemple Priority 1 / Priority 2).

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Cliquez sur l'icône à trois lignes à droite et maintenez-la pour réorganiser les tunnels, puis cliquez sur **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Lorsque plusieurs tunnels sont activés, le routeur achemine le trafic dans l'ordre suivant** :

1. Le trafic tente d'abord de correspondre à la règle du tunnel ayant la plus haute priorité. S'il correspond, il est acheminé par ce tunnel ; sinon, il tente le tunnel de priorité suivante, et ainsi de suite, jusqu'à correspondre au tunnel "All Other Traffic".

2. Si un tunnel VPN se déconnecte de manière inattendue, le système détermine si le trafic doit basculer vers le tunnel de priorité suivante selon que le **Kill Switch** de ce tunnel est activé ou non.

    - Si le Kill Switch est activé, le trafic sera bloqué et ne basculera pas vers le tunnel suivant.
    - Si le Kill Switch est désactivé, le trafic basculera vers le tunnel suivant et tentera de correspondre à ses règles de tunnel.

3. Le tunnel **All Other Traffic** est activé par défaut afin de garantir que le trafic ne correspondant pas aux tunnels VPN puisse toujours accéder à Internet.

    - S'il est activé, il achemine le trafic non correspondant ou basculé via le WAN local.
    - S'il est désactivé, il renforce le Kill Switch et bloque l'accès Internet classique pour éviter les fuites d'IP.

#### Options du tunnel {#tunnel-options}

Vous pouvez configurer des paramètres avancés pour chaque tunnel VPN, tels que le Kill Switch VPN, le masquage IP et le MTU.

Cliquez sur l'icône d'engrenage à côté du nom d'un tunnel, puis sélectionnez **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch** : s'il est activé, le trafic correspondant à ce tunnel VPN sera bloqué si la connexion VPN échoue de manière inattendue. S'il est désactivé, ce trafic basculera vers le tunnel de priorité suivante ou vers le WAN local.

- **Services from GL.iNet Use VPN** : si cette option est activée, les services GoodCloud, DDNS et rtty transmettront leurs paquets via les tunnels VPN. Cette option est désactivée par défaut, car ces services ont normalement besoin de la véritable adresse IP de l'appareil pour fonctionner correctement.

- **Allow Remote Access the LAN Subnet** : si cette option est activée, l'accès à distance à ce routeur et à ses appareils LAN via le VPN sera autorisé. Cela nécessite que le serveur VPN annonce une route de retour vers son sous-réseau LAN.

- **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l'adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

- **MTU** : la valeur MTU que vous définissez pour le tunnel remplacera les paramètres MTU du fichier de configuration.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
