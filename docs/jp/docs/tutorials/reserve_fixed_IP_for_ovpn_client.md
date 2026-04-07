# 自作OpenVPN接続でOpenVPNクライアント用に固定IPを予約する方法

このチュートリアルでは、サーバーへ接続するOpenVPNクライアントに固定IPを予約する方法を紹介します。以下の手順を実行する前に、まずGL.iNetルーターをOpenVPNサーバーとして設定してください。

1. OpenVPNサーバーのWeb管理パネルにログインし、左側のサイドバーから **VPN** -> **OpenVPN Server** に移動します。

    **Configuration** タブで **IPv4 subnet**（下の画像では 10.8.0.0/24 など）を控え、Authentication Mode を **Username and Password Only** に切り替えます。

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. **Users** タブに切り替え、以下のようにユーザー名とパスワードを作成します。

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. ルーターへSSHログインし、次のコマンドを実行してOpenVPNサーバー設定スクリプトファイルを開きます。

    `vi /lib/netifd/proto/openserver.sh`

    開いたファイル内で、スクリプトに "*client-config-dir /etc/openvpn/ccd*" という行が存在するか確認します。

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    存在しない場合は手動で追加し、保存して終了します。

4. `/etc/openvpn/` に移動し、`mkdir ccd` で ccd フォルダーを作成します。

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. "GLsupport" というファイルを追加し、`ifconfig-push 10.8.0.10 255.255.255.0` と入力して保存・終了します。

    `cat GLsupport` で内容を確認します。

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - GLsupport でOpenVPNサーバーに接続すると、この GLsupport ユーザーには固定IP 10.8.0.10 が割り当てられます。

    - "255.255.255.0" はサブネットマスクです。OpenVPNサーバーのサブネットマスクに置き換えることもできます。

    **Note**: 複数のOpenVPNクライアントに固定IPを設定したい場合は、Step 2 で複数のユーザー名とパスワードを作成し、その後 Step 5 を繰り返して、CCDフォルダーに user_1、user_2、user_3 のようにユーザーごとのファイルを追加し、それぞれに "ifconfig push" コマンドと対応する固定IPおよびサブネットマスクを記述してください。

    例: `ifconfig-push 10.8.0.20 225.225.225.0`、`ifconfig-push 10.8.0.30 225.225.225.0`、`ifconfig-push 10.8.0.40 225.225.225.0`

6. 最後に、OVPNクライアントで接続テストを行い、クライアント仮想IP (IPv4) が予約したIPになっているか確認します。

    たとえば、OpenVPNクライアントがGL.iNetルーターであれば、OpenVPNクライアントルーターのWeb管理パネルにログインし、VPN Dashboard に移動してクライアント仮想IP (IPv4) を確認できます。

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(ファームウェア v4.7 以前の VPN Dashboard)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(ファームウェア v4.8 の VPN Dashboard)</small>

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
