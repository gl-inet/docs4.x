# Guide d'utilisation de Brume 3 (GL-MT5000)

## Aperçu du produit

Brume 3 (GL-MT5000) est une passerelle de sécurité hautes performances fonctionnant sous OpenWrt v21.02, équipée d'un processeur MediaTek Cortex-A53 quadricœur, de 1 Go de RAM et de 8 Go de stockage eMMC pour l'extension par plug-ins. Son design compact est idéal pour les déploiements dans des espaces restreints. Il prend en charge l'hébergement VPN à domicile, le SD-WAN site-to-site, ainsi que plus de 30 services VPN pour une connectivité sécurisée entre différents sites. En outre, il intègre la fonction DPI de GL.iNet, ainsi que le contrôle parental et AdGuard Home, afin de répondre aux besoins variés des passionnés de technologie et des utilisateurs professionnels.

![gl-mt5000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/hardware_info/mt5000_interface.png){class="glboxshadow"}

## Contenu du colis

- 1 x Brume 3 (GL-MT5000)
- 1 x Adaptateur secteur
- 1 x Câble Ethernet
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Convertisseur (selon votre pays de livraison)

Regardez ci-dessous la vidéo de déballage du Brume 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PupxjK_u8O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Comment configurer Brume 3

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwbdUy79WHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre Brume 3 puis sur une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil filaire (par exemple un ordinateur de bureau ou un ordinateur portable) au port LAN du Brume 3 à l'aide d'un câble Ethernet.

### 3. Se connecter au panneau d'administration web

**Remarque :** Les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet.

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 4. Configuration de la connexion Internet

Configurez votre Brume 3 en utilisant l'une des méthodes de connexion Internet prises en charge : Ethernet, Tethering et Cellular (optionnel). Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_ethernet.png){class="glboxshadow"}

    Connectez le port WAN du Brume 3 à un appareil en amont (par ex. un modem) à l'aide d'un câble Ethernet.

    Une fois le Brume 3 connecté avec succès à Internet, un point vert apparaîtra à côté de "Ethernet" sur la page INTERNET du panneau d'administration web, et la LED physique du Brume 3 deviendra blanche fixe.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt5000/internet/mt5000_tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile au port USB Type-C du Brume 3 à l'aide d'un câble de données USB 3.0.
    2. Dans les paramètres de votre appareil mobile, activez le partage de connexion USB.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section "Tethering".

    Une fois le Brume 3 connecté avec succès à Internet, un point vert apparaîtra à côté de "Tethering" sur la page INTERNET du panneau d'administration web, et la LED physique du Brume 3 deviendra blanche fixe.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    Un câble adaptateur USB-C vers USB-A supplémentaire est requis pour cette méthode de connexion.

    Branchez un modem USB cellulaire sur le port USB Type-C du Brume 3 à l'aide d'un câble adaptateur USB-C vers USB-A supplémentaire. Cela permet de partager la connexion Internet d'un modem USB avec tous les appareils clients connectés.

    Une fois le Brume 3 connecté avec succès à Internet, un point vert apparaîtra à côté de "Cellular" sur la page INTERNET du panneau d'administration web, et la LED physique du Brume 3 deviendra blanche fixe.

    Veuillez consulter [Connexion à Internet via un réseau cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

---

Vous trouverez ci-dessous un aperçu des fonctionnalités disponibles dans le panneau d'administration web du Brume 3.

## Clients

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet également de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    Le service de gestion Cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.

    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Conçue spécialement pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils sur l'ensemble du réseau, y compris les appareils de niveau supérieur et inférieur. Axée sur la gestion à l'échelle du réseau et sur une future prise en charge du contrôle matériel, AstroWarp fournit une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.

    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Le Brume 3 prend en charge OpenVPN et WireGuard.

=== "OpenVPN"

    Brume 3 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Brume 3 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui permet de configurer le routeur avec plusieurs connexions Internet simultanées (par ex. cellular, repeater et ethernet). Si votre connexion Internet actuelle tombe en panne, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Le LAN, ou réseau local, est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme une maison ou un bureau. Il permet des transferts de données rapides et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.

    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

=== "DNS"

    La page DNS permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS et le remplacement des paramètres DNS de tous les clients, d'autoriser un DNS personnalisé à remplacer le DNS VPN, et de configurer le mode des paramètres DNS en automatique ou en saisissant manuellement des serveurs DNS provenant de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

---

=== "Port Ethernet"

    La page Ethernet Port permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet.

    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    L'IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast.

    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Mode réseau"

    Le mode réseau désigne les paramètres de configuration qui déterminent comment un appareil se connecte à un réseau et communique avec d'autres appareils.

    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "Passerelle Drop-in"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment avec AdGuard Home, le DNS chiffré et le client VPN.

    Pour configurer Drop-in Gateway, consultez les liens suivants :

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accélération réseau"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.

    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle du flux

=== "DPI Engine"

    Le DPI (Deep Packet Inspection) est une capacité essentielle de la gestion réseau intelligente. Il permet de dépasser les limites des routeurs traditionnels (qui n'identifient que les adresses source ou de destination), d'analyser en profondeur le contenu des paquets de données et d'identifier avec précision les applications et sites web consultés par l'utilisateur grâce à la comparaison avec une base de signatures, ce qui permet une classification et un contrôle affinés du trafic.

    Intégrée à [Netify](https://www.netify.ai/){target="_blank"}, la fonction DPI de GL.iNet utilise un plug-in embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, elle permet une gestion fiable et rend le contrôle du réseau plus précis et plus efficace.

    Veuillez consulter [DPI Engine](../../interface_guide/dpi_engine.md) pour des instructions détaillées.

=== "Statistiques des données"

    Statistiques des données offre un tableau de bord intelligent de visibilité du trafic qui catégorise et visualise l'utilisation du réseau par application, afin de vous aider à suivre le trafic en temps réel et historique pour une meilleure visibilité et un meilleur contrôle du réseau.

    Veuillez consulter [Statistiques des données](../../interface_guide/data_statistics.md) pour des instructions détaillées.

=== "Filtrage du contenu"

    Filtrage du contenu offre une protection intelligente en ligne basée sur la classification DPI, en bloquant automatiquement les sites nuisibles ou malveillants afin de garder votre réseau propre et sécurisé.

    Veuillez consulter [Filtrage du contenu](../../interface_guide/content_filter.md) pour des instructions détaillées.

---

=== "Contrôle parental"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre l'accès à certains contenus.

    Pour configurer le contrôle parental, consultez [Contrôle parental](../../interface_guide/parental_control.md).

=== "QoS"

    La QoS (Quality of Service) optimise l'allocation de bande passante en priorisant les activités critiques (par exemple les appels vidéo et les jeux) lors de la congestion du réseau, réduisant ainsi la latence et améliorant les performances globales du réseau. Notez que cela s'applique au trafic des clients locaux et au trafic du tunnel client VPN, mais pas au trafic reçu lorsque le routeur fonctionne comme serveur VPN.

    Veuillez consulter [QoS](../../interface_guide/qos.md) pour des instructions détaillées.

=== "SQM"

    Le SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur afin de minimiser la latence et le « bufferbloat », garantissant des jeux et des appels vocaux plus fluides.

    Veuillez consulter [SQM](../../interface_guide/sqm.md) pour des instructions détaillées.

## Sécurité

=== "Redirection de ports"

    La redirection de port permet à des serveurs et appareils distants sur Internet d'accéder à des appareils situés sur un réseau privé.

    Pour configurer la redirection de ports, consultez [Redirection de ports](../../interface_guide/port_forwarding.md).

=== "Contrôle de gestion"

    Contrôle de gestion vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Contrôle d'accès local : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la sécurité contre les menaces externes.
    * Ports ouverts sur le routeur : contrôlez quels ports sont ouverts sur le routeur, afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé et à protéger à la fois le routeur et les appareils connectés.

    Veuillez consulter [Sécurité](../../interface_guide/security.md) pour des instructions détaillées.

=== "Mode NAT"

    La page Mode NAT vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [Mode NAT](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant ainsi de le personnaliser et d'en étendre les capacités.

    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est particulièrement utile aux utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant.

    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder à des fichiers et de les partager via un réseau.

    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traceurs à l'échelle du réseau qui agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés au réseau domestique.

    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier est une solution réseau définie par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, reliant les appareils comme s'ils se trouvaient sur le même réseau local.

    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications partout.

    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet des communications anonymes sur Internet. Il achemine le trafic Internet via une série de serveurs bénévoles (nœuds) afin de masquer l'emplacement et l'usage de l'utilisateur, rendant les activités en ligne difficiles à tracer.

    * [Comment configurer Tor](../../interface_guide/tor.md)

## Système

=== "Aperçu"

    La page Overview fournit une vue d'ensemble complète de l'état actuel du routeur et de ses performances. Sur cette page, vous pouvez voir :

    * Charge moyenne du CPU : surveillez la charge moyenne du CPU du routeur afin d'évaluer les performances et d'identifier d'éventuels goulots d'étranglement.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire utilisée sur le routeur afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser ses indicateurs visuels.
    * Utilisation du stockage flash : consultez l'utilisation de la mémoire flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez à des informations détaillées sur le système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC et le numéro de série.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, comme les clés USB ou les cartes TF.

    Ces fonctionnalités offrent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement du routeur.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Overview](../../interface_guide/system_overview.md).

=== "Mot de passe administrateur"

    La page Admin Password vous permet de définir ou de modifier le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour des raisons de sécurité, nous vous recommandons d'activer **Prevent Weak Password**.

    Lorsque **Prevent Weak Password** est activé, les exigences applicables aux nouveaux mots de passe sont les suivantes.

    * Minimum 5 caractères et maximum 63 caractères.
    * Les lettres (sensibles à la casse), les chiffres et les symboles `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sont autorisés.
    * Au moins deux catégories parmi lettres majuscules, lettres minuscules, chiffres et symboles sont requises.

=== "Mise à niveau"

    La page Upgrade sert à mettre à jour le firmware du routeur vers la dernière version, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : vérifie et installe automatiquement la dernière version du firmware depuis le serveur du fabricant, ce qui simplifie la mise à jour.
    * Firmware Local Upgrade : permet de téléverser manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous laisse le contrôle sur la version et le moment de la mise à jour.

    Ces options vous permettent de maintenir le routeur à jour avec les dernières améliorations et correctifs.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Upgrade](../../interface_guide/upgrade.md).

---

=== "Tâches planifiées"

    La page Scheduled Tasks permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, afin d'améliorer le confort d'utilisation et l'efficacité. Les principales fonctionnalités de cette page incluent :

    * Planification de l'affichage LED : définissez un calendrier pour allumer ou éteindre automatiquement les voyants LED du routeur, afin de réduire la pollution lumineuse à certains moments.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis, afin de préserver des performances et une stabilité optimales.

    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur, afin qu'il réponde à vos besoins et préférences spécifiques.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Fuseau horaire"

    La page Time Zone permet de définir le fuseau horaire correct pour le routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements exacts et pour assurer l'exécution correcte des configurations basées sur le temps.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Time Zone](../../interface_guide/time_zone.md).

=== "Journal"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau système.
    * Journal du noyau : journaux liés aux opérations et événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Journal cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.

    En outre, cette page propose un bouton Export Log, qui permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Log](../../interface_guide/log.md).

---

=== "Réinitialiser le firmware"

    La page Reset Firmware permet de réinitialiser la version actuelle du firmware du routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Paramètres avancés"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, ce qui permet aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de base de l'interface. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées et plus d'informations, veuillez consulter [Advanced Settings](../../interface_guide/advanced_settings.md).
