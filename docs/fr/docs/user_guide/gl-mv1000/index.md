# Guide d'utilisation du Brume (GL-MV1000) {#brume-gl-mv1000-user-guide}

## Aperçu du produit {#product-overview}

Le Brume (GL-MV1000) et le Brume-W (GL-MV1000W) sont des produits réseau puissants et stables conçus pour les traitements informatiques de pointe. Grâce au chipset hautes performances Marvell, le Brume et le Brume-W* peuvent exécuter une cryptographie de pointe à des vitesses impressionnantes pour offrir une excellente expérience de routage VPN. Préinstallés avec OpenWrt et compatibles avec Ubuntu, le Brume et le Brume-W* permettent des développements approfondis pour les projets IoT commerciaux.

Le Brume-W (GL-MV1000W) est l'édition spéciale du Brume (GL-MV1000) équipée d'un module Wi‑Fi intégré, offrant des performances Wi‑Fi élevées sur la bande 2.4GHz avec une vitesse Wi‑Fi pouvant atteindre 300Mbps.

## Spécifications {#specifications}

[Spécifications du GL-MV1000](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## Configuration initiale {#first-time-setup}

Tous les routeurs GL.iNet suivent un processus de configuration similaire. [Cliquez ici pour en savoir plus sur la configuration initiale](../../faq/first_time_setup.md).

---

## INTERNET {#internet}

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** dans le menu de gauche.

Cette page vous permet de sélectionner votre type de connexion Internet, par exemple Ethernet, Repeater, Tethering ou Cellular, selon votre modèle.

Pour le Brume (GL-MV1000), trois types de connexion sont pris en charge : Ethernet, Tethering et Cellular.

### Ethernet {#ethernet}

Connectez votre routeur à un modem actif ou à un équipement réseau actif via un câble Ethernet pour accéder à Internet. Cette méthode offre généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour découvrir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering {#tethering}

Connectez le port USB du routeur à un smartphone disposant d'une connexion de données mobiles active à l'aide d'un câble USB pour accéder à Internet. Cette méthode permet à plusieurs appareils connectés au routeur d'accéder à Internet via les données mobiles du smartphone.

[Cliquez ici pour découvrir comment vous connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular {#cellular}

Connectez le routeur à Internet en branchant un modem USB compatible réseau cellulaire sur son port USB. Cette méthode est utile pour partager la connexion Internet d'un modem USB avec tous les appareils connectés.

[Cliquez ici pour découvrir comment vous connecter à Internet via un modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN est une fonctionnalité réseau qui vous permet de configurer votre routeur avec plusieurs connexions Internet (par exemple Ethernet et Repeater) en même temps. Si la connexion Internet prioritaire échoue, le routeur bascule automatiquement vers une autre connexion. Ce mécanisme est également appelé basculement et garantit un accès à Internet fluide et ininterrompu.

Accédez à [Multi-WAN](../../interface_guide/multi-wan.md) pour définir la priorité de chaque connexion Internet.

Vous pouvez également faire passer le mode Multi-WAN de Failover à Load Balance, ce qui permet d'utiliser plusieurs interfaces réseau simultanément afin d'augmenter la bande passante totale du routeur.

---

## CLIENTS {#clients}

Les clients sont les appareils connectés au routeur. Vous pouvez bloquer des clients ou limiter leur vitesse réseau. Cette interface est accessible en cliquant sur **CLIENTS** dans le menu latéral du panneau d'administration du routeur.

[Cliquez ici pour en savoir plus sur la gestion des appareils clients.](../../interface_guide/clients.md)

---

## VPN {#vpn}

Les routeurs GL.iNet sont préinstallés avec OpenVPN et WireGuard® et prennent en charge plus de 30 services VPN. Lorsque le client VPN est activé, le routeur peut chiffrer le trafic des appareils du réseau, y compris ceux qui ne peuvent pas exécuter d'applications VPN, selon vos paramètres de politique VPN. Nos routeurs peuvent également agir comme serveurs VPN, en redirigeant le trafic des appareils clients situés à distance vers le serveur VPN via un tunnel VPN avant d'accéder à l'Internet public.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Consultez les liens suivants pour obtenir un guide de configuration pas à pas :

- [**Setup OpenVPN Client**](../../interface_guide/openvpn_client.md)
- [**Setup OpenVPN Server**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Consultez les liens suivants pour obtenir un guide de configuration pas à pas :

- [**Setup WireGuard Client**](../../interface_guide/wireguard_client.md)
- [**Setup WireGuard Server**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

Les routeurs GL.iNet incluent un large éventail de fonctions complémentaires qui simplifient la gestion des appareils, améliorent l'expérience Internet de l'utilisateur, automatisent la mise à jour du firmware, et plus encore.

### Plug-ins {#plug-ins}

Veuillez consulter le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Veuillez consulter le tutoriel [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Veuillez consulter le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage {#network-storage}

Veuillez consulter le tutoriel [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home {#adguard-home}

Veuillez consulter le tutoriel [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control {#parental-control}

Veuillez consulter le tutoriel [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Veuillez consulter le tutoriel [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale {#tailscale}

Veuillez consulter le tutoriel [**Tailscale**](../../interface_guide/tailscale.md).

---

## NETWORK {#network}

### Firewall {#firewall}

Les routeurs GL.iNet intègrent plusieurs fonctions de pare-feu afin de garantir une connexion sécurisée et un contrôle complet par l'utilisateur. Vous pouvez y configurer des règles de pare-feu, notamment Port Forwarding, Open Ports et DMZ.

[Cliquez ici pour en savoir plus sur le pare-feu des routeurs GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Veuillez consulter le tutoriel [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Veuillez consulter le tutoriel [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Veuillez consulter le tutoriel [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Veuillez consulter le tutoriel [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Veuillez consulter le tutoriel [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

La page Mac Address s'appelait auparavant Mac Clone et a été renommée Mac Address depuis la version v4.2.

Veuillez consulter le tutoriel [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Veuillez consulter le tutoriel [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Veuillez consulter le tutoriel [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Veuillez consulter le tutoriel [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet publie régulièrement des mises à jour du firmware de ses routeurs afin d'améliorer les performances, de corriger les bogues et de résoudre les vulnérabilités.

Veuillez consulter le tutoriel [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Veuillez consulter le tutoriel [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Cette fonctionnalité a été déplacée vers [**Security**](../../interface_guide/security.md) depuis la version v4.5.

Veuillez consulter le tutoriel [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Veuillez consulter le tutoriel [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings {#toggle-button-settings}

Veuillez consulter le tutoriel [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log {#log}

Veuillez consulter le tutoriel [**Log**](../../interface_guide/log.md).

### Security {#security}

Cette fonctionnalité est disponible depuis la version v4.5.

Veuillez consulter le tutoriel [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Veuillez consulter le tutoriel [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Veuillez consulter le tutoriel [**Advanced Settings**](../../interface_guide/advanced_settings.md).
