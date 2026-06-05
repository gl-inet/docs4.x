# Port Forwarding

> Ce guide s’applique aux firmwares v4.6 et versions ultérieures. Pour les versions antérieures, veuillez consulter [Firewall](firewall.md).

Sur le panneau d’administration web, sur la gauche, allez dans **NETWORK** -> **Port Forwarding** ou **SECURITY** -> **Port Forwarding** (pour les firmwares v4.9 et versions ultérieures).

Cette page vous permet de configurer des règles de pare-feu, notamment la DMZ et la redirection de port.

Remarque : pour ouvrir les ports du routeur, allez dans SYSTEM -> [Security](security.md) ou SECURITY -> [Admin Access](admin_access.md) (pour les firmwares v4.9 et versions ultérieures).

## DMZ

La DMZ permet d’exposer un ordinateur à Internet ; tous les paquets entrants seront alors redirigés vers cet ordinateur.

Basculez **Enable DMZ**. Sélectionnez l’adresse IP interne de votre appareil hôte, qui recevra tous les paquets entrants.

Vous pouvez définir la priorité de la DMZ. Si la priorité de la DMZ est supérieure à celle des règles de redirection de port, toutes les règles de redirection de port seront invalidées. Sinon, les requêtes seront transférées vers l’appareil hôte DMZ uniquement si le port consulté ne possède aucune règle de redirection de port correspondante.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Port Forwarding

Le **Port Forwarding** permet aux ordinateurs distants de se connecter à un ordinateur local ou à un serveur situé derrière le pare-feu du routeur sur le LAN (par exemple des serveurs web, des serveurs FTP, etc.).

Pour configurer une redirection de port, cliquez sur **Add** dans la section Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, ajoutez une nouvelle règle de redirection de port, puis cliquez sur **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

- **Protocol:** Choisissez `TCP`, `UDP` ou `TCP and UDP` pour cette règle.

- **External Zone:** Les options disponibles pour la zone externe sont `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN` et `Guest`.

- **External Port:** Numéros des ports externes. Vous pouvez saisir ici un numéro de port précis. La plage de ports va de 1 à 65535. Vous pouvez définir un seul port ou une plage de ports en reliant le premier et le dernier numéro de port avec le symbole `-`, par exemple `501-510`.

- **Internal Zone:** Les options disponibles pour la zone interne sont `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server` et `WAN`.

- **Internal IP:** Adresse IP attribuée par le routeur à l’appareil qui doit être accessible à distance. Si vous définissez un seul port dans **External Port**, vous devez définir ici ce même port. Si vous définissez une plage de ports dans **External Port**, vous devez définir ici la plage correspondante.

- **Internal Port:** Numéro du port interne de l’appareil. Vous pouvez saisir un numéro de port précis. Laissez ce champ vide s’il est identique au port externe.

- **Description:** Définissez un nom personnalisé ou ajoutez une description pour cette règle (facultatif).

- **Enable:** Activez ou désactivez cette règle.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
