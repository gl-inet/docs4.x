# Guide d'utilisation de Flint 3e (GL-BE6500)

## Aperçu du produit

Flint 3e (GL-BE6500) est un routeur de bureau Wi-Fi 7 bi-bande conçu pour les particuliers et les petits bureaux. Il prend en charge la technologie Wi-Fi 7 Multi-Link Operation (MLO), qui fusionne intelligemment les canaux 2.4GHz et 5GHz en une seule connexion. L'utilisation simultanée des ressources bi-bande réduit les interférences et l'encombrement, tandis que le 4K QAM offre un débit bi-bande combiné de 6453Mbps — soit 20 % de plus que le Wi-Fi 6. La bande 5GHz améliorée (4x4 MIMO, 160MHz) renforce également de manière significative les performances à longue distance.

Doté de 5× ports Ethernet 2.5G et de 1× port USB 3.0, il prend en charge une connectivité filaire haut débit ainsi que l'extension du stockage. En outre, il est compatible avec plus de 30 services VPN et offre des performances VPN allant jusqu'à 680Mbps avec WireGuard® et OpenVPN-DCO. Il inclut également gratuitement Bark Parental Control, pour un excellent équilibre entre performances, praticité et sécurité.

![interface gl-be6500](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**Remarque** : la différence d'apparence entre Flint 3e et Flint 3 réside dans la sérigraphie : celle du Flint 3e est bleue, tandis que celle du Flint 3 est blanche.

## Contenu du colis

- 1 x Flint 3e (GL-BE6500)
- 1 x adaptateur secteur
- 1 x câble Ethernet
- 1 x manuel d'utilisation
- 1 x carte de remerciement
- 1 x adaptateur (selon votre pays de livraison)

Découvrez ci-dessous la vidéo de déballage du Flint 3e.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration initiale de Flint 3e

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur, puis à une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi-Fi de votre routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. Le nom du réseau et le mot de passe par défaut figurent sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 4. Configuration Internet

**Remarque :** les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions affichées à l'écran. 

Configurez votre Flint 3e avec l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), configurez plus d'une connexion Internet.

=== "Ethernet"
    
    ![Connexion Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Reliez le port WAN du Flint 3e à un appareil amont (par exemple un modem) à l'aide d'un câble Ethernet.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Connexion Repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi parmi les réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Repeater de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un réseau Wi-Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Connexion Tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Paramètres et activez le partage de connexion USB.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois le routeur connecté à Internet, un point vert apparaît dans la section Tethering de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Connexion Cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du Flint 3e. Cela permet de partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie, un point vert apparaît dans la section Cellular de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md).

---

Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d'administration web du Flint 3e.

## Wi-Fi

La page Wireless vous permet de configurer les paramètres des réseaux Wi-Fi 5 GHz et 2.4 GHz, notamment l'activation du Wi-Fi, la puissance TX, le nom du réseau Wi-Fi (SSID), l'activation d'un BSSID aléatoire, le mode de sécurité Wi-Fi et le mot de passe, la visibilité du SSID, ainsi que le mode Wi-Fi, la bande passante et le canal.
    
En outre, Flint 3e prend en charge le Wi-Fi MLO, c'est-à-dire Multi-Link Operation, qui combine plusieurs réseaux sans fil simultanément afin d'offrir une bande passante plus élevée et des connexions plus fiables.

Pour configurer Wireless, reportez-vous à [Wireless](../../interface_guide/wireless.md).

## Clients

La page Clients affiche les informations relatives aux appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

Pour configurer Clients, reportez-vous à [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, reportez-vous à [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Spécialement conçue pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils sur l'ensemble du réseau, en permettant de contrôler aussi bien les équipements en amont qu'en aval. Axée sur la gestion à l'échelle du réseau et sur une future prise en charge du contrôle au niveau matériel, AstroWarp offre une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sécurisés et stables.
    
    Pour configurer AstroWarp, reportez-vous à [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

Un VPN (réseau privé virtuel) établit un tunnel sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Flint 3e prend en charge OpenVPN, WireGuard et Tor.

=== "OpenVPN" 
    
    Le Flint 3e (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité élevée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Le Flint 3e (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet une communication anonyme sur Internet. Il achemine le trafic Internet via une série de serveurs (nœuds) exploités par des bénévoles afin de masquer la localisation et l'utilisation de l'utilisateur, ce qui rend les activités en ligne difficiles à retracer.
    
    * [Configurer Tor](../../interface_guide/tor.md)

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, afin de permettre la personnalisation et l'amélioration de ses capacités.
    
    Pour configurer les plug-ins, reportez-vous à [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met automatiquement à jour en temps réel l'adresse IP associée à un domaine. Il est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique afin d'accéder à un réseau distant.
    
    Pour configurer Dynamic DNS, reportez-vous à [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, reportez-vous à [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l'échelle du réseau, qui agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, reportez-vous à [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre leur accès à certains contenus.

    Pour configurer le contrôle parental, reportez-vous à [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, reportez-vous à [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications où que vous soyez.
    
    Pour configurer Tailscale, reportez-vous à [Tailscale](../../interface_guide/tailscale.md).

## Paramètres réseau

=== "Port forwarding"

    La redirection de ports permet à des serveurs et appareils distants sur Internet d'accéder aux appareils d'un réseau privé.
    
    Pour configurer la redirection de ports, reportez-vous à [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Cellular, Repeater et Ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion Internet. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, reportez-vous à [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, ou réseau local (Local Area Network), est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme un domicile ou un bureau. Il permet un transfert de données à haut débit et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer LAN, reportez-vous à [Lan](../../interface_guide/lan.md).

---

=== "Guest Network"

    Il vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de la passerelle et du masque réseau, et de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, reportez-vous à [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS et de remplacer les paramètres DNS de tous les clients, d'autoriser les DNS personnalisés à remplacer les DNS VPN, ainsi que de régler le mode des paramètres du serveur DNS sur automatique ou de spécifier manuellement les serveurs DNS de la connexion Ethernet.

    Pour configurer DNS, reportez-vous à [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La page Ethernet Port vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, reportez-vous à [Ethernet Port](../../interface_guide/ethernet_port.md).

---

=== "Network Mode"

    Le mode réseau désigne les paramètres de configuration qui déterminent la façon dont un appareil se connecte à un réseau et communique avec d'autres appareils.
    
    Pour configurer le mode réseau, reportez-vous à [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPV6, reportez-vous à [IPV6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, reportez-vous aux liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

---

=== "IGMP Snooping"

    IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP Snooping, reportez-vous à [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La fonctionnalité Network Acceleration peut réduire la charge CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer Network Acceleration, reportez-vous à [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La page NAT Settings vous permet d'activer ou de désactiver les fonctionnalités Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer NAT Settings, reportez-vous à [NAT Settings](../../interface_guide/nat_settings.md).

## Paramètres système

=== "Overview"

    La page Overview fournit un aperçu complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez afficher :

    * CPU Average Load : surveillez la charge moyenne du CPU de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulots d'étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée par votre routeur afin de mieux gérer les ressources.
    * LED Control : activez ou désactivez les voyants LED du routeur afin de personnaliser les indicateurs visuels de l'appareil.
    * Flash Usage : consultez l'utilisation du stockage flash du routeur pour vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Device Info : accédez à des informations détaillées sur le système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC de l'appareil et son numéro de série.
    * External Storage : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que des clés USB ou des cartes TF.
    
    Ces fonctions fournissent des informations et des commandes essentielles pour vous aider à gérer et à surveiller efficacement le fonctionnement de votre routeur.

    Pour des instructions détaillées, reportez-vous à [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La page Upgrade sert à mettre à jour le firmware de votre routeur vers la dernière version, afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : recherchez et installez automatiquement la dernière version du firmware directement depuis le serveur du fabricant, afin de simplifier la mise à jour.
    * Firmware Local Upgrade : importez manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous permet de contrôler la version installée et le moment de la mise à jour.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Pour des instructions détaillées, reportez-vous à [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La page Scheduled Tasks vous permet d'automatiser diverses fonctions du routeur selon un calendrier prédéfini, afin d'améliorer le confort d'utilisation et l'efficacité. Les principales fonctions de cette page comprennent :

    * LED Display Schedule : définissez un calendrier pour allumer ou éteindre automatiquement les voyants LED du routeur, afin de réduire la pollution lumineuse à certaines heures.
    * Schedule Reboot : configurez le redémarrage automatique du routeur à des intervalles définis, afin de maintenir des performances et une stabilité optimales.
    * Wi-Fi Status Schedule : définissez un calendrier pour contrôler la bande Wi-Fi 5GHz / 2.4GHz / MLO, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement de votre routeur, afin qu'il réponde à vos besoins et préférences.

    Pour des instructions détaillées, reportez-vous à [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements précis et assurer le bon fonctionnement des configurations basées sur le temps.

    Pour des instructions détaillées, reportez-vous à [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés au fonctionnement et aux événements du noyau.
    * Crash Log : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et le fonctionnement du serveur.
    
    En outre, la page propose un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées, reportez-vous à [Log](../../interface_guide/log.md).

---

=== "Security"

    La page Security vous permet de configurer différents paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend des options pour :

    * Admin Password : définir ou modifier le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Local Access Control : gérer et restreindre l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurer et restreindre l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la protection contre les menaces externes.
    * Open Ports on Router : contrôler les ports ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé et à protéger à la fois votre routeur et les appareils connectés.

    Pour des instructions détaillées, reportez-vous à [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    La page Reset Firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware de votre routeur, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir de zéro avec la configuration par défaut du firmware actuel.

    Pour des instructions détaillées, reportez-vous à [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées, reportez-vous à [Advanced Settings](../../interface_guide/advanced_settings.md).
