# ドメイン名を使ってクライアントからWireGuardサーバー側LAN機器へアクセスする方法

このチュートリアルでは、クライアント側から WireGuard サーバーの LAN 上にある家庭内機器（NAS、IP カメラなど）へ、ドメイン名を使ってアクセスする方法を説明します。

## ネットワーク構成

以下のように、クライアント側 LAN 上の PC から、それぞれのドメイン名を使って WireGuard サーバー側 LAN にある NAS や IP カメラへアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## 設定手順

### 1. サーバー側で Hosts を編集する（任意）

この手順は、VPN サーバーがローカルドメイン名を正しく解決できない場合に必要です。必要かどうか分からない場合は、この手順はスキップしてください。

VPN サーバールーターの Web 管理パネルにログインし、**NETWORK** -> **DNS** -> **Edit Hosts** に移動します。

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

アクセスしたい家庭内機器の IP アドレスとドメイン名を入力し、**Apply** をクリックします。

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. サーバー側で LAN へのリモートアクセスを許可する

??? "ファームウェア v4.8 のサーバールーターの場合"

    サーバーの Web 管理パネルで、**VPN** -> **WireGuard Server** に移動し、右上の **Options** をクリックします。

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **有効にすると、VPN 経由でこのルーターおよび LAN 上の機器へリモートアクセスできるようになります。**

??? "ファームウェア v4.7 以前のサーバールーターの場合"

    サーバーの Web 管理パネルで、**VPN** -> **VPN Dashboard** -> **VPN Server** セクションに移動し、WireGuard サーバー右側の歯車アイコンをクリックします。

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    **Remote Access LAN** を有効にし、**Apply** をクリックします。

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **有効にすると、VPN 経由でこのルーターおよび LAN 上の機器へリモートアクセスできるようになります。**

### 3. VPN設定をエクスポートする

サーバーの管理パネルで、**VPN** -> **WireGuard Server** -> **Profiles** タブに移動し、**Add** をクリックして設定プロファイルをエクスポートします。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

すると、以下のような **.conf** ファイルが取得できます。

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

このファイルを開き、DNS フィールドが WireGuard Server ページの **Configuration** タブに表示されているサーバーのトンネル IP を指していることを確認してください。DNS 解決エラーを避けるため、DNS フィールドに `64.6.64.6` が含まれている場合は削除します。

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Note**: WireGuard サーバーのトンネル IP はファームウェアのバージョンによって異なります。実際のサーバーのトンネル IP を確認してください。

### 4. VPNサーバーを有効にする

**WireGuard Server** ページで、右上の **Start** ボタンをクリックしてサーバーを起動します。

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. VPN設定をアップロードする

VPN クライアントルーターの Web 管理パネルにログインし、**VPN** -> **WireGuard Client** に移動して **Add Manually** をクリックします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

このグループの名前を設定し、設定ファイルをアップロードします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

アップロードが成功したら **Apply** をクリックします。

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

設定ファイルが一覧に表示されます。

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. VPNクライアント接続を開始する

三点アイコンをクリックして VPN 接続を開始します。

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

灰色のドットが緑色に変われば、WireGuard クライアントは正常にサーバーへ接続できています。

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

これで、クライアント側 LAN の PC から、ドメイン名を使ってサーバー側 LAN の家庭内機器（NAS など）へアクセスできます。

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
