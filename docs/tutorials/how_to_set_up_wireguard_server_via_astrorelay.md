# AstroRelayを使ってWireGuardサーバーを設定する方法

シナリオ: GL.iNetルーターを使用して自宅/オフィスのローカルサービスにリモートアクセスするためにWireGuardサーバーを設定したいが、ISPがパブリックIPアドレスを提供していない場合。

[AstroRelay](https://www.astrorelay.com){target="_blank"}は、安全なリバースプロキシトンネルを提供し、NATおよびファイアウォールの背後にあるリソースにアクセスすることができます。

1. パブリックIPアドレスがなくても、WireGuardサーバーを設定するためのガイドに従ってください。[ガイドはこちら](../interface_guide/wireguard_server.md)。**ローカルネットワークへのアクセスを許可する**を有効にしてください。

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    次に、WireGuardの設定を作成します。以下の画像はその例です。

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. AstroRelayのアカウントにサインアップし、[チュートリアル](https://www.astrorelay.com/tutorial.html){target="_blank"}に従ってください。

    新しいドメインを追加する際には、ルーターに最も近いサーバーを選択してください。

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際には、**Destination Host IP**にルーターのIPアドレス（デフォルトは**192.168.8.1**）を入力してください。

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    最終的に、**wg_server_test.arlab1.cc:33331**のようなリンクを取得できます。

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

3. このリンクをWireGuard設定の**Endpoint**に置き換えてください。その後、WireGuardクライアントアプリで修正された設定を使用できます。

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

4. 自宅やオフィスの外にいるときでも、上記で作成した設定を使用してWireGuardクライアントアプリを使用することで、自宅やオフィスにいるようにローカルサービスにアクセスできます。