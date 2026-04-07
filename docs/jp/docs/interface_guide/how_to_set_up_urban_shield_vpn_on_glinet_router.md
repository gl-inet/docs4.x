# GL.iNetルーターでUrban Shield VPNを設定する方法

[Urban Shield VPN](https://urbanshieldvpn.com/) は、世界中のユーザー向けに高セキュリティかつ高性能なVPNソリューションを提供するVPNプロバイダーです。事前設定済みのGL.iNet VPNルーターと柔軟なサブスクリプションプランを提供し、安全でプライベートなブラウジングを実現します。ルーターでUrban Shield VPNを有効にするだけで、グローバルサーバーにアクセスでき、安心して閲覧やストリーミングを行えます。

## セットアップガイド

ここでは、GL-B3000をWireGuard Clientとして設定してUrban Shield VPNを有効化する例を紹介します。

### 1. Sign Up Urban Shield VPN

[Urban Shield VPN公式サイト](https://urbanshieldvpn.com/){class="_blank"} にアクセスするか、[こちら](https://payment.urbanshieldvpn.com/sign-up) をクリックしてUrban Shield VPNアカウントを登録します。

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Power on and Connect

ルーターの電源を入れます。EthernetケーブルまたはWi-Fiでデバイスをルーターに接続します。

### 3. Access Web Admin Panel

以下の手順に従ってWeb Admin Panelにアクセスします。すでにログイン済みの場合は、[次の手順](#4-network-setup)に進んでください。

Webブラウザ（Chrome、Edge、Safari推奨）を開き、[192.168.8.1](http://192.168.8.1){target="_blank"} にアクセスします。下図のようにWeb Admin Panelの初期設定画面が表示されます。管理者パスワードを設定し、**Next** をクリックして続行します。

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Wi-Fiネットワークを設定します。ページには出荷時のWi-Fi情報（Wi-Fi名（SSID）とパスワード）が表示され、変更することもそのまま使うこともできます。Wi-Fi情報を変更した場合は、更新後のWi-Fiにデバイスを再接続してください。

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

続いて **Next** をクリックし、管理者パスワードでログインします。

### 4. Network Setup

右上に **Network Setup Wizard** があります（ファームウェア v4.7 以降で利用可能）。VPNを設定する前に、このウィザードに従ってルーターのインターネット接続を設定してください。

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Activate Urban Shield VPN

左側メニューから **VPN** -> **WireGuard Client** を選択します。内蔵のUrban Shield VPNログインページが表示されます。

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

**Email** と **Password** を入力し、**Save And Continue** をクリックします。各サーバーの設定ファイルが生成されます。

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

使用したいサーバーを選択し、**Apply** をクリックします。

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

利用可能なサーバーが一覧に表示されます。

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

三点アイコンをクリックして接続を開始します。

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

接続に成功すると、青いドットが表示されます。

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

VPN Dashboard でも接続状態を確認できます。

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## アカウント情報の編集またはログアウト

歯車アイコンをクリックすると、アカウント情報の編集やログアウトを行えます。

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## 更新ページへ移動

**Go Renew** をクリックすると、公式サイトへ移動してサブスクリプションを更新できます。

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Delete

ワンクリックで、すべての設定ファイルと秘密鍵・公開鍵を削除できます。

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
