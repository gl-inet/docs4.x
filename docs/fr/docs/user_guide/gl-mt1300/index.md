# Guide d'utilisation du Beryl (GL-MT1300)

## Aperçu du produit

Le Beryl (GL-MT1300) est un routeur de poche hautes performances. Il associe un matériel puissant, des protocoles de cybersécurité de premier ordre et un design moderne et distinctif. Version avancée de notre modèle phare Slate (GL-AR750S), Beryl représente une nouvelle génération de routeurs de voyage.

![gl-mt1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/hardware_info/mt1300_interface.jpg){class="glboxshadow"}

## Contenu du colis

Veuillez noter que l'adaptateur fourni dépend du pays de livraison.

Le colis comprend :

- 1 x manuel d'utilisation
- 1 x Beryl (GL-MT1300)
- 1 x câble Ethernet
- 1 x carte de remerciement
- 1 x carte de garantie
- 1 x adaptateur d'alimentation (type de prise sélectionné)

![gl-mt1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/first_time_setup/mt1300_unboxing.jpg){class="glboxshadow"}

Consultez la [vidéo de déballage](../../video_library/unboxing_first_set_up.md/#gl-mt1300-beryl) du Beryl.

## Spécifications

[Spécifications du GL-MT1300](https://www.gl-inet.com/products/gl-mt1300/#specs){target="_blank"}

## Configuration initiale

Tous les routeurs GL.iNet suivent un processus de configuration similaire. [Cliquez ici pour en savoir plus sur la configuration initiale](../../faq/first_time_setup.md/).

## INTERNET

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** dans le menu de gauche.

Cette page vous permet de sélectionner le type de connexion Internet, par exemple Ethernet, Repeater, Tethering ou Cellular.

### Ethernet

Connectez votre routeur à un modem actif ou à un équipement réseau actif via un câble Ethernet pour accéder à Internet. Cette méthode offre généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour découvrir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_ethernet.png){class="glboxshadow"}

### Repeater

Configurez votre routeur en mode répéteur afin d'étendre la couverture Wi‑Fi d'un réseau Wi‑Fi existant. En tant que répéteur, il reçoit et retransmet les signaux sans fil dans sa portée, ce qui étend la zone couverte. Cette méthode est utile lorsqu'un seul routeur ne peut pas couvrir toute la zone d'utilisation.

[Cliquez ici pour découvrir comment vous connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_repeater.png){class="glboxshadow"}

### Tethering

Connectez le port USB du routeur à un smartphone disposant d'une connexion de données mobiles active à l'aide d'un câble USB pour accéder à Internet. Cette méthode permet à plusieurs appareils connectés au routeur d'accéder à Internet via les données mobiles du smartphone.

[Cliquez ici pour découvrir comment vous connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_tethering.png){class="glboxshadow"}

### Cellular

Connectez le routeur à Internet en branchant un modem USB compatible réseau cellulaire sur son port USB. Cette méthode est utile pour partager la connexion Internet d'un modem USB avec tous les appareils connectés.

[Cliquez ici pour découvrir comment vous connecter à Internet via un modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mt1300/internet/mt1300_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Ethernet et Repeater) en même temps. Si la connexion Internet prioritaire échoue, le routeur bascule automatiquement vers une autre connexion. Ce mécanisme est également appelé basculement et garantit un accès à Internet fluide et ininterrompu.

Accédez à [Multi-WAN](../../interface_guide/multi-wan.md) pour définir la priorité de chaque connexion Internet.

Vous pouvez également faire passer le mode Multi-WAN de Failover à Load Balance, ce qui permet d'utiliser plusieurs interfaces réseau simultanément afin d'augmenter la bande passante totale du routeur.

---

## WIRELESS

Les paramètres sans fil permettent de gérer la sécurité réseau du Wi‑Fi principal et du Wi‑Fi invité. Ils sont accessibles via **WIRELESS** dans le menu latéral.

[Cliquez ici pour en savoir plus sur la configuration sans fil](../../interface_guide/wireless.md)

---

## CLIENTS

Les clients sont les appareils connectés au routeur. Vous pouvez bloquer des clients ou limiter leur vitesse réseau. Cette interface est accessible en cliquant sur **CLIENTS** dans le menu latéral du panneau d'administration du routeur.

[Cliquez ici pour en savoir plus sur la gestion des appareils clients.](../../interface_guide/clients.md)

---

## VPN

Les routeurs GL.iNet intègrent un client VPN et un serveur VPN préinstallés pour OpenVPN et WireGuard.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Consultez les liens ci-dessous pour obtenir des instructions de configuration détaillées :

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard

Consultez les liens ci-dessous pour obtenir des instructions de configuration détaillées :

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

### Plug-ins

Veuillez consulter le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Veuillez consulter le tutoriel [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Veuillez consulter le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage

Veuillez consulter le tutoriel [**Network Storage**](../../interface_guide/network_storage.md).

---

## NETWORK

### Firewall

Les routeurs GL.iNet intègrent plusieurs fonctions de pare-feu afin de garantir une connexion sécurisée et un contrôle complet par l'utilisateur. Vous pouvez y configurer des règles de pare-feu, notamment Port Forwarding, Open Ports et DMZ.

[Cliquez ici pour en savoir plus sur le pare-feu des routeurs GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Veuillez consulter le tutoriel [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Veuillez consulter le tutoriel [**LAN**](../../interface_guide/lan.md).

### DNS

Veuillez consulter le tutoriel [**DNS**](../../interface_guide/dns.md).

### Network Mode

Veuillez consulter le tutoriel [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Veuillez consulter le tutoriel [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

La page Mac Address s'appelait auparavant Mac Clone et a été renommée Mac Address depuis la version v4.2.

Veuillez consulter le tutoriel [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Veuillez consulter le tutoriel [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Veuillez consulter le tutoriel [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

### Network Acceleration

Anciennement appelé [Hardware Acceleration](../../interface_guide/hardware_acceleration.md).

Veuillez consulter le tutoriel [**Network Acceleration**](../../interface_guide/network_acceleration.md).

---

## SYSTEM

### Overview

Veuillez consulter le tutoriel [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet publie régulièrement des mises à jour du firmware de ses routeurs afin d'améliorer les performances, de corriger les bogues et de résoudre les vulnérabilités.

Veuillez consulter le tutoriel [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Veuillez consulter le tutoriel [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Cette fonctionnalité a été déplacée vers [**Security**](../../interface_guide/security.md) depuis la version v4.5.

Veuillez consulter le tutoriel [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Veuillez consulter le tutoriel [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings

Veuillez consulter le tutoriel [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Veuillez consulter le tutoriel [**Log**](../../interface_guide/log.md).

### Security

Cette fonctionnalité est disponible depuis la version v4.5.

Veuillez consulter le tutoriel [**Security**](../../interface_guide/security.md).

### Reset Firmware

Veuillez consulter le tutoriel [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Veuillez consulter le tutoriel [**Advanced Settings**](../../interface_guide/advanced_settings.md).
