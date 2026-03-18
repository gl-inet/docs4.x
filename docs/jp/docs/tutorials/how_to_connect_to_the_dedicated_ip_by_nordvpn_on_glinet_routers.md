# GL.iNetルーターでNordVPNのDedicated IPに接続する方法

この記事では、NordVPNのDedicated IPを設定する手順を紹介します。

ここでは GL-AXT1800 を例に説明します。

1. Nord Account にログインし、Dedicated IP の情報を確認します。下図の例では、割り当てられたIPアドレスは **193.32.211.142**、サーバー情報は **United Kingdom #1625** です。

   ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/){target="\_blank"} にアクセスし、**United Kingdom #1625** の設定ファイルを探します。必要に応じてUDPまたはTCPの設定ファイルをダウンロードしてください。

   ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Nord Account のページへ戻り、Manual setup に進んで **Set up NordVPN Manually** をクリックし、サービス認証情報を確認します。

   ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

   ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. ルーターのWeb管理画面にログインし、**VPN** > **OpenVPN Client** に移動します。新しいグループを作成して、手順2でダウンロードした設定ファイルをアップロードします。続いて、手順3で確認したサービス認証情報を入力します。

   ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

5. **VPN Dashboard** に移動し、設定ファイルを選択して **Apply** をクリックし、接続します。

   ![connect nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/connect_nordvpn_on_glinet_router.png){class="glboxshadow"}

6. 接続後、[https://whatismyipaddress.com/](https://whatismyipaddress.com/){target="\_blank"} で現在のパブリックIPアドレスを確認し、NordVPNのDedicated IPと一致しているか確認します。

   ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
