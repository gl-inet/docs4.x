# Guide d'utilisation de Slate Plus (GL-A1300)

## Aperçu du produit

Slate Plus (GL-A1300) est un routeur de voyage de poche doté d'un processeur puissant, optimisé pour la stabilité du réseau et le traitement efficace du chiffrement VPN. Il intègre nos dernières fonctionnalités de sécurité et fonctionne avec la dernière version du système d'exploitation OpenWrt. Il est conçu pour les voyageurs fréquents ayant un usage intensif des réseaux VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Contenu du colis

Veuillez noter que l'adaptateur inclus dans le colis dépend de votre pays de livraison.

Le colis comprend :

- 1 x Manuel d'utilisation
- 1 x Slate Plus (GL-A1300)
- 1 x Câble Ethernet
- 1 x Carte de garantie
- 1 x Adaptateur secteur (type de prise sélectionné)

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Indication LED

[Indication LED](../../faq/led.md#gl-a1300)

## Spécifications

[Spécifications du GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## Configuration initiale

Tous les routeurs GL.iNet ont un processus de configuration simple et presque identique. [Cliquez ici pour découvrir la configuration initiale](../../faq/first_time_setup.md/).

Pour configurer Slate Plus, vous pouvez utiliser l'une des quatre méthodes de connexion Internet prises en charge : Ethernet, Repeater, Tethering et Cellular. Reportez-vous à cette vidéo de configuration.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET

L'interface de configuration de la connexion Internet permet de choisir le type de connexion pris en charge par le routeur.

Configurez la connexion Internet en sélectionnant **INTERNET** dans le panneau d'administration web du routeur.

Quatre méthodes de connexion Internet sont prises en charge, comme indiqué ci-dessous :

### Ethernet

Utilisez un câble Ethernet pour connecter le routeur à un modem actif ou à un périphérique réseau actif. Cette méthode fournit généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour savoir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater

Étendez la couverture Wi‑Fi d'un réseau Wi‑Fi existant en utilisant le routeur pour recevoir les signaux sans fil à portée et les retransmettre plus loin. Cette méthode est particulièrement utile lorsqu'un seul routeur ne couvre pas toute la zone d'utilisation.

[Cliquez ici pour savoir comment vous connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering

Établissez un accès Internet pour les appareils connectés en partageant les données mobiles d'un smartphone avec le routeur via un câble. Cette méthode est particulièrement utile si vous souhaitez utiliser les données du téléphone pour accéder à Internet.

[Cliquez ici pour savoir comment vous connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular

Connectez le routeur à Internet en insérant un modem USB compatible réseau cellulaire dans le port USB du routeur. Cette méthode est particulièrement utile pour partager l'accès Internet d'un modem USB avec tous les appareils connectés.

[Cliquez ici pour savoir comment vous connecter à Internet via un modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Priorité et équilibrage de charge

Accédez à [Multi-WAN](../../interface_guide/multi-wan.md) pour définir la priorité de chaque méthode d'accès Internet ou l'équilibrage de charge lorsque plusieurs méthodes d'accès Internet sont utilisées en même temps.

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

---

## APPLICATIONS

Les routeurs GL.iNet incluent un large éventail de fonctionnalités complémentaires qui simplifient la gestion des appareils, améliorent l'expérience Internet de l'utilisateur, automatisent les mises à jour du firmware, et plus encore.

### Plug-ins

Consultez le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### DNS dynamique

Consultez le tutoriel [**DNS dynamique**](../../interface_guide/ddns.md).

### GoodCloud

Consultez le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

### Stockage réseau

Consultez le tutoriel [**stockage réseau**](../../interface_guide/network_storage.md).

### AdGuard Home

Consultez le tutoriel [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Contrôle parental

Consultez le tutoriel [**contrôle parental**](../../interface_guide/parental_control.md).

### ZeroTier

Consultez le tutoriel [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale

Consultez le tutoriel [**Tailscale**](../../interface_guide/tailscale.md).

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

### Paramètres du bouton bascule

Consultez le tutoriel [**paramètres du bouton bascule**](../../interface_guide/toggle_button_settings.md).

### Journal

Consultez le tutoriel [**journal**](../../interface_guide/log.md).

### Sécurité

Cette fonctionnalité est disponible depuis la version 4.5.

Consultez le tutoriel [**sécurité**](../../interface_guide/security.md).

### Réinitialiser le firmware

Consultez le tutoriel [**réinitialiser le firmware**](../../interface_guide/reset_firmware.md).

### Paramètres avancés

Consultez le tutoriel [**paramètres avancés**](../../interface_guide/advanced_settings.md).

