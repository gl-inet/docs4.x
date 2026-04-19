# Guide d'utilisation du Slate 7 Pro (GL-BE10000)

## Aperçu du produit

Le Slate 7 Pro (GL-BE10000) est un routeur de voyage portable tri-bande Wi‑Fi 7. Version améliorée du Slate 7 (GL-BE3600), il dispose d’un écran tactile plus grand sur le dessus et embarque 1 Go de RAM DDR4 ainsi que 8 Go de stockage eMMC pour des performances stables et une bonne compatibilité avec les plug-ins. Il offre des vitesses VPN élevées allant jusqu’à 1 100 Mbps avec WireGuard® et 1 000 Mbps avec OpenVPN-DCO. Avec 2 ports Ethernet 2,5G (1 WAN + 1 LAN), 1 port USB-C 3.0 et la prise en charge de l’alimentation PD, il garantit une connectivité solide et une utilisation pratique en déplacement.

![gl-be10000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/hardware/be10000_interface.png){class="glboxshadow"}

## Contenu du colis

Le colis comprend :

- 1 x Slate 7 Pro (GL-BE10000)
- 1 x Manuel d’utilisation
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Câble d’alimentation
- 1 x Adaptateur secteur
- 4 x Convertisseurs (prises US, EU, UK et AU)

## Comment configurer le Slate 7 Pro

Pour configurer le Slate 7 Pro, vous utiliserez l’une des quatre méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Suivez les étapes ci-dessous.

### 1. Mise sous tension

Assemblez les deux parties de l’adaptateur secteur. Connectez-le à votre routeur, puis branchez-le sur une prise électrique. Il démarre automatiquement.

### 2. Écran tactile

Lorsque le routeur est mis sous tension, le logo GL.iNet s’affiche à l’écran, suivi de la barre de progression du démarrage.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/power_on.png){class="glboxshadow" width="360"}

Une fois la barre de progression entièrement chargée, l’appareil termine son démarrage et affiche l’écran de bienvenue. Suivez les instructions pour définir votre mot de passe administrateur et votre réseau Wi‑Fi.

![set admin password](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_admin.png){class="glboxshadow" width="360"}

![set WiFi](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/set_wifi.png){class="glboxshadow" width="360"}

Vous accéderez ensuite à l’écran d’accueil. La partie gauche affiche les informations système en temps réel, notamment l’heure système et la vitesse du réseau, et fournit des raccourcis vers le Wi‑Fi, les Clients, le VPN et d’autres fonctions. La partie droite propose des raccourcis vers les quatre modes de connexion : Ethernet, Repeater, Tethering et Cellular.

![home](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/home.png){class="glboxshadow" width="360"}

Les différentes couleurs des quatre raccourcis indiquent des états réseau différents.

![internet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/touchscreen/internet.png){class="glboxshadow" width="360"}

- **Bleu** : actif / connecté à Internet
- **Jaune** : connexion en cours / échec réseau
- **Blanc** : connexion inactive

### 3. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via le Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l’aide d’un câble Ethernet.

- Wi‑Fi

    Sur votre appareil, repérez le nom du réseau Wi‑Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. Vous trouverez le nom du réseau par défaut (SSID) et le mot de passe sur l’étiquette du routeur.

### 4. Se connecter au panneau d’administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d’adresse, puis connectez-vous. Choisissez une langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 5. Configuration Internet

Configurez votre Slate 7 Pro à l’aide de l’une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), configurez plus d’une connexion Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_ethernet.jpg){class="glboxshadow"}
    
    1. Connectez le port WAN du Slate 7 Pro à un appareil en amont (par exemple un modem FAI, un commutateur réseau ou une prise Ethernet murale) à l’aide d’un câble Ethernet.
    2. Le Slate 7 Pro tentera automatiquement d’obtenir les paramètres réseau, tels que l’adresse IP, la passerelle et le serveur DNS, afin d’établir une connexion Ethernet.
    3. Une fois la connexion Internet établie, la section Ethernet de l’écran d’accueil devient bleue (active). Vous pouvez soit toucher Ethernet sur l’écran d’accueil, soit vous connecter au panneau d’administration web pour consulter les détails de la connexion.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_repeater.jpg){class="glboxshadow"}

    1. Touchez **Repeater** sur l’écran tactile. Le routeur commence à rechercher les réseaux Wi‑Fi disponibles.
    2. Sélectionnez le réseau Wi‑Fi que vous souhaitez étendre avec le Slate 7 Pro.
    3. Saisissez le mot de passe, puis touchez **Apply**.
    4. Une fois la connexion Internet établie, la section Repeater de l’écran d’accueil devient bleue (active). Vous pouvez soit toucher Repeater sur l’écran d’accueil, soit vous connecter au panneau d’administration web pour consulter les détails de la connexion.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB du routeur à l’aide d’un câble USB.
    2. Sur votre appareil mobile, accédez aux réglages et activez **USB Tethering** ou **Personal Hotspot**. Si vous utilisez un iPhone, touchez **Trust This Device** si cela vous est demandé.
    3. Sur l’écran tactile, sélectionnez **Tethering**, puis touchez **Connect**. Le routeur se connectera à votre appareil.
    4. Une fois la connexion Internet établie, la section Tethering de l’écran d’accueil devient bleue (active). Vous pouvez soit toucher Tethering sur l’écran d’accueil, soit vous connecter au panneau d’administration web pour consulter les détails de la connexion.

    **Remarque** : si la connexion échoue, assurez-vous que la tension d’alimentation est supérieure à 9V 3A, car une alimentation insuffisante peut empêcher l’alimentation du port USB. Répétez les étapes ci-dessus, ou connectez-vous au panneau d’administration web pour vérifier l’état de la connexion Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be10000/internet/be10000_cellular.jpg){class="glboxshadow"}

    1. Branchez un modem USB cellulaire sur le port USB du Slate 7 Pro. Cela permet de partager la connexion Internet du modem USB avec tous les appareils connectés.
    2. Une fois la connexion Internet établie, la section Cellular de l’écran d’accueil devient bleue (active). Vous pouvez soit toucher Cellular sur l’écran d’accueil, soit vous connecter au panneau d’administration web pour consulter les détails de la connexion.

---

Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d’administration web du Slate 7 Pro.

## Réseau sans fil

La page Wireless permet de configurer les paramètres des réseaux Wi‑Fi 6 GHz, 5 GHz et 2,4 GHz, notamment l’activation du Wi‑Fi, le réglage de la puissance TX, le nom du réseau Wi‑Fi (SSID), l’activation d’un BSSID aléatoire, le choix du mode de sécurité Wi‑Fi et du mot de passe, la visibilité du SSID, ainsi que le mode Wi‑Fi, la bande passante et le canal.

En outre, le Slate 7 Pro prend en charge le Wi‑Fi MLO (Multi-Link Operation), qui combine plusieurs réseaux sans fil simultanément pour offrir une bande passante plus élevée et des connexions plus fiables.

Pour configurer le Wi‑Fi, consultez [Wireless](../../interface_guide/wireless.md).

## Clients

La page Clients affiche les informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d’envoi, le trafic total, et permet également de bloquer le client ou d’effectuer d’autres actions.

Pour configurer les Clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    Le service de gestion cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d’accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une fonctionnalité réseau avancée intégrée aux routeurs GL.iNet. Elle permet un accès à distance fluide à votre réseau domestique sans inscription ni connexion. En utilisant le protocole AmneziaWG avec obfuscation de trafic intégrée, elle maintient une connexion stable et sécurisée, ce qui en fait une solution idéale pour un accès à distance fiable, où que vous soyez. Les utilisateurs peuvent configurer un réseau AstroWarp directement depuis le panneau d’administration du routeur GL.iNet. Il suffit d’appairer vos routeurs à l’aide d’un code d’accès pour connecter en toute sécurité votre routeur de voyage à votre réseau domestique en quelques secondes.
    
    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d’accéder à un réseau distant (serveur VPN). Le Slate 7 Pro prend en charge OpenVPN et WireGuard.

=== "OpenVPN"

    Le Slate 7 Pro (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Le Slate 7 Pro (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d’excellentes vitesses et une utilisation pratique. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple cellular, repeater et ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Un LAN, ou réseau local, est un réseau qui relie des ordinateurs et des appareils dans une zone géographique limitée, telle qu’un domicile ou un bureau. Il permet un transfert de données à grande vitesse et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Cette fonction vous permet de définir un sous-réseau dans les plages d’adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de la passerelle et du masque réseau, et de configurer des paramètres de sécurité comme l’isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d’activer la protection contre les attaques DNS rebinding et de remplacer les paramètres DNS de tous les clients, d’autoriser le DNS personnalisé à remplacer le DNS du VPN, et de configurer le mode des paramètres du serveur DNS sur automatique ou de spécifier manuellement les serveurs DNS de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Port Ethernet"

    La page Ethernet Port vous permet de configurer les ports WAN et LAN, de définir l’interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l’adresse MAC de l’interface WAN, et d’afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d’adressage bien plus vaste, permettant un nombre quasiment illimité d’adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d’appareils connectés à Internet.
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    L’IGMP snooping est une technique d’optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer l’IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Mode réseau"

    Le mode réseau désigne les paramètres de configuration qui déterminent comment un appareil se connecte à un réseau et communique avec d’autres appareils.
    
    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "Passerelle Drop-in"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment avec AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, consultez les liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accélération réseau"

    L’accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer l’accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle du flux

=== "DPI Engine"

    Le DPI (Deep Packet Inspection) est une capacité essentielle de la gestion réseau intelligente. Il permet de dépasser les limites des routeurs traditionnels (qui n’identifient que les adresses source ou de destination), d’analyser en profondeur le contenu des paquets de données et d’identifier avec précision les applications et sites web consultés par l’utilisateur grâce à la comparaison avec une base de signatures, ce qui permet une classification et un contrôle affinés du trafic.
    
    Intégrée à [Netify](https://www.netify.ai/){target="_blank"}, la fonction DPI de GL.iNet utilise un plug-in embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, elle permet une gestion fiable et rend le contrôle du réseau plus précis et plus efficace.

    Veuillez consulter [DPI Engine](../../interface_guide/dpi_engine.md) pour des instructions détaillées.

=== "Statistiques des données"

    Statistiques des données offre un tableau de bord intelligent de visibilité du trafic qui catégorise et visualise l’utilisation du réseau par application, afin de vous aider à suivre le trafic en temps réel et historique pour une meilleure visibilité et un meilleur contrôle du réseau.

    Veuillez consulter [Statistiques des données](../../interface_guide/data_statistics.md) pour des instructions détaillées.

=== "Filtrage du contenu"

    Filtrage du contenu offre une protection intelligente en ligne basée sur la classification DPI, en bloquant automatiquement les sites nuisibles ou malveillants afin de garder votre réseau propre et sécurisé.

    Veuillez consulter [Filtrage du contenu](../../interface_guide/content_filter.md) pour des instructions détaillées.

---

=== "Contrôle parental"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d’écran et de restreindre l’accès à certains contenus.

    Pour configurer le contrôle parental, consultez [Contrôle parental](../../interface_guide/parental_control.md).

=== "QoS"

    La QoS (Quality of Service) optimise l’allocation de bande passante en priorisant les activités critiques (par exemple les appels vidéo et les jeux) lors de la congestion du réseau, réduisant ainsi la latence et améliorant les performances globales du réseau. Notez que cela s’applique au trafic des clients locaux et au trafic du tunnel client VPN, mais pas au trafic reçu lorsque le routeur fonctionne comme serveur VPN.

    Veuillez consulter [QoS](../../interface_guide/qos.md) pour des instructions détaillées.

=== "SQM"

    Le SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur afin de minimiser la latence et le « bufferbloat », pour des jeux en ligne et des appels vocaux plus fluides.

    Veuillez consulter [SQM](../../interface_guide/sqm.md) pour des instructions détaillées.

## Sécurité

=== "Redirection de port"

    La redirection de port permet aux serveurs distants et aux appareils sur Internet d’accéder aux appareils d’un réseau privé.
    
    Pour configurer la redirection de port, consultez [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Contrôle de gestion"

    Le contrôle de gestion vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Contrôle d’accès local : gérez et limitez l’accès à l’interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d’accès à distance : configurez et limitez l’accès à l’interface du routeur depuis des emplacements distants sur Internet, afin de renforcer la sécurité contre les menaces externes.
    * Open Ports on Router : contrôlez quels ports sont ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils qui y sont connectés.

    Veuillez consulter [Security](../../interface_guide/security.md) pour des instructions détaillées.

=== "Mode NAT"

    La page NAT Mode vous permet d’activer ou de désactiver Full Cone NAT et la fonctionnalité SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctions spécifiques à un programme existant, ce qui permet d’en personnaliser et d’en enrichir les capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte automatiquement et met à jour en temps réel l’adresse IP associée à un domaine. Il est particulièrement utile pour les utilisateurs qui ont besoin d’une adresse IP statique pour accéder à un réseau distant.
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution de stockage centralisée qui permet à plusieurs utilisateurs et appareils d’accéder à des fichiers et de les partager via un réseau.
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l’échelle du réseau. Elle agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d’accéder à vos appareils et à vos applications où que vous soyez.
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, en connectant les appareils comme s’ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet une communication anonyme sur Internet. Il achemine le trafic Internet à travers une série de serveurs bénévoles (nœuds) afin de masquer la localisation et l’utilisation de l’utilisateur, ce qui rend les activités en ligne difficiles à retracer.
    
    * [Comment configurer Tor](../../interface_guide/tor.md)

## Système

=== "Vue d’ensemble"

    La page Overview fournit un aperçu complet de l’état actuel et des performances de votre routeur. Sur cette page, vous pouvez consulter :

    * Charge moyenne du CPU : surveillez la charge moyenne du processeur de votre routeur pour évaluer les performances et identifier d’éventuels goulots d’étranglement.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire utilisée afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l’appareil.
    * Utilisation de la mémoire flash : affichez l’occupation du stockage flash du routeur afin de vérifier qu’il reste suffisamment d’espace pour le firmware et les données de configuration.
    * Informations sur l’appareil : accédez aux informations détaillées du système, notamment la durée de fonctionnement, le nom d’hôte, le modèle, l’architecture, la version d’OpenWrt, la version du noyau, l’ID de l’appareil, la MAC de l’appareil et le S/N de l’appareil.
    * Stockage externe : vérifiez l’état des périphériques de stockage externes connectés au routeur, comme les clés USB ou les cartes TF.
    
    Ces fonctions fournissent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez consulter [Vue d’ensemble](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Mot de passe administrateur"

    La page Admin Password vous permet de définir ou de modifier le mot de passe de l’interface d’administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour des raisons de sécurité, nous vous recommandons d’activer **Prevent Weak Password**.

    Lorsque **Prevent Weak Password** est activé, les exigences pour les nouveaux mots de passe sont les suivantes.

    * 5 caractères minimum et 63 caractères maximum.
    * Les lettres (sensibles à la casse), les chiffres et les symboles `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sont autorisés.
    * Au moins deux des catégories suivantes sont requises : lettres majuscules, lettres minuscules, chiffres et symboles.

    Veuillez consulter [Admin Password](../../interface_guide/admin_password.md) pour des instructions détaillées.

=== "Mise à niveau"

    La page Upgrade permet de mettre à jour le firmware de votre routeur vers la dernière version afin d’améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à niveau :

    * Firmware Online Upgrade : vérifie et installe automatiquement la dernière version du firmware directement depuis le serveur du fabricant, ce qui simplifie le processus de mise à jour.
    * Firmware Local Upgrade : permet de téléverser manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous donne plus de contrôle sur la version et le moment de la mise à niveau.

    Ces options vous permettent de garder votre routeur à jour avec les dernières améliorations et correctifs.

    Veuillez consulter [Upgrade](../../interface_guide/upgrade.md) pour des instructions détaillées.

---

=== "Tâches planifiées"

    La page Scheduled Tasks vous permet d’automatiser diverses fonctions du routeur selon une planification prédéfinie, afin d’améliorer la commodité et l’efficacité. Les principales fonctions de cette page sont les suivantes :

    * Planification de l’écran LCD : définissez une plage horaire pour allumer ou éteindre automatiquement l’écran LCD du routeur, afin de réduire la pollution lumineuse à certains moments.
    * Redémarrage planifié : configurez le routeur pour qu’il redémarre automatiquement à des intervalles définis, afin de maintenir des performances et une stabilité optimales.
    * Planification de l’état du Wi‑Fi : définissez une plage horaire pour contrôler les bandes Wi‑Fi 6 GHz / 5 GHz / 2,4 GHz / MLO, afin de mieux gérer la disponibilité du réseau et la consommation d’énergie.
    
    Ces options de planification vous offrent un contrôle accru sur le fonctionnement de votre routeur afin qu’il réponde mieux à vos besoins et à vos préférences.

    Veuillez consulter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.
    
=== "Gestion de l’affichage"

    La page Display Management vous offre un ensemble complet de fonctions pour gérer l’écran tactile et les paramètres associés.

    ‒ Fond d’écran : personnalisez le fond d’écran et le style de réveil de l’écran.
    ‒ Luminosité : ajustez la luminosité de l’écran tactile. Utilisez le curseur ou saisissez un pourcentage précis pour l’adapter à différentes conditions d’éclairage.
    ‒ Verrouillage automatique : définissez le délai avant le verrouillage automatique de l’écran en cas d’inactivité. La plage va de 1 minute à 30 minutes.
    ‒ Écran toujours activé : activez ou désactivez cette option pour décider si l’écran tactile reste allumé en continu ou s’éteint après une période d’inactivité.
    ‒ Activer le code d’accès de l’écran : définissez un code pour l’écran tactile afin d’ajouter une couche de sécurité supplémentaire.

    Veuillez consulter [Gestion de l’affichage](../../interface_guide/display_management.md) pour des instructions détaillées.

=== "Fuseau horaire"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements exacts et pour le bon fonctionnement des configurations basées sur le temps.

    Veuillez consulter [Fuseau horaire](../../interface_guide/time_zone.md) pour des instructions détaillées.

---

=== "Paramètres du bouton à bascule"

    La page Toggle Button Settings vous permet de configurer le bouton à bascule physique du routeur, afin de lui attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonction offre des raccourcis pratiques vers des tâches et des paramètres fréquents, ce qui améliore l’expérience utilisateur et simplifie la gestion du routeur.

    Veuillez consulter [Paramètres du bouton à bascule](../../interface_guide/toggle_button_settings.md) pour des instructions détaillées.

=== "Réinitialisation du firmware"

    La page Reset Firmware vous permet de réinitialiser la version actuelle du firmware de votre routeur à ses paramètres par défaut, en supprimant toutes les configurations personnalisées. Ce processus rétablit les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir sur une base propre avec la configuration par défaut du firmware actuel.

    Veuillez consulter [Réinitialisation du firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

=== "Journal"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau système.
    * Journal du noyau : journaux liés au fonctionnement et aux événements du noyau.
    * Journal des plantages : enregistrements des plantages système et des erreurs, utiles pour diagnostiquer les problèmes critiques.
    * Journal cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s’il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, la page propose un bouton Export Log qui vous permet d’exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Journal](../../interface_guide/log.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Advanced Settings donne accès aux options de configuration avancées via l’interface OpenWrt LuCI, ce qui permet aux utilisateurs expérimentés d’ajuster finement les paramètres et les fonctionnalités de leur routeur au-delà des options de l’interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d’autres personnalisations avancées du système.

    Veuillez consulter [Paramètres avancés](../../interface_guide/advanced_settings.md) pour des instructions détaillées.
