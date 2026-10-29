# Guide d'utilisation de Flint 3e (GL-BE6500) {#flint-3e-gl-be6500-user-guide}

## Aperçu du produit {#product-overview}

Flint 3e (GL-BE6500) est un routeur de bureau Wi-Fi 7 bi-bande conçu pour les particuliers et les petits bureaux. Il prend en charge Multi-Link Operation (MLO), qui permet aux appareils compatibles d’utiliser des liaisons sur les bandes 2.4 GHz et 5 GHz afin d’atténuer les effets des interférences et de la congestion. Sa modulation 4K-QAM offre des débits théoriques jusqu’à 20% supérieurs à ceux de la modulation 1024-QAM du Wi-Fi 6 dans des conditions par ailleurs identiques. Le routeur prend en charge un débit théorique bi-bande combiné allant jusqu’à 6452 Mbps, avec 4×4 MIMO et une largeur de canal de 160 MHz sur la bande 5 GHz. Les débits réels dépendent des capacités des clients et des conditions du réseau.

Doté de 5× ports Ethernet 2.5G et de 1× port USB 3.0, il prend en charge une connectivité filaire haut débit ainsi que l'extension du stockage. En outre, il est compatible avec plus de 30 services VPN et offre des performances VPN allant jusqu'à 680Mbps avec WireGuard® et OpenVPN-DCO. Il inclut également gratuitement Bark Parental Control, pour un excellent équilibre entre performances, praticité et sécurité.

![interface gl-be6500](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/hardware_info/be6500_interface.jpg){class="glboxshadow"}

**Remarque** : la différence d'apparence entre Flint 3e et Flint 3 réside dans la sérigraphie : celle du Flint 3e est bleue, tandis que celle du Flint 3 est blanche.

## Contenu du colis {#package-contents}

- 1 x Flint 3e (GL-BE6500)
- 1 x adaptateur secteur
- 1 x câble Ethernet
- 1 x manuel d'utilisation
- 1 x carte de remerciement
- 1 x adaptateur (selon votre pays de livraison)

Découvrez ci-dessous la vidéo de déballage du Flint 3e.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-E0LtWqshk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration initiale de Flint 3e {#how-to-set-up-flint-3e}

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/R40QsUFYuUk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension {#1-power-on}

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur, puis à une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil {#2-connect-device}

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi-Fi de votre routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. Le nom du réseau et le mot de passe par défaut figurent sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web {#3-log-in-to-web-admin-panel}

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 4. Configuration Internet {#4-internet-setup}

**Remarque :** les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions affichées à l'écran. 

Configurez votre Flint 3e avec l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), configurez plus d'une connexion Internet.

=== "Ethernet"
    
    ![Connexion Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_ethernet.jpg){class="glboxshadow"}

    Reliez le port WAN du Flint 3e à un appareil amont (par exemple un modem) à l'aide d'un câble Ethernet.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Connexion Repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_repeater.jpg){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi parmi les réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Repeater de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via un réseau Wi-Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Connexion Tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Paramètres et activez le partage de connexion USB.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois le routeur connecté à Internet, un point vert apparaît dans la section Tethering de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Connexion Cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be6500/internet/be6500_cellular.jpg){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du Flint 3e. Cela permet de partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie, un point vert apparaît dans la section Cellular de la page INTERNET.

    Pour des instructions détaillées, reportez-vous à [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md).

---

Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d'administration web du Flint 3e.

## Wi-Fi {#wireless}

La page Wireless vous permet de configurer les paramètres des réseaux Wi-Fi 5 GHz et 2.4 GHz, notamment l'activation du Wi-Fi, la puissance TX, le nom du réseau Wi-Fi (SSID), l'activation d'un BSSID aléatoire, le mode de sécurité Wi-Fi et le mot de passe, la visibilité du SSID, ainsi que le mode Wi-Fi, la bande passante et le canal.
    
En outre, Flint 3e prend en charge le Wi-Fi MLO, c'est-à-dire Multi-Link Operation, qui combine plusieurs réseaux sans fil simultanément afin d'offrir une bande passante plus élevée et des connexions plus fiables.

Pour configurer Wireless, reportez-vous à [Wireless](../../interface_guide/wireless.md).

## Clients {#clients}

La page Clients affiche les informations relatives aux appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

Pour configurer Clients, reportez-vous à [Clients](../../interface_guide/clients.md).

## Services cloud {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, reportez-vous à [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Spécialement conçue pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils sur l'ensemble du réseau, en permettant de contrôler aussi bien les équipements en amont qu'en aval. Axée sur la gestion à l'échelle du réseau et sur une future prise en charge du contrôle au niveau matériel, AstroWarp offre une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sécurisés et stables.
    
    Pour configurer AstroWarp, reportez-vous à [AstroWarp](../../interface_guide/astrowarp.md).

## VPN {#vpn}

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Flint 3e prend en charge OpenVPN et WireGuard.

=== "OpenVPN" 
    
    Le Flint 3e (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité élevée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Le Flint 3e (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau {#network}

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer simultanément plusieurs connexions Internet sur votre routeur (par exemple Ethernet, Tethering et Cellular). Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, reportez-vous à [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, ou réseau local (Local Area Network), est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme un domicile ou un bureau. Il permet un transfert de données à haut débit et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Il vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de la passerelle et du masque réseau, et de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, reportez-vous à [Guest Network](../../interface_guide/guest_network.md).

=== "IoT Network"

    Cette fonction permet de créer un réseau Wi-Fi dédié aux appareils IoT. Isolé du réseau principal, il offre une meilleure compatibilité et une sécurité renforcée.

    Pour configurer le IoT Network, consultez [Lan](../../interface_guide/iot_network.md).

---

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d’activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients et d’autoriser les DNS personnalisés à remplacer les DNS VPN. Vous pouvez utiliser les serveurs DNS obtenus automatiquement auprès des appareils en amont ou spécifier manuellement des serveurs DNS personnalisés.

    Pour configurer DNS, reportez-vous à [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La page Ethernet Port vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, reportez-vous à [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPV6, reportez-vous à [IPV6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP Snooping, reportez-vous à [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Le mode réseau désigne les paramètres de configuration qui déterminent la façon dont un appareil se connecte à un réseau et communique avec d'autres appareils.
    
    Pour configurer le mode réseau, reportez-vous à [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in gateway"

    Drop-in gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, reportez-vous aux liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    La fonctionnalité Network Acceleration peut réduire la charge CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer Network Acceleration, reportez-vous à [Network Acceleration](../../interface_guide/network_acceleration.md).

## Contrôle du trafic {#flow-control}

=== "DPI Engine"

    DPI (Deep Packet Inspection) est une fonction essentielle de la gestion intelligente des réseaux. Elle dépasse les limites des routeurs traditionnels, qui identifient uniquement les adresses source ou de destination, en analysant en profondeur le contenu des paquets. La comparaison avec une bibliothèque de signatures identifie avec précision les applications et sites Web consultés afin d’affiner la classification et le contrôle du trafic.
    
    Intégrée à [Netify](https://www.netify.ai/){target="_blank"}, la fonction DPI de GL.iNet utilise un module embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, elle assure une gestion fiable et un contrôle du réseau plus précis et efficace.

    Veuillez consulter [DPI Engine](../../interface_guide/dpi_engine.md) pour des instructions détaillées.

=== "Data Statistics"

    Data Statistics propose un tableau de bord intelligent qui classe et représente l’utilisation du réseau par application. Il permet de surveiller le trafic en temps réel et l’historique afin de mieux comprendre et contrôler le réseau.

    Pour des instructions détaillées, consultez [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter assure une sécurité en ligne intelligente grâce à la classification DPI et bloque automatiquement les sites Web dangereux ou malveillants afin de préserver la sécurité du réseau.

    Pour des instructions détaillées, consultez [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) optimise l’attribution de la bande passante en donnant la priorité aux activités importantes, par exemple les appels vidéo et les jeux, en cas de congestion. Cela réduit la latence et améliore les performances globales du réseau. Cette fonction s’applique au trafic des clients locaux et des tunnels VPN Client, mais pas au trafic reçu lorsque le routeur fonctionne comme VPN Server.

    Veuillez consulter [QoS](../../interface_guide/qos.md) pour des instructions détaillées.

=== "SQM"

    SQM (Smart Queue Management) gère intelligemment le trafic réseau du routeur afin de réduire la latence et le « bufferbloat », pour des jeux et des appels vocaux plus fluides.

    Veuillez consulter [SQM](../../interface_guide/sqm.md) pour des instructions détaillées.

=== "Parental Control"

    Parental Control aide à gérer et à contrôler les appareils de vos enfants, notamment en limitant leur temps d’écran et l’accès à certains contenus.

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control_v4.9.md).

## Sécurité {#security}

=== "Port Forwarding"

    La redirection de ports permet à des serveurs et appareils distants sur Internet d'accéder aux appareils d'un réseau privé.
    
    Pour configurer la redirection de ports, reportez-vous à [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, ou Access Control List, permet de créer des règles de gestion du trafic réseau selon les protocoles de connexion, les adresses des appareils et les ports. Ces règles autorisent ou bloquent l’accès au réseau. Si plusieurs règles ACL sont en conflit, le système applique celle dont la priorité est la plus élevée.

    Pour plus de détails, consultez [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access permet de configurer différents paramètres de sécurité afin de protéger le réseau et le routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Local Access Control : gérer et restreindre l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurer et restreindre l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la protection contre les menaces externes.
    * Open Ports on Router : contrôler les ports ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Pour plus de détails, consultez [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La page NAT Mode permet d’activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications {#applications}

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, afin de permettre la personnalisation et l'amélioration de ses capacités.
    
    Pour configurer les plug-ins, reportez-vous à [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met automatiquement à jour en temps réel l'adresse IP associée à un domaine. Il associe un nom de domaine à l'adresse IP publique dynamique de votre routeur, ce qui vous permet d'accéder à votre réseau à distance sans adresse IP statique.
    
    Pour configurer Dynamic DNS, reportez-vous à [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, reportez-vous à [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l'échelle du réseau, qui agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, reportez-vous à [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Intégré à Flint 3e, le service Bark aide à protéger l’environnement numérique de votre enfant et offre une protection en ligne complète. Il nécessite généralement un abonnement payant. Cependant, dans le cadre de son partenariat avec Bark, GL.iNet offre gratuitement l’offre Bark Home sur certains modèles de routeurs, dont Flint 3e, avec une surveillance avancée et des alertes sans frais supplémentaires.

    Pour plus de détails, consultez [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications où que vous soyez.
    
    Pour configurer Tailscale, reportez-vous à [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, reportez-vous à [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet une communication anonyme sur Internet. Il achemine le trafic Internet via une série de serveurs (nœuds) exploités par des bénévoles afin de masquer la localisation et l'utilisation de l'utilisateur, ce qui rend les activités en ligne difficiles à retracer.
    
    Pour plus de détails, consultez [Tor](../../interface_guide/tor.md).

## Système {#system}

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

=== "Admin Password"

    La page Admin Password permet de gérer le mot de passe de l’interface d’administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour plus de détails, consultez [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La page Upgrade sert à mettre à jour le firmware de votre routeur vers la dernière version, afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : recherche automatiquement la dernière version du firmware sur le serveur du fabricant. Vous pouvez l'installer si elle est disponible en ligne.
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

=== "Reset Firmware"

    La page Reset Firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware de votre routeur, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir de zéro avec la configuration par défaut du firmware actuel.

    Pour des instructions détaillées, reportez-vous à [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés au fonctionnement et aux événements du noyau.
    * Crash Log : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et le fonctionnement du serveur.
    
    En outre, la page propose un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées, reportez-vous à [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées, reportez-vous à [Advanced Settings](../../interface_guide/advanced_settings.md).

## Déclaration UE de conformité {#declaration-of-conformity}

Par la présente, GL TECHNOLOGIES (HONG KONG) LIMITED déclare que le type d'équipement radio [BE6500 Wi-Fi 7 Router, GL-BE6500] est conforme aux exigences essentielles et autres dispositions pertinentes de la Directive 2014/53/UE. Le texte complet de la déclaration de conformité UE est disponible à l'adresse internet suivante: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
