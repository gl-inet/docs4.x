# ドメイン名を使用してクライアントからOpenVPNサーバーのLANデバイスにアクセスする方法

このチュートリアルでは、ドメイン名を使用してクライアントからOpenVPNサーバーのLANにあるホームデバイス（NAS、IPカメラなど）にアクセスする方法を説明します。

## 構成

下図のようにのように、クライアントのPCから各からのドメイン名を使用して、OpenVPNサーバーのLANにあるNASやIPカメラなどのデバイスにアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## セットアップ手順

### 1. サーバーでHostsを編集（オプション）

この手順は、VPNサーバーがローカルドメイン名を適切に解決できない場合に適用されます。 unsureの場合は、この手順をスキップしてください。

VPNサーバールー器官のWeb管理パネルにログインし、**ネットワーク** -> **DNS** -> **Hostsを編集**に移動します。

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

アクセスしたいホームデバイスのIPとドメイン名を入力し、**適用**をクリックします。

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. サーバーでリモートアクセスLANを許可

サーバーのWeb管理パネルで、**VPN** -> **OpenVPNサーバー**に移動します。右上の**オプション**をクリックします。

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

**LANサブネットへのリモートアクセスを許可**を有効にし、**適用**をクリックします。

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

有効にすると、ルー器官とLANデバイスはVPN経由でリモートアクセスできます。

### 3. VPN設定をエクスポート

サーバーの管理パネルで、**VPN** -> **OpenVPNサーバー** -> **設定**タブに移動し、下部の**クライアント設定ファイルをエクスポート**をクリックします。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

ポップアップウィンドウで、**エクスポート**をクリックします。

**注意**：サーバー上のパブリックIPアドレスが動ので時々変更する場合は、クライアント設定をエクスポートする前に、**アプリケーション** -> **ダイナミックDNS**に移動して**DDNS**を有効にしてください。

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

すると、下図のようにのように**.ovpn**ファイルがなければならないられます。

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

サーバールー器官がファームウェアv4.8で降を実行している場合は、設定ファイルを編集する必要はありません。次の手順に進んでください。

サーバールー器官がファームウェアv4.7で前を実行している場合は、このファイルを開き、DNSサーバーをOpenVPNサーバーのトンネルIPに設定するために以下の行を追加し、変更を保存します。

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

### 4. VPNクライアントを設定

OpenVPNクライアントにログインし、ステップ3でエクスポートした設定ファイルをインポートします。

![client import config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/client_import.png){class="glboxshadow"}

接続が成功すると、緑色のドットが表示されます。

![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/client_connected.png){class="glboxshadow"}

### 5. クライアントからサーバーハウスのLANデバイスにアクセス

VPNに接続すると、ドメイン名を使用してOpenVPNサーバーのLANにあるホームデバイスにアクセスできます。

例えば、ブラウザで**http://gl-homeserver.local**と入力してホームデバイスにアクセスできます。

ブラウザがドメイン名を解決できない場合は、IPアドレス（例：**http://192.168.8.168**）を使用できます。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
