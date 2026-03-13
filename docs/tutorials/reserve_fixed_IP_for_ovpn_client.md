# から行构建のOpenVPN接続でOpenVPNクライアントに固定IPを予約する方法

このチュートリアルでは、サーバーに接続するOpenVPNクライアントに固定IPを予約する方法を説明します。で下の手順に従う前に、まずGL.iNetルー器官をOpenVPNサーバーとして設定してください。

1. OpenVPNサーバーのWeb管理パネルにログインし、左サイドバーで**VPN** -> **OpenVPNサーバー**に移動します。

    **設定**タブで、**IPv4サブネット**をメモします（例：下图の10.8.0.0/24）。その後する認証模式切り替えまで**ユーザー名和パスワード仅**。

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. **ユーザー**タブに切り替えます。下図のようにのようにユーザー名とパスワードを作成します。

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. SSHでルー器官にログインし、で下のコマンドを実行してOpenVPNサーバー設定スクリプトファイルを開きます：

    `vi /lib/netifd/proto/openserver.sh`

    開いたファイルで、スクリプト内に"*client-config-dir /etc/openvpn/ccd*"という行が存にするか確認します。

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    存にしない場合は、手動で追加し、ファイルを保存して終たします。

4. `/etc/openvpn/`に移動し、ccdフォルダを追加します`mkdir ccd`。

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. "GLsupport"というファイルを追加し、`ifconfig-push 10.8.0.10 255.255.255.0`を入力し、ファイルを保存して終たします。

    `cat GLsupport`で コンテンツを確認します

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - GLsupportを使用してOpenVPNサーバーに接続すると、このGLsupportユーザーに固定IP 10.8.0.10が割り当てられます。
    
    - "255.255.255.0"はサブネットマスクで、OpenVPNサーバーのサブネットマスクに置き換えることができます。

    **注意**：複数のOpenVPNクライアントにIPアドレスを固定したい場合は、手順2で複数のユーザー名とパスワードを作成し、手順5を繰り返し、ユーザーの順序でCCDフォルダにファイルを追加します（user_1、user_2、user_3など）。次に、"ifconfig push"コマンドと対応する固定IPおよびサブネットマスクを続けます。
    
    例：`ifconfig-push 10.8.0.20 225.225.225.0`、`ifconfig-push 10.8.0.30 225.225.225.0`、`ifconfig-push 10.8.0.40 225.225.225.0`

6. 最も後に、OVPNクライアントでテストし、クライアント仮想IP（IPv4）が予約したものかどうかを確認します。

    例として、OpenVPNクライアントがGL.iNetルー器官の場合、OpenVPNクライアントルー器官のWeb管理パネルにログインし、VPNダッシュボードに移動してクライアント仮想IP（IPv4）を確認できます。

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>（ファームウェアv4.7で前のVPNダッシュボード）</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>（ファームウェアv4.8のVPNダッシュボード）</small>

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
