# GL.iNet ルーターで OpenVPN サーバーを設定する

OpenVPN は、仮想プライベートネットワーク技術を用いて安全な site-to-site 接続または point-to-point 接続を確立する、オープンソースの VPN プロトコルです。

GL.iNet ルーターで OpenVPN サーバーを設定するには、以下の動画を見るか、下記の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## パブリック IP アドレスがあることを確認する {#make-sure-you-have-a-public-ip-address}

インターネットサービスプロバイダーからパブリック IP アドレスが割り当てられているかどうかは、[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) で確認してください。

**割り当てられていない場合、このルーターを OpenVPN Server として設定することはできません。**

代替手段:

1. メインルーターがある場合は、そのルーターにログインして、ISP からパブリック IP を取得しているか確認します。
2. ISP にパブリック IP アドレスの提供を依頼します。追加料金が発生する場合があります。
3. 上記 2 つの方法が使えない場合（ネットワークが CGNAT 配下にある場合など）は、SD-WAN ソリューション [AstroWarp](https://www.astrowarp.net/){target="_blank"} の利用をご検討ください。

## ポートフォワーディングが必要か確認する {#confirm-if-port-forwarding-is-required}

**Network Topology**

??? "GL.iNet がメインルーターの場合"

    * GL.iNet ルーターがネットワークのメインルーターであれば、ポートフォワーディングは不要です。[次の手順](#setup-openvpn-server) に進んでください。

??? "GL.iNet がサブルーターの場合"

    * すでにメインルーターがあり、GL.iNet ルーターをサブルーターとして使用している場合は、メインルーター側で [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) を設定する必要があります。

    * すでにメインルーターがあり、GL.iNet ルーターがさらに下位階層にある場合は、途中の各ルーターで [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) を設定してください。

## OpenVPN サーバーを設定する {#setup-openvpn-server}

Web 管理パネルにログインし、**VPN** -> **OpenVPN Server** を開きます。

1. **Generate Configuration** をクリックします（VPN サーバー初回設定時のみ）。

    ![ovpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_generate_config.png){class="glboxshadow"}

2. 設定を適用します。

    ほとんどの環境ではデフォルト設定のままで利用できます。

    設定を変更する必要がない場合は、画面下部の **Export Client Configuration** をクリックして手順 3 に進んでください。

    設定を変更した場合は、クライアント設定をエクスポートする前に **Apply** をクリックしてください。

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S または Tun。違いについては [こちら](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode) を参照してください。

    * **Protocol:** UDP または TCP。違いについては [こちら](../faq/openvpn_tcp_udp.md) を参照してください。

    * **Authentication Mode:** クライアントがサーバーへ接続する際の認証方法を決定します。以下の 3 つの選択肢があります。

        - **Certificate Only**: ルーターがサーバー証明書とクライアント証明書のキーを自動生成し、クライアント設定ファイルに埋め込みます。クライアント側で設定を読み込む際に、追加の認証情報は不要です。

        - **Username/Password Only**: ルーターは証明書キーを含まないクライアント設定を生成します。クライアント設定をエクスポートする前に、Users タブでユーザー名とパスワードを追加する必要があります。クライアント側で設定を読み込む際に、これらの認証情報の入力が必要です。

        - **Username/Password and Certificate**: まず Users タブでユーザー名とパスワードを追加する必要があります。次に、ルーターがサーバー証明書とクライアント証明書のキーを自動生成し、設定ファイルに埋め込みます。クライアント側では最初に証明書キーが検証され、その後ユーザー名/パスワード認証が行われるため、二要素の保護になります。

        ユーザー作成例は以下のとおりです。

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: 必要に応じて、さらに詳細なサーバー設定を変更できます。

        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. クライアント設定をエクスポートします。

    Configuration タブの下部にある **Export Client Configuration** をクリックします（または変更した設定を適用します）。すると、以下のようなウィンドウが表示されます。

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_export_configuration.png){class="glboxshadow"}

    - ネットワークのパブリック IP が頻繁に変わる場合は、[DDNS](ddns.md) を有効にして DDNS ドメインをサーバーアドレスとして使用できます。

    - ファームウェア v4.8 以降では、サーバーアドレスとしてパブリック IP、DDNS ドメイン、現在の WAN IP のいずれかを指定できます。変更すると、設定ファイル内のサーバーアドレスも同時に更新されます。

    その後、**Download** をクリックして設定をエクスポートします。

4. OpenVPN サーバーを起動します。

    OpenVPN Server ページ右上の **Start** ボタンをクリックしてサーバーを起動します。起動後は VPN Dashboard ページで状態や関連設定を確認できます。

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## OpenVPN サーバーが正常に動作しているか確認する

### サーバー状態を確認する

ファームウェア v4.8 以降では、**OpenVPN Server** ページでサーバー接続状態を確認できます。

アップロード/ダウンロードのトラフィック統計が表示されていれば、OpenVPN サーバーは稼働しています。

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

ファームウェア v4.7 以前では、**VPN Dashboard** ページでサーバー接続状態を確認してください。

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

### クライアント側の IP を確認する

サーバーへの接続が成功しているか確認するには、先ほどエクスポートした OpenVPN 設定を別ネットワーク上のデバイス（サーバーと同じローカルネットワークではないデバイス）にインポートします。その後 Web ブラウザで自身の IP アドレスと位置情報を確認し、インターネットサービスプロバイダーの IP ではなく VPN サーバーの IP と位置情報が表示されれば、VPN 接続は成功です。

最も簡単なのは、公式の [OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"} をインストールしたスマートフォンを使う方法です。まずスマートフォンの Wi-Fi を無効にし、モバイルデータ通信（4G/5G）のみでインターネットに接続します。次に OpenVPN App を開いて設定ファイルをインポートし、接続を開始します。スマートフォンがインターネットへ接続できるか、また IP アドレスが OpenVPN Server の IP と一致するか確認してください。

OpenVPN App に設定ファイルをインポートすると、以下のようなメッセージが表示されることがあります。証明書はすでに設定ファイルに埋め込まれているため、**CONTINUE** をクリックして進めてください。

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

接続に失敗する主な原因は次のとおりです。

* インターネットサービスプロバイダーからパブリック IP アドレスが割り当てられていない。[こちら](#make-sure-you-have-a-public-ip-address) を確認してください。
* ポートフォワーディングの設定が必要な場合がある。[こちら](#confirm-if-port-forwarding-is-required) を確認してください。
* OpenVPN Server で使用しているポートがインターネットサービスプロバイダーによってブロックされている。別のポートに変更するか、ISP に問い合わせてください。
* 一部の国や地域では VPN 接続がブロックされる場合があります。

## クライアント間アクセス

**Network Topology**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

client to client のトグルを有効にして、新しい設定をクライアントへエクスポートすると、クライアント同士で相互アクセスできるようになります。

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## OpenVPN App のインストール

[OpenVPN 公式サイト](https://openvpn.net/vpn-client/){target="_blank"} から OpenVPN App をダウンロードしてください。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
