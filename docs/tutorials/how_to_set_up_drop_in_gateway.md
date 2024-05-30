# GL.iNetルーターでドロップインゲートウェイを設定する方法

GL.iNetは、AdGuard Home、暗号化されたDNS、VPNなど、プライマリルーターにない機能を追加するドロップインゲートウェイ機能を提供しています。この機能を使用することで、プライマリルーターを通常通り使用しながら追加の機能を楽しむことができます。

ドロップインゲートウェイをプライマリルーターに接続された[すべてのデバイス](#すべてのデバイスに対してドロップインゲートウェイを有効にする)または[特定のデバイス](#特定のデバイスに対してドロップインゲートウェイを有効にする)に対して有効にすることができます。適切なセクションに従って設定を行ってください。

---

## すべてのデバイスに対してドロップインゲートウェイを有効にする

### 1. GL.iNetルーターをメインルーターに接続する

GL.iNetルーターのWANポートをメインルーターのLANポートにイーサネットケーブルで接続します。

### 2. ドロップインゲートウェイモードを有効にする
ドロップインゲートウェイモードを有効にする方法は2つあります：[ルーター管理パネルを通じて](#ルーター管理パネルを通じて)または[GL.iNetモバイルアプリを通じて](#glinetモバイルアプリを通じて)。

#### ルーター管理パネルを通じて

1. Webブラウザーで192.168.8.1と入力します。  
2. パスワードを入力して、**ログイン**をクリックします。
3. 左側のサイドバーで、**ネットワーク** > **ドロップインゲートウェイ**をクリックします。
![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

4. **ドロップインゲートウェイモードを有効にする**の隣にあるスイッチをオンにします。
5. **すべてのデバイスがドロップインゲートウェイを通じてネットワークに接続される**を選択します。
![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

6. **適用**をクリックします。

#### GL.iNetモバイルアプリを通じて

**注:** 始める前に、デバイスにGL.iNetモバイルアプリをインストールして設定してください。

1. メインアプリ画面で、**システム**タブ > **ドロップインゲートウェイ**をタップします。
![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

2. **有効にする**をタップします。
3. **デバイスがドロップインゲートウェイを介してネットワークに接続される**のために、**すべて**をタップします。
![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}
4. **完了**をタップします。

### 3. メインルーターのDHCPサーバーを無効にする
特定のルーターでDHCPサーバーを無効にする方法については、ルーターメーカーが提供する指示を参照してください。

### 4. AdGuard、DNS、VPN、およびその他の機能を設定する

GL.iNetルーターで機能を有効にする方法については、以下の記事を参照してください：

* [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/){target="_blank"}
* [暗号化DNS](https://docs.gl-inet.com/router/en/4/interface_guide/dns/){target="_blank"}
* [ペアレンタル・コントロール](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control/){target="_blank"}
* [WireGaurd クライアント](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/){target="_blank"}
* [OpenVPN クライアント](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/){target="_blank"}

---

## 特定のデバイスに対してドロップインゲートウェイを有効にする

### 1. GL.iNetルーターをメインルーターに接続する
GL.iNetルーターのWANポートをメインルーターのLANポートにイーサネットケーブルで接続します。

### 2. ドロップインゲートウェイモードを有効にする
ドロップインゲートウェイモードを有効にする方法は2つあります：[ルーター管理パネルを通じて](#specific-devices-admin)または[GL.iNetモバイルアプリを通じて](#specific-devices-mobile)。

#### ルーター管理パネルを通じて {#specific-devices-admin}

1. Webブラウザーで192.168.8.1と入力します。
2. パスワードを入力して、**ログイン**をクリックします。
3. 左側のサイドバーで、**ネットワーク** > **ドロップインゲートウェイ**をクリックします。
![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}
4. **ドロップインゲートウェイモードを有効にする**の隣にあるスイッチをオンにします。
5. **一部のデバイスが独自のネットワーキングゲートウェイを選択する**を選択します。
![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

6. **適用**をクリックします。

**注:** このタブを閉じないでください。次のステップで表示されるIPアドレスを入力する必要があります。

#### GL.iNetモバイルアプリを通じて {#specific-devices-mobile}

**注:** 始める前に、デバイスにGL.iNetモバイルアプリをインストールして設定してください。

1. メインアプリ画面で、**システム**タブ > **ドロップインゲートウェイ**をタップします。
![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
2. **有効にする**をタップします。
3. **デバイスがドロップインゲートウェイを介してネットワークに接続される**のために、**一部**をタップします。
![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}
4. **完了**をタップします。

**注:** このタブを閉じないでください。次のステップで表示されるIPアドレスを入力する必要があります。

### 3. デバイスでゲートウェイとDNSを設定する

??? "Windows"
    1. デバイスをメインルーターに接続します。
    2. Windowsで、**設定** > **ネットワークとインターネット**を開きます。
    3. 接続方法に基づいて、以下の手順に従います: 
        * Ethernet: **Ethernet**をクリックします。
        * Wi-Fi: **Wi-Fi**をクリックし、Wi-Fiネットワーク名をクリックします。
    4. IPv4アドレスをコピーします。**IP割り当て**の隣にある**編集**をクリックします。
    5. **手動**をクリックします。
    6. **IPv4**をオンに切り替えます。
    7. 以下の情報を入力します:
        * **IPアドレス:** ステップ4でコピーしたIPアドレスを貼り付けます。
        * **サブネットマスク:** **255.255.255.0**と入力します。
        * **ゲートウェイ:** **ドロップインゲートウェイ**ページに表示されるIPアドレスを入力します。
        * **優先DNS:** **ドロップインゲートウェイ**ページに表示されるIPアドレスを入力します。
    8. **保存**をクリックします。

??? "Android"
    1. デバイスをメインルーターに接続します。
    2. Androidで、**設定** を開きます。
    3. **接続** > **Wi-Fi** をタップします。
    4. 接続しているネットワークの **設定** アイコンをタップします。
    5. **詳細を表示** をタップします。
    6. **IP設定** > **静的** をタップします。
    7. **ゲートウェイ** と **DNS 1** に **ドロップインゲートウェイ** 画面に表示されるIPアドレスを入力します。
    8. **保存** をタップします。

??? "iOS"
    1. デバイスをメインルーターに接続します。
    2. iOSで、**設定** を開きます。
    3. **Wi-Fi** をタップします。
    4. 接続しているWi-Fiネットワークをタップします。
    5. **IPv4アドレス** の下で **IPアドレス** と **サブネットマスク** を記録します。
    6. **IPを構成** > **手動** をタップします。
    7. 次の情報を入力します：
        * **IPアドレス**：ステップ5で取得したIPアドレスを入力します。
        * **サブネットマスク**：ステップ5で取得したサブネットマスクを入力します。
        * **ルーター**：**ドロップインゲートウェイ** 画面に表示されるIPアドレスを入力します。
    8. **保存** をタップします。
    9. **DNSを構成** をタップし、**手動** をタップします。
    10. **サーバーを追加** をタップし、**ドロップインゲートウェイ** 画面に表示されるIPアドレスを入力します。
    11. **保存** をタップします。

??? "Mac"
    1. デバイスをメインルーターに接続します。
    2. Macで、Appleアイコン > **システム設定** をクリックします。
    3. 左のサイドバーで **ネットワーク** をクリックします。
    4. 接続しているネットワークの横で **詳細** をクリックします。
    5. **TCP/IP** をクリックします。
    6. **IPアドレス** と **サブネットマスク** を記録します。
    7. **IPv4を構成** の横で **手動** をクリックします。
    8. 次の情報を入力します：
        * **IPアドレス**：ステップ5で取得したIPアドレスを入力します。
        * **サブネットマスク**：ステップ5で取得したサブネットマスクを入力します。
        * **ルーター**：**ドロップインゲートウェイ** ページに表示されるIPアドレスを入力します。
    9. **OK** > **OK** をクリックします。

### 4. AdGuard、DNS、VPN、その他の機能を設定する

GL.iNetルーターで機能を有効にするには、以下の記事を参照してください：

* [AdGuard Home](https://docs.gl-inet.com/router/en/4/interface_guide/adguardhome/){target="_blank"}
* [暗号化されたDNS](https://docs.gl-inet.com/router/en/4/interface_guide/dns/){target="_blank"}
* [ペアレンタルコントロール](https://docs.gl-inet.com/router/en/4/interface_guide/parental_control/){target="_blank"}
* [WireGuardクライアント](https://docs.gl-inet.com/router/en/4/interface_guide/wireguard_client/){target="_blank"}
* [OpenVPNクライアント](https://docs.gl-inet.com/router/en/4/interface_guide/openvpn_client/){target="_blank"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}を訪問してください。