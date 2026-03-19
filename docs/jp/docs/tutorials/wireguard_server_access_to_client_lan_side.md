# サーバー側からWireGuardクライアントのLAN側へアクセスする方法

このチュートリアルでは、WireGuardサーバー側から、WireGuardクライアント側のLANサブネットにあるデバイス（IPカメラ、NAS など）へアクセスする手順を説明します。

## トポロジー

下図では、GL-MT2500 が WireGuard サーバー、GL-AXT1800 がその WireGuard クライアントです。サーバー側から、GL-AXT1800 の LAN 側にあるデバイス（IPカメラや NAS など）へアクセスできます。

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. サーバー側でルートルールを追加する

??? "For firmware v4.7 and earlier"

    <u>WireGuard サーバー側</u>の Web 管理画面にログインし、**VPN** -> **VPN Dashboard** -> **VPN Server** に移動します。

    右側のルートアイコンをクリックして、ルートルール設定画面を開きます。

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    右上の **Add Route Rule** をクリックし、アクセスしたいサブネットを入力します。

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    たとえば、WireGuard クライアント GL-AXT1800 の LAN サブネットが **192.168.8.0/24** の場合、Target Address には **192.168.8.0/24** を入力します。

    Gateway には、WireGuard サーバーがこのクライアント向けに割り当てたクライアント IP を入力します。これは **WireGuard Server** ページの **Profiles** タブで確認できます。下図では、WireGuard クライアント GL-AXT1800 のクライアント IP は **10.0.0.4** です。

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    そのため、Gateway は **10.0.0.4**、Scope は **global** に設定し、**Apply** をクリックします。

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    <u>WireGuard サーバー側</u>の Web 管理画面にログインし、**VPN** -> **WireGuard Server** に移動します。

    **Route Rules** タブをクリックし、右側の **Add Route Rule** をクリックします。

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    ポップアップウィンドウで、アクセスしたいサブネットを入力します。

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    たとえば、WireGuard クライアント GL-AXT1800 の LAN サブネットが **192.168.8.0/24** の場合、Target Address には **192.168.8.0/24** を入力します。

    Gateway には、WireGuard サーバーがこのクライアント向けに割り当てたクライアント IP を入力します。これは同じページの **Profiles** タブで確認できます。下図では、WireGuard クライアント GL-AXT1800 のクライアント IP は **10.1.0.2** です。

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    そのため、Gateway は **10.1.0.2** に設定し、**Apply** をクリックします。

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. クライアント側で LAN へのリモートアクセスを許可する

??? "For firmware v4.7 and earlier"

    <u>WireGuard クライアント側</u>の Web 管理画面にログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動します。

    WireGuard の右側にある歯車アイコンをクリックします。

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Remote Access LAN** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    <u>WireGuard クライアント側</u>の Web 管理画面にログインし、**VPN** -> **VPN Dashboard** に移動します。

    VPN トンネル左上の歯車アイコンをクリックして、トンネルオプションを開きます。

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. 接続をテストする

WireGuard サーバー側から、WireGuard クライアントの LAN 側デバイスへアクセスできるか確認します。

`ping` を使って接続確認できます。たとえば、WireGuard サーバー（GL-MT2500）へ接続されているデバイスから、WireGuard クライアント（GL-AXT1800）の LAN 内にあるデバイスの IP アドレスへ `ping` を送り、応答が返るか確認してください。

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
