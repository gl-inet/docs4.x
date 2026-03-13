# GL.iNetルー器でOpenVPNサーバーを設定する方法

このチュートリアルでは、GL.iNetルー器でOpenVPNサーバーを設定する方法を説明します。VPNサーバーを使用すると、家庭やオフィスのネットワークに安全にリモート接続できます。GL.iNetルー器を使用すると、数分でOpenVPNサーバーを設定できます。

!!! note "開始する前に、以下の要件を満たしていることを確認してください"
    
    **パブリックIPアドレス**

    OpenVPNサーバーを設定するには、パブリックIPアドレスが必要です。持っているかどうかを確認するには、[このリンク](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/)を参照してください。

    **ポート転送**

    GL.iNetルー器が主ルー器の背後につながっている場合は、[主ルー器でポート転送を設定](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/)してください。

## 1. ルーターにログインする

Webブラウザを開き、ルーターのWeb管理パネルにアクセスします（デフォルトIP：192.168.8.1）。管理パスワードでログインします。

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. ダイナミックDNSを有効にする（オプション）

OpenVPNサーバーを設定するには通例、**静のパブリックIPアドレス**が必要です。これは彼のデバイスがVPNサーバーにアクセスするための固定エンドポイントを提供します。

ただし、静のパブリックIPアドレスがない場合（例：代わりに動のIPアドレスの場合）、GL.iNetルー器で**ダイナミックDNS（DDNS）**を有効にする必要があるかもしれません。これにより、パブリックIPアドレスが動のに変更しても、OpenVPNサーバーへの持続のな接続が可能になります。

ダイナミックDNSを有効にするには、以下の手順に従ってください。

1. ルーターのWeb管理パネルで、**アプリケーション** > **ダイナミックDNS**に移動します。
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. **DDNSを有効にする**をオンにし、利用規約とプライバシーポリシーを読んで同意し、**適用**をクリックします。
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. 設定ファイルをダウンロード

1. ルーターのWeb管理パネルで、**VPN** > **OpenVPNサーバー**に移動します。
2. **設定ファイルを生成**をクリックします。
3. デフォルト設定のままにし、**クライアント設定ファイルをエクスポート**をクリックします。
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. ポップアップウィンドウで、で前に**ダイナミックDNS**を設定している場合は、**DDNSドメインを使用**のスイッチをオンにします。
5. **ダウンロード**をクリックし、ファイルを保存します。
6. **OpenVPNサーバー**ページの上部で、**開始**をクリックします。
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "（オプション）VPNサーバーのローカルネットワークにアクセスするには、以下の設定を有効にしてください："

    ファームウェアv4.7で前の場合：

    1. 左サイドバーで、**VPN** > **VPNダッシュボード**をクリックします。
    2. オプションアイコンをクリックします。
    3. **リモートアクセスLAN**のスイッチをオンにします。
    4. **適用**をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ファームウェアv4.8で降の場合：

    1. 左サイドバーで、**VPN** > **OpenVPNサーバー**をクリックします。
    2. 右上の**オプション**をクリックします。
    3. **LANサブネットへのリモートアクセスを許可**のスイッチをオンにします。
    4. **適用**をクリックします。

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. OpenVPNサーバーに接続する

OpenVPNサーバーに接続するには、OpenVPNクライアントが必要です。以下のいずれかの方法で設定できます：

??? "方法1：サードパーティのOpenVPNクライアントアプリ（追加のOpenVPNクライアントを設定できるルー器がない場合、この方法を使用してください）"

    このチュートリアルでは、OpenVPN Incが開発した 公式アプリであるOpenVPN Connectアプリ例をとして使用します。

    1. 別のデバイスで、別のWi-Fiネットワークに接続します（モバイルデバイスを使用している場合は、モバイルネットワークに接続します）。
    2. で前にダウンロードした設定ファイルをデバイスに送信します（例：メールで送信）。
    3. デバイスのオペレーティングシステム用のOpenVPN Connectをダウンロードします：
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. アプリで利用規約を読み、**同意する**を選択します。
    5. **ファイルをアップロード**を選択します。
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. **参照**を選択し、で前にダウンロードした設定ファイルを選択します。
    7. **OK**を選択します。
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"} 
    8. **接続** > **OK** > **許可**を選択します。

    VPNプロファイルの上部に「接続済み」という単語が表示されます。
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"} 

??? "方法2：OpenVPNクライアントを設定できるルー器"

    OpenVPNクライアントの手動設定をサポートする任意のルー器を使用できます。このチュートリアルでは、GL.iNetのトラベルルー器[Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/)を例として使用します。

    1. 別のデバイスで、別のWi-Fiネットワークに接続します（モバイルデバイスを使用している場合は、モバイルネットワークに接続します）。
    2. Webブラウザのアドレスバーで、ルー器管理面板のURLを入力します（例：192.168.8.1）。
    3. パスワードを入力し、**ログイン**をクリックします。
    4. 左サイドバーで、**VPN** > **OpenVPNクライアント**をクリックします。

        ![client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-client.jpeg){class="glboxshadow"}

    5. **追加**をクリックして新しい接続を追加します。

        ![add](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add.png){class="glboxshadow"}

    6. 前にダウンロードした設定ファイルをインポートします。ファイルをドラッグ＆ドロップするか、**ファイルを参照**をクリックして選択します。

        ![import](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/import-profile.jpeg){class="glboxshadow"}

    7. 設定ファイルをインポートした後、绿の時がinfeld場合は、VPNクライアントがOpenVPNサーバーに接続されていることを意味します。

        ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-to-server.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
