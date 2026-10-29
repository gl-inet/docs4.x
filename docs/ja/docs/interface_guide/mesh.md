# Mesh {#mesh}

**注**：この機能はファームウェアv4.10で導入されました。

Mango 2（GL-MG1300）とMudi 7（GL-E5800）は、ファームウェアv4.10以降でもMeshに対応していません。 詳しくは[対応モデル](#supported-models)をご覧ください。

---

Web管理パネルの左側で**MESH**に移動します。

MeshはWi-Fi EasyMesh™規格に基づく機能で、家全体のWi‑Fiカバレッジを拡張し、シームレスなローミングを可能にします。複数のGL.iNetルーターがある場合、1台をメインルーター、残りをMeshノードに設定すると、家中でシームレスにWi-Fiローミングできます。

どのモードを選ぶべきか迷っている場合は、[Mesh・Extender・Access Pointモードの比較](#mesh-vs-extender-vs-access-point-mode)をご覧ください。

## 対応モデル {#supported-models}

??? "対応モデル"
    - ※GL-BE14000 (Flint 4)
    - ※GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X3000 (Spitz AX)
    - GL-MT3000 (Beryl AX)

    **注**：※印のモデルは、ベータ版ファームウェアでMeshに対応しています。

??? "非対応モデル"
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

## クイックセットアップ {#quick-setup}

次の例では、Flint 3（GL‑BE9300）とSlate 7（GL‑BE3600）でMeshネットワークを構築します。

**Flint 3**は、インターネットに接続し、すべてのMeshノードを管理するメインルーターです。

**Slate 7**は、メインルーターのWi-Fiカバレッジを拡張するMeshノードです。

1. Meshノードの電源を入れ、メインルーターの近くに置きます。

    初回設定時は、すばやくスキャンできるようにMeshノードをメインルーターの隣に置きます。設定が完了したら、Wi-Fiカバレッジを拡張するため、メインルーターとWi-Fiの届かない場所の中間付近に移動できます。

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

## ノードの管理 {#manage-nodes}

設定後、Meshノードには元のIPアドレスでアクセスできなくなります。メインルーターの管理パネルからメインルーターとすべてのノードを管理できます。

### ノードの詳細を表示する {#view-node-details}

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Main Router**をクリックします。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

モデル、IP/MACアドレス、稼働時間、接続クライアントなどの詳細を確認できます。

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

モデル、IP/MACアドレス、ファームウェアバージョン、稼働時間、接続クライアントを確認できます。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Meshノードを編集する {#edit-mesh-node}

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

各ノードのデフォルト名は「Node」とMACアドレス末尾4桁の組み合わせです。編集アイコンをクリックして名前を変更できます。

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Meshノードにアクセスする {#access-mesh-node}

メインルーターの管理パネルで**MESH**に移動し、トポロジーの**Mesh Node**をクリックします。

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

右上の歯車アイコンをクリックして**Open Admin Panel**を選択します。

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

メインルーターから割り当てられたIPアドレスにあるMeshノードのログインページへ移動します。ここからMeshノードにログインできます。

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### ノードを追加する {#add-more-nodes}

必要に応じて、トポロジー右上の**Add**をクリックします。

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

## Mesh・Extender・Access Pointモードの比較 {#mesh-vs-extender-vs-access-point-mode}

これら3つのモードはいずれもWi-Fiカバレッジを拡張できます。主な違いは、メインルーターへの接続方式と、デバイスの設定・管理方法です。**バックホール**とは、メインルーターと、中継機、アクセスポイント、またはMeshノードとの間の接続を指します。

以下の表では、GL.iNetの独立したネットワークモードであるExtenderとAccess Pointを、Mesh機能と比較します。

| 機能 | Extenderモード | Access Pointモード | Meshモード |
|---|---|---|---|
| **無線バックホール** | ✅ 対応 | ❌ 該当なし | ✅ 対応 |
| **Ethernetバックホール** | ❌ このモードでは使用しない | ✅ 対応 | ✅ 対応 |
| **全二重バックホール** | ❌ Wi-Fiは半二重 | ✅ Ethernet | ✅ Ethernetのみ。無線バックホールは半二重のまま |
| **2.4/5 GHz無線バックホール** | ⚠️ 利用可能な帯域はモデルとファームウェアによる | ❌ 該当なし | ⚠️ 利用可能な帯域はモデルとファームウェアによる |
| **6 GHz無線バックホール** | ⚠️ モデルとファームウェアによる | ❌ 該当なし | 🔜 今後対応予定 |
| **Wi-Fiローミング** | ✅ クライアントが制御 | ✅ クライアントが制御 | ✅ クライアントが制御し、802.11k/vが支援 |
| **Wi-Fi設定の自動同期** | ❌ 個別に設定 | ❌ 個別に設定 | ✅ メインルーターから同期 |
| **ノードの一元管理** | ❌ 個別に設定 | ❌ 個別に設定 | ✅ メインルーター経由で管理 |
| **ネットワークトポロジーとクライアントの一覧** | ❌ Mesh全体の一覧はなし | ❌ Mesh全体の一覧はなし | ✅ メインルーターで確認可能 |
| **一元管理による拡張** | ❌ 独立した中継機 | ❌ 独立したアクセスポイント | ✅ メインルーター1台と最大8台のノード |
| **一元管理される無線ホップ** | ❌ Meshによる管理なし | ❌ 該当なし | ✅ 最大3回の無線ホップ |
| **有線・無線バックホールの自動切り替え** | ❌ Meshによる切り替え管理なし | ❌ Meshによる切り替え管理なし | ✅ Ethernetを優先 |
| **適した用途** | シンプルな無線カバレッジの拡張 | Ethernetを利用できる場所でのカバレッジ拡張 | 有線、無線、または混在する接続での協調的なカバレッジ拡張 |

✅ 対応 · ❌ このモードでは非対応または該当なし · ⚠️ ハードウェア、ファームウェア、設定による · 🔜 対応予定の機能

Meshは、対応するメイン、ゲスト、IoT、MLOのWi-Fi設定を同期します。また、対応するGL.iNetノードの再起動、削除、更新など、ノードの一元管理も提供します。ノードはWi-Fiスキャン、Ethernet接続、または対応モデルのMesh/WPSボタンで追加できます。バックホール管理には、Ethernetの優先、有線・無線の切り替え、ループ防止が含まれます。

### 性能の違いについて {#understanding-performance-differences}

#### Extenderモード {#extender-mode}

デバイスは既存のWi-Fiネットワークに接続します。この上位接続に使用する無線部のチャネルは、メインルーターに従います。同じ無線部を使用するクライアントもそのチャネルを使うため、上位接続とクライアントのトラフィックは通信時間を共有します。

対応するマルチバンドモデルでは、独立した無線部で別の帯域のクライアントに通信を提供することもできます。たとえば、中継機は2.4 GHzで上位ルーターに接続しながら、独立した5 GHz無線部でクライアントに通信を提供できます。この2つの接続は、同じチャネルの通信時間を奪い合いません。利用可能な組み合わせはモデルとファームウェアによって異なり、Extenderモード自体がシングルバンド動作に制限されているわけではありません。

上位接続のチャネルに従うという要件は、GL.iNetのRepeater接続機能にも適用されます。ただし、Repeaterの動作と独立したExtenderネットワークモードには、他の点で違いがあります。

#### 無線Mesh {#wireless-mesh}

検証したトライバンドMesh構成では、ノードは**無線バックホールに5 GHzを使用**します。ノードの5 GHzチャネルはメインルーターに従い、個別には変更できません。一方、独立した**2.4 GHzと6 GHzのチャネル設定は個別に変更できます**。これはチャネル設定に関する説明であり、クライアントが接続できる帯域を示すものではありません。クライアント向けのチャネルを変更しても、バックホールの帯域は変わりません。

そのため、性能への影響はクライアントの接続方式によって異なります。

- **5 GHzで接続するデバイス：** スマートフォン、ノートパソコンなどがMeshノードの5 GHz Wi-Fiに接続し、その同じ無線部で無線バックホールも通信する場合、これらの接続は通信時間を共有します。ノードの5 GHzチャネルが固定されていても、その帯域へのクライアント接続が必ずしも妨げられるわけではありません。
- **2.4 GHzまたは6 GHzで接続するデバイス：** これらのクライアントが5 GHz無線バックホールとは別の無線部を使う場合、2つのリンクに同一チャネルでの転送による性能低下は生じません。

これは検証した構成の説明であり、すべての対応Meshモデルに当てはまるわけではありません。独立した無線部での転送はMeshだけの機能ではなく、ExtenderからMeshに切り替えても、自動的にスループットが向上するわけではありません。

#### Access Pointモードと有線Mesh {#access-point-mode-and-wired-mesh}

どちらもメインルーターへの接続にEthernetを使用します。Ethernetバックホールは全二重で動作し、バックホールのトラフィックをWi-Fiで送信する必要がありません。クライアントのWi-Fi接続は半二重のままです。ハードウェアと条件が同等であれば、Access Pointモードと有線Meshは同程度のスループットを提供できます。Meshには、協調的な設定と管理が加わります。

MeshはEthernetバックホールを優先し、適切な無線接続が利用可能な場合は無線への切り替えに対応します。検証した構成では、Ethernetバックホールが有効な間も、ノードの5 GHzチャネルはメインルーターと一致したままです。これは、無線バックホールがトラフィックを転送しているという意味ではありません。Ethernetによってデータのバックホールで無線ホップが不要になりますが、同じWi-Fiチャネルを使う近くのノードやクライアントは、引き続き通信時間を奪い合う場合があります。

!!! note "6 GHz Meshバックホール — 今後対応予定"

    6 GHz Meshバックホールには、メインルーターとMeshノードの両方に互換性のある6 GHzハードウェアと、対応するファームウェアが必要です。Mesh対応のすべてのモデルでこの機能を利用できるとは限りません。

    これは、ノードの既存の6 GHz Wi-Fiネットワークにクライアントを接続することとは異なります。6 GHzバックホールを使用すれば、独立した5 GHz無線部はバックホールのチャネルの通信時間を共有せずにクライアントに通信を提供できます。無線部がバックホール専用となるのは、その用途に予約され、クライアントへの通信には使われない場合だけです。

!!! important "独立した無線部を使ってもWi-Fiは全二重になりません"

    各Wi-Fiリンクは半二重のままです。独立した無線部で転送することで、バックホールとクライアントのリンクが1つのチャネルを共有せずに済みますが、他の干渉、競合、マルチホップによる制限はなくなりません。エンドツーエンドのスループットは、引き続き遅い方のリンクとネットワークの状態によって制限されます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
