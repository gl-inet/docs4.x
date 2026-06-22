# AstroMesh

> この機能は firmware v4.10 で導入されました。

AstroMesh は、EasyMesh と AstroWarp を組み合わせた GL.iNet 独自のグローバル Mesh 技術です。単一のローカルネットワーク内でしか動作しない一般的な無線 Mesh システムとは異なり、AstroMesh は場所の制限をなくし、どこからでも自宅ネットワークへ接続できるようにします。

自宅では、トラベルルーターが通常の Mesh Node として動作し、シームレスなローミングで家庭内 Wi-Fi のカバー範囲を拡張します。外出時には Astro Node モードへ自動的に切り替わり、クラウド経由で自宅 Wi-Fi 設定を同期します。これにより、自宅 LAN デバイスへリモートアクセスし、トラフィックを自宅ネットワーク出口経由でルーティングできます。複雑な設定なしで plug-and-play に利用できるため、自宅でも外出先でもシームレスなインターネット体験を提供します。

## クイックセットアップ

この例では、Flint 3 (GL-BE9300) と Slate 7 (GL-BE3600) を使用して AstroMesh ネットワークを構築します。

- **Flint 3**: Main Node として、インターネットゲートウェイ、Mesh Node 管理、リモート Astro Nodes のネットワーク出口を担当します。
- **Slate 7**: ローカルでは EasyMesh のカバー範囲を拡張し、リモートでは AstroWarp でネットワークを拡張する Mesh Node として機能します。

以下の手順でセットアップを完了します。

1. Flint 3 の Web Admin Panel にログインし、**INTERNET** に移動します。Ethernet、Repeater、Tethering、Cellular のいずれかでインターネットに接続します。
2. **ASTROMESH** に移動し、**Main Node** をクリックします。

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. **Wi-Fi Scan** または **Pairing Code** でノードを追加します。

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    ??? note "Wi-Fi Scan"

        スキャン前に、次の点を確認してください。

        1. 追加するルーターの電源が入っており、Main ルーターの近くにあること。
        2. 追加するルーターで AstroMesh が有効で、**Mesh Node** モードで動作していること。
        ---

        **Add nodes via Wi-Fi Scan** をクリックします。

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        ポップアップウィンドウで **Scan** をクリックします。

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        ルーターが Wi-Fi で近くの Mesh Nodes をスキャンします。

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        ノードを選択し、**Add** をクリックします。

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Mesh Node が AstroMesh に追加されます。**Finish** をクリックします。

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **注意**: 接続後、この Mesh Node には元の IP アドレスではアクセスできなくなります。Main Node から割り当てられた新しい IP アドレスを使用し、すべてのノードは Main Node の Admin Panel で管理してください。詳しくは [こちら](#manage-nodes) を参照してください。

    ??? note "Pairing Code"

        **Add nodes via Pairing Code** をクリックします。

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Main Node が生成したペアリングコードをコピーします。

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Slate 7 の Web Admin Panel にログインし、**AstroMesh** に移動して **Mesh/Astro Node** をクリックします。

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        ペアリングコードを入力し、**Apply** をクリックします。

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Mesh Node が Main Node への接続を開始します。**Done** をクリックします。

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **注意**: 接続後、この Mesh Node には元の IP アドレスではアクセスできなくなります。Main Node から割り当てられた新しい IP アドレスを使用し、すべてのノードは Main Node の Admin Panel で管理してください。詳しくは [こちら](#manage-nodes) を参照してください。

4. ノードが AstroMesh ネットワークに追加されると、Main Node の Admin Panel に以下のようにネットワークトポロジーが表示されます。

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    Mesh Node の Admin Panel にも以下のように接続状態が表示されます。

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **注意**: AstroMesh ネットワークに追加されると、Mesh Node には元の IP アドレスではアクセスできなくなります。再度アクセスするには、Main Node から割り当てられた新しい IP アドレスを使用してください。すべてのノードは Main Node の Admin Panel で管理してください。詳しくは [こちら](#manage-nodes) を参照してください。

5. Mesh Node を自宅の外へ持ち出すと、自動的に Astro Node モードへ切り替わります。

## ノードを管理する {#manage-nodes}

AstroMesh は Main Node の Admin Panel で管理します。

### ノード情報を表示する

AstroMesh トポロジーで **Main Node** をクリックします。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

モデル、IP アドレス、MAC アドレス、稼働時間、接続クライアントなど、Main Node の詳細を確認できます。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

AstroMesh トポロジーで **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

モデル、IP アドレス、MAC アドレス、ファームウェアバージョン、稼働時間、接続クライアントなど、Mesh Node の詳細を確認できます。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh Node を編集する

AstroMesh トポロジーで **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

各 Mesh Node はデフォルトで "Node" に MAC アドレス末尾 4 桁を付けた名前になります。名前を変更するには編集アイコンをクリックします。

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Mesh Node にアクセスする

AstroMesh トポロジーで **Mesh Node** をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

右上の歯車アイコンをクリックし、**Open Admin Panel** を選択します。

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Mesh Node のログインページへリダイレクトされます。Main Node から割り当てられた IP アドレスで Admin Panel にアクセスするには、管理者パスワードを入力します。

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} までご連絡ください。
