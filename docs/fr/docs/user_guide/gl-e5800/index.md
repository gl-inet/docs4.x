# Guide d'utilisation du Mudi 7 (GL-E5800)

## Aperçu du produit

Mudi 7 est un routeur de voyage portable 5G NR Wi‑Fi 7 conçu pour les voyageurs fréquents et les professionnels en déplacement. Il fournit des réseaux privés fiables afin de protéger les données contre les cybermenaces. Il intègre la 5G haut débit, la commutation automatique double SIM (basculement), et le Wi‑Fi 7 (canaux 320MHz et 4K QAM) pour une connectivité stable et rapide, adaptée aux téléchargements rapides, au streaming 4K et à la visioconférence sans latence, même dans les zones très fréquentées.

Équipé d'un écran tactile, le Mudi 7 vous permet de surveiller en temps réel l'utilisation des données, la puissance du signal, les appareils connectés et la vitesse des clients, tout en ajustant les paramètres d'un simple toucher pour une utilisation intuitive et sans contrainte.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Contenu du colis

- 1 x Mudi 7 (GL-E5800)
- 1 x Batterie
- 1 x Câble USB-C 10Gbps
- 1 x Pochette de transport
- 1 x Manuel d'utilisation

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Regardez la vidéo de déballage du Mudi 7 ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Configuration initiale du Mudi 7

Regardez cette vidéo de configuration ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Installer la carte SIM

Installez la ou les cartes Nano-SIM dans votre Mudi 7. Si vous préférez utiliser l'eSIM, ignorez cette étape et passez à l'étape 2.

Commencez par retirer le couvercle de la batterie, puis retirez la batterie du Mudi 7.

Insérez ensuite la ou les cartes Nano-SIM. Si vous n'utilisez qu'une seule carte, privilégiez SIM 1.

Remettez enfin la batterie et le couvercle en place.

![install nano-sim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/install_nano-sim.png){class="glboxshadow"}

### 2. Mise sous tension

Maintenez le bouton d'alimentation enfoncé pendant **3 secondes**, ou branchez un adaptateur secteur.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power_on.png){class="glboxshadow"}

### 3. Paramètres de base

Suivez les instructions affichées à l'écran pour configurer les paramètres de base, notamment le **screen passcode**, le **admin password**, le **Wi-Fi name**, le **Wi-Fi password** et les **frequency bands**.

**Astuce** : le mot de passe administrateur par défaut correspond aux 9 derniers caractères du S/N de l'appareil, suivis du caractère #. Vous pouvez utiliser ce mot de passe par défaut ou en définir un personnalisé.

### 4. Configuration Internet

Configurez votre Mudi 7 à l'aide de l'une des méthodes de connexion Internet prises en charge : Cellular, Ethernet, Repeater, Tethering et USB Ethernet. Si vous souhaitez utiliser la fonctionnalité [Multi-WAN](../../interface_guide/multi-wan.md), configurez plus d'une connexion Internet.


=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Le Mudi 7 est équipé d’une **eSIM intégrée** et de **deux emplacements Nano‑SIM**. Vous pouvez vous connecter à Internet en achetant un forfait eSIM (sans carte SIM physique), ou en insérant vos cartes Nano‑SIM pour accéder au réseau mobile 5G.

    **Configurer l’eSIM** :

    1. Sur l’écran tactile, accédez à **Cellular** -> **SIM Card Switch**, puis activez **enable eSIM**.

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. Connectez-vous au panneau d’administration web, puis accédez à **INTERNET** -> **Cellular** -> **eSIM Management**.

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. Dans la fenêtre contextuelle, cliquez sur **Add eSIM Profile** en bas.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        Importez votre profil eSIM via un QR code ou un code d’activation, puis cliquez sur **Install**. Notez que la plupart des profils eSIM ne peuvent être téléchargés et ajoutés qu’une seule fois.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Astuce** : si vous n’avez pas encore acheté de profil eSIM, vous pouvez en acheter un dans **eSIM Profile Recommended Store**.

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. Une fois le profil importé, accédez à **Cellular** et cliquez sur **SIM Card Switch**.

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        Dans la fenêtre contextuelle, sélectionnez **eSIM** comme carte SIM active, puis cliquez sur **Apply**.

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. Le routeur commencera à se connecter via ce profil eSIM. Patientez, puis vérifiez que la connexion a réussi.

    **Configurer une Nano‑SIM** :

    1. Retirez le couvercle arrière, sortez la batterie, insérez votre carte Nano‑SIM dans l’emplacement prévu, puis remettez la batterie en place.

    2. Le routeur commencera automatiquement à se connecter via cette carte Nano‑SIM. Patientez, puis vérifiez que la connexion a réussi.

    Une fois la connexion Internet établie, les barres de signal et l’état de la connexion cellulaire s’affichent dans l’angle supérieur droit de l’écran tactile. Vous pouvez également consulter les détails de la connexion dans le panneau d’administration web.

    Pour des instructions détaillées, consultez [Se connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md).

    !!! note

        1. L’eSIM intégrée et la SIM 2 sont mutuellement exclusives et ne peuvent pas être activées en même temps. L’eSIM est désactivée par défaut. Si vous activez l’eSIM, la SIM 2 ne fonctionnera pas, même si une carte SIM est insérée.
        2. Comme le Mudi 7 dispose d’une eSIM intégrée, une carte eSIM physique SIMPoYo sera reconnue comme une carte SIM classique, sans fonctionnalité eSIM, sur le Mudi 7.

=== "Ethernet"
    
    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Connectez le port Ethernet du Mudi 7 à une source réseau en amont (par exemple un modem du FAI, un commutateur réseau ou une prise Ethernet murale) à l'aide d'un câble Ethernet.
    2. Sur l'écran tactile ou dans le panneau d'administration web, accédez à **Network** -> **Ethernet Ports**, définissez la fonction du port sur **WAN**, puis cliquez sur **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Une fois la connexion Internet établie, une icône de port Ethernet s'affiche dans l'angle supérieur droit de l'écran tactile. Vous pouvez également consulter les détails de la connexion dans le panneau d'administration web.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md).

=== "Repeater"
    
    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Sur l'écran tactile ou dans le panneau d'administration web, accédez à **Internet** -> **Repeater**, puis cliquez sur **Connect**. Le Mudi 7 commence alors à rechercher les réseaux Wi‑Fi disponibles.
    2. Sélectionnez le réseau Wi‑Fi que vous souhaitez étendre avec le Mudi 7.
    3. Saisissez le mot de passe, puis cliquez sur **Apply**.
    4. Une fois la connexion Internet établie, une icône Wi‑Fi s'affiche dans l'angle supérieur droit de l'écran tactile. Vous pouvez également consulter les détails de la connexion dans le panneau d'administration web.

    Pour des instructions détaillées, consultez [Se connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Connectez votre appareil mobile (par exemple un smartphone ou un dongle USB) au port USB-C du Mudi 7 à l'aide d'un câble USB.
    2. Sur votre appareil mobile, accédez aux réglages et activez **USB Tethering**. Si vous utilisez un iPhone, appuyez sur **Trust This Device** si cela vous est demandé.
    3. Le Mudi 7 se connectera ensuite automatiquement à votre appareil. Si ce n'est pas le cas, répétez les étapes ci-dessus, ou connectez-vous au panneau d'administration web et vérifiez la connexion Tethering sur la page INTERNET.
    4. Une fois la connexion Internet établie, une icône en forme de maillon de chaîne s'affiche dans l'angle supérieur droit de l'écran tactile. Vous pouvez également consulter les détails de la connexion dans le panneau d'administration web.

    Pour des instructions détaillées, consultez [Se connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md).

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Le Mudi 7 est équipé d'un port USB-C **compatible OTG**, ce qui vous permet d'ajouter un second port Ethernet pour une configuration Dual-Ethernet WAN. Cela nécessite un **adaptateur USB‑C‑vers‑Ethernet vendu séparément**.

    <small>*USB OTG (On-The-Go) est une norme USB qui permet aux appareils compatibles, comme les routeurs, de basculer entre les rôles d'hôte et de périphérique, afin d'assurer la transmission directe des données et l'interaction électrique sans appareil hôte distinct.</small>

    1. Connectez une source réseau en amont (par exemple un modem du FAI, un commutateur réseau ou une prise Ethernet murale) au port USB-C du Mudi 7 à l'aide d'un adaptateur USB‑C‑vers‑Ethernet.
    2. Sur l'écran tactile ou dans le panneau d'administration web, accédez à **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, définissez la fonction du port sur **WAN**, puis cliquez sur **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Le Mudi 7 se connectera ensuite automatiquement à votre appareil. Si ce n'est pas le cas, répétez les étapes ci-dessus, ou connectez-vous au panneau d'administration web et vérifiez la connexion USB Ethernet sur la page INTERNET.
    3. Une fois la connexion Internet établie, une icône USB et une icône de port Ethernet s'affichent dans l'angle supérieur droit de l'écran tactile. Vous pouvez également consulter les détails de la connexion dans le panneau d'administration web.


## Mise à niveau du firmware

!!! note "Avant la mise à niveau, veuillez noter les points suivants :"

    1. Pour conserver la configuration de votre Mudi 7, sélectionnez **Keep Settings** sur la page de mise à niveau.
    2. Ne sélectionnez pas **Keep Settings** lors d'une rétrogradation du firmware, car des problèmes de compatibilité peuvent survenir.
    3. La mise à niveau du firmware consomme un certain volume de données. Si votre forfait de données SIM est limité, il est recommandé de connecter le routeur à Internet par d’autres méthodes (comme Repeater, USB Tethering, etc.) pour éviter une consommation supplémentaire.

Vous pouvez mettre à niveau le firmware du Mudi 7 via l’écran tactile ou le panneau d’administration web.

### Mise à niveau via l’écran tactile

1. Connectez votre Mudi 7 à Internet.

2. Une fois connecté, le système vérifie automatiquement si des mises à jour du firmware sont disponibles. Si une nouvelle version est disponible, une invite s’affiche à l’écran. Dans cette fenêtre, cliquez sur **Go to Upgrade** pour continuer.

    ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. Si la fenêtre contextuelle n’apparaît pas, cliquez sur **More** sur l’écran d’accueil -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade**, puis suivez les instructions à l’écran pour mettre le firmware à niveau.

    ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Mise à niveau via l’interface web

1. Mise à niveau en ligne

    Connectez-vous au panneau d’administration web, puis accédez à **SYSTEM** -> **Upgrade** -> **Firmware Online Upgrade** pour mettre à jour le firmware de votre routeur.

    Pour plus de détails, consultez [cette section](../../interface_guide/upgrade.md#online-upgrade).

2. Mise à niveau locale

    Connectez-vous au panneau d’administration web, puis accédez à **SYSTEM** -> **Upgrade** -> **Firmware Local Upgrade** pour mettre à jour le firmware de votre routeur.

    Pour plus de détails, consultez [cette section](../../interface_guide/upgrade.md#local-upgrade).

## Réparation et réinitialisation

Vous pouvez rétablir la connectivité réseau ou réinitialiser le Mudi 7 aux paramètres d'usine à l'aide du bouton physique de réinitialisation.

**Remarque** : avant d'effectuer une réinitialisation, assurez-vous que le Mudi 7 a complètement démarré. N'appuyez **PAS** sur le bouton de réinitialisation immédiatement après la mise sous tension, car cela pourrait déclencher le mode de secours U-Boot.

Retirez le couvercle arrière, puis localisez le bouton de réinitialisation comme illustré ci-dessous.

![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

!!! note "Réparation du réseau"

    Maintenez le bouton de réinitialisation enfoncé pendant **4 secondes**, puis relâchez-le pour réparer votre réseau. Pendant que vous maintenez le bouton, suivez les indications affichées à l'écran.

    Cela redémarrera l'interface réseau tout en conservant les paramètres Wi‑Fi, les configurations VPN (désactivées), les paramètres système, etc.

    **Remarque** :

    1. Si le Wi‑Fi a été désactivé, une réinitialisation logicielle le réactivera avec son état par défaut.

    2. Une réinitialisation logicielle peut également être utilisée pour faire basculer rapidement l'appareil du mode non-routeur au mode routeur.

!!! note "Réinitialisation de l'appareil"

    Maintenez le bouton de réinitialisation enfoncé pendant **10 secondes**, puis relâchez-le pour effectuer une réinitialisation complète. Pendant que vous maintenez le bouton, suivez les indications affichées à l'écran.
    
    Cette opération effacera tous vos paramètres. Procédez avec prudence.

## Connexion au panneau d'administration web

Vous pouvez vous connecter au panneau d'administration web du Mudi 7 pour configurer ou consulter davantage de paramètres.

Commencez par connecter un appareil (par exemple un ordinateur, un ordinateur portable ou un smartphone) au Mudi 7 via le Wi‑Fi, un câble Ethernet ou un câble USB.

- **Wi-Fi**

    - <u>QR code</u> : utilisez votre appareil pour scanner le QR code affiché sur l'écran du Mudi 7. Cliquez ensuite sur "Join" sur votre appareil pour vous connecter.
    - <u>Manual Connect</u> : sur votre appareil, accédez à Paramètres -> WLAN, repérez le nom du réseau Wi‑Fi du Mudi 7 dans la liste des réseaux disponibles, puis saisissez le mot de passe pour vous y connecter. (Le nom du réseau et le mot de passe par défaut sont imprimés sur l'étiquette.)

- **Ethernet**

    Connectez votre appareil au port Ethernet du Mudi 7 (LAN par défaut) à l'aide d'un câble Ethernet.

- **USB**

    Connectez votre appareil au port USB-C du Mudi 7 à l'aide d'un câble USB. Le port USB-C compatible OTG vous permet d'accéder à la WebGUI du Mudi 7 à l'étape suivante.

Ouvrez ensuite un navigateur web et saisissez `192.168.8.1` dans la barre d'adresse pour accéder à la page de connexion. Sélectionnez votre langue, définissez votre mot de passe administrateur, puis cliquez sur **Apply**.

Vous serez alors connecté au panneau d'administration web du Mudi 7.

Vous trouverez ci-dessous un aperçu des fonctionnalités du panneau d'administration web du Mudi 7.

## Réseau sans fil

La page Wireless permet de configurer les paramètres des réseaux Wi‑Fi 6 GHz, 5 GHz et 2,4 GHz, notamment l'activation du Wi‑Fi, le réglage de la puissance TX, la définition du nom du réseau Wi‑Fi (SSID), l'activation d'un BSSID aléatoire, le choix du mode de sécurité Wi‑Fi et du mot de passe, la configuration de la visibilité du SSID, ainsi que le mode Wi‑Fi, la bande passante et le canal.

Pour configurer le réseau sans fil, consultez [Wireless](../../interface_guide/wireless.md).

**Remarque** : les paramètres sans fil du Mudi 7 présentent quelques différences par rapport à ceux des autres routeurs GL.iNet Wi‑Fi 7.

1. En raison des contraintes matérielles du chipset, les réseaux Wi‑Fi 5 GHz et 6 GHz ne peuvent pas être activés simultanément.
2. Lorsque Repeater est activé, le réseau invité sera désactivé automatiquement.
3. Conformément à la réglementation, passez le Wi‑Fi en mode Outdoor lors d'une utilisation en extérieur. Cela peut réduire la zone de couverture. Vous pouvez modifier le Usage Environment (Indoor ou Outdoor) en haut de la page Wireless.

## Clients

La page Clients affiche les informations sur les appareils connectés. Pour chaque client, elle indique le nom, les adresses IP et MAC, les vitesses de téléchargement et d'envoi, le trafic total, et permet de bloquer le client ou d'effectuer d'autres actions.

Pour configurer les clients, consultez [Clients](../../interface_guide/clients.md).

## Services Cloud

=== "GoodCloud"

    Le service de gestion cloud GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} offre un moyen simple et pratique d'accéder à distance aux routeurs GL.iNet et de les gérer.
    
    Pour configurer GoodCloud, consultez [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp est une plateforme réseau avancée conçue pour offrir une mise en réseau à distance fluide et une gestion à distance des appareils. Spécialement conçue pour l'intégration avec les routeurs GL.iNet, AstroWarp prend en charge une gestion complète des appareils à l'échelle de réseaux entiers, permettant le contrôle des équipements en amont comme en aval. En mettant l'accent sur la gestion réseau globale et sur une future prise en charge du contrôle au niveau matériel, AstroWarp offre une solution plus robuste et plus fiable pour gérer les appareils et maintenir des réseaux sûrs et stables.
    
    Pour configurer AstroWarp, consultez [AstroWarp](../../interface_guide/astrowarp.md).

## VPN 

Un VPN (réseau privé virtuel) crée un trafic sécurisé et chiffré entre votre appareil et le serveur VPN. Il ajoute une couche supplémentaire de confidentialité et de sécurité (client VPN) et vous permet d'accéder à un réseau distant (serveur VPN). Le Mudi 7 prend en charge OpenVPN et WireGuard.

=== "OpenVPN" 
    
    Le Mudi 7 (comme les autres routeurs GL.iNet) prend en charge le protocole OpenVPN, qui offre une sécurité renforcée. Pour configurer OpenVPN, suivez ces tutoriels :

    * [Configurer un client OpenVPN](../../interface_guide/openvpn_client.md)
    * [Configurer un serveur OpenVPN](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Le Mudi 7 (comme les autres routeurs GL.iNet) prend en charge le protocole WireGuard, qui offre d'excellentes vitesses et une utilisation pratique. Pour configurer WireGuard, suivez ces tutoriels :

    * [Configurer un client WireGuard](../../interface_guide/wireguard_client.md)
    * [Configurer un serveur WireGuard](../../interface_guide/wireguard_server.md)

## Réseau

=== "Multi-WAN"

    Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Ethernet, Repeater, Tethering, Cellular et USB Ethernet) en même temps. Si votre connexion Internet actuelle échoue, le routeur bascule automatiquement vers une autre connexion Internet. Cela garantit un accès Internet fluide et ininterrompu.

    Pour configurer Multi-WAN, consultez [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    Un LAN, ou Local Area Network, est un réseau qui relie des ordinateurs et des appareils dans une zone géographique limitée, telle qu'un domicile ou un bureau. Il permet un transfert de données à grande vitesse et le partage de ressources, afin que les appareils puissent communiquer efficacement entre eux.
    
    Pour configurer le LAN, consultez [Lan](../../interface_guide/lan.md).

=== "Guest Network"

    Cette fonction vous permet de définir un sous-réseau dans les plages d'adresses privées IPv4 192.168.0.0/16, 172.16.0.0/12 ou 10.0.0.0/8, de spécifier les adresses IP de la passerelle et du masque réseau, et de configurer des paramètres de sécurité tels que l'isolation AP pour le réseau invité.

    Pour configurer le réseau invité, consultez [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    La page DNS vous permet de définir des serveurs DNS personnalisés, d'activer la protection contre les attaques DNS rebinding et de remplacer les paramètres DNS de tous les clients, d'autoriser le DNS personnalisé à remplacer le DNS du VPN, et de configurer le mode des paramètres du serveur DNS sur automatique ou de spécifier manuellement les serveurs DNS de la connexion Ethernet.

    Pour configurer le DNS, consultez [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    La page Ethernet Port vous permet de définir la fonction du port Ethernet (c'est-à-dire l'utiliser en WAN ou en LAN), de modifier le mode MAC et l'adresse MAC de l'interface WAN, et d'afficher la vitesse négociée du port.

    Le Mudi 7 dispose d'un seul port Ethernet, configuré par défaut en LAN. Vous pouvez le faire passer en port WAN sur l'écran tactile ou dans le panneau d'administration web si nécessaire.

    Pour gérer les ports Ethernet, consultez [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, abréviation de version 6 du protocole Internet, est la version la plus récente du protocole Internet conçue pour remplacer IPv4. Elle fournit un espace d'adressage bien plus vaste, permettant un nombre quasiment illimité d'adresses IP uniques, ce qui est essentiel face au nombre croissant d'appareils connectés à Internet.
    
    Pour configurer IPV6, consultez [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP snooping est une technique d'optimisation réseau utilisée dans les commutateurs Ethernet pour gérer et contrôler le trafic multicast.
    
    Pour configurer IGMP snooping, consultez [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Le mode réseau correspond à la configuration qui détermine la manière dont un appareil se connecte à un réseau et communique avec les autres appareils.
    
    Pour configurer le mode réseau, consultez [Network Mode](../../interface_guide/network_mode.md).

    **Remarque** : le Mudi 7 prend en charge les modes Router, Access Point et Extender. Il ne prend pas en charge le mode WDS.

=== "Drop-in gateway"

    Drop-in gateway étend les fonctionnalités de votre routeur principal, notamment AdGuard Home, le DNS chiffré et le client VPN.
    
    Pour configurer drop-in gateway, consultez les liens suivants :
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [Comment configurer drop-in gateway](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    Network Acceleration peut réduire la charge CPU et accélérer l'acheminement des paquets réseau.
    
    Pour configurer Network Acceleration, consultez [Network Acceleration](../../interface_guide/network_acceleration.md).

## Contrôle du flux

=== "Parental Control"

    Parental Control est conçu pour vous aider à gérer et contrôler les appareils de vos enfants. Il permet notamment de limiter leur temps d'écran et de restreindre leur accès à certains contenus.

    Pour configurer le contrôle parental, consultez [Parental Control](../../interface_guide/parental_control.md).

## Sécurité

=== "Port Forwarding"

    Port Forwarding permet aux serveurs distants et aux appareils situés sur Internet d'accéder aux appareils d'un réseau privé.
    
    Pour configurer la redirection de ports, consultez [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Management Control vous permet de configurer différents paramètres de sécurité afin de protéger votre réseau et votre routeur contre les accès non autorisés. Cette page comprend les options suivantes :

    * Local Access Control : gérez et limitez l'accès à l'interface du routeur depuis les appareils connectés à votre réseau local.
    * Remote Access Control : configurez et limitez l'accès à l'interface du routeur depuis des emplacements distants via Internet, afin de renforcer la sécurité face aux menaces externes.
    * Open Ports on Router : contrôlez les ports ouverts sur le routeur afin de limiter les vulnérabilités potentielles et les accès non autorisés.

    Ces paramètres vous aident à maintenir un environnement réseau sécurisé, en protégeant à la fois votre routeur et les appareils connectés.

    Pour des instructions détaillées, consultez [Security](../../interface_guide/security.md).

=== "NAT Mode"

    La page NAT Mode vous permet d'activer ou de désactiver les fonctions Full Cone NAT et SIP ALG.

    Pour configurer les paramètres NAT, consultez [NAT Mode](../../interface_guide/nat_settings.md).

## Applications

=== "Plug-ins"

    Un plug-in est un composant logiciel qui ajoute des fonctions spécifiques à un programme informatique existant, permettant de personnaliser et d'étendre ses capacités.
    
    Pour configurer les plug-ins, consultez [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Le DNS dynamique (DDNS) détecte et met à jour automatiquement en temps réel l'adresse IP associée à un domaine. Il est particulièrement utile pour les utilisateurs qui ont besoin d'une adresse IP statique afin d'accéder à un réseau distant.
    
    Pour configurer Dynamic DNS, consultez [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Le stockage réseau désigne une solution de stockage de données centralisée qui permet à plusieurs utilisateurs et appareils d'accéder aux fichiers et de les partager sur un réseau.
    
    Pour configurer le stockage réseau, consultez [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home est une solution de blocage des publicités et des traqueurs à l'échelle du réseau. Elle agit comme un serveur DNS pour filtrer les contenus indésirables sur tous les appareils connectés à un réseau domestique.
    
    Pour configurer AdGuard Home, consultez [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier est une solution réseau définie par logiciel qui permet de créer des réseaux virtuels sécurisés via Internet, en connectant les appareils comme s'ils se trouvaient sur le même réseau local.
    
    Pour configurer ZeroTier, consultez [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale est un service VPN qui vous permet d'accéder à vos appareils et à vos applications où que vous soyez.
    
    Pour configurer Tailscale, consultez [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, abréviation de The Onion Router, est un réseau axé sur la protection de la vie privée qui permet une communication anonyme sur Internet. Il achemine le trafic Internet via une série de serveurs exploités par des bénévoles (nœuds) afin de masquer l'emplacement et l'utilisation de l'utilisateur, ce qui rend les activités en ligne difficiles à tracer.
    
    Pour configurer Tor, consultez [Tor](../../interface_guide/tor.md).

## Système

=== "Overview"

    La page Overview fournit un aperçu complet de l'état actuel et des performances de votre routeur. Sur cette page, vous pouvez consulter :

    * CPU Average Load : surveillez la charge moyenne du CPU de votre routeur afin d'évaluer les performances et d'identifier d'éventuels goulots d'étranglement.
    * Memory Usage : vérifiez la quantité de mémoire utilisée par votre routeur afin de mieux gérer les ressources.
    * LED Control : activez ou désactivez les voyants LED du routeur pour personnaliser les indicateurs visuels de l'appareil.
    * Flash Usage : affichez l'utilisation de la mémoire flash du routeur afin de vérifier qu'il reste suffisamment d'espace pour le firmware et les données de configuration.
    * Device Info : accédez aux informations détaillées du système de votre routeur, notamment l'uptime, le hostname, le model, l'architecture, la version OpenWrt, la version du kernel, le device ID, la device MAC et le device S/N.
    * External Storage : vérifiez l'état des périphériques de stockage externes connectés au routeur, tels que les clés USB ou les cartes TF.
    
    Ces fonctionnalités fournissent des informations essentielles et des commandes utiles pour gérer et surveiller efficacement le fonctionnement de votre routeur.

    Pour des instructions détaillées, consultez [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    La page Admin Password vous permet de définir ou de modifier le mot de passe de l'interface d'administration du routeur.

    Le mot de passe administrateur doit respecter les exigences suivantes :

    * Minimum 10 caractères et maximum 63 caractères.
    * Les lettres (sensibles à la casse), les chiffres et les symboles `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` sont autorisés.
    * Au moins deux des catégories suivantes sont requises : lettres majuscules, lettres minuscules, chiffres et symboles.

=== "Upgrade"

    La page Upgrade permet de mettre à jour le firmware de votre routeur vers la dernière version afin d'améliorer les performances, la sécurité et d'ajouter de nouvelles fonctionnalités. Cette page propose deux options de mise à niveau :

    * Firmware Online Upgrade : vérifiez automatiquement la disponibilité de la dernière version du firmware et installez-la directement depuis le serveur du fabricant, ce qui simplifie la mise à jour.
    * Firmware Local Upgrade : téléversez manuellement un fichier de firmware depuis votre ordinateur pour mettre à jour le routeur, ce qui vous permet de contrôler la version et le moment de la mise à niveau.

    Ces options vous permettent de maintenir votre routeur à jour avec les dernières améliorations et corrections.

    Pour des instructions détaillées, consultez [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    La page Scheduled Tasks vous permet de configurer le redémarrage automatique du routeur à des intervalles spécifiés, afin de maintenir des performances et une stabilité optimales.

    Pour des instructions détaillées, consultez [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Remarque** : le Mudi 7 ne prend pas en charge la programmation de l'affichage LED ni la programmation de l'état du Wi‑Fi.

=== "Display Management"

    La page Display Management vous permet de gérer l'écran tactile et les paramètres associés.
    
    - Wallpaper : personnalisez le fond d'écran et le mode de réveil de l'affichage.
    - Brightness : ajustez la luminosité de l'écran tactile. Utilisez le curseur ou saisissez un pourcentage en fonction des conditions d'éclairage.
    - Personalised Signature : ajoutez un texte personnalisé à l'écran tactile pour afficher votre style ou identifier rapidement l'appareil.
    - Auto Lock : définissez le délai avant le verrouillage automatique de l'écran en l'absence d'activité. La plage va de 15 secondes à 5 minutes.
    - Passcode : définissez un code pour l'écran tactile afin d'ajouter une couche de sécurité supplémentaire.

    Pour des instructions détaillées, consultez [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    La page USB & Power vous permet de configurer les paramètres liés à l'USB et à la gestion de l'alimentation de votre routeur, comme le protocole USB, le sens de l'alimentation, les délais d'inactivité et le comportement en veille.

    Pour des instructions détaillées, consultez [USB & Power](../../interface_guide/usb_power.md).

---

=== "Time Zone"

    La page Time Zone vous permet de définir le fuseau horaire correct pour votre routeur, afin que toutes les tâches planifiées, les journaux et les événements système soient horodatés avec précision selon votre heure locale. Ce réglage est essentiel pour conserver des enregistrements précis et pour le bon fonctionnement des configurations basées sur le temps.

    Pour des instructions détaillées, consultez [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    La page Reset Firmware vous permet de réinitialiser la version actuelle du firmware de votre routeur à ses paramètres par défaut, en effaçant toutes les configurations personnalisées. Ce processus restaure les paramètres par défaut de la version du firmware actuellement installée. Cela peut être utile pour résoudre des problèmes persistants ou repartir sur une configuration propre avec les paramètres par défaut du firmware actuel.

    Pour des instructions détaillées, consultez [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    La page Log donne accès à différents journaux qui enregistrent les activités et événements du routeur, ce qui facilite le dépannage et le suivi des performances. Cette page comprend :

    * System Log : journaux détaillés des événements et activités au niveau système.
    * Kernel Log : journaux liés aux opérations et événements du noyau.
    * Crash Log : enregistrements des plantages système et des erreurs, utiles pour diagnostiquer les problèmes critiques.
    * Cloud Log : journaux des interactions et activités liées aux services GoodCloud intégrés au routeur.
    * Nginx Log : journaux du serveur web Nginx, s'il est utilisé par le routeur, détaillant le trafic web et le fonctionnement du serveur.
    
    La page comporte également un bouton Export Log, qui vous permet d'exporter tous les journaux collectés pour analyse par le support technique. Cette fonction est particulièrement utile pour diagnostiquer des problèmes complexes et obtenir une assistance professionnelle.

    Pour des instructions détaillées, consultez [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    La page Advanced Settings donne accès à des options de configuration avancées via l'interface OpenWrt LuCI, permettant aux utilisateurs expérimentés d'ajuster finement les paramètres et fonctionnalités du routeur au-delà des options de l'interface de base. Cela inclut des configurations réseau détaillées, des paramètres de pare-feu et d'autres personnalisations système avancées.

    Pour des instructions détaillées, consultez [Advanced Settings](../../interface_guide/advanced_settings.md).
