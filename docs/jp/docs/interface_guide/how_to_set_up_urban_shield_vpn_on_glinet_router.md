# GL.iNetルーターでUrban Shield VPNを設定する方法

[Urban Shield VPN](https://urbanshieldvpn.com/)は、世界中のユーザーにセキュリティが高く高パフォーマンスなVPNソリューションを提供するVPNプロバイダーです。GL.iNet VPNルーターの事前設定されたモデルと柔軟なサブスクリプションプランを提供し、安全でプライベートなブラウジングを確保します。ルー器でUrban Shield VPNを有効にするだけで、グローバルサーバーへのアクセスで保護され、ストレスのないブラウジングとストリーミングを楽しむことができます。

## 設定ガイド

GL-B3000をWireGuardクライアントとして設定してUrban Shield VPNを有効にする例を示します。

### 1. Urban Shield VPNにサインアップ

[Urban Shield VPN公式ウェブサイト](https://urbanshieldvpn.com/){class="_blank"}を訪問するか、[ここをクリック](https://payment.urbanshieldvpn.com/sign-up)してUrban Shield VPNアカウントにサインアップしてください。

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. 電源を入れて接続

ルーターの電源を入れます。有線LANまたはWi-Fiでデバイスをルーターに接続します。

### 3. Web管理パネルにアクセス

Web管理パネルにアクセスするには、以下の手順に従ってください。すでにログインしている場合は、[次のパート](#4ネットワーク設定)に進んでください。

Webブラウザ（Chrome、Edge、Safari推奨）を開き、[192.168.8.1](http://192.168.8.1){target="_blank"}にアクセスします。以下に示すように、Web管理パネルの初期設定画面が表示されます。管理者パスワードを設定し、**次へ**をクリックして続行します。

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Wi-Fiネットワークを設定します。ページには、出荷時のWi-Fi詳細（Wi-Fi名（SSID）とパスワード）が表示され、変更するかそのまま使用できます。Wi-Fi詳細を変更した場合は、デバイスをアップデートされたWi-Fiに再接続してください。

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

その後、**次へ**をクリックして管理者パスワードでログインします。

### 4. ネットワーク設定

右上にある**ネットワーク設定ウィザード**があります（ファームウェアv4.7で上）。VPNを設定する前に、ウィザードに従ってインターネットアクセス用のルーターを設定してください。

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Urban Shield VPNを有効にする

左メニューから**VPN** → **WireGuard Client**を選択すると、内蔵されたUrban Shield VPNログインページが表示されます。

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

**メールアドレス**と**パスワード**を入力し、**保存して続行**をクリックします。各サーバーの設定ファイルが生成されます。

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

お好みのサーバーを選択し、**適用**をクリックします。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

利用可能なサーバーがリストに表示されます。

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

3時アイコンをクリックして接続を開始します。

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

接続に成功すると、青いドットが表示されます。

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

VPNダッシュボードで接続状態を確認することもできます。

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## アカウント情報の編集またはログアウト

歯車アイコンをクリックして、アカウント情報を編集またはログアウトします。

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## アップデートする

**アップデートする**をクリックすると、公式ウェブサイトにジャンプしてサブスクリプションをアップデートします。

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## 削除

すべての設定ファイルと、秘密鍵と公開鍵をワンクリックで削除できます。

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
