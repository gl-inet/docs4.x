# Guide d'utilisation de Cirrus (GL-AP1300)

## Aperçu du produit

Cirrus (GL-AP1300) est un point d'accès sans fil de plafond, de classe professionnelle, doté d'une solution Wi‑Fi MU-MIMO. L'alimentation PoE et la fonction de temporisation Watchdog intégrée permettent de répondre à la plupart des besoins en environnement d'entreprise. Grâce au système de gestion GoodCloud bien conçu, la gestion de l'appareil est simple et pratique. Vous pouvez activer un accès distant sécurisé où que vous soyez et à tout moment.

![gl-ap1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Spécifications

[Spécifications du GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

---

## Configuration initiale

Tous les routeurs GL.iNet ont un processus de configuration similaire. [Cliquez ici pour découvrir la configuration initiale](../../faq/first_time_setup.md/).

---

## INTERNET

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** dans le menu de gauche.

Cette page vous permet de sélectionner le type de connexion Internet, comme Ethernet, Repeater, Tethering et Cellular, selon votre modèle.

Pour Cirrus (GL-AP1300), deux types de connexion sont pris en charge : Ethernet et Repeater.

### Ethernet

Connectez le routeur à un modem actif ou à un périphérique réseau actif via un câble Ethernet pour accéder à Internet. Cette méthode fournit généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour savoir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

### Repeater

Configurez le routeur en mode répétiteur afin d'étendre la couverture Wi‑Fi d'un réseau Wi‑Fi existant. En tant que répétiteur, il reçoit et retransmet les signaux sans fil dans sa portée, ce qui élargit la couverture. Cette méthode est utile lorsqu'un seul routeur ne peut pas couvrir toute la zone d'utilisation.

[Cliquez ici pour savoir comment vous connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md)

### Multi-WAN

Multi-WAN est une fonctionnalité réseau qui permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Ethernet et Repeater) en même temps. Si la connexion Internet prioritaire échoue, le routeur bascule automatiquement vers une autre connexion Internet. Cela s'appelle aussi le basculement, ce qui garantit un accès Internet fluide et ininterrompu.

Accédez à [Multi-WAN](../../interface_guide/multi-wan.md) pour définir la priorité de chaque connexion Internet.

Vous pouvez également passer le mode Multi-WAN de Failover à Load Balance, ce qui permet d'utiliser plusieurs interfaces réseau en même temps afin d'augmenter la bande passante totale du routeur.

---

## WIRELESS

Les paramètres sans fil permettent de gérer la sécurité réseau du Wi‑Fi principal et du Wi‑Fi invité. Pour y accéder, accédez à **WIRELESS** dans le menu de gauche.

[Cliquez ici pour en savoir plus sur la configuration sans fil](../../interface_guide/wireless.md)

---

## CLIENTS

Les clients sont les appareils connectés au routeur. Vous pouvez les bloquer ou limiter leur vitesse réseau. Cette interface est accessible en cliquant sur **CLIENTS** dans le panneau d'administration web du routeur.

[Cliquez ici pour en savoir plus sur la gestion des appareils clients.](../../interface_guide/clients.md)

---

## VPN

Les routeurs GL.iNet sont préinstallés avec OpenVPN et WireGuard® et prennent en charge plus de 30 services VPN. Ils chiffrent automatiquement tout le trafic réseau du réseau connecté, y compris les appareils invités et les appareils clients qui ne peuvent pas exécuter eux-mêmes un chiffrement VPN. Nos routeurs peuvent également agir comme serveurs VPN, en redirigeant le trafic des appareils clients situés à distance vers le serveur VPN via un tunnel VPN avant d'accéder à l'Internet public.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Consultez les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurer le serveur OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Consultez les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurer le serveur WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

Les routeurs GL.iNet incluent un large éventail de fonctionnalités complémentaires qui simplifient la gestion des appareils, améliorent l'expérience Internet de l'utilisateur, automatisent les mises à jour du firmware, et plus encore.

### Plug-ins

Consultez le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### DNS dynamique

Consultez le tutoriel [**DNS dynamique**](../../interface_guide/ddns.md).

### GoodCloud

Consultez le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home

Consultez le tutoriel [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## NETWORK

### Pare-feu

Les routeurs GL.iNet intègrent plusieurs fonctionnalités de pare-feu pour garantir une connexion sécurisée et un contrôle complet par l'utilisateur. Elles permettent de configurer des règles de pare-feu, notamment la redirection de ports, les ports ouverts et la DMZ.

[Cliquez ici pour en savoir plus sur le pare-feu des routeurs GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Consultez le tutoriel [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Consultez le tutoriel [**LAN**](../../interface_guide/lan.md).

### DNS

Consultez le tutoriel [**DNS**](../../interface_guide/dns.md).

### Mode réseau

Consultez le tutoriel [**mode réseau**](../../interface_guide/network_mode.md).

### IPv6

Consultez le tutoriel [**IPv6**](../../interface_guide/ipv6.md).

### Adresse MAC

La page **Mac Address** s'appelait auparavant **Mac Clone** et a été renommée **Mac Address** depuis la version 4.2.

Consultez le tutoriel [**adresse MAC**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Consultez le tutoriel [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Consultez le tutoriel [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Aperçu

Consultez le tutoriel [**aperçu du système**](../../interface_guide/system_overview.md).

### Mise à niveau

GL.iNet fournit régulièrement des mises à jour du firmware de ses routeurs afin d'améliorer les performances, de corriger les bogues et de résoudre les vulnérabilités.

Consultez le tutoriel [**mise à niveau**](../../interface_guide/upgrade.md).

### Tâches planifiées

Consultez le tutoriel [**tâches planifiées**](../../interface_guide/scheduled_tasks.md).

### Mot de passe administrateur

Cette fonctionnalité a été déplacée vers [**Security**](../../interface_guide/security.md) depuis la version 4.5.

Consultez le tutoriel [**mot de passe administrateur**](../../interface_guide/admin_password.md).

### Fuseau horaire

Consultez le tutoriel [**fuseau horaire**](../../interface_guide/time_zone.md).

### Journal

Consultez le tutoriel [**journal**](../../interface_guide/log.md).

### Sécurité

Cette fonctionnalité est disponible depuis la version 4.5.

Consultez le tutoriel [**sécurité**](../../interface_guide/security.md).

### Réinitialiser le firmware

Consultez le tutoriel [**réinitialiser le firmware**](../../interface_guide/reset_firmware.md).

### Paramètres avancés

Consultez le tutoriel [**paramètres avancés**](../../interface_guide/advanced_settings.md).


