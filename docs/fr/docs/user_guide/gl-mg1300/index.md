# Guide d'utilisation de Mango 2 (GL-MG1300)

## Aperçu du produit

Mango 2 (GL-MG1300) est le premier mini-routeur de voyage Wi-Fi 5 double bande de GL.iNet, doté d'un design ultrafin et portable. Il offre des débits théoriques de 400 Mbit/s (2,4 GHz) et 866 Mbit/s (5 GHz), avec une configuration MIMO 2×2. OpenVPN et WireGuard sont préinstallés ; le routeur prend en charge plus de 30 services VPN, chiffre automatiquement tout le trafic réseau et permet la gestion à distance via GoodCloud, conciliant ainsi performances, praticité et sécurité.

![mg1300 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/product_info/mg1300_overview.jpg){class="glboxshadow"}

## Contenu du colis

- 1 x Mango 2 (GL-MG1300)
- 1 x Manuel d'utilisation
- 1 x Câble d'alimentation USB-C vers USB-C
- 1 x Carte de remerciement

## Comment configurer Mango 2

Pour configurer Mango 2, utilisez l'une des quatre méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering ou Cellular. Suivez les étapes ci-dessous.

### 1. Mise sous tension

Branchez le câble d'alimentation USB Type-C sur le port d'alimentation du routeur. Connectez l'autre extrémité à un adaptateur secteur 5 V/2 A (non fourni), puis branchez-le sur une prise électrique.

### 2. Connecter un appareil

Connectez un appareil (par exemple, un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi-Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Settings -> WLAN, recherchez le nom du réseau Wi-Fi du routeur dans la liste des réseaux disponibles et saisissez le mot de passe. Le nom et le mot de passe par défaut figurent sur l'étiquette sous le routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue, définissez le mot de passe administrateur, puis cliquez sur **Apply**.

Si vous modifiez les informations Wi-Fi, reconnectez ensuite votre appareil au réseau Wi-Fi du routeur avec les nouveaux identifiants.

### 4. Configuration de la connexion Internet

**Remarque :** Les instructions suivantes concernent les utilisateurs qui configurent le routeur depuis le GL.iNet Web Admin Panel. Si vous préférez l'application GL.iNet, [téléchargez-la](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez Mango 2 avec l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering ou Cellular. Pour utiliser [Multi-WAN](../../interface_guide/multi-wan.md), configurez plusieurs connexions Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_ethernet.png){class="glboxshadow"}

    Connectez le port WAN du Mango 2 à un appareil en amont (par ex. un modem) à l'aide d'un câble Ethernet.

    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_repeater.png){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi-Fi parmi les réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.

    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Repeater de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile (par ex. un smartphone ou un dongle USB) au port USB du Mango 2 à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Settings et activez **USB Tethering** ou **Personal Hotspot**. Sur un iPhone, appuyez sur **Trust This Device** si vous y êtes invité.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.

    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Tethering de la page INTERNET.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mg1300/internet/mg1300_cellular.png){class="glboxshadow"}

    Avec Mango 2, vous pouvez connecter directement un modem USB-C ou utiliser un adaptateur USB-C vers USB-A pour connecter un modem USB-A.

    Branchez un modem USB cellulaire sur le port USB du Mango 2. Cela permet de partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion à Internet établie avec succès, un point vert apparaîtra dans la section Cellular de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

---

Vous trouverez ci-dessous un aperçu des fonctions du panneau d'administration web de Mango 2.

## Réseau sans fil

La page Wireless permet de configurer Main Network, Guest Network et IoT Network. Pour chaque type de réseau Wi-Fi, les bandes 5 GHz et 2,4 GHz peuvent être configurées indépendamment. Vous pouvez également activer et définir les paramètres de base de chaque bande, notamment le SSID Wi-Fi, le mode de sécurité, le mot de passe et le BSSID aléatoire.

Pour configurer le réseau sans fil, consultez [Réseau sans fil](../../interface_guide/wireless.md).

## Clients

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet également de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GL.iNet Account"

    GL.iNet Account permet de connecter et de gérer vos appareils et services Cloud. Vous pouvez accéder facilement à GoodCloud et à la glinet App afin de gérer votre réseau de façon sécurisée et pratique, où que vous soyez et à tout moment.

    Pour configurer GL.iNet Account, consultez [GL.iNet Account](../../interface_guide/glinet_account.md).

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} permet d'accéder à distance aux routeurs GL.iNet et de les gérer facilement.

=== "GoodPAS"

    GoodPAS est une fonction réseau avancée conçue pour offrir un accès à distance et une gestion des appareils fluides. Développé spécialement pour l'intégration aux routeurs GL.iNet, GoodPAS utilise le protocole AmneziaWG avec obfuscation intégrée du trafic afin d'assurer des connexions sécurisées et stables. Il étend votre réseau domestique en toute sécurité partout dans le monde, vous permettant d'accéder aux ressources de votre domicile tandis que tout le trafic semble provenir de l'adresse IP publique de celui-ci.

## VPN

Un VPN (réseau privé virtuel) crée une connexion sécurisée et chiffrée entre votre appareil et le serveur VPN. Il renforce la confidentialité et la sécurité (client VPN) et permet d'accéder à un réseau distant (serveur VPN). Mango 2 prend en charge OpenVPN et WireGuard.

=== "OpenVPN"

    Mango 2 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango 2 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui permet de configurer le routeur avec plusieurs connexions Internet simultanées (par ex. cellular, repeater et ethernet). Si votre connexion Internet actuelle tombe en panne, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "Subnet"

    Subnet centralise la gestion du LAN, de Guest Network, d'IoT Network et des réseaux VLAN personnalisés. Vous pouvez ainsi créer et gérer plusieurs sous-réseaux afin d'isoler différents types d'appareils ou de trafic.

    Pour configurer cette fonction, consultez [Subnet](../../interface_guide/subnet.md).

=== "Ethernet Port"

    La page Ethernet Port permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port réseau.

    Pour gérer les ports Ethernet, consultez [Port Ethernet](../../interface_guide/ethernet_port_v4.10.md).

---

=== "DNS"

    La page DNS permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS et le remplacement des paramètres DNS de tous les clients, d'autoriser un DNS personnalisé à remplacer le DNS VPN, et de configurer le mode des paramètres DNS en automatique ou en saisissant manuellement des serveurs DNS provenant de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, ce qui est essentiel pour prendre en charge le nombre croissant d'appareils connectés à Internet.

    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

=== "IGMP Snooping"

    L'IGMP snooping est une technique d'optimisation réseau utilisée sur les commutateurs Ethernet pour gérer et contrôler le trafic multicast.

    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

---

=== "Network Mode"

    La page Network Mode permet de configurer le rôle opérationnel du routeur pour répondre à différents besoins de déploiement réseau. Vous pouvez choisir parmi plusieurs modes, de la couverture Wi-Fi domestique aux réseaux multi-liens d'entreprise ; chaque mode active ou désactive des fonctions précises du routeur afin d'optimiser les performances.

    Pour configurer cette fonction, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "Network Acceleration"

    L'accélération réseau peut réduire la charge du CPU et accélérer le transfert des paquets réseau.

    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

## Contrôle des flux

=== "Parental Control"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre l'accès à certains contenus.

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control.md).

## Sécurité

=== "Port Forwarding"

    La redirection de port permet à des serveurs et appareils distants sur Internet d'accéder à des appareils situés sur un réseau privé.

    Pour configurer la redirection de ports, consultez [Redirection de ports](../../interface_guide/port_forwarding.md).

=== "Admin Access"

    Admin Access permet de configurer divers paramètres de sécurité destinés à protéger le réseau et le routeur contre les accès non autorisés.

    Pour configurer cette fonction, consultez [Admin Access](../../interface_guide/admin_access.md).

=== "NAT Mode"

    La page NAT Settings permet d'activer ou de désactiver les fonctionnalités Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [Paramètres NAT](../../interface_guide/nat_settings.md).

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

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et applications partout.

    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

## Système

=== "Aperçu"

    La page Overview fournit une vue d'ensemble complète de l'état actuel du routeur et de ses performances. Sur cette page, vous pouvez voir :

    * Charge moyenne du CPU : surveillez la charge moyenne du CPU du routeur afin d'évaluer les performances et d'identifier d'éventuels goulots d'étranglement.
    * Utilisation de la mémoire : vérifiez la quantité de mémoire utilisée sur le routeur afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser ses indicateurs visuels.
    * Flash : consultez l'utilisation de la mémoire flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez à des informations détaillées sur le système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC et le numéro de série.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, comme les clés USB ou les cartes TF.

    Ces fonctionnalités offrent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement du routeur.

    Veuillez consulter [Overview](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Admin Password"

    La page Admin Password permet de définir ou de modifier le mot de passe de l'interface d'administration du routeur.

    Le mot de passe administrateur doit respecter les exigences suivantes :

    * 10 caractères minimum et 63 caractères maximum.
    * Les lettres (sensibles à la casse), les chiffres et les symboles `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sont autorisés.
    * Au moins deux types parmi les majuscules, les minuscules, les chiffres et les symboles sont requis.

=== "Mise à niveau"

    La page Upgrade sert à mettre à jour le firmware du routeur vers la dernière version, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à jour :

    * Firmware Online Upgrade : vérifie et installe automatiquement la dernière version du firmware depuis le serveur du fabricant, ce qui simplifie la mise à jour.
    * Firmware Local Upgrade : permet de téléverser manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous laisse le contrôle sur la version et le moment de la mise à jour.

    Ces options vous permettent de maintenir le routeur à jour avec les dernières améliorations et correctifs.

    Veuillez consulter [Upgrade](../../interface_guide/upgrade.md) pour des instructions détaillées.

---

=== "Tâches planifiées"

    La page Scheduled Tasks permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, afin d'améliorer le confort d'utilisation et l'efficacité. Les principales fonctionnalités de cette page incluent :

    * Contrôle des LED : activez ou désactivez les voyants LED du routeur pour personnaliser ses indicateurs visuels.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis, afin de préserver des performances et une stabilité optimales.
    * Planification de l'état du Wi-Fi : définissez un calendrier pour contrôler les bandes Wi-Fi 5 GHz / 2.4 GHz , afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.

    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur, afin qu'il réponde à vos besoins et préférences spécifiques.

    Veuillez consulter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.

=== "Fuseau horaire"

    La page Time Zone permet de définir le fuseau horaire correct pour le routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce paramètre est essentiel pour conserver des enregistrements exacts et pour assurer l'exécution correcte des configurations basées sur le temps.

    Veuillez consulter [Time Zone](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Paramètres du bouton à bascule"

    La page Paramètres du bouton à bascule vous permet de configurer le bouton physique du routeur et de lui attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonctionnalité offre des raccourcis pratiques pour les tâches et réglages courants, améliorant l'expérience utilisateur et simplifiant la gestion du routeur.

    Veuillez consulter [Paramètres du bouton à bascule](../../interface_guide/toggle_button_settings.md) pour des instructions détaillées.

---

=== "Réinitialiser le firmware"

    La page Reset Firmware permet de réinitialiser la version actuelle du firmware du routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version actuellement installée du firmware. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre avec les paramètres par défaut du firmware actuel.

    Veuillez consulter [Reset Firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

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

## Déclaration de conformité

Par la présente, GL TECHNOLOGIES (HONG KONG) LIMITED déclare que le type d’équipement radio [Mini routeur de voyage bi‑bande, GL‑MG1300] est conforme aux exigences essentielles et aux autres dispositions pertinentes de la directive 2014/53/UE. Le texte intégral de la déclaration de conformité UE est disponible à l’adresse Internet suivante: [https://www.gl-inet.com/products/certificate](https://www.gl-inet.com/products/certificate){target="_blank"}.