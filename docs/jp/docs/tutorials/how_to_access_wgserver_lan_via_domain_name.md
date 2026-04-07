# ドメイン名を使用してクライアントから WireGuard サーバーの LAN デバイスにアクセスする方法

このチュートリアルでは、クライアントから、WireGuard サーバーの LAN 上にある家庭内デバイス（NAS、IP カメラなど）へドメイン名を使ってアクセスする方法を説明します。

## トポロジー

以下のように、クライアント側 LAN の PC から、それぞれのドメイン名を使って WireGuard サーバー側 LAN の NAS や IP カメラなどのデバイスにアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## 設定手順

### 1. サーバー側で Hosts を編集する（任意）

この手順は、VPN サーバーがローカルのドメイン名を正しく解決できない場合に行います。必要かどうかわからない場合は、この手順をスキップしてください。

VPN サーバールーターの Web 管理画面にログインし、**NETWORK** -> **DNS** -> **Edit Hosts** に移動します。

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

アクセスしたい家庭内デバイスの IP アドレスとドメイン名を入力し、**Apply** をクリックします。

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. サーバー側で LAN へのリモートアクセスを許可する

??? "ファームウェア v4.8 のサーバールーターの場合"

    サーバーの Web 管理画面で、**VPN** -> **WireGuard Server** に移動し、右上の **Options** をクリックします。

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    **Allow Remote Access the LAN Subnet** を有効にして、**Apply** をクリックします。

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **有効にすると、このルーターおよび LAN 上のデバイスに VPN 経由でリモートアクセスできるようになります。**

??? "ファームウェア v4.7 以前のサーバールーターの場合"

    サーバーの Web 管理画面で、**VPN** -> **VPN Dashboard** -> **VPN Server** セクションに移動し、WireGuard サーバー右側の歯車アイコンをクリックします。

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    **Remote Access LAN** を有効にして、**Apply** をクリックします。

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **有効にすると、このルーターおよび LAN 上のデバイスに VPN 経由でリモートアクセスできるようになります。**

### 3. VPN 設定をエクスポートする

サーバーの管理画面で、**VPN** -> **WireGuard Server** -> **Profiles** タブに移動し、**Add** をクリックして設定プロファイルをエクスポートします。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

すると、以下のような **.conf** ファイルが取得されます。

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

このファイルを開き、DNS フィールドがサーバーのトンネル IP を参照していることを確認してください。サーバーのトンネル IP は、下図のように **WireGuard Server** ページの **Configuration** タブに表示されます。また、DNS 解決エラーを防ぐため、DNS フィールドに `64.6.64.6` が含まれている場合は削除してください。

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Note**: WireGuard サーバーのトンネル IP はファームウェアのバージョンによって異なります。サーバーで実際に使われているトンネル IP を確認してください。

### 4. VPN サーバーを有効にする

**WireGuard Server** ページで、右上の **Start** ボタンをクリックしてサーバーを起動します。

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. VPN 設定をアップロードする

VPN クライアントルーターの Web 管理画面にログインし、**VPN** -> **WireGuard Client** に移動して、**Add Manually** をクリックします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

このグループの名前を作成し、設定ファイルをアップロードします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

アップロードに成功したら、**Apply** をクリックします。

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

設定ファイルがここに一覧表示されます。

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. VPN クライアント接続を開始する

三点アイコンをクリックして VPN 接続を開始します。

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

灰色のドットが緑色に変われば、WireGuard クライアントは正常にサーバーへ接続されています。

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

これで、クライアント側 LAN の PC から、ドメイン名を使ってサーバー側 LAN 上の家庭内デバイス（NAS など）にアクセスできます。

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

まだご不明な点がありますか？ [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
