# Mesh

**Remarque** : cette fonction est disponible à partir du micrologiciel v4.10.

---

Dans la partie gauche du panneau d’administration Web, accédez à **MESH**.

Mesh est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi à l’ensemble du domicile et assure une itinérance fluide. Si vous disposez de plusieurs routeurs GL.iNet, configurez-en un comme routeur principal et les autres comme nœuds Mesh afin de bénéficier d’une itinérance Wi-Fi fluide dans toute la maison.

L’exemple suivant utilise Flint 3 (GL‑BE9300) et Slate 7 (GL‑BE3600) pour créer un réseau Mesh.

- **Flint 3** est le routeur principal qui se connecte à Internet et gère tous les nœuds Mesh.

- **Slate 7** est le nœud Mesh qui étend la couverture Wi-Fi du routeur principal.

## Configuration rapide

1. Mettez votre nœud Mesh sous tension et placez-le à proximité du routeur principal.

    Lors de la première configuration, gardez le nœud Mesh à côté du routeur principal afin d’accélérer la détection. Une fois la configuration terminée, vous pouvez le déplacer à mi-chemin entre le routeur principal et la zone non couverte par le Wi-Fi afin d’étendre la couverture.

2. Connectez-vous au panneau d’administration Web du nœud Mesh, accédez à **MESH**, puis cliquez sur **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Il devient détectable et ne dispose d’aucune connexion réseau tant qu’il n’a pas été ajouté au réseau Mesh.

3. Connectez-vous au panneau d’administration Web du routeur principal et accédez à **INTERNET**. Connectez-le à Internet à l’aide de n’importe quel type de connexion pris en charge : Ethernet, Repeater, Tethering ou Cellular.

4. Une fois la connexion Internet configurée, accédez à **MESH** et cliquez sur **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. La page présente deux méthodes pour ajouter des nœuds Mesh : Wi-Fi Scan et Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Sélectionnez le tutoriel correspondant ci-dessous pour ajouter vos nœuds Mesh.

    ??? note "Wi-Fi Scan"

        Cliquez sur **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Le routeur commence à rechercher les nœuds Mesh à proximité via Wi-Fi. Sélectionnez les appareils à ajouter, puis cliquez sur **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Le nœud Mesh est alors ajouté à votre réseau Mesh. Cliquez sur **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Reliez le port WAN du nœud Mesh au port LAN du routeur principal à l’aide d’un câble Ethernet. Un réseau Ethernet Backhaul sera alors configuré automatiquement.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Une fois le nœud Mesh ajouté, la topologie apparaît dans le panneau d’administration du routeur principal.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Gérer les nœuds

Une fois la configuration terminée, le nœud Mesh n’est plus accessible à son adresse IP d’origine. Vous pouvez gérer le routeur principal et tous les nœuds Mesh depuis le panneau d’administration du routeur principal.

### Afficher les informations d’un nœud

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Main Router** dans la topologie.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Vous pouvez consulter les informations du routeur principal, notamment le modèle, les adresses IP et MAC, la durée de fonctionnement et les clients connectés.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Vous pouvez consulter les informations du nœud Mesh, notamment le modèle, les adresses IP et MAC, la version du micrologiciel, la durée de fonctionnement et les clients connectés.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Modifier un nœud Mesh

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Par défaut, chaque nœud Mesh est nommé « Node », suivi des quatre derniers caractères de son adresse MAC. Cliquez sur l’icône de modification pour renommer votre nœud Mesh.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Accéder à un nœud Mesh

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Cliquez sur l’icône en forme d’engrenage dans l’angle supérieur droit, puis sélectionnez **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Vous êtes redirigé vers la page de connexion du nœud Mesh à l’adresse IP attribuée par le routeur principal. Vous pouvez maintenant vous connecter au nœud Mesh.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Ajouter d’autres nœuds

Cliquez sur **Add** dans l’angle supérieur droit de la topologie pour ajouter d’autres nœuds si nécessaire.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
