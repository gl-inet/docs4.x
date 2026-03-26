# Guide d'utilisation du Creta (GL-AR750)

## Aperçu du produit

Creta (GL-AR750) est un routeur de voyage AC double bande. La double bande simultanée prend en charge un débit sans fil allant jusqu'à 733Mbps (2.4GHz : 300Mbps + 5GHz : 433Mbps). Creta peut transformer un réseau public en Wi‑Fi privé pour une navigation sécurisée. Le stockage externe prend en charge les cartes MicroSD jusqu'à 128GB. OpenWrt/LEDE et OpenVPN sont préinstallés. Creta offre ainsi aux utilisateurs soucieux de leur confidentialité une solution VPN rapide et simple basée sur une cryptographie de pointe.

![ar750 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/product_info/ar750_overview.png){class="glboxshadow"}

### Spécifications

[Spécifications du GL-AR750](https://www.gl-inet.com/products/gl-ar750/#specs){target="_blank"}

## Configuration initiale du Creta

Pour configurer le Creta, utilisez l'une des quatre méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3dm0w5kjAlc?si=3YykOcaz_YK_vp28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise un autre routeur GL.iNet pour illustrer la configuration, mais les étapes sont identiques pour le Creta et les autres modèles de routeurs.)</small>

### 1. Mettre Creta sous tension

Branchez le câble d'alimentation Micro USB sur le port d'alimentation du routeur. Assurez-vous d'utiliser un adaptateur secteur standard 5V/2A.

!!! Note

    Le branchement à chaud des cartes TF n'est pas pris en charge. Si vous souhaitez utiliser une carte TF, insérez-la avant de mettre le routeur sous tension.

### 2. Connecter votre appareil à Creta

Connectez votre ordinateur ou votre appareil mobile au routeur via le Wi‑Fi ou Ethernet.

=== "Wi-Fi"

    Sur votre appareil, repérez le nom du réseau Wi‑Fi du routeur dans la liste des réseaux disponibles et saisissez le mot de passe. (Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.)

=== "Ethernet"

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

### 3. Connecter Creta à Internet

**Note:** Les instructions ci-dessous s'adressent aux utilisateurs qui connectent le routeur à Internet via le panneau d'administration web. Si vous préférez utiliser l'application GL.iNet plutôt que le panneau d'administration web, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

#### 1. Se connecter au panneau d'administration web du routeur

Dans la barre d'adresse d'un navigateur web, saisissez `192.168.8.1`. Choisissez votre langue, puis cliquez sur **Next**. Définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

#### 2. Configurer la ou les méthodes de connexion Internet

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/ethernet.png){class="glboxshadow"}
    
    Connectez un câble Ethernet entre le port WAN du routeur et un équipement en amont, par exemple un modem. Si la connexion Internet est établie avec succès, un point vert apparaît à côté de « Ethernet ».

    Pour des instructions détaillées, consultez [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/repeater.png){class="glboxshadow"}

    1. Sur l'écran principal du panneau d'administration web, repérez la section « Repeater », puis cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi.
    3. Saisissez le mot de passe du réseau, puis cliquez sur **Apply**.
    
    Si la connexion Internet est établie avec succès, un point vert apparaît à côté du nom du réseau Wi‑Fi.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/tethering.png){class="glboxshadow"}

    1. Connectez votre smartphone au routeur à l'aide d'un câble USB et activez le partage de connexion réseau dans les paramètres du point d'accès personnel.
    2. Sur l'écran principal du panneau d'administration web, repérez la section « Tethering », puis cliquez sur **Connect**.
    3. Si la connexion Internet est établie avec succès, un point vert apparaît à côté de « Tethering ».

    Pour des instructions détaillées, consultez [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750/internet_setup/usb_modem.png){class="glboxshadow"}

    1. Insérez un modem USB compatible avec le réseau cellulaire dans le port USB du routeur.
    2. Sur l'écran principal du panneau d'administration web, repérez la section « Cellular », puis cliquez sur **Connect**.
    3. Si la connexion Internet est établie avec succès, un point vert apparaît à côté de « Cellular ».

    Pour des instructions détaillées, consultez [Se connecter à Internet via un modem USB](../../interface_guide/internet_cellular.md).

**Note:** Si vous souhaitez utiliser la fonctionnalité multi-WAN, vous devez configurer plus d'une méthode de connexion Internet.

---

## Configurer un VPN

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et permet d'accéder à un réseau distant (serveur VPN). Creta, comme les autres routeurs GL.iNet, prend en charge OpenVPN et WireGuard.

=== "OpenVPN"

    Creta, comme les autres routeurs GL.iNet, prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Creta, comme les autres routeurs GL.iNet, prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

---

## Applications supplémentaires

=== "Plug-ins"

    Les plug-ins sont des fonctionnalités additionnelles qui étendent les capacités de votre routeur. Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Cette fonction est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant. Pour configurer Dynamic DNS, consultez [Dynamic DNS](../../interface_guide/ddns.md).

=== "GoodCloud"

    Le service de gestion cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer. Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

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

=== "DNS"

    La page DNS propose des options permettant de personnaliser les paramètres Domain Name System de votre routeur afin d'améliorer à la fois la sécurité et les performances. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Encrypted DNS : configurez un DNS chiffré pour empêcher la surveillance ou la falsification de vos données de navigation et garantir la confidentialité.
    * Manual DNS : définissez manuellement les serveurs DNS de votre choix pour mieux contrôler les requêtes DNS et, potentiellement, accélérer leur résolution.
    * DNS Proxy : activez le proxy DNS afin d'acheminer les requêtes DNS de vos appareils via un serveur DNS spécifié, ce qui ajoute une couche de contrôle supplémentaire sur le trafic DNS.

    Ces paramètres vous permettent d'optimiser les performances et la sécurité DNS de votre réseau selon vos besoins.

    Pour des instructions détaillées et plus d'informations, consultez [DNS](../../interface_guide/dns.md).

=== "Network Mode"

    La page Network Mode vous permet de configurer votre routeur pour qu'il fonctionne selon différents modes, afin de répondre à divers besoins réseau. Les modes disponibles sont les suivants :

    * Router : fonctionne comme un routeur standard, en gérant le trafic entre votre réseau local et Internet et en fournissant des fonctions telles que NAT, le pare-feu et DHCP.
    * Access Point : fonctionne comme un point d'accès, en étendant votre réseau filaire existant grâce à une connectivité sans fil sans assurer de routage du trafic.
    * Extender : fonctionne comme un répéteur de portée, en renforçant le signal de votre réseau sans fil existant pour couvrir une zone plus large et éliminer les zones mortes.
    * WDS (Wireless Distribution System) : similaire à Extender ; choisissez WDS si votre routeur principal prend en charge le mode WDS.

    Pour des instructions détaillées et plus d'informations, consultez [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    La page IPv6 vous permet de configurer les paramètres IPv6 de votre réseau afin de prendre en charge le protocole Internet le plus récent. Sur cette page, vous pouvez activer IPv6 et sélectionner l'un des quatre modes proposés selon vos besoins réseau :

    * Native : obtient une adresse IPv6 directement auprès de votre FAI pour une connectivité IPv6 native simple et efficace.
    * Passthrough : laisse le trafic IPv6 traverser le routeur vers les appareils de votre réseau, ce qui assure un pont réseau sans que le routeur gère lui-même le routage IPv6.
    * NAT6 : utilise la traduction d'adresses réseau pour IPv6 (NAT6) afin de traduire les adresses IPv6 internes et externes, de manière similaire au fonctionnement du NAT pour IPv4.
    * Static IPv6 : permet de configurer manuellement une adresse IPv6 statique pour votre routeur afin de garantir une adresse fixe pour une connectivité stable et une gestion plus simple des services réseau.

    Ces paramètres vous aident à tirer parti des avantages d'IPv6, notamment un espace d'adressage plus vaste, des fonctions de sécurité améliorées et de meilleures performances.

    Pour des instructions détaillées et plus d'informations, consultez [IPv6](../../interface_guide/ipv6.md).

---

=== "MAC Address"

    La page MAC Address vous permet d'afficher et de gérer les adresses Media Access Control (MAC) associées à votre routeur. Les principales fonctions disponibles sur cette page sont les suivantes :

    * Factory Default : affiche les adresses MAC par défaut du routeur pour les modes Ethernet et Repeater, afin de fournir une référence aux paramètres matériels d'origine.
    * Clone : clone l'adresse MAC d'un appareil client spécifique. Cette fonction est particulièrement utile lorsque l'accès au réseau est limité à certains appareils.
    * Manual : permet de définir manuellement une adresse MAC personnalisée pour votre routeur. Vous pouvez également utiliser le bouton Random pour générer une adresse MAC aléatoire, ce qui offre davantage de souplesse et de confidentialité.

    Ces fonctions vous permettent de gérer efficacement les adresses MAC de votre routeur afin d'assurer la compatibilité et la flexibilité dans différents environnements réseau.

    Pour des instructions détaillées et plus d'informations, consultez [MAC Address](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctions qu'il ne propose peut-être pas, notamment AdGuard Home, le DNS chiffré et le VPN. Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    La page IGMP Snooping vous permet de configurer des paramètres qui optimisent la gestion du trafic multicast au sein de votre réseau. IGMP Snooping écoute et extrait les informations des paquets du protocole IGMP, puis établit et maintient des tables de transfert multicast de couche 2. Cela garantit que les données des groupes multicast ne sont transmises qu'aux hôtes ayant rejoint le groupe, évitant ainsi que du trafic multicast non désiré n'atteigne les autres hôtes.

    Ces paramètres contribuent à optimiser les performances et l'efficacité du réseau, en particulier dans les environnements comportant un trafic multicast important, comme le streaming vidéo ou les jeux en ligne.

    Pour des instructions détaillées et plus d'informations, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Paramètres système

=== "Overview"

    La page Overview fournit une vue d'ensemble complète de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * CPU Average Load : surveillez la charge moyenne du CPU du routeur pour évaluer les performances et identifier d'éventuels goulots d'étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée afin de mieux gérer les ressources.
    * Flash Usage : consultez l'utilisation du stockage flash du routeur afin de vous assurer qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * LED Control : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l'appareil.
    * System Info : accédez à des informations détaillées sur le système de votre routeur, notamment la version du firmware, l'uptime et l'état du réseau.
    
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
    * 5GHz Wi-Fi Status Schedule : créez un calendrier pour activer ou désactiver la bande Wi‑Fi 5GHz à certains moments afin d'optimiser l'utilisation du réseau et l'efficacité énergétique.
    * 2.4GHz Wi-Fi Status Schedule : définissez un calendrier pour contrôler la bande Wi‑Fi 2.4GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle sur le fonctionnement du routeur afin qu'il réponde à vos besoins et préférences spécifiques.

    Pour des instructions détaillées et plus d'informations, consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

---

=== "Admin Password"

    La page Admin Password vous permet de définir ou de modifier le mot de passe de l'interface d'administration du routeur, afin que seuls les utilisateurs autorisés puissent accéder aux paramètres du routeur et les modifier. Ce mot de passe est essentiel pour préserver la sécurité et l'intégrité de votre réseau et pour empêcher les accès non autorisés ainsi que les changements de configuration indésirables.

    Pour des instructions détaillées et plus d'informations, consultez [Admin Password](../../interface_guide/admin_password.md).

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, tous les journaux et tous les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements précis et pour garantir le bon fonctionnement des configurations basées sur l'heure.

    Pour des instructions détaillées et plus d'informations, consultez [Time Zone](../../interface_guide/time_zone.md).

=== "Toggle Button Settings"

    La page Toggle Button Settings vous permet de configurer le bouton physique à bascule de votre routeur afin de lui attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonction offre des raccourcis pratiques pour les tâches et réglages courants, améliorant ainsi l'expérience utilisateur et simplifiant la gestion du routeur.

    Pour des instructions détaillées et plus d'informations, consultez [Toggle Button Settings](../../interface_guide/toggle_button_settings.md).

---

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés au fonctionnement et aux événements du noyau.
    * Crash Log : enregistrements des plantages et erreurs système, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    En outre, cette page propose un bouton Export Log, qui vous permet d'exporter tous les journaux collectés pour une analyse par le support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées et plus d'informations, consultez [Log](../../interface_guide/log.md).

=== "Reset Firmware"

    La page Reset Firmware vous permet de réinitialiser la version actuelle du firmware de votre routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Cette opération restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre du firmware actuel.

    Pour des instructions détaillées et plus d'informations, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès aux options de configuration avancée via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster avec précision les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des réglages de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées et plus d'informations, consultez [Advanced Settings](../../interface_guide/advanced_settings.md).