# GL.iNet ルーターで OpenVPN サーバーを設定する方法

このチュートリアルでは、GL.iNet ルーターで OpenVPN サーバーを設定する方法を説明します。VPN サーバーを使うと、自宅やオフィスのネットワークへ安全にリモート接続できます。GL.iNet ルーターなら、数分で OpenVPN サーバーを構成できます。

!!! note "開始する前に、以下の要件を満たしていることを確認してください"

    **パブリックIPアドレス**

    OpenVPN サーバーの構築にはパブリック IP アドレスが必要です。お使いの回線に割り当てられているかどうかは、[こちら](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/) を参照してください。

    **ポート転送**

    GL.iNet ルーターが主ルーターの背後に接続されている場合は、[主ルーターでポート転送を設定](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) してください。

## 1. ルーターにログインする

Webブラウザを開き、ルーターのWeb管理パネルにアクセスします（デフォルトIP：192.168.8.1）。管理パスワードでログインします。

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. ダイナミックDNSを有効にする（オプション）

OpenVPN サーバーを設定するには、通常 **固定のパブリック IP アドレス** が必要です。これにより、他のデバイスが VPN サーバーへアクセスするための固定エンドポイントを用意できます。

ただし、固定のパブリック IP アドレスがなく、動的 IP アドレスが割り当てられている場合は、GL.iNet ルーターで **Dynamic DNS（DDNS）** を有効にする必要がある場合があります。これにより、パブリック IP アドレスが変わっても OpenVPN サーバーへ継続的に接続できます。

ダイナミックDNSを有効にするには、以下の手順に従ってください。

1. ルーターの Web 管理パネルで、**APPLICATIONS** > **Dynamic DNS** に移動します。
   ![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. **Enable DDNS** をオンにし、**Terms of Service & Privacy Policy** を読んで同意したうえで、**Apply** をクリックします。
   ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. 設定ファイルをダウンロード

1. ルーターのWeb管理パネルで、**VPN** > **OpenVPNサーバー**に移動します。
2. **設定ファイルを生成**をクリックします。
3. デフォルト設定のままにし、**クライアント設定ファイルをエクスポート**をクリックします。
   ![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. ポップアップウィンドウで、以前に **Dynamic DNS** を設定している場合は、**Use DDNS Domain** をオンにします。
5. **ダウンロード**をクリックし、ファイルを保存します。
6. **OpenVPNサーバー**ページの上部で、**開始**をクリックします。
   ![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "（オプション）VPN サーバー側のローカルネットワークへアクセスするには、以下の設定を有効にしてください:"

    ファームウェア v4.7 以前の場合:

    1. 左サイドバーで、**VPN** > **VPNダッシュボード**をクリックします。
    2. オプションアイコンをクリックします。
    3. **Remote Access LAN** をオンにします。
    4. **適用**をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ファームウェア v4.8 以降の場合:

    1. 左サイドバーで、**VPN** > **OpenVPNサーバー**をクリックします。
    2. 右上の**オプション**をクリックします。
    3. **Allow Remote Access the LAN Subnet** をオンにします。
    4. **適用**をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

## 4. OpenVPNサーバーに接続する

OpenVPN サーバーへ接続するには、OpenVPN クライアントが必要です。以下のいずれかの方法で設定できます。

??? "方法 1: サードパーティ製 OpenVPN クライアントアプリを使う（OpenVPN クライアントを設定できる追加ルーターがない場合）"

    このチュートリアルでは、OpenVPN Inc が提供する公式アプリ **OpenVPN Connect** を例に使用します。

    1. 別のデバイスで、別の Wi-Fi ネットワークへ接続します。モバイルデバイスを使う場合は、モバイル回線へ接続してください。
    2. 先ほどダウンロードした設定ファイルを、そのデバイスへ送ります。たとえばメールで送信できます。
    3. 使用する OS に対応した OpenVPN Connect をダウンロードします:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. アプリで利用規約を読み、**Agree** を選択します。
    5. **Upload File** を選択します。
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. **Browse** を選択し、先ほどダウンロードした設定ファイルを指定します。
    7. **OK** を選択します。
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. **Connect** > **OK** > **Allow** を選択します。

    VPN プロファイルの上部に "Connected" と表示されれば接続完了です。
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "方法 2: OpenVPN クライアントを設定できるルーターを使う"

    OpenVPN クライアントの手動設定に対応した任意のルーターを使用できます。このチュートリアルでは、GL.iNet のトラベルルーター [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) を例に使用します。

    1. 別のデバイスで、別の Wi-Fi ネットワークへ接続します。モバイルデバイスを使用している場合は、モバイル回線へ接続してください。
    2. Web ブラウザのアドレスバーに、ルーター管理画面の URL（例: 192.168.8.1）を入力します。
    3. パスワードを入力し、**ログイン**をクリックします。
    4. 左サイドバーで、**VPN** > **OpenVPN Client** をクリックします。
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. **Add Manually** をクリックします。
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. 名前を入力し、チェックアイコンをクリックします。
    7. 先ほどダウンロードした設定ファイルをアップロードします。
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. **Apply** をクリックします。
    9. 三点アイコンをクリックし、**Start** をクリックします。
    10. OpenVPN クライアントを動かしているルーターにデバイスを接続します。

## 5. VPN 接続を確認する

Web ブラウザを開き、IP アドレスと位置情報を確認してください。表示された IP アドレスと位置情報が、インターネットサービスプロバイダーのものではなく VPN サーバーのものになっていれば、VPN 接続は正常です。

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
