# Tableau de bord VPN (firmware v4.7 et antérieur)

Connectez-vous au panneau d'administration web et accédez à **VPN** -> **VPN Dashboard**.

La page du tableau de bord VPN affiche les détails de la connexion VPN, tels que l'adresse du serveur, les statistiques de trafic, l'IP virtuelle du client et le journal de connexion. Elle permet également de configurer des paramètres avancés tels que le Kill Switch VPN, la politique VPN, le masquage IP, le MTU et VPN Cascading.

Cette page est divisée en deux sections : [Client VPN](#client-vpn) et [Serveur VPN](#serveur-vpn).

![tableau de bord VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## Client VPN

Lorsque vous ouvrez cette page pour la première fois, si aucun fichier de configuration n'est disponible pour OpenVPN et WireGuard, la page s'affiche comme ci-dessous. Cliquez sur **Set Up Now** pour être redirigé vers la page [OpenVPN Client](openvpn_client.md) ou [WireGuard Client](wireguard_client.md) afin de téléverser votre fichier de configuration VPN.

![configuration du client VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

Une fois le fichier téléversé, votre configuration s'affiche dans la colonne **Configuration File**. Si plusieurs fichiers de configuration sont téléversés, vous pouvez changer de fichier en cliquant sur la zone correspondante.

![fichiers de configuration VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### Options du client

Cliquez sur l'icône d'engrenage à droite pour accéder aux options du client OpenVPN ou WireGuard.

![options du client VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

Les options du client OpenVPN s'affichent comme suit.

![options du client OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

Les options du client WireGuard s'affichent comme suit.

![options du client WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN** : si cette option est activée, l'accès à distance à ce routeur et à ses appareils LAN via le VPN sera autorisé. Le serveur VPN doit annoncer une route vers le sous-réseau LAN de ce routeur.

    Par exemple, comme illustré dans le schéma ci-dessous, le routeur GL.iNet fonctionne comme client VPN et se connecte à un serveur VPN via le tunnel VPN. Lorsque cette option est activée, le routeur GL.iNet et ses appareils côté LAN peuvent être accessibles par les appareils situés du côté du serveur VPN (par ex. un NAS). Cela nécessite l'ajout d'une règle de routage sur le serveur VPN pour atteindre le sous-réseau LAN du routeur GL.iNet.

    ![accès à distance au LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l'adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

- **MTU** : abréviation de Maximum Transmission Unit. Ce paramètre facultatif vous permet de personnaliser le MTU du tunnel VPN, ce qui remplace la valeur définie dans le fichier de configuration.

### Mode proxy

Le mode proxy par défaut pour la connexion VPN est **Global Proxy**. Vous pouvez cliquer sur la zone en haut à droite pour passer à un autre mode proxy.

![mode proxy VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

Trois modes proxy sont disponibles : **Global Proxy**, **Policy Mode** et **Route Mode**.

1. Global Proxy

    Dans ce mode, tout le trafic sera acheminé via le VPN. Une seule instance de client VPN peut être activée.

2. Policy Mode

    Ce mode peut être subdivisé en trois politiques.

    - En fonction du domaine cible ou de l'adresse IP.

        Dans ce mode, seul le trafic de certains sites web identifiés par adresse IP ou nom de domaine sera acheminé via le VPN. Une seule instance de client VPN peut être activée.

    - En fonction de l'appareil client.

        Dans ce mode, seul le trafic de certains appareils du LAN identifiés par leur adresse MAC sera acheminé via le VPN. Une seule instance de client VPN peut être activée.

    - En fonction du VLAN.

        Dans ce mode, seul le trafic de certains VLAN sera acheminé via le VPN. Une seule instance de client VPN peut être activée.

3. Route Mode

    - Auto Detect

        Les règles de routage définies dans chaque fichier de configuration du client VPN ou envoyées par le serveur VPN seront utilisées.

    - Customize Routing Rules

        Vous pouvez configurer manuellement les règles de routage pour chaque instance de client VPN.

### Options globales

Cliquez sur **Global Options** en haut à droite pour configurer les paramètres avancés de votre client VPN.

![options globales du client VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![options globales](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic** : si cette option est activée, tout le trafic Internet est forcé à passer exclusivement par le tunnel VPN et ne peut pas être acheminé via d'autres interfaces, telles que le WAN local du FAI. Si la connexion VPN tombe de manière inattendue, tout le trafic Internet est entièrement bloqué afin d'éviter tout basculement vers le WAN classique. Cela permet d'éviter les fuites VPN causées par une panne VPN, des paramètres DNS clients incorrects ou des problèmes similaires.

    Cette fonctionnalité est également connue sous le nom de [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Elle empêche l'exposition des données utilisateur sur Internet. Un Kill Switch typique coupe automatiquement l'accès à Internet lorsque la connexion VPN échoue. La fonction **Block Non-VPN Traffic** des routeurs GL.iNet offre une protection plus large contre les fuites et couvre les scénarios suivants :

    1. DNS Leak

    2. IPv6 Leak

    3. WebRTC Leak

    4. VPN Connection Drop

    5. Applications Launched Before VPN Establishment

    6. Per-Application Traffic Leaks

- **Allow Access WAN** : si cette option est activée, les appareils clients locaux peuvent toujours accéder aux services côté WAN (par ex. imprimantes, NAS et autres appareils du sous-réseau amont) pendant que le VPN est actif.

    ![autoriser l'accès au WAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Comme illustré dans le schéma ci-dessus, l'activation de cette fonction permet à vos appareils locaux d'atteindre les hôtes du sous-réseau amont, tels que les imprimantes et les NAS.

    Cette option vise principalement à permettre aux clients d'accéder aux appareils du sous-réseau amont. Cependant, le routeur ne peut pas distinguer le trafic du sous-réseau amont du trafic Internet classique. Si les appareils clients accèdent directement à des ressources via des adresses IP publiques, il existe un risque potentiel de fuite de trafic. C'est pourquoi **Allow Access WAN** et **Block Non-VPN Traffic** sont mutuellement exclusifs et ne peuvent pas être activés simultanément.

- **Services From GL.iNet Use VPN** : si cette option est activée, les services GoodCloud, DDNS et rtty transmettront leurs paquets via les tunnels VPN. Cette option est désactivée par défaut, car ces services ont normalement besoin de la véritable adresse IP de l'appareil pour fonctionner correctement.

## Serveur VPN

Si le routeur n'a jamais été configuré comme serveur OpenVPN ou WireGuard, la page s'affichera comme ci-dessous. Cliquez sur **Set Up Now** pour être redirigé vers la page **OpenVPN Server** ou **WireGuard Server** afin d'initialiser votre serveur VPN.

![configuration du serveur VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

Après l'activation du serveur OpenVPN ou WireGuard, la page affichera l'état du serveur comme suit.

![serveur VPN activé](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### Options du serveur

Cliquez sur l'icône d'engrenage à droite pour accéder aux options du serveur OpenVPN ou WireGuard.

![options du serveur VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

Les options du serveur OpenVPN s'affichent comme suit.

![options du serveur OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

Les options du serveur WireGuard s'affichent comme suit.

![options du serveur WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN** : si cette option est activée, les ressources situées dans le sous-réseau LAN du serveur peuvent être accessibles via le tunnel VPN.

* **IP Masquerading** : si cette option est activée, les adresses IP source des clients LAN seront réécrites avec l'adresse IP du tunnel VPN du routeur. Désactivez cette option uniquement pour les configurations site à site où le pair distant connaît vos sous-réseaux LAN.

* **MTU** : abréviation de Maximum Transmission Unit. La valeur MTU que vous définissez pour le tunnel remplacera les paramètres MTU du fichier de configuration.

* **Client to Client** : si cette option est activée, les clients VPN connectés à ce serveur peuvent accéder les uns aux autres via leurs adresses IP de tunnel VPN. Si vous souhaitez également permettre aux clients d'accéder aux sous-réseaux LAN des autres clients, le serveur VPN doit annoncer les routes correspondantes vers ces sous-réseaux LAN distants.

### Règles de routage du serveur

Cliquez sur l'icône de route à droite pour personnaliser les règles de routage OpenVPN ou WireGuard selon vos besoins.

![règles de routage du serveur VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

Les règles de routage du serveur OpenVPN s'affichent comme suit. Cliquez sur **Add Route Rule**, saisissez **Target Address** et **Gateway**, puis cliquez sur l'icône verte de validation pour appliquer.

![règles de routage du serveur OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

Les règles de routage du serveur WireGuard s'affichent comme suit. Cliquez sur **Add Route Rule**, saisissez **Target Address** et **Gateway**, puis cliquez sur l'icône verte de validation pour appliquer.

![règles de routage du serveur WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Remarque** : en mode routes personnalisées, le client VPN ignore le fichier de configuration et la configuration de routage envoyée par le serveur. L'utilisation ou non du tunnel VPN chiffré lors de l'accès à un segment réseau dépend des règles de routage que vous définissez manuellement.

### Options globales

Cliquez sur **Global Options** en haut à droite pour configurer les paramètres avancés de votre serveur VPN.

![options globales du serveur VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![options globales du serveur VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading** : si cette option est activée, lorsque ce routeur agit simultanément comme serveur VPN et client VPN, le trafic des clients VPN distants connectés au serveur VPN de ce routeur sera acheminé via le tunnel VPN amont que ce routeur utilise en tant que client VPN. [En savoir plus sur VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
