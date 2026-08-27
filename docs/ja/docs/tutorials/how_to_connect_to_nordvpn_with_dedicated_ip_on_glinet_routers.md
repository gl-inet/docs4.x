# GL.iNetルーターでNordVPNのDedicated IPに接続する方法

この記事では、GL.iNet ルーターで NordVPN の Dedicated IP 接続を設定する手順を紹介します。

ここでは GL-AXT1800 を例に説明します。

1. Nord Account にログインし、Dedicated IP の詳細を確認します。以下の例では、割り当てられた IP アドレスは **193.32.211.142**、サーバーは **United Kingdom #1625** です。

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) にアクセスし、**United Kingdom #1625** の設定ファイルを探します。UDP または TCP の設定ファイルをダウンロードしてください。

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Nord Account ページに戻り、**Manual Setup** に進んで **Set up NordVPN Manually** をクリックし、**service credentials** を取得します。

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. ルーターの Web 管理画面にログインし、**VPN** > **OpenVPN Client** に移動します。新しいグループを作成し、手順 2 でダウンロードした設定ファイルをアップロードしてから、手順 3 で取得した service credentials を入力します。

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    上図のように、有効な設定ファイルが検出されます。NordVPN の service credentials を入力してください。

5. 右側の三点アイコンをクリックして接続します。あるいは **VPN Dashboard** に移動し、設定ファイルを選択して **Apply** をクリックして接続することもできます。

6. 接続後、[こちら](https://whatismyipaddress.com/) でパブリック IP アドレスを確認し、NordVPN の Dedicated IP と一致しているか確認します。

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
