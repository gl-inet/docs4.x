# Guide d'activation d'ExpressVPN

**Remarque :** ce guide s'applique uniquement au routeur commercialisé conjointement par GL.iNet et ExpressVPN, **Fortify (GL-MT6000)**.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} est l'un des principaux services VPN premium au monde, conçu pour protéger votre confidentialité en ligne, sécuriser votre connexion Internet et permettre une diffusion sécurisée depuis n'importe où. Il offre des vitesses ultra-rapides, un cryptage de niveau militaire et un accès à des serveurs dans plus de 100 pays. Que vous souhaitiez diffuser du streaming, naviguer en privé ou protéger vos données sur un réseau Wi-Fi public, ExpressVPN vous offre une expérience rapide et sécurisée.

**Fortify (GL-MT6000)** est un routeur co-marqué publié conjointement par GL.iNet et ExpressVPN. Chaque unité est livrée avec un abonnement ExpressVPN gratuit d'un an. Les utilisateurs peuvent utiliser l'abonnement et connecter leurs comptes directement sur le panneau d'administration Web du routeur. Une fois activé, tout le trafic passant par le routeur exploitera le réseau haut débit d'ExpressVPN et le cryptage robuste pour protéger l'ensemble de votre connexion réseau et votre confidentialité en ligne.

Ce guide vous explique comment utiliser le forfait ExpressVPN de 12 mois dans le panneau d'administration Web du routeur. Il couvre également la personnalisation des politiques VPN en fonction de vos scénarios d'utilisation et de vos exigences, vous aidant ainsi à profiter sans effort d'une connectivité Internet cryptée, sécurisée et haut débit.

## Utiliser le forfait ExpressVPN

Connectez-vous au panneau d'administration Web de Fortify et accédez à **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Lisez et acceptez **Terms of Service** et **Privacy Policy**, puis cliquez sur **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Cliquez sur **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

Dans la fenêtre contextuelle, entrez votre **Order ID**. Si vous avez acheté ce routeur sur GL.iNet Store, **Order Email** est également requis. Cliquez ensuite sur **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

Vous serez dirigé vers la caisse ExpressVPN. Un code de remboursement a été appliqué sur le droit pour activer l'abonnement de 12 mois sans frais supplémentaires.

Entrez votre adresse e-mail en haut et ajoutez un mode de paiement pour garantir un accès VPN ininterrompu à la fin de la durée initiale. Cliquez ensuite sur **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Votre forfait a été activé. Revenez au panneau d'administration Web de votre routeur Fortify pour vous connecter avec votre compte.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Connectez-vous à ExpressVPN

Sur le panneau d'administration Web de votre Fortify, accédez à **VPN** -> **VPN Client Profile**.

Cliquez sur **Log in to ExpressVPN** et vous serez dirigé vers la page de connexion sécurisée d'ExpressVPN.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Entrez votre e-mail et cliquez sur **Send Code**. Un code de vérification à 6 chiffres sera envoyé à votre adresse e-mail.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Entrez le code de vérification et cliquez sur **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Changez votre mot de passe pour activer votre compte.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

À l'étape suivante, cliquez sur **Yes** pour autoriser l'accès à ExpressVPN sur votre routeur.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Connexion réussie. Vous pouvez fermer cette fenêtre de navigateur et revenir à votre appareil.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

Sur le panneau d'administration Web de votre Fortify, accédez à **VPN** -> **VPN Client Profile**.

Vous êtes connecté à ExpressVPN sur ce routeur. Cliquez sur **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Vous pouvez désormais ajouter des tunnels VPN et configurer des politiques VPN en fonction de vos besoins.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## Ajouter un tunnel VPN

### Étapes générales

Suivez les étapes ci-dessous pour ajouter votre tunnel VPN et configurer les politiques VPN. Voir [Référence de cas](#case-reference) si nécessaire.

1. Sur le panneau d'administration Web de votre Fortify, accédez à **VPN** -> **ExpressVPN Dashboard**. Cliquez sur **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Sélectionnez le profil VPN, puis cliquez sur **Next**.

    Vous obtiendrez une liste de profils ExpressVPN. Sélectionnez un ou plusieurs profils et ajustez leur priorité à droite si nécessaire.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        Lorsque plusieurs profils sont sélectionnés, le tunnel tentera de se connecter en utilisant chaque profil par ordre de priorité jusqu'à ce qu'une connexion soit établie avec succès. Si tous les profils d'un même tunnel ne parviennent pas à se connecter, le système déterminera s'il doit basculer vers le réseau local (WAN) du routeur en fonction de l'état du Kill Switch dans les paramètres [Options du tunnel](#tunnel-options) et [All Other Traffic](#all-other-traffic).

3. Sélectionnez la source client, puis cliquez sur **Next**.

    Il existe quatre options :

    - **All Clients** : si cette option est sélectionnée, le trafic de tous les appareils correspondra à cette règle.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types** : si cette option est sélectionnée, le trafic des types de connexion spécifiés (par exemple, sous-réseau LAN, passerelle d'accès direct, réseau invité) correspondra à cette règle.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par l'adresse MAC) correspondra à cette règle.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices** : si cette option est sélectionnée, le trafic des appareils spécifiés (identifiés par l'adresse MAC) ne correspondra pas à cette règle.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Sélectionnez la destination cible, puis cliquez sur **Apply**.

    Il existe trois options :

    - **All Targets** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers toutes les cibles.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle sera acheminé vers des domaines ou des adresses IP spécifiés. Vous devez les saisir manuellement.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List** : si cette option est sélectionnée, le trafic correspondant à cette règle ne sera pas acheminé vers les domaines ou les adresses IP spécifiés. Vous devez les saisir manuellement.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. Un tunnel VPN a été ajouté avec succès. Vous serez dirigé vers le **ExpressVPN Dashboard**. Ajoutez plus de tunnels VPN si nécessaire.

### Référence de cas {#case-reference}

Voici deux cas typiques de configuration de politique VPN avec des instructions de configuration étape par étape pour votre référence.

??? note "Cas 1 : acheminer uniquement les appareils spécifiés via le VPN."

    **Exigences :**

    1. Seuls les appareils spécifiques connectés à ce routeur accèdent à Internet via le VPN. Tous les autres appareils accèdent à Internet via le WAN local.

    2. Les appareils sélectionnés doivent utiliser uniquement la connexion VPN. Si le VPN se déconnecte de manière inattendue, l'accès Internet de ces appareils sera bloqué pour éviter les fuites DNS et le suivi IP.

    **Étapes de configuration :**

    1. Sélectionnez le profil VPN.

        Sélectionnez un ou plusieurs profils et ajustez leur priorité à droite si nécessaire, puis cliquez sur **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Sélectionnez la source du client.

        Cliquez sur l'onglet **Specified Devices**, sélectionnez les appareils sur lesquels vous souhaitez utiliser le VPN, puis cliquez sur **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Sélectionnez la destination cible.

        Cliquez sur l'onglet **All Targets**, définissez-le comme destination du trafic, puis cliquez sur **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

4. Vous serez dirigé vers le tableau de bord ExpressVPN. Un tunnel VPN a maintenant été ajouté avec succès.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Assurez-vous que le **Kill Switch** pour ce tunnel est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet pour le trafic correspondant à ce tunnel sera bloqué pour éviter les fuites DNS et le suivi IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Assurez-vous que le **Allow Non-VPN Traffic** est activé. Ceci est activé par défaut pour garantir que le trafic ne correspondant pas au tunnel VPN peut toujours accéder à Internet via le réseau WAN local.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Cliquez sur le bouton du milieu pour activer ce tunnel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Une fois connecté, la page affichera les détails de la connexion VPN, y compris la politique VPN, l'adresse IP virtuelle du client, l'adresse du serveur, le port d'écoute et les statistiques de trafic.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Désormais, seuls deux appareils spécifiés accèdent à Internet via VPN. Si le VPN se déconnecte de manière inattendue, l'accès Internet de ces appareils sera bloqué pour éviter les fuites DNS et le suivi IP. Tous les autres appareils accéderont à Internet via le réseau WAN local.

??? note "Cas 2 : acheminez tous les appareils via VPN 1 pour des sites Web spécifiques et acheminez tout le trafic restant via VPN 2."

    **Exigences :**

    1. Tous les appareils utilisent le tunnel VPN 1 lorsqu'ils accèdent à des sites Web de médias sociaux et de services de streaming spécifiques, et utilisent le tunnel VPN 2 pour tous les accès Internet restants.

    2. Si les tunnels VPN se déconnectent de manière inattendue, l'accès Internet de tous les appareils sera bloqué pour éviter les fuites DNS et le suivi IP.

    **Étapes de configuration :**

    1. Sélectionnez le profil VPN pour le tunnel 1.

        Sélectionnez un ou plusieurs profils et ajustez leur priorité à droite si nécessaire, puis cliquez sur **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Sélectionnez la source du client.

        Cliquez sur l'onglet **All Clients**, définissez-le comme source client pour le tunnel 1, puis cliquez sur **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Sélectionnez la destination cible.

        Cliquez sur l'onglet **Specified Domain / IP List**, entrez les domaines de médias sociaux et de services de streaming spécifiques, comme indiqué ci-dessous, puis cliquez sur **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. Vous serez dirigé vers le tableau de bord ExpressVPN. Le tunnel VPN 1 a maintenant été ajouté avec succès.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Assurez-vous que le **Kill Switch** pour le tunnel 1 est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet pour le trafic correspondant à ce tunnel sera bloqué pour éviter les fuites DNS et le suivi IP.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Cliquez sur **Add New Tunnel** pour ajouter le tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Sélectionnez le profil VPN pour le tunnel 2.

        Sélectionnez un ou plusieurs profils et ajustez leur priorité à droite si nécessaire, puis cliquez sur **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

    8. Sélectionnez la source du client.

        Cliquez sur l'onglet **All Clients**, définissez-le comme source client pour Tunnel 2, puis cliquez sur **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    9. Sélectionnez la destination cible.

        Cliquez sur l'onglet **All Targets**, définissez-le comme destination du trafic pour le tunnel 2, puis cliquez sur **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. Vous serez dirigé vers le tableau de bord VPN. Le tunnel VPN 2 a maintenant été ajouté avec succès.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Assurez-vous que le **Kill Switch** pour le tunnel 2 est activé. Si le VPN se déconnecte de manière inattendue, l'accès Internet pour le trafic correspondant à ce tunnel sera bloqué pour éviter les fuites DNS et le suivi IP.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Cliquez sur l'icône d'engrenage en haut à droite, activez **Enhanced Kill Switch**, puis cliquez sur **Apply**. Cela garantit que tout le trafic ne peut atteindre Internet que via VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        Une fois appliqué, **Enhanced Kill Switch** apparaîtra en haut de la page.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Cliquez sur le bouton du milieu pour activer Tunnel 1 et Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Une fois connecté, la page affichera les détails de la connexion VPN, y compris la politique VPN, l'adresse IP virtuelle du client, l'adresse du serveur, le port d'écoute et les statistiques de trafic.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Désormais, tous les appareils utiliseront **VPN Tunnel 1** pour accéder aux domaines spécifiés et utiliseront **VPN Tunnel 2** pour tous les accès Internet restants. Si les tunnels VPN se déconnectent de manière inattendue, l'accès Internet de tous les appareils sera bloqué pour éviter les fuites DNS et le suivi IP.

## Kill Switch

Kill Switch est une fonctionnalité de sécurité pour les connexions VPN. Il coupe automatiquement tout accès Internet à votre réseau local si la connexion VPN s'interrompt de manière inattendue, empêchant ainsi votre véritable adresse IP et vos données en ligne d'être exposées et garantissant une confidentialité et une sécurité continues. Cette fonctionnalité est particulièrement utile pour maintenir un accès Internet sécurisé et anonyme, par exemple lorsque vous utilisez des réseaux publics, traitez des données sensibles ou masquez votre véritable adresse IP.

Lorsqu'il est activé, il bloque tout trafic client qui tente de contourner le tunnel VPN, arrêtant ainsi efficacement les fuites VPN causées par des problèmes de configuration DNS, des déconnexions inattendues, des requêtes IP directes et d'autres scénarios similaires.

Fortify prend en charge la configuration Kill Switch pour la connexion VPN globale, ainsi que pour chaque tunnel VPN individuel.

- Pour configurer Kill Switch pour la connexion VPN globale (c'est-à-dire Enhanced Kill Switch), reportez-vous à [All Other Traffic](#all-other-traffic).

- Pour configurer Kill Switch pour chaque tunnel VPN individuel, reportez-vous à [Options du tunnel](#tunnel-options).

## All Other Traffic

Cliquez sur l'icône d'engrenage en haut à droite pour configurer une politique pour le trafic ne correspondant pas au tunnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Cette stratégie contrôle si le trafic qui ne correspond à aucun de vos groupes de tunnels VPN peut accéder ou non à Internet. Deux options disponibles : **Allow Non-VPN Traffic** et **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic** : activé par défaut pour garantir un accès Internet normal pour le trafic non VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch** : force tous les appareils à accéder à Internet via un VPN. Tout trafic ne correspondant pas à un tunnel VPN sera bloqué. Ce paramètre global ne remplace pas le Kill Switch configuré pour les tunnels VPN individuels.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Options des tunnels {#tunnel-options}

Vous pouvez configurer des paramètres avancés pour chaque tunnel VPN, tels que le VPN Kill Switch, le masquage IP et le MTU.

Cliquez sur l'icône d'engrenage dans un groupe de tunnels et sélectionnez **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch** : si activé, le trafic correspondant à ce tunnel VPN sera bloqué si la connexion VPN échoue de manière inattendue. S'il est désactivé, ce trafic basculera vers le tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN** : s'ils sont activés, les services GoodCloud, DDNS et rtty transmettront les paquets via des tunnels VPN. Cette option est désactivée par défaut, car ces services nécessitent normalement la véritable adresse IP de l'appareil pour fonctionner correctement.

- **Allow Remote Access to the LAN Subnet** : si activé, l'accès à distance à ce routeur et à ses périphériques LAN via le VPN sera autorisé. Cela nécessite que le serveur VPN annonce une route vers son sous-réseau LAN.

- **IP Masquerading** : si activé, les adresses IP sources des clients LAN seront réécrites sur l'IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où l'homologue distant connaît vos sous-réseaux LAN.

- **MTU** : la valeur MTU que vous avez définie pour le tunnel remplacera les paramètres MTU dans le fichier de configuration.

## Priorité des tunnels

Pour ajuster la priorité du tunnel, cliquez sur l'icône d'engrenage dans un groupe de tunnels et sélectionnez **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Cliquez et maintenez l'icône à trois lignes à droite pour réorganiser les tunnels, puis cliquez sur **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router routes traffic according to the following rules** :

1. Le trafic tentera d’abord de correspondre à la règle de tunnel la plus prioritaire. S'il correspond, il sera acheminé via ce tunnel ; sinon, il essaiera le tunnel prioritaire suivant, et ainsi de suite.

2. Chaque groupe de tunnels fonctionne de manière indépendante. Une fois que le trafic correspond à une règle de tunnel, il sera acheminé via ce tunnel et ne basculera pas entre les groupes de tunnels.

3. Plusieurs profils peuvent être sélectionnés dans chaque groupe de tunnels pour permettre le basculement intra-tunnel. Lorsque le profil ayant la priorité la plus élevée dans un groupe de tunnels tombe en panne, le tunnel se connectera automatiquement en utilisant le profil ayant la deuxième priorité la plus élevée, et ainsi de suite.

4. Si un tunnel VPN se déconnecte de manière inattendue, le système déterminera s'il doit basculer le trafic vers le tunnel All Other Traffic en fonction de l'activation ou non du **Kill Switch** de ce tunnel.

    - Si le Kill Switch est activé, le trafic sera bloqué et ne basculera pas vers le tunnel All Other Traffic.
    - Si le Kill Switch est désactivé, le trafic basculera vers le tunnel All Other Traffic.

5. Dans le tunnel **All Other Traffic**, différents modes déterminent si le trafic qui ne correspond pas au tunnel VPN peut accéder à Internet.

    - **Allow Non-VPN Traffic** : Il est activé par défaut pour garantir que le trafic ne correspondant pas aux tunnels VPN puisse toujours accéder à Internet via le WAN local.

    - **Enhanced Kill Switch** : Il oblige tous les appareils à accéder à Internet via un VPN. Tout trafic ne correspondant pas à un tunnel VPN sera bloqué. Ce paramètre global ne remplace pas le Kill Switch configuré pour les tunnels VPN individuels. Bref, il renforce le Kill Switch et bloque l’accès régulier à Internet pour éviter les fuites IP.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
