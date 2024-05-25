# AstroRelay経由でOpenVPNサーバーを設定する方法

シナリオ: GL.iNetルーターでOpenVPNサーバーを設定してローカルサービスにリモートアクセスしたいが、ISPがパブリックIPアドレスを提供していない場合。

[AstroRelay](https://www.astrorelay.com){target="_blank"}は、NATおよびファイアウォールの背後にあるリソースにアクセスできる安全なリバースプロキシトンネルを提供します。

1. パブリックIPアドレスがないことを無視して、[こちら](../interface_guide/openvpn_server.md)のガイドに従ってOpenVPNサーバーを設定してください。**ローカルネットワークへのアクセスを許可**を有効にしてください。

    ![openvpnサーバーを設定](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    次に、OpenVPN構成をエクスポートします。以下の画像はその例です。

    ![openvpn構成](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. AstroRelayアカウントにサインアップし、[チュートリアル](https://www.astrorelay.com/tutorial.html){target="_blank"}に従ってください。

    新しいドメインを追加する際、ルーターに最も近いサーバーを選択してください。

    ![astrorelay 新しいドメインを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際、**Destination Host IP**にはルーターのIPアドレス（この場合は**192.168.48.1**）を入力してください。

    ![openvpnサーバーのリンク](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    最終的にリンクを取得できます。例えば、**testforx3000.arlab1.cc:37202**のようになります。アイコンをクリックしてリンクをコピーできます。

    ![astrorelayリンク](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

3. このリンクをOpenVPN構成の**リモート**の後に置き、**":"**をスペースに置き換えます。その後、修正された構成をOpenVPNクライアントアプリで使用できます。

    ![openvpn構成にリンクを置き換える](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

4. 自宅やオフィスにいない場合でも、上記で作成した構成を使用してOpenVPNクライアントアプリを利用し、自宅やオフィスのローカルサービスにアクセスできます。

    ![openvpn起動](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}