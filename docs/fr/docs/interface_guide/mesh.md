# Mesh {#mesh}

**Remarque** : cette fonction est disponible à partir du micrologiciel v4.10.

Mango 2 (GL-MG1300) et Mudi 7 (GL-E5800) ne prennent pas en charge Mesh, même avec le firmware v4.10 ou une version ultérieure. Consultez les [modèles pris en charge](#supported-models) pour plus de détails.

---

Dans la partie gauche du panneau d’administration Web, accédez à **MESH**.

Mesh est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi à l’ensemble du domicile et assure une itinérance fluide. Si vous disposez de plusieurs routeurs GL.iNet, configurez-en un comme routeur principal et les autres comme nœuds Mesh afin de bénéficier d’une itinérance Wi-Fi fluide dans toute la maison.

Vous ne savez pas quel mode choisir ? Consultez la [comparaison des modes Mesh, Extender et Access Point](#mesh-vs-extender-vs-access-point-mode).

## Modèles pris en charge {#supported-models}

??? "Modèles pris en charge"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X3000 (Spitz AX)
    - GL-MT3000 (Beryl AX)

    **Remarque** : les modèles marqués d’un ※ prennent en charge Mesh avec un firmware bêta.

??? "Modèles non pris en charge"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Configuration rapide {#quick-setup}

L’exemple suivant utilise Flint 3 (GL‑BE9300) et Slate 7 (GL‑BE3600) pour créer un réseau Mesh.

**Flint 3** est le routeur principal qui se connecte à Internet et gère tous les nœuds Mesh.

**Slate 7** est le nœud Mesh qui étend la couverture Wi-Fi du routeur principal.

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

## Gérer les nœuds {#manage-nodes}

Une fois la configuration terminée, le nœud Mesh n’est plus accessible à son adresse IP d’origine. Vous pouvez gérer le routeur principal et tous les nœuds Mesh depuis le panneau d’administration du routeur principal.

### Afficher les informations d’un nœud {#view-node-details}

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Main Router** dans la topologie.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Vous pouvez consulter les informations du routeur principal, notamment le modèle, les adresses IP et MAC, la durée de fonctionnement et les clients connectés.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Vous pouvez consulter les informations du nœud Mesh, notamment le modèle, les adresses IP et MAC, la version du micrologiciel, la durée de fonctionnement et les clients connectés.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Modifier un nœud Mesh {#edit-mesh-node}

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Par défaut, chaque nœud Mesh est nommé « Node », suivi des quatre derniers caractères de son adresse MAC. Cliquez sur l’icône de modification pour renommer votre nœud Mesh.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Accéder à un nœud Mesh {#access-mesh-node}

Dans le panneau d’administration du routeur principal, accédez à **MESH**, puis cliquez sur **Mesh Node** dans la topologie.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Cliquez sur l’icône en forme d’engrenage dans l’angle supérieur droit, puis sélectionnez **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Vous êtes redirigé vers la page de connexion du nœud Mesh à l’adresse IP attribuée par le routeur principal. Vous pouvez maintenant vous connecter au nœud Mesh.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Ajouter d’autres nœuds {#add-more-nodes}

Cliquez sur **Add** dans l’angle supérieur droit de la topologie pour ajouter d’autres nœuds si nécessaire.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Comparaison des modes Mesh, Extender et Access Point {#mesh-vs-extender-vs-access-point-mode}

Les trois modes permettent d’étendre la couverture Wi-Fi. Les principales différences concernent leur connexion au routeur principal ainsi que la configuration et la gestion des appareils. Le **backhaul** est la liaison entre le routeur principal et un répéteur, un point d’accès ou un nœud Mesh.

Ce tableau compare les modes autonomes Extender et Access Point de GL.iNet à son implémentation Mesh.

| Fonction | Mode Extender | Mode Access Point | Mode Mesh |
|---|---|---|---|
| **Backhaul sans fil** | ✅ Pris en charge | ❌ Sans objet | ✅ Pris en charge |
| **Backhaul Ethernet** | ❌ Non utilisé dans ce mode | ✅ Pris en charge | ✅ Pris en charge |
| **Backhaul en duplex intégral** | ❌ Le Wi-Fi est en semi-duplex | ✅ Ethernet | ✅ Ethernet uniquement ; le backhaul sans fil reste en semi-duplex |
| **Backhaul sans fil 2.4/5 GHz** | ⚠️ Les bandes disponibles dépendent du modèle et du firmware | ❌ Sans objet | ⚠️ Les bandes disponibles dépendent du modèle et du firmware |
| **Backhaul sans fil 6 GHz** | ⚠️ Dépend du modèle et du firmware | ❌ Sans objet | 🔜 À venir |
| **Itinérance Wi-Fi** | ✅ Contrôlée par le client | ✅ Contrôlée par le client | ✅ Contrôlée par le client, avec l’assistance de 802.11k/v |
| **Synchronisation automatique des paramètres Wi-Fi** | ❌ Configuration séparée | ❌ Configuration séparée | ✅ Depuis le routeur principal |
| **Gestion centralisée des nœuds** | ❌ Configuration séparée | ❌ Configuration séparée | ✅ Via le routeur principal |
| **Topologie du réseau et vue d’ensemble des clients** | ❌ Aucune vue d’ensemble du réseau Mesh | ❌ Aucune vue d’ensemble du réseau Mesh | ✅ Disponible sur le routeur principal |
| **Extension gérée de manière centralisée** | ❌ Répéteurs indépendants | ❌ Points d’accès indépendants | ✅ Un routeur principal et jusqu’à huit nœuds |
| **Sauts sans fil gérés de manière centralisée** | ❌ Non gérés par Mesh | ❌ Sans objet | ✅ Jusqu’à trois sauts sans fil |
| **Basculement automatique entre backhaul filaire et sans fil** | ❌ Aucun basculement géré par Mesh | ❌ Aucun basculement géré par Mesh | ✅ Priorité à Ethernet |
| **Usage le plus adapté** | Extension simple de la couverture sans fil | Extension de la couverture lorsqu’Ethernet est disponible | Couverture coordonnée avec des connexions filaires, sans fil ou mixtes |

✅ Pris en charge · ❌ Non pris en charge ou sans objet dans ce mode · ⚠️ Dépend du matériel, du firmware ou de la configuration · 🔜 Fonction prévue

Mesh synchronise les paramètres Wi-Fi pris en charge des réseaux principal, invité, IoT et MLO. Il offre également une gestion centralisée des nœuds, notamment le redémarrage, la suppression et la mise à jour des nœuds GL.iNet pris en charge. Les nœuds peuvent être ajoutés par recherche Wi-Fi, connexion Ethernet ou bouton Mesh/WPS lorsque cette méthode est prise en charge. La gestion du backhaul comprend la priorité à Ethernet, le basculement filaire/sans fil et la prévention des boucles.

### Comprendre les différences de performances {#understanding-performance-differences}

#### Mode Extender {#extender-mode}

L’appareil se connecte à un réseau Wi-Fi existant. La radio utilisée pour cette connexion montante suit le canal du routeur principal. Les clients utilisant la même radio utilisent également ce canal : le trafic montant et celui des clients partagent donc le temps d’antenne.

Sur les modèles multibandes pris en charge, des radios distinctes peuvent continuer à desservir des clients sur d’autres bandes. Par exemple, un répéteur peut se connecter au routeur principal en 2.4 GHz tout en desservant les clients avec sa radio 5 GHz distincte. Ces deux connexions ne se disputent pas le temps d’antenne d’un même canal. Les combinaisons disponibles dépendent du modèle et du firmware ; le mode Extender n’est pas intrinsèquement limité au fonctionnement sur une seule bande.

La même contrainte de canal montant s’applique à la fonction de connexion Repeater de GL.iNet, même si le fonctionnement Repeater et le mode réseau autonome Extender diffèrent sur d’autres points.

#### Mesh sans fil {#wireless-mesh}

Dans la configuration Mesh tribande testée, le nœud utilise **la bande 5 GHz pour le backhaul sans fil**. Le canal 5 GHz du nœud suit celui du routeur principal et ne peut pas être modifié indépendamment, tandis que ses **paramètres de canaux 2.4 GHz et 6 GHz distincts restent configurables séparément**. Il s’agit de paramètres de canaux, et non d’une indication des bandes auxquelles les clients peuvent se connecter. Modifier un canal utilisé par les clients ne change pas la bande de backhaul.

L’effet sur les performances dépend donc du mode de connexion du client :

- **Appareils connectés en 5 GHz :** si un téléphone, un ordinateur portable ou un autre appareil se connecte au Wi-Fi 5 GHz du nœud Mesh alors que la même radio assure le backhaul sans fil, les connexions partagent le temps d’antenne. Le verrouillage du canal 5 GHz du nœud n’empêche pas nécessairement les clients de se connecter à cette bande.
- **Appareils connectés en 2.4 GHz ou 6 GHz :** lorsque ces clients utilisent une radio distincte de celle du backhaul sans fil 5 GHz, les deux liaisons ne subissent pas la pénalité de retransmission sur un même canal.

Cette description concerne la configuration testée, pas tous les modèles Mesh pris en charge. Le transfert par radios distinctes n’est pas propre à Mesh, et passer d’Extender à Mesh n’améliore pas automatiquement le débit.

#### Mode Access Point et Mesh filaire {#access-point-mode-and-wired-mesh}

Tous deux utilisent Ethernet pour la connexion au routeur principal. Le backhaul Ethernet fonctionne en duplex intégral et évite de transmettre son trafic par Wi-Fi. Les connexions Wi-Fi des clients restent en semi-duplex. Avec un matériel et des conditions comparables, le mode Access Point et le Mesh filaire peuvent offrir un débit similaire ; Mesh ajoute une configuration et une gestion coordonnées.

Mesh privilégie le backhaul Ethernet et permet de basculer vers le sans-fil lorsqu’une connexion sans fil appropriée est disponible. Dans la configuration testée, le canal 5 GHz du nœud reste aligné sur celui du routeur principal même lorsque le backhaul Ethernet est actif. Cela ne signifie pas que le backhaul sans fil transporte le trafic. Ethernet supprime le saut sans fil du backhaul de données, mais les nœuds et clients voisins utilisant le même canal Wi-Fi peuvent toujours se disputer le temps d’antenne.

!!! note "Backhaul Mesh 6 GHz — À venir"

    Le backhaul Mesh 6 GHz nécessitera du matériel 6 GHz compatible sur le routeur principal et le nœud Mesh, ainsi qu’un firmware prenant cette fonction en charge. Ne supposez pas que tous les modèles compatibles Mesh la prendront en charge.

    Cela diffère de la connexion d’un client au réseau Wi-Fi 6 GHz existant d’un nœud. Avec un backhaul 6 GHz, une radio 5 GHz distincte pourrait desservir les clients sans partager le temps d’antenne du canal de backhaul. Une radio n’est dédiée au backhaul que si elle est réservée à cet usage et ne dessert pas également des clients.

!!! important "Des radios distinctes ne rendent pas le Wi-Fi duplex intégral"

    Chaque liaison Wi-Fi reste en semi-duplex. Le transfert par radios distinctes évite de partager un canal entre les liaisons de backhaul et des clients, mais ne supprime pas les autres interférences, la contention ni les limites liées aux sauts multiples. Le débit de bout en bout reste limité par la liaison la plus lente et les conditions du réseau.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
