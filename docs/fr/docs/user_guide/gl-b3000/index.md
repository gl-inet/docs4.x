# Guide d'utilisation du Marble (GL-B3000)

## Aperçu du produit

Le routeur Marble (GL-B3000) se distingue par son design faisant office de cadre photo pour mettre en valeur l'œuvre de votre choix et sublimer votre intérieur. Au-delà de son aspect esthétique, le Marble (GL-B3000) offre d'excellentes performances grâce au Wi‑Fi 6 et à la prise en charge des VPN.

![gl-b3000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/hardware_info/b3000_interface.png){class="glboxshadow"}

## Contenu du colis

- 1 x Marble (GL-B3000)
- 1 x Manuel d'utilisation
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Kit de fixation murale
- 1 x Tampon adhésif
- 1 x Support de routeur
- 1 x Cadre photo (optionnel)
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/first_time_setup/b3000_unboxing.jpg){class="glboxshadow"}

## Configuration initiale du Marble

Regardez ces vidéos d'installation et de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/AiIC_HdJfws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/-U2WTVYRkPU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Mise sous tension

Assemblez l'adaptateur secteur en deux parties. Connectez-le au routeur, puis branchez-le sur une prise électrique. Le routeur démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via le Wi‑Fi ou un câble Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe. (Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.)

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez votre langue, définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

### 4. Configuration Internet

**Note:** Les instructions ci-dessous s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Marble à l'aide des méthodes de connexion Internet prises en charge : Ethernet et Repeater. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), configurez deux connexions Internet.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_ethernet.jpg){class="glboxshadow"}
    
    Connectez un câble Ethernet entre le port WAN du routeur et un équipement en amont, par exemple un modem.
    
    Une fois la connexion Internet établie, un point vert s'affiche dans la section Ethernet de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-b3000/internet/b3000_repeater.jpg){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater, puis cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe du réseau, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert s'affiche dans la section Repeater de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md).

---

## Configurer un VPN

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et permet d'accéder à un réseau distant (serveur VPN). Marble, comme les autres routeurs GL.iNet, prend en charge OpenVPN et WireGuard. Il prend également en charge Tor.

=== "OpenVPN"

    Marble, comme les autres routeurs GL.iNet, prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Marble, comme les autres routeurs GL.iNet, prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor est un service axé sur la confidentialité qui vous permet d'accéder à Internet de manière anonyme. Pour configurer Tor, suivez ce tutoriel :

    * [Comment configurer Tor](../../interface_guide/tor.md)

---

## Réseau sans fil et clients

=== "Wireless"

    La page Wireless vous permet de configurer les paramètres des réseaux Wi‑Fi 5GHz et 2.4GHz, notamment l'activation ou la désactivation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation ou la désactivation d'un BSSID aléatoire, le choix du mode de sécurité Wi‑Fi, la définition du mot de passe Wi‑Fi, la configuration de la visibilité du SSID, ainsi que le mode Wi‑Fi, la bande passante et le canal.

    Pour configurer le réseau sans fil, consultez [Wireless](../../interface_guide/wireless.md).

=== "Clients"

    La page Clients affiche les informations sur les appareils connectés. Pour chaque client, elle indique le nom de l'appareil, le type de connexion (c'est-à-dire via Ethernet ou Wi‑Fi), les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

    Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services cloud

=== "GoodCloud"

    Le service GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    Cette fonctionnalité est disponible à partir du firmware v4.7.

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Spécialement conçue pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils à l'échelle de réseaux entiers, permettant le contrôle des équipements en amont comme en aval. En mettant l'accent sur la gestion réseau globale et sur une future prise en charge du contrôle au niveau matériel, AstroWarp offre une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.

## Applications

=== "Plug-ins"

    Les plug-ins sont des fonctionnalités additionnelles qui étendent les capacités de votre routeur. Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Cette fonction est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant. Pour configurer Dynamic DNS, consultez [Dynamic DNS](../../interface_guide/ddns.md).

---

=== "AdGuard Home"

    AdGuard Home est un outil tiers qui bloque les publicités et le pistage afin de vous protéger.
    
    Pour savoir comment activer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Le contrôle parental regroupe des paramètres conçus pour vous aider à gérer et contrôler les appareils de vos enfants. Il inclut la limitation du temps d'écran et la restriction de l'accès à certains contenus. Marble propose deux options de contrôle parental : la version locale développée par GL.iNet et la version intégrée de Bark, une application de contrôle parental.

    Pour configurer le contrôle parental, consultez [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"
   
    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et à vos applications où que vous soyez. Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "ZeroTier"

    ZeroTier est un service VPN qui vous permet de connecter vos appareils à un réseau virtuel. Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

---

## Paramètres réseau

=== "Firewall"

    La page Firewall apporte des améliorations de sécurité essentielles à votre réseau. Elle comprend notamment Port Forwarding, Open Ports et DMZ. Ces outils vous permettent de gérer et de personnaliser les flux de trafic de votre réseau tout en renforçant sa sécurité.

    * Port Forwarding : redirige un trafic spécifique provenant d'Internet vers des appareils précis de votre réseau afin de permettre l'accès à des services tels que des serveurs de jeu ou des serveurs web.
    * Open Ports : permet de surveiller et de contrôler les ports ouverts sur votre routeur afin de limiter les accès non autorisés et les menaces potentielles.
    * DMZ (Demilitarized Zone) : place un appareil en dehors du pare-feu principal afin de lui permettre un accès Internet sans restriction tout en protégeant le reste du réseau contre les menaces potentielles.

    Pour des instructions détaillées et plus d'informations, consultez [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui permet d'utiliser plusieurs connexions Internet sur votre routeur en même temps (par exemple Cellular, Repeater et Ethernet). Si votre connexion Internet actuelle tombe en panne, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La page LAN vous permet de gérer et de configurer les paramètres du réseau local de votre routeur. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Router IP Address : modifiez l'adresse IP du routeur pour l'adapter à votre configuration réseau.
    * Netmask : définissez le masque de sous-réseau de votre réseau, qui détermine la taille du réseau et la plage d'adresses IP.
    * DHCP : activez ou configurez le protocole Dynamic Host Configuration Protocol, qui attribue automatiquement des adresses IP aux appareils de votre réseau.
    * Address Reservation : réservez des adresses IP spécifiques pour certains appareils afin qu'ils reçoivent toujours la même adresse IP du serveur DHCP.

    Pour des instructions détaillées et plus d'informations, consultez [LAN](../../interface_guide/lan.md).

---

=== "Guest Network"

    La page Guest Network vous permet de créer et de gérer un réseau distinct pour vos invités, en leur donnant accès à Internet tout en gardant votre réseau principal sécurisé. Les principales fonctions de cette page sont les suivantes :

    * Gateway : définissez une plage d'adresses IP spécifique pour le réseau invité afin de le distinguer de votre réseau principal.
    * DHCP : configurez le protocole Dynamic Host Configuration Protocol pour le réseau invité, qui attribue automatiquement des adresses IP aux appareils qui s'y connectent.

    Ces fonctions garantissent à vos invités un accès Internet sans compromettre la sécurité ni les performances de votre réseau principal.
    
    Pour des instructions détaillées et plus d'informations, consultez [Guest Network](../../interface_guide/guest_network.md).

=== "DNS"

    La page DNS propose des options permettant de personnaliser les paramètres Domain Name System de votre routeur afin d'améliorer à la fois la sécurité et les performances. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Encrypted DNS : configurez un DNS chiffré pour empêcher la surveillance ou la falsification de vos données de navigation et garantir la confidentialité.
    * Manual DNS : définissez manuellement les serveurs DNS de votre choix pour mieux contrôler les requêtes DNS et, potentiellement, accélérer leur résolution.
    * DNS Proxy : activez le proxy DNS afin d'acheminer les requêtes DNS de vos appareils via un serveur DNS spécifié, ce qui ajoute une couche de contrôle supplémentaire sur le trafic DNS.

    Ces paramètres vous permettent d'optimiser les performances et la sécurité DNS de votre réseau selon vos besoins.

=== "Network Mode"

    La page Network Mode vous permet de configurer votre routeur pour qu'il fonctionne selon différents modes, afin de répondre à divers besoins réseau. Les modes disponibles sont les suivants :

    * Router : fonctionne comme un routeur standard, en gérant le trafic entre votre réseau local et Internet et en fournissant des fonctions telles que NAT, le pare-feu et DHCP.
    * Access Point : fonctionne comme un point d'accès, en étendant votre réseau filaire existant grâce à une connectivité sans fil sans assurer de routage du trafic.
    * Extender : fonctionne comme un répéteur de portée, en renforçant le signal de votre réseau sans fil existant pour couvrir une zone plus large et éliminer les zones mortes.
    * WDS (Wireless Distribution System) : similaire à Extender ; choisissez WDS si votre routeur principal prend en charge le mode WDS.

    Pour des instructions détaillées et plus d'informations, consultez [Network Mode](../../interface_guide/network_mode.md).

---

=== "IPv6"

    La page IPv6 vous permet de configurer les paramètres IPv6 de votre réseau afin de prendre en charge le protocole Internet le plus récent. Sur cette page, vous pouvez activer IPv6 et sélectionner l'un des quatre modes proposés selon vos besoins réseau :

    * Native : obtient une adresse IPv6 directement auprès de votre FAI pour une connectivité IPv6 native simple et efficace.
    * Passthrough : laisse le trafic IPv6 traverser le routeur vers les appareils de votre réseau, ce qui assure un pont réseau sans que le routeur gère lui-même le routage IPv6.
    * NAT6 : utilise la traduction d'adresses réseau pour IPv6 (NAT6) afin de traduire les adresses IPv6 internes et externes, de manière similaire au fonctionnement du NAT pour IPv4.
    * Static IPv6 : permet de configurer manuellement une adresse IPv6 statique pour votre routeur afin de garantir une adresse fixe pour une connectivité stable et une gestion plus simple des services réseau.

    Ces paramètres vous aident à tirer parti des avantages d'IPv6, notamment un espace d'adressage plus vaste, des fonctions de sécurité améliorées et de meilleures performances.

    Pour des instructions détaillées et plus d'informations, consultez [IPv6](../../interface_guide/ipv6.md).

=== "MAC Address"

    La page MAC Address vous permet d'afficher et de gérer les adresses Media Access Control (MAC) associées à votre routeur. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Factory Default : affiche les adresses MAC par défaut du routeur pour les modes Ethernet et Repeater, afin de fournir une référence aux paramètres matériels d'origine.
    * Clone : clone l'adresse MAC d'un appareil client spécifique. Cette fonction est particulièrement utile lorsque l'accès au réseau est limité à certains appareils.
    * Manual : permet de définir manuellement une adresse MAC personnalisée pour votre routeur. Vous pouvez également utiliser le bouton Random pour générer une adresse MAC aléatoire, ce qui offre davantage de souplesse et de confidentialité.

    Ces fonctions vous permettent de gérer efficacement les adresses MAC de votre routeur afin d'assurer la compatibilité et la flexibilité dans différents environnements réseau.

    Pour des instructions détaillées et plus d'informations, consultez [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctions qu'il ne propose peut-être pas, notamment AdGuard Home, le DNS chiffré et le VPN.
    
    Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    La page IGMP Snooping vous permet de configurer des paramètres qui optimisent la gestion du trafic multicast au sein de votre réseau. IGMP Snooping écoute et extrait les informations des paquets du protocole IGMP, puis établit et maintient des tables de transfert multicast de couche 2. Cela garantit que les données des groupes multicast ne sont transmises qu'aux hôtes ayant rejoint le groupe, évitant ainsi que du trafic multicast non désiré n'atteigne les autres hôtes.

    Ces paramètres contribuent à optimiser les performances et l'efficacité du réseau, en particulier dans les environnements comportant un trafic multicast important, comme le streaming vidéo ou les jeux en ligne.

    Pour des instructions détaillées et plus d'informations, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Acceleration"

    La page Network Acceleration vous permet d'activer des fonctions qui réduisent la charge CPU et accélèrent le transfert des paquets de trafic, améliorant ainsi les performances globales du réseau. Cependant, l'activation de l'accélération réseau peut entrer en conflit avec certaines fonctionnalités.

    Pour des instructions détaillées et plus d'informations, consultez [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT Settings"

    La page NAT Settings vous permet de configurer les options Network Address Translation (NAT) afin d'optimiser certaines applications et d'améliorer les performances du réseau. Les principaux réglages disponibles sur cette page sont les suivants :

    * Enable Full Cone NAT : Full Cone NAT peut être utilisé pour réduire la latence dans les jeux en offrant un chemin plus direct et moins restrictif au trafic réseau. Cependant, son activation peut être moins sûre, car elle permet plus facilement aux hôtes externes d'initier des connexions vers les appareils internes.
    * Enable SIP ALG : Session Initiation Protocol Application Layer Gateway (SIP ALG) peut contribuer à atténuer les problèmes causés par les NAT multiples, qui peuvent affecter les services VoIP. Cependant, dans la plupart des cas, SIP ALG n'est pas bénéfique et peut entraîner des problèmes tels qu'un son à sens unique (une seule personne entend l'autre), des téléphones qui ne sonnent pas pendant un appel, des téléphones qui se déconnectent alors qu'ils sont connectés, ou des appels redirigés directement vers la messagerie vocale.

    Ces paramètres vous permettent d'adapter le comportement NAT du routeur aux besoins de votre réseau, en équilibrant les gains de performance avec les considérations de sécurité et de fonctionnement.

    Pour des instructions détaillées et plus d'informations, consultez [NAT Settins](../../interface_guide/nat_settings.md).

---

## Paramètres système

=== "Overview"

    La page Overview fournit une vue d'ensemble complète de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * CPU Average Load : surveillez la charge moyenne du CPU du routeur pour évaluer les performances et identifier d'éventuels goulots d'étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée afin de mieux gérer les ressources.
    * Flash Usage : consultez l'utilisation du stockage flash du routeur afin de vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * System Info : accédez à des informations détaillées sur le système de votre routeur, notamment la version du firmware, l'uptime et l'état du réseau.
    * LED Control : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l'appareil.
    
    Ces fonctions fournissent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Pour des instructions détaillées et plus d'informations, consultez [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La page Upgrade permet de mettre à jour le firmware de votre routeur vers la dernière version afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à niveau :

    * Online Upgrade : recherche et installe automatiquement la dernière version du firmware depuis le serveur du fabricant, ce qui simplifie la mise à jour.
    * Local Upgrade : permet de téléverser manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous donne le contrôle sur la version installée et le moment de l'opération.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Pour des instructions détaillées et plus d'informations, consultez [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La page Scheduled Tasks vous permet d'automatiser diverses fonctions du routeur selon un calendrier prédéfini, pour plus de confort et d'efficacité. Les principales fonctions de cette page sont les suivantes :

    * LED Display Schedule : définissez un calendrier pour allumer ou éteindre automatiquement les voyants LED du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Schedule Reboot : configurez le redémarrage automatique du routeur à intervalles définis afin de maintenir des performances et une stabilité optimales.
    * 5GHz Wi-Fi Status Schedule : définissez un calendrier pour activer ou désactiver la bande Wi‑Fi 5GHz à certains moments, afin d'optimiser l'utilisation du réseau et l'efficacité énergétique.
    * 2.4GHz Wi-Fi Status Schedule : définissez un calendrier pour contrôler la bande Wi‑Fi 2.4GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur afin qu'il réponde à vos besoins et préférences spécifiques.

    Pour des instructions détaillées et plus d'informations, consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements précis et pour garantir le bon fonctionnement des configurations basées sur l'heure.

    Pour des instructions détaillées et plus d'informations, consultez [Time Zone](../../interface_guide/time_zone.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés au fonctionnement et aux événements du noyau.
    * Crash Log : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, cette page propose un bouton Export Log, qui vous permet d'exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées et plus d'informations, consultez [Log](../../interface_guide/log.md).

=== "Security"

    La page Security vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend notamment les options suivantes :

    * Admin Password : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Local Access Control : gérez et restreignez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurez et restreignez l'accès à l'interface du routeur depuis des emplacements distants via Internet, pour une meilleure protection contre les menaces externes.
    * Open Ports on Router : contrôlez les ports ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.

    Pour des instructions détaillées et plus d'informations, consultez [Security](../../interface_guide/security.md).

---

=== "Reset Firmware"

    La page Reset Firmware vous permet de réinitialiser la version actuelle du firmware de votre routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Cette opération restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre du firmware actuel.

    Pour des instructions détaillées et plus d'informations, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès aux options de configuration avancée via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster avec précision les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des réglages de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées et plus d'informations, consultez [Advanced Settings](../../interface_guide/advanced_settings.md).
