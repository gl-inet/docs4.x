# Guide d'utilisation de Flint 3 (GL-BE9300) {#flint-3-gl-be9300-user-guide}

## Aperçu du produit {#product-overview}

Flint 3 (GL-BE9300) est un routeur de bureau tri-bande Wi-Fi 7 conçu pour les particuliers, les petits bureaux et les environnements à forte demande. Il prend en charge la technologie Wi-Fi 7 Multi-Link Operation (MLO), qui regroupe intelligemment les bandes 2.4GHz, 5GHz et 6GHz en une seule connexion afin de réduire les interférences et l'encombrement du réseau. Associé au 4K QAM, il offre des débits théoriques tri-bande de 688Mbps (2.4GHz), 2882Mbps (5GHz) et 5765Mbps (6GHz). La connectivité MLO ou 6GHz fournit les meilleures performances, tandis que la bande 2.4GHz peut être réservée aux appareils IoT.

Il dispose de 5 ports Ethernet 2.5G (1 WAN dédié, 1 WAN/LAN commutable, 3 LAN), prenant en charge les configurations dual-WAN avec une bande passante partagée maximale de 5Gbps, ainsi que d'un port USB 3.0 pour étendre ses fonctionnalités. De plus, il est livré avec AdGuard Home préinstallé pour le blocage des publicités et l'anti-pistage, prend en charge Bark Parental Control et plus de 30 services VPN, et permet la gestion à distance via GoodCloud — un excellent équilibre entre performances, praticité et sécurité.

![interface gl-be9300](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/hardware_info/be9300_interface.jpg){class="glboxshadow"}

## Contenu du colis {#package-contents}

- 1 x Flint 3 (GL-BE9300)
- 1 x Adaptateur secteur
- 1 x Câble Ethernet
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Convertisseur (selon votre pays de livraison)

Découvrez ci-dessous la vidéo de déballage de Flint 3.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qAq6IFtKtj0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration initiale de Flint 3 {#how-to-set-up-flint-3}

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WQqD-8NrAOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension {#1-power-on}

Assemblez les deux parties de l'adaptateur secteur. Connectez-le à votre routeur puis branchez-le sur une prise électrique. Il démarrera automatiquement.

### 2. Connecter un appareil {#2-connect-device}

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi de votre routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous connecter. Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web {#3-log-in-to-web-admin-panel}

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez votre langue, définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 4. Configuration de la connexion Internet {#4-internet-setup}

**Remarque :** Les instructions ci-dessous s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} puis suivez les instructions affichées à l'écran.

Configurez votre Flint 3 à l'aide de l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), configurez plusieurs connexions Internet.

=== "Ethernet"
    
    ![Connexion Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_ethernet.jpg){class="glboxshadow"}

    Connectez le port WAN du Flint 3 à un appareil en amont (par exemple un modem) à l'aide d'un câble Ethernet.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![Connexion Repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_repeater.jpg){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater puis cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Repeater de la page INTERNET.

    Veuillez consulter [Se connecter à Internet via un réseau Wi-Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![Connexion Tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Settings et activez USB Tethering.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Tethering de la page INTERNET.

    Veuillez consulter [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![Connexion Cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-be9300/internet/be9300_cellular.jpg){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du Flint 3. Cette méthode est utile pour partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie avec succès, un point vert apparaît dans la section Cellular de la page INTERNET.

    Veuillez consulter [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

---
    
Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d'administration web de Flint 3.

## Sans fil {#wireless}

La page Sans fil vous permet de configurer les paramètres des réseaux Wi-Fi 6GHz, 5GHz et 2.4GHz, notamment l'activation du Wi-Fi, le réglage de la puissance TX, la définition du nom du réseau Wi-Fi (SSID), l'activation du BSSID aléatoire, le choix du mode de sécurité Wi-Fi et du mot de passe, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi-Fi, de la bande passante et du canal.
    
De plus, Flint 3 prend en charge le Wi-Fi MLO, c'est-à-dire Multi-Link Operation, qui combine simultanément plusieurs réseaux sans fil afin d'obtenir une bande passante plus élevée et des connexions plus fiables.

Pour configurer le Wi-Fi, consultez [Wi-Fi](../../interface_guide/wireless.md).

## Mesh {#mesh}

Mesh est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi à tout le domicile et permet une itinérance transparente. Si vous disposez de plusieurs routeurs GL.iNet, configurez-en un comme routeur principal et les autres comme nœuds mesh pour bénéficier d’une itinérance Wi-Fi transparente dans votre domicile.

Pour configurer Mesh, consultez [Mesh](../../interface_guide/mesh.md).

## Clients {#clients}

La page Clients affiche les informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet également de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services cloud {#cloud-services}

=== "GL.iNet Account"

    GL.iNet Account permet de connecter et de gérer vos appareils et services Cloud. Vous pouvez accéder facilement à GoodCloud et à la glinet App afin de gérer votre réseau de façon sécurisée et pratique, où que vous soyez et à tout moment.

    Pour configurer GL.iNet Account, consultez [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre une solution simple et pratique pour accéder à distance aux routeurs GL.iNet et les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "GoodPAS"

    GoodPAS est une fonction réseau avancée conçue pour offrir un accès à distance et une gestion des appareils fluides. Développé spécialement pour l'intégration aux routeurs GL.iNet, GoodPAS utilise le protocole AmneziaWG avec obfuscation intégrée du trafic afin d'assurer des connexions sécurisées et stables. GoodPAS vous permet d’accéder à distance à votre réseau domestique. Lorsque votre routeur domestique sert de nœud de sortie GoodPAS, le trafic Internet envoyé via GoodPAS utilise l’adresse IP publique WAN de ce routeur.

    Pour configurer GoodPAS, consultez [GoodPAS](../../interface_guide/goodpas.md).

## VPN {#vpn}

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Flint 3 prend en charge OpenVPN et WireGuard.

=== "OpenVPN" 
    
    Flint 3 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre un haut niveau de sécurité. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 3 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes performances et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau {#network}

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Cellular, Repeater et Ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion Internet. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Cette page permet de configurer et de gérer de manière centralisée **Main Network**, **Guest Network**, **IoT Network** et les **VLAN Networks** personnalisés. Vous pouvez créer et gérer plusieurs sous-réseaux afin d’isoler différents types d’appareils ou de trafic.

    Pour configurer cette fonction, consultez [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La page Port Ethernet vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d’activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients et d’autoriser les DNS personnalisés à remplacer les DNS VPN. Vous pouvez utiliser les serveurs DNS obtenus automatiquement auprès des appareils en amont ou spécifier manuellement des serveurs DNS personnalisés.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour répondre au nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/ipv6.md).

=== "IGMP Snooping"

    L'IGMP snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).
    
---

=== "Network Mode"

    La page Network Mode permet de configurer le rôle opérationnel du routeur pour répondre à différents besoins de déploiement réseau. Vous pouvez choisir parmi plusieurs modes, de la couverture Wi-Fi domestique aux réseaux multi-liens d'entreprise ; chaque mode active ou désactive des fonctions précises du routeur afin d'optimiser les performances.

    Pour configurer cette fonction, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, consultez les liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Accélération réseau"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle du trafic {#flow-control}

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

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control_v4.9.md).

## Sécurité {#security}

=== "Port Forwarding"

    La redirection de port permet à des serveurs et appareils distants sur Internet d'accéder à des appareils situés sur un réseau privé.
    
    Pour configurer la redirection de port, consultez [Redirection de port](../../interface_guide/port_forwarding.md).

=== "ACL"

    ACL, ou Access Control List, permet de créer des règles de gestion du trafic réseau selon les protocoles de connexion, les adresses des appareils et les ports. Ces règles autorisent ou bloquent l’accès au réseau. Si plusieurs règles ACL sont en conflit, le système applique celle dont la priorité est la plus élevée.

    Pour plus de détails, consultez [ACL](../../interface_guide/acl.md).

=== "Admin Access"

    Admin Access permet de configurer différents paramètres de sécurité afin de protéger le réseau et le routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Contrôle d'accès local : gérer et restreindre l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurer et restreindre l'accès à l'interface du routeur depuis des emplacements distants via Internet, renforçant ainsi la protection contre les menaces externes.
    * Ouvrir des ports sur le routeur : contrôler quels ports sont ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Pour plus de détails, consultez [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La page NAT Mode vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG.

    Pour configurer les paramètres NAT, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications {#applications}

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctions ou fonctionnalités spécifiques à un programme informatique existant, afin de permettre sa personnalisation et d'étendre ses capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Le DNS dynamique (DDNS) détecte et met automatiquement à jour en temps réel l'adresse IP associée à un domaine. Il associe un nom de domaine à l'adresse IP publique dynamique de votre routeur, ce qui vous permet d'accéder à votre réseau à distance sans adresse IP statique.
    
    Pour configurer le DNS dynamique, consultez [Dynamic DNS](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution de stockage de données centralisée qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l'échelle du réseau. Elle fonctionne comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Bark"

    Intégré à Flint 3, le service Bark aide à protéger l’environnement numérique de votre enfant et offre une protection en ligne complète. Il nécessite généralement un abonnement payant. Cependant, dans le cadre de son partenariat avec Bark, GL.iNet offre gratuitement l’offre Bark Home sur certains modèles de routeurs, dont Flint 3, avec une surveillance avancée et des alertes sans frais supplémentaires.

    Pour plus de détails, consultez [Bark](../../interface_guide/bark.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications où que vous soyez.
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer des réseaux virtuels sécurisés via Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet une communication anonyme sur Internet. Il fait transiter le trafic Internet par une série de serveurs (nœuds) exploités par des bénévoles afin de masquer l'emplacement et l'utilisation de l'utilisateur, ce qui rend les activités en ligne difficiles à tracer.
    
    Pour plus de détails, consultez [Tor](../../interface_guide/tor.md).

## Système {#system}

=== "Aperçu"

    La page Aperçu fournit un aperçu complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez afficher :

    * Charge moyenne du CPU : surveillez la charge moyenne du CPU de votre routeur afin d'évaluer ses performances et d'identifier d'éventuels goulots d'étranglement.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire utilisée par votre routeur afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l'appareil.
    * Utilisation du flash : consultez l'utilisation du stockage flash du routeur afin de vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez aux informations détaillées du système de votre routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, la MAC de l'appareil et le S/N de l'appareil.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que les clés USB ou les cartes TF.
    
    Ces fonctions fournissent des informations essentielles et des commandes utiles pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez consulter [Aperçu](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Admin Password"

    La page Admin Password permet de gérer le mot de passe de l’interface d’administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.

    Pour plus de détails, consultez [Admin Password](../../interface_guide/admin_password.md).

=== "Mise à niveau"

    La page Mise à niveau permet de mettre à jour le firmware de votre routeur vers la dernière version afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à niveau :

    * Mise à niveau du firmware en ligne : recherche automatiquement la dernière version du firmware sur le serveur du fabricant. Vous pouvez l'installer si elle est disponible en ligne.
    * Mise à niveau locale du firmware : téléversez manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous permet de choisir la version et le moment de la mise à niveau.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Veuillez consulter [Mise à niveau](../../interface_guide/upgrade.md) pour des instructions détaillées.

=== "Tâches planifiées"

    La page Tâches planifiées vous permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, afin d'améliorer la praticité et l'efficacité. Les principales fonctions de cette page comprennent :

    * Programmation de l'affichage LED : définissez un planning pour allumer ou éteindre automatiquement les voyants LED du routeur, afin de réduire la pollution lumineuse à certaines heures.
    * Redémarrage planifié : configurez votre routeur pour qu'il redémarre automatiquement à des intervalles définis, afin de maintenir des performances et une stabilité optimales.
    * Programmation de l'état du Wi-Fi : définissez un planning pour contrôler les bandes Wi-Fi 6GHz / 5GHz / 2.4GHz / MLO, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement de votre routeur afin qu'il réponde à vos besoins et préférences.

    Veuillez consulter [Tâches planifiées](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.

---

=== "Fuseau horaire"

    La page Fuseau horaire vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements précis et pour exécuter correctement les configurations basées sur le temps.

    Veuillez consulter [Fuseau horaire](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Reset Firmware"

    La page Réinitialiser le firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware de votre routeur, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Pour plus de détails, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Journal"

    La page Journal donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau du système.
    * Journal du noyau : journaux liés au fonctionnement et aux événements du noyau.
    * Journal de crash : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Journal Cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    De plus, la page comporte un bouton Export Log, qui vous permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Journal](../../interface_guide/log.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Paramètres avancés donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'affiner les paramètres et fonctionnalités du routeur au-delà des options proposées par l'interface de base. Cela inclut des configurations réseau détaillées, les paramètres du pare-feu et d'autres personnalisations système avancées.

    Veuillez consulter [Paramètres avancés](../../interface_guide/advanced_settings.md) pour des instructions détaillées.

## Déclaration UE de conformité {#declaration-of-conformity}

Par la présente, GL TECHNOLOGIES (HONG KONG) LIMITED déclare que le type d'équipement radio [BE9300 Wi-Fi 7 Router, GL-BE9300] est conforme aux exigences essentielles et autres dispositions pertinentes de la Directive 2014/53/UE. Le texte complet de la déclaration de conformité UE est disponible à l'adresse internet suivante: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.
