# OpenVPNクライアントのLAN側からサーバーにアクセスする方法

このチュートリアルでは、OpenVPNサーバー側からOpenVPNクライアントのLANサブネット（NAS、IPカメラなど）にアクセスする手順説明します。

## 構成

下図のように、GL-AXT1800はOpenVPNサーバーであり、GL-MT2500はそれに接続されたOpenVPNクライアントです。サーバー側からGL-MT2500のLAN側にあるデバイス（NASやGL-MT3000、サブルーターなど）にアクセスできます。

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. サーバーでルートルールを追加

??? "ファームウェアv4.7で前の場合"

    <u>OpenVPNサーバー</u>のWeb管理パネルにログインし、**VPN** -> **VPNダッシュボード** -> **VPNサーバー**に移動します。

    右側のルートアイコンをクリックしてルートルールに入ります。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    ポップアップウィンドウで、右側の**ルートルールを追加**ボタンをクリックし、アクセスしたいサブネットを入力します。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    例として、OpenVPNクライアントGL-MT2500のLANサブネットは**192.168.48.0/24**なので、ターゲットアドレスは**192.168.48.0/24**です。
    
    ゲートウェイは、このOpenVPNクライアントに対してOpenVPNサーバーが生成したクライアントIPです。ここではゲートウェイを**10.8.0.1**に設定し、**適用**をクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    注意：アクセスする必要があるLANサブネットを持つ複数のOpenVPNクライアントがある場合は、ルートルールを設定する前に、[このリンク](reserve_fixed_IP_for_ovpn_client.md)を参照して各OpenVPNクライアントのクライアントIPを予約してください。

??? "ファームウェアv4.8で降の場合"

    <u>OpenVPNサーバー</u>のWeb管理パネルにログインし、**VPN** -> **OpenVPNサーバー**に移動します。

    **ルートルール**タブをクリックし、右側の**ルートルールを追加**ボタンをクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    ポップアップウィンドウで、アクセスしたいサブネットを入力します。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    例として、OpenVPNクライアントGL-MT2500のLANサブネットは**192.168.48.0/24**なので、ターゲットアドレスは**192.168.48.0/24**です。
    
    ゲートウェイは、このOpenVPNクライアントに対してOpenVPNサーバーが生成したクライアントIPです。ここではゲートウェイを**10.8.0.2**に設定し、**適用**をクリックします。

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

## 2. サーバーでNATを有効にする

**重要**：NATを有効にしないと、サーバー側からクライアントのLAN側のデバイスにアクセスできません。

??? "For firmware v4.7 and earlier"

    **VPN** -> **VPNダッシュボード** -> **VPNサーバー**に移動します。

    右側のオプションアイコンをクリックします。

    ![ovpn nat](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-nat-1.png){class="glboxshadow"}

    **NATを有効にする**をオンにし、**適用**をクリックします。

    ![ovpn nat](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-nat-2.png){class="glboxshadow"}

??? "For firmware v4.8 and higher"

    **VPN** -> **OpenVPNサーバー**に移動します。

    右上の**オプション**をクリックします。

    ![ovpn nat](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-nat-1.png){class="glboxshadow"}

    **NATを有効にする**をオンにし、**適用**をクリックします。

    ![ovpn nat](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-nat-2.png){class="glboxshadow"}

## 3. クライアントのLANサブネットへのアクセスをテスト

これで、サーバー側からOpenVPNクライアントのLANサブネットのデバイスにアクセスできるはずです。

例えば、サーバー側のブラウザで**192.168.48.1**（GL-MT2500のLAN IP）を入力すると、GL-MT2500の管理パネルにアクセスできます。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
