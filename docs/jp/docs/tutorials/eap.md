# EAPネットワークにGL.iNetルーターを接続する方法

一部の GL.iNet ルーターは、EAP（Extensible Authentication Protocol）Wi-Fi ネットワークへの接続をサポートしています。

EAP は、**802.1X 認証**を利用する **WPA2-Enterprise / WPA3-Enterprise** ネットワークで広く使われている認証フレームワークです。代表的な例として、教育機関や研究機関で使われるグローバル Wi-Fi ローミングサービス **eduroam** があります。

このガイドでは、GL.iNet ルーターを EAP Wi-Fi ネットワークに接続する 2 つの方法を紹介します。1 つは Web 管理パネル経由、もう 1 つは LuCI 経由です。

## 対応モデル

??? "対応モデル" - GL-MT3600BE (Beryl 7) - GL-E5800 (Mudi 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-AX1800 (Flint) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus) - GL-XE300 (Puli) - GL-E750/GL-E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-AR750 (Creta) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-X300B (Collie) - ※GL-MT6000 (Flint 2) - ※GL-MT3000 (Beryl AX) - ※GL-SFT1200 (Opal)

    **Note:**

    1. GL-MT6000 (Flint 2) と GL-MT3000 (Beryl AX) は、デフォルトファームウェアでは EAP ネットワーク接続に対応していません。ただし、GL.iNet はこれらのモデル向けにネイティブ OpenWrt 24 ファームウェアを提供しており、これを導入することで EAP 接続を利用できます。[Download Center](https://dl.gl-inet.com/){target="_blank"} で対象モデルを検索し、OPENWRT 24 タブを確認してください。

    2. GL-SFT1200 (Opal) はファームウェア v4.8 で EAP ネットワーク接続をサポートしています。

??? "非対応モデル" - GL-MT5000 (Brume 3) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT1300 (Beryl) - GL-MT300N-V2 (Mango)

## Web管理パネルから接続する

1. Web 管理パネルにログインし、**INTERNET** -> **Repeater** に移動して **Connect** をクリックします。

   ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

   利用可能なネットワークがスキャンされます。接続したい EAP の SSID を見つけて選択してください。

   ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

   または、右上の **Join Other Network** をクリックして、EAP ネットワークへ手動で参加することもできます。

   ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. **SSID** を入力します。

   ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. **Security** で **WPA/WPA2/WPA3 Enterprise** を選択します。

   ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. **Username** と **Password** を入力し、**Apply** をクリックして接続します。

   ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## LuCI から接続する

GL.iNet の Web 管理パネルで対応している EAP タイプは限られています。

接続したい EAP ネットワークが Web 管理パネルから接続できない場合は、LuCI 経由で接続してください。

1. Web 管理パネルで **SYSTEM** -> **Advanced Settings** に移動します。LuCI をインストールし、**Go to LuCI** をクリックします。

   ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. 同じ管理者パスワードで LuCI にログインし、`Network -> Wireless` に進みます。

   ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. 2.4G または 5G セクションで **Scan** をクリックします。

   ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. 接続したいネットワークを選んで参加します。

   ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## トラブルシューティング

接続先の EAP ネットワークで、EAP タイプ（PEAP、TTLS など）、domain suffix match、identity、anonymous identity などの追加パラメータが必要な場合、Web 管理パネルからの EAP 接続は失敗することがあります。

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

追加設定が必要な EAP ネットワークへ LuCI から接続するには、以下の手順に従ってください。

1.  設定情報を確認します。

    接続先 EAP ネットワークに必要なパラメータを事前に確認してください。例えば次のような情報です。
    - EAP Type（例: PEAP、TTLS、TLS）
    - 認証ドメインサフィックス（例: `@company.com`）
    - Identity（通常はフルユーザー名）
    - Anonymous Identity（任意）
    - Inner authentication type（例: MSCHAPv2、PAP）
    - CA 証明書（必要な場合は `.crt` 形式のファイルを準備）

    参考として、以下は Xfinity Mobile Wi-Fi の設定例です。

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2.  LuCI にログインします。

    ルーターの Web 管理パネルにログインします。すでに WebGUI から対象の EAP ネットワークへの接続を試して失敗している場合は、先にその接続を中止してください。

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

    次に **SYSTEM** -> **Advanced Settings** -> **Go to LuCI** に進み、同じ管理者パスワードで LuCI にログインします。

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3.  LuCI で Repeater を設定します。

    LuCI で `Network -> Wireless` に移動します。

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

    5G または 2.4G セクションの **Scan** をクリックして、利用可能な Wi-Fi を検索します。

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

    スキャン結果から対象の EAP ネットワークを見つけ、**Join Network** をクリックします。

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

    `Joining Network` ページで **WPA passphrase** を入力し、**Submit** をクリックします。

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

    その後、Wireless Client の設定画面に移動します。

4.  **Interface Configuration** -> **Wireless Security** を設定します。

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

    対象の EAP ネットワークに合わせて、必要なパラメータを選択または入力します。**この時点ではまだ Save を押さないでください。**

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

5.  **Advanced Settings** タブに切り替え、インターフェース名を指定します。例えば **wlan0** です。その後、右下の **Save** をクリックします。

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

6.  Wireless ページに戻ると保留中の変更が表示されます。右下の **Save & Apply** をクリックします。

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

    これでルーターは対象の EAP ネットワークに正常に接続されます。

7.  接続を確認します。

    ??? "WebGUI で確認する"

        ルーターが対象の EAP ネットワークに正常に接続されると、下図のように WebGUI 上のリピーターアイコンが点灯します。

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

        **Note**: LuCI で行った設定は WebGUI とは同期されないため、接続先 IP やゲートウェイなどリピーターインターフェースの詳細は WebGUI には表示されません。

        画像のように下部のリピーター欄が空でも、上部のリピーターアイコンが点灯していれば、ルーターはすでに対象 EAP ネットワークへリピーターとして接続しています。

    ??? "SSH で確認する"

        1. [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} でルーターにログインします。

        2. `ifconfig` を入力して Enter を押します。

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

            **wlan0** インターフェースの状態を確認できます。

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
