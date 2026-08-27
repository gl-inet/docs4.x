# GL.iNetルーターでOpenVPNサーバーを設定する方法

このチュートリアルでは、GL.iNetルーターでOpenVPNサーバーを設定する方法を紹介します。VPNサーバーを使うと、自宅やオフィスのネットワークへ安全にリモート接続できます。GL.iNetルーターなら、数分でOpenVPNサーバーを設定できます。

!!! note "開始前に、以下の要件を満たしていることを確認してください"

    **パブリックIPアドレス**

    OpenVPNサーバーを設定するには、パブリックIPアドレスが必要です。所有しているか確認するには、[こちらのリンク](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/)を参照してください。

    **ポートフォワーディング**

    GL.iNetルーターが上位ルーターの配下に接続されている場合は、[上位ルーターでポートフォワーディングを設定](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/)してください。

## 1. ルーターにログインする

Webブラウザを開き、ルーターのWeb管理パネル（デフォルトIP: 192.168.8.1）にアクセスします。管理者パスワードでログインしてください。

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Dynamic DNSを有効にする（任意）

通常、OpenVPNサーバーの設定には、他のデバイスがVPNサーバーへアクセスするための固定された接続先となる**固定パブリックIPアドレス**が必要です。

ただし、固定パブリックIPアドレスがなく、代わりに動的IPアドレスを使用している場合は、GL.iNetルーターで**Dynamic DNS (DDNS)** を有効にする必要があることがあります。これにより、パブリックIPアドレスが変動してもOpenVPNサーバーへの接続を維持できます。

以下の手順でDynamic DNSを有効にしてください。

1. ルーターのWeb管理パネルで、**APPLICATIONS** > **Dynamic DNS** に移動します。
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. **Enable DDNS** をオンにし、**Terms of Service & Privacy Policy** を確認して同意したうえで、**Apply** をクリックします。
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. 設定ファイルをダウンロードする

1. ルーターのWeb管理パネルで、**VPN** > **OpenVPN Server** に移動します。
2. **Generate Configuration** をクリックします。
3. デフォルト設定のまま、**Export Client Configuration** をクリックします。
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. ポップアップウィンドウで、事前に**Dynamic DNS**を設定している場合は、**Use DDNS Domain** をオンにします。
5. **Download** をクリックし、ファイルを保存します。
6. **OpenVPN Server** ページ上部の **Start** をクリックします。
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "（任意）VPNサーバーのローカルネットワークにアクセスするには、以下の設定を有効にしてください:"

    ファームウェア v4.7 以前:

    1. 左側のサイドバーで **VPN** > **VPN Dashboard** をクリックします。
    2. Optionsアイコンをクリックします。
    3. **Remote Access LAN** をオンにします。
    4. **Apply** をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ファームウェア v4.8 以降:

    1. 左側のサイドバーで **VPN** > **OpenVPN Server** をクリックします。
    2. 右上の **Options** をクリックします。
    3. **Allow Remote Access the LAN Subnet** をオンにします。
    4. **Apply** をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. OpenVPNサーバーに接続する

OpenVPNサーバーに接続するには、OpenVPNクライアントが必要です。以下のいずれかの方法で設定できます。

??? "方法1: サードパーティ製OpenVPNクライアントアプリを使う（OpenVPNクライアントを設定できる追加のルーターがない場合はこちらを使用）"

    このチュートリアルでは、OpenVPN Inc が提供する公式アプリ **OpenVPN Connect** を例として使用します。

    1. 別のデバイスで別のWi-Fiネットワークに接続します（モバイルデバイスを使用している場合はモバイル通信でも構いません）。
    2. 先ほどダウンロードした設定ファイルを、そのデバイスに送信し（例: メール）、ダウンロードします。
    3. 使用するOS向けの OpenVPN Connect をダウンロードします。
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. アプリで利用規約を読み、**Agree** を選択します。
    5. **Upload File** を選択します。
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. **Browse** を選択し、先ほどダウンロードした設定ファイルを選択します。
    7. **OK** を選択します。
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. **Connect** > **OK** > **Allow** を選択します。

    VPNプロファイルの上部に "Connected" と表示されます。
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "方法2: OpenVPNクライアントを設定できるルーターを使う"

    OpenVPNクライアントの手動設定に対応した任意のルーターを使用できます。このチュートリアルでは、GL.iNetのトラベルルーター [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) を例として使用します。

    1. 別のデバイスで別のWi-Fiネットワークに接続します（モバイルデバイスを使用している場合はモバイル通信でも構いません）。
    2. Webブラウザのアドレス欄に、ルーターの管理パネルURL（例: 192.168.8.1）を入力します。
    3. パスワードを入力し、**Login** をクリックします。
    4. 左側のサイドバーで **VPN** > **OpenVPN Client** をクリックします。
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. **Add Manually** をクリックします。
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. フィールドに名前を入力し、チェックアイコンをクリックします。
    7. 先ほどダウンロードした設定ファイルをアップロードします。
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. **Apply** をクリックします。
    9. 三点アイコンをクリックし、**Start** をクリックします。
    10. OpenVPNクライアントを実行しているルーターにデバイスを接続します。

## 5. VPN接続を確認する

Webブラウザを開き、自分のIPアドレスと所在地を検索します。表示された情報がインターネットサービスプロバイダーのIPと所在地ではなく、VPNサーバーのIPと所在地に一致していれば、VPN接続は成功しています。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
