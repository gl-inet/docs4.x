# Guide d'utilisation de Puli (GL-XE300)

## Aperçu du produit

Puli (GL-XE300) est un routeur intelligent 4G portable, idéal pour la maison, les voyages, les activités professionnelles et les solutions IoT. Grâce à sa compatibilité avec OpenWrt et à la prise en charge de grands espaces de stockage, il est conçu pour vous permettre de développer vos propres projets IoT. Il est également équipé d'une batterie rechargeable, ce qui permet une utilisation mobile dans différents environnements.

![gl-xe300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/hardware_info/gl-xe300_interface.jpg){class="glboxshadow"}

## Contenu du colis

Veuillez noter que l'adaptateur inclus dans l'emballage dépend de votre pays de livraison.

Le colis comprend :

- 1 x Manuel de l'utilisateur
- 1 x Puli (GL-XE300)
- 1 x Câble Ethernet
- 1 x Carte de remerciement
- 1 x Carte de garantie
- 1 x Adaptateur secteur (type de prise sélectionné)

![gl-xe300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/first_time_setup/xe300_unboxing.jpg){class="glboxshadow"}

Regardez la [vidéo de déballage de Puli](../../video_library/unboxing_first_set_up.md/#gl-xe300-puli).

## Spécifications

[Spécifications du GL-XE300](https://www.gl-inet.com/products/gl-xe300/#specs){target="_blank"}

---

## Configuration initiale

Tous les routeurs GL.iNet suivent un processus de configuration similaire. [Cliquez ici pour découvrir la configuration initiale](../../faq/first_time_setup.md/).

---

## Connexion Internet

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** dans le menu de gauche.

Cette page vous permet de choisir votre type de connexion Internet, par exemple Ethernet, Repeater, Tethering et Cellular.

### Ethernet

Connectez votre routeur à un modem actif ou à un équipement réseau actif à l'aide d'un câble Ethernet pour accéder à Internet. Cette méthode offre généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour découvrir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_ethernet.png){class="glboxshadow"}

### Repeater

Configurez votre routeur en mode répéteur pour étendre la couverture Wi‑Fi d'un réseau Wi‑Fi existant. En tant que répéteur, il reçoit et retransmet les signaux sans fil dans sa portée, ce qui étend la couverture. Cette méthode est utile lorsqu'un seul routeur ne peut pas couvrir toute la zone d'utilisation.

[Cliquez ici pour découvrir comment vous connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_repeater.png){class="glboxshadow"}

### Tethering

Connectez le port USB du routeur à un smartphone disposant de données mobiles actives à l'aide d'un câble USB pour accéder à Internet. Cette méthode permet à plusieurs appareils connectés au routeur d'accéder à Internet via les données mobiles du smartphone.

[Cliquez ici pour découvrir comment vous connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_tethering.png){class="glboxshadow"}

### Cellular

Insérez une carte SIM dans l'emplacement pour carte SIM afin de vous connecter à Internet. Cette méthode est utile pour partager l'accès à Internet d'une seule carte SIM avec tous les appareils connectés.

[Cliquez ici pour découvrir comment vous connecter à Internet via le réseau cellulaire ou un modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Ethernet et Repeater) en même temps. Si la connexion Internet prioritaire échoue, le routeur bascule automatiquement vers une autre connexion Internet. Ce mécanisme est également appelé basculement, afin d'assurer un accès Internet fluide et ininterrompu.

Accédez à [Multi-WAN](../../interface_guide/multi-wan.md) pour définir la priorité de chaque connexion Internet.

Vous pouvez également passer le mode Multi-WAN de Failover à Load Balance, ce qui vous permet d'utiliser plusieurs interfaces réseau en même temps afin d'augmenter la bande passante totale du routeur.

---

## Wi‑Fi

Les paramètres sans fil permettent de gérer la sécurité du réseau Wi‑Fi principal et du Wi‑Fi invité. Ils sont accessibles en allant dans **WIRELESS** dans le menu latéral.

[Cliquez ici pour en savoir plus sur la configuration du Wi‑Fi](../../interface_guide/wireless.md)

---

## Clients

Les clients sont les appareils connectés au routeur. Vous pouvez les bloquer ou limiter leur vitesse réseau. Cette interface est accessible en cliquant sur **CLIENTS** dans le menu latéral du panneau d'administration du routeur.

[Cliquez ici pour en savoir plus sur la gestion des appareils clients.](../../interface_guide/clients.md)

---

## VPN

Les routeurs GL.iNet sont préinstallés avec OpenVPN et WireGuard® et prennent en charge plus de 30 services VPN. Ils chiffrent automatiquement tout le trafic réseau au sein du réseau connecté, y compris les appareils invités et les appareils clients qui ne prennent pas en charge eux-mêmes le chiffrement VPN. Nos routeurs peuvent également fonctionner comme serveurs VPN, en redirigeant le trafic des appareils clients situés à distance vers le serveur VPN via un tunnel VPN avant d'accéder à l'Internet public.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Veuillez consulter les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurer le serveur OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Veuillez consulter les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurer le serveur WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## Applications

Les routeurs GL.iNet incluent un large éventail de fonctionnalités complémentaires qui simplifient la gestion des appareils, améliorent l'expérience Internet de l'utilisateur, automatisent la mise à jour du firmware, et bien plus encore.

### Plug-ins

Veuillez consulter le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Veuillez consulter le tutoriel [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Veuillez consulter le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

### Stockage réseau

Veuillez consulter le tutoriel [**Stockage réseau**](../../interface_guide/network_storage.md).

### AdGuard Home

Veuillez consulter le tutoriel [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Contrôle parental

Veuillez consulter le tutoriel [**Contrôle parental**](../../interface_guide/parental_control.md).

### ZeroTier

Veuillez consulter le tutoriel [**ZeroTier**](../../interface_guide/zerotier.md).

---

## Réseau

### Pare-feu

Les routeurs GL.iNet intègrent plusieurs fonctionnalités de pare-feu pour garantir une connexion sécurisée et offrir un contrôle complet aux utilisateurs. Elles permettent de configurer des règles de pare-feu, notamment la redirection de ports, l'ouverture de ports et la DMZ.

[Cliquez ici pour en savoir plus sur le pare-feu des routeurs GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Veuillez consulter le tutoriel [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Veuillez consulter le tutoriel [**LAN**](../../interface_guide/lan.md).

### DNS

Veuillez consulter le tutoriel [**DNS**](../../interface_guide/dns.md).

### Mode réseau

Veuillez consulter le tutoriel [**Mode réseau**](../../interface_guide/network_mode.md).

### IPv6

Veuillez consulter le tutoriel [**IPv6**](../../interface_guide/ipv6.md).

### Adresse MAC

La page **MAC Address** s'appelait auparavant **Mac Clone** et a été renommée **MAC Address** depuis la version v4.2.

Veuillez consulter le tutoriel [**Adresse MAC**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Veuillez consulter le tutoriel [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Veuillez consulter le tutoriel [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## Système

### Aperçu

Veuillez consulter le tutoriel [**Aperçu du système**](../../interface_guide/system_overview.md).

### Mise à niveau

GL.iNet publie régulièrement des mises à jour du firmware de ses routeurs afin d'améliorer les performances, de corriger des bugs et de résoudre des vulnérabilités.

Veuillez consulter le tutoriel [**Mise à niveau**](../../interface_guide/upgrade.md).

### Tâches planifiées

Veuillez consulter le tutoriel [**Tâches planifiées**](../../interface_guide/scheduled_tasks.md).

### Mot de passe administrateur

Cette fonctionnalité a été déplacée vers [**Security**](../../interface_guide/security.md) à partir de la version v4.5.

Veuillez consulter le tutoriel [**Mot de passe administrateur**](../../interface_guide/admin_password.md).

### Fuseau horaire

Veuillez consulter le tutoriel [**Fuseau horaire**](../../interface_guide/time_zone.md).

### Journal

Veuillez consulter le tutoriel [**Journal**](../../interface_guide/log.md).

### Sécurité

Cette fonctionnalité est disponible depuis la version v4.5.

Veuillez consulter le tutoriel [**Sécurité**](../../interface_guide/security.md).

### Réinitialisation du firmware

Veuillez consulter le tutoriel [**Réinitialisation du firmware**](../../interface_guide/reset_firmware.md).

### Paramètres avancés

Veuillez consulter le tutoriel [**Paramètres avancés**](../../interface_guide/advanced_settings.md).
