# AstroMesh

> この機能は firmware v4.10 で導入されました。

AstroMesh は、EasyMesh と AstroWarp を組み合わせた GL.iNet 独自のグローバル Mesh 技術です。単一のローカルネットワーク内でしか動作しない一般的な無線 Mesh システムとは異なり、AstroMesh は場所の制限をなくし、どこからでも自宅ネットワークへ接続できるようにします。

自宅では、トラベルルーターが通常の Mesh Node として動作し、シームレスなローミングで家庭内 Wi-Fi のカバー範囲を拡張します。外出時には Astro Node モードへ自動的に切り替わり、クラウド経由で自宅 Wi-Fi 設定を同期します。これにより、自宅 LAN デバイスへリモートアクセスし、トラフィックを自宅ネットワーク出口経由でルーティングできます。複雑な設定なしで plug-and-play に利用できるため、自宅でも外出先でもシームレスなインターネット体験を提供します。

## クイックセットアップ

この例では、Flint 3 (GL-BE9300) と Slate 7 (GL-BE3600) を使用して AstroMesh ネットワークを構築します。

- **Flint 3**: Main Router としてインターネットに接続し、すべての Mesh Nodes を管理します。また、すべてのリモート Astro Nodes のネットワーク出口としても機能します。
- **Slate 7**: Mesh Node として、EasyMesh により Main Router の Wi-Fi カバー範囲をローカルで拡張するか、AstroWarp により自宅ネットワークをリモート拠点へ拡張します。

以下の手順でセットアップを完了します。

1. Flint 3 の Web Admin Panel にログインし、**INTERNET** に移動します。Ethernet、Repeater、Tethering、Cellular のいずれかの対応接続方式でインターネットに接続します。

2. **ASTROMESH** に移動し、**Main Router** をクリックします。

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. **Wi-Fi Scan** または **Pairing Code** でノードを追加します。

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    以下の該当する手順を参照してください。

    ??? note "Wi-Fi Scan"

        スキャン前に、次の点を確認してください。

        1. 追加するルーターの電源が入っており、Main ルーターの近くにあること。
        2. 追加するルーターで AstroMesh が有効で、**Mesh Node** モードで動作していること。
        ---

        **Add nodes via Wi-Fi Scan** をクリックします。

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        ポップアップウィンドウで **Scan** をクリックします。

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Wi-Fi で近くの Mesh Nodes のスキャンを開始します。

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        ノードを選択し、**Add** をクリックします。

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Mesh Node が AstroMesh ネットワークに追加されます。**Finish** をクリックします。

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **注意**: ノードが AstroMesh ネットワークに参加すると、元の IP アドレスではアクセスできなくなります。すべてのノードは Main Router の Admin Panel から管理できます。詳しくは [Mesh Nodes を管理する](#manage-mesh-nodes) を参照してください。

    ??? note "Pairing Code"

        **Add nodes via Pairing Code** をクリックします。

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Main Router がペアリングコードを生成します。このコードをコピーします。

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Slate 7 の Web Admin Panel にログインし、**ASTROMESH** に移動して **Mesh/Astro Node** をクリックします。

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        コピーしたペアリングコードを入力し、**Apply** をクリックします。*ペアリングコードには有効期限があります。期限切れになる前に入力してください。*

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Mesh Node が Main Router への接続を開始します。**Done** をクリックします。

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **注意**: ノードが AstroMesh ネットワークに参加すると、元の IP アドレスではアクセスできなくなります。すべてのノードは Main Router の Admin Panel から管理できます。詳しくは [Mesh Nodes を管理する](#manage-mesh-nodes) を参照してください。

4. ノードが AstroMesh に正常に追加されると、Main Router の Admin Panel に以下のようなトポロジーが表示されます。

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Mesh Nodes を管理する {#manage-mesh-nodes}

Mesh Nodes は Main Router の Admin Panel で管理します。

### ノード情報を表示する

Main Router の Admin Panel で **ASTROMESH** に移動し、AstroMesh トポロジー上の **Main Router** をクリックします。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

モデル、IP アドレス、MAC アドレス、稼働時間、接続クライアントなど、Main Router の詳細を確認できます。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

AstroMesh トポロジー上の **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

モデル、IP アドレス、MAC アドレス、ファームウェアバージョン、稼働時間、接続クライアントなど、Mesh Node の詳細を確認できます。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh Node を編集する

Main Router の Admin Panel で **ASTROMESH** に移動し、AstroMesh トポロジー上の **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

各 Mesh Node はデフォルトで "Node" に MAC アドレス末尾 4 桁を付けた名前になります。名前を変更するには編集アイコンをクリックします。

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Mesh Node にアクセスする

Main Router の Admin Panel で **ASTROMESH** に移動し、AstroMesh トポロジー上の **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

右上の歯車アイコンをクリックし、**Open Admin Panel** を選択します。

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Main Router から割り当てられた IP アドレスの Mesh Node ログインページへリダイレクトされます。管理者パスワードを入力してログインします。

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

ログイン後、**ASTROMESH** に移動して接続状態を確認します。

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### ノードをさらに追加する

ノードをさらに追加するには、AstroMesh トポロジー右上の **Add** をクリックします。

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Astro Nodes を管理する

Mesh Node を自宅ネットワーク外へ移動すると、自動的に **Astro Node** モードへ切り替わります。

たとえば、Slate 7 を別の場所へ持っていきます。電源を入れ、タッチスクリーンで **Mesh Node** Mode を選択します。

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

現在のネットワーク環境を検出し、自動的に **Astro Node** モードへ切り替えて接続を開始します。

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

接続されると元の IP アドレスが表示され、このアドレスで Web Admin Panel にアクセスできます。

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

この IP アドレスを使用して Astro Node にログインします。

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

ログイン後、**ASTROMESH** に移動して接続状態を確認します。デフォルトの接続モードは **Exit Node Mode** です。必要に応じて **Traffic Split Mode** に切り替えることができます。

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: このモードでは、Astro Node からのすべてのトラフィックが自宅ネットワーク経由でインターネットへルーティングされます。Astro Node のパブリック IP は自宅ネットワークのパブリック IP アドレスと一致します。

- **Traffic Split Mode**: このモードでは、自宅ネットワーク宛てのトラフィックのみが Main Router に転送され、その他のインターネットトラフィックは Astro Node のローカル WAN を直接通過します。Astro Node がローカルのインターネットネットワークに接続されていることを確認してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} までご連絡ください。
