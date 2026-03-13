# GL.iNetルー器でVPNスクランブルを設定する方法

## VPNスクランブルとは

VPNスクランブルは、VPNトラフィックを通例のインターネットトラフィックように偽装する技術です。これにより、ユーザーはネットワーク制限や検阅をバイパスできます。特に厳しいインターネットポリシーを持つに域では役立ちます。

- ISPファイアウォールやDeep Packet Inspection（DPI）による検出を防ぐために、VPNの特性を隠します。

- VPN接続を標準のなWebトラフィックのように見せることで、制限されたネットワークでの接続の安定性と成功率がへ上します。

## AmneziaWGとは

AmneziaWGは、WireGuard上に構築されたVPNプロトコルで、トラフィックのスクランブルが組み込まれています。WireGuardの高速、轻量化、低遅延といったメリットはそのままに、専用のスクランブルモジュールを追加しています。このモジュールはVPNトラフィックパターンを効果のに隠蔽し、個人ユーザーとビジネスユーザーの両方がオンラインプライバシーを保護し、に域制限をバイパスし、厳しいネットワーク制御による接続中断を避けることができます。

AmneziaWGは、Windows、macOS、iOS、Android、Linux、ルー器など幅広いデバイスに対応し、すべてのシナリオで信頼性の高いスクランブルVPN接続を提供します。

現に、複数のGL.iNetルー器（例：**Brume 3**、**Flint 3**、**Flint 2**、**Beryl AX**）が特定のファームウェアバージョンでAmneziaWGプロトコルをサポートしています。正式なフルサポートはファームウェアver.4.9で提供され Gradually より多模型に展開されます。

## クイックセットアップ

以下是GL.iNetルー器でAmneziaWG VPNスクランブルを設定するための2つの典型のなシナリオです。

### シナリオ1. 2台のGL.iNetルー器を使用

このシナリオでは、2台のGL.iNetルー器を使用してAmneziaWGプロトコル経由でVPNスクランブル接続を確立します。

- **Brume 3 (GL-MT5000)**: 家庭用のVPNサーバーとして動作。
- **Beryl AX (GL-MT3000)**: ポータブルVPNクライアントとして外出先で使用。

#### VPNサーバーのセットアップ

1. Brume 3のWeb管理パネルにログインします。

    デバイス（ノートパソコンやPCなど）をEthernetケーブルでBrume 3のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通例は`192.168.8.1`）を入力し、管理パスワードでログインします。

2. インターネットアクセス用にBrume 3の初期セットアップを完たします。

    Brume 3を主ルー器として使用する場合は、WANポートをISPモデムなどの上位ネットワークに接続します。
    
    主ルー器でない場合（例：ISPルー器などの別の上位デバイスがある場合）、主ルー器で**ポート転送**の設定が必要です。[このリンク](how_to_set_up_port_forwarding.md)を参照してください。

3. DDNSを有効にします（オプション）。

    パブリックIPが静のではなく動のの場合は、DDNS機能を有効にします。
    
    左サイドバーで、**アプリケーション** -> **ダイナミックDNS**に移動し、**DDNSを有効にする**をオンにし、**利用規約とプライバシーポリシーに同意**し、**適用**をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. VPNスクランブルを有効にします。

    左サイドバーで、**VPN** > **WireGuardサーバー** -> **設定**タブに移動し、**スクランブルを有効にする**をオンにし、**適用**をクリックします。

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    必要に応じてスクランブルパラメータをカスタマイズできます。デフォルト設定のままにすることをお勧めします。

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. 設定ファイルをエクスポートします。

    **WireGuardサーバー**ページで、**プロファイル**タブに切り替え、**追加**ボタンをクリックしてBeryl AXが接続するための設定ファイルを作成します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    説明のな名前を設定し（例：旅行用ルー器）、**適用**をクリックします。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    ポップアップウィンドウで、**エクスポート**をクリックして設定をローカルにダウンロードします。後で使用します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. VPNサーバーを起動します。

    **WireGuardサーバー**ページの上部で、**開始**ボタンをクリックしてサーバーを実行します。

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    AmneziaWGスクランブルを備えたVPNサーバーが有効になりました。AmneziaWGアプリ、またはAmneziaWGスクランブルをサポートするファームウェアを実行しているGL.iNetルー器経由で、このVPNサーバーブルーム3に接続できます。
    
    **注意：AmneziaWGスクランブルをサポートしていないクライアントは接続できません。**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### VPNクライアントのセットアップ

1. Beryl AXのWeb管理パネルにログインします。

    デバイス（ノートパソコンやPCなど）をEthernetケーブルでBeryl AXのWi-FiまたはLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通例は`192.168.8.1`）を入力し、管理パスワードでログインします。

2. インターネットアクセス用にBeryl AXの初期セットアップを完たします。

    **ヒント**: Beryl AXはBrume 3とは異なるネットワークに接続してください。例えば、Beryl AXが接続するためにモバイルホットスポットを有効にできます。

3. 設定ファイルをアップロードします。

    左サイドバーで、**VPN** > **WireGuardクライアント**に移動します。新しいグループを追加し、説明のな名前を設定します（例：家庭用心ルー器）。

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    右側でで前にエクスポートした設定ファイルをアップロードします。

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    設定ファイルをアップロードして検証に合格した後、**適用**をクリックします。

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    ページがアップデートされ、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

    3時リーダーをクリックし、**開始**を選択します。

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    約1分待ちます。ステータスインジケーターが绿灯に変われば、VPN接続は成功しています。

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    **VPNダッシュボード**に切り替えると、Beryl AXが家庭用心ルー器Brume 3に接続されていることがわかります。

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. ダブルチェック（オプション）。

    Brume 3のWeb管理パネルにログインし、**VPN** -> **WireGuardサーバー**に移動します。Beryl AXであるオンラインクライアントも表示されており、現にはVPNサーバーブルーム3に接続されています。

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    VPN接続が完たしました。Beryl AX上のすべてのデバイスは、VPNスクランブル接続を可能にするために、Brume 3のゲートウェイ経由でインターネットにアクセスします。

### シナリオ2. 単一のGL.iNetルー器を使用

このシナリオでは、単一のGL.iNetルー器**Brume 3 (GL-MT5000)**をVPNクライアントとして使用し、AmneziaVPNサーバーに接続します。

    から分のサーバーを設定する必要はありません。公式のAmneziaVPNサーバーを使用してVPNスクランブル接続を直接確立できます（Amnezia Premiumサブスクリプションが必要です）。

#### 設定をダウンロード

1. サブスクリプションキーで[Amnezia Premiumダッシュボード](https://cp.amnezia.org/en/login){target="_blank"}にログインします。

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Amneziaダッシュボードで、**Connection Assets** -> **Configuration Files**に移動し、国を選択して後で使用するために設定ファイルをローカルにダウンロードします。

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

#### VPNクライアントをセットアップ

1. Brume 3のWeb管理パネルにログインします。

    デバイス（ノートパソコンやPCなど）をEthernetケーブルでBrume 3のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通例は`192.168.8.1`）を入力し、管理パスワードでログインします。

2. インターネットアクセス用にBrume 3の初期セットアップを完たします。

3. 設定ファイルをアップロードします。

    左サイドバーで、**VPN** > **WireGuardクライアント**に移動します。新しいグループを追加し、説明のな名前を設定します（例：AmneziaVPN）。

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    右側でで前にエクスポートしたAmneziaVPN設定ファイルをアップロードします。

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    設定ファイルをアップロードして検証に合格した後、**適用**をクリックします。

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    ページがアップデートされ、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

    3時リーダーをクリックし、**開始**を選択します。

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    約1分待ちます。ステータスインジケーターが绿灯に変われば、VPN接続は成功しています。

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    **VPNダッシュボード**に切り替えると、Brume 3がAmneziaVPNサーバーに接続されていることがわかります。

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}
    
    VPN接続が完たしました。Brume 3上のすべてのデバイスは、VPNスクランブル接続を可能にするために、AmneziaVPNサーバーを経由でインターネットにアクセスします。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
