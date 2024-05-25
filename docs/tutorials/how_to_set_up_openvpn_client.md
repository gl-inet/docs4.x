# GL.iNet ルーターに OpenVPN クライアントを設定する方法

このチュートリアルでは、**GL.iNet ルーターに OpenVPN クライアントを設定する方法**を説明します。

始める前に、OpenVPN の手動構成をサポートする VPN サービスプロバイダーの有効なサブスクリプションが必要です。[GL.iNet がサポートする OpenVPN 対応 VPN のリストをご覧ください](https://www.gl-inet.com/solutions/vpn/)。

以下の手順は、ルーター管理パネルを通じて OpenVPN クライアントを設定するために書かれています。（GL.iNet モバイルアプリ経由で OpenVPN クライアントを設定するには、[アプリをダウンロード](https://www.gl-inet.com/app/)して設定してください。）

## 1. ルーター管理パネルにサインインする

ウェブブラウザでルーター管理パネルの URL（例：192.168.8.1）を入力します。パスワードを入力し、**ログイン**をクリックします。

## 2. VPN プロファイルを設定して接続する

使用している VPN サービスプロバイダーに応じて、適切なセクションに従ってください。

=== "NordVPN"

    1. 左側のサイドバーで **VPN** > **OpenVPN クライアント** をクリックします。
    2. **NordVPN** をクリックします。

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. サービスの認証情報を入力し、**保存して続行**をクリックします。

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. プロンプトで接続したい VPN ロケーションを選択し、**適用**をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. 接続したい VPN サーバーの横にある三点アイコンをクリックし、**開始**を選択します。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

=== "その他の VPN サービスプロバイダー（例：ExpressVPN、Surfshark）"

    1. 左側のサイドバーで **VPN** > **OpenVPN クライアント** をクリックします。
    2. **手動で追加** をクリックします。

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. VPN サービスプロバイダーの名前（例：ExpressVPN）を入力し、チェックアイコンをクリックします。

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. サービスの認証情報を見つけ、VPN サービスプロバイダーから提供された構成ファイルをダウンロードします。
    5. 先ほどダウンロードした構成ファイルをアップロードします。
    6. 先ほど見つけたサービスの認証情報を入力し、**適用**をクリックします。
    
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

7. VPN サーバーアドレスの横にある三点アイコンをクリックし、**開始**を選択します。

    ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. VPN に正常に接続されているか確認する

ウェブブラウザで自分の IP アドレスの場所を検索します。接続している VPN サーバーの場所と一致する場合、VPN 接続は成功です。これで設定は完了です。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。