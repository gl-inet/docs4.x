# GL.iNetルーターでOpenVPNクライアントを設定する方法

このチュートリアルでは、GL.iNetルーターでOpenVPNクライアントを設定する方法を紹介します。

この動画を見るか、以下の手順を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

開始前に、OpenVPNの手動設定に対応したVPNサービスプロバイダーの有効な契約があることを確認してください。GL.iNetと互換性のあるOpenVPNプロバイダーは[こちら](https://www.gl-inet.com/solutions/vpn/){target="_blank"}で確認できます。

以下は、ルーターのWeb管理パネルからOpenVPNクライアントを設定する手順です。

## 1. ルーターにログインする

Webブラウザを開き、ルーターのWeb管理パネル（デフォルトIP: 192.168.8.1）にアクセスします。管理者パスワードでログインしてください。

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. VPNクライアントを設定する

利用しているVPNサービスプロバイダーに対応するセクションを参照してください。

??? "NordVPN"

    1. ルーターのWeb管理パネルで、**VPN** > **OpenVPN Client** に移動します。

    2. **NordVPN** をクリックします。

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. サービス認証情報を入力し、**Save and Continue** をクリックします。

        注: ここで入力するのはログイン用のメールアドレスやパスワードではなく、NordVPNのWebサイト -> Nord Dashboard で取得したサービス認証情報です。

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. 表示された画面で接続したいVPNロケーションを選択し、**Apply** をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. 接続したいVPNサーバーを選択し、三点アイコンから **Start** をクリックします。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "その他のVPNサービスプロバイダー（例: Surfshark）"

    1. ルーターのWeb管理パネルで、**VPN** > **OpenVPN Client** に移動します。

    2. **Add Manually** をクリックします。

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. 名前を設定します。VPNサービスプロバイダー名を入力し、チェックアイコンをクリックします。

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. VPNサービスプロバイダーから提供された設定ファイルと、必要に応じてサービス認証情報をダウンロードしてあることを確認します。
    5. ダウンロードした設定ファイルをアップロードします。

        必要に応じてサービス認証情報を入力し、**Apply** をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. VPNサーバーアドレスの横にある三点アイコンをクリックし、**Start** を選択します。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. VPN接続を確認する

Webブラウザを開き、自分のIPアドレスと所在地を検索します。表示された情報がインターネットサービスプロバイダーのIPと所在地ではなく、VPNサーバーのIPと所在地に一致していれば、VPN接続は成功しています。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
