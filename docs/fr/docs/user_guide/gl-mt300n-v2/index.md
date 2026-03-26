# Guide d'utilisation de Mango (GL-MT300N-V2)

## Aperçu du produit

Mango (GL-MT300N-V2) est un mini-routeur de poche conçu pour être portable et adapté aux voyages, avec un débit sans fil allant jusqu'à 300 Mbps. Mango offre des fonctions de sécurité avancées, notamment la prise en charge d'OpenVPN, de WireGuard® et d'un serveur DNS. Il vous permet non seulement de transformer un réseau public en Wi‑Fi privé pour naviguer en toute sécurité, mais aussi de téléverser des fichiers de configuration VPN provenant de plus de 30 fournisseurs de services VPN et de l'utiliser comme client VPN, afin d'ajouter une couche de confidentialité et de sécurité en créant un trafic chiffré entre votre appareil et le serveur VPN.

![mt300n-v2 illustration](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/product_info/mt300n_v2_overview.png){class="glboxshadow"}

## Comment configurer Mango

Pour configurer Mango, utilisez l'une des quatre méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Suivez les étapes ci-dessous.

### 1. Mise sous tension

Branchez le câble d'alimentation Micro USB sur le port d'alimentation du routeur, puis connectez l'autre extrémité à un adaptateur secteur 5V/2A (non inclus) et branchez-le sur une prise électrique.

### 2. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi‑Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi de votre routeur dans la liste des réseaux disponibles et saisissez le mot de passe. Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette située sous le routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse et connectez-vous. Choisissez votre langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**. 

Veuillez noter que si vous modifiez les informations Wi‑Fi, vous devrez reconnecter votre appareil au Wi‑Fi du routeur avec les nouveaux identifiants.

### 4. Configuration de la connexion Internet

**Remarque :** Les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Mango en utilisant l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/ethernet.png){class="glboxshadow"}
    
    Branchez un câble Ethernet entre le port WAN de votre routeur et un équipement amont tel qu'un modem.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/repeater.png){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Repeater de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou une clé USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Paramètres et activez le partage de connexion USB.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Tethering de la page INTERNET.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt300n-v2/internet_setup/usb_modem.png){class="glboxshadow"}

    Cette méthode permet de partager la connexion Internet d'un modem USB avec tous les appareils connectés.

    1. Insérez un modem USB compatible réseau cellulaire dans le port USB du routeur.
    2. Sur la page INTERNET du panneau d'administration web, repérez la section Cellular et cliquez sur **Connect**.
    3. Une fois la connexion Internet établie, un point vert apparaît dans la section Cellular de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un modem USB](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

## Comment configurer un VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Mango (comme les autres routeurs GL.iNet) prend en charge OpenVPN et WireGuard.

=== "OpenVPN" 

    Mango (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mango (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Applications

=== "Plug-ins"

    Les plug-ins sont des fonctions additionnelles qui étendent les capacités de votre routeur.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant.
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "GoodCloud"

    Le service de gestion Cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

## Paramètres réseau

=== "Pare-feu"

    La page Pare-feu apporte des améliorations de sécurité essentielles à votre réseau. Elle inclut des fonctions telles que la redirection de ports, les ports ouverts et la DMZ. Ces outils vous permettent de gérer et de personnaliser le flux de trafic de votre réseau et d'en renforcer la sécurité.

    * Redirection de ports : redirigez un trafic spécifique depuis Internet vers des appareils désignés de votre réseau, afin de permettre l'accès à des services tels que des serveurs de jeu ou des serveurs web.
    * Ports ouverts : surveillez et contrôlez les ports ouverts sur votre routeur afin de prévenir les accès non autorisés et les menaces de sécurité potentielles.
    * DMZ (zone démilitarisée) : placez un appareil en dehors du pare-feu principal pour lui permettre un accès sans restriction à Internet tout en protégeant le reste du réseau contre les menaces potentielles.

    Pour configurer les paramètres liés au pare-feu, consultez [Pare-feu](../../interface_guide/firewall.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer simultanément plusieurs connexions Internet sur votre routeur (par exemple Cellular, Repeater et Ethernet). Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    La page LAN vous permet de gérer et de configurer les paramètres du réseau local de votre routeur. Les principales fonctions disponibles sur cette page sont :

    * Adresse IP du routeur : modifiez l'adresse IP de votre routeur pour mieux l'adapter à votre configuration réseau.
    * Masque de sous-réseau : définissez le masque de sous-réseau de votre réseau, qui détermine sa taille et sa plage d'adresses IP.
    * DHCP : activez ou configurez le Dynamic Host Configuration Protocol, qui attribue automatiquement des adresses IP aux appareils de votre réseau.
    * Réservation d'adresse : réservez des adresses IP spécifiques pour certains appareils afin qu'ils reçoivent toujours la même adresse IP du serveur DHCP.

    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

---

=== "DNS"

    La page DNS propose des options pour personnaliser les paramètres Domain Name System de votre routeur, améliorant à la fois la sécurité et les performances. Les principales fonctions disponibles sur cette page sont :

    * DNS chiffré : configurez un DNS chiffré afin de protéger vos données de navigation contre la surveillance ou les modifications, pour plus de confidentialité et de sécurité.
    * DNS manuel : définissez manuellement les serveurs DNS de votre choix pour un contrôle personnalisé des requêtes DNS et des temps de résolution potentiellement plus rapides.
    * Proxy DNS : activez le proxy DNS pour faire transiter les requêtes DNS de vos appareils via un serveur DNS spécifié, offrant un contrôle supplémentaire sur le trafic DNS.

    Ces paramètres vous permettent d'optimiser les performances et la sécurité DNS de votre réseau en fonction de vos besoins spécifiques.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Mode réseau"

    La page Mode réseau vous permet de configurer votre routeur pour fonctionner dans différents modes, offrant la flexibilité nécessaire pour répondre à divers besoins réseau. Les modes disponibles comprennent :

    * Routeur : fonctionne comme un routeur standard, en gérant le trafic entre votre réseau local et Internet, et en fournissant des fonctions telles que le NAT, le pare-feu et le DHCP.
    * Point d'accès : fonctionne comme un point d'accès, étendant votre réseau filaire existant en fournissant une connectivité sans fil sans assurer le routage du trafic.
    * Extender : fonctionne comme un répéteur, renforçant le signal de votre réseau sans fil existant pour couvrir une zone plus large et éliminer les zones mortes.
    * WDS (Wireless Distribution System) : similaire à Extender ; choisissez WDS si votre routeur principal prend en charge le mode WDS.

    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "IPv6"

    La page IPv6 vous permet de configurer les paramètres IPv6 de votre réseau, en apportant la prise en charge du dernier protocole Internet. Sur cette page, vous pouvez activer IPv6 et choisir parmi quatre modes différents selon les besoins de votre réseau :

    * Native : obtenez une adresse IPv6 directement auprès de votre FAI pour une connectivité IPv6 native simple et efficace.
    * Passthrough : laissez le trafic IPv6 traverser le routeur jusqu'aux appareils de votre réseau, ce qui revient à faire transiter la connexion sans que le routeur ne gère lui-même le routage IPv6.
    * NAT6 : utilisez la traduction d'adresses réseau pour IPv6 (NAT6) afin d'assurer la traduction entre les adresses IPv6 internes et externes, de manière similaire au NAT pour IPv4.
    * IPv6 statique : configurez manuellement une adresse IPv6 statique pour votre routeur, afin de disposer d'une adresse fixe pour une connectivité stable et une gestion plus simple des services réseau.

    Ces paramètres vous aident à tirer parti des avantages d'IPv6, notamment un espace d'adressage étendu, des fonctions de sécurité renforcées et de meilleures performances.

    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

---

=== "Adresse MAC"

    La page Adresse MAC vous permet d'afficher et de gérer les adresses MAC associées à votre routeur. Les principales fonctions disponibles sur cette page sont :

    * Valeur par défaut d'usine : affiche les adresses MAC par défaut des modes Ethernet et Repeater du routeur, servant de référence pour les réglages matériels d'origine.
    * Clonage : clonez l'adresse MAC d'un appareil client spécifique. Cette fonction est particulièrement utile lorsque l'accès au réseau est limité à certains appareils.
    * Manuel : spécifiez manuellement une adresse MAC personnalisée pour votre routeur. Vous pouvez également utiliser le bouton Random pour générer une adresse MAC aléatoire, offrant davantage de flexibilité et de confidentialité.

    Ces fonctions vous permettent de gérer efficacement les adresses MAC de votre routeur, assurant compatibilité et flexibilité dans différents environnements réseau.

    Pour gérer l'adresse MAC, consultez [Adresse MAC](../../interface_guide/mac_address.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctions qu'il peut ne pas posséder, notamment AdGuard Home, le DNS chiffré et le VPN.
    
    Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    La page IGMP Snooping vous permet de configurer des paramètres qui optimisent la gestion du trafic multicast dans votre réseau. IGMP Snooping écoute les paquets du protocole IGMP et en extrait les informations afin d'établir et de maintenir des tables de transfert multicast de couche 2. Cela garantit que les données des groupes multicast ne sont transmises qu'aux hôtes ayant rejoint le groupe multicast, évitant ainsi que du trafic multicast indésirable n'atteigne d'autres hôtes.

    Ces paramètres contribuent à optimiser les performances et l'efficacité du réseau, en particulier dans les environnements comportant un trafic multicast important, comme le streaming vidéo ou les jeux en ligne.

    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

## Paramètres système

=== "Aperçu"

    La page Aperçu fournit un instantané complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * Charge CPU moyenne : surveillez la charge moyenne du processeur de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulets d'étranglement.
    * Utilisation de la mémoire : vérifiez quelle part de la mémoire du routeur est utilisée afin de mieux gérer les ressources.
    * Utilisation du stockage flash : visualisez l'occupation du stockage flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur afin de personnaliser les indicateurs visuels de l'appareil.
    * Informations système : accédez aux informations détaillées du système de votre routeur, notamment la version du firmware, la durée de fonctionnement et l'état du réseau.
    
    Ces fonctionnalités fournissent des informations et des commandes essentielles pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez consulter [Aperçu](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Mise à niveau"

    La page Mise à niveau permet de mettre à jour le firmware du routeur vers la version la plus récente, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à niveau :

    * Mise à niveau en ligne : recherchez et installez automatiquement la dernière version du firmware directement depuis le serveur du fabricant afin de simplifier la mise à jour.
    * Mise à niveau locale : téléversez manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, avec un contrôle total sur la version et le moment de la mise à jour.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Veuillez consulter [Mise à niveau](../../interface_guide/upgrade.md) pour des instructions détaillées.

=== "Tâches planifiées"

    La page Tâches planifiées vous permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, pour plus de confort et d'efficacité. Les principales fonctions de cette page sont :

    * Planification de l'affichage des LED : définissez un planning pour allumer ou éteindre automatiquement les voyants LED du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Planification de l'état du Wi‑Fi 2,4 GHz : définissez un planning pour contrôler la bande Wi‑Fi 2,4 GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle des opérations du routeur afin de répondre à vos besoins et à vos préférences.

    Veuillez consulter [Tâches planifiées](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.

---

=== "Mot de passe administrateur"

    La page Mot de passe administrateur vous permet de définir ou de modifier le mot de passe de l'interface d'administration de votre routeur afin que seuls les utilisateurs autorisés puissent accéder aux paramètres du routeur et les modifier. Ce mot de passe est essentiel pour préserver la sécurité et l'intégrité de votre réseau et le protéger contre les accès non autorisés et les changements de configuration.

    Veuillez consulter [Mot de passe administrateur](../../interface_guide/admin_password.md) pour des instructions détaillées.

=== "Fuseau horaire"

    La page Fuseau horaire vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements exacts et exécuter correctement les configurations basées sur le temps.

    Veuillez consulter [Fuseau horaire](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Paramètres du bouton à bascule"

    La page Paramètres du bouton à bascule vous permet de configurer le bouton physique du routeur et de lui attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonctionnalité offre des raccourcis pratiques pour les tâches et réglages courants, améliorant l'expérience utilisateur et simplifiant la gestion du routeur.

    Veuillez consulter [Paramètres du bouton à bascule](../../interface_guide/toggle_button_settings.md) pour des instructions détaillées.

---

=== "Journal"

    La page Journal donne accès à différents journaux qui enregistrent les activités et les événements du routeur, facilitant ainsi le dépannage et le suivi des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau du système.
    * Journal du noyau : journaux liés au fonctionnement et aux événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs du système, utiles pour diagnostiquer les problèmes critiques.
    * Journal Cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    La page comporte également un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour les transmettre au support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Journal](../../interface_guide/log.md) pour des instructions détaillées.

=== "Réinitialiser le firmware"

    La page Réinitialiser le firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware du routeur, en effaçant toutes les configurations personnalisées. Ce processus remet le routeur aux paramètres par défaut de la version de firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre.

    Veuillez consulter [Réinitialiser le firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Paramètres avancés donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'affiner les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Veuillez consulter [Paramètres avancés](../../interface_guide/advanced_settings.md) pour des instructions détaillées.
