# GL.iNetルーターでVPNスクランブルを設定する方法

## VPNスクランブルとは

VPNスクランブルは、VPNトラフィックを通常のインターネットトラフィックのように見せる技術です。これにより、ネットワーク制限や検閲を回避しやすくなり、特にインターネット規制が厳しい地域で役立ちます。

- ISP、ファイアウォール、Deep Packet Inspection（DPI）による検出を避けるため、VPN特有の通信パターンを隠します。

- VPN接続を一般的なWebトラフィックのように見せることで、制限のあるネットワークでも接続の安定性と成功率を高めます。

## AmneziaWGとは

AmneziaWGは、WireGuardをベースにしたVPNプロトコルで、トラフィックのスクランブル機能を内蔵しています。WireGuardの高速性、軽量性、低遅延といった特長を維持しながら、専用のスクランブルモジュールを追加することで、VPNトラフィックのパターンを効果的に隠します。これにより、個人ユーザーにも法人ユーザーにも、オンラインプライバシーの保護、地域制限の回避、厳しいネットワーク制御による接続中断の抑制といった利点があります。

AmneziaWGは、Windows、macOS、iOS、Android、Linux、ルーターなど幅広いデバイスに対応しており、さまざまな利用シーンで信頼性の高いスクランブルVPN接続を提供します。

現在、**Brume 3**、**Flint 3**、**Flint 2**、**Beryl AX** など複数のGL.iNetルーターが、一部のファームウェアでAmneziaWGをサポートしています。正式なフルサポートはファームウェア ver.4.9 で提供され、今後さらに多くのモデルへ順次展開される予定です。

## クイックセットアップ

以下では、GL.iNetルーターでAmneziaWGによるVPNスクランブルを設定する代表的な2つのシナリオを紹介します。

### シナリオ1. 2台のGL.iNetルーターを使用する

このシナリオでは、2台のGL.iNetルーターを使って、AmneziaWGプロトコル経由のVPNスクランブル接続を構築します。

- **Brume 3 (GL-MT5000)**: 自宅側のVPNサーバーとして使用
- **Beryl AX (GL-MT3000)**: 外出先で使うポータブルVPNクライアントとして使用

#### VPNサーバーを設定する

1. Brume 3 のWeb管理パネルにログインします。

   ノートPCやデスクトップPCなどの端末を、EthernetケーブルでBrume 3のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は`192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Brume 3 の初期設定を完了し、インターネットに接続できる状態にします。

   Brume 3 をメインルーターとして使う場合は、WANポートをISPモデムなど上位ネットワークに接続してください。

   メインルーターではない場合、つまりISPルーターなど別の上位機器がメインルーターとして動作している場合は、メインルーター側で**ポート転送**を設定する必要があります。詳しくは[こちら](how_to_set_up_port_forwarding.md)を参照してください。

3. DDNS を有効にします（任意）。

   Public IP が固定ではなく動的に変わる場合は、DDNS機能を有効にしてください。

   左側のサイドバーで **APPLICATIONS** -> **Dynamic DNS** に移動し、**Enable DDNS** をオンにします。**Terms of Service & Privacy Policy** に同意し、**Apply** をクリックします。

   ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. VPNスクランブルを有効にします。

   左側のサイドバーで **VPN** > **WireGuard Server** -> **Configurations** タブに移動し、**Enable Obfuscation** をオンにして **Apply** をクリックします。

   ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

   必要に応じてスクランブルのパラメータを調整できますが、通常はデフォルト設定のまま使用することをおすすめします。

   ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. 設定ファイルをエクスポートします。

   **WireGuard Server** ページで **Profiles** タブに切り替え、**Add** ボタンをクリックして、Beryl AX から接続するための設定ファイルを作成します。

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

   分かりやすい名前を設定し（例: Travel Router）、**Apply** をクリックします。

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

   ポップアップウィンドウで **Export** をクリックし、設定ファイルをローカルにダウンロードします。後で使用します。

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. VPNサーバーを起動します。

   **WireGuard Server** ページ上部の **Start** ボタンをクリックしてサーバーを起動します。

   ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

   これで、AmneziaWGスクランブルを有効にしたVPNサーバーが動作します。AmneziaWGアプリ、またはAmneziaWGスクランブル対応ファームウェアを搭載したGL.iNetルーターから、この Brume 3 のVPNサーバーに接続できます。

   **注意：AmneziaWGスクランブルに対応していないクライアントは接続できません。**

   ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### VPNクライアントを設定する

1. Beryl AX のWeb管理パネルにログインします。

   ノートPCやデスクトップPCなどの端末を、EthernetケーブルでBeryl AXのWi-FiまたはLANに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は`192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Beryl AX の初期設定を完了し、インターネットに接続できる状態にします。

   **ヒント**: Beryl AX は Brume 3 とは別のネットワークに接続してください。たとえば、モバイルホットスポットを有効にしてBeryl AXを接続できます。

3. 設定ファイルをアップロードします。

   左側のサイドバーで **VPN** > **WireGuard Client** に移動します。新しいグループを追加し、分かりやすい名前（例: Home Router）を設定します。

   ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

   右側で、先ほどエクスポートした設定ファイルをアップロードします。

   ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

   設定ファイルをアップロードして検証が完了したら、**Apply** をクリックします。

   ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

   ページが更新され、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

   三点アイコンをクリックし、**Start** を選択します。

   ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

   約1分待ちます。ステータスインジケーターが緑色になれば、VPN接続は成功です。

   ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

   **VPN Dashboard** を開くと、Beryl AX が自宅側ルーター Brume 3 に接続されていることを確認できます。

   ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. 接続を再確認します（任意）。

   Brume 3 のWeb管理パネルにログインし、**VPN** -> **WireGuard Server** に移動します。オンラインクライアントとして Beryl AX が表示され、このVPNサーバーに現在接続していることを確認できます。

   ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

   これでVPN接続は完了です。Beryl AX に接続しているすべての端末は、Brume 3 のゲートウェイ経由でインターネットにアクセスし、VPNスクランブル接続を利用できます。

### シナリオ2. 1台のGL.iNetルーターを使用する

このシナリオでは、1台のGL.iNetルーター **Brume 3 (GL-MT5000)** をVPNクライアントとして使用し、AmneziaVPNサーバーに接続します。

自前のサーバーを構築する必要はありません。公式のAmneziaVPNサーバーを使って、直接VPNスクランブル接続を確立できます。ただし、Amnezia Premium のサブスクリプションが必要です。

#### 設定ファイルをダウンロードする

1. [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="\_blank"} に Subscription Key でログインします。

   ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Amnezia ダッシュボードで **Connection Assets** -> **Configuration Files** に進み、国を選択して、後で使う設定ファイルをローカルにダウンロードします。

   ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

#### VPNクライアントを設定する

1. Brume 3 のWeb管理パネルにログインします。

   ノートPCやデスクトップPCなどの端末を、EthernetケーブルでBrume 3のLANポートに接続します。ブラウザを開き、デフォルトの管理アドレス（通常は`192.168.8.1`）を入力し、管理者パスワードでログインします。

2. Brume 3 の初期設定を完了し、インターネットに接続できる状態にします。

3. 設定ファイルをアップロードします。

   左側のサイドバーで **VPN** > **WireGuard Client** に移動します。新しいグループを追加し、分かりやすい名前（例: AmneziaVPN）を設定します。

   ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

   右側で、先ほどダウンロードした AmneziaVPN の設定ファイルをアップロードします。

   ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

   設定ファイルをアップロードして検証が完了したら、**Apply** をクリックします。

   ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

   ページが更新され、リストに設定ファイルが1つ表示されます。

4. VPN接続を開始します。

   三点アイコンをクリックし、**Start** を選択します。

   ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

   約1分待ちます。ステータスインジケーターが緑色になれば、VPN接続は成功です。

   ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

   **VPN Dashboard** を開くと、Brume 3 が AmneziaVPN サーバーに接続されていることを確認できます。

   ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

   これでVPN接続は完了です。Brume 3 に接続しているすべての端末は、AmneziaVPNサーバー経由でインターネットにアクセスし、VPNスクランブル接続を利用できます。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
