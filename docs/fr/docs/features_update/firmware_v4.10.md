# Firmware v4.10

Cette version introduit Mesh, le compte GL.iNet et la prise en charge native des VLAN. Elle améliore également la gestion des comptes GoodCloud et propose une interface plus conviviale.

Téléchargez le dernier firmware depuis le [Centre de téléchargement des firmwares](https://dl.gl-inet.com/){target="_blank"}.

## Mesh

[Mesh](../interface_guide/mesh.md) est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi dans toute la maison et permet une itinérance transparente. Si vous possédez plusieurs routeurs GL.iNet, définissez-en un comme routeur principal et les autres comme nœuds mesh afin de vous déplacer dans votre domicile sans interruption de la connexion Wi-Fi.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/mesh.png){class="glboxshadow"}

## Services cloud

Les services cloud regroupent des fonctionnalités cloud intégrées au routeur et gérées de manière centralisée à l'aide de votre compte GL.iNet. Ils permettent de surveiller l'état en temps réel, de gérer les appareils à distance, de déployer les firmwares par lots et de bénéficier d'un accès distant sécurisé. Dans le firmware v4.10, ce module offre une gestion unifiée du cloud améliorée.

Le module comprend GL.iNet Account, GoodCloud et GoodPAS.

### GL.iNet Account

Le [compte GL.iNet](../interface_guide/glinet_account.md) fournit une page de profil centralisée à partir de laquelle vous pouvez connecter ou gérer vos appareils et accéder aux services cloud. Un seul compte GL.iNet vous permet d'accéder simplement à GoodCloud, GoodPAS et à l'application GL.iNet afin de gérer votre réseau plus facilement.

![gl.inet account](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/account.png){class="glboxshadow"}

### GoodCloud

[GoodCloud](../interface_guide/cloud.md) est une plateforme cloud permettant de déployer et de gérer à distance les routeurs GL.iNet. Elle centralise les appareils répartis sur plusieurs sites et prend en charge la configuration et la mise à niveau du firmware par lots. Elle permet également d'accéder à distance au panneau d'administration Web et au terminal de l'appareil via SSH.

Dans le firmware v4.10, GoodCloud simplifie l'association du compte et permet d'effacer les données du compte cloud lors d'une réinitialisation d'usine.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodcloud.png){class="glboxshadow"}

### GoodPAS

[GoodPAS](../interface_guide/goodpas.md) est une solution avancée d'accès à distance intégrée au SDK des routeurs GL.iNet. Basée sur le protocole AmneziaWG, elle permet d'accéder en toute sécurité à un réseau domestique par un simple appairage des appareils, sans inscription de compte ni connexion utilisateur.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/goodpas.png){class="glboxshadow"}

## Sous-réseau

La page [Sous-réseau](../interface_guide/subnet.md) regroupe la configuration du LAN, du réseau invité, du réseau IoT et des réseaux VLAN personnalisés dans une vue unique. Elle fournit une interface centralisée pour tous les paramètres liés aux sous-réseaux et permet de créer et gérer plusieurs sous-réseaux afin d'isoler différents types d'appareils ou de trafic.

La figure suivante présente la page Subnet du Flint 3 (GL-BE9300).

![subnet](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/subnet.png){class="glboxshadow"}

## Port Ethernet

La page [Port Ethernet](../interface_guide/ethernet_port_v4.10.md) affiche toutes les interfaces Ethernet du routeur. Elle permet de vérifier l'état de la connexion, d'attribuer aux ports le rôle WAN ou LAN et d'afficher des informations telles que l'adresse MAC, la vitesse négociée et l'état de la liaison. Les interfaces physiques peuvent également être affectées aux sous-réseaux que vous avez créés.

La figure suivante présente la page Ethernet Port du Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.10/ehternet_port.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
