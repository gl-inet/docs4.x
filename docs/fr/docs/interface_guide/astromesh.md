# AstroMesh

> Cette fonction est introduite avec le firmware v4.10.

AstroMesh est la technologie mesh globale propriétaire de GL.iNet basée sur EasyMesh. Contrairement aux systèmes mesh sans fil classiques qui ne fonctionnent que dans un réseau local, AstroMesh supprime les limites géographiques pour vous connecter à votre réseau domestique où que vous soyez.

À la maison, votre routeur de voyage agit comme un Mesh Node classique pour étendre la couverture Wi-Fi avec une itinérance fluide. En déplacement, il peut basculer automatiquement en mode Astro Node et synchroniser les réglages Wi-Fi domestiques via le cloud, afin d’accéder à distance aux appareils du LAN et de faire sortir le trafic par le réseau domestique. Plug-and-play et sans configuration compliquée, AstroMesh offre une expérience Internet fluide, que vous soyez chez vous ou en déplacement.

## Configuration rapide

Dans cet exemple, Flint 3 (GL-BE9300) et Slate 7 (GL-BE3600) sont utilisés pour créer un réseau AstroMesh.

- **Flint 3** : sert de Main Router, se connecte à Internet et gère tous les Mesh Nodes. Il sert également de sortie réseau pour tous les Astro Nodes distants.
- **Slate 7** : fonctionne comme Mesh Node, qui étend localement la couverture Wi-Fi du Main Router ou prolonge le réseau domestique vers des sites distants.

Suivez les étapes ci-dessous pour terminer la configuration.

### Configurer le Main Router

1. Connectez-vous au Web Admin Panel du Flint 3 et allez dans **INTERNET**. Connectez-le à Internet avec l’un des types de connexion pris en charge : Ethernet, Repeater, Tethering ou Cellular.

2. Allez dans **ASTROMESH** et cliquez sur **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

### Configurer le Mesh Node

Connectez-vous au Web Admin Panel du Slate 7. Allez dans **ASTROMESH** et cliquez sur **Mesh/Astro Node**.

![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

### Appairage

Ajoutez des Mesh Nodes à votre réseau AstroMesh via **Wi-Fi Scan** ou **Pairing Code**.

![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

Consultez les instructions correspondantes ci-dessous.

??? note "Wi-Fi Scan"

    Avant le scan, vérifiez que :

    1. Le Mesh Node est allumé et proche du routeur principal.
    2. Le Mesh Node a AstroMesh activé et fonctionne en mode **Mesh Node**.
     ---

    Connectez-vous au Web Admin Panel du Flint 3 et allez dans **ASTROMESH**. Cliquez sur **Add nodes via Wi-Fi Scan**.

    ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, cliquez sur **Scan**.

    ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

    Le routeur recherche les Mesh Nodes à proximité via Wi-Fi.

    ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

    Sélectionnez un nœud et cliquez sur **Add**.

    ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

    Le Mesh Node est ajouté au réseau AstroMesh. Cliquez sur **Finish**.

    ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

    **Remarque** : lorsqu’un nœud rejoint le réseau AstroMesh, il n’est plus accessible via son adresse IP d’origine. Tous les nœuds peuvent être gérés depuis l’Admin Panel du Main Router. Consultez [Gérer les Mesh Nodes](#manage-mesh-nodes) pour plus de détails.

??? note "Pairing Code"

    Connectez-vous au Web Admin Panel du Flint 3 et allez dans **ASTROMESH**. Cliquez sur **Add nodes via Pairing Code**.

    ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

    Le Main Router génère un code d’appairage. Copiez ce code.

    ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

    Connectez-vous au Web Admin Panel du Slate 7 et allez dans **ASTROMESH**. Saisissez le code d’appairage copié et cliquez sur **Apply**.

    ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

    ***Remarque** : le code d’appairage est limité dans le temps. Saisissez-le avant son expiration.*

    Le Mesh Node commence à se connecter au Main Router. Cliquez sur **Done**.

    ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

    **Remarque** : lorsqu’un nœud rejoint le réseau AstroMesh, il n’est plus accessible via son adresse IP d’origine. Tous les nœuds peuvent être gérés depuis l’Admin Panel du Main Router. Consultez [Gérer les Mesh Nodes](#manage-mesh-nodes) pour plus de détails.

Une fois les nœuds ajoutés à AstroMesh, une topologie apparaît dans l’Admin Panel du Main Router, comme ci-dessous.

![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Gérer les Mesh Nodes {#manage-mesh-nodes}

Gérez vos Mesh Nodes depuis l’Admin Panel du Main Router.

### Afficher les informations du nœud

Dans l’Admin Panel du Main Router, allez dans **ASTROMESH** et cliquez sur **Main Router** dans la topologie AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Vous pouvez afficher les détails du Main Router, notamment le modèle, les adresses IP et MAC, la durée de fonctionnement et les clients connectés.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Vous pouvez afficher les détails du Mesh Node, notamment le modèle, les adresses IP et MAC, la version du firmware, la durée de fonctionnement et les clients connectés.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Modifier un Mesh Node

Dans l’Admin Panel du Main Router, allez dans **ASTROMESH** et cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Chaque Mesh Node est nommé par défaut "Node" suivi des quatre derniers chiffres de son adresse MAC. Cliquez sur l’icône de modification pour renommer le Mesh Node.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Accéder au Mesh Node

Dans l’Admin Panel du Main Router, allez dans **ASTROMESH** et cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Cliquez sur l’icône d’engrenage en haut à droite et sélectionnez **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Vous êtes redirigé vers la page de connexion du Mesh Node à l’adresse IP attribuée par le Main Router. Saisissez votre mot de passe administrateur pour vous connecter.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

Après la connexion, allez dans **ASTROMESH** pour afficher l’état de connexion.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Ajouter d’autres nœuds

Pour ajouter d’autres nœuds, cliquez sur **Add** en haut à droite de la topologie AstroMesh.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Gérer les Astro Nodes

Lorsque vous déplacez un Mesh Node hors de votre réseau domestique, il bascule automatiquement en mode **Astro Node**.

Par exemple, emportez le Slate 7 dans un autre lieu. Allumez-le et sélectionnez le mode **Mesh Node** sur l’écran tactile.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

Il détecte l’environnement réseau actuel, bascule automatiquement en mode **Astro Node** et lance la connexion.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Une fois connecté, il affiche son adresse IP d’origine, qui peut être utilisée pour accéder à son Web Admin Panel.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Utilisez cette adresse IP pour vous connecter à votre Astro Node.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

Après la connexion, allez dans **ASTROMESH** pour afficher l’état de connexion. Le mode de connexion par défaut est **Exit Node Mode**. Vous pouvez passer à **Traffic Split Mode** si nécessaire.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode** : dans ce mode, tout le trafic de l’Astro Node est routé via votre réseau domestique pour accéder à Internet. L’adresse IP publique de l’Astro Node correspond à l’adresse IP publique de votre réseau domestique.

- **Traffic Split Mode** : dans ce mode, seul le trafic destiné à votre réseau domestique est renvoyé vers le Main Router, tandis que le reste du trafic Internet passe directement par le WAN local de l’Astro Node. Assurez-vous que l’Astro Node est connecté à un réseau Internet local.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
