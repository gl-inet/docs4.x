# ドメイン名を使ってクライアントからOpenVPNサーバー側LAN機器へアクセスする方法

このチュートリアルでは、クライアント側から OpenVPN サーバーの LAN 上にある家庭内機器（NAS、IP カメラなど）へ、ドメイン名を使ってアクセスする方法を説明します。

## ネットワーク構成

以下のように、クライアント側 LAN 上の PC から、それぞれのドメイン名を使って OpenVPN サーバー側 LAN にある NAS や IP カメラへアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## 設定手順

### 1. サーバー側で Hosts を編集する（任意）

この手順は、VPN サーバーがローカルドメイン名を正しく解決できない場合に必要です。必要かどうか分からない場合は、この手順はスキップしてください。

VPN サーバールーターの Web 管理パネルにログインし、**NETWORK** -> **DNS** -> **Edit Hosts** に移動します。

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

アクセスしたい家庭内機器の IP アドレスとドメイン名を入力し、**Apply** をクリックします。

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. サーバー側で LAN へのリモートアクセスを許可する

サーバーの Web 管理パネルで、**VPN** -> **OpenVPN Server** に移動し、右上の **Options** をクリックします。

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

**Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

有効にすると、VPN 経由でこのルーターおよび LAN 上の機器へリモートアクセスできるようになります。

### 3. VPN設定をエクスポートする

サーバーの管理パネルで、**VPN** -> **OpenVPN Server** -> **Configuration** タブに移動し、下部の **Export Client Configuration** をクリックします。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

ポップアップウィンドウで **Export** をクリックします。

**Note**: サーバーのパブリック IP アドレスが動的で、ときどき変更される場合は、クライアント設定をエクスポートする前に **APPLICATIONS** -> **Dynamic DNS** で **DDNS** を有効にしてください。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

すると、以下のような **.ovpn** ファイルが取得できます。

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

サーバールーターがファームウェア v4.8 以降の場合は、設定ファイルを編集する必要はありません。そのまま次の手順へ進んでください。

サーバールーターがファームウェア v4.7 以前の場合は、このファイルを開き、DNS サーバーを OpenVPN サーバーのトンネル IP に設定するために、以下の 1 行を追加して保存してください。

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

ヒント: OpenVPN サーバーのトンネル IPv4 サブネットは、下図のように OpenVPN Server ページの **Configuration** タブで確認できます。ファームウェアによって異なるため、実際のトンネル IP を確認してください。

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. VPNサーバーを有効にする

**OpenVPN Server** ページで、右上の **Start** ボタンをクリックしてサーバーを起動します。

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. VPN設定をアップロードする

VPN クライアントルーターの Web 管理パネルにログインし、**VPN** -> **OpenVPN Client** に移動して **Add Manually** をクリックします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

このグループの名前を設定し、設定ファイルをアップロードします。

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

アップロードが成功したら **Apply** をクリックします。

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

設定ファイルが一覧に表示されます。

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. VPNクライアント接続を開始する

三点アイコンをクリックして VPN 接続を開始します。

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

灰色のドットが緑色に変われば、OpenVPN クライアントは正常にサーバーへ接続できています。

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

これで、クライアント側 LAN の PC から、ドメイン名を使ってサーバー側 LAN の家庭内機器（NAS など）へアクセスできます。

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
