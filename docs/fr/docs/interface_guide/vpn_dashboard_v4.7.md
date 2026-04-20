# Tableau de bord VPN (firmware v4.7 et antérieur)

Connectez-vous au panneau d'administration web, puis accédez à **VPN** -> **VPN Dashboard**.

La page VPN Dashboard affiche l'état et les paramètres de la connexion VPN. Elle comporte deux sections : [VPN Client](#vpn-client) et [VPN Server](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## VPN Client

Au départ, aucune configuration n'est disponible pour OpenVPN et WireGuard. Cliquez sur **Set Up Now** pour accéder respectivement aux pages [OpenVPN Client](openvpn_client.md) et [WireGuard Client](wireguard_client.md).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Une fois la configuration terminée, vous pouvez sélectionner le fichier de configuration dans la colonne **Configuration file**.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### Options du client VPN

Cliquez sur l'icône d'engrenage d'OpenVPN ou de WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

Options du client OpenVPN.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

Options du client WireGuard.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* Allow Remote Access LAN

    Si cette option est activée, les appareils connectés au routeur sont autorisés à accéder au LAN situé du côté du serveur VPN, ce qui nécessite également les réglages appropriés côté serveur VPN.

    Par exemple, dans l'image ci-dessous, si cette option est activée, cela signifie que *Your Device* peut accéder au *NAS*, mais le *VPN Server* doit toujours vous autoriser à accéder au NAS dans son sous-réseau.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* IP Masquerading

    Si cette option est activée, lorsque les appareils clients du LAN envoient leurs paquets IP, le routeur remplace l'adresse IP source par sa propre adresse, puis les transmet au tunnel VPN.

* MTU

    Signifie **maximum transmission unit**. La valeur MTU définie pour cette instance remplacera l'élément MTU dans le fichier de configuration.

### Mode proxy

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

Comme illustré ci-dessus, le mode proxy actuel est **Global Proxy**. Cliquez dessus pour passer à un autre mode proxy. Trois modes sont disponibles : **Global Proxy**, **Policy Mode** et **Route Mode**.

1. Global Proxy

    Tout le trafic passera par le VPN. Une seule instance de client VPN peut être activée.

2. Policy Mode

    1. En fonction du domaine cible ou de l'adresse IP.

        Dans ce mode, seul le trafic de certains sites web définis par adresse IP ou nom de domaine passe par le VPN. Une seule instance de client VPN peut être activée.

    2. En fonction de l'appareil client.

        Dans ce mode, seul le trafic de certains appareils clients locaux définis par adresse MAC passe par le VPN. Une seule instance de client VPN peut être activée.

    3. En fonction du VLAN.

        Dans ce mode, seul le trafic de certains VLAN peut passer par le VPN. Une seule instance de client VPN peut être activée.

3. Route Mode

    1. Détection automatique

        Les règles de routage définies dans chaque fichier de configuration client VPN ou envoyées par le serveur VPN seront utilisées.

    2. Personnaliser les règles de routage

        Vous pouvez configurer manuellement des règles de routage pour chaque instance de client VPN.

### Options globales du client VPN

Cliquez sur **Global Options** pour afficher une boîte de dialogue d'options globales.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Block Non-VPN Traffic

    Si cette option est activée, tout le trafic des appareils clients qui tente de contourner le tunnel VPN sera bloqué, ce qui empêche efficacement les fuites VPN causées par la configuration DNS des clients, les coupures de connexion VPN, les applications clientes qui accèdent directement par IP, etc.

    Cette fonctionnalité est également connue sous le nom de [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Elle est conçue pour empêcher la fuite de vos données vers Internet. La fonctionnalité Block Non-VPN Traffic des routeurs GL.iNet peut couvrir plusieurs scénarios, notamment les six suivants :

    1. DNS Leak
    2. IPv6 Leak
    3. WebRTC Leak
    4. Dropped VPN Connection
    5. Programs Started Before VPN
    6. Application Specific Leaks

2. Allow Access WAN

    Si cette option est activée, lorsque le VPN est connecté, les appareils clients peuvent toujours accéder au WAN, par exemple à votre imprimante, votre NAS, etc. dans le sous-réseau amont.

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Comme illustré ci-dessus, si cette fonctionnalité est activée, votre appareil pourra accéder aux équipements du sous-réseau amont, comme une imprimante ou un NAS.

    Le but principal est de permettre aux clients d'accéder aux appareils du sous-réseau amont, mais le routeur ne peut pas distinguer le sous-réseau amont d'Internet. Si un appareil client accède directement à une ressource par IP, il peut donc exister un risque de fuite. Cette option est donc mutuellement exclusive avec Block Non-VPN Traffic.

3. Services From GL.iNet Use VPN

    Si cette option est activée, les services du routeur qui nécessitent normalement l'utilisation de l'IP réelle passeront par le VPN, notamment GoodCloud, DDNS et rtty. rtty inclut **Remote SSH** et **Remote Web Access** sur la page [GoodCloud](cloud.md#enable-goodcloud-on-router).

    L'objectif principal est d'utiliser en même temps le client VPN et [GoodCloud](cloud.md) / [DDNS](ddns.md). Il est recommandé de désactiver cette option si vous souhaitez utiliser GoodCloud, sinon sa stabilité dépendra de l'état du VPN. Si vous souhaitez utiliser DDNS, vous devez désactiver cette option, sinon DDNS pointera vers l'adresse IP du serveur VPN.

## VPN Server

Au départ, les deux serveurs VPN ne sont pas encore initialisés. Cliquez sur **Set Up Now** pour accéder respectivement aux pages [OpenVPN Server](openvpn_server.md) et [WireGuard Server](wireguard_server.md).

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

Après le démarrage d'OpenVPN Server et de WireGuard Server :

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### Options du serveur OpenVPN

Cliquez sur l'icône d'engrenage du serveur OpenVPN.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Si cette option est activée, les ressources situées dans le sous-réseau LAN deviennent accessibles via le tunnel VPN.

* **IP Masquerading**

    Si cette option est activée, lorsque les appareils clients du LAN envoient leurs paquets IP, le routeur remplace l'adresse IP source par sa propre adresse, puis les transmet au tunnel VPN.

* **MTU**

    La valeur MTU définie pour cette instance remplacera l'élément MTU dans le fichier de configuration.

### Règles de routage du serveur OpenVPN

Cliquez sur l'icône réseau du serveur OpenVPN.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

En mode de routes personnalisées, le client VPN ignore le fichier de configuration et la configuration de routage envoyée par le serveur. Le fait d'utiliser ou non le tunnel chiffré du VPN pour accéder à un segment réseau donné dépend des règles de routage que vous définissez manuellement.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### Options du serveur WireGuard

Cliquez sur l'icône d'engrenage du serveur WireGuard.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Allow Remote Access LAN**

    Si cette option est activée, les ressources situées dans le sous-réseau LAN deviennent accessibles via le tunnel VPN.

* **IP Masquerading**

    Si cette option est activée, lorsque les appareils clients du LAN envoient leurs paquets IP, le routeur remplace l'adresse IP source par sa propre adresse, puis les transmet au tunnel VPN.

* **MTU**

    La valeur MTU définie pour cette instance remplacera l'élément MTU dans le fichier de configuration.

* **Client to Client**

    Les clients WireGuard peuvent communiquer entre eux. Cela permet aux utilisateurs d'accéder à des équipements du réseau interne à domicile ou au bureau tout en étant à distance. L'accès aux données via le serveur WireGuard est plus sûr que la redirection de ports grâce au chiffrement, et la connexion est généralement plus stable et plus rapide une fois établie.

### Règles de routage du serveur WireGuard

Cliquez sur l'icône réseau du serveur WireGuard.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

En mode de routes personnalisées, le client VPN ignore le fichier de configuration et la configuration de routage envoyée par le serveur. Le fait d'utiliser ou non le tunnel chiffré du VPN pour accéder à un segment réseau donné dépend des règles de routage que vous définissez manuellement.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Options globales du serveur VPN

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **VPN Cascading** : si cette option est activée, lorsque le serveur VPN et le client VPN fonctionnent en même temps sur ce routeur, les clients connectés au serveur VPN seront ensuite acheminés vers le tunnel du client VPN. [En savoir plus sur VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
