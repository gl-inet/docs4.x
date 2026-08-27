# サーバー側からWireGuardクライアントのLAN側へアクセスする方法

このチュートリアルでは、WireGuardサーバー側から、WireGuardクライアントのLANサブネット（IPカメラ、NAS など）へアクセスする手順を紹介します。

## トポロジー

以下の図のように、GL-MT2500 がWireGuardサーバー、GL-AXT1800 が接続先のWireGuardクライアントです。サーバー側から GL-AXT1800 のLAN側にあるデバイス（IPカメラやNASなど）へアクセスできます。

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. サーバーでルートルールを追加する

??? "ファームウェア v4.7 以前"

    <u>WireGuardサーバー側</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Server** に移動します。

    右側のルートアイコンをクリックしてルートルール画面に入ります。

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    右上の **Add Route Rule** をクリックし、アクセスしたいサブネットを入力します。

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    たとえば、WireGuardクライアント GL-AXT1800 のLANサブネットが **192.168.8.0/24** の場合、Target Address は **192.168.8.0/24** です。

    Gateway には、WireGuardサーバーがこのWireGuardクライアント向けに生成したクライアントIPを指定します。これは **WireGuard Server** ページの **Profiles** タブで確認できます。下図では、WireGuardクライアント GL-AXT1800 のクライアントIPは **10.0.0.4** です。

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    したがって、Gateway を **10.0.0.4**、Scope を **global** に設定し、**Apply** をクリックします。

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "ファームウェア v4.8 以降"

    <u>WireGuardサーバー側</u>のWeb管理パネルにログインし、**VPN** -> **WireGuard Server** に移動します。

    **Route Rules** タブをクリックし、右側の **Add Route Rule** をクリックします。

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    ポップアップウィンドウで、アクセスしたいサブネットを入力します。

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    たとえば、WireGuardクライアント GL-AXT1800 のLANサブネットが **192.168.8.0/24** の場合、Target Address は **192.168.8.0/24** です。

    Gateway には、WireGuardサーバーがこのWireGuardクライアント向けに生成したクライアントIPを指定します。これは同じページの **Profiles** タブで確認できます。下図では、WireGuardクライアント GL-AXT1800 のクライアントIPは **10.1.0.2** です。

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    したがって、Gateway を **10.1.0.2** に設定し、**Apply** をクリックします。

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. クライアントLANへのリモートアクセスを許可する

??? "ファームウェア v4.7 以前"

    <u>WireGuardクライアント側</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動します。

    WireGuard の右側にある歯車アイコンをクリックします。

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Remote Access LAN** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "ファームウェア v4.8 以降"

    <u>WireGuardクライアント側</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** に移動します。

    VPNトンネル左上の歯車アイコンをクリックして、トンネルオプションを開きます。

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. 接続をテストする

サーバー側からWireGuardクライアントのLANデバイスへアクセスできるかテストします。

ping でテストできます。たとえば、WireGuardサーバー（GL-MT2500）に接続されたデバイスから、WireGuardクライアント（GL-AXT1800）のLAN内デバイスのIPアドレスへ ping を送信し、正常に応答するか確認してください。

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
