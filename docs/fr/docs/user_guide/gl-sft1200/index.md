# Guide d'utilisation de Opal (GL-SFT1200)

## Aperçu du produit

Opal (GL-SFT1200) est un routeur de voyage de poche prenant en charge un débit sans fil de 1200 Mbps. Son format compact est conçu pour une utilisation portable et répond aux besoins d'accès Internet sans fil des petites entreprises, des petits appartements ou des voyageurs d'affaires.

![gl-sft1200 interface](https://static.gl-inet.com/docs/router/en/3/setup/gl-sft1200/first_time_setup/gl-sft1200.jpg){class="glboxshadow"}

## Contenu du colis

- 1 x Opal (GL-SFT1200)
- 1 x Manuel d'utilisation
- 1 x Câble Ethernet
- 1 x Carte de remerciement
- 1 x Carte de garantie
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![gl-sft1200 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/first_time_setup/sft1200_unboxing.jpg){class="glboxshadow"}

## Comment configurer Opal

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZAVn92F5RV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo utilise un autre routeur GL.iNet pour la démonstration, mais les étapes sont les mêmes pour Opal et les autres modèles de routeurs.)</small>

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur puis sur une prise électrique. Il démarre automatiquement.

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

Configurez votre Opal en utilisant l'une des méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Ethernet"
    
    ![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_ethernet.png){class="glboxshadow"}

    Branchez un câble Ethernet entre le port WAN de votre routeur et un équipement amont tel qu'un modem.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_repeater.png){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration web, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Repeater de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

    ![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_tethering.png){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou une clé USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Paramètres et activez le partage de connexion USB.
    3. Sur la page INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Tethering de la page INTERNET.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

=== "Cellular"

    ![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-sft1200/internet/sft1200_cellular.png){class="glboxshadow"}

    Branchez un modem USB cellulaire sur le port USB du routeur. Cela permet de partager la connexion Internet du modem USB avec tous les appareils connectés.

    Une fois la connexion Internet établie, un point vert apparaît dans la section Cellular de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau cellulaire](../../interface_guide/internet_cellular.md) pour des instructions détaillées.

## Comment configurer un VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Opal prend en charge OpenVPN, WireGuard et Tor*.

=== "OpenVPN" 
    
    Opal (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Comment configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Opal (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Comment configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la confidentialité qui permet des communications anonymes sur Internet. Il fait transiter le trafic Internet par une série de serveurs bénévoles (nœuds) afin de masquer la localisation et l'utilisation de l'utilisateur, rendant le suivi des activités en ligne plus difficile.

    **Remarque :** Opal ne prend pas en charge Tor nativement, mais les utilisateurs peuvent l'installer manuellement via un plug-in. Cliquez [ici](../../interface_guide/tor.md#manual-install) pour plus de détails.

## Réseau sans fil et clients

=== "Réseau sans fil"

    La page Réseau sans fil vous permet de configurer les paramètres des réseaux Wi‑Fi 5 GHz et 2,4 GHz, notamment l'activation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation du BSSID aléatoire, le choix du mode de sécurité Wi‑Fi et du mot de passe, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi‑Fi, de la bande passante et du canal.

    Pour configurer le réseau sans fil, consultez [Réseau sans fil](../../interface_guide/wireless.md).

=== "Clients"

    La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

    Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    Le service GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Conçue spécifiquement pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge la gestion complète des appareils sur l'ensemble du réseau, avec un contrôle des équipements en amont comme en aval. Axée sur l'administration à l'échelle du réseau et avec une future prise en charge du contrôle au niveau matériel, AstroWarp constitue une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.
    
    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

    **Remarque :** veuillez mettre à niveau le firmware de votre routeur vers la version 1.7 ou supérieure avant d'utiliser cette fonctionnalité.

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant de le personnaliser et d'en étendre les capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant.
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution centralisée de stockage des données qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

    **Remarque :** veuillez mettre à niveau le firmware de votre routeur vers la version 1.7 ou supérieure avant d'utiliser cette fonctionnalité.

## Paramètres réseau

=== "Redirection de ports"

    La redirection de ports permet à des serveurs et appareils distants sur Internet d'accéder aux appareils d'un réseau privé.
    
    Pour configurer la redirection de ports, consultez [Redirection de ports](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer simultanément plusieurs connexions Internet sur votre routeur (par exemple Cellular, Repeater et Ethernet). Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Le LAN, ou réseau local, est un réseau qui relie des ordinateurs et des appareils dans une zone géographique limitée, comme une maison ou un bureau. Il permet des transferts de données à grande vitesse et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [LAN](../../interface_guide/lan.md).

---

=== "Réseau invité"

    Cette fonction vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de passerelle et de masque de sous-réseau, et de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Réseau invité](../../interface_guide/guest_network.md).

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients, d'autoriser les DNS personnalisés à remplacer les DNS du VPN et de configurer le mode des paramètres du serveur DNS en automatique ou de spécifier manuellement les serveurs DNS issus de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Gestion des ports"

    La page Gestion des ports est disponible à partir du firmware v4.7.

    Cette page vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher le débit négocié du port réseau.

    Pour gérer les ports Ethernet, consultez [Gestion des ports](../../interface_guide/ethernet_port.md).

---

=== "Mode réseau"

    Le mode réseau désigne les paramètres de configuration qui déterminent comment un appareil se connecte à un réseau et communique avec les autres appareils.
    
    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, indispensable pour répondre au nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal, notamment avec AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](../../tutorials/how_to_set_up_drop_in_gateway.md).

---

=== "IGMP Snooping"

    L'IGMP Snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Accélération réseau"

    L'accélération réseau peut réduire la charge CPU et accélérer le transfert des paquets de trafic.
    
    Pour configurer l'accélération réseau, consultez [Accélération réseau](../../interface_guide/network_acceleration.md).

=== "Paramètres NAT"

    La page Paramètres NAT vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [Paramètres NAT](../../interface_guide/nat_settings.md).

## Paramètres système

=== "Aperçu"

    La page Aperçu fournit un instantané complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * Charge CPU moyenne : surveillez la charge moyenne du processeur de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulets d'étranglement.
    * Utilisation de la mémoire : vérifiez quelle part de la mémoire du routeur est utilisée afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur afin de personnaliser les indicateurs visuels de l'appareil.
    * Utilisation du stockage flash : visualisez l'occupation du stockage flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez aux informations détaillées du système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC de l'appareil et son numéro de série.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que des clés USB ou des cartes TF.
    
    Ces fonctionnalités fournissent des informations et des commandes essentielles pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez consulter [Aperçu](../../interface_guide/system_overview.md) pour des instructions détaillées.

=== "Mise à niveau"

    La page Mise à niveau permet de mettre à jour le firmware du routeur vers la version la plus récente, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à niveau :

    * Mise à niveau du firmware en ligne : recherchez et installez automatiquement la dernière version du firmware directement depuis le serveur du fabricant afin de simplifier la mise à jour.
    * Mise à niveau locale du firmware : téléversez manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, avec un contrôle total sur la version et le moment de la mise à jour.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Veuillez consulter [Mise à niveau](../../interface_guide/upgrade.md) pour des instructions détaillées.

=== "Tâches planifiées"

    La page Tâches planifiées vous permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, pour plus de confort et d'efficacité. Les principales fonctions de cette page sont :

    * Planification de l'affichage des LED : définissez un planning pour allumer ou éteindre automatiquement les voyants LED du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Planification de l'état du Wi‑Fi : définissez un planning pour contrôler les bandes Wi‑Fi 5 GHz / 2,4 GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle des opérations du routeur afin de répondre à vos besoins et à vos préférences.

    Veuillez consulter [Tâches planifiées](../../interface_guide/scheduled_tasks.md) pour des instructions détaillées.

---

=== "Fuseau horaire"

    La page Fuseau horaire vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements exacts et exécuter correctement les configurations basées sur le temps.

    Veuillez consulter [Fuseau horaire](../../interface_guide/time_zone.md) pour des instructions détaillées.

=== "Paramètres du bouton à bascule"

    La page Paramètres du bouton à bascule vous permet de configurer le bouton physique du routeur et de lui attribuer des fonctions spécifiques pour un accès et un contrôle rapides. Cette fonctionnalité offre des raccourcis pratiques pour les tâches et réglages courants, améliorant l'expérience utilisateur et simplifiant la gestion du routeur.

    Veuillez consulter [Paramètres du bouton à bascule](../../interface_guide/toggle_button_settings.md) pour des instructions détaillées.

=== "Journal"

    La page Journal donne accès à différents journaux qui enregistrent les activités et les événements du routeur, facilitant ainsi le dépannage et le suivi des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau du système.
    * Journal du noyau : journaux liés au fonctionnement et aux événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs du système, utiles pour diagnostiquer les problèmes critiques.
    * Journal Cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    La page comporte également un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour les transmettre au support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Journal](../../interface_guide/log.md) pour des instructions détaillées.

---

=== "Sécurité"

    La page Sécurité vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend des options pour :

    * Mot de passe administrateur : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Contrôle d'accès local : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, renforçant ainsi la sécurité face aux menaces externes.
    * Ports ouverts sur le routeur : contrôlez quels ports sont ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.

    Veuillez consulter [Sécurité](../../interface_guide/security.md) pour des instructions détaillées.

=== "Réinitialiser le firmware"

    La page Réinitialiser le firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware du routeur, en effaçant toutes les configurations personnalisées. Ce processus remet le routeur aux paramètres par défaut de la version de firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre.

    Veuillez consulter [Réinitialiser le firmware](../../interface_guide/reset_firmware.md) pour des instructions détaillées.

=== "Paramètres avancés"

    La page Paramètres avancés donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'affiner les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Veuillez consulter [Paramètres avancés](../../interface_guide/advanced_settings.md) pour des instructions détaillées.
