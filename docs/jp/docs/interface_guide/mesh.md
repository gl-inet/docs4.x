# Mesh

**注**：この機能はファームウェアv4.10で導入されました。

---

Web管理パネルの左側で**MESH**に移動します。

MeshはWi-Fi EasyMesh™規格に基づく機能で、家全体のWi‑Fiカバレッジを拡張し、シームレスなローミングを可能にします。複数のGL.iNetルーターがある場合、1台をメインルーター、残りをMeshノードに設定します。

次の例では、Flint 3（GL‑BE9300）とSlate 7（GL‑BE3600）でMeshネットワークを構築します。

- **Flint 3**：インターネットに接続し、すべてのMeshノードを管理するメインルーターです。
- **Slate 7**：メインルーターのWi-Fiカバレッジを拡張するMeshノードです。

## クイックセットアップ

1. Meshノードの電源を入れ、メインルーターの近くに置きます。

    初回設定時は、すばやくスキャンできるようにMeshノードをメインルーターの隣に置きます。設定後、Wi-Fiの圏外を補うため、両者の中間付近に移動できます。

2. MeshノードのWeb管理パネルにログインし、**MESH**に移動して**Mesh Node**をクリックします。

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    ノードが検出可能になります。Meshネットワークに追加されるまではネットワーク接続がありません。

3. メインルーターのWeb管理パネルにログインして**INTERNET**に移動し、Ethernet、Repeater、Tethering、Cellularのいずれかでインターネットに接続します。

4. インターネットを設定したら、**MESH**に移動して**Main Router**をクリックします。

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. Meshノードの追加方法として、Wi-Fi ScanとEthernet Backhaulが表示されます。

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    使用する方法を選択します。

    ??? note "Wi-Fi Scan"

        **Start Scanning**をクリックします。

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        近くのMeshノードがWi-Fi経由でスキャンされます。追加するデバイスを選択して**Add**をクリックします。

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        ノードがMeshネットワークに追加されます。**Finish**をクリックします。

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        EthernetケーブルでMeshノードのWANポートをメインルーターのLANポートに接続します。Ethernet Backhaulネットワークが自動的に設定されます。

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. ノードを追加すると、メインルーターの管理パネルにトポロジーが表示されます。

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## ノードの管理

設定後、Meshノードには元のIPアドレスでアクセスできなくなります。メインルーターの管理パネルからメインルーターとすべてのノードを管理できます。

### ノードの詳細を表示する

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Main Router**をクリックします。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

モデル、IP/MACアドレス、稼働時間、接続クライアントなどの詳細を確認できます。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

モデル、IP/MACアドレス、ファームウェアバージョン、稼働時間、接続クライアントを確認できます。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Meshノードを編集する

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

各ノードのデフォルト名は「Node」とMACアドレス末尾4桁の組み合わせです。編集アイコンをクリックして名前を変更できます。

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Meshノードにアクセスする

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

右上の歯車アイコンをクリックして**Open Admin Panel**を選択します。

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

メインルーターから割り当てられたIPアドレスにあるMeshノードのログインページへ移動します。

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### ノードを追加する

必要に応じて、トポロジー右上の**Add**をクリックします。

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
