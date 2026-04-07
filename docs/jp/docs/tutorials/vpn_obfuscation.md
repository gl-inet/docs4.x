# GL.iNetルーターでVPN Obfuscationを設定する方法

## VPN Obfuscationとは

VPN Obfuscation は、VPNトラフィックを通常のインターネットトラフィックのように見せかける技術です。これにより、特にインターネット規制が厳しい地域で、ネットワーク制限や検閲を回避しやすくなります。

- ISP、ファイアウォール、Deep Packet Inspection（DPI）に検出されないよう、VPN特有の通信パターンを隠します。

- VPN接続を通常のWebトラフィックのように見せることで、制限のあるネットワークでも接続の安定性と成功率を高めます。

## AmneziaWGとは

AmneziaWG は、WireGuard をベースにしたVPNプロトコルで、トラフィック難読化機能を内蔵しています。高速、軽量、低遅延といった WireGuard 本来の利点を維持しながら、専用の難読化モジュールを追加しています。このモジュールによりVPNトラフィックのパターンを効果的に隠せるため、個人ユーザーにも法人ユーザーにも、オンラインプライバシーの保護、地域制限の回避、厳しいネットワーク制御による接続中断の防止に役立ちます。

AmneziaWG は、Windows、macOS、iOS、Android、Linux、ルーターなど幅広いデバイスに対応しており、さまざまなシーンで信頼性の高い難読化VPN接続を提供します。

現在、**Brume 3**、**Flint 3**、**Flint 2**、**Beryl AX** などの一部の GL.iNet ルーターが、特定のファームウェアバージョンで AmneziaWG プロトコルをサポートしています。正式なフルサポートはファームウェア ver.4.9 で提供され、今後さらに多くのモデルへ順次展開される予定です。

## クイックセットアップ

以下では、GL.iNetルーターで AmneziaWG のVPN Obfuscationを設定する代表的な2つのシナリオを紹介します。

### シナリオ1. 2台のGL.iNetルーターを使用する

このシナリオでは、2台の GL.iNet ルーターを使って、AmneziaWG プロトコル経由の VPN Obfuscation 接続を確立します。

- **Brume 3 (GL-MT5000)**: 自宅用のVPNサーバーとして使用
- **Beryl AX (GL-MT3000)**: 外出先で使うポータブルVPNクライアントとして使用

#### VPNサーバーを設定する

1. Brume 3 のWeb管理パネルにログインします。

    ノートPCやデスクトップPCなどの端末を Ethernet ケーブルで Brume 3 のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は `192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Brume 3 の初期設定を完了し、インターネット接続を有効にします。

    Brume 3 をメインルーターとして使う場合は、WANポートを ISP モデムなどの上位ネットワークに接続します。

    メインルーターではない場合（つまり、ISPルーターなど別の上位機器がメインルーターとして動作している場合）は、メインルーター側で **port forwarding** を設定する必要があります。詳しくは[こちら](how_to_set_up_port_forwarding.md)をご覧ください。

3. DDNS を有効にします（任意）。

    Public IP が固定ではなく動的に変わる場合は、DDNS機能を有効にしてください。

    左側のサイドバーで **APPLICATIONS** -> **Dynamic DNS** に移動し、**Enable DDNS** をオンにします。**Terms of Service & Privacy Policy** に同意してから **Apply** をクリックします。

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. VPN Obfuscation を有効にします。

    左側のサイドバーで **VPN** > **WireGuard Server** -> **Configurations** タブに移動し、**Enable Obfuscation** をオンにして **Apply** をクリックします。

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    必要に応じて難読化パラメーターをカスタマイズできますが、デフォルト設定のまま使用することをおすすめします。

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. 設定ファイルをエクスポートします。

    **WireGuard Server** ページで **Profiles** タブに切り替え、**Add** ボタンをクリックして Beryl AX が接続するための設定ファイルを作成します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    分かりやすい名前（例: Travel Router）を設定し、**Apply** をクリックします。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    ポップアップウィンドウで **Export** をクリックして設定ファイルをローカルにダウンロードします。後で使用します。

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. VPNサーバーを起動します。

    **WireGuard Server** ページ上部の **Start** ボタンをクリックしてサーバーを起動します。

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    これで、AmneziaWG Obfuscation を有効にしたVPNサーバーが動作します。AmneziaWG アプリ、または AmneziaWG Obfuscation に対応したファームウェアを実行している GL.iNet ルーターから、この Brume 3 のVPNサーバーへ接続できます。

    **Note: AmneziaWG Obfuscation に対応していないクライアントは接続できません。**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### VPNクライアントを設定する

1. Beryl AX のWeb管理パネルにログインします。

    ノートPCやデスクトップPCなどの端末を Ethernet ケーブルで Beryl AX のWi-FiまたはLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は `192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Beryl AX の初期設定を完了し、インターネット接続を有効にします。

    **Tips**: Beryl AX は Brume 3 とは別のネットワークに接続してください。たとえば、モバイルホットスポットを有効にして Beryl AX を接続できます。

3. 設定ファイルをアップロードします。

    左側のサイドバーで **VPN** > **WireGuard Client** に移動します。新しいグループを追加し、分かりやすい名前（例: Home Router）を設定します。

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    右側で、先ほどエクスポートした設定ファイルをアップロードします。

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    設定ファイルをアップロードして検証が完了したら、**Apply** をクリックします。

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    ページが更新され、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

    三点アイコンをクリックして **Start** を選択します。

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    約1分待ちます。ステータスインジケーターが緑色になれば、VPN接続は成功です。

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    **VPN Dashboard** に移動すると、Beryl AX が自宅側ルーターの Brume 3 に接続されていることを確認できます。

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. 再確認します（任意）。

    Brume 3 のWeb管理パネルにログインし、**VPN** -> **WireGuard Server** に移動します。オンラインクライアントとして Beryl AX が表示され、この Brume 3 のVPNサーバーに現在接続していることを確認できます。

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    これでVPN接続は完了です。Beryl AX に接続されたすべてのデバイスは、Brume 3 のゲートウェイ経由でインターネットにアクセスし、VPN Obfuscation 接続を利用できます。

### シナリオ2. 1台のGL.iNetルーターを使用する

このシナリオでは、1台の GL.iNet ルーター **Brume 3 (GL-MT5000)** をVPNクライアントとして使い、AmneziaVPN サーバーに接続します。

この場合、自分でサーバーを構築する必要はありません。[Amnezia 公式サイト](https://amnezia.org/){target="_blank"} または AmneziaWG を統合しているVPNサービスプロバイダーから AmneziaWG 設定ファイルをダウンロードし、そのファイルを GL.iNet ルーターにアップロードするだけで、難読化を有効にしたVPN接続を確立できます。

#### 設定ファイルをダウンロードする

<u>Option 1</u>: Amnezia 公式から設定ファイルをダウンロードする（Premium サブスクリプションが必要です）。

1. Subscription Key を使って [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} にログインします。

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Amnezia Dashboard で **Connection Assets** -> **Configuration Files** に移動し、国を選択して、後で使う設定ファイルをローカルにダウンロードします。

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Option 2</u>: AmneziaWG を統合している他のVPNプロバイダーから設定ファイルをダウンロードする。

StarVPN を例に説明します。

1. StarVPN の[料金プラン](https://www.starvpn.com/#pricing){target="_blank"}にアクセスし、用途に合ったVPNプランを選択します。StarVPN アカウントは購入手続き中または[こちら](https://www.starvpn.com/dashboard/register.php){target="_blank"}から直接登録できます。

2. [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"} にログインし、**VPN Configuration** を見つけて **AmneziaWG Config** をクリックし、設定ファイルをダウンロードします。

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. 設定ファイルに IPv6 アドレスが含まれている場合があります。互換性や接続性の問題を避けるため、以下の図のように .conf ファイルを開いて IPv6 アドレスを削除してください。

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    その後、以下の手順に従ってVPNクライアントを設定します。

#### VPNクライアントを設定する

1. Brume 3 のWeb管理パネルにログインします。

    ノートPCやデスクトップPCなどの端末を Ethernet ケーブルで Brume 3 のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は `192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Brume 3 の初期設定を完了し、インターネット接続を有効にします。

3. 設定ファイルをアップロードします。

    左側のサイドバーで **VPN** > **WireGuard Client** に移動します。新しいグループを追加し、分かりやすい名前（例: AmneziaVPN）を設定します。

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    右側で、先ほどダウンロードした AmneziaVPN の設定ファイルをアップロードします。

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    設定ファイルをアップロードして検証が完了したら、**Apply** をクリックします。

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    ページが更新され、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

    三点アイコンをクリックして **Start** を選択します。

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    約1分待ちます。ステータスインジケーターが緑色になれば、VPN接続は成功です。

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    **VPN Dashboard** に移動すると、Brume 3 が AmneziaVPN サーバーに接続されていることを確認できます。

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    これでVPN接続は完了です。Brume 3 に接続されたすべてのデバイスは、AmneziaVPN サーバー経由でインターネットにアクセスし、VPN Obfuscation 接続を利用できます。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
