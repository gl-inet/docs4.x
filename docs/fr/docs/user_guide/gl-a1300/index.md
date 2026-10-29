# Guide d'utilisation de Slate Plus (GL-A1300) {#slate-plus-gl-a1300-user-guide}

## Aperçu du produit {#product-overview}

Slate Plus (GL-A1300) est un routeur de voyage de poche doté d'un processeur puissant, optimisé pour la stabilité du réseau et le traitement efficace du chiffrement VPN. Il intègre nos dernières fonctionnalités de sécurité et fonctionne avec la dernière version du système d'exploitation OpenWrt. Il est conçu pour les voyageurs fréquents ayant un usage intensif des réseaux VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Contenu du colis {#package-contents}

Veuillez noter que l'adaptateur inclus dans le colis dépend de votre pays de livraison.

Le colis comprend :

- 1 x Manuel d'utilisation
- 1 x Slate Plus (GL-A1300)
- 1 x Câble Ethernet
- 1 x Carte de remerciement
- 1 x Carte de garantie
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Configuration initiale du Slate Plus {#how-to-set-up-slate-plus}

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Pour obtenir des conseils supplémentaires, consultez [Première configuration](../../faq/first_time_setup.md).

### 1. Mise sous tension {#1-power-on}

Assemblez l'adaptateur secteur en deux parties. Connectez-le au routeur, puis branchez-le sur une prise électrique. Le routeur démarre automatiquement.

### 2. Connecter un appareil {#2-connect-device}

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via le Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi-Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi du routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe. Le nom de réseau et le mot de passe par défaut sont imprimés sur l'étiquette située sous le routeur.

### 3. Se connecter au panneau d'administration web {#3-log-in-to-web-admin-panel}

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. Choisissez votre langue, définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

Lors de la confirmation des informations Wi‑Fi, notez que si vous modifiez les paramètres Wi‑Fi, vous devrez reconnecter votre appareil au Wi‑Fi du routeur à l'aide des identifiants mis à jour.

### 4. Configuration Internet {#4-internet-setup}

**Note:** Les instructions ci-dessous s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Slate Plus en utilisant l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Ethernet"

    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

    Connectez un câble Ethernet entre le port WAN du routeur et un équipement en amont, par exemple un modem.
    
    Une fois la connexion Internet établie, un point vert s'affiche dans la section Ethernet de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater, puis cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert s'affiche dans la section Repeater de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou une clé USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez aux réglages et activez **USB Tethering**.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie, un point vert s'affiche dans la section Tethering de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du routeur. Cette méthode est utile pour partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie, un point vert s'affiche dans la section Cellular de la page INTERNET.

    Pour des instructions détaillées, consultez [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md).

---

## Sans fil {#wireless}

La page Wireless permet de configurer les paramètres des réseaux Wi-Fi 5 GHz et 2.4 GHz, notamment l’activation du Wi-Fi, la puissance d’émission, le nom Wi-Fi (SSID), le mode de sécurité et le mot de passe Wi-Fi, la visibilité du SSID, le mode Wi-Fi, la bande passante et le canal.

Pour configurer le réseau sans fil, consultez [Wireless](../../interface_guide/wireless_v4.8.md).

## Clients {#clients}

La page Clients affiche les informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## VPN {#vpn}

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Slate Plus (comme les autres routeurs GL.iNet) prend en charge OpenVPN et WireGuard. Il prend également en charge Tor.

=== "OpenVPN"

    Slate Plus (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Slate Plus (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet une communication anonyme sur Internet. Il fait transiter le trafic Internet via une série de serveurs exploités par des bénévoles (nœuds) afin de masquer la localisation et l'utilisation de l'utilisateur, rendant plus difficile la traçabilité des activités en ligne.
    
    * [Comment configurer Tor](../../interface_guide/tor.md).

## Applications {#applications}

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant de le personnaliser et d'en étendre les capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il associe un nom de domaine à l'adresse IP publique dynamique de votre routeur, ce qui vous permet d'accéder à votre réseau à distance sans adresse IP statique.
    
    Pour configurer Dynamic DNS, consultez [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Le service de gestion Cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "Network Storage"

    Le stockage réseau désigne une solution de stockage de données centralisée qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager via un réseau.
    
    Pour configurer le stockage réseau, consultez [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage à l'échelle du réseau pour les publicités et les traqueurs. Elle agit comme un serveur DNS afin de filtrer les contenus indésirables sur tous les appareils connectés au réseau domestique.
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control aide à gérer et à contrôler les appareils de vos enfants, notamment en limitant leur temps d’écran et l’accès à certains contenus.

    Pour configurer le contrôle parental, consultez [Parental Control](../../interface_guide/parental_control.md).

=== "ZeroTier"

    ZeroTier est une solution de réseau défini par logiciel qui permet de créer des réseaux virtuels sécurisés sur Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et à vos applications où que vous soyez.
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

## Réseau {#network}

=== "Firewall"

    La page Firewall apporte des améliorations de sécurité essentielles à votre réseau. Elle comprend notamment Port Forwarding, Open Ports et DMZ. Ces outils vous permettent de gérer et de personnaliser les flux de trafic de votre réseau tout en renforçant sa sécurité.

    * Port Forwarding : redirige un trafic spécifique provenant d'Internet vers des appareils précis de votre réseau afin de permettre l'accès à des services tels que des serveurs de jeu ou des serveurs web.
    * Open Ports : permet de surveiller et de contrôler les ports ouverts sur votre routeur afin de limiter les accès non autorisés et les menaces potentielles.
    * DMZ (Demilitarized Zone) : expose un appareil à Internet en lui redirigeant tout le trafic entrant.

    Pour configurer le pare-feu, consultez [Firewall](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer simultanément plusieurs connexions Internet sur votre routeur (par exemple Ethernet, Repeater et Tethering). Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Le LAN, ou Local Area Network, est un réseau qui relie des ordinateurs et des appareils dans une zone géographique limitée, comme un domicile ou un bureau. Il permet un transfert de données à haut débit et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

=== "Guest Network"

    Cette page vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de la passerelle et du masque de sous-réseau, et de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d’activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients et d’autoriser les DNS personnalisés à remplacer les DNS VPN. Vous pouvez utiliser les serveurs DNS obtenus automatiquement auprès des appareils en amont ou spécifier manuellement des serveurs DNS personnalisés.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    Le mode réseau désigne les paramètres de configuration qui déterminent la manière dont un appareil se connecte à un réseau et communique avec les autres appareils.
    
    Pour configurer le mode réseau, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre pratiquement illimité d'adresses IP uniques, ce qui est essentiel pour répondre à l'augmentation du nombre d'appareils connectés à Internet.
    
    Pour configurer IPv6, consultez [IPV6](../../interface_guide/ipv6.md).

=== "MAC Address"

    La page MAC Address vous permet d'afficher et de gérer les adresses Media Access Control (MAC) associées à votre routeur. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Factory Default : affiche les adresses MAC par défaut du routeur pour les modes Ethernet et Repeater, afin de fournir une référence aux paramètres matériels d'origine.
    * Clone : clone l'adresse MAC d'un appareil client spécifique. Cette fonction est particulièrement utile lorsque l'accès au réseau est limité à certains appareils.
    * Manual : permet de définir manuellement une adresse MAC personnalisée pour votre routeur. Vous pouvez également utiliser le bouton Random pour générer une adresse MAC aléatoire, ce qui offre davantage de souplesse et de confidentialité.

    Ces fonctions vous permettent de gérer efficacement les adresses MAC de votre routeur afin d'assurer la compatibilité et la flexibilité dans différents environnements réseau.

    Pour gérer l'adresse MAC, consultez [MAC Address](../../interface_guide/mac_address.md).

---

=== "Drop-in Gateway"

    Drop-in gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, consultez les liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Configuration de Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "IGMP Snooping"

    IGMP snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "NAT Settings"

    La page NAT Settings vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [NAT Settings](../../interface_guide/nat_settings.md).

## Système {#system}

=== "Overview"

    La page Overview fournit une vue d'ensemble complète de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * CPU Average Load : surveillez la charge moyenne du processeur du routeur afin d’évaluer les performances et de repérer les éventuels goulets d’étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée afin de mieux gérer les ressources.
    * LED Control : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l'appareil.
    * Flash Usage : consultez l'utilisation du stockage flash du routeur afin de vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Device Info : accédez à des informations détaillées sur le système de votre routeur, notamment l'uptime, le nom d'hôte, le modèle, l'architecture, la version OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC de l'appareil et son S/N.
    * External Storage : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que des clés USB ou des cartes TF.
    
    Ces fonctions fournissent des informations et des contrôles essentiels pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Pour des instructions détaillées, consultez [Overview](../../interface_guide/system_overview.md).

=== "Upgrade"

    La page Upgrade permet de mettre à jour le firmware de votre routeur vers la dernière version afin d'améliorer les performances, la sécurité et les fonctionnalités. Cette page propose deux options de mise à niveau :

    * Firmware Online Upgrade : recherche automatiquement la dernière version du firmware sur le serveur du fabricant. Vous pouvez l'installer si elle est disponible en ligne.
    * Firmware Local Upgrade : permet de téléverser manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous donne le contrôle sur la version installée et le moment de l'opération.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Pour des instructions détaillées, consultez [Upgrade](../../interface_guide/upgrade.md).

=== "Scheduled Tasks"

    La page Scheduled Tasks vous permet d'automatiser diverses fonctions du routeur selon un calendrier prédéfini, pour plus de confort et d'efficacité. Les principales fonctions de cette page sont les suivantes :

    * LED Display Schedule : définissez un calendrier pour allumer ou éteindre automatiquement les voyants LED du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Schedule Reboot : configurez le redémarrage automatique du routeur à intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Wi-Fi Status Schedule : définissez un calendrier pour contrôler les bandes Wi‑Fi 5GHz / 2.4GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur afin qu'il réponde à vos besoins et préférences spécifiques.

    Pour des instructions détaillées, consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements précis et pour garantir le bon fonctionnement des configurations basées sur l'heure.

    Pour des instructions détaillées, consultez [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La page Toggle Button Settings vous permet de configurer le bouton bascule physique de votre routeur, afin d'y attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonctionnalité offre des raccourcis pratiques pour les tâches et réglages courants, améliore l'expérience utilisateur et simplifie la gestion du routeur.

    Pour des instructions détaillées, reportez-vous à [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés au fonctionnement et aux événements du noyau.
    * Crash Log : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, cette page propose un bouton Export Log, qui vous permet d'exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées, consultez [Log](../../interface_guide/log.md).

---

=== "Security"

    **Remarque**: Cette fonctionnalité est disponible depuis la version 4.5.

    La page Security vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend notamment les options suivantes :

    * Admin Password : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Local Access Control : gérez et restreignez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurez et restreignez l'accès à l'interface du routeur depuis des emplacements distants via Internet, pour une meilleure protection contre les menaces externes.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.
    
    Pour des instructions détaillées, consultez [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    La page Reset Firmware vous permet de réinitialiser la version actuelle du firmware de votre routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Cette opération restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre du firmware actuel.

    Pour des instructions détaillées, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès aux options de configuration avancée via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster avec précision les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des réglages de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées, consultez [Advanced Settings](../../interface_guide/advanced_settings.md).
