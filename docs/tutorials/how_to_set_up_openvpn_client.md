# GL.iNet ルーターで OpenVPN クライアントを設定する方法

このチュートリアルでは、**GL.iNet ルーターで OpenVPN クライアントを設定する方法**を説明します。

始める前に、OpenVPN の手動設定をサポートする VPN サービスプロバイダーとの有効なサブスクリプションが必要です。[GL.iNet がサポートする OpenVPN 対応 VPN のリストを見る](https://www.gl-inet.com/solutions/vpn/)。

以下の手順は、ルーター管理パネルを通じて OpenVPN クライアントを設定するためのものです。（GL.iNet モバイルアプリを使って OpenVPN クライアントを設定する場合は、[アプリをダウンロード](https://www.gl-inet.com/app/)して設定してください。）

## 1. ルーター管理パネルにログインする

Web ブラウザでルーター管理パネルの URL（例：192.168.8.1）を入力します。パスワードを入力し、**ログイン**をクリックします。

## 2. VPN プロファイルを設定し、接続する

使用している VPN サービスプロバイダーに応じたセクションに従います。

=== "NordVPN"

    1. 左サイドバーで **VPN** > **OpenVPN クライアント** をクリックします。
    2. **NordVPN** をクリックします。

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. サービスの資格情報を入力し、**保存して続行**をクリックします。

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. プロンプトで接続したい VPN の場所を選択し、**適用**をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. 接続したい VPN サーバーの横にある三点リーダーアイコン > **開始**をクリックします。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

=== "その他の VPN サービスプロバイダー (例：ExpressVPN、Surfshark)"

    1. 左サイドバーで **VPN** > **OpenVPN クライアント** をクリックします。
    2. **手動で追加**をクリックします。

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. VPN サービスプロバイダーの名前（例：ExpressVPN）を入力し、チェックアイコンをクリックします。

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. サービスの資格情報を見つけ、VPN サービスプロバイダーが提供する設定ファイルをダウンロードします。
    5. 以前にダウンロードした設定ファイルをアップロードします。
    6. 以前に見つけたサービスの資格情報を入力し、**適用**をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    7. VPN サーバーアドレスの横にある三点リーダーアイコン > **開始**をクリックします。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. VPN に正常に接続されているか確認する

Web ブラウザで IP アドレスの位置を検索します。それが接続している VPN サーバーの位置と一致していれば、VPN 接続は成功しています。設定は完了です。

---

まだ質問がありますか？私たちの [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪れてください。