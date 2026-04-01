# Utiliser WireGuard pour sécuriser RDP depuis un réseau externe

Vous pouvez avoir besoin d'accéder à distance à votre PC depuis un réseau externe, ou inversement. La méthode la plus sécurisée consiste à y accéder via votre propre tunnel WireGuard. Cela offre davantage de sécurité que l'utilisation de la redirection de port et de l'accès via votre adresse IP publique. Une fois le tunnel configuré, vous pouvez utiliser l'application **Remote Desktop** de Windows pour accéder à votre PC depuis n'importe où.

## Topologie

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Configurer votre propre réseau WireGuard

Vous devez configurer votre propre serveur WireGuard et votre client WireGuard avant de pouvoir utiliser le tunnel WireGuard pour RDP. Vous pouvez configurer le tunnel avec deux routeurs GL.iNet. [Créer votre propre serveur WireGuard domestique avec deux routeurs GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Autoriser votre serveur à accéder au côté LAN du client

Si vous souhaitez un accès mutuel depuis le serveur et le client, vous devez d'abord autoriser votre serveur à accéder au côté LAN du client. [Accéder au LAN du client depuis le serveur](wireguard_server_access_to_client_lan_side.md).

## Autoriser votre client à accéder au côté LAN du serveur

Activez ensuite **Allow Remote LAN Access** sur les tableaux de bord VPN du serveur et du client. Pour plus de détails, côté client cliquez [ici](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options) ; côté serveur cliquez [ici](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Configurer le PC côté serveur pour le rendre accessible

### PC côté serveur

Si vous souhaitez accéder au PC connecté au côté LAN de votre serveur avec l'IP **192.168.29.123**, accédez aux paramètres Windows de ce PC et cliquez sur **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Activez-le.

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Cliquez sur **Confirm**.

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Démarrer l'application Remote Desktop sur l'ordinateur portable client

### Ordinateur portable côté client

Recherchez l'application **Remote Desktop Connection**.

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Lancez-la et saisissez l'IP du PC côté serveur **192.168.29.123** dans le champ.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Saisissez les identifiants du PC côté serveur.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Vous contrôlez alors immédiatement à distance votre PC côté serveur.

Si vous souhaitez effectuer l'opération inverse, inversez simplement les étapes entre le PC serveur et l'ordinateur portable client.
