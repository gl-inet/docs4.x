# Guide d'utilisation du Slate 7 (GL-BE3600)

## Aperçu du produit

Le Slate 7 (GL-BE3600) est le premier routeur de voyage portable Wi-Fi 7 double bande de GL.iNet, conçu avec des technologies Wi-Fi 7 haut de gamme, dont Multi-Link Operation et le 4K QAM. Il offre des débits théoriques double bande de 688Mbps (2.4GHz) et 2882Mbps (5GHz), pour une expérience fluide de streaming 8K et de jeux mobiles. Son écran tactile permet de vérifier l'état du réseau d'un seul coup d'œil et d'effectuer facilement les opérations de base.

Équipé de 2 ports Ethernet 2.5G (1 WAN + 1 LAN) et de 1 port USB 3.0, ce routeur répond aux besoins de connexions filaires à haut débit et d'extension de stockage flexible. Il prend également en charge l'alimentation Type-C PD (5V/3A, 9V/3A, 12V/2.5A) et adopte un format compact et léger facile à transporter. Préinstallé avec AdGuard Home et compatible avec plus de 30 services VPN, il offre une protection renforcée à votre réseau. Alliant mobilité et performances de niveau professionnel, le Slate 7 constitue un excellent choix pour le travail à distance et le partage de réseau en déplacement.

![gl-be3600 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/hardware_info/be3600_interface.jpg){class="glboxshadow"}

## Contenu du colis

- 1 x Slate 7 (GL-BE3600)
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Câble d'alimentation
- 1 x Adaptateur secteur US
- 3 x Adaptateurs (prises EU, UK et AU)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/first_time_setup/be3600_unboxing.jpg){class="glboxshadow"}

Découvrez la vidéo de déballage du Slate 7 ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bEuwGm0hQ5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration initiale du Slate 7

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHQK8wSQGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Dans cette vidéo, nous montrons la configuration du Slate 7 en mode Repeater. Si vous devez configurer le Slate 7 avec une autre méthode de connexion Internet, reportez-vous aux étapes ci-dessous.)</small>

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur, puis à une prise électrique. Il démarrera automatiquement.

### 2. Écran tactile

??? "Mise sous tension"

    Lorsque le routeur est mis sous tension, le logo GL.iNet s'affiche à l'écran, suivi de la barre de progression du démarrage.

    ![booting](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/booting.png){class="glboxshadow"}
    
    Une fois la barre de progression entièrement chargée, le démarrage de l'appareil est terminé.

??? "Réseau"

    L'écran d'accueil affiche quatre icônes correspondant à quatre types de connexion réseau : Ethernet, Repeater, Tethering et Cellular.

    ![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

    | Couleur            | État                               |
    | :----------------- | :--------------------------------- |
    | Vert               | Actif / Connecté à Internet        |
    | Jaune              | Connexion en cours / Échec réseau  |
    | Blanc              | Connexion inactive                 |

    Touchez l'une de ces icônes pour afficher l'état du réseau ou des informations détaillées sur la configuration.

??? "Fonctions"

    Vous pouvez accéder aux fonctions en balayant l'écran vers la gauche ou la droite.

    En balayant de droite à gauche, les éléments suivants s'affichent dans l'ordre. Certains nécessitent une configuration préalable dans le panneau d'administration. En balayant de gauche à droite, l'ordre d'affichage est inversé.

    - Connexion réseau

        ![network connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/network.png){class="glboxshadow"}

    - Détails du Wi-Fi tri-bande (y compris le SSID, le mot de passe, le code QR et le bouton d'activation)

        ![wifi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wifi-details.png){class="glboxshadow"}

    - OpenVPN

        ![openvpn](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/nordvpn-4.7.jpg){class="glboxshadow"}

    - WireGuard

        ![wireguard](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/wireguard.png){class="glboxshadow"}

    - AdGuard Home

        ![adguard home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/adguard_home.png){class="glboxshadow"}

    - Tor

        ![tor](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/tor.png){class="glboxshadow"}

    - Statistiques du trafic (il s'agit de la vitesse moyenne de l'ensemble du trafic transitant par le routeur. La vitesse est calculée toutes les 3 secondes.)

        ![traffic statistics](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/traffic_statistics.png){class="glboxshadow"}

    - Aperçu du CPU

        ![CPU overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/overview.png){class="glboxshadow"}

    - Heure

        ![time](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/time.png){class="glboxshadow"}

??? "Système"

    Balayez de haut en bas pour accéder aux paramètres système : Reboot et Lock Screen.

    ![system settings](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/system_settings.png){class="glboxshadow"}

    - Reboot : en touchant "Reboot", l'invite "Slide To Reboot" s'affiche (vérification en deux étapes), puis le routeur lance le processus de redémarrage.

        ![slide to reboot](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-reboot.png){class="glboxshadow"}

    - Lock Screen : l'écran s'éteint lorsque vous touchez l'option "Lock Screen". Touchez l'écran pour le rallumer ; la page de fonction sur laquelle il se trouvait en dernier s'affiche. En touchant à nouveau, l'invite "Slide To Unlock" s'affiche.

        ![slide to unlock](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/touchscreen/slide-to-unlock.png){class="glboxshadow"}

### 3. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via le Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, repérez le nom du réseau Wi-Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour rejoindre le réseau. Le nom du réseau et le mot de passe par défaut sont indiqués sur l'étiquette du routeur.

### 4. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez une langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 5. Configuration de la connexion Internet

**Remarque :** Les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Slate 7 à l'aide de l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_ethernet.jpg){class="glboxshadow"}
    
    Connectez le port WAN du Slate 7 à un appareil amont (par exemple un modem) à l'aide d'un câble Ethernet.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_repeater.jpg){class="glboxshadow"}

    1. Sur l'écran INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Repeater de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un réseau Wi-Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, ouvrez les paramètres et activez le partage de connexion USB.
    3. Sur l'écran INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Tethering de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be3600/internet/be3600_cellular.jpg){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du Slate 7. Cette méthode est utile pour partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Cellular de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md).

---

Vous trouverez ci-dessous un aperçu des fonctions disponibles dans le panneau d'administration web du Slate 7.

## Wireless

La page Wireless vous permet de configurer les paramètres des réseaux Wi-Fi 5 GHz et 2.4 GHz, notamment l'activation du Wi-Fi, le réglage de la puissance TX, la définition du nom du réseau Wi-Fi (SSID), l'activation du BSSID aléatoire, le choix du mode de sécurité Wi-Fi et du mot de passe, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi-Fi, de la largeur de bande et du canal.

En outre, le Slate 7 prend en charge le Wi-Fi MLO, c'est-à-dire Multi-Link Operation, qui combine plusieurs réseaux sans fil simultanément afin d'obtenir une bande passante plus élevée et des connexions plus fiables.

Pour configurer Wireless, reportez-vous à [Wireless](../../interface_guide/wireless.md).

## Clients

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et de téléversement, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

Pour configurer Clients, reportez-vous à [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, reportez-vous à [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Développé spécifiquement pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge la gestion complète des appareils sur des réseaux entiers, avec contrôle des appareils supérieurs et inférieurs. Axé sur la gestion à l'échelle du réseau et sur la prise en charge future du contrôle au niveau matériel, AstroWarp constitue une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.
    
    Pour configurer AstroWarp, reportez-vous à [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Le Slate 7 prend en charge OpenVPN, WireGuard et Tor.

=== "OpenVPN" 
    
    Le Slate 7 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Le Slate 7 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet des communications anonymes sur Internet. Il fait transiter le trafic Internet par une série de serveurs gérés par des bénévoles (nœuds) afin de masquer l'emplacement et l'utilisation de l'utilisateur, ce qui rend le suivi des activités en ligne difficile.
    
    * [Comment configurer Tor](../../interface_guide/tor.md)

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, afin de permettre sa personnalisation et l'extension de ses capacités.
    
    Pour configurer les plug-ins, reportez-vous à [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met automatiquement à jour en temps réel l'adresse IP associée à un domaine. Cette fonction est utile pour les utilisateurs qui ont besoin d'une adresse IP statique afin d'accéder à un réseau distant.
    
    Pour configurer Dynamic DNS, reportez-vous à [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder à des fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, reportez-vous à [Stockage réseau](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des trackers à l'échelle du réseau, qui agit comme un serveur DNS afin de filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, reportez-vous à [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Le contrôle parental est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre leur accès à certains contenus.

    Pour configurer le contrôle parental, reportez-vous à [Contrôle parental](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier est une solution réseau définie par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, reportez-vous à [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et à vos applications où que vous soyez.
    
    Pour configurer Tailscale, reportez-vous à [Tailscale](../../interface_guide/tailscale.md).

## Réseau

=== "Port forwarding"

    La redirection de port permet aux serveurs distants et aux appareils sur Internet d'accéder aux appareils situés sur un réseau privé.
    
    Pour configurer la redirection de port, reportez-vous à [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Cellular, Repeater et Ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion Internet. Cela garantit un accès à Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, reportez-vous à [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Le LAN, ou Local Area Network, est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme un domicile ou un bureau. Il permet un transfert de données à grande vitesse et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, reportez-vous à [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Cette fonction vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de passerelle et de masque réseau, ainsi que de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, reportez-vous à [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS et de remplacer les paramètres DNS de tous les clients, d'autoriser les DNS personnalisés à remplacer les DNS du VPN, et de configurer le mode des paramètres du serveur DNS sur automatique ou de spécifier manuellement les serveurs DNS de la connexion Ethernet.

    Pour configurer DNS, reportez-vous à [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La page Ethernet Port vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, reportez-vous à [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Le mode réseau désigne les paramètres de configuration qui déterminent la manière dont un appareil se connecte à un réseau et communique avec d'autres appareils.
    
    Pour configurer le mode réseau, reportez-vous à [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage beaucoup plus vaste, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour accueillir le nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPV6, reportez-vous à [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, reportez-vous aux liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP snooping, reportez-vous à [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets de trafic.
    
    Pour configurer l'accélération réseau, reportez-vous à [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La page NAT Settings vous permet d'activer ou de désactiver les fonctionnalités Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, reportez-vous à [NAT Settings](../../interface_guide/nat_settings.md).

## Système

=== "Overview"

    La page Overview fournit un aperçu complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez afficher :

    * CPU Average Load : surveillez la charge moyenne du CPU de votre routeur afin d'évaluer les performances et d'identifier les éventuels goulots d'étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée par votre routeur pour faciliter la gestion des ressources.
    * LED Control : activez ou désactivez les LED du routeur afin de personnaliser les indicateurs visuels de l'appareil.
    * Flash Usage : consultez l'utilisation du stockage flash du routeur afin de vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Device Info : accédez aux informations détaillées du système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, la MAC de l'appareil et son numéro de série.
    * External Storage : vérifiez l'état des périphériques de stockage externes connectés au routeur, comme des clés USB ou des cartes TF.
    
    Ces fonctions fournissent des informations et des contrôles essentiels pour gérer et surveiller efficacement le fonctionnement de votre routeur.

    Pour des instructions détaillées, reportez-vous à [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La page Upgrade sert à mettre à jour le firmware de votre routeur vers la version la plus récente, afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à niveau :

    * Firmware Online Upgrade : vérifie automatiquement la disponibilité de la dernière version du firmware et l'installe directement depuis le serveur du fabricant, ce qui simplifie la mise à jour.
    * Firmware Local Upgrade : téléverse manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous permet de contrôler la version installée et le moment de la mise à jour.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et correctifs.

    Pour des instructions détaillées, reportez-vous à [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La page Scheduled Tasks vous permet d'automatiser différentes fonctions du routeur selon un calendrier prédéfini, pour plus de praticité et d'efficacité. Les principales fonctions de cette page comprennent :

    * LED Display Schedule : définissez un calendrier pour allumer ou éteindre automatiquement les LED du routeur, afin de réduire la pollution lumineuse à certaines heures.
    * Schedule Reboot : configurez le redémarrage automatique du routeur à des intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Wi-Fi Status Schedule : définissez un calendrier pour contrôler la bande Wi-Fi 5GHz / 2.4GHz / MLO, afin de mieux gérer la disponibilité du réseau et la consommation électrique.
    
    Ces options de planification vous offrent davantage de contrôle sur le fonctionnement de votre routeur afin qu'il réponde à vos besoins et à vos préférences.

    Pour des instructions détaillées, reportez-vous à [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Display Management"

    La page Display Management propose un ensemble complet de fonctions pour gérer l'écran tactile et les paramètres associés.
    
    - Function Management : gérez les fonctions affichées sur l'écran tactile afin d'adapter l'affichage à vos besoins.
    - Lock Screen : personnalisez les paramètres de l'écran verrouillé. Vous pouvez définir le fond d'écran et le réveil de l'écran.
    - Brightness : réglez la luminosité de l'écran tactile. Utilisez le curseur ou saisissez un niveau précis (de 1 à 10) en fonction des conditions d'éclairage.
    - Auto Lock : définissez le délai avant le verrouillage automatique de l'écran lorsqu'il n'y a aucune activité. La plage va de 1 à 30 minutes.
    - Screen Always On : activez ou désactivez cette option pour décider si l'écran tactile reste allumé en continu ou s'éteint après une période d'inactivité.
    - Enable Screen Passcode : ajoutez une couche de sécurité supplémentaire en activant un code d'accès pour l'écran tactile.

    Pour des instructions détaillées, reportez-vous à [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour tenir des enregistrements précis et garantir l'exécution correcte des configurations basées sur l'heure.

    Pour des instructions détaillées, reportez-vous à [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La page Toggle Button Settings vous permet de configurer le bouton bascule physique de votre routeur, afin d'y attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonctionnalité offre des raccourcis pratiques pour les tâches et réglages courants, améliore l'expérience utilisateur et simplifie la gestion du routeur.

    Pour des instructions détaillées, reportez-vous à [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * System Log : des journaux détaillés des événements et activités au niveau système.
    * Kernel Log : des journaux liés aux opérations et événements du noyau.
    * Crash Log : des enregistrements des plantages et erreurs du système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : des journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : des journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et le fonctionnement du serveur.
    
    En outre, la page comporte un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées, reportez-vous à [Log](../../interface_guide/log.md).

=== "Security"

    La page Security vous permet de configurer différents paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend des options pour :

    * Admin Password : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Local Access Control : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants sur Internet, pour renforcer la sécurité face aux menaces externes.
    * Open Ports on Router : contrôlez quels ports sont ouverts sur le routeur afin de réduire les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.

    Pour des instructions détaillées, reportez-vous à [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    La page Reset Firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware de votre routeur, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Pour des instructions détaillées, reportez-vous à [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées, reportez-vous à [Advanced Settings](../../interface_guide/advanced_settings.md).

