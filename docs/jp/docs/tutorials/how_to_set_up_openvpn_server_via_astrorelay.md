# AstroRelay経由でOpenVPNサーバーを設定する方法

このチュートリアルでは、GL.iNetルーターでAstroRelay経由のOpenVPNサーバーを設定する手順を紹介します。ISPからパブリックIPアドレスが提供されていないものの、自宅やオフィスのローカルサービスへリモートアクセスしたいユーザーに適しています。

[AstroRelay](https://www.astrorelay.com){target="_blank"} は安全なリバースプロキシトンネルを提供し、NATやファイアウォールの内側にあるリソースへ安全にアクセスできます。

1. [このガイド](../interface_guide/openvpn_server.md)を参照して、パブリックIPアドレスがなくてもGL.iNetルーターにOpenVPNサーバーを設定します。

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    その後、OpenVPN設定をエクスポートします。以下は設定ファイルの例です。

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. （任意）VPNサーバーのLANへリモートアクセスする必要がある場合は、**Allow Remote Access LAN** を有効にします。不要であればこの手順はスキップしてください。

    ??? "ファームウェア v4.7 以前"

        1. 左側のサイドバーで **VPN** > **VPN Dashboard** をクリックします。
        2. Optionsアイコンをクリックします。
        3. **Remote Access LAN** をオンにします。
        4. **Apply** をクリックします。

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "ファームウェア v4.8 以降"

        1. 左側のサイドバーで **VPN** > **OpenVPN Server** をクリックします。
        2. 右上の **Options** をクリックします。
        3. **Allow Remote Access the LAN Subnet** をオンにします。
        4. **Apply** をクリックします。

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. AstroRelayアカウントを登録し、この[チュートリアル](https://www.astrorelay.com/tutorial.html){target="_blank"}に従って初回設定を完了します。

    新しいドメインを追加する際は、ルーターに最も近いサーバーを選択してください。

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際は、**Destination Host IP** フィールドにルーターの **LAN IP address** を入力し、**Destination Port** フィールドに **1194** を入力します。

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    すると、**testforx3000.arlab1.cc:37202** のようなリンクが発行されます。クリックしてコピーしてください。

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. OpenVPN設定ファイルを開き、**Remote** の後ろにある値を前の手順で取得したリンクに置き換えます。以下の例では、"42.200.00.00 1194" を "testforx3000.arlab1.cc:37202" に置き換えています。その後、コロン ":" をスペースに置き換えて変更を保存します。

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. OpenVPNクライアントとして使いたいデバイスに [OpenVPN Connectアプリ](https://openvpn.net/client/){target="_blank"} をインストールします。次に、変更した設定ファイルをアプリにアップロードして接続を開始します。別のGL.iNetルーターにアップロードして、OpenVPNクライアントとして設定することもできます。

    接続が完了すると、自宅やオフィスのローカルサービスへリモートアクセスできるようになります。

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
