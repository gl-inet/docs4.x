# GL.iNetルーターでDrop-in Gatewayを設定する方法

GL.iNetはDrop-in Gateway機能を提供しており、AdGuard Home、暗号化DNS、VPNなど、メインルーターにはない機能を追加できます。この機能を使えば、メインルーターはそのまま利用しながら、追加機能だけをGL.iNetルーター側で利用できます。

Drop-in Gatewayは、メインルーターに接続されている[すべてのデバイス](#すべてのデバイスでdrop-in-gatewayを有効にする)または[特定のデバイス](#特定のデバイスでdrop-in-gatewayを有効にする)に対して有効にできます。利用したい構成に合わせて該当する手順を実行してください。

**Note**: ファームウェアが v4.5.0 未満のモデルでは、Drop-in Gatewayを有効にできるのはすべてのデバイスに対してのみです。Drop-in Gatewayを有効にすると、接続中のすべてのクライアントデバイスの通信はまずこのルーターを経由して処理されます。

---

## すべてのデバイスでDrop-in Gatewayを有効にする

### 1. GL.iNetルーターをメインルーターに接続する

GL.iNetルーターのWANポートを、メインルーターのLANポートにイーサネットケーブルで接続します。

### 2. Drop-in Gatewayを有効にする

Drop-in Gatewayを有効にする方法は2通りあります。ルーターの管理画面を使う方法と、GL.iNetモバイルアプリを使う方法です。

??? "Using web admin panel"

    1. Webブラウザーで `192.168.8.1` を開きます。

    2. パスワードを入力し、**Login** をクリックします。

    3. 左側のサイドバーで **Network** > **Drop-in Gateway** をクリックします。

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. **Enable Drop-in Gateway Mode** の横にあるスイッチをオンにします。

    5. **All devices are networked through drop-in gateway** を選択します。

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. **Apply** をクリックします。

??? "Using GL.iNet mobile app"

    **Note:** 開始前に、端末へGL.iNetモバイルアプリをインストールしてください。

    1. アプリのメイン画面で **System** タブ > **Drop-in Gateway** をタップします。

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. **Enable** をタップします。

    3. **Devices are networked via drop-in gateway** で **All** をタップします。

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. **Done** をタップします。

### 3. メインルーターのDHCPサーバーを無効にする

メインルーターにログインして、DHCPサーバーを無効にしてください。設定方法はルーターメーカーの案内を参照するか、メーカーサポートへお問い合わせください。

### 4. AdGuard、DNS、VPNなどの機能を設定する

GL.iNetルーターで利用したい機能に応じて、以下のガイドを参照してください。

- [AdGuard Home](../interface_guide/adguardhome.md){target="\_blank"}
- [暗号化DNS](../interface_guide/dns.md){target="\_blank"}
- [ペアレンタルコントロール](../interface_guide/parental_control.md){target="\_blank"}
- [WireGaurd Client](../interface_guide/wireguard_client.md){target="\_blank"}
- [OpenVPN Client](../interface_guide/openvpn_client.md){target="\_blank"}

---

## 特定のデバイスでDrop-in Gatewayを有効にする

### 1. GL.iNetルーターをメインルーターに接続する

GL.iNetルーターのWANポートを、メインルーターのLANポートにイーサネットケーブルで接続します。

### 2. Drop-in Gatewayを有効にする

Drop-in Gatewayを有効にする方法は2通りあります。ルーターの管理画面を使う方法と、GL.iNetモバイルアプリを使う方法です。

??? "Using web admin panel"

    1. Webブラウザーで `192.168.8.1` を開きます。

    2. パスワードを入力し、**Login** をクリックします。

    3. 左側のサイドバーで **Network** > **Drop-in Gateway** をクリックします。

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. **Enable Drop-in Gateway Mode** の横にあるスイッチをオンにします。

    5. **Some devices select their own networking gateway** を選択します。

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. **Apply** をクリックします。

    **Note:** このタブは閉じないでください。次の手順で、画面に表示されるIPアドレスを入力する必要があります。

??? "Using GL.iNet mobile app"

    **Note:** 開始前に、端末へGL.iNetモバイルアプリをインストールしてください。

    1. アプリのメイン画面で **System** タブ > **Drop-in Gateway** をタップします。

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. **Enable** をタップします。

    3. **Devices are networked via drop-in gateway** で **part** をタップします。

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. **Done** をタップします。

    **Note:** このタブは閉じないでください。次の手順で、画面に表示されるIPアドレスを入力する必要があります。

### 3. 特定のデバイスでゲートウェイとDNSを設定する

??? "Windows" 1. デバイスをメインルーターに接続します。2. Windowsで **Settings** > **Network & Internet** を開きます。3. 接続方法に応じて、以下のいずれかを選択します。
_ Ethernet: **Ethernet** をクリックします。
_ Wi-Fi: **Wi-Fi** をクリックし、接続中のWi-Fi名をクリックします。4. IPv4アドレスをコピーします。続いて **IP assignment** の横にある **Edit** をクリックします。5. **Manual** をクリックします。6. **IPv4** をオンにします。7. 以下の情報を入力します。
_ **IP address:** 手順4でコピーしたIPアドレスを貼り付けます。
_ **Subnet mask:** `255.255.255.0` を入力します。
_ **Gateway:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。
_ **Preferred DNS:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。8. **Save** をクリックします。

??? "Android" 1. デバイスをメインルーターに接続します。2. Androidで **Settings** を開きます。3. **Connections** > **Wi-Fi** をタップします。4. 接続中のネットワークの横にある **Settings** アイコンをタップします。5. **View more** をタップします。6. **IP settings** > **Static** をタップします。7. **Gateway** と **DNS 1** に、**Drop-in Gateway** 画面に表示されているIPアドレスを入力します。8. **Save** をタップします。

??? "iOS" 1. デバイスをメインルーターに接続します。2. iOSで **Settings** を開きます。3. **Wi-Fi** をタップします。4. 接続中のWi-Fiネットワークをタップします。5. **IPv4 Address** の項目で、**IP Address** と **Subnet Mask** を控えます。6. **Configure IP** > **Manual** をタップします。7. 以下の情報を入力します。
_ **IP Address:** 手順5で控えたIP Addressを入力します。
_ **Subnet Mask:** 手順5で控えたSubnet Maskを入力します。\* **Router:** **Drop-in Gateway** 画面に表示されているIPアドレスを入力します。8. **Save** をタップします。9. **Configure DNS** をタップし、**Manual** をタップします。10. **Add Server** をタップし、**Drop-in Gateway** 画面に表示されているIPアドレスを入力します。11. **Save** をタップします。

??? "Mac" 1. デバイスをメインルーターに接続します。2. MacでAppleアイコン > **System Settings** をクリックします。3. 左側のサイドバーで **Network** をクリックします。4. 接続中のネットワークの横にある **Details** をクリックします。5. **TCP/IP** をクリックします。6. **IP Address** と **Subnet Mask** を控えます。7. **Configure IPv4** の横で **Manually** をクリックします。8. 以下の情報を入力します。
_ **IP address:** 手順6で控えたIP Addressを入力します。
_ **Subnet mask:** 手順6で控えたSubnet Maskを入力します。\* **Router:** **Drop-in Gateway** ページに表示されているIPアドレスを入力します。9. **OK** > **OK** をクリックします。

### 4. AdGuard、DNS、VPNなどの機能を設定する

GL.iNetルーターで利用したい機能に応じて、以下のガイドを参照してください。

- [AdGuard Home](../interface_guide/adguardhome.md){target="\_blank"}
- [暗号化DNS](../interface_guide/dns.md){target="\_blank"}
- [ペアレンタルコントロール](../interface_guide/parental_control.md){target="\_blank"}
- [WireGaurd Client](../interface_guide/wireguard_client.md){target="\_blank"}
- [OpenVPN Client](../interface_guide/openvpn_client.md){target="\_blank"}

---

関連記事:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
