# WireGuardサーバ LAN機器にドメイン名を使用してクライアントからアクセスする方法

このチュートリアルでは、ドメイン名を使用してクライアントからWireGuardサーバーのLANにある家庭内機器（NAS、IPカメラなど）にアクセスする方法について説明します。

## ネットワーク構成

下図のように client's LAN上のPCから、それぞれのドメイン名を使用してWireGuardサーバーのLAN上にあるNASやIPカメラなどのデバイスにアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## 設定手順

### 1. サーバーでのHostsの編集（オプション）

このステップは、VPNサーバーがローカルドメイン名を適切に解決できない場合に適用します。不確実な場合はこのステップをスキップしてください。

VPNサーバールーターのWeb管理パネルにログインし、**NETWORK** -> **DNS** -> **Edit Hosts**に移動します。

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

アクセスしたい家庭内デバイスのIPとドメイン名を入力し、**Apply**をクリックします。

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. サーバーでリモートアクセスLANを許可

??? "ファームウェアv4.8を実行しているサーバーの場合"

    サーバーのWeb管理パネルで、**VPN** -> **WireGuard Server**に移動します。右上隅の**Options**をクリックします。

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    **Allow Remote Access the LAN Subnet**を有効化し、**Apply**をクリックします。

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **有効にすると、このルーターとLANデバイスにVPN経よりでリモートアクセスできます。**
 
??? "ファームウェアv4.7で前のサーバールーターの場合"

    サーバーのWeb管理パネルで、**VPN** -> **VPN Dashboard** -> **VPN Server**セクションに移動します。WireGuardサーバーの右側にある歯車アイコンをクリックします。

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    **Remote Access LAN**を有効化し、**Apply**をクリックします。

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **有効にすると、このルーターとLANデバイスにVPN経よりでリモートアクセスできます。**

### 3. VPN設定のエクスポート

サーバーの管理パネルで、**VPN** -> **WireGuard Server** -> **Profiles**タブに移動し、**Add**をクリックして設定プロファイルをエクスポートします。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

で下のとおり**設定ファイル**を取なければならないできます。

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

このファイルを開きます。ファイル内のDNSフィールドが、WireGuard Serverページの**Configuration**タブに表示されるサーバーのトンネルIPを指していることを確認します。DNS解決の失敗を避けるため、DNSフィールドに「64.6.64.6」があれば削除してください。

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**注意**：WireGuardサーバーのトンネルIPはファームウェアバージョンによって異なります。サーバーのトンネルIPを確認してください。

### 4. VPNサーバーの有効化

**WireGuard Server**ページで、右上隅の**Start**ボタンをクリックしてサーバーを起動します。

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. VPN設定のアップロード

VPNクライアントルー器のWeb管理パネルにログインし、**VPN** -> **WireGuard Client**に移動し、**Add Manually**をクリックします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

このグループの名前を作成し、設定ファイルをアップロードします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

アップロード成功。**Apply**をクリックします。

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

ここに設定ファイルが一覧表示されます。

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. VPNクライアント接続の開始

3時アイコンをクリックしてVPN接続を開始します。

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

灰色ドットが緑色に変わると、WireGuardクライアントは正常にサーバーに接続されています。

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

これによりクライアントのLAN上のPCから、ドメイン名を使用してサーバーのLAN上の家庭内デバイス（NASなど）にアクセスできます。

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
