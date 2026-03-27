# AstroRelay経由でWireGuardサーバーを設定する方法

このチュートリアルでは、GL.iNet ルーターで AstroRelay 経由の WireGuard サーバーを設定する手順を紹介します。ISP からパブリック IP アドレスが提供されていない場合でも、自宅やオフィスのローカルサービスへリモートアクセスしたいユーザーに適しています。

[AstroRelay](https://www.astrorelay.com){target="\_blank"} は、安全なリバースプロキシトンネルを提供し、NAT やファイアウォールの背後にあるリソースへ安全にアクセスできます。

1.  [このガイド](../interface_guide/wireguard_server.md)に従って、パブリック IP アドレスがなくても GL.iNet ルーターで WireGuard サーバーを設定します。

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    その後、**Profiles** をクリックして WireGuard 設定ファイルをエクスポートします。以下は設定ファイルの例です。

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2.  （任意）VPN サーバーの LAN にリモートアクセスする必要がある場合は、**Allow Remote Access LAN** を有効にします。不要な場合はこの手順をスキップしてください。

    ??? "ファームウェア v4.7 以前の場合"

        サーバーの Web 管理画面で **VPN** -> **VPN Dashboard** -> **VPN Server** セクションに移動します。WireGuard Server の右側にある歯車アイコンをクリックします。

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        **Remote Access LAN** を有効にし、**Apply** をクリックします。

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **有効にすると、このルーターと LAN 内のデバイスへ VPN 経由でリモートアクセスできます。**

    ??? "ファームウェア v4.8 以降の場合"

        サーバーの Web 管理画面で **VPN** -> **WireGuard Server** に移動し、右上の **Options** をクリックします。

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **有効にすると、このルーターと LAN 内のデバイスへ VPN 経由でリモートアクセスできます。**

3.  AstroRelay アカウントを登録し、この[チュートリアル](https://www.astrorelay.com/tutorial.html){target="\_blank"}に従って初期設定を完了します。

    新しいドメインを追加する際は、ルーターに最も近いサーバーを選択してください。

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際は、ルーターの **LAN IP アドレス** を **Destination Host IP** フィールドに入力し、**Destination Port** フィールドに **51820** を入力します。

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    すると **wg_server_test.arlab1.cc:33331** のようなリンクが発行されます。クリックしてリンクをコピーしてください。

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4.  WireGuard 設定ファイルを開き、**Endpoint** の後ろの値を前の手順で取得したリンクに置き換えて変更を反映します。

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5.  WireGuard クライアントとして使用するデバイスに [WireGuard アプリ](https://www.wireguard.com/install/){target="\_blank"} をインストールします。次に、修正した設定ファイルをアプリへアップロードして接続を開始します。別の GL.iNet ルーターへアップロードして WireGuard クライアントとして設定することもできます。

    接続後は、自宅やオフィスのローカルサービスへリモートからアクセスできます。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
