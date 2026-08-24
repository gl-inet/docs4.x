# Guide de l’utilisateur de Flint 4 (GL-BE14000)

## Présentation du produit

Flint 4 (GL‑BE14000) redéfinit les possibilités d’un routeur domestique. Il propose le Wi‑Fi 7 tri-bande avec MLO, avec des débits maximaux de 688 Mbit/s (2,4 GHz) + 4 323 Mbit/s (5 GHz) + 8 646 Mbit/s (6 GHz). Pour les connexions filaires, il dispose d’une infrastructure entièrement multi-gigabit comprenant un port WAN/LAN 10G SFP+, un port WAN/LAN 10GE, un port WAN/LAN 2,5GE, trois ports LAN 2,5GE et quatre ports LAN 1GE. Il prend en charge les VPN hautes performances et atteint jusqu’à 1,5 Gbit/s avec WireGuard® comme avec OpenVPN DCO. Son écran tactile de 2,4 pouces permet de surveiller l’état du réseau en temps réel et de consulter directement les principales données réseau sur l’appareil.

![be14000 interfaces](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/hardware/be14000_interfaces.png){class="glboxshadow"}

## Contenu de l’emballage

- 1 Flint 4 (GL-BE14000)
- 1 adaptateur secteur
- 1 câble Ethernet
- 1 manuel de l’utilisateur
- 1 carte de remerciement
- 1 convertisseur (selon le pays de livraison)

Regardez ci-dessous la vidéo de déballage de Flint 4.

<iframe width="560" height="315" src="https://www.youtube.com/embed/x48iKZaLaN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration de Flint 4

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N3zw02XGFSU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension

Assemblez les deux parties de l’adaptateur secteur. Branchez-le au routeur, puis sur une prise électrique. Le routeur démarre automatiquement.

### 2. Connexion d’un appareil

Connectez un appareil, par exemple un ordinateur, un ordinateur portable ou un smartphone, au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Reliez votre appareil au port LAN du routeur à l’aide d’un câble Ethernet.

- Wi-Fi

    Sur votre appareil, recherchez le nom du réseau Wi-Fi de votre routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous connecter. Le nom de réseau (SSID) et le mot de passe par défaut sont imprimés sur l’étiquette du routeur.

### 3. Connexion au panneau d’administration Web

Ouvrez un navigateur Web, saisissez `192.168.8.1` dans la barre d’adresse et connectez-vous. Définissez votre mot de passe administrateur et les paramètres Wi-Fi, puis cliquez sur **Apply**.

### 4. Configuration d’Internet

Configurez votre Flint 4 à l’aide de l’une des méthodes de connexion Internet prises en charge : Ethernet (SFP+), Ethernet (RJ45), Repeater, Tethering ou Cellular. Pour utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), configurez plusieurs connexions Internet.

=== "Ethernet (SFP+)"

    ![Ethernet SFP+](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_10g-sfp.png){class="glboxshadow"}

    Flint 4 dispose d’un port WAN/LAN 10G SFP+ conçu pour les liaisons montantes fibre, les liaisons haute vitesse vers un commutateur et l’extension de réseaux hautes performances. Ce port est configuré en WAN par défaut et peut être converti en LAN si nécessaire.

    L’exemple ci-dessous montre comment connecter le port 10G SFP+ de Flint 4 à la liaison montante fibre d’un FAI au moyen d’un émetteur-récepteur optique et d’un câble à fibre pour accéder à Internet. Pour découvrir d’autres solutions, consultez [Connexion du port 10G SFP+ de Flint 4](../../faq/connecting_10g_sfp_plus_port_on_flint4.md).

    1. Insérez un émetteur-récepteur 10G SFP+ compatible dans le port SFP+ de Flint 4, puis connectez-le à la liaison montante fibre de votre FAI.
    2. Flint 4 tente d’obtenir automatiquement les paramètres réseau (adresse IP, passerelle et DNS) via DHCP. Si votre FAI exige une connexion PPPoE ou une adresse IP statique, modifiez les paramètres de connexion WAN correspondants dans le panneau d’administration Web.
    3. Une fois la connexion à Internet établie, la section Ethernet de la page d’accueil de l’écran tactile devient bleue (active). Appuyez sur Ethernet sur l’écran tactile ou connectez-vous au panneau d’administration Web pour consulter les informations de connexion.

=== "Ethernet (RJ45)"

    ![Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_ethernet.png){class="glboxshadow"}

    1. Reliez le port WAN de Flint 4 à un appareil en amont, par exemple le modem du FAI, un commutateur réseau ou une prise Ethernet murale, à l’aide d’un câble Ethernet.
    2. Flint 4 tente d’obtenir automatiquement les paramètres réseau (adresse IP, passerelle et DNS) via DHCP. Si votre FAI exige une connexion PPPoE ou une adresse IP statique, modifiez les paramètres de connexion WAN correspondants dans le panneau d’administration Web.
    3. Une fois la connexion à Internet établie, la section Ethernet de la page d’accueil de l’écran tactile devient bleue (active). Appuyez sur Ethernet sur l’écran tactile ou connectez-vous au panneau d’administration Web pour consulter les informations de connexion.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_repeater.png){class="glboxshadow"}

    1. Appuyez sur **Repeater** sur l’écran tactile. Le routeur recherche les réseaux Wi-Fi disponibles.
    2. Sélectionnez le réseau Wi-Fi que Flint 4 doit étendre.
    3. Saisissez le mot de passe, puis appuyez sur **Apply**.
    4. Une fois la connexion à Internet établie, la section Repeater de la page d’accueil de l’écran tactile devient bleue (active). Appuyez sur Repeater sur l’écran tactile ou connectez-vous au panneau d’administration Web pour consulter les informations de connexion.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_tethering.png){class="glboxshadow"}

    1. Connectez un appareil mobile, par exemple un smartphone, au port USB de Flint 4 à l’aide d’un câble USB.
    2. Sur votre appareil mobile, accédez aux paramètres et activez **USB Tethering** ou **Personal Hotspot**. Sur un iPhone, appuyez sur **Trust This Device** si vous y êtes invité.
    3. Sur l’écran tactile de Flint 4, sélectionnez **Tethering**, puis appuyez sur **Connect**. Le routeur se connecte alors à votre appareil.
    4. Une fois la connexion à Internet établie, la section Tethering de la page d’accueil de l’écran tactile devient bleue (active). Appuyez sur Tethering sur l’écran tactile ou connectez-vous au panneau d’administration Web pour consulter les informations de connexion.

    **Remarque** : si la connexion échoue, vérifiez que l’alimentation fournit 12 V 4 A. Une alimentation insuffisante peut empêcher le port USB de fonctionner. Répétez les étapes ci-dessus ou connectez-vous au panneau d’administration Web pour vérifier l’état de la connexion Tethering.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be14000/internet/be14000_cellular.png){class="glboxshadow"}

    1. Branchez un modem cellulaire ou une clé USB sur le port USB de Flint 4. Cela permet de partager la connexion Internet d’un modem USB avec tous les appareils connectés.
    2. Une fois la connexion à Internet établie, la section Cellular de la page d’accueil de l’écran tactile devient bleue (active). Appuyez sur Cellular sur l’écran tactile ou connectez-vous au panneau d’administration Web pour consulter les informations de connexion.

---

Vous trouverez ci-dessous une présentation des fonctions du panneau d’administration Web de Flint 4.

## Sans fil

La page Wireless permet de configurer les différents réseaux Wi-Fi de Flint 4, notamment MLO Wi-Fi, Main Network, Guest Network et IoT Network.

Pour plus de détails, consultez [Sans fil](../../interface_guide/wireless.md).

## Clients

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les débits de téléchargement et de téléversement ainsi que le trafic total. Elle permet également de bloquer le client ou d’effectuer d’autres actions.

Pour plus de détails, consultez [Clients](../../interface_guide/clients.md).

## Services cloud

=== "GoodCloud"

    [GoodCloud](https://www.goodcloud.xyz){target="_blank"} de GL.iNet offre un moyen simple d’accéder à distance aux routeurs GL.iNet et de les gérer.

    Pour plus de détails, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une fonction réseau avancée intégrée aux routeurs GL.iNet. Elle permet d’accéder facilement à distance à votre réseau domestique sans inscription ni connexion. Grâce au protocole AmneziaWG avec obfuscation du trafic intégrée, elle assure une connexion stable et sécurisée, idéale pour un accès à distance fiable où que vous soyez. Vous pouvez configurer un réseau AstroWarp directement depuis le panneau d’administration du routeur GL.iNet. Il suffit d’associer les routeurs au moyen d’un code d’accès pour connecter en quelques secondes et en toute sécurité votre routeur de voyage à votre réseau domestique.

    Pour plus de détails, consultez [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Un VPN (réseau privé virtuel) crée un canal sécurisé et chiffré entre votre appareil et le serveur VPN. Il renforce la confidentialité et la sécurité avec un client VPN et permet d’accéder à un réseau distant avec un serveur VPN. Flint 4 prend en charge les protocoles OpenVPN et WireGuard.

=== "OpenVPN"

    Flint 4, comme les autres routeurs GL.iNet, prend en charge le protocole OpenVPN, qui offre une sécurité robuste. Pour configurer OpenVPN, consultez les tutoriels suivants :

    * [Configuration d’un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Configuration d’un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 4, comme les autres routeurs GL.iNet, prend en charge le protocole WireGuard, qui offre rapidité et simplicité. Pour configurer WireGuard, consultez les tutoriels suivants :

    * [Configuration d’un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Configuration d’un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau

=== "Multi-WAN"

    Multi-WAN permet de configurer simultanément plusieurs connexions Internet sur le routeur, par exemple Cellular, Repeater et Ethernet. Si la connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion afin de garantir un accès Internet fluide et ininterrompu.

    Pour plus de détails, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    La page Subnet centralise la gestion des réseaux LAN, Guest Network, IoT Network et des réseaux VLAN personnalisés. Elle permet de créer et de gérer plusieurs sous-réseaux afin d’isoler différents types d’appareils ou de trafic.

    Pour plus de détails, consultez [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La page Ethernet Port permet de gérer le rôle des ports Ethernet (WAN/LAN) et la segmentation VLAN, et d’afficher des informations telles que l’adresse MAC et le débit négocié.

    Pour plus de détails, consultez [Ethernet Port](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La page DNS permet de définir des serveurs DNS personnalisés, d’activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients, d’autoriser le DNS personnalisé à remplacer le DNS du VPN et de configurer les serveurs DNS automatiquement ou à partir de la connexion Ethernet.

    Pour plus de détails, consultez [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Son espace d’adressage beaucoup plus vaste offre un nombre pratiquement illimité d’adresses IP uniques, indispensable face à l’augmentation du nombre d’appareils connectés à Internet.

    Pour plus de détails, consultez [IPV6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    IGMP snooping est une technique d’optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.

    Pour plus de détails, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    Le mode réseau désigne les différents rôles et fonctions que le routeur peut adopter pour répondre aux besoins de déploiement. Les modes courants comprennent le mode routeur, le mode répéteur et le mode point d’accès.

    Pour plus de détails, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway permet d’étendre les fonctions d’un routeur principal existant sans le remplacer ni le reconfigurer. En configurant un routeur GL.iNet comme Drop-in Gateway, vous pouvez ajouter à l’infrastructure réseau existante des fonctions avancées telles qu’AdGuard Home, un VPN ou un DNS chiffré.

    Consultez les liens ci-dessous pour configurer Drop-in Gateway.

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Configuration de Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    L’accélération réseau réduit la charge du processeur et accélère le transfert des paquets.

    Pour plus de détails, consultez [Network Acceleration](../../interface_guide/network_acceleration.md).

## Contrôle du trafic

=== "DPI Engine"

    DPI (Deep Packet Inspection) est une fonction essentielle de la gestion intelligente des réseaux. Elle dépasse les limites des routeurs traditionnels, qui identifient uniquement les adresses source ou de destination, en analysant en profondeur le contenu des paquets. La comparaison avec une bibliothèque de signatures identifie avec précision les applications et sites Web consultés afin d’affiner la classification et le contrôle du trafic.

    Intégrée à [Netify](https://www.netify.ai/){target="_blank"}, la fonction DPI de GL.iNet utilise un module embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, elle assure une gestion fiable et un contrôle du réseau plus précis et efficace.

    Pour plus de détails, consultez [DPI Engine](../../interface_guide/dpi_engine.md).

=== "Data Statistics"

    Data Statistics propose un tableau de bord intelligent qui classe et représente l’utilisation du réseau par application. Il permet de surveiller le trafic en temps réel et l’historique afin de mieux comprendre et contrôler le réseau.

    Pour plus de détails, consultez [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter assure une sécurité en ligne intelligente grâce à la classification DPI et bloque automatiquement les sites Web dangereux ou malveillants afin de préserver la sécurité du réseau.

    Pour plus de détails, consultez [Content Filter](../../interface_guide/content_filter.md).

---

=== "QoS"

    QoS (Quality of Service) optimise l’attribution de la bande passante en donnant la priorité aux activités importantes, par exemple les appels vidéo et les jeux, en cas de congestion. Cela réduit la latence et améliore les performances globales du réseau. Cette fonction s’applique au trafic des clients locaux et des tunnels VPN Client, mais pas au trafic reçu lorsque le routeur fonctionne comme VPN Server.

    Pour plus de détails, consultez [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gère intelligemment le trafic réseau du routeur afin de réduire la latence et le « bufferbloat », pour des jeux et des appels vocaux plus fluides.

    Pour plus de détails, consultez [SQM](../../interface_guide/sqm.md).

=== "Parental Control"

    Parental Control aide à gérer et à contrôler les appareils de vos enfants, notamment en limitant leur temps d’écran et l’accès à certains contenus.

    Pour plus de détails, consultez [Parental Control](../../interface_guide/parental_control_v4.9.md).

## Sécurité

=== "Port Forwarding"

    La redirection de ports permet aux serveurs et appareils distants sur Internet d’accéder aux appareils d’un réseau privé.

    Pour plus de détails, consultez [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, ou Access Control List, permet de créer des règles de gestion du trafic réseau selon les protocoles de connexion, les adresses des appareils et les ports. Ces règles autorisent ou bloquent l’accès au réseau. Si plusieurs règles ACL sont en conflit, le système applique celle dont la priorité est la plus élevée.

    Pour plus de détails, consultez [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access permet de configurer différents paramètres de sécurité afin de protéger le réseau et le routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Local Access Control : gérez et limitez l’accès à l’interface du routeur depuis les appareils connectés au réseau local.
    * Remote Access Control : configurez et limitez l’accès à l’interface du routeur depuis Internet afin de renforcer la protection contre les menaces externes.
    * Open Ports on Router : contrôlez les ports ouverts sur le routeur afin de limiter les vulnérabilités et les accès non autorisés.

    Pour plus de détails, consultez [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La page NAT Mode permet d’activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour plus de détails, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctions spécifiques à un programme existant afin de le personnaliser et d’étendre ses possibilités.

    Pour plus de détails, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met à jour automatiquement et en temps réel l’adresse IP associée à un domaine. Il est particulièrement utile aux utilisateurs qui ont besoin d’une adresse IP statique pour accéder à un réseau distant.

    Pour plus de détails, consultez [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Le stockage réseau est une solution de stockage centralisée qui permet à plusieurs utilisateurs et appareils d’accéder à des fichiers et de les partager sur un réseau.

    Pour plus de détails, consultez [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l’échelle du réseau. Elle agit comme serveur DNS pour filtrer le contenu indésirable sur tous les appareils connectés au réseau domestique.

    Pour plus de détails, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Bark"

    Intégré à Flint 4, le service Bark aide à protéger l’environnement numérique de votre enfant et offre une protection en ligne complète. Il nécessite généralement un abonnement payant. Cependant, dans le cadre de son partenariat avec Bark, GL.iNet offre gratuitement l’offre Bark Home sur certains modèles de routeurs, dont Flint 4, avec une surveillance avancée et des alertes sans frais supplémentaires.

    Pour plus de détails, consultez [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale est un service VPN qui permet d’accéder à vos appareils et applications où que vous soyez.

    Pour plus de détails, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer sur Internet des réseaux virtuels sécurisés et de connecter les appareils comme s’ils se trouvaient sur le même réseau local.

    Pour plus de détails, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet de communiquer anonymement sur Internet. Il achemine le trafic Internet à travers une série de serveurs exploités par des bénévoles, appelés nœuds, afin de masquer la position et l’utilisation de l’utilisateur et de rendre les activités en ligne difficiles à retracer.

    Pour plus de détails, consultez [Tor](../../interface_guide/tor.md).

## Système

=== "Overview"

    La page Overview présente un aperçu complet de l’état actuel et des performances du routeur. Elle permet de consulter les informations suivantes :

    * CPU Average Load : surveillez la charge moyenne du processeur du routeur afin d’évaluer les performances et de repérer les éventuels goulets d’étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée par le routeur afin de mieux gérer les ressources.
    * Flash Usage : consultez l’utilisation du stockage flash du routeur et vérifiez que l’espace disponible est suffisant pour le micrologiciel et les données de configuration.
    * Device Info : consultez les informations détaillées du système, notamment la durée de fonctionnement, le nom d’hôte, le modèle, l’architecture, la version d’OpenWrt, la version du noyau, l’identifiant de l’appareil, l’adresse MAC et le numéro de série.
    * External Storage : vérifiez l’état des périphériques de stockage externes connectés au routeur, tels que les clés USB ou les cartes TF.

    Ces fonctions fournissent des informations et des commandes essentielles pour gérer et surveiller efficacement le fonctionnement du routeur.

    Pour plus de détails, consultez [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La page Admin Password permet de gérer le mot de passe de l’interface d’administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour plus de détails, consultez [Admin Password](../../interface_guide/admin_password.md).

=== "Upgrade"

    La page Upgrade sert à mettre à jour le micrologiciel du routeur vers la dernière version afin de bénéficier de meilleures performances, d’une sécurité renforcée et de nouvelles fonctions. Elle propose deux méthodes :

    * Firmware Online Upgrade : recherchez automatiquement la dernière version du micrologiciel sur le serveur du fabricant et installez-la si elle est disponible en ligne.
    * Firmware Local Upgrade : téléversez manuellement un fichier de micrologiciel depuis votre ordinateur afin de choisir la version et le moment de la mise à niveau.

    Pour plus de détails, consultez [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La page Scheduled Tasks permet d’automatiser différentes fonctions du routeur selon un calendrier prédéfini. Elle comprend notamment les fonctions suivantes :

    * LCD Display Schedule : programmez l’activation ou la désactivation automatique de l’écran LCD du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Schedule Reboot : configurez le redémarrage automatique du routeur à intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Wi-Fi Status Schedule : programmez les bandes Wi-Fi 6 GHz, 5 GHz, 2,4 GHz et MLO afin de gérer la disponibilité du réseau et de réduire la consommation électrique.

    Ces options offrent un meilleur contrôle du fonctionnement du routeur et permettent de l’adapter à vos besoins et préférences.

    Pour plus de détails, consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

=== "Display Management"

    La page Display Management propose un ensemble complet de fonctions pour gérer l’écran tactile et ses paramètres.

    ‒ Wallpaper : personnalisez le fond d’écran et le style d’affichage au réveil.
    ‒ Brightness : réglez la luminosité de l’écran tactile à l’aide du curseur ou saisissez un pourcentage adapté à l’éclairage ambiant.
    ‒ Auto Lock : définissez le délai de verrouillage automatique de l’écran en l’absence d’activité, de 1 à 30 minutes.
    ‒ Screen Always On : choisissez si l’écran tactile reste allumé en permanence ou s’éteint après une période d’inactivité.
    ‒ Enable Screen Passcode : définissez un code d’accès pour l’écran tactile afin d’ajouter une protection supplémentaire.

    Pour plus de détails, consultez [Display Management](../../interface_guide/display_management.md).

=== "Time Zone"

    La page Time Zone permet de définir le fuseau horaire correct du routeur afin que les tâches planifiées, les journaux et les événements système soient horodatés selon l’heure locale. Ce paramètre est essentiel à la précision des enregistrements et au bon fonctionnement des configurations temporelles.

    Pour plus de détails, consultez [Time Zone](../../interface_guide/time_zone.md).

---

=== "Reset Firmware"

    La page Reset Firmware permet de rétablir les paramètres par défaut de la version actuelle du micrologiciel et efface toutes les configurations personnalisées. Cette opération peut être utile pour résoudre des problèmes persistants ou repartir de la configuration par défaut du micrologiciel installé.

    Pour plus de détails, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur pour faciliter le dépannage et le suivi des performances. Elle comprend :

    * System Log : journaux détaillés des activités et événements du système.
    * Kernel Log : journaux relatifs aux opérations et événements du noyau.
    * Crash Log : enregistrements des pannes et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur Web Nginx utilisé par le routeur, avec des informations sur le trafic Web et le fonctionnement du serveur.

    La page comprend également un bouton Export Log qui permet d’exporter tous les journaux collectés pour les faire analyser par l’assistance technique. Cette fonction est particulièrement utile pour diagnostiquer les problèmes complexes et obtenir l’aide de professionnels.

    Pour plus de détails, consultez [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès aux options de configuration avancées depuis l’interface OpenWrt LuCI. Elle permet aux utilisateurs expérimentés d’affiner les paramètres et les fonctions du routeur au-delà des options de l’interface de base, notamment la configuration détaillée du réseau et du pare-feu ainsi que d’autres personnalisations avancées du système.

    Pour plus de détails, consultez [Advanced Settings](../../interface_guide/advanced_settings.md).
