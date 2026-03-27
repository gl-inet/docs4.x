# AstroRelay経由でOpenVPNサーバーを設定する方法

このチュートリアルでは、GL.iNet ルーターで AstroRelay 経由の OpenVPN サーバーを設定する手順を紹介します。ISP からパブリック IP アドレスが提供されていない場合でも、自宅やオフィスのローカルサービスへリモートアクセスしたいユーザーに適しています。

[AstroRelay](https://www.astrorelay.com){target="\_blank"} は、安全なリバースプロキシトンネルを提供し、NAT やファイアウォールの背後にあるリソースへ安全にアクセスできます。

1.  [このガイド](../interface_guide/openvpn_server.md)に従って、パブリック IP アドレスがなくても GL.iNet ルーターで OpenVPN サーバーを設定します。

    ![openvpnサーバーを設定](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    その後、OpenVPN 設定ファイルをエクスポートします。以下は設定ファイルの例です。

    ![openvpn構成](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2.  （任意）VPN サーバーの LAN にリモートアクセスする必要がある場合は、**Allow Remote Access LAN** を有効にします。不要な場合はこの手順をスキップしてください。

    ??? "ファームウェア v4.7 以前の場合"

        1. 左側のサイドバーで **VPN** > **VPN Dashboard** をクリックします。
        2. オプションアイコンをクリックします。
        3. **Remote Access LAN** のスイッチをオンにします。
        4. **Apply** をクリックします。

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "ファームウェア v4.8 以降の場合"

        1. 左側のサイドバーで **VPN** > **OpenVPN Server** をクリックします。
        2. 右上の **Options** をクリックします。
        3. **Allow Remote Access the LAN Subnet** のスイッチをオンにします。
        4. **Apply** をクリックします。

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3.  AstroRelay アカウントを登録し、この[チュートリアル](https://www.astrorelay.com/tutorial.html){target="\_blank"}に従って初期設定を完了します。

    新しいドメインを追加する際は、ルーターに最も近いサーバーを選択してください。

    ![astrorelay 新しいドメインを追加](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際は、ルーターの **LAN IP アドレス** を **Destination Host IP** フィールドに入力し、**Destination Port** フィールドに **1194** を入力します。

    ![openvpnサーバーのリンク](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    すると **testforx3000.arlab1.cc:37202** のようなリンクが発行されます。クリックしてリンクをコピーしてください。

    ![astrorelayリンク](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4.  OpenVPN 設定ファイルを開き、**Remote** の後ろの値を前の手順で取得したリンクに置き換えます。以下の例では、"42.200.00.00 1194" を "testforx3000.arlab1.cc:37202" に置き換えます。その後、コロン ":" を半角スペースに置き換えて変更を反映します。

    ![openvpn構成](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![openvpn構成にリンクを置き換える](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5.  OpenVPN クライアントとして使用するデバイスに [OpenVPN Connect アプリ](https://openvpn.net/client/){target="\_blank"} をインストールします。次に、修正した設定ファイルをアプリへアップロードして接続を開始します。別の GL.iNet ルーターへアップロードして OpenVPN クライアントとして設定することもできます。

    接続後は、自宅やオフィスのローカルサービスへリモートからアクセスできます。

    ![openvpn起動](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
