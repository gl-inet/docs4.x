# Guide d'utilisation de Flint 2 (GL-MT6000)

## Aperçu du produit

Flint 2 (GL-MT6000) est un routeur Wi‑Fi 6 pour la maison et le bureau, parfaitement adapté aux transferts de données intensifs, à la connexion simultanée d'un grand nombre d'appareils ou aux environnements de jeu à très faible latence. Flint 2 offre des vitesses WireGuard pouvant atteindre 900 Mbps. Il prend également en charge des fonctions avancées de redondance réseau, notamment le Multi-WAN, la conmutation par erreur et l'équilibrage de charge, afin de garantir un réseau ininterrompu.

![gl-mt6000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/hardware_info/gl-mt6000_interface.jpg){class="glboxshadow"}

## Contenu du colis

- 1 x Flint 2 (GL-MT6000)
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![gl-mt6000 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt6000/first_time_setup/gl-mt6000_unboxing.jpg){class="glboxshadow"}

Découvrez ci-dessous la vidéo de déballage du Flint 2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ru1O-zxKgKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Comment configurer Flint 2

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise un autre routeur GL.iNet pour illustrer la configuration, mais les étapes sont identiques pour le Flint 2 et les autres modèles de routeurs.)</small>

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur puis sur une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet. 

- Wi‑Fi

    Sur votre appareil, accédez à Settings -> WLAN, repérez le nom du réseau Wi-Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. Vous trouverez le nom de réseau et le mot de passe par défaut sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**. 

Lors de la confirmation des paramètres Wi‑Fi, veuillez noter que si vous modifiez les informations Wi‑Fi, vous devrez reconnecter votre appareil au Wi‑Fi du routeur avec les nouveaux identifiants.

### 4. Configuration de la connexion Internet

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

## Comment configurer un VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Flint 2 (comme les autres routeurs GL.iNet) prend en charge OpenVPN et WireGuard. Il prend également en charge Tor.

=== "OpenVPN" 

    Flint 2 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Flint 2 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet des communications anonymes sur Internet. Il achemine le trafic Internet via une série de serveurs bénévoles (nœuds) afin de masquer l'emplacement et l'usage de l'utilisateur, rendant les activités en ligne difficiles à tracer. 
    
    * [Comment configurer Tor](../../interface_guide/tor.md).

## Réseau sans fil et clients

=== "Réseau sans fil"

    La page Réseau sans fil vous permet de configurer les paramètres des réseaux Wi‑Fi 5 GHz et 2,4 GHz, notamment l'activation/la désactivation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation/la désactivation du BSSID aléatoire, le choix du mode de sécurité Wi‑Fi, la définition du mot de passe Wi‑Fi, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi‑Fi, de la bande passante et du canal.

    Pour configurer le réseau sans fil, consultez [Réseau sans fil](../../interface_guide/wireless.md).

=== "Clients"

    La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom de l'appareil, le type de connexion (Ethernet ou Wi-Fi), les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de réserver une IP, de bloquer le client ou d'effectuer d'autres actions.

    Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    Le service GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer. 
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Conçue spécialement pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils sur l'ensemble du réseau, y compris les appareils de niveau supérieur et inférieur. Axée sur la gestion à l'échelle du réseau et sur une future prise en charge du contrôle matériel, AstroWarp fournit une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables. 
    
    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant ainsi de le personnaliser et d'en étendre les capacités. 
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est utile aux utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant. 
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution centralisée de stockage de données qui permet à plusieurs utilisateurs et appareils d'accéder à des fichiers et de les partager via un réseau. 
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traceurs à l'échelle du réseau qui agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés au réseau domestique. 
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

---

=== "Contrôle parental"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre l'accès à certains contenus. 
    
    Le Flint 2 propose deux options de contrôle parental : la version locale développée par GL.iNet et la version intégrée de Bark.

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier est une solution réseau définie par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, reliant les appareils comme s'ils se trouvaient sur le même réseau local. 
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications partout. 
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

---

## Paramètres réseau

=== "Redirection de ports"

    La redirection de port permet à des serveurs et appareils distants sur Internet d'accéder à des appareils situés sur un réseau privé. 
    
    Pour configurer la redirection de ports, consultez [Redirection de ports](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui permet de configurer le routeur avec plusieurs connexions Internet simultanées (par ex. cellular, repeater et ethernet). Si votre connexion Internet actuelle tombe en panne, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu. 

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Le LAN, ou réseau local, est un réseau qui connecte des ordinateurs et des appareils dans une zone géographique limitée, comme une maison ou un bureau. Il permet des transferts de données rapides et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux. 
    
    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

=== "Réseau invité"

    La page Guest Network permet de définir un sous-réseau dans les plages d'adresses IPv4 privées 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de passerelle et de masque réseau, et de configurer des paramètres de sécurité tels que l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Tutoriel LAN](../../interface_guide/guest_network.md).

---

=== "DNS"

    La page DNS permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS et le remplacement des paramètres DNS de tous les clients, d'autoriser un DNS personnalisé à remplacer le DNS VPN, et de configurer le mode des paramètres DNS en automatique ou en saisissant manuellement des serveurs DNS provenant de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Port Ethernet"

    La page Ethernet Port permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port.md).

=== "Mode réseau"

    Le mode réseau désigne les paramètres de configuration qui déterminent comment un appareil se connecte à un réseau et communique avec d'autres appareils. 
    
    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet. 
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

---

=== "Passerelle Drop-in"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctions qu'il ne possède pas forcément, notamment AdGuard Home, le DNS chiffré et le VPN. 
    
    Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    L'IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast. 
    
    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Accélération réseau"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.
    
    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

=== "Paramètres NAT"

    La page NAT Settings permet d'activer ou de désactiver les fonctionnalités Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [Paramètres NAT](../../interface_guide/nat_settings.md).

---

## Paramètres système

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

=== "Mise à niveau"

    La page Upgrade sert à mettre à jour le firmware du routeur vers la dernière version, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : vérifie et installe automatiquement la dernière version du firmware depuis le serveur du fabricant, ce qui simplifie la mise à jour.
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

---

=== "Fuseau horaire"

    La page Time Zone permet de définir le fuseau horaire correct pour le routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements exacts et pour assurer l'exécution correcte des configurations basées sur le temps.

    Veuillez consulter [Time Zone](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Journal"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et la surveillance des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau système.
    * Journal du noyau : journaux liés aux opérations et événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Journal cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, cette page propose un bouton Export Log, qui permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Log](../../interface_guide/log.md) pour des instructions détaillées.

---

=== "Sécurité"

    La page Security permet de configurer divers paramètres de sécurité pour protéger votre réseau et votre routeur contre les accès non autorisés. Cette page inclut notamment :

    * Mot de passe administrateur : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Contrôle d'accès local : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la sécurité contre les menaces externes.
    * Ports ouverts sur le routeur : contrôlez quels ports sont ouverts sur le routeur, afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé et à protéger à la fois le routeur et les appareils connectés.

    Veuillez consulter [Sécurité](../../interface_guide/security.md) pour des instructions détaillées.

=== "Réinitialiser le firmware"

    La page Reset Firmware permet de réinitialiser la version actuelle du firmware du routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Veuillez consulter [Reset Firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, ce qui permet aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de base de l'interface. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Veuillez consulter [Advanced Settings](../../interface_guide/advanced_settings.md) pour des instructions détaillées.
