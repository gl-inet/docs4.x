# GL.iNetルーターにOpenVPNサーバーをセットアップする

OpenVPNはオープンソースのVPNプロトコルであり、仮想プライベートネットワーク（VPN）技術を利用して、安全なサイト間接続またはポイント・ツー・ポイント接続を確立します。

OpenVPNよりもWireGuardの方がはるかに高速なので、WireGuardをお勧めします。WireGuardサーバーのセットアップについては [こちら](wireguard_server.md)をご覧ください。

---

## インターネットサービスプロバイダーがパブリックIPアドレスを割り当てていることを確認する

インターネット サービス プロバイダーがパブリック IP アドレスを割り当てているかどうかを[こちら](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md)から確認してください 。

**そうではないと、OpenVPN サーバーに接続できません。**

別の方法として、リバース・プロキシ・ソリューションを使うこともできます。 [AstroRelay](https://www.astrorelay.com/){target="_blank"}をお勧めします。

## ネットワークトポロジー

* GL.iNet ルーターがネットワーク内のメインルーターである場合、これは簡単です。 [次のステップ](#setup-openvpn-server)に進んでください。
* すでにメインルーターがあり、GL.iNetルーターがメインルーターの下にある場合、メインルーターでポートフォワーディングをセットアップする必要があるかもしれません。
* すでにメインルーターがある場合、GL.iNetルーターはその数段下にあり、それぞれのレベルでポートフォワーディングを設定する必要があります。

## OpenVPNサーバーのセットアップ

1. **設定を作成する**をクリックします（初回のみ）。

    ![openvpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_generate_config.png){class="glboxshadow"}

2. 設定を適用します。

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_configuration.png){class="glboxshadow"}

    設定を変更する必要がない場合は、ページ下部の**クライアント設定をエクスポート**を直接クリックしてください。設定を変更した場合は、**Apply**ボタンをクリックして続行してください。

    * **デバイスモード:** TAP-S2SまたはTun。その違いについては、 [tap s2s vs tun](../tutorials/tap_s2s_vs_tun.md)をご覧ください。

    * **プロトコル:** UDP または TCP。 その違いについては、 [tcp vs udp](../faq/openvpn_tcp_udp.md)をご覧ください。

    * **認証モード:** **証明書のみ**、**ユーザー名/パスワードのみ**、**ユーザー名/パスワードと証明書**の3つのオプションがあります。
    
        **ユーザー名/パスワード** および **ユーザー名/パスワードと証明書** オプションでは、ユーザーを追加する必要があります。OpenVPN クライアントがこのサーバーに接続する場合、ユーザー名とパスワードを入力する必要があります。

        ![openvpn server users](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_users.png){class="glboxshadow"}

       ユーザーを作成。

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_add_a_user.png){class="glboxshadow"}

        **証明書のみ**と**ユーザー名/パスワードと証明書**の場合、ルーターは自動的にサーバーとクライアントの認証キーを生成し、クライアント設定ファイルを生成するときに設定ファイルに書き込みます。

        **詳細設定**については、 [こちら](#advanced-configuration) をご確認ください。

3. クライアント設定のエクスポート

    下部の **クライアント設定のエクスポート**ボタンをクリックするか、変更した設定を適用すると、このダイアログがポップアップ表示されます。

    ネットワークのパブリックIPが時々変更される場合は、設定でDDNSドメインを使用して [DDNS](ddns.md) を有効にすることができます。 **ダウンロード** をクリックすると、設定がエクスポートされます。

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_export_client_configuration.png){class="glboxshadow"}

4. OpenVPNサーバーの起動

    OpenVPN サーバーページの右上にある **スタート** ボタンをクリックしてサーバーを起動します。その後、 [VPNダッシュボードページ](vpn_dashboard.md#vpn-server) に移動し、ステータスやその他の設定を確認します。

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_openvpn_server.png){class="glboxshadow"}

## OpenVPN サーバーが正常に動作しているかどうかを確認する

多くの人は、サーバーが起動しているのを見て、接続されていると誤解します。 間違ったポートやアドレスを転送した場合でも、サーバーは稼働する可能性があります。

![openserverup](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

OpenVPN サーバーが正しく動作しているかどうかを確認するには、別のネットワークに接続された別のデバイスを使い、先ほどエクスポートした OpenVPN 設定を使用して接続し、正しく接続されるかどうか、IP アドレスが OpenVPN サーバーの IP かどうかを確認できます。

最も簡単な方法は、 [OpenVPN公式クライアントアプリ](https://openvpn.net/vpn-client/){target="_blank"} をインストールしたスマホを使い、Wi-Fi接続をオフにして、3G/4G/5G経由でのみインターネットに接続します。そしてOpenVPNアプリを開き、この前エクスポートしたOpenVPNの設定をインポートします。 接続を有効にして、スマートフォンがインターネットにアクセスできるかどうか、そしてその IP アドレスが OpenVPN サーバーの IP アドレスであるかどうかを確認します。

設定ファイルを OpenVPN アプリにインポートする際、以下のようなメッセージが表示されることがありますが、証明書はすでに設定ファイルに含まれていますので、**CONTINUE** をクリックしてください。

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow"}

失敗の原因はいくつかある：

* インターネット・サービス・プロバイダーがパブリックIPアドレスを割り当てていません。 [ こちら](#make-sure-internet-service-provider-assigns-you-a-public-ip-address)からご確認ください。
* ポートフォワーディングの設定が必要な場合があります。 [こちら](#network-topology)からご確認ください。
* OpenVPN サーバーに使用しているポートが、インターネットサービスプロバイダによってブロックされています。 別のポートに変更するか、インターネットサービスプロバイダーにお問い合わせください。
* 国や地域によっては、VPN接続がブロックされる場合があります。

## 詳細設定

このタブで自分の設定を編集することができます。

![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openvpn_server_advanced_configuration.png){class="glboxshadow"}

## クライアントからクライアントへのアクセス

### ネットワーク・トポロジー

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

クライアントからクライアントへの切り替えを有効にし、クライアントに新しい設定をエクスポートすると、クライアントは相互にアクセスできるようになります。

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## OpenVPNクライアントアプリ

他のGL.iNetルーターをOpenVPNクライアントとして使うこともできるし、様々なOSの他のデバイスで公式アプリを使うこともできます。

- OpenVPN公式サイトをご参照ください: [https://openvpn.net/vpn-client/](https://openvpn.net/vpn-client/){target="_blank"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。
