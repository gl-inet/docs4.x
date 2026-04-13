# GL.iNet ルーターで WireGuard クライアントを設定する（ファームウェア v4.6 以前）

**Note**: このガイドはファームウェア v4.6 以前に適用されます。新しいバージョンについては [こちら](wireguard_client.md) を参照してください。

---

WireGuard® は、最先端の暗号技術を利用した、非常にシンプルで高速かつモダンな VPN です。IPsec よりも高速・簡潔・軽量で使いやすいことを目指しており、OpenVPN よりも大幅に高いパフォーマンスを期待できます。

すでにプロバイダーの WireGuard サービスを契約しているものの、設定ファイルの取得方法が分からない場合は、[WireGuard サービスプロバイダーから設定ファイルを取得する方法](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) を参照するか、プロバイダーのサポートへお問い合わせください。

WireGuard Client は、Web 管理パネルまたは [モバイルアプリ](../faq/mobile_app.md) から設定できます。

- モバイルアプリには、AzireVPN、Mullvad、OVPN、StrongVPN、PIA VPN など複数の WireGuard サービスプロバイダーが統合されています。

- Web 管理パネルでは対応している WireGuard サービスプロバイダーはやや少ないものの、より直感的で詳細な設定画面を利用できます。

以下では、Web 管理パネルから設定する手順を説明します。

---

Web 管理パネルにログインし、**VPN** -> **WireGuard Client** を開きます。

**AzireVPN** または **Mullvad** の契約がある場合は、その認証情報で直接ログインできます。手動で設定する場合は **Add Manually** をクリックして WireGuard プロファイルをアップロードします。

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## AzireVPN を設定する

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} は、WireGuard のような安全でモダンかつ堅牢なトンネルを提供する、プライバシー重視の VPN サービスです。

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. **Username** と **Password** を入力し、**Save Credentials & Get Servers** をクリックします。各サーバー用の設定ファイルが生成されます。

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. VPN Dashboard へ移動して接続を有効にします。

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    接続が確立すると、ユーザーの IP アドレスと送受信バイト数が表示されます。

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. サーバー一覧を更新します。

    AzireVPN 側でサーバーのメンテナンスや停止が行われると接続できなくなることがあります。**Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得できます。

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. 認証情報を編集します。

    歯車アイコンをクリックして認証情報を編集します。

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Mullvad を設定する

[Mullvad](https://mullvad.net/){target="_blank"} は、オンラインでの行動、個人情報、位置情報のプライバシー保護を支援する VPN サービスです。

ファームウェア 4.x には Mullvad WireGuard サービスが統合されています。

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. **Account** を入力し、**Save Credentials & Get Servers** をクリックします。

    Mullvad のアカウント番号は、`1000 0000 0000 0000` から `9999 9999 9999 9999` の範囲にある 16 桁の数字です。

    ロケーションを選択するダイアログが表示されます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    選択したロケーションのサーバー設定ファイルが生成されます。

    **Public Key** は Mullvad サーバーへ送信する WireGuard 公開鍵です。同時に最大 5 個のキーを持つことができ、WireGuard のキーは [Mullvad のページ](https://mullvad.net/en/account/#/ports){target="_blank"} で管理できます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. VPN Dashboard へ移動して接続を有効にします。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    接続が確立すると、ユーザーの IP アドレスと送受信バイト数が表示されます。

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. サーバー一覧を更新します。

    Mullvad 側でサーバーのメンテナンスや停止が行われると接続できなくなることがあります。**Update Servers** をクリックすると、最新の利用可能サーバー一覧を取得できます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. 認証情報を編集します。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. アカウント情報を削除します。

    **Delete** をクリックすると、アカウント認証情報、秘密鍵、公開鍵、および設定ファイルが **ルーター内から** 削除されます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. 削除します。

    すべての設定ファイルをワンクリックで削除でき、秘密鍵と公開鍵も削除するかどうかを確認するプロンプトが表示されます。

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## WireGuard Client を設定する

ファームウェア 4.0 以降では、WireGuard プロファイルをグループ化して管理できます。

1. **Add Manually** をクリックします。

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. グループが作成されます。

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. グループに分かりやすい名前（例: azirevpn）を付けます。その後、設定ファイルをアップロードするか、手動で設定を追加できます。

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        WireGuard 設定ファイルをアップロードし、**Apply** をクリックします。

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration**

        WireGuard 設定を貼り付けたい場合や、各項目を手動で入力したい場合はこちらを使用します。

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        分かりやすい名前を付けて設定を貼り付け、**Apply** をクリックして続行します。

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        または、各項目を入力して設定を追加することもできます。**Item Mode** をクリックします。

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. 三点アイコンをクリックすると、プロファイルの開始 / 編集 / 削除を行えます。

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. [VPN Dashboard](vpn_dashboard_v4.7.md) ページで接続状態を確認します。

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® は Jason A.Donenfeld の登録商標です。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
