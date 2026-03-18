# GL.iNetルーターにOpenVPNクライアントを設定する方法

このチュートリアルでは、GL.iNet ルーターで OpenVPN クライアントを設定する方法を説明します。

以下の動画を見るか、手順を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

始める前に、OpenVPN の手動設定に対応した VPN サービスプロバイダーの有効な契約が必要です。GL.iNet と互換性のある OpenVPN プロバイダーは [こちら](https://www.gl-inet.com/solutions/vpn/){target="\_blank"} で確認できます。

以下では、ルーターの Web 管理パネルから OpenVPN クライアントを設定する手順を説明します。

## 1. ルーターにログインする

ブラウザを開き、ルーターの Web 管理パネルにアクセスします。デフォルトの IP アドレスは `192.168.8.1` です。管理者パスワードを入力してログインします。

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. VPNクライアントを設定する

利用する VPN サービスプロバイダーに応じて、対応する手順に従ってください。

??? "NordVPN"

    1. ルーターの Web 管理パネルで **VPN** > **OpenVPN Client** に移動します。

    2. **NordVPN** をクリックします。

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. サービス用の認証情報を入力し、**Save and Continue** をクリックします。

        Note: ログイン用のメールアドレスやパスワードではなく、NordVPN の Web サイトにある Nord Dashboard から取得したサービス認証情報を使用してください。

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. 表示された画面で接続したい VPN ロケーションを選択し、**Apply** をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. 接続したい VPN サーバーを選択し、三点アイコンから **Start** をクリックします。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "その他のVPNサービスプロバイダー（例: Surfshark）"

    1. ルーターの Web 管理パネルで **VPN** > **OpenVPN Client** に移動します。

    2. **Add Manually** をクリックします。

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. 名前を設定します。VPN サービスプロバイダー名を入力し、チェックアイコンをクリックしてください。

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. VPN サービスプロバイダーから提供された設定ファイルと、必要であればサービス認証情報を事前に用意しておきます。

    5. ダウンロードした設定ファイルをアップロードします。

        認証情報が必要な場合は入力し、**Apply** をクリックします。

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. VPN サーバーアドレスの横にある三点アイコンをクリックし、**Start** を選択します。

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. VPN接続を確認する

ブラウザで自分の IP アドレスと位置情報を確認してください。表示される IP と場所が、契約しているインターネット回線ではなく、接続先 VPN サーバーの情報と一致していれば、VPN 接続は成功です。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
