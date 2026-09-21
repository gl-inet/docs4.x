# Guide de l'utilisateur de Fortify (GL-MT6000)

## Présentation du produit

Fortify (GL-MT6000) est un routeur Wi-Fi 6 co-marqué publié conjointement par GL.iNet et ExpressVPN. Chaque unité est livrée avec un abonnement ExpressVPN gratuit d'un an. Les utilisateurs peuvent utiliser l'abonnement et connecter leurs comptes directement sur le panneau d'administration Web du routeur. Une fois activé, tout le trafic passant par le routeur exploitera le réseau haut débit d'ExpressVPN et le cryptage robuste pour protéger l'ensemble de votre connexion réseau et votre confidentialité en ligne.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Comment configurer Fortify

### 1. Allumer

Assemblez l'adaptateur secteur en deux parties. Connectez-le à votre routeur Fortify et branchez-le sur une prise. Il démarrera automatiquement.

### 2. Connecter l'appareil

Connectez un appareil (par exemple, un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi-Fi ou Ethernet.

-Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, localisez le nom du réseau Wi-Fi de votre routeur dans la liste des réseaux disponibles et saisissez le mot de passe pour rejoindre le réseau. Vous pouvez trouver le nom de réseau et le mot de passe par défaut imprimés sur l'étiquette du routeur.

### 3. Connectez-vous au panneau d'administration Web

Ouvrez un navigateur Web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue dans le coin supérieur droit, définissez votre mot de passe administrateur, puis cliquez sur **Next**. Le mot de passe doit comporter entre 10 et 63 caractères et contenir au moins deux des éléments suivants : des lettres majuscules, des lettres minuscules, des chiffres et des symboles spéciaux.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configurez votre Wi-Fi. Veuillez noter que si vous modifiez les informations Wi‑Fi, vous devrez reconnecter votre appareil au Wi‑Fi du routeur à l'aide des informations d'identification mises à jour.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configuration Internet

**Remarque :** les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur depuis le panneau d'administration Web de GL.iNet. Si vous préférez l'[application GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, téléchargez-la et suivez les instructions affichées.

Configurez votre Fortify à l'aide de l'une des méthodes de connexion Internet prises en charge : Ethernet, répéteur, partage de connexion et cellulaire. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plusieurs connexions Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Connectez un câble Ethernet entre le port WAN de votre routeur Fortify et un périphérique en amont tel qu'un modem.

    Une fois connecté avec succès à Internet, le voyant du routeur devient blanc fixe.

    Veuillez vous référer à [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Sur le panneau d'administration Web, accédez à la section INTERNET -> Répéteur et cliquez sur **Connect**.
    2. Sélectionnez un Wi-Fi parmi les réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.

    Une fois connecté avec succès à Internet, le voyant du routeur devient blanc fixe.

    Veuillez vous référer à [Connexion à Internet via un réseau Wi-Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Connectez votre smartphone au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre smartphone, accédez à Paramètres et activez le partage de connexion USB. Pour iPhone, faites confiance à cet appareil et activez Personal Hotspot.
    3. Sur le panneau d'administration Web, accédez à la section INTERNET -> Partage de connexion et cliquez sur **Connect**.

    Une fois connecté avec succès à Internet, le voyant du routeur devient blanc fixe.

    Veuillez vous référer à [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du routeur. Ceci est utile pour partager Internet depuis un modem USB vers tous les appareils connectés.

    Une fois connecté avec succès à Internet, le voyant du routeur devient blanc fixe.

    Veuillez vous référer à [Connexion à Internet via cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

---

Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d'administration Web Fortify.

## Sans fil

La page Sans fil vous permet de configurer les réseaux Wi-Fi de Fortify, y compris le réseau principal, le réseau invité et le réseau IoT. Chaque réseau prend en charge les bandes 2,4 GHz et 5 GHz.

Pour configurer le sans fil, reportez-vous à [Sans fil](../../interface_guide/wireless.md).

## Clients

La page Clients affiche des informations sur les appareils connectés, notamment le nom de l'appareil, le type de connexion, les adresses IP et MAC, les vitesses de téléchargement et de téléchargement, le trafic, et offre la possibilité de bloquer un client spécifique en un seul clic ou d'effectuer d'autres actions.

Veuillez vous référer à [Clients](../../interface_guide/clients.md) pour plus de détails.

## Services cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} fournit un moyen simple et facile d'accéder et de gérer à distance vos routeurs GL.iNet.

    Veuillez vous référer à [GoodCloud](../../interface_guide/cloud.md) pour plus de détails.

=== "AstroWarp"

    AstroWarp est une fonctionnalité conçue pour une mise en réseau à distance transparente sur les routeurs GL.iNet. Il adopte le protocole AmneziaWG avec obscurcissement du trafic intégré, offrant un accès à distance stable et sécurisé à tout moment et en tout lieu.

    Veuillez vous référer à [AstroWarp](../../interface_guide/astrowarp.md) pour plus de détails.

## VPN

Un VPN (réseau privé virtuel) établit des tunnels de trafic sécurisés et cryptés entre votre appareil local et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité au client VPN et permet d'accéder au réseau du serveur VPN distant.

Fortify s'intègre à [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, vous permettant d'activer une connexion ExpressVPN en quelques minutes. Chaque appareil Fortify est livré avec un abonnement ExpressVPN gratuit d'un an. Vous pouvez utiliser l'abonnement et connecter votre compte ExpressVPN directement sur le panneau d'administration Web du routeur. Une fois la connexion VPN activée, tout le trafic acheminé via le routeur utilisera les serveurs haut débit d'ExpressVPN et un cryptage robuste pour sécuriser l'ensemble de votre réseau et votre confidentialité en ligne.

Pour bénéficier d'un abonnement gratuit et configurer un tunnel VPN, reportez-vous au [Guide d'activation ExpressVPN](../../interface_guide/expressvpn_activation_guide.md).

Pour configurer un serveur OpenVPN, reportez-vous à [OpenVPN Server](../../interface_guide/openvpn_server.md).

Pour configurer un serveur WireGuard, reportez-vous à [WireGuard Server](../../interface_guide/wireguard_server.md).

## Réseau

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple, cellulaire, répéteur et Ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur passera automatiquement à une autre connexion Internet. Cela garantit un accès Internet fluide et ininterrompu.

Veuillez vous référer à [Multi-WAN](../../interface_guide/multi-wan.md) pour plus de détails.

=== "LAN"

    Un LAN, ou Local Area Network, est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme une maison ou un bureau. Il s'agit du réseau local auquel votre appareil rejoint lorsqu'il est connecté au Wi-Fi principal ou via un câble Ethernet. La page LAN couvre les paramètres de base, les paramètres du serveur DHCP et la réservation d'adresse.

    Veuillez vous référer à [LAN](../../interface_guide/lan.md) pour plus de détails.

=== "Guest Network"

    La page Réseau invité vous permet de créer un réseau Wi-Fi dédié aux visiteurs. Isolé du réseau principal, il renforce la sécurité tout en offrant un accès Internet pratique. Vous pouvez définir un sous-réseau invité dans les plages d'adresses privées IPv4 `192.168.0.0/16`, `172.16.0.0/12` ou `10.0.0.0/8`, spécifier les adresses IP de la passerelle et du masque de réseau.

    Veuillez vous référer à [Réseau invité](../../interface_guide/guest_network.md) pour plus de détails.

=== "IoT Network"

    La page Réseau IoT vous permet de créer un réseau Wi-Fi dédié aux appareils IoT. Isolé du réseau principal, il offre une meilleure compatibilité et une sécurité améliorée.

    Veuillez vous référer à [Réseau IoT](../../interface_guide/iot_network.md) pour plus de détails.

<br>

=== "DNS"

    Les paramètres DNS de votre routeur contrôlent la manière dont les noms de domaine sont traduits en adresses IP. Cette page vous permet d'utiliser le(s) serveur(s) DNS automatiquement obtenus à partir des appareils en amont, ou d'en définir des personnalisés, et de configurer les priorités DNS.

    Veuillez vous référer à [DNS](../../interface_guide/dns.md) pour plus de détails.

=== "Ethernet Port"

    La page Port Ethernet vous permet de gérer les rôles de port Ethernet (WAN/LAN) et d'afficher les détails du port tels que l'adresse MAC et la vitesse négociée.

    Veuillez vous référer à [Port Ethernet](../../interface_guide/ethernet_port.md) pour plus de détails.

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Il fournit un espace d'adressage beaucoup plus grand, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour s'adapter au nombre croissant d'appareils connectés à Internet.

    Veuillez vous référer à [IPV6](../../interface_guide/network_mode.md) pour plus de détails.

=== "IGMP Snooping"

    La surveillance IGMP est une technique d'optimisation du réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic de multidiffusion.

    Veuillez vous référer à [IGMP Snooping](../../interface_guide/igmp_snooping.md) pour plus de détails.

<br>

=== "Network Mode"

    Le mode réseau fait référence aux paramètres de configuration qui déterminent la manière dont un appareil se connecte à un réseau et communique avec d'autres appareils.

    Pour configurer le mode réseau, reportez-vous à [Mode réseau](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctionnalités qu'il n'a peut-être pas, notamment AdGuard Home, DNS crypté et VPN.

    Pour configurer une passerelle d'accès direct, reportez-vous à [Comment configurer une passerelle d'accès direct](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    L'accélération du réseau peut réduire la charge du processeur et accélérer le transfert des paquets de trafic.

    Pour configurer l'accélération réseau, reportez-vous à [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle de flux

=== "DPI Engine"

DPI (Deep Packet Inspection) est une fonctionnalité essentielle de la gestion intelligente des réseaux. Il peut surmonter les limites des routeurs traditionnels (qui identifient uniquement les adresses source ou de destination), analyser en profondeur les charges utiles des paquets de données et identifier avec précision les applications et les sites Web accessibles par les utilisateurs grâce à une comparaison de bibliothèques de fonctionnalités, permettant une classification et un contrôle affinés du trafic.

    Intégrée à [Netify](https://www.netify.ai/){target="_blank"}, la fonctionnalité GL.iNet DPI adopte un plug-in intégré léger pour un déploiement efficace. Avec la base de données de signatures mise à jour en ligne de Netify, il permet une gestion fiable, rendant le contrôle du réseau plus précis et efficace.

    Veuillez vous référer à [Moteur DPI](../../interface_guide/dpi_engine.md) pour plus de détails.

=== "Data Statistics"

    Data Statistics propose un tableau de bord intelligent d'analyse du trafic qui catégorise et visualise l'utilisation du réseau par applications, vous aidant ainsi à surveiller le trafic en temps réel et historique pour une meilleure connaissance et un meilleur contrôle du réseau.

    Veuillez vous référer à [Statistiques des données](../../interface_guide/data_statistics.md) pour plus de détails.

=== "Content Filter"

    Content Filter offre une sécurité en ligne intelligente optimisée par une classification basée sur DPI, bloquant automatiquement les sites Web nuisibles ou malveillants pour maintenir votre réseau propre et sécurisé.

    Veuillez vous référer à [Filtre de contenu](../../interface_guide/content_filter.md) pour plus de détails.

<br>

=== "QoS"

    La QoS (Qualité de Service) optimise l'allocation de bande passante en donnant la priorité aux activités critiques (par exemple, les appels vidéo, les jeux) pendant la congestion du réseau, réduisant ainsi la latence et améliorant les performances globales du réseau. Notez que cela s'applique au trafic client local et au trafic du tunnel client VPN, mais pas au trafic reçu lorsque le routeur fonctionne comme serveur VPN.

    Veuillez vous référer à [QoS](../../interface_guide/qos.md) pour plus de détails.

=== "SQM"

    SQM (Smart Queue Management) gère intelligemment le trafic réseau de votre routeur pour minimiser la latence et le « bufferbloat », garantissant ainsi des jeux et des appels vocaux plus fluides.

    Veuillez vous référer à [SQM](../../interface_guide/sqm.md) pour plus de détails.

=== "Parental Control"

    Le contrôle parental est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Cela inclut la limitation de leur temps d’écran et la restriction de leur accès à certains contenus.

    Veuillez vous référer à [Contrôle parental](../../interface_guide/parental_control_v4.9.md) pour plus de détails.

## Sécurité

=== "Port forwarding"

    La redirection de port permet aux serveurs et appareils distants sur Internet d'accéder aux appareils sur un réseau privé.

    Veuillez vous référer à [Redirection de port](../../interface_guide/port_forwarding.md) pour plus de détails.

=== "ACL"

    ACL, abréviation de Access Control List, vous permet de créer des règles pour gérer le trafic réseau en fonction des protocoles de connexion, des adresses des appareils et des ports. Il contrôle s’il faut autoriser ou bloquer l’accès au réseau. Si plusieurs règles ACL entrent en conflit, le système applique celle ayant la priorité la plus élevée.

    Veuillez vous référer à [ACL](../../interface_guide/acl.md) pour plus de détails.

=== "Admin Access"

    L'accès administrateur vous permet de configurer divers paramètres de sécurité pour protéger votre réseau et votre routeur contre tout accès non autorisé. Cette page comprend les options suivantes :

    * Contrôle d'accès : gérez et restreignez l'accès à l'interface du routeur à partir des appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur à partir d'emplacements distants via Internet, améliorant ainsi la sécurité contre les menaces externes.
    * Ports ouverts sur le routeur : contrôlez les ports ouverts sur le routeur, limitant ainsi les vulnérabilités potentielles et les accès non autorisés.

    Veuillez vous référer à [Accès administrateur](../../interface_guide/admin_access.md) pour plus de détails.

=== "NAT Mode"

    La page Mode NAT vous permet d'activer ou de désactiver les fonctionnalités Full Cone NAT et SIP ALG (Application Layer Gateway).

    Veuillez vous référer à [Mode NAT](../../interface_guide/nat_settings.md) pour plus de détails.

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des caractéristiques ou des fonctionnalités spécifiques à un programme informatique existant, permettant la personnalisation et l'amélioration de ses capacités.

    Veuillez vous référer à [Plug-ins](../../interface_guide/plugins.md) pour plus de détails.

=== "Dynamic DNS"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement l'adresse IP associée à un domaine en temps réel. Il est utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant.

    Veuillez vous référer à [DNS dynamique](../../interface_guide/ddns.md) pour plus de détails.

=== "Network Storage"

    Le stockage réseau fait référence à une solution de stockage de données centralisée qui permet à plusieurs utilisateurs et appareils d'accéder et de partager des fichiers sur un réseau.

    Veuillez vous référer à [Stockage réseau](../../interface_guide/network_storage.md) pour plus de détails.

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des trackers à l'échelle du réseau qui agit comme un serveur DNS pour filtrer le contenu indésirable sur tous les appareils connectés à un réseau domestique.

    Veuillez vous référer à [AdGuard Home](../../interface_guide/adguardhome.md) pour plus de détails.

<br>

=== "Bark"

    Le service [Bark](https://www.bark.us/){target="_blank"} peut aider à protéger le monde numérique de votre enfant et fournir une protection en ligne complète. Cela nécessite généralement un abonnement payant. Cependant, dans le cadre du partenariat GL.iNet avec Bark, nous proposons gratuitement le plan Bark Home sur Fortify (GL-MT6000), offrant une surveillance et des alertes avancées sans frais supplémentaires.

    Veuillez vous référer à [Bark](../../interface_guide/bark.md) pour plus de détails.

=== "Tailscale"

    Tailscale est un service VPN qui rend les appareils et applications que vous possédez accessibles partout dans le monde, en toute sécurité et sans effort.

    Fortify (GL-MT6000) s'intègre à Tailscale, vous permettant de rejoindre le routeur dans un réseau virtuel Tailscale. Une fois connecté, vous pouvez y accéder à distance, y compris à ses ressources WAN et LAN.

    Veuillez vous référer à [Tailscale](../../interface_guide/tailscale.md) pour plus de détails.

=== "ZeroTier"

    ZeroTier est une solution de mise en réseau définie par logiciel qui permet aux utilisateurs de créer des réseaux virtuels sécurisés sur Internet, en connectant des appareils comme s'ils se trouvaient sur le même réseau local.

    Veuillez vous référer à [ZeroTier](../../interface_guide/zerotier.md) pour plus de détails.

=== "Tor"

    Tor (dérivé de The Onion Router) est un logiciel gratuit et open source permettant la communication anonyme. Il aide les utilisateurs à explorer Internet en toute confidentialité.

    Veuillez vous référer à [Tor](../../interface_guide/tor.md) pour plus de détails.

## Système

=== "Overview"

    La page Présentation fournit un aperçu complet de l'état actuel et des mesures de performances de votre routeur. Sur cette page, vous pouvez consulter :

    * Charge moyenne du processeur : surveillez la charge moyenne du processeur de votre routeur, aidant ainsi à évaluer les performances et à identifier les goulots d'étranglement potentiels.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire de votre routeur utilisée, ce qui facilite la gestion des ressources.
    * Contrôle LED : allumez ou éteignez les lumières LED du routeur, permettant ainsi de personnaliser les indicateurs visuels de l'appareil.
    * Utilisation du flash : affichez l'utilisation du stockage flash du routeur, en vous assurant qu'il y a suffisamment d'espace pour le micrologiciel et les données de configuration.
    * Informations sur l'appareil : accédez à des informations détaillées sur le système de votre routeur, notamment la disponibilité, le nom d'hôte, le modèle, l'architecture, la version OpenWrt, la version du noyau, l'ID de l'appareil, le MAC de l'appareil et le S/N de l'appareil.
    * Stockage externe : vérifiez l'état de tous les périphériques de stockage externes connectés au routeur, tels que les clés USB ou les cartes TF.

    Ces fonctionnalités fournissent des informations et des contrôles essentiels, vous aidant à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez vous référer à [Présentation](../../interface_guide/system_overview.md) pour plus de détails.

=== "Admin Password"

    La page Mot de passe administrateur vous permet de définir ou de modifier le mot de passe de l'interface d'administration du routeur.

    Veuillez vous référer à [Mot de passe administrateur](../../interface_guide/admin_password.md) pour plus de détails.

=== "Upgrade"

    La page Mise à niveau est utilisée pour mettre à jour le micrologiciel de votre routeur vers la dernière version, garantissant ainsi des performances, une sécurité et de nouvelles fonctionnalités améliorées. Cette page propose deux options :

    * Mise à niveau du micrologiciel en ligne : recherchez et installez automatiquement la dernière version du micrologiciel directement à partir du serveur du fabricant, simplifiant ainsi le processus de mise à jour.
    * Mise à niveau locale du micrologiciel : téléchargez manuellement un fichier de micrologiciel depuis votre ordinateur pour mettre à jour le routeur, permettant ainsi de contrôler la version et le calendrier de la mise à niveau.

    Veuillez vous référer à [Mise à niveau](../../interface_guide/upgrade.md) pour plus de détails.

=== "Scheduled Tasks"

    La page Tâches planifiées vous permet d'automatiser diverses fonctions du routeur en fonction d'un calendrier prédéfini, améliorant ainsi la commodité et l'efficacité. Les principales fonctionnalités de cette page incluent :

    * Programme d'affichage LED : définissez un programme pour allumer ou éteindre automatiquement les lumières LED du routeur, réduisant ainsi la pollution lumineuse à des heures spécifiques.
    * Planifier le redémarrage : configurez votre routeur pour qu'il redémarre automatiquement à des intervalles spécifiés, contribuant ainsi à maintenir des performances et une stabilité optimales.
    * Calendrier d'état Wi-Fi 5 GHz/2,4 GHz : définissez un calendrier pour contrôler la bande Wi-Fi 5 GHz/2,4 GHz, permettant une meilleure gestion de la disponibilité du réseau et de la consommation d'énergie.

    Ces options de planification vous offrent un meilleur contrôle sur les opérations de votre routeur, garantissant qu'il répond à vos besoins et préférences spécifiques.

    Veuillez vous référer à [Tâches planifiées](../../interface_guide/scheduled_tasks.md) pour plus de détails.

<br>

=== "Time Zone"

    La page Fuseau horaire vous permet de définir le fuseau horaire correct pour votre routeur, garantissant ainsi que toutes les tâches planifiées, les journaux et les événements système sont horodatés avec précision en fonction de votre heure locale. Ce paramètre est crucial pour conserver des enregistrements précis et pour la bonne exécution des configurations temporelles.

    Veuillez vous référer à [Fuseau horaire](../../interface_guide/time_zone.md) pour plus de détails.

=== "Reset Firmware"

La page Réinitialiser le micrologiciel vous permet de réinitialiser la version actuelle du micrologiciel de votre routeur à ses paramètres par défaut, effaçant ainsi toutes les configurations personnalisées. Ce processus restaurera le routeur aux paramètres par défaut de la version du micrologiciel actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou pour repartir à zéro avec la configuration par défaut du micrologiciel actuel.

    Veuillez vous référer à [Réinitialiser le micrologiciel](../../interface_guide/reset_firmware.md) pour plus de détails.

=== "Log"

    La page Journal permet d'accéder à divers journaux qui enregistrent les activités et les événements du routeur, facilitant le dépannage et la surveillance des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et des activités au niveau du système.
    * Journal du noyau : journaux liés aux opérations et aux événements du noyau.
    * Crash Log : enregistrements des pannes et des erreurs du système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : Journaux d'interactions et d'activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur Web Nginx, s'il est utilisé par le routeur, détaillant le trafic Web et les opérations du serveur.

    De plus, la page comporte un bouton Exporter le journal, vous permettant d'exporter tous les journaux collectés pour une analyse du support technique. Cette fonction est inestimable pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez vous référer à [Journal](../../interface_guide/log.md) pour plus de détails.

=== "Advanced Settings"

    La page Paramètres avancés donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'affiner les paramètres et les fonctionnalités de leur routeur au-delà des options d'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations avancées du système.

    Veuillez vous référer à [Paramètres avancés](../../interface_guide/advanced_settings.md) pour plus de détails.
