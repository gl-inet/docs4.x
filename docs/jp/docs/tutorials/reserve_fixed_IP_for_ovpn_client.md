# 自作OpenVPN接続でOpenVPNクライアントに固定IPを予約する方法

このチュートリアルでは、OpenVPNサーバーへ接続するOpenVPNクライアントに固定IPを予約する方法を説明します。以下の手順を実行する前に、まず GL.iNet ルーターを OpenVPN Server として設定してください。

1. OpenVPN Server のWeb管理画面にログインし、左側のサイドバーで **VPN** -> **OpenVPN Server** に移動します。

   **Configuration** タブで **IPv4 subnet** を控えます。以下の画像では `10.8.0.0/24` です。続いて Authentication Mode を **Username and Password Only** に切り替えます。

   ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. **Users** タブへ移動し、以下のようにユーザー名とパスワードを作成します。

   ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. SSHでルーターへログインし、次のコマンドを実行して OpenVPN Server の設定スクリプトファイルを開きます。

   `vi /lib/netifd/proto/openserver.sh`

   開いたファイル内で、`client-config-dir /etc/openvpn/ccd` という行が存在するか確認します。

   ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

   存在しない場合は手動で追加し、ファイルを保存して終了してください。

4. `/etc/openvpn/` に移動し、`mkdir ccd` を実行して ccd フォルダーを作成します。

   ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. `GLsupport` という名前のファイルを作成し、`ifconfig-push 10.8.0.10 255.255.255.0` と入力して保存し、終了します。

   続いて `cat GLsupport` を実行して内容を確認します。

   ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}
   - `GLsupport` ユーザーで OpenVPN Server に接続すると、このユーザーには固定IP `10.8.0.10` が割り当てられます。
   - `255.255.255.0` はサブネットマスクです。必要に応じて、OpenVPN Server のサブネットマスクに置き換えてください。

   **Note**: 複数の OpenVPN クライアントに固定IPを割り当てたい場合は、手順2で複数のユーザー名とパスワードを作成し、手順5を繰り返して、ユーザー名ごとに CCD フォルダーへファイルを追加してください。たとえば `user_1`、`user_2`、`user_3` などのファイルを作成し、それぞれに `ifconfig-push` コマンドと対応する固定IPおよびサブネットマスクを記述します。

   例: `ifconfig-push 10.8.0.20 225.225.225.0`、`ifconfig-push 10.8.0.30 225.225.225.0`、`ifconfig-push 10.8.0.40 225.225.225.0`

6. 最後に、OVPNクライアントでテストし、Client Virtual IP (IPv4) が予約したIPアドレスになっているか確認します。

   たとえば、OpenVPN クライアントが GL.iNet ルーターであれば、そのWeb管理画面にログインし、VPN Dashboard へ移動して Client Virtual IP (IPv4) を確認できます。

   ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
   <small>(ファームウェア v4.7 以前の VPN Dashboard)</small>

   ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
   <small>(ファームウェア v4.8 の VPN Dashboard)</small>

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
