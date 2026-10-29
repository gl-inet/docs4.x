# Guide d'utilisation de Flint 2 (GL-MT6000) {#flint-2-gl-mt6000-user-guide}

## Aperçu du produit {#product-overview}

Flint 2 (GL-MT6000) est un routeur Wi‑Fi 6 pour la maison et le bureau, parfaitement adapté aux transferts de données intensifs, à la connexion simultanée d'un grand nombre d'appareils ou aux environnements de jeu à très faible latence. Flint 2 offre des vitesses WireGuard pouvant atteindre 900 Mbps. Il prend également en charge des fonctions avancées de redondance réseau, notamment le Multi-WAN, la conmutation par erreur et l'équilibrage de charge, afin de garantir un réseau ininterrompu.

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## Contenu du colis {#package-contents}

- 1 x Flint 2 (GL-MT6000)
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

Découvrez ci-dessous la vidéo de déballage du Flint 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Comment configurer Flint 2 {#how-to-set-up-flint-2}

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise un autre routeur GL.iNet pour illustrer la configuration, mais les étapes sont identiques pour le Flint 2 et les autres modèles de routeurs.)</small>

### 1. Mise sous tension {#1-power-on}

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur puis sur une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil {#2-connect-device}

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet. 

- Wi‑Fi

    Sur votre appareil, accédez à Settings -> WLAN, repérez le nom du réseau Wi-Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. Vous trouverez le nom de réseau et le mot de passe par défaut sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web {#3-log-in-to-web-admin-panel}

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**. 

Lors de la confirmation des paramètres Wi‑Fi, veuillez noter que si vous modifiez les informations Wi‑Fi, vous devrez reconnecter votre appareil au Wi‑Fi du routeur avec les nouveaux identifiants.

### 4. Configuration de la connexion Internet {#4-internet-setup}

**Remarque :** Les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Flint 2 en utilisant l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plusieurs connexions Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_ethernet.png){class="glboxshadow"}

    Connectez un câble Ethernet entre le port WAN du routeur et un appareil en amont, tel qu'un modem. 
    
    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_repeater.png){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi parmi les réseaux disponibles. 
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Repeater de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile (par ex. un smartphone ou un dongle USB) au port USB du routeur à l'aide d'un câble USB. 
    2. Sur votre appareil mobile, accédez à Settings et activez USB Tethering. 
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering. 
    
    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Tethering de la page INTERNET.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/internet/mt6000_cellular.png){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du routeur. Cela permet de partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Cellular de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées. 

---

## DNS {#dns}

Les paramètres DNS de votre routeur contrôlent la résolution des noms de domaine en adresses IP. Cette page vous permet d’utiliser les serveurs DNS obtenus automatiquement auprès des appareils en amont ou de définir des serveurs personnalisés. Vous pouvez également configurer les options DNS et modifier les règles d’hôtes statiques.

Pour plus d’informations, consultez [DNS](../../interface_guide/dns_v4.11.md).

## Sans fil {#wireless}

La page Réseau sans fil vous permet de configurer les paramètres des réseaux Wi‑Fi 5 GHz et 2,4 GHz, notamment l'activation/la désactivation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation/la désactivation du BSSID aléatoire, le choix du mode de sécurité Wi‑Fi, la définition du mot de passe Wi‑Fi, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi‑Fi, de la bande passante et du canal.

Pour configurer le réseau sans fil, consultez [Réseau sans fil](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi à tout le domicile et permet une itinérance transparente. Si vous disposez de plusieurs routeurs GL.iNet, configurez-en un comme routeur principal et les autres comme nœuds mesh pour bénéficier d’une itinérance Wi-Fi transparente dans votre domicile.

Pour plus d’informations, consultez [Mesh](../../interface_guide/mesh.md).

## Clients {#clients}

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom de l'appareil, le type de connexion (Ethernet ou Wi-Fi), les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de réserver une IP, de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services cloud {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account permet de connecter et de gérer vos appareils et services Cloud. Vous pouvez accéder facilement à GoodCloud et à la glinet App afin de gérer votre réseau de façon sécurisée et pratique, où que vous soyez et à tout moment.

    Pour configurer GL.iNet Account, consultez [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    Le service GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer. 
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS est une fonction réseau avancée conçue pour offrir un accès à distance et une gestion des appareils fluides. Développé spécialement pour l'intégration aux routeurs GL.iNet, GoodPAS utilise le protocole AmneziaWG avec obfuscation intégrée du trafic afin d'assurer des connexions sécurisées et stables. GoodPAS vous permet d’accéder à distance à votre réseau domestique. Lorsque votre routeur domestique sert de nœud de sortie GoodPAS, le trafic Internet envoyé via GoodPAS utilise l’adresse IP publique WAN de ce routeur.

    Pour configurer GoodPAS, consultez [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et permet d'accéder à un réseau distant (serveur VPN). Flint 2, comme les autres routeurs GL.iNet, prend en charge OpenVPN et WireGuard.

=== "OpenVPN" 

    Flint 2 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau {#network}

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui permet de configurer le routeur avec plusieurs connexions Internet simultanées (par ex. cellular, repeater et ethernet). Si votre connexion Internet actuelle tombe en panne, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu. 

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La page LAN centralise la configuration et la gestion du réseau principal, du réseau invité, du réseau IoT et des réseaux VLAN personnalisés. Vous pouvez créer et gérer plusieurs sous-réseaux pour isoler différents types d’appareils ou de trafic.

=== "Port Ethernet"

    La page Ethernet Port permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port_v4.10.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet. 
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/ipv6.md).

<br>

=== "IGMP Snooping"

    L'IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast. 
    
    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Mode réseau"

    La page Network Mode permet de configurer le rôle opérationnel du routeur pour répondre à différents besoins de déploiement réseau. Vous pouvez choisir parmi plusieurs modes, de la couverture Wi-Fi domestique aux réseaux multi-liens d'entreprise ; chaque mode active ou désactive des fonctions précises du routeur afin d'optimiser les performances.

    Pour configurer cette fonction, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "Passerelle Drop-in"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment avec AdGuard Home, le DNS chiffré et le client VPN.

    Pour configurer Drop-in Gateway, consultez les liens suivants :

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Configuration de Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accélération réseau"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle du trafic {#flow-control}

=== "Network Quality"

    Le tableau de bord Network Quality surveille la qualité de votre connexion Internet en temps réel. Il évalue la réactivité, la latence et les performances DNS tout en détectant les coupures de connexion et les pertes de paquets. Ces indicateurs vous aident à identifier les instabilités du réseau et les problèmes de connectivité que les seuls tests de bande passante peuvent ne pas révéler.

    Pour plus d’informations, consultez [Network Quality](../../interface_guide/network_quality.md).

=== "Data Statistics"

    Data Statistics propose un tableau de bord intelligent qui classe et représente l’utilisation du réseau par application. Il permet de surveiller le trafic en temps réel et l’historique afin de mieux comprendre et contrôler le réseau.

    Pour plus de détails, consultez [Data Statistics](../../interface_guide/data_statistics.md).

=== "Content Filter"

    Content Filter assure une sécurité en ligne intelligente grâce à la classification DPI et bloque automatiquement les sites Web dangereux ou malveillants afin de préserver la sécurité du réseau.

    Pour plus de détails, consultez [Content Filter](../../interface_guide/content_filter.md).

<br>

=== "QoS"

    QoS (Quality of Service) optimise l’attribution de la bande passante en donnant la priorité aux activités importantes, par exemple les appels vidéo et les jeux, en cas de congestion. Cela réduit la latence et améliore les performances globales du réseau. Cette fonction s’applique au trafic des clients locaux et des tunnels VPN Client, mais pas au trafic reçu lorsque le routeur fonctionne comme VPN Server.

    Pour plus de détails, consultez [QoS](../../interface_guide/qos.md).

=== "SQM"

    SQM (Smart Queue Management) gère intelligemment le trafic réseau du routeur afin de réduire la latence et le « bufferbloat », pour des jeux et des appels vocaux plus fluides.

    Pour plus de détails, consultez [SQM](../../interface_guide/sqm.md).

=== "Contrôle parental"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre l'accès à certains contenus. 

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control_v4.9.md).

## Sécurité {#security}

=== "Security Scan"

    Security Scan effectue un contrôle de sécurité de votre routeur. Cette fonctionnalité évalue ses paramètres de sécurité et fournit un score de sécurité, des alertes de risque et des suggestions d’optimisation. Vous pouvez ajuster votre configuration en fonction des résultats de l’analyse pour améliorer la sécurité du routeur.

    Pour plus d’informations, consultez [Security Scan](../../interface_guide/security_scan.md).

=== "ACL"

    ACL, ou Access Control List, permet de créer des règles de gestion du trafic réseau selon les protocoles de connexion, les adresses des appareils et les ports. Ces règles autorisent ou bloquent l’accès au réseau. Si plusieurs règles ACL sont en conflit, le système applique celle dont la priorité est la plus élevée.

    Pour plus de détails, consultez [ACL](../../interface_guide/acl.md).

=== "Port Forwarding"

    La redirection de port permet à des serveurs et appareils distants sur Internet d'accéder à des appareils situés sur un réseau privé. 

    Pour configurer la redirection de ports, consultez [Port Forwarding](../../interface_guide/port_forwarding.md).

<br>

=== "UPnP"

    UPnP (Universal Plug and Play) permet aux appareils et applications LAN compatibles de demander automatiquement des mappages de ports sur les routeurs GL.iNet. Ces mappages redirigent le trafic WAN entrant vers des adresses IP et des ports LAN spécifiés, permettant aux clients externes de se connecter aux services locaux sans configurer manuellement de règles de redirection de ports.

    Pour plus d’informations, consultez [UPnP](../../interface_guide/upnp.md).

=== "Admin Access"

    Admin Access permet de configurer différents paramètres de sécurité afin de protéger le réseau et le routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Contrôle d'accès local : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la sécurité contre les menaces externes.
    * Ports ouverts sur le routeur : contrôlez quels ports sont ouverts sur le routeur, afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Pour plus de détails, consultez [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La page NAT Mode vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG.

    Pour configurer les paramètres NAT, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications {#applications}

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant ainsi de le personnaliser et d'en étendre les capacités. 
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il associe un nom de domaine à l'adresse IP publique dynamique de votre routeur, ce qui vous permet d'accéder à votre réseau à distance sans adresse IP statique. 
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder à des fichiers et de les partager via un réseau. 
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

<br>

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traceurs à l'échelle du réseau qui agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés au réseau domestique. 
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications partout. 
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est une solution réseau définie par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, reliant les appareils comme s'ils se trouvaient sur le même réseau local. 
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet des communications anonymes sur Internet. Il achemine le trafic Internet via une série de serveurs bénévoles (nœuds) afin de masquer l'emplacement et l'usage de l'utilisateur, rendant les activités en ligne difficiles à tracer. 

    Pour plus de détails, consultez [Tor](../../interface_guide/tor.md).

## Système {#system}

=== "Aperçu"

    La page Overview fournit une vue d'ensemble complète de l'état actuel du routeur et de ses performances. Sur cette page, vous pouvez voir :

    * Charge CPU moyenne : surveillez la charge moyenne du processeur de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulets d'étranglement.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire utilisée sur le routeur afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser ses indicateurs visuels.
    * Utilisation du stockage flash : consultez l'utilisation de la mémoire flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez à des informations détaillées sur le système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC et le numéro de série.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, comme les clés USB ou les cartes TF.
    
    Ces fonctionnalités offrent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement du routeur.

    Veuillez consulter [Overview](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Admin Password"

    La page Admin Password permet de gérer le mot de passe de l’interface d’administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour plus de détails, consultez [Admin Password](../../interface_guide/admin_password.md).

=== "Mise à niveau"

    La page Upgrade sert à mettre à jour le firmware du routeur vers la dernière version, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : recherche automatiquement la dernière version du firmware sur le serveur du fabricant. Vous pouvez l'installer si elle est disponible en ligne.
    * Firmware Local Upgrade : permet de téléverser manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous laisse le contrôle sur la version et le moment de la mise à jour.

    Ces options vous permettent de maintenir le routeur à jour avec les dernières améliorations et correctifs.

    Veuillez consulter [Upgrade](../../interface_guide/upgrade.md) pour des instructions détaillées.

=== "Tâches planifiées"

    La page Scheduled Tasks permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, afin d'améliorer le confort d'utilisation et l'efficacité. Les principales fonctionnalités de cette page incluent :

    * Planification de l'affichage LED : définissez un calendrier pour allumer ou éteindre automatiquement les voyants LED du routeur, afin de réduire la pollution lumineuse à certains moments.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis, afin de préserver des performances et une stabilité optimales.
    * Planification de l'état du Wi-Fi 5 GHz / 2.4 GHz : définissez un calendrier pour contrôler les bandes Wi-Fi 5 GHz / 2.4 GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur, afin qu'il réponde à vos besoins et préférences spécifiques.

    Veuillez consulter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.

=== "Fuseau horaire"

    La page Time Zone permet de définir le fuseau horaire correct pour le routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements exacts et pour assurer l'exécution correcte des configurations basées sur le temps.

    Veuillez consulter [Time Zone](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Réinitialiser le firmware"

    La page Reset Firmware permet de réinitialiser la version actuelle du firmware du routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Veuillez consulter [Reset Firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

<br>

=== "Journal"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau système.
    * Journal du noyau : journaux liés aux opérations et événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Journal cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, cette page propose un bouton Export Log, qui permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Log](../../interface_guide/log.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, ce qui permet aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de base de l'interface. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Veuillez consulter [Advanced Settings](../../interface_guide/advanced_settings.md) pour des instructions détaillées.

## Déclaration UE de conformité {#declaration-of-conformity}

Par la présente, GL TECHNOLOGIES (HONG KONG) LIMITED déclare que l'équipement radio de type [AX6000 Wireless Router, GL-MT6000] est conforme aux exigences essentielles et aux autres dispositions pertinentes de la directive 2014/53/UE. Le texte complet de la déclaration de conformité UE est disponible à l'adresse internet suivante: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
