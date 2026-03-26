# Guide d'utilisation de Spitz Plus (GL-X2000)

## Aperçu du produit

Spitz Plus (GL-X2000) est une passerelle cellulaire Wi‑Fi 6 4G LTE double SIM conçue pour fournir des connexions rapides et fiables, en particulier dans les zones éloignées et lors des déplacements sur la route. Grâce à l'agrégation de 3 porteuses, le routeur transmet des données simultanément sur trois bandes opérateur, offrant une bande passante disponible 3 fois supérieure pour éviter la congestion. Il propose quatre méthodes d'accès à Internet : Cellular (cartes SIM), Ethernet, Repeater et Tethering. Il prend en charge le Multi-WAN (conmutation par erreur et équilibrage de charge), les VPN (OpenVPN et WireGuard), le contrôle parental, AdGuard Home, la redirection de ports, Tailscale et bien plus encore.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Contenu du colis

- 1 x Spitz Plus (GL-X2000)
- 1 x Manuel d'utilisation
- 4 x Antennes externes
- 1 x Carte de remerciement
- 1 x Câble Ethernet
- 1 x Kit de fixation murale
- 1 x Pastille adhésive
- 4 x Vis
- 1 x Adaptateur secteur
- 1 x Convertisseur (selon votre pays de livraison)

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/first_time_setup/x2000_unboxing.jpg){class="glboxshadow"}

## Indicateurs LED

| État de fonctionnement                                                      | Alimentation                         | Internet                    | 2.4GHz                      | 5GHz                        | Cellular | 
| ----------------------------------------------------------------------------- | ------------------------------------ | --------------------------- | --------------------------- | --------------------------- | ------- |
| Fonctionnement normal (connecté à Internet)                                  | Vert                                 | Vert                        | Vert                        | Vert                        | Vert     |
| Non connecté à Internet                                                      | Vert                                 | Éteint                      | Vert                        | Vert                        | Vert     |
| Mise à jour du firmware                                                      | Vert                                 | Vert clignotant (toutes les 0,5 s) | Vert clignotant (toutes les 0,5 s) | Vert clignotant (toutes les 0,5 s) | Vert     | 
| Réinitialisation réseau (maintenez le bouton "reset" enfoncé pendant > 3 s) | Vert clignotant (toutes les 1 s)     | Vert                        | Vert                        | Vert                        | Vert     |
| Restauration des paramètres d'usine (maintenez le bouton "reset" enfoncé pendant 10 s) | Vert clignotant rapidement (toutes les 0,25 s) | Vert | Vert | Vert | Vert | 

## Comment configurer Spitz Plus

Pour configurer Spitz Plus, utilisez l'une des quatre méthodes de connexion Internet prises en charge : Cellular (carte SIM requise), Ethernet, Repeater et Tethering. Regardez cette vidéo de configuration ou suivez les étapes ci-dessous. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Cette vidéo montre la configuration Cellular de Spitz Plus. Si vous devez configurer Spitz Plus avec d'autres méthodes de connexion Internet, veuillez suivre les étapes ci-dessous.)</small>

!!! note "Avant de commencer, suivez ces étapes (si vous utilisez la méthode cellulaire) :"

    Au moins une carte nano SIM est nécessaire pour vous connecter à Internet via la méthode cellulaire. Si votre ou vos cartes nano SIM sont prêtes, suivez les étapes ci-dessous :
    
    1. Activez votre ou vos cartes SIM si votre opérateur l'exige.
    2. Éteignez votre routeur.
    3. Insérez la ou les cartes SIM dans les emplacements SIM. (**Remarque :** une seule carte SIM est active à la fois. L'autre sert uniquement de secours.)

### 1. Mise sous tension

Assemblez les deux parties de l'adaptateur secteur. Branchez-le à votre routeur puis sur une prise électrique. Il démarre automatiquement.

### 2. Connecter un appareil

Connectez un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au routeur via Wi‑Fi ou Ethernet.

- Ethernet

    Connectez votre appareil au port LAN du routeur à l'aide d'un câble Ethernet.

- Wi‑Fi

    Sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi de votre routeur dans la liste des réseaux disponibles et saisissez le mot de passe. (Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.)

    Sur votre appareil, repérez le nom du réseau Wi‑Fi de votre routeur dans la liste des réseaux disponibles, puis saisissez le mot de passe pour rejoindre le réseau. Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette du routeur.

### 3. Se connecter au panneau d'administration web

Ouvrez un navigateur web, saisissez `192.168.8.1` dans la barre d'adresse pour accéder au panneau d'administration web GL.iNet. Choisissez une langue et définissez votre mot de passe administrateur, puis cliquez sur **Apply**. 

### 4. Configuration de la connexion Internet

**Remarque :** Les instructions suivantes s'appliquent aux utilisateurs qui configurent le routeur via le panneau d'administration web GL.iNet. Si vous préférez utiliser l'application GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/){target="_blank"} et suivez les instructions à l'écran.

Configurez votre Spitz Plus en utilisant l'une des méthodes de connexion Internet prises en charge : Cellular, Ethernet, Repeater et Tethering. Si vous souhaitez utiliser la fonction [Multi-WAN](../../interface_guide/multi-wan.md), veuillez configurer plus d'une connexion Internet.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Si vous avez inséré la carte SIM dans votre routeur, la connexion Internet devrait s'établir automatiquement. Vous devriez voir le nom de votre opérateur SIM et un point vert dans la section Cellular.
    
    Sinon, éteignez le routeur, réinsérez la carte SIM et rallumez-le.
    
    Veuillez consulter [Connexion à Internet via un réseau cellulaire](../../interface_guide/internet_cellular.md/#setup-for-dual-sim-models) pour des instructions détaillées.

    **Remarque** : la fonctionnalité eSIM de Spitz Plus est disponible à partir du firmware v4.7. Découvrez [ici](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md) comment utiliser la carte physique eSIM sur un routeur GL.iNet.

    Si vous rencontrez des problèmes, consultez le [guide de dépannage du réseau cellulaire](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}
    
    Connectez le port WAN du Spitz Plus à un équipement amont (par exemple un modem) à l'aide d'un câble Ethernet.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Ethernet de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md) pour des instructions détaillées.

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Sur la page INTERNET du panneau d'administration, repérez la section Repeater et cliquez sur **Connect**.
    2. Sélectionnez un réseau Wi‑Fi dans la liste des réseaux disponibles.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Repeater de la page INTERNET.

    Veuillez consulter [Connexion à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md) pour des instructions détaillées.

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou une clé USB) au port USB du routeur à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez à Paramètres et activez le partage de connexion USB.
    3. Sur l'écran INTERNET du panneau d'administration web, cliquez sur **Connect** dans la section Tethering.
    
    Une fois la connexion Internet établie, un point vert apparaît dans la section Tethering de la page INTERNET.

    Veuillez consulter [Connexion à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md) pour des instructions détaillées.

---

Vous trouverez ci-dessous un aperçu des fonctionnalités disponibles dans le panneau d'administration web du Spitz Plus.

## Réseau sans fil

La page Réseau sans fil vous permet de configurer les paramètres des réseaux Wi‑Fi 5 GHz et 2,4 GHz, notamment l'activation/la désactivation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation/la désactivation du BSSID aléatoire, le choix du mode de sécurité Wi‑Fi, la définition du mot de passe Wi‑Fi, la configuration de la visibilité du SSID, ainsi que le choix du mode Wi‑Fi, de la bande passante et du canal.

Pour configurer le réseau sans fil, consultez [Réseau sans fil](../../interface_guide/wireless.md).

## Clients

La page Clients affiche des informations sur les appareils connectés. Pour chaque client, elle indique le nom de l'appareil, le type de connexion (Ethernet ou Wi‑Fi), les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de réserver une IP, de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Conçue spécifiquement pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge la gestion complète des appareils sur l'ensemble du réseau, avec un contrôle des équipements en amont comme en aval. Axée sur l'administration à l'échelle du réseau et avec une future prise en charge du contrôle au niveau matériel, AstroWarp constitue une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.
    
    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

    **Remarque** : veuillez mettre à niveau votre Spitz Plus vers le firmware v4.8 ou supérieur pour utiliser AstroWarp.

## VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Spitz Plus prend en charge OpenVPN et WireGuard. 

=== "OpenVPN" 
    
    Spitz Plus (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Comment configurer un client OpenVPN](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/)
    * [Comment configurer un serveur OpenVPN](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_server/)

=== "WireGuard"
    
    Spitz Plus (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une grande simplicité d'utilisation. Pour configurer WireGuard, suivez ces tutoriels :

    * [Comment configurer un client WireGuard](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/)
    * [Comment configurer un serveur WireGuard](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_server/)

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctionnalités spécifiques à un programme existant, permettant de le personnaliser et d'en étendre les capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "DNS dynamique"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est utile pour les utilisateurs qui ont besoin d'une adresse IP statique pour accéder à un réseau distant.
    
    Pour configurer le DNS dynamique, consultez [DNS dynamique](../../interface_guide/ddns.md).

=== "Stockage réseau"

    Le stockage réseau désigne une solution centralisée de stockage des données qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, consultez [Stockage réseau](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est un outil tiers qui bloque les publicités et le pistage pour vous protéger. Pour savoir comment activer AdGuard Home, consultez [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/).

=== "Contrôle parental"

    Le contrôle parental est un ensemble de paramètres conçu pour vous aider à gérer et à contrôler les appareils de vos enfants. Il comprend notamment la limitation du temps d'écran et la restriction de l'accès à certains contenus. Spitz Plus propose deux options de contrôle parental : une version locale développée par GL.iNet et une version intégrée de Bark, une application de contrôle parental.

    Pour configurer le contrôle parental, consultez [contrôle parental](../../interface_guide/parental_control.md).

=== "Tailscale"

    Spitz Plus prend en charge Tailscale à partir du firmware v4.7.
    
    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et à vos applications depuis n'importe où.
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/parental_control.md).

=== "eSIM"

    Spitz Plus prend en charge la fonctionnalité eSIM à partir du firmware v4.7.
    
    Pour savoir comment configurer et gérer l'eSIM sur votre appareil, veuillez consulter [ce tutoriel](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
## Réseau

=== "Redirection de ports"

    La redirection de ports permet à des serveurs et appareils distants sur Internet d'accéder aux appareils d'un réseau privé. Pour configurer la redirection de ports, consultez [Redirection de ports](https://docs.gl-inet.com/router/en/4/interface_guide/firewall/#port-forwards).

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer simultanément plusieurs connexions Internet sur votre routeur (par exemple Cellular, Repeater et Ethernet). Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer le Multi-WAN, consultez [Multi-WAN](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

=== "LAN"

    Le LAN, ou réseau local, est un réseau qui relie des ordinateurs et des appareils dans une zone géographique limitée, comme une maison ou un bureau. Il permet des transferts de données à grande vitesse et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [Tutoriel LAN](../../interface_guide/lan.md).

---

=== "Réseau invité"

    Cette fonction vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de passerelle et de masque de sous-réseau, et de configurer des paramètres de sécurité comme l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Tutoriel LAN](../../interface_guide/guest_network.md).

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques de rebinding DNS, de remplacer les paramètres DNS de tous les clients, d'autoriser les DNS personnalisés à remplacer les DNS du VPN et de configurer le mode des paramètres du serveur DNS en automatique ou de spécifier manuellement les serveurs DNS issus de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Gestion des ports"

    La page Gestion des ports vous permet de configurer les ports WAN et LAN, de définir l'interface WAN/LAN sur Ethernet, de spécifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher le débit négocié du port réseau.

    Pour gérer les ports Ethernet, consultez [Gestion des ports](../../interface_guide/ethernet_port.md).

---

=== "Mode réseau"

    Le mode réseau désigne les paramètres de configuration qui déterminent comment un appareil se connecte à un réseau et communique avec les autres appareils.
    
    Pour configurer le mode réseau, consultez [Mode réseau](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, ou Internet Protocol version 6, est la version la plus récente du protocole Internet, conçue pour remplacer IPv4. Elle offre un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, indispensable pour répondre au nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPv6, consultez [IPv6](../../interface_guide/network_mode.md).

=== "Drop-in Gateway"

    Drop-in Gateway étend les fonctionnalités de votre routeur principal avec des fonctions qu'il peut ne pas posséder, notamment AdGuard Home, le DNS chiffré et le VPN. Pour configurer Drop-in Gateway, consultez [Comment configurer Drop-in Gateway](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_drop_in_gateway/).

---

=== "IGMP Snooping"

    L'IGMP Snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer l'IGMP Snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Accélération réseau"

    L'accélération matérielle désigne l'utilisation de composants matériels spécialisés pour exécuter certaines tâches plus efficacement que des processeurs généralistes.
    
    Pour configurer l'accélération réseau, consultez ce tutoriel [Accélération réseau](../../interface_guide/network_acceleration.md).

=== "Paramètres NAT"

    La page Paramètres NAT vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG (Application Layer Gateway).

    Pour configurer les paramètres NAT, consultez [Paramètres NAT](../../interface_guide/nat_settings.md).

## Système

=== "Aperçu"

    La page Aperçu fournit un instantané complet de l'état actuel de votre routeur et de ses indicateurs de performance. Sur cette page, vous pouvez consulter :

    * Charge CPU moyenne : surveillez la charge moyenne du processeur de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulets d'étranglement.
    * Utilisation de la mémoire : vérifiez quelle part de la mémoire du routeur est utilisée afin de mieux gérer les ressources.
    * Contrôle des LED : activez ou désactivez les voyants LED du routeur afin de personnaliser les indicateurs visuels de l'appareil.
    * Utilisation du stockage flash : visualisez l'occupation du stockage flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Informations sur l'appareil : accédez aux informations détaillées du système du routeur, notamment la durée de fonctionnement, le nom d'hôte, le modèle, l'architecture, la version d'OpenWrt, la version du noyau, l'ID de l'appareil, l'adresse MAC de l'appareil et son numéro de série.
    * Stockage externe : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que des clés USB ou des cartes TF.
    
    Ces fonctionnalités fournissent des informations et des commandes essentielles pour vous aider à gérer et surveiller efficacement le fonctionnement de votre routeur.

    Veuillez consulter [Aperçu](../../interface_guide/system_overview.md){target="_blank"} pour des instructions de configuration détaillées.

=== "Mise à niveau"

    La page Mise à niveau permet de mettre à jour le firmware du routeur vers la version la plus récente, afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à niveau :

    * Mise à niveau du firmware en ligne : recherchez et installez automatiquement la dernière version du firmware directement depuis le serveur du fabricant afin de simplifier la mise à jour.
    * Mise à niveau locale du firmware : téléversez manuellement un fichier firmware depuis votre ordinateur pour mettre à jour le routeur, avec un contrôle total sur la version et le moment de la mise à jour.
    * Mise à niveau en ligne du module : recherchez et installez automatiquement la dernière version du module 4G/5G directement depuis le serveur du fabricant afin de simplifier la mise à jour.
    * Mise à niveau locale du module : téléversez manuellement un fichier de module depuis votre ordinateur pour mettre à jour le module 4G/5G.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Veuillez consulter [Mise à niveau](../../interface_guide/upgrade.md){target="_blank"} pour des instructions détaillées.

=== "Tâches planifiées"

    La page Tâches planifiées vous permet d'automatiser différentes fonctions du routeur selon un planning prédéfini, pour plus de confort et d'efficacité. Les principales fonctions de cette page sont :

    * Planification de l'affichage des LED : définissez un planning pour allumer ou éteindre automatiquement les voyants LED du routeur afin de réduire la pollution lumineuse à certaines heures.
    * Redémarrage planifié : configurez le routeur pour redémarrer automatiquement à des intervalles définis afin de maintenir des performances et une stabilité optimales.
    * Planification de l'état du Wi‑Fi : définissez un planning pour contrôler les bandes Wi‑Fi 5 GHz / 2,4 GHz, afin de mieux gérer la disponibilité du réseau et la consommation d'énergie.
    
    Ces options de planification vous offrent un meilleur contrôle des opérations du routeur afin de répondre à vos besoins et à vos préférences.

    Veuillez consulter [Tâches planifiées](../../interface_guide/scheduled_tasks.md){target="_blank"} pour des instructions détaillées.

---

=== "Fuseau horaire"

    La page Fuseau horaire vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements exacts et exécuter correctement les configurations basées sur le temps.

    Veuillez consulter [Fuseau horaire](../../interface_guide/time_zone.md){target="_blank"} pour des instructions détaillées.

=== "Journal"

    La page Journal donne accès à différents journaux qui enregistrent les activités et les événements du routeur, facilitant ainsi le dépannage et le suivi des performances. Cette page comprend :

    * Journal système : journaux détaillés des événements et activités au niveau du système.
    * Journal du noyau : journaux liés au fonctionnement et aux événements du noyau.
    * Journal des plantages : enregistrements des plantages et erreurs du système, utiles pour diagnostiquer les problèmes critiques.
    * Journal Cloud : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Journal Nginx : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et les opérations du serveur.
    
    La page comporte également un bouton Export Log qui vous permet d'exporter tous les journaux collectés pour les transmettre au support technique. Cette fonction est précieuse pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Veuillez consulter [Journal](../../interface_guide/log.md){target="_blank"} pour des instructions détaillées.

=== "Sécurité"

    La page Sécurité vous permet de configurer divers paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend des options pour :

    * Mot de passe administrateur : définissez ou modifiez le mot de passe de l'interface d'administration du routeur afin que seuls les utilisateurs autorisés puissent modifier les paramètres.
    * Contrôle d'accès local : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Contrôle d'accès à distance : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, renforçant ainsi la sécurité face aux menaces externes.
    * Ports ouverts sur le routeur : contrôlez quels ports sont ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.

    Veuillez consulter [Sécurité](../../interface_guide/security.md) pour des instructions détaillées.

---

=== "Réinitialiser le firmware"

    La page Réinitialiser le firmware vous permet de rétablir les paramètres par défaut de la version actuelle du firmware du routeur, en effaçant toutes les configurations personnalisées. Ce processus remet le routeur aux paramètres par défaut de la version de firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir d'une configuration propre.

    Veuillez consulter [Réinitialiser le firmware](../../interface_guide/reset_firmware.md){target="_blank"} pour des instructions détaillées.

=== "Paramètres avancés"

    La page Paramètres avancés donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'affiner les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions de configuration détaillées et plus d'informations, consultez [Paramètres avancés](../../interface_guide/advanced_settings.md){target="_blank"}.
