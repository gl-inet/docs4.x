# サーバー側からOpenVPNクライアントのLAN側へアクセスする方法

このチュートリアルでは、OpenVPNサーバー側から OpenVPN クライアントのLANサブネット（NAS、IPカメラなど）にアクセスする手順を説明します。

## トポロジー

以下の図のように、GL-AXT1800 は OpenVPN サーバー、GL-MT2500 はそれに接続された OpenVPN クライアントです。サーバー側から、GL-MT2500 のLAN側にあるデバイス（NAS や GL-MT3000 などのサブルーター）へアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. サーバー側でルートルールを追加する

??? "ファームウェア v4.7 以前"

    <u>OpenVPNサーバー</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Server** に移動します。

    右側のルートアイコンをクリックして、ルートルール画面を開きます。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    ポップアップウィンドウで、右側の **Add Route Rule** ボタンをクリックし、アクセスしたいサブネットを入力します。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    たとえば、OpenVPNクライアント GL-MT2500 のLANサブネットが **192.168.48.0/24** の場合、**Target Address** は **192.168.48.0/24** です。

    **Gateway** は、この OpenVPN クライアントに対して OpenVPN サーバーが割り当てたクライアントIPです。ここでは **Gateway** を **10.8.0.1** に設定し、**Apply** をクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    注: LANサブネットにアクセスしたい OpenVPN クライアントが複数ある場合は、ルートルールを設定する前に、[こちら](reserve_fixed_IP_for_ovpn_client.md) を参照して各 OpenVPN クライアントのクライアントIPを予約してください。

??? "ファームウェア v4.8 以降"

    <u>OpenVPNサーバー</u>のWeb管理パネルにログインし、**VPN** -> **OpenVPN Server** に移動します。

    **Route Rules** タブをクリックし、右側の **Add Route Rule** ボタンをクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    ポップアップウィンドウで、アクセスしたいサブネットを入力します。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    たとえば、OpenVPNクライアント GL-MT2500 のLANサブネットが **192.168.48.0/24** の場合、**Target Address** は **192.168.48.0/24** です。

    **Gateway** は、この OpenVPN クライアントに対して OpenVPN サーバーが割り当てたクライアントIPです。ここでは **Gateway** を **10.8.0.2** に設定し、**Apply** をクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    注: LANサブネットにアクセスしたい OpenVPN クライアントが複数ある場合は、ルートルールを設定する前に、[こちら](reserve_fixed_IP_for_ovpn_client.md) を参照して各 OpenVPN クライアントのクライアントIPを予約してください。

## 2. クライアントLANへのリモートアクセスを許可する

??? "ファームウェア v4.7 以前"

    <u>OpenVPNクライアント</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** -> **VPN Client** に移動します。

    歯車アイコンをクリックしてクライアントオプションを開きます。

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Remote Access LAN** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "ファームウェア v4.8 以降"

    <u>OpenVPNクライアント</u>のWeb管理パネルにログインし、**VPN** -> **VPN Dashboard** に移動します。

    VPNトンネルの左上にある歯車アイコンをクリックして、トンネルオプションを開きます。

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    ポップアップウィンドウで **Allow Remote Access the LAN Subnet** を有効にし、**Apply** をクリックします。

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. 接続をテストする

OpenVPNクライアントのLAN内にある GL-MT3000 に、IPアドレス **192.168.48.211** でアクセスする例を示します。

OpenVPNサーバーに接続しているデバイスから、GL-MT3000 のIPアドレス **192.168.48.211** に ping を実行します。これは、OpenVPNクライアント（GL-MT2500）が自分のLAN内で GL-MT3000 に割り当てたIPアドレスです。

ping が成功すれば、設定は正しく完了しています。OpenVPNクライアントのLANサブネット内にある他のデバイスにも、それぞれのIPアドレスでアクセスできるようになります。

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
