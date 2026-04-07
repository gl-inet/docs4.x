# AstroRelay経由でWireGuardサーバーを設定する方法

このチュートリアルでは、GL.iNetルーターでAstroRelay経由のWireGuardサーバーを設定する手順を紹介します。ISPからパブリックIPアドレスが提供されていないものの、自宅やオフィスのローカルサービスへリモートアクセスしたいユーザーに適しています。

[AstroRelay](https://www.astrorelay.com){target="_blank"} は安全なリバースプロキシトンネルを提供し、NATやファイアウォールの内側にあるリソースへ安全にアクセスできます。

1. [このガイド](../interface_guide/wireguard_server.md)を参照して、パブリックIPアドレスがなくてもGL.iNetルーターにWireGuardサーバーを設定します。

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    次に、**Profiles** をクリックしてWireGuard設定をエクスポートします。以下は設定ファイルの例です。

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. （任意）VPNサーバーのLANへリモートアクセスする必要がある場合は、**Allow Remote Access LAN** を有効にします。不要であればこの手順はスキップしてください。

    ??? "ファームウェア v4.7 以前"

        サーバーのWeb管理パネルで、**VPN** -> **VPN Dashboard** -> **VPN Server** セクションに移動します。WireGuardサーバーの右側にある歯車アイコンをクリックします。

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        **Remote Access LAN** を有効にし、**Apply** をクリックします。

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **有効にすると、このルーターとLAN内デバイスへVPN経由でリモートアクセスできます。**

    ??? "ファームウェア v4.8 以降"

        サーバーのWeb管理パネルで、**VPN** -> **WireGuard Server** に移動します。右上の **Options** をクリックします。

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **有効にすると、このルーターとLAN内デバイスへVPN経由でリモートアクセスできます。**

3. AstroRelayアカウントを登録し、この[チュートリアル](https://www.astrorelay.com/tutorial.html){target="_blank"}に従って初回設定を完了します。

    新しいドメインを追加する際は、ルーターに最も近いサーバーを選択してください。

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    新しいリンクを追加する際は、**Destination Host IP** フィールドにルーターの **LAN IP address** を入力し、**Destination Port** フィールドに **51820** を入力します。

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    すると、**wg_server_test.arlab1.cc:33331** のようなリンクが発行されます。クリックしてコピーしてください。

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. WireGuard設定ファイルを開き、**Endpoint** の後ろにある値を前の手順で取得したリンクに置き換えて、変更を保存します。

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. WireGuardクライアントとして使いたいデバイスに [WireGuardアプリ](https://www.wireguard.com/install/){target="_blank"} をインストールします。次に、変更した設定ファイルをアプリにアップロードして接続を開始します。別のGL.iNetルーターにアップロードして、WireGuardクライアントとして設定することもできます。

    接続が完了すると、自宅やオフィスのローカルサービスへリモートアクセスできるようになります。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
