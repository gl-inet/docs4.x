# EAPネットワークにGL.iNetルーターを接続する方法 {#connect-glinet-routers-to-an-eap-network}

一部の GL.iNet ルーターは、EAP（Extensible Authentication Protocol）Wi-Fi ネットワークへのリピーターとしての接続をサポートしています。

EAP は、**802.1X 認証**を使用する **WPA2‑Enterprise / WPA3‑Enterprise** ネットワークで一般的に利用される認証フレームワークです。代表的な例として、802.1X と EAP に基づく教育・研究向けのグローバル Wi‑Fi ローミングサービス **eduroam** があります。

このフレームワークには、EAP-PEAP、EAP-TLS、EAP-TTLS、EAP-FAST など、複数の EAP 認証方式があります。ただし、すべての EAP 方式がすべてのルーターのインターフェースやモデルでサポートされているわけではありません。

このガイドでは、GL.iNet ルーターを EAP Wi-Fi ネットワークに接続する 2 つの方法を紹介します。1 つは GL.iNet Web 管理パネル、もう 1 つは LuCI を使用する方法です。それぞれ対応する EAP 認証方式が異なり、前者は **EAP-PEAP** のみ、後者は **EAP-TLS**、**EAP-TTLS**、**EAP-PEAP**、**EAP-FAST** に対応しています。

一部の GL.iNet ルーターでは、この 2 つの方法のうち一方でのみ EAP リピーター機能を利用できます。以下の対応モデルを確認してください。

### 対応モデル {#supported-models}

??? "対応モデル"
    - <u>GL-MG1300 (Mango 2)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-AX1800 (Flint)</u><sup>1</sup>
    - <u>GL-AXT1800 (Slate AX)</u><sup>1</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - <u>GL-E750/GL-E750V2 (Mudi)</u><sup>1</sup>
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

    ---

    **注意**:

    1. GL-MG1300 (Mango 2)、GL-AX1800 (Flint)、GL-AXT1800 (Slate AX)、GL-E750/GL-E750V2 (Mudi) は、リピーターとして、GL.iNet Web 管理パネルから EAP-PEAP ネットワークに、LuCI から EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST ネットワークに接続できます。

    2. GL-MT6000 (Flint 2) と GL-MT3000 (Beryl AX) は、デフォルトファームウェアでは、リピーターとして EAP ネットワークに接続できません。ただし、GL.iNet はこれらのモデル向けに、EAP に対応した OpenWrt ファームウェアを提供しています。このファームウェアをインストールすると、ルーターをリピーターモードに設定し、GL.iNet Web 管理パネルから EAP-PEAP ネットワークに、または LuCI から EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST ネットワークに接続できます。

        必要に応じて、[Download Center](https://dl.gl-inet.com/){target="_blank"} でモデルを検索し、OpenWrt タブを選択してダウンロードしてください。

    3. GL-SFT1200 (Opal) は、ファームウェア v4.8 以降で、GL.iNet Web 管理パネル（EAP-PEAP）と LuCI（EAP-TLS/EAP-TTLS/EAP-PEAP/EAP-FAST）の両方から、リピーターとして EAP ネットワークに接続できます。

    4. 上記のその他すべてのモデルは、GL.iNet Web 管理パネルからのみ、リピーターとして EAP-PEAP ネットワークに接続できます。その他の EAP 方式（EAP-TLS、EAP-TTLS、EAP-FAST など）はサポートされていません。

??? "非対応モデル"
    - GL-MT6000 (Fortify)
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Web 管理パネルから接続する {#connect-via-web-admin-panel}

GL.iNet Web 管理パネルから、ルーターをリピーターとして EAP-PEAP ネットワークに接続できます。

1. Web 管理パネルにログインし、**INTERNET** -> **Repeater** に移動して **Connect** をクリックします。

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    利用可能なネットワークがスキャンされます。接続する EAP SSID を見つけて選択してください。

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    または、右上の **Join Other Network** をクリックして、EAP ネットワークに手動で参加することもできます。

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. **SSID** を入力します。

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. **Security** で WPA/WPA2/WPA3 Enterprise を選択します。

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. **Username** と **Password** を入力し、**Apply** をクリックして接続します。

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## LuCI から接続する {#connect-via-luci}

LuCI から、ルーターをリピーターとして EAP-TLS、EAP-TTLS、EAP-PEAP、または EAP-FAST ネットワークに接続できます。

以下の手順は参考です。お使いのデバイスの実際の LuCI ページを参照してください。

1. Web 管理パネルにログインし、**SYSTEM** -> **Advanced Settings** に移動します。LuCI をインストールし、**Go to LuCI** をクリックします。

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. 同じ管理者パスワードで LuCI にログインし、Network -> Wireless に移動します。

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. 2.4G セクションまたは 5G セクションの **Scan** をクリックします。

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. 接続したいネットワークに参加します。

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## トラブルシューティング {#troubleshooting}

接続先の EAP ネットワークで、EAP type（PEAP、TTLS など）、domain suffix match、identity、anonymous identity などの追加パラメーターが必要な場合、Web 管理パネルからの EAP 接続は失敗することがあります。

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

高度な設定が必要な EAP ネットワークに LuCI インターフェース経由で GL.iNet ルーターを接続するには、以下の手順に従ってください。

1. 設定情報を取得します。

    接続先の EAP ネットワークに必要な設定パラメーターを事前に確認してください。例:

    - EAP Type（例: PEAP、TTLS、TLS）
    - Authentication domain suffix（例: @company.com）
    - Identity（通常は完全なユーザー名）
    - Anonymous Identity（任意）
    - Inner authentication type（例: MSCHAPv2、PAP）
    - CA certificate（必要な場合は .crt 形式のファイルを準備）

    参考として、以下は Xfinity Mobile Wi-Fi の例です。

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. LuCI にログインします。

    ルーターの Web 管理パネルにログインします。ログイン後、以前に WebGUI から対象の EAP ネットワークへの接続を試して失敗している場合は、その接続を中止してください。

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    その後、**SYSTEM** -> **Advanced Settings** -> **Go to LuCI** に移動します。同じ管理者パスワードで LuCI にログインしてください。

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. LuCI で Repeater を設定します。

    LuCI インターフェースで Network -> Wireless に移動します。

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    5G または 2.4G セクションの **Scan** ボタンをクリックし、利用可能な Wi-Fi ネットワークを検索します。

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    スキャン結果から対象の EAP ネットワークを見つけ、**Join Network** をクリックします。

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    「Joining Network」ページで **WPA passphrase** を入力し、**Submit** ボタンをクリックします。

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    Wireless Client の設定画面に移動します。

4. **Interface Configuration** -> **Wireless Security** を探します。

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    以下のように、対象の EAP ネットワークに合わせて正しい設定パラメーターを選択または入力します。**まだ Save はクリックしないでください**。

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. **Advanced Settings** タブに切り替え、**wlan0** などのインターフェース名を指定します。その後、右下の **Save** をクリックします。

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Wireless ページに戻ると、保留中の変更が表示されます。右下の **Save & Apply** ボタンをクリックします。

    ![save and apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    これでルーターは対象の EAP ネットワークに正常に接続されます。

7. 接続を確認します。

    ??? "WebGUI で接続を確認する"

        ルーターが対象の EAP ネットワークに正常に接続すると、以下のように WebGUI のリピーターアイコンが点灯します。

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **注意**: LuCI の設定は WebGUI の設定と同期されないため、接続された IP、gateway など、リピーターインターフェースの詳細は WebGUI に表示されません。

        画像のように下部のリピーター欄が空欄でも、上部のリピーターアイコンが点灯していれば、ルーターはすでにリピーターとして対象の EAP ネットワークに接続しています。

    ??? "SSH で接続を確認する"

        1. [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} でルーターにログインします。

        2. **ifconfig** と入力して Enter を押します。

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            **wlan0** インターフェースの状態を確認できます。

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
