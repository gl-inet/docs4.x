# Pare-feu

Ce guide s'applique au firmware v4.5 et aux versions antérieures.

Depuis la v4.6, la page Pare-feu a été scindée. Les fonctions **Port Forwarding** et **DMZ** ont été déplacées vers [Port Forwarding](port_forwarding.md). La fonction **Open Ports** a été déplacée vers [Security](security.md).

---

Dans le panneau d'administration web, accédez à **NETWORK** -> **Firewall**.

La page Pare-feu permet de définir des règles telles que **Port Forwarding**, **Open Ports on Router** et **DMZ**.

## Redirection de port

Le **Port Forwarding** permet à des ordinateurs distants de se connecter à un ordinateur local ou à un serveur situé derrière le pare-feu du routeur sur le LAN (par exemple un serveur web ou un serveur FTP).

Pour configurer une redirection de port, cliquez sur l'onglet **Port Forwards**, puis sur **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

Dans la fenêtre contextuelle, ajoutez une nouvelle règle de redirection de port, puis cliquez sur **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Nom de la règle.

**Protocol:** Protocole utilisé ; vous pouvez choisir TCP, UDP ou à la fois TCP et UDP.

**External Zone:** Les options disponibles pour la zone externe sont `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** Numéro du port externe. Vous pouvez saisir ici un numéro de port précis.

**Internal Zone:** Les options disponibles pour la zone interne sont `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** Adresse IP attribuée par le routeur à l'appareil qui doit être accessible à distance.

**Internal Port:** Numéro du port interne de l'appareil. Vous pouvez saisir un numéro de port précis. Laissez ce champ vide s'il est identique au port externe.

**Enable:** Active ou désactive la règle.

## Ouverture de ports sur le routeur

Les services du routeur, comme le web et le FTP, nécessitent que leurs ports respectifs soient ouverts sur le routeur afin d'être accessibles publiquement.

Pour ouvrir un port, passez à l'onglet **Open Ports on Router**, puis cliquez sur **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

Dans la fenêtre contextuelle, ouvrez un nouveau port puis cliquez sur **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** Nom de la règle, librement défini par l'utilisateur.

**Protocol:** Protocole utilisé ; vous pouvez choisir TCP, UDP ou à la fois TCP et UDP.

**Port:** Numéro du port que vous souhaitez ouvrir.

**Enable:** Active ou désactive la règle.

## DMZ

La DMZ permet d'exposer un ordinateur à Internet ; tous les paquets entrants seront alors redirigés vers cet ordinateur.

Activez **Enable DMZ**. Sélectionnez l'adresse IP interne de l'appareil hôte qui doit recevoir tous les paquets entrants.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
