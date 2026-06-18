# AstroMesh

> Cette fonction est introduite avec le firmware v4.10.

AstroMesh est la technologie mesh globale propriétaire de GL.iNet, combinant EasyMesh et AstroWarp. Contrairement aux systèmes mesh sans fil classiques qui ne fonctionnent que dans un réseau local, AstroMesh supprime les limites géographiques pour vous connecter à votre réseau domestique où que vous soyez.

À la maison, votre routeur de voyage agit comme un Mesh Node classique pour étendre la couverture Wi-Fi avec une itinérance fluide. En déplacement, il peut basculer automatiquement en mode Astro Node et synchroniser les réglages Wi-Fi domestiques via le cloud, afin d’accéder à distance aux appareils du LAN et de faire sortir le trafic par le réseau domestique. Plug-and-play et sans configuration compliquée, AstroMesh offre une expérience Internet fluide, que vous soyez chez vous ou en déplacement.

## Configuration rapide

Dans cet exemple, Flint 3 (GL-BE9300) et Slate 7 (GL-BE3600) sont utilisés pour créer un réseau AstroMesh.

- **Flint 3** : Main Node, passerelle Internet, gestionnaire des Mesh Nodes et sortie réseau pour les Astro Nodes distants.
- **Slate 7** : Mesh Node pour étendre la couverture locale avec EasyMesh ou prolonger le réseau à distance avec AstroWarp.

Suivez les étapes ci-dessous pour terminer la configuration.

1. Connectez-vous au Web Admin Panel du Flint 3 et allez dans **INTERNET**. Connectez-le à Internet par Ethernet, Repeater, Tethering ou Cellular.
2. Allez dans **ASTROMESH** et cliquez sur **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Ajoutez des nœuds via **Wi-Fi Scan** ou **Pairing Code**.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"

        Avant le scan, vérifiez que :

        1. Le routeur à ajouter est allumé et proche du routeur principal.
        2. Le routeur à ajouter a AstroMesh activé et fonctionne en mode **Mesh Node**.
        ---

        Cliquez sur **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        Dans la fenêtre contextuelle, cliquez sur **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Le routeur recherche les Mesh Nodes à proximité via Wi-Fi.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Sélectionnez un nœud et cliquez sur **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Le Mesh Node est ajouté à AstroMesh. Cliquez sur **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Remarque** : une fois connecté, ce Mesh Node n’est plus accessible via son adresse IP d’origine. Utilisez la nouvelle adresse IP attribuée par le Main Node et gérez tous les nœuds depuis l’Admin Panel du Main Node. Voir [ici](#manage-nodes).

    ??? note "Pairing Code"

        Cliquez sur **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Copiez le code d’appairage généré par le Main Node.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Connectez-vous au Web Admin Panel du Slate 7, allez dans **AstroMesh** et cliquez sur **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Saisissez le code d’appairage et cliquez sur **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Le Mesh Node commence à se connecter au Main Node. Cliquez sur **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Remarque** : une fois connecté, ce Mesh Node n’est plus accessible via son adresse IP d’origine. Utilisez la nouvelle adresse IP attribuée par le Main Node et gérez tous les nœuds depuis l’Admin Panel du Main Node. Voir [ici](#manage-nodes).

4. Une fois le nœud ajouté au réseau AstroMesh, l’Admin Panel du Main Node affiche la topologie réseau, comme illustré ci-dessous.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    L’Admin Panel du Mesh Node affiche également l’état de connexion, comme illustré ci-dessous.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Remarque** : une fois ajouté au réseau AstroMesh, le Mesh Node n’est plus accessible via son adresse IP d’origine. Pour y accéder de nouveau, utilisez la nouvelle adresse IP attribuée par le Main Node. Gérez tous les nœuds depuis l’Admin Panel du Main Node. Voir [ici](#manage-nodes).

5. Lorsque vous emportez le Mesh Node hors de chez vous, il passe automatiquement en mode Astro Node.

## Gérer les nœuds {#manage-nodes}

Gérez AstroMesh depuis l’Admin Panel du Main Node.

### Afficher les informations du nœud

Cliquez sur **Main Node** dans la topologie AstroMesh.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Vous pouvez afficher les détails du Main Node, notamment le modèle, les adresses IP et MAC, la durée de fonctionnement et les clients connectés.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Vous pouvez afficher les détails du Mesh Node, notamment le modèle, les adresses IP et MAC, la version du firmware, la durée de fonctionnement et les clients connectés.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Modifier le Mesh Node

Cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Par défaut, chaque Mesh Node est nommé "Node" suivi des quatre derniers chiffres de son adresse MAC. Cliquez sur l’icône de modification pour le renommer.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Accéder au Mesh Node

Cliquez sur **Mesh Node** dans la topologie AstroMesh.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Cliquez sur l’icône d’engrenage en haut à droite et sélectionnez **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Vous êtes redirigé vers la page de connexion du Mesh Node. Saisissez le mot de passe administrateur pour accéder à son Admin Panel à l’adresse IP attribuée par le Main Node.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
