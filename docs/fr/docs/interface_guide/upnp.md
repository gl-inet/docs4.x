# UPnP {#upnp}

**Remarque** : Cette fonctionnalité a été introduite dans le firmware v4.11.

---

Dans le menu de gauche du panneau d’administration web, accédez à **SECURITY** -> **UPnP**.

UPnP (Universal Plug and Play) permet aux appareils LAN et aux applications compatibles de demander automatiquement des mappages de ports sur les routeurs GL.iNet. Ces mappages redirigent le trafic WAN entrant vers des adresses IP et des ports LAN spécifiques, permettant aux clients externes de se connecter aux services locaux sans règles de redirection de port configurées manuellement.

UPnP diffère de la [redirection de port](./port_forwarding.md) et de la [DMZ](./port_forwarding.md#dmz) : UPnP crée automatiquement des mappages à la demande des appareils. La redirection de port expose certains ports, tandis que la DMZ expose tous les ports d’un hôte LAN ; toutes deux nécessitent une configuration manuelle. Avant d’activer l’une de ces fonctionnalités, assurez-vous de comprendre son fonctionnement et les risques de sécurité associés.

**Remarque** : 

1. Lorsque UPnP est activé, les appareils LAN et les applications compatibles peuvent demander des mappages de ports sans approbation de chaque demande.

2. Un appareil compromis ou une application malveillante peut utiliser UPnP pour exposer des services locaux sur Internet. Activez UPnP uniquement sur des réseaux de confiance et désactivez-le lorsqu’il n’est pas nécessaire.

3. UPnP nécessite une IP publique sur l’interface WAN du routeur pour accepter les connexions entrantes depuis Internet. Il ne fonctionnera pas si votre fournisseur d’accès utilise CGNAT.

Les utilisations courantes d’UPnP comprennent :

- **Jeux en ligne** : les jeux et consoles compatibles (par exemple, les jeux multijoueurs Steam, Xbox Series X|S, PlayStation 5, Nintendo Switch) peuvent créer automatiquement des mappages de ports pour faciliter les connexions avec d’autres joueurs.

- **Partage de fichiers entre pairs** : les clients BitTorrent et les autres applications P2P compatibles peuvent mapper automatiquement les ports d’écoute pour accepter les connexions entrantes des pairs.

- **Accès à distance** : les appareils et applications prenant en charge le mappage de ports UPnP, tels que certains NAS, caméras IP et serveurs multimédias, peuvent configurer automatiquement des mappages pour un accès depuis l’extérieur du réseau local.

## Configuration rapide {#quick-setup}

Activez le commutateur pour activer UPnP. Les appareils et applications compatibles peuvent alors demander des mappages de ports selon leurs besoins, comme dans l’exemple ci-dessous.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- **Client / Application** : description du client ou de l’application et adresse IP LAN de l’appareil demandeur.

- **Protocol** : protocole de transport du mappage, par exemple `TCP` ou `UDP`.

- **External Port** : port WAN pour les connexions entrantes.

- **Internal Target** : adresse IP LAN et port cibles.

- **Lease** : temps restant avant l’expiration du mappage. La durée du bail par défaut est de 7 jours.

- **Action** : cliquez sur l’icône de corbeille pour supprimer le mappage. Le client ou l’application peut le demander à nouveau s’il est toujours en cours d’exécution.

Les mappages de ports actifs sont supprimés lorsque le client les libère ou que leurs baux expirent. Cliquez sur **Refresh** pour afficher les derniers mappages de ports.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
