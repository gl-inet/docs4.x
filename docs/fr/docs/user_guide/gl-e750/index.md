# Guide d'utilisation de Mudi V2 (GL-E750V2)

**Remarque :** Mudi V2 (GL-E750V2) et Mudi (GL-E750) utilisent le même firmware. Si vous utilisez Mudi (GL-E750), [mettez à niveau votre firmware](https://dl.gl-inet.com/?model=e750) pour profiter des dernières fonctionnalités.

## Aperçu du produit

Mudi V2 (GL-E750V2) est un routeur de voyage 4G LTE portable compatible avec les opérateurs du monde entier. Il fonctionne entièrement en open source sur OpenWrt et le SDK 4.0 de GL.iNet, offrant des possibilités de personnalisation et un ensemble complet de fonctionnalités. Mudi V2 (GL-E750V2) prend en charge des débits Wi‑Fi de 300Mbps (2.4GHz) et 433Mbps (5GHz), ainsi qu'une carte MicroSD jusqu'à 1TB. Il intègre une batterie de 7000mAh. Il prend également en charge le multi-WAN (basculement et équilibrage de charge) afin d'assurer une connexion fluide pour tous vos appareils.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Bouton

- Appuyez sur le bouton d'alimentation pendant **3 secondes** : allumez l'appareil.

- Appuyez sur le bouton d'alimentation pendant **3 à 5 secondes** : activez le mode veille.

- Appuyez sur le bouton d'alimentation pendant **plus de 5 secondes** : éteignez l'appareil.

    (Lorsque vous appuyez pendant 3 secondes, l'écran OLED affiche d'abord « Standby Mode On ». CONTINUEZ À APPUYER sur le bouton d'alimentation jusqu'à ce que « Shut Down » apparaisse sous « Standby Mode On ». Un compte à rebours de 3 secondes s'affiche, puis l'appareil s'éteint.)

## Mode veille

En mode veille, Mudi V2 (GL-E750V2) désactive le Wi‑Fi et la 4G pour économiser de l'énergie. Vous ne pouvez pas vous connecter à Mudi V2 (GL-E750V2) dans ce mode.

Pour activer ou désactiver le mode veille, appuyez sur le bouton d'alimentation pendant 3 secondes. L'écran OLED affiche alors « Standby Mode On » ou « Standby Mode Off ».

## Contenu du colis

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Routeur portable 4G LTE Mudi V2 (GL-E750V2)
- 1 x Adaptateur secteur
- 4 x Convertisseurs (prises US, EU, UK et AU)
- 1 x Manuel d'utilisation
- 1 x Carte de garantie
- 1 x Câble Ethernet
- 1 x Réplicateur de ports USB-C
- 1 x Câble USB-C vers USB-C
- 1 x Câble USB-A vers USB-C
- 1 x Pochette
- 1 x Carte de remerciement

---

## Configuration initiale

Regardez cette vidéo ou suivez les étapes ci-dessous pour configurer Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Insérer une carte SIM

Insérez une carte SIM et, si nécessaire, une carte MicroSD dans Mudi V2 (GL-E750V2).

Remarque : si vous utilisez une carte SIM, vous devez l'insérer dans l'appareil avant de l'allumer.

1. Retournez Mudi V2 (GL-E750V2).
2. Insérez votre doigt dans l'encoche située près du bord du couvercle.
3. Faites glisser le long du bord.
4. Lorsque le couvercle se soulève légèrement (d'environ 25 à 30 degrés), tirez-le vers le haut pour l'ouvrir.
5. Insérez la carte dans l'emplacement prévu, en suivant le symbole situé près du coin.
6. Appuyez sur le couvercle pour refermer la plaque arrière.

### 2. Mise sous tension

Appuyez sur le bouton d'alimentation pour allumer l'appareil.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

Lorsque Mudi V2 (GL-E750V2) est éteint, vous pouvez toujours vérifier l'état de la batterie en appuyant sur le bouton d'alimentation. L'écran affiche l'état de la batterie lorsque vous appuyez sur le bouton.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

Assurez-vous d'utiliser un adaptateur secteur standard 5V/2A. Dans le cas contraire, cela peut provoquer un dysfonctionnement.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** dans le menu de gauche.

Cette page vous permet de sélectionner votre type de connexion Internet, par exemple Ethernet, Repeater, Tethering et Cellular.

### Ethernet

Connectez votre routeur à un modem actif ou à un équipement réseau actif via un câble Ethernet pour accéder à Internet. Cette méthode fournit généralement la connexion Internet la plus rapide et la plus fiable.

[Cliquez ici pour découvrir comment vous connecter à Internet via un câble Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Configurez votre routeur en mode répétiteur afin d'étendre la couverture Wi‑Fi d'un réseau Wi‑Fi existant. En tant que répétiteur, il reçoit et retransmet les signaux sans fil dans sa portée, ce qui étend la zone couverte. Cette méthode est utile lorsqu'un seul routeur ne peut pas couvrir toute la zone d'utilisation.

[Cliquez ici pour découvrir comment vous connecter à Internet via un réseau Wi‑Fi existant](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Connectez le port USB du routeur à un smartphone disposant de données mobiles actives à l'aide d'un câble USB pour accéder à Internet. Cette méthode permet à plusieurs appareils connectés au routeur d'accéder à Internet via les données mobiles du smartphone.

[Cliquez ici pour découvrir comment vous connecter à Internet via le partage de connexion USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular
 
Retirez le couvercle arrière de Mudi V2, puis insérez une carte SIM dans l'emplacement prévu pour vous connecter à Internet. Cette méthode est utile pour partager l'accès à Internet d'une seule carte SIM avec tous les appareils connectés.

[Cliquez ici pour découvrir comment vous connecter à Internet via le réseau cellulaire](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

Pour utiliser une carte eSIM physique sur votre routeur GL.iNet, cliquez ici : [Comment utiliser la carte eSIM physique avec les routeurs GL.iNet ?](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## WIRELESS

Les paramètres sans fil permettent de gérer la sécurité du Wi‑Fi principal et du Wi‑Fi invité. Pour y accéder, accédez à **WIRELESS** dans le menu latéral.

[Cliquez ici pour en savoir plus sur la configuration sans fil](../../interface_guide/wireless.md)

---

## CLIENTS

Les clients sont les appareils connectés au routeur. Vous pouvez les bloquer ou limiter leur vitesse réseau. Cette interface est accessible en cliquant sur **CLIENTS** dans le menu latéral du panneau d'administration web du routeur.

[Cliquez ici pour en savoir plus sur la gestion des appareils clients.](../../interface_guide/clients.md)

---

## VPN

Les routeurs GL.iNet sont préinstallés avec OpenVPN et WireGuard® et prennent en charge plus de 30 services VPN. Ils chiffrent automatiquement tout le trafic réseau au sein du réseau connecté, y compris les appareils invités et les appareils clients qui ne peuvent pas exécuter eux-mêmes un chiffrement VPN. Nos routeurs peuvent également agir comme serveurs VPN, en redirigeant le trafic des appareils clients situés à distance vers le serveur VPN via un tunnel VPN avant d'accéder à l'Internet public.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Veuillez consulter les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurer le serveur OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Veuillez consulter les liens suivants pour un guide de configuration étape par étape :

- [**Configurer le client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurer le serveur WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

Les routeurs GL.iNet incluent un large éventail de fonctionnalités complémentaires qui simplifient la gestion des appareils, améliorent l'expérience Internet de l'utilisateur, automatisent les mises à jour du firmware, et bien plus encore.

### Plug-ins

Veuillez consulter le tutoriel [**Plug-ins**](../../interface_guide/plugins.md).

### DNS dynamique

Veuillez consulter le tutoriel [**DNS dynamique**](../../interface_guide/ddns.md).

### GoodCloud

Veuillez consulter le tutoriel [**GoodCloud**](../../interface_guide/cloud.md).

---

## NETWORK

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

La page **Mac Address** s'appelait auparavant **Mac Clone** et a été renommée **Mac Address** depuis la version v4.2.

Veuillez consulter le tutoriel [**Adresse MAC**](../../interface_guide/mac_address.md).

### IGMP Snooping

Veuillez consulter le tutoriel [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Aperçu

Veuillez consulter le tutoriel [**Aperçu du système**](../../interface_guide/system_overview.md).

### Mise à niveau

GL.iNet publie régulièrement des mises à jour du firmware de ses routeurs afin d'améliorer les performances, de corriger les bugs et de résoudre les vulnérabilités.

Veuillez consulter le tutoriel [**Mise à niveau**](../../interface_guide/upgrade.md).

### Paramètres de l'écran OLED

Sur cette page, vous pouvez ajuster les informations affichées sur l'écran OLED de votre Mudi V2 (GL-E750V2).


### Tâches planifiées

Veuillez consulter le tutoriel [**Tâches planifiées**](../../interface_guide/scheduled_tasks.md).

### Mot de passe administrateur

Cette fonctionnalité a été déplacée vers [**Security**](../../interface_guide/security.md) depuis la version v4.5.

Veuillez consulter le tutoriel [**Mot de passe administrateur**](../../interface_guide/admin_password.md).

### Fuseau horaire

Veuillez consulter le tutoriel [**Fuseau horaire**](../../interface_guide/time_zone.md).

### Paramètres du bouton bascule

Veuillez consulter le tutoriel [**Paramètres du bouton bascule**](../../interface_guide/toggle_button_settings.md).

### Journal

Veuillez consulter le tutoriel [**Journal**](../../interface_guide/log.md).

### Réinitialiser le firmware

Veuillez consulter le tutoriel [**Réinitialiser le firmware**](../../interface_guide/reset_firmware.md).

### Paramètres avancés

Veuillez consulter le tutoriel [**Paramètres avancés**](../../interface_guide/advanced_settings.md).

