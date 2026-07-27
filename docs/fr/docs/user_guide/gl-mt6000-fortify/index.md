# Guide utilisateur de Fortify (GL-MT6000)

## Présentation du produit

Fortify (GL-MT6000) est un routeur Wi-Fi 6 co-marqué publié conjointement par GL.iNet et ExpressVPN. Chaque unité inclut un abonnement ExpressVPN gratuit d'un an. Les utilisateurs peuvent utiliser l'abonnement et lier leur compte directement depuis le panneau d'administration web du routeur. Une fois activé, tout le trafic passant par le routeur utilise le réseau haut débit et le chiffrement robuste d'ExpressVPN afin de protéger l'ensemble de la connexion réseau et la confidentialité en ligne.

![fortify gl-mt6000](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000-fortify_interface.png){class="glboxshadow"}

## Configurer Fortify

### 1. Mettre sous tension

Assemblez l'adaptateur secteur en deux parties. Branchez-le sur votre routeur Fortify, puis sur une prise électrique. Le routeur démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil, par exemple un ordinateur, un ordinateur portable ou un smartphone, au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Settings -> WLAN, trouvez le nom du réseau Wi-Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe. Le nom et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez la langue en haut à droite, définissez le mot de passe administrateur, puis cliquez sur **Next**. Le mot de passe doit contenir de 10 à 63 caractères et au moins deux des types suivants : majuscules, minuscules, chiffres et symboles spéciaux.

![fortify login1](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login1.png){class="glboxshadow"}

Configurez le Wi-Fi. Si vous modifiez les informations Wi-Fi, vous devrez reconnecter votre appareil au Wi-Fi du routeur avec les nouveaux identifiants.

![fortify login2](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/login2.png){class="glboxshadow"}

### 4. Configurer Internet

**Note :** Les instructions suivantes concernent la configuration du routeur via le panneau d'administration web GL.iNet. Si vous préférez l'[application GL.iNet](https://www.gl-inet.com/pages/app#download-app-glinet){target="_blank"}, téléchargez-la et suivez les instructions à l'écran.

Configurez Fortify avec l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser [Multi-WAN](../../interface_guide/multi-wan.md), configurez plusieurs connexions Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_ethernet.png){class="glboxshadow"}

    Connectez un câble Ethernet entre le port WAN du routeur Fortify et un appareil en amont, par exemple un modem.

    Lorsque la connexion Internet est établie, la LED du routeur devient blanche fixe.

    Consultez [Connect to the Internet via an Ethernet cable](../../interface_guide/internet_ethernet.md) pour les instructions détaillées.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_repeater.png){class="glboxshadow"}

    1. Dans le panneau d'administration web, accédez à la section INTERNET -> Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.

    Lorsque la connexion Internet est établie, la LED du routeur devient blanche fixe.

    Consultez [Connect to the Internet via an existing Wi-Fi network](../../interface_guide/internet_repeater.md) pour les instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_tethering.png){class="glboxshadow"}

    1. Connectez votre smartphone au port USB du routeur à l'aide d'un câble USB.
    2. Sur le smartphone, accédez à Settings et activez USB Tethering. Sur iPhone, faites confiance à cet appareil et activez Personal Hotspot.
    3. Dans le panneau d'administration web, accédez à la section INTERNET -> Tethering et cliquez sur **Connect**.

    Lorsque la connexion Internet est établie, la LED du routeur devient blanche fixe.

    Consultez [Connect to the Internet via USB tethering](../../interface_guide/internet_tethering.md) pour les instructions détaillées.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000-fortify/mt6000_cellular.png){class="glboxshadow"}

    Branchez un modem USB cellulaire au port USB du routeur afin de partager l'accès Internet du modem avec tous les appareils connectés.

    Lorsque la connexion Internet est établie, la LED du routeur devient blanche fixe.

    Consultez [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md) pour les instructions détaillées.

---

Voici un aperçu des fonctions du panneau d'administration web de Fortify.

## Wireless

La page Wireless permet de configurer les réseaux Wi-Fi de Fortify, notamment Main Network, Guest Network et IoT Network. Chaque réseau prend en charge les bandes 2,4 GHz et 5 GHz.

Pour configurer Wireless, consultez [Wireless](../../interface_guide/wireless_v4.9.md).

## Clients

La page Clients affiche les appareils connectés, avec le nom de l'appareil, le type de connexion, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic, ainsi que la possibilité de bloquer un client spécifique en un clic.

Consultez [Clients](../../interface_guide/clients.md) pour plus de détails.

## Services cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} fournit un moyen simple d'accéder à distance à vos routeurs GL.iNet et de les gérer.

    Consultez [GoodCloud](../../interface_guide/cloud.md) pour plus de détails.

=== "AstroWarp"

    AstroWarp est conçu pour la mise en réseau à distance sur les routeurs GL.iNet. Il utilise le protocole AmneziaWG avec obfuscation du trafic intégrée pour offrir un accès à distance stable et sécurisé.

    Consultez [AstroWarp](../../interface_guide/astrowarp.md) pour plus de détails.

## VPN

Un VPN (réseau privé virtuel) établit des tunnels de trafic sécurisés et chiffrés entre votre appareil local et le serveur VPN. Il renforce la confidentialité et la sécurité du client VPN et permet d'accéder au réseau distant du serveur VPN.

Fortify s'intègre à [ExpressVPN](https://www.expressvpn.com/){target="_blank"}, ce qui permet d'activer une connexion ExpressVPN en quelques minutes. Chaque appareil Fortify inclut un abonnement ExpressVPN gratuit d'un an, que vous pouvez utiliser et lier à votre compte ExpressVPN depuis le panneau d'administration web.

Pour utiliser l'abonnement gratuit et configurer un tunnel VPN, consultez [ExpressVPN Dashboard](../../interface_guide/expressvpn_dashboard.md).

Pour configurer un serveur OpenVPN, consultez [OpenVPN Server](../../interface_guide/openvpn_server.md).

Pour configurer un serveur WireGuard, consultez [WireGuard Server](../../interface_guide/wireguard_server.md).

## Réseau

=== "Multi-WAN"

    Multi-WAN permet d'utiliser plusieurs connexions Internet simultanément, par exemple cellular, repeater et ethernet. Si la connexion actuelle échoue, le routeur bascule automatiquement vers une autre connexion.

    Consultez [Multi-WAN](../../interface_guide/multi-wan.md) pour plus de détails.

=== "LAN"

    Le LAN est le réseau local rejoint par votre appareil lorsqu'il est connecté au Wi-Fi principal ou via un câble Ethernet. La page LAN couvre Basic Settings, DHCP Server Settings et Address Reservation.

    Consultez [LAN](../../interface_guide/lan.md) pour plus de détails.

=== "Guest Network"

    Guest Network crée un réseau Wi-Fi dédié aux visiteurs. Il est isolé du réseau principal et peut utiliser un sous-réseau invité dans les plages IPv4 privées `192.168.0.0/16`, `172.16.0.0/12` ou `10.0.0.0/8`.

    Consultez [Guest Network](../../interface_guide/guest_network.md) pour plus de détails.

=== "IoT Network"

    IoT Network permet de créer un réseau Wi-Fi dédié aux appareils IoT, isolé du réseau principal afin d'améliorer la compatibilité et la sécurité.

    Consultez [IoT Network](../../interface_guide/iot_network.md) pour plus de détails.

<br>

=== "DNS"

    Les paramètres DNS contrôlent la traduction des noms de domaine en adresses IP. Vous pouvez utiliser les serveurs DNS obtenus automatiquement, définir des serveurs personnalisés et configurer les priorités DNS.

    Consultez [DNS](../../interface_guide/dns.md) pour plus de détails.

=== "Ethernet Port"

    Ethernet Port permet de gérer les rôles des ports WAN/LAN et d'afficher les détails des ports, comme l'adresse MAC et la vitesse négociée.

    Consultez [Ethernet Port](../../interface_guide/ethernet_port.md) pour plus de détails.

=== "IPv6"

    IPv6 est la version la plus récente du protocole Internet et fournit un espace d'adressage beaucoup plus vaste qu'IPv4.

    Consultez [IPV6](../../interface_guide/network_mode.md) pour plus de détails.

=== "IGMP Snooping"

    IGMP Snooping est une technique d'optimisation utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.

    Consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md) pour plus de détails.

<br>

=== "Network Mode"

    Network Mode définit la façon dont un appareil se connecte à un réseau et communique avec d'autres appareils.

    Pour le configurer, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctions de votre routeur principal avec AdGuard Home, le DNS chiffré et le VPN.

    Pour le configurer, consultez [How to set up drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "Network Acceleration"

    Network Acceleration peut réduire la charge CPU et accélérer le transfert des paquets.

    Pour le configurer, consultez [Network Acceleration](../../interface_guide/network_acceleration.md).

## Flow Control

=== "DPI Engine"

    DPI (Deep Packet Inspection) analyse le contenu des paquets pour identifier plus précisément les applications et sites web à l'aide d'une bibliothèque de signatures. La fonction DPI de GL.iNet s'intègre à [Netify](https://www.netify.ai/){target="_blank"}.

    Consultez [DPI Engine](../../interface_guide/dpi_engine.md) pour plus de détails.

=== "Data Statistics"

    Data Statistics classe et visualise l'utilisation du réseau par application afin de surveiller le trafic en temps réel et historique.

    Consultez [Data Statistics](../../interface_guide/data_statistics.md) pour plus de détails.

=== "Content Filter"

    Content Filter utilise une classification basée sur DPI pour bloquer automatiquement les sites web dangereux ou malveillants.

    Consultez [Content Filter](../../interface_guide/content_filter.md) pour plus de détails.

<br>

=== "QoS"

    QoS priorise les activités critiques, comme les appels vidéo ou les jeux, pendant la congestion du réseau. Cela s'applique au trafic local des clients et au trafic des tunnels VPN Client, mais pas au trafic reçu lorsque le routeur fonctionne comme VPN Server.

    Consultez [QoS](../../interface_guide/qos.md) pour plus de détails.

=== "SQM"

    SQM (Smart Queue Management) gère le trafic réseau afin de réduire la latence et le bufferbloat.

    Consultez [SQM](../../interface_guide/sqm.md) pour plus de détails.

=== "Parental Control"

    Parental Control aide à gérer les appareils de vos enfants, à limiter leur temps d'écran et à restreindre l'accès à certains contenus.

    Consultez [Parental Control](../../interface_guide/parental_control_v4.9.md) pour plus de détails.

## Sécurité

=== "Port forwarding"

    Port forwarding permet à des serveurs et appareils distants sur Internet d'accéder à des appareils d'un réseau privé.

    Consultez [Port Forwarding](../../interface_guide/port_forwarding.md) pour plus de détails.

=== "ACL"

    ACL (Access Control List) permet de créer des règles de gestion du trafic selon les protocoles, adresses d'appareils et ports. En cas de conflit, le système applique la règle ayant la priorité la plus élevée.

    Consultez [ACL](../../interface_guide/acl.md) pour plus de détails.

=== "Admin Access"

    Admin Access regroupe les paramètres de sécurité qui protègent le réseau et le routeur contre les accès non autorisés, notamment Access Control, Remote Access Control et Open Ports on Router.

    Consultez [Admin Access](../../interface_guide/admin_access.md) pour plus de détails.

=== "NAT Mode"

    NAT Mode permet d'activer ou de désactiver Full Cone NAT et SIP ALG.

    Consultez [NAT Mode](../../interface_guide/nat_settings.md) pour plus de détails.

## Applications

=== "Plug-ins"

    Un plug-in ajoute des fonctions spécifiques à un programme ou système existant.

    Consultez [Plug-ins](../../interface_guide/plugins.md) pour plus de détails.

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine.

    Consultez [Dynamic DNS](../../interface_guide/ddns.md) pour plus de détails.

=== "Network Storage"

    Network Storage fournit un stockage centralisé accessible à plusieurs utilisateurs et appareils sur le réseau.

    Consultez [Network Storage](../../interface_guide/network_storage.md) pour plus de détails.

=== "AdGuard Home"

    AdGuard Home bloque les publicités et traceurs à l'échelle du réseau en agissant comme serveur DNS pour filtrer le contenu indésirable.

    Consultez [AdGuard Home](../../interface_guide/adguardhome.md) pour plus de détails.

<br>

=== "Bark"

    [Bark](https://www.bark.us/){target="_blank"} peut aider à protéger l'environnement numérique de votre enfant. Dans le cadre du partenariat entre GL.iNet et Bark, Fortify (GL-MT6000) propose gratuitement le forfait Bark Home.

    Consultez [Bark](../../interface_guide/bark.md) pour plus de détails.

=== "Tailscale"

    Tailscale permet d'accéder à vos appareils et applications de manière sécurisée depuis n'importe où. Fortify (GL-MT6000) peut rejoindre un réseau virtuel Tailscale pour accéder à distance aux ressources WAN et LAN.

    Consultez [Tailscale](../../interface_guide/tailscale.md) pour plus de détails.

=== "ZeroTier"

    ZeroTier crée des réseaux virtuels sécurisés via Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.

    Consultez [ZeroTier](../../interface_guide/zerotier.md) pour plus de détails.

=== "Tor"

    Tor est un logiciel libre et open source destiné aux communications anonymes et à une navigation plus privée.

    Consultez [Tor](../../interface_guide/tor.md) pour plus de détails.

## Système

=== "Overview"

    Overview affiche l'état actuel du routeur et ses indicateurs, notamment CPU Average Load, Memory Usage, LED Control, Flash Usage, Device Info et External Storage.

    Consultez [Overview](../../interface_guide/system_overview.md) pour plus de détails.

=== "Admin Password"

    Admin Password permet de définir ou modifier le mot de passe de l'interface d'administration du routeur.

    Consultez [Admin Password](../../interface_guide/admin_password.md) pour plus de détails.

=== "Upgrade"

    Upgrade sert à mettre à jour le firmware du routeur. Il inclut Firmware Online Upgrade et Firmware Local Upgrade.

    Consultez [Upgrade](../../interface_guide/upgrade.md) pour plus de détails.

=== "Scheduled Tasks"

    Scheduled Tasks automatise les fonctions du routeur selon un calendrier, notamment LED Display Schedule, Schedule Reboot et 5GHz / 2.4GHz Wi-Fi Status Schedule.

    Consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) pour plus de détails.

<br>

=== "Time Zone"

    Time Zone définit le fuseau horaire correct pour les tâches planifiées, les journaux et les événements système.

    Consultez [Time Zone](../../interface_guide/time_zone.md) pour plus de détails.

=== "Reset Firmware"

    Reset Firmware restaure le firmware actuel à ses paramètres par défaut et efface les configurations personnalisées.

    Consultez [Reset Firmware](../../interface_guide/reset_firmware.md) pour plus de détails.

=== "Log"

    Log donne accès à System Log, Kernel Log, Crash Log, Cloud Log et Nginx Log. Le bouton Export Log permet d'exporter les journaux collectés pour l'analyse du support technique.

    Consultez [Log](../../interface_guide/log.md) pour plus de détails.

=== "Advanced Settings"

    Advanced Settings ouvre l'interface OpenWrt LuCI pour les configurations avancées.

    Consultez [Advanced Settings](../../interface_guide/advanced_settings.md) pour plus de détails.
