# GL.iNetルーターでNordVPNの専用IPに接続する方法

この記事では、NordVPNの専用IPを設定する手順を紹介します。ここではGL-AXT1800を例にしていますが、他のモデルも同様です。

1. Nordアカウントにログインして、専用IP情報を確認します。以下の画像のように、割り当てられたIPは**193.32.211.142**で、サーバ情報は**United Kingdom #1625**です。

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. このリンクにアクセスします: [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) そして**United Kingdom #1625**の設定ファイルを見つけます。ここでは**uk1625.nordvpn.com**です。UDPまたはTCPの設定ファイルをダウンロードします。

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Nordアカウントページに戻り、マニュアル設定に進み、**Set up NordVPN Manually**をクリックしてサービス認証情報を取得します。

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. ルーターのWeb管理パネルにログインし、VPN > OpenVPN Clientに進み、新しいグループを作成して、ステップ2でダウンロードした設定ファイルをアップロードします。その後、ステップ3で取得したサービス認証情報を入力します。

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

5. VPNダッシュボードに進み、設定ファイルを選択して**適用**をクリックして接続します。

    ![connect nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/connect_nordvpn_on_glinet_router.png){class="glboxshadow"}

6. 接続が完了したら、このウェブサイトにアクセスして公開IPを確認します: [https://whatismyipaddress.com/](https://whatismyipaddress.com/) そして、NordVPNの専用IPと一致するか確認します。

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}にアクセスしてください。