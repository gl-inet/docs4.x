# GL.iNetルーターでDrop-in Gatewayを設定する方法

GL.iNetはDrop-in Gateway機能を提供しており、AdGuard Home、暗号化DNS、VPNなど、メインルーターにない機能を追加できます。この機能を使うことで、メインルーターをこれまでどおり使いながら、追加機能も利用できます。

Drop-in Gatewayは、メインルーターに接続されている[すべてのデバイス](#enable-drop-in-gateway-for-all-devices)または[特定のデバイス](#enable-drop-in-gateway-for-specific-devices)に対して有効にできます。利用する構成に応じて、該当するセクションの手順に従ってください。

**Note**: ファームウェアバージョンが v4.5.0 未満のモデルでは、Drop-in Gatewayをすべてのデバイスに対してのみ有効にできます。Drop-in Gatewayを有効にすると、すべてのクライアントデバイスはDrop-in Gateway経由でネットワークに接続されるため、接続中のクライアントからのすべてのトラフィックは、まずこのルーターで処理されます。

---

## すべてのデバイスでDrop-in Gatewayを有効にする {#enable-drop-in-gateway-for-all-devices}

### 1. GL.iNetルーターをメインルーターに接続する

GL.iNetルーターのWANポートを、メインルーターのLANポートにイーサネットケーブルで接続します。

### 2. Drop-in Gatewayを有効にする

Drop-in Gatewayを有効にする方法は2つあります。ルーターの管理画面を使う方法と、GL.iNet mobile app を使う方法です。

??? "Using web admin panel"

    1. Webブラウザーで `192.168.8.1` を入力します。

    2. パスワードを入力し、**Login** をクリックします。

    3. 左側のサイドバーで **Network** > **Drop-in Gateway** をクリックします。

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. **Enable Drop-in Gateway Mode** の横にあるスイッチをオンにします。

    5. **All devices are networked through drop-in gateway** を選択します。

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. **Apply** をクリックします。

??? "Using GL.iNet mobile app"

    **Note:** 開始前に、デバイスにGL.iNet mobile app をインストールしてください。

    1. アプリのメイン画面で、**System** タブ > **Drop-in Gateway** をタップします。

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. **Enable** をタップします。

    3. **Devices are networked via drop-in gateway** で **All** をタップします。

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. **Done** をタップします。

### 3. メインルーターのDHCPサーバーを無効にする

メインルーターにログインして、DHCPサーバーを無効にしてください。ルーターメーカーが提供する手順を参照するか、サポートにお問い合わせください。

### 4. AdGuard、DNS、VPN、その他の機能を設定する

GL.iNetルーターで利用したい機能を有効にするには、以下のガイドを参照してください。

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

## 特定のデバイスでDrop-in Gatewayを有効にする {#enable-drop-in-gateway-for-specific-devices}

### 1. GL.iNetルーターをメインルーターに接続する

GL.iNetルーターのWANポートを、メインルーターのLANポートにイーサネットケーブルで接続します。

### 2. Drop-in Gatewayを有効にする

Drop-in Gatewayを有効にする方法は2つあります。 [ルーターの管理画面](#using-web-admin-panel)を使う方法と、[GL.iNet mobile app](#using-glinet-mobile-app)を使う方法です。

??? "Using web admin panel"

    1. Webブラウザーで `192.168.8.1` を入力します。

    2. パスワードを入力し、**Login** をクリックします。

    3. 左側のサイドバーで **Network** > **Drop-in Gateway** をクリックします。

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. **Enable Drop-in Gateway Mode** の横にあるスイッチをオンにします。

    5. **Some devices select their own networking gateway** を選択します。

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. **Apply** をクリックします。

    **Note:** このタブは閉じないでください。次の手順で、画面に表示されているIPアドレスを入力する必要があります。

??? "Using GL.iNet mobile app"

    **Note:** 開始前に、デバイスにGL.iNet mobile app をインストールしてください。

    1. アプリのメイン画面で、**System** タブ > **Drop-in Gateway** をタップします。

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. **Enable** をタップします。

    3. **Devices are networked via drop-in gateway** で **part** をタップします。

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. **Done** をタップします。

    **Note:** このタブは閉じないでください。次の手順で、画面に表示されているIPアドレスを入力する必要があります。

### 3. 特定のデバイスでゲートウェイとDNSを設定する

??? "Windows"

    1. デバイスをメインルーターに接続します。
    2. Windowsで **Settings** > **Network & Internet** を開きます。
    3. 接続方法に応じて、以下の手順に従ってください。
        * Ethernet: **Ethernet** をクリックします。
        * Wi-Fi: **Wi-Fi** をクリックし、接続中のWi-Fiネットワーク名をクリックします。
    4. IPv4アドレスをコピーします。次に **IP assignment** の横にある **Edit** をクリックします。
    5. **Manual** をクリックします。
    6. **IPv4** をオンにします。
    7. 以下の情報を入力します。
        * **IP address:** 手順4でコピーしたIPアドレスを貼り付けます。
        * **Subnet mask:** **255.255.255.0** を入力します。
        * **Gateway:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。
        * **Preferred DNS:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。
    8. **Save** をクリックします。

??? "Android"
    1. デバイスをメインルーターに接続します。
    2. Androidで **Settings** を開きます。
    3. **Connections** > **Wi-Fi** をタップします。
    4. 接続中のネットワークの横にある **Settings** アイコンをタップします。
    5. **View more** をタップします。
    6. **IP settings** > **Static** をタップします。
    7. **Gateway** と **DNS 1** に、**Drop-in Gateway** 画面に表示されているIPアドレスを入力します。
    8. **Save** をタップします。

??? "iOS"
    1. デバイスをメインルーターに接続します。
    2. iOSで **Settings** を開きます。
    3. **Wi-Fi** をタップします。
    4. 接続中のWi-Fiネットワークをタップします。
    5. **IPv4 Address** の下で、**IP Address** と **Subnet Mask** を控えておきます。
    6. **Configure IP** > **Manual** をタップします。
    7. 以下の情報を入力します。
        * **IP Address:** 手順5で確認したIP Addressを入力します。
        * **Subnet Mask:** 手順5で確認したSubnet Maskを入力します。
        * **Router:** **Drop-in Gateway** 画面に表示されているIPアドレスを入力します。
    8. **Save** をタップします。
    9. **Configure DNS** をタップし、続けて **Manual** をタップします。
    10. **Add Server** をタップし、**Drop-in Gateway** 画面に表示されているIPアドレスを入力します。
    11. **Save** をタップします。

??? "Mac"
    1. デバイスをメインルーターに接続します。
    2. MacでAppleアイコン > **System Settings** をクリックします。
    3. 左側のサイドバーで **Network** をクリックします。
    4. 接続中のネットワークの横にある **Details** をクリックします。
    5. **TCP/IP** をクリックします。
    6. **IP Address** と **Subnet Mask** を控えておきます。
    7. **Configure IPv4** の横で **Manually** をクリックします。
    8. 以下の情報を入力します。
        * **IP address:** 手順6で確認したIP Addressを入力します。
        * **Subnet mask:** 手順6で確認したSubnet Maskを入力します。
        * **Router:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。
    9. **OK** > **OK** をクリックします。

### 4. AdGuard、DNS、VPN、その他の機能を設定する

GL.iNetルーターで利用したい機能を有効にするには、以下のガイドを参照してください。

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

Related Article:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
