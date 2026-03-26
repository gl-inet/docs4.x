# Port Forwarding

Cette page est disponible depuis le firmware v4.6. Pour les versions antérieures, veuillez consulter [Firewall](firewall.md).

---

Dans le panneau d'administration web, accédez à **NETWORK** -> **Port Forwarding**.

Cette page vous permet de définir des règles de pare-feu telles que **DMZ** et **Port Forwarding**.

Pour les paramètres **Open Ports on Router**, veuillez aller dans SYSTEM -> Security.

## DMZ

La DMZ permet d'exposer un ordinateur à Internet ; tous les paquets entrants seront alors redirigés vers cet ordinateur.

Activez **Enable DMZ**. Sélectionnez l'adresse IP interne de votre appareil hôte, qui recevra tous les paquets entrants.

Vous pouvez définir la priorité de la DMZ. Si la priorité de la DMZ est supérieure à celle des règles de redirection de port, toutes les règles de redirection de port seront invalidées. Sinon, les requêtes seront transférées vers l'appareil hôte DMZ uniquement si le port consulté ne possède aucune règle de redirection de port correspondante.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding

Le **Port Forwarding** permet aux ordinateurs distants de se connecter à un ordinateur local ou à un serveur situé derrière le pare-feu du routeur sur le LAN (par exemple des serveurs web, des serveurs FTP, etc.).

Pour configurer une redirection de port, cliquez sur **Add** dans la section Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, ajoutez une nouvelle règle de redirection de port, puis cliquez sur **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

**Protocol:** Protocole utilisé ; vous pouvez choisir TCP, UDP, ou à la fois TCP et UDP.

**External Zone:** Les options disponibles pour la zone externe sont `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN`, `Guest`.

**External Port:** Numéro des ports externes. Vous pouvez saisir ici un numéro de port précis. La plage de ports va de 1 à 65535. Vous pouvez définir un seul port ou une plage de ports en reliant le premier et le dernier numéro de port avec le symbole - (par exemple 501-510).

**Internal Zone:** Les options disponibles pour la zone interne sont `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `WAN`.

**Internal IP:** Adresse IP attribuée par le routeur à l'appareil qui doit être accessible à distance. Si vous définissez un seul port dans **External Port**, vous devez définir ici le port unique correspondant. Si vous définissez une plage de ports dans **External Port**, vous devez définir ici la plage de ports correspondante.

**Internal Port:** Numéro du port interne de l'appareil. Vous pouvez saisir un numéro de port précis. Laissez ce champ vide s'il est identique au port externe.

**Description:** Définissez un nom ou ajoutez une description pour la règle de redirection de port (facultatif).

**Enable:** Active ou désactive la règle.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
