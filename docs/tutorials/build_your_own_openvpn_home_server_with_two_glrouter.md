# GL.iNetルーターでOpenVPNサーバーをセットアップする方法

このチュートリアルでは、**GL.iNetルーターでOpenVPNサーバーをセットアップする方法**を説明します。VPNサーバーを使用すると、自宅やオフィスのネットワークにリモートで安全に接続することができます。GL.iNetルーターを使用すると、数分でOpenVPNサーバーをセットアップできます。

!!! 注意 "開始する前に、次の要件を確認してください:"
    **パブリックIPアドレス**

    OpenVPNサーバーをセットアップするには、パブリックIPアドレスが必要です。パブリックIPアドレスがあるかどうかを確認するには、[こちらの手順](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/)に従ってください。

    **ポートフォワーディング**

    GL.iNetルーターがプライマリルーターに接続されている場合は、[プライマリルーターでポートフォワーディングを設定する必要があります](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/)。

## 1. ルーターにサインイン

ウェブブラウザでルーター管理パネルのURL（例：192.168.8.1）を入力します。パスワードを入力し、**ログイン**をクリックします。

![sign in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. 動的DNSを設定する（オプション）

OpenVPNサーバーをセットアップするには、静的パブリックIPアドレスが必要です。ほとんどの場合、静的パブリックIPアドレスを持っていないことが多いです。この場合、GL.iNetルーターで動的DNSを設定する必要があります。これにより、パブリックIPアドレスが動的（静的ではない）で常に変わる場合でも、OpenVPNサーバーに接続できます。

動的DNSを設定するには、次の手順に従ってください：

1. 左側のサイドバーで、**アプリケーション** > **動的DNS**をクリックします。
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. **DDNSを有効にする**の隣にあるスイッチをオンにします。
3. **利用規約とプライバシーポリシーを読み、同意します**のチェックボックスをオンにします。
4. **適用する**をクリックします。
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. 設定ファイルをダウンロード

1. 左側のサイドバーで、**VPN** > **OpenVPN サーバ**をクリックします。
2. **構成を生成する**をクリックします。
3. デフォルト設定のまま、**クライアント構成のエクスポート**をクリックします。
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. この前**動的DNS**を設定した場合は、**DDNSドメインを使用する**のスイッチをオンにします。
5. **ダウンロード**をクリックし、ファイルを保存します。
6. 上部で、**スタート**をクリックします。
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(オプション) VPNサーバーのローカルネットワークにアクセスするには、次の設定を有効にします:"
    1. 左側のサイドバーで、**VPN** > **VPN ダッシュボード**をクリックします。
    2. オプションアイコンをクリックします。
    3. **リモートアクセスLAN**のスイッチをオンにします。
    4. **適用する**をクリックします。
    ![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class}

## 4. OpenVPNサーバーに接続する

OpenVPNサーバーに接続するには、OpenVPNクライアントが必要です。以下の方法のいずれかを使用して設定できます:

??? "方法1: サードパーティのOpenVPNクライアントアプリ（OpenVPNクライアントを設定できる追加のルーターがない場合はこちらの方法を使用してください）"

    このチュートリアルでは、OpenVPN Inc.が開発した公式アプリであるOpenVPN Connectアプリを例として使用します。

    1. 他のデバイスで、異なるWi-Fiネットワークに接続します（モバイルデバイスを使用している場合はセルラーに接続します）。
    2. 以前にダウンロードした設定ファイルをそのデバイスに送信し（例: メールで）、そのデバイスにファイルをダウンロードします。
    3. デバイスのオペレーティングシステムに対応するOpenVPN Connectをダウンロードします：
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. アプリで、利用規約を読み、**同意する**を選択します。
    5. **ファイルをアップロードする**を選択します。
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. **ブラウズ**を選択し、以前にダウンロードした設定ファイルを選択します。
    7. **OK**を選択します。
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"} 
    8. **接続する** > **OK** > **許可する**を選択します。

    VPNプロファイルの上部に「接続済み」の表示が見えます。
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "方法2: OpenVPNクライアントの設定をサポートするルーターを使用"

    OpenVPNクライアントの手動設定をサポートする任意のルーターを使用できます。このチュートリアルでは、GL.iNetの旅行用ルーター [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) を例として使用します。

    1. 他のデバイスで、異なるWi-Fiネットワークに接続します（モバイルデバイスを使用している場合はセルラーに接続します）。
    2. ウェブブラウザのアドレスバーにルーターの管理パネルのURL（例: 192.168.8.1）を入力します。
    3. パスワードを入力し、**ログイン**をクリックします。
    4. 左側のサイドバーで、**VPN** > **OpenVPN クライアント**をクリックします。
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. **手動で追加**をクリックします。
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. フィールドに名前を入力し、チェックアイコンをクリックします。
    7. この前にダウンロードした設定ファイルをアップロードします。
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. **適用する**をクリックします。
    9. 三点アイコンをクリックし、**スタート**をクリックします。
    10. OpenVPNクライアントを実行しているルーターにデバイスを接続します。

## 5. 接続が成功したか確認する

OpenVPNサーバーに正常に接続されているか確認するには、オンラインで自分のIPアドレスを調べます。もしそれがインターネットサービスプロバイダが提供するネットワークのIPアドレスと一致していれば、OpenVPNサーバーに正常に接続されています。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪れてください。