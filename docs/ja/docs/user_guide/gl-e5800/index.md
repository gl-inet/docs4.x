# Mudi 7 (GL-E5800) ユーザーガイド {#mudi-7-gl-e5800-user-guide}

## 製品概要 {#product-overview}

Mudi 7は、ロードウォリアーとビジネス旅行者向けのポータブル5G NR Wi-Fi 7トラベルルーターです。5Gハイスピード、デュアルSIM自動切替（フェイルオーバー）、Wi-Fi 7（320MHzチャンネルと4K QAM）を特徴とし、安定した高速接続を実現します。高速ダウンロード、4Kストリーミング、混雑した地域でも遅延のないビデオ会議をサポートします。

タッチスクリーンを備えたMudi 7では、リアルタイムのデータ使用量、信号強度、接続中のデバイス、クライアントの通信速度を確認できます。簡単なタップ操作で設定を調整でき、直感的に操作できます。

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## パッケージコンテンツ {#package-contents}

- 1 x Mudi 7 (GL-E5800)
- 1 x バッテリーパック
- 1 x 10Gbps USB-Cケーブル
- 1 x トラベルポーチ
- 1 x ユーザーマニュアル

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

以下のMudi 7の開梱動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Mudi 7の設定方法 {#how-to-set-up-mudi-7}

このセットアップ動画を視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Nano-SIMカードのインストール {#1-install-sim-card}

Mudi 7 に Nano-SIM カードを挿入します。eSIM を使用する場合は、この手順を飛ばして手順 2 に進んでください。

!!! Warning

    バッテリーが膨張している、液漏れしている、異常に熱い、損傷している、または取り外しにくい場合は、デバイスの使用を中止し、バッテリーを取り外そうとしないでください。[バッテリーの安全性](#battery-safety)を参照してください。

まず、本体背面カバー右下の小さな切り欠きを支点にし、すき間に沿ってこじ開けて背面カバーを外し、Mudi 7 のバッテリーを取り出します。

![small notch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/notch.png){class="glboxshadow"}

![remove battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery1.png){class="glboxshadow"}

次に、Nano-SIM カードを挿入します。1 枚だけ使用する場合は、SIM 1 を優先してください。

![sim slots](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/sim-slots.png){class="glboxshadow"}

最後に、バッテリーとカバーを元に戻します。

![restore battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery2.png){class="glboxshadow"}

### 2. 電源を入れる {#2-power-on}

**3秒間**電源ボタンを長押しするか、電源アダプターを挿します。

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power-button.png){class="glboxshadow"}

### 3. 基本設定 {#3-basic-settings}

画面の指示に従い、**画面のパスコード**、**管理者パスワード**、**Wi-Fi名**、**Wi-Fiパスワード**、**周波数帯**などの基本設定を行います。

**ヒント**: デフォルトの管理者パスワードは、デバイスのS/Nの末尾9文字に「#」を追加したものです。デフォルトのパスワードを使うか、独自のパスワードを設定できます。

### 4. インターネットの設定 {#4-internet-setup}

サポートされているインターネット接続方法（Cellular、Ethernet、Repeater、Tethering、USB Ethernet）のいずれかを使用してMudi 7を設定します。[Multi-WAN](../../interface_guide/multi-wan.md)機能を使用する場合は、複数のインターネット接続を設定してください。

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}
    
    Mudi 7 には**組み込み eSIM**と**デュアル Nano‑SIM**スロットが備わっています。eSIM パッケージを購入して（物理 SIM カード不要）インターネットへ接続することも、Nano‑SIM カードを挿入して 5G モバイルネットワークへアクセスすることもできます。

    **eSIM を設定する**:

    1. タッチスクリーンで **Cellular** -> **SIM Card Switch** に移動し、スイッチを切り替えて **eSIM** を有効にします。

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. [Web 管理パネル](./index.md#log-in-to-web-admin-panel)にログインし、**INTERNET** -> **Cellular** -> **eSIM Management** に移動します。

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. ポップアップウィンドウの下部にある **Add eSIM Profile** をクリックします。

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        **注意**: アップロードを行う前に、デバイスがインターネットに接続されていることを確認してください。ネットワークエラーが発生すると、eSIM 設定ファイルのアップロードに失敗します。

        QR コードまたはアクティベーションコードで eSIM プロファイルをアップロードし、**Install** をクリックします。多くの eSIM プロファイルは一度しかダウンロードして追加できない点に注意してください。

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Tips**: まだ eSIM プロファイルを購入していない場合は、eSIM Profile Recommended Store で購入できます。

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. アップロード後、**Cellular** に戻って **SIM Card Switch** をクリックします。

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        ポップアップウィンドウで **eSIM** をアクティブな SIM カードとして選択し、**Apply** をクリックします。

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. ルーターがこの eSIM プロファイルで接続を開始します。しばらく待って、接続に成功したか確認してください。

    **Nano‑SIM を設定する**:

    6. 背面カバーを外し、バッテリーを取り出して、Nano‑SIM カードをスロットに挿入してからバッテリーを戻します。

    7. ルーターはこの Nano‑SIM カードで自動的に接続を開始します。しばらく待って、接続に成功したか確認してください。

    インターネットに正常に接続されると、タッチスクリーンの右上にシグナルバーとcellularステータスが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[Cellularでインターネットに接続する](../../interface_guide/internet_cellular.md)を参照してください。

    !!! note

        1. 組み込みeSIMとSIM 2は相互に排他的であり、同時にアクティブにできません。eSIMはデフォルトで無効です。eSIMを有効にすると、SIMカードが挿入されていてもSIM 2は機能しません。
        2. Mudi 7には組み込みeSIMが備わっているため、SIMPoYo eSIM物理カードはMudi 7ではeSIM機能なしで通常のSIMカードとして認識されます。

=== "Ethernet"
    
    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. お使いの Mudi 7 のEthernetポートをEthernetケーブルで上流のネットワークソース（ISPモデム、ネットワークスイッチ、または壁のEthernetジャック）に接続します。
    2. タッチスクリーンまたはWeb管理パネルで、**Network** -> **Ethernet Ports**に移動し、ポートの役割を**WAN**に設定し、**Apply**をクリックします。

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. インターネットに正常に接続されると、タッチスクリーンの右上にEthernetポートアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[Ethernet cableでインターネットに接続する](../../interface_guide/internet_ethernet.md)を参照してください。

=== "Repeater"
    
    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. タッチスクリーンまたはWeb管理パネルで、**Internet** -> **Repeater**に移動し、**Connect**をクリックします。Mudi 7は利用可能なWi-Fiネットワークのスキャンを開始します。
    2. Mudi 7が拡張するWi-Fiネットワークを選択します。
    3. パスワードを入力し、**Apply**をクリックします。
    4. インターネットに正常に接続されると、タッチスクリーンの右上にWi-Fiアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[既存のWi-Fiネットワークでインターネットに接続する](../../interface_guide/internet_repeater.md)を参照してください。

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. モバイルデバイス（スマートフォンやUSB dongleなど）をUSB cableでMudi 7のUSB-Cポートに接続します。
    2. モバイルデバイスでSettingsを開き、**USB Tethering**を有効にします。iPhoneを使用する場合は、表示される場合は「Trust This Device」をタップします。
    3. タッチスクリーンにUSBモードの選択が表示されたら、**Host (USB OTG) mode** を選択します。Mudi 7はデバイスに自動的に接続します。接続しない場合は、上記の手順を繰り返すか、Web管理パネルにログインし、INTERNETページでTethering接続を確認してください。

        USBモードの違いについては、[こちら](https://docs.gl-inet.com/router/en/4/tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg)を参照してください。
    4. インターネットに正常に接続されると、タッチスクリーンの右上にチェーンリンクアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    詳細な手順については、[USBテザリングでインターネットに接続する](../../interface_guide/internet_tethering.md)を参照してください。

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7は**OTG対応**USB-Cポートを備えており、**別途販売されているUSB‑C‑to‑Ethernetアダプター**を使用して2番目のEthernetポートを追加し、Dual-Ethernet WANを可能にします。

    <small>*USB OTG（On-The-Go）は、ルーターなどの互換性のあるデバイスがホストと周辺機器の役割を切り替えて、個別のホストデバイスなしで直接データ伝送と電力交互作用を可能にするUSB標準です。</small>

    1. 上流のネットワークソース（ISPモデム、ネットワークスイッチ、または壁のEthernetジャック）をUSB C-to-Ethernetアダプター経由でMudi 7のUSB-Cポートに接続します。
    2. タッチスクリーンまたはWeb管理パネルで、**Network** -> **Ethernet Ports** -> **USB Ethernet Port**に移動し、ポートの役割を**WAN**に設定し、**Apply**をクリックします。

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7は自動的にデバイスに接続します。接続しない場合は、上記の手順を繰り返すか、Web管理パネルにログインしてINTERNETページでUSB Ethernet接続を確認します。

    4. インターネットに正常に接続されると、タッチスクリーンの右上にUSBアイコンとEthernetポートアイコンが表示されます。Web管理パネルで接続の詳細を確認することもできます。

    Mudi 7 の USB-C OTG の詳細については、[こちら](../../tutorials/what_is_usb-c_otg_and_how_to_share_your_network_via_usb-c_otg.md)をクリックしてください。


## ファームウェアのアップグレード {#firmware-upgrade}

!!! note "アップグレード前の注意"

    1. Mudi 7 の設定を保持したい場合は、アップグレードページで **Keep Settings** を選択してください。
    2. ダウングレード時は、互換性の問題が発生する可能性があるため **Keep Settings** を選択しないでください。
    3. ファームウェアのアップグレードには一定量のデータ通信が必要です。SIM カードのデータ容量に制限がある場合は、追加のデータ消費を避けるため、Repeater や USB Tethering など他の方法でルーターをインターネットへ接続することを推奨します。

Mudi 7 のファームウェアは、タッチスクリーンまたは Web 管理パネルからアップグレードできます。

### タッチスクリーンからアップグレードする {#upgrade-via-touchscreen}

1. Mudi 7 をインターネットへ接続します。

2. 接続後、システムが利用可能なファームウェア更新を自動的に確認します。新しいファームウェアがある場合は、画面にポップアップが表示されます。ポップアップで **Go to Upgrade** をタップして進みます。

    ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. ポップアップが表示されない場合は、ホーム画面で **More** -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade** をタップし、画面の指示に従ってファームウェアをアップグレードしてください。

    ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Web からアップグレードする {#upgrade-via-web}

Web管理パネルにログインし、**SYSTEM** -> **Upgrade** に移動します。ルーターのファームウェアは、オンラインまたはローカルでアップグレードできます。

詳細は[こちら](../../interface_guide/upgrade.md)を参照してください。

## 工場出荷時設定へのリセット {#factory-reset}

Mudi 7 をリセットする方法は 3 つあります。タッチスクリーン上で直接行う方法、Reset ボタンを使う方法、Web 管理パネルから行う方法です。

**注意**: リセットを実行する前に、Mudi 7 が完全に起動していることを確認してください。電源投入直後に Reset ボタンを押さないでください。U-Boot フェイルセーフモードが起動するおそれがあります。

この動画を視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### タッチスクリーンでリセットする {#reset-via-touchscreen}

1. ホーム画面で **More** をタップします。

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset1.png){class="glboxshadow" width="300"}

2. **More** ページの一番下までスクロールして **Reset** をタップします。

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset2.png){class="glboxshadow" width="300"}

3. 確認のため、もう一度 **Reset** をタップします。ルーターはリセットを開始し、その後再起動します。

    ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset3.png){class="glboxshadow" width="300"}

### ボタンでリセットする {#reset-via-button}

1. 背面カバーを外すと、下図のように Reset ボタンがあります。

    ![reset button](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

2. 必要に応じて、ソフトリセットまたは工場出荷時設定へのリセットを実行します。

    - **ソフトリセット**: データを消去せずにネットワーク接続を再起動したい場合は、Reset ボタンを **4 秒間**長押ししてから離し、ネットワーク修復を実行してください。押している間は画面上の案内を確認し、指示に従って操作してください。これにより、Wi-Fi 設定、VPN 設定（無効）、システム設定などを保持したまま、ネットワークインターフェースが再起動します。Wi-Fi が無効になっている場合、ソフトリセットにより Wi-Fi はデフォルトの有効状態に戻ります。ソフトリセットは、デバイスを非ルーターモードからルーターモードへ素早く切り替える用途にも使用できます。

    - **工場出荷時設定へのリセット**: Reset ボタンを **10 秒間**長押ししてから離すと、ハードリセットが実行されます。押している間は画面上の案内を確認し、指示に従って操作してください。これにより、すべての設定が削除されます。十分ご注意ください。

### Web からリセットする {#reset-via-web}

1. Web 管理パネルにログインし、**SYSTEM** -> **Reset Firmware** に移動します。

2. **Delete All and Reboot** をクリックします。ルーターはリセットを開始し、その後再起動します。

    ![web reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/web_reset.png){class="glboxshadow"}

## Web管理パネルにログインする {#log-in-to-web-admin-panel}

Mudi 7のWeb管理パネルにログインすると、より多くの設定を確認・変更できます。

まず、コンピューター、ノートPC、スマートフォンなどのデバイスを、Wi-Fi、Ethernetケーブル、またはUSBケーブルでMudi 7に接続します。

- **Wi-Fi**

    - <u>QRコード</u>: デバイスでMudi 7の画面に表示されているQRコードをスキャンし、デバイス上で「Join」をタップして接続します。
    - <u>手動接続</u>: デバイスでSettings -> WLANに移動し、利用可能なネットワーク一覧からMudi 7のWi-Fi名を選択して、パスワードを入力します。デフォルトのネットワーク名とパスワードは、ラベルに記載されています。

- **Ethernet**

    Ethernetケーブルで、デバイスをMudi 7のEthernetポート（デフォルトはLAN）に接続します。

- **USB**

    USBケーブルで、デバイスをMudi 7のUSB-Cポートに接続します。OTG対応のUSB-Cポートを使うと、次の手順でMudi 7のWebGUIにアクセスできます。

次に、Webブラウザーを開き、アドレスバーに `192.168.8.1` を入力してログインページにアクセスします。言語を選択し、管理者パスワードを設定して **Apply** をクリックします。

Mudi 7のWeb管理パネルにログインします。

以下は、Mudi 7のWeb管理パネルの機能概要です。


## Wireless {#wireless}

Wirelessページでは、6 GHz、5 GHz、2.4 GHz Wi-Fiネットワークの設定を構成できます。Wi-Fiの有効化、TX電力の設定、Wi-Fi名（SSID）の指定、ランダムBSSIDの有効化、Wi-Fiセキュリティモードとパスワードの選択、SSID可視性の設定、Wi-Fiモード、帯域幅、チャネルの選択が含まれます。

Wirelessの設定については、[Wireless](../../interface_guide/wireless.md)を参照してください。

**注意**: Mudi 7 の Wireless 設定には、他の GL.iNet Wi-Fi 7 ルーターと異なる点がいくつかあります。

1. チップセットのハードウェア制約により、5 GHzと6 GHz Wi-Fiを同時に有効にできません。
2. Repeaterが有効になっている場合、Guest Networkは自動的に無効になります。
3. 規制により、屋外で使用する場合はWi-FiをOutdoorモードに切り替えする必要があります。これにより、カバー範囲が減少する可能性があります。Wirelessページの上部で、使用環境（IndoorまたはOutdoor）を切り替えることができます。

## Clients {#clients}

Clients ページには、接続中のデバイスに関する情報が表示されます。各クライアントについて、名前、IPアドレス、MACアドレス、ダウンロード速度、アップロード速度、合計トラフィックを確認でき、クライアントをブロックしたり、その他の操作を実行したりできます。

Clientsの設定については、[Clients](../../interface_guide/clients.md)を参照してください。

## クラウドサービス {#cloud-services}

=== "GoodCloud"

    GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"}クラウド管理サービスは、GL.iNetルーターに簡単かつシンプルにリモートアクセスと管理を提供します。
    
    GoodCloudの設定については、[GoodCloud](../../interface_guide/cloud.md)を参照してください。

=== "AstroWarp"

    AstroWarp は、シームレスなリモートネットワーク接続とリモートデバイス管理を実現する高度なネットワーキングプラットフォームです。GL.iNet ルーターとの連携に特化しており、ネットワーク全体のデバイス管理をサポートし、上位・下位デバイスの制御も可能にします。将来的なハードウェアレベル制御にも対応できる設計で、安全かつ安定したネットワークを維持するための堅牢で信頼性の高いソリューションを提供します。
    
    AstroWarpの設定については、[AstroWarp](../../interface_guide/astrowarp.md)を参照してください。

## VPN {#vpn}

VPN（仮想プライベートネットワーク）は、デバイスとVPNサーバー間の安全で暗号化されたトラフィックを作成します。VPNクライアントとしてプライバシーとセキュリティの追加レイヤーを提供し、VPNサーバーとしてリモートネットワークにアクセスできます。Mudi 7はOpenVPNとWireGuardをサポートしています。

=== "OpenVPN"
    
    Mudi 7（およびその他の GL.iNet ルーター）は、高いセキュリティを提供する OpenVPN プロトコルをサポートしています。OpenVPN を設定するには、以下のチュートリアルを参照してください。

    * [OpenVPNクライアントの設定方法](../../interface_guide/openvpn_client.md)
    * [OpenVPNサーバーの設定方法](../../interface_guide/openvpn_server.md)

=== "WireGuard"
    
    Mudi 7（およびその他の GL.iNet ルーター）は、高速で使いやすい WireGuard プロトコルをサポートしています。WireGuard を設定するには、以下のチュートリアルを参照してください。

    * [WireGuardクライアントの設定方法](../../interface_guide/wireguard_client.md)
    * [WireGuardサーバーの設定方法](../../interface_guide/wireguard_server.md)

## ネットワーク {#network}

=== "Multi-WAN"

    Multi-WANは、ルーターに複数のインターネット接続（ethernet、repeater、tethering、cellular、USB ethernetなど）を同時に設定できるネットワーキング機能です。現在のインターネット接続が失敗すると、ルーターは自動的に別のインターネット接続に切り替えます。これにより、スムーズで途切れないインターネットアクセスが確保されます。

    Multi-WANの設定については、[Multi-WAN](../../interface_guide/multi-wan.md)を参照してください。

=== "LAN"

    LAN（Local Area Network）は、自宅やオフィスなどの限られた物理的な範囲内でコンピューターやデバイスを接続するネットワークです。高速なデータ転送とリソース共有を可能にし、デバイス同士が効率的に通信できます。
    
    LANの設定については、[Lan](../../interface_guide/lan.md)を参照してください。

=== "Guest Network"

    IPv4プライベートアドレス範囲192.168.0.0/16、172.16.0.0/12、または10.0.0.0/8内でサブネットを設定し、ゲートウェイとネットマスクIPアドレスを指定し、ゲストネットワークのAP分離などのセキュリティ設定を構成できます。

    ゲストネットワークの設定については、[Guest Network](../../interface_guide/guest_network.md)を参照してください。

---

=== "DNS"

    DNSページでは、カスタムDNSサーバーを設定し、DNSリバインディング攻撃保護を有効にしてすべてのクライアントのDNS設定を上書きし、カスタムDNSがVPN DNSを上書きできるようにし、Ethernet接続からDNSサーバーを自動的に指定するか手動で指定するモードを構成できます。

    DNSの設定については、[DNS](../../interface_guide/dns.md)を参照してください。

=== "Ethernet Port"

    Ethernet Portページでは、Ethernetポートの役割（WAN/LANとして使用）の設定、WANインターフェースのMACモードとMACアドレスの切り替え、ネゴシエーション済みポート速度の表示を行うことができます。

    Mudi 7には単一のEthernetポートが備わっており、デフォルトでLANです。必要に応じて、タッチスクリーンまたはWeb管理パネルでWANポートに切り替えできます。

    Ethernetポートの管理については、[Port Management](../../interface_guide/ethernet_port.md)を参照してください。

=== "IPv6"

    IPv6（Internet Protocol version 6）は、IPv4 を置き換えるために設計された最新のインターネットプロトコルです。ほぼ無制限の固有IPアドレスを提供する広大なアドレス空間を備え、インターネット接続デバイスの増加に対応するうえで不可欠です。
    
    IPV6の設定については、[IPV6](../../interface_guide/ipv6.md)を参照してください。

---

=== "IGMP Snooping"

    IGMPスヌーピングは、イーサネットスイッチでマルチキャストトラフィックを管理および制御するために使用されるネットワーク最適化技術です。
    
    IGMPスヌーピングの設定については、[IGMP Snooping](../../interface_guide/igmp_snooping.md)を参照してください。

=== "Network Mode"

    ネットワークモードは、デバイスがネットワークへ接続し、他のデバイスと通信する方法を決定する構成です。
    
    ネットワークモードの設定については、[Network Mode](../../interface_guide/network_mode.md)を参照してください。

    **注意**: Mudi 7はRouter、Access Point、Extenderモードをサポートします。WDSモードはサポートされていません。

=== "Drop-in gateway"

    ドロップインゲートウェイは、AdGuard Home、暗号化DNS、VPNクライアントを含むメインルーターの機能を拡張します。
    
    ドロップインゲートウェイの設定については、以下のリンクを参照してください：
    
    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [ドロップインゲートウェイの設定方法](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Network Acceleration"

    ネットワークアクセラレーションは、CPU負荷を削減し、トラフィックパケットの転送を高速化できます。
    
    ネットワークアクセラレーションの設定については、[Network Acceleration](../../interface_guide/network_acceleration.md)を参照してください。

## フロー制御 {#flow-control}

=== "Parental Control"

    Parental Controlは、子どものデバイスを管理および制御するために設計されています。スクリーン時間の制限や特定コンテンツへのアクセス制限が含まれます。

    保護者による制御の設定については、[Parental Control](../../interface_guide/parental_control.md)を参照してください。

## セキュリティ {#security}

=== "Port Forwarding"

    ポートフォワーディングにより、リモートサーバーとインターネット上のデバイスがプライベートネットワーク上のデバイスにアクセスできます。
    
    ポートフォワーディングの設定については、[Port Forwarding](../../interface_guide/port_forwarding.md)を参照してください。

=== "Management Control"

    Management Controlでは、ネットワークとルーターを不正アクセスから保護するためのさまざまなセキュリティ設定を構成できます。このページには以下のオプションがあります：

    * ローカルアクセス制御：ローカルネットワークに接続されたデバイスからルーターのインターフェースへのアクセスを管理および制限します。
    * リモートアクセス制御：インターネット上のリモート場所からルーターのインターフェースへのアクセスを構成および制限し、外部脅威に対するセキュリティを強化します。
    * ルーターで開いているポート：ルーター上で開いているポートを制御し、潜在的な脆弱性と不正アクセスを制限します。

    これらの設定は、ネットワーク環境を安全に保ち、ルーターと接続されたデバイスを保護するのに役立ちます。

    詳細な手順については、[Security](../../interface_guide/security.md)を参照してください。

=== "NAT Mode"

    NAT Modeページでは、Full Cone NATとSIP ALG機能を有効または無効にできます。

    NAT設定については、[NAT Mode](../../interface_guide/nat_settings.md)を参照してください。

## アプリケーション {#applications}

=== "Plug-ins"

    プラグインは、既存のコンピュータプログラムに特定の機能または機能を追加するソフトウェアコンポーネントであり、カスタマイズと機能拡張を可能にします。
    
    プラグインの設定については、[Plug-ins](../../interface_guide/plugins.md)を参照してください。

=== "Dynamic DNS"

    Dynamic DNS（DDNS）は、ドメインに関連付けられたIPアドレスをリアルタイムで自動的に検出およびアップデートします。ドメイン名をルーターの動的なパブリックIPアドレスに対応付けるため、固定IPアドレスがなくてもネットワークにリモートアクセスできます。
    
    Dynamic DNSの設定については、[Dynamic DNS](../../interface_guide/ddns.md)を参照してください。

=== "Network Storage"

    ネットワークストレージとは、複数のユーザーとデバイスがネットワーク上でファイルにアクセスして共有できる集中型データストレージソリューションを指します。
    
    ネットワークストレージの設定については、[Network Storage](../../interface_guide/network_storage.md)を参照してください。

---

=== "AdGuard Home"

    AdGuard Homeは、ネットワーク全体の広告およびトラッカーブロッキングソリューションであり、家庭内ネットワークに接続されたすべてのデバイスで不要なコンテンツをフィルタリングするDNSサーバーとして機能します。
    
    AdGuard Homeの設定については、[AdGuard Home](../../interface_guide/adguardhome.md)を参照してください。

=== "ZeroTier"

    ZeroTierは、ソフトウェア定義ネットワーキングソリューションであり、インターネット上で安全に仮想ネットワークを作成し、デバイスが同一のローカルネットワーク上にあるかのように接続できます。
    
    ZeroTierの設定については、[ZeroTier](../../interface_guide/zerotier.md)を参照してください。

=== "Tailscale"

    Tailscaleは、どこからでもデバイスやアプリケーションにアクセスできるVPNサービスです。
    
    Tailscaleの設定については、[Tailscale](../../interface_guide/tailscale.md)を参照してください。

=== "Tor"

    Tor（The Onion Routerのやや称）は、匿名通信を可能にするプライバシー重視のネットワークです。ユーザーの位置情報と使用状況を不明瞭にするために、一連のボランティアが運用するサーバー（ノード）を介してインターネットトラフィックをルーティングします。
    
    * [Torの設定方法](../../interface_guide/tor.md)

## システム {#system}

=== "Overview"

    Overviewページは、ルーターの現在のパフォーマンス指標とステータスのを含むスナップショットを提供します。このページでは以下を表示できます：

    * CPU平均負荷：ルーターのCPUの平均負荷を監視し、パフォーマンスの評価と潜在的なボトルネックの特定に役立ちます。
    * メモリ使用量：ルーターのメモリ使用量を確認し、リソース管理に役立ちます。
    * LEDコントロール：ルーターのLEDライトのオン/オフを切り替え、デバイスの視覚インジケーターのカスタマイズを可能にします。
    * フラッシュ使用量：ルーターのフラッシュストレージの使用率を確認し、ファームウェアと設定データのための十分な空間を確保します。
    * デバイス情報：ルーターのシステムに関する詳細情報（アップタイム、ホスト名、モデル、アーキテクチャ、OpenWrtバージョン、カーネルバージョン、デバイスID、デバイスMAC、デバイスS/N）にアクセスします。
    * 外部ストレージ：ルーターに接続されたUSBドライブやTFカードなどの外部ストレージデバイスの状態を確認します。
    
    これらの機能は、ルーターの操作を効果的に管理および監視するのに役立つ重要な洞察とコントロールを提供します。

    詳細な設定手順と詳細については、[Overview](../../interface_guide/system_overview.md)を参照してください。

=== "Admin Password"

    Admin Passwordページでは、ルーターの管理インターフェースのパスワードを設定または変更できます。

    管理者パスワードは、次の要件を満たす必要があります。

    * 10文字以上63文字以下。
    * 文字（大文字小文字を区別）、数字、記号`` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ ``を使用できます。
    * 大文字、小文字、数字、記号のうち少なくとも2種類が必要です。

=== "Upgrade"

    Upgrade ページでは、ルーターのファームウェアを最新バージョンへ更新できます。これにより、性能向上、セキュリティ強化、新機能の利用が可能になります。このページには次の2つのアップグレード方法があります。

    * ファームウェアオンラインアップグレード：メーカーのサーバーで最新のファームウェアバージョンを自動的に確認します。オンラインで利用できる場合はインストールできます。
    * ファームウェアローカルアップグレード：コンピューターからファームウェアファイルをアップロードしてルーターをアップデートし、アップグレードバージョンとタイミングを制御できます。

    これらのオプションにより、最新の改善や修正を適用した状態にルーターを保てます。

    詳細な設定手順と詳細については、[Upgrade](../../interface_guide/upgrade.md)を参照してください。

---

=== "Scheduled Tasks"

    Scheduled Tasksページでは、ルーターを指定した間隔で自動的に再起動するように設定でき、最適なパフォーマンスと安定性の維持に役立ちます。

    詳細な設定手順と詳細については、[Scheduled Tasks](../../interface_guide/scheduled_tasks.md)を参照してください。

    **注意**: Mudi 7はLED表示スケジュールとWi-Fiステータススケジュールをサポートしていません。

=== "Display Management"

    Display Managementページでは、タッチスクリーン表示とその関連設定を管理できます。
    
    - 壁紙：壁紙とウェイク表示スタイルをカスタマイズします。
    - 明るさ：タッチスクリーンの明るさを調整します。スライダーを使用するか、パーセンテージを入力して、さまざまな照明条件に合わせます。
    - パーソナル署名：タッチスクリーンにカスタムテキストを追加して、独自のスタイルを表示したり簡単な識別を可能にします。
    - 自動ロック：アクティビティがない場合にスクリーンが自動的にロックされるまでの遅延時間を設定します。範囲は15秒から5分です。
    - パスコード：セキュリティのレイヤーを追加するために、タッチスクリーンにパスコードを設定します。

    詳細な設定手順と詳細については、[Display Management](../../interface_guide/display_management.md)を参照してください。

=== "USB & Power"

    USB & Powerページでは、USBプロトコル、給電方向、アイドルタイムアウト、スタンバイ動作など、ルーターのUSB関連設定と電源管理を設定できます。

    詳細な手順については、[USB & Power](../../interface_guide/usb_power.md)を参照してください。

---

=== "Time Zone"

    Time Zoneページでは、ルーターの正しいタイムゾーンを設定でき、すべてのスケジュールタスク、ログ、システムイベントが現地時間に従って正確にタイムスタンプ付けられます。この設定は、正確な記録の維持と、時間ベースの構成の適切な実行に不可欠です。

    詳細な設定手順と詳細については、[Time Zone](../../interface_guide/time_zone.md)を参照してください。

=== "Reset Firmware"

    Reset Firmwareページでは、ルーターの現在のファームウェアバージョンをデフォルト設定にリセットし、すべてのカスタム設定を消去できます。このプロセスは、現にインストールされているファームウェアバージョンのデフォルト設定にルーターを復元します。持続的な問題のトラブルシューティングや現在のファームウェアのデフォルト設定で新鮮に開始するのに便利です。

    詳細な設定手順と詳細については、[Reset Firmware](../../interface_guide/reset_firmware.md)を参照してください。

=== "Log"

    Logページは、ルーターのアクティビティとイベントを記録するさまざまなログへのアクセスを提供し、トラブルシューティングとパフォーマンスの監視を支援します。このページには以下が含まれます：

    * システムログ：システムレベルのイベントとアクティビティの詳細なログ。
    * カーネルログ：カーネルの操作とイベントに関連するログ。
    * クラッシュログ：システムクラッシュとエラーの記録。重大な問題の診断に便利です。
    * クラウドログ：ルーターに統合されたGoodCloudサービスに関連するインタラクションとアクティビティのログ。
    * Nginxログ：ルーターで使用されている場合は、Nginx Webサーバーからのログ。Webトラフィックとサーバー操作の詳細。
    
    さらに、ページにはExport Logボタンがあり、収集したすべてのログをエクスポートして技術サポートの分析にできます。この機能は、複雑な問題の診断と専門のサポートの取得に非常に便利です。

    詳細な設定手順と詳細については、[Log](../../interface_guide/log.md)を参照してください。

=== "Advanced Settings"

    Advanced Settings ページでは、OpenWrt LuCI インターフェースを通じて高度な設定オプションにアクセスできます。経験豊富なユーザーは、基本インターフェースの範囲を超えて、詳細なネットワーク設定、ファイアウォール設定、その他の高度なシステムカスタマイズを行えます。

    詳細な設定手順と詳細については、[Advanced Settings](../../interface_guide/advanced_settings.md)を参照してください。

## バッテリーの安全性 {#battery-safety}

バッテリーが膨張している、液漏れしている、異常に熱い、損傷している、または異臭がする場合は、Mudi 7 の使用と充電を中止してください。

- バッテリーを押す、曲げる、穴を開ける、押しつぶすなど、圧力を加える行為をしないでください。
- 膨張したバッテリーや損傷したバッテリーを、工具でこじって取り外そうとしないでください。
- バッテリーが膨張している、取り外せない、液漏れしている、熱い、または安全に扱えない場合は、取り外そうとしないでください。
- 損傷したリチウムイオンバッテリーを家庭ごみや通常のリサイクルに出さないでください。
- 膨張したバッテリーや損傷したバッテリーを、通常の郵便や宅配便で送らないでください。
- 保証に関するサポートと今後の対応について、[GL.iNet サポート](https://www.gl-inet.com/contacts/)にお問い合わせください。

損傷したバッテリーをすでに取り外している場合は、再度取り付けないでください。損傷したリチウムイオンバッテリーを受け入れる、お住まいの地域の適切なバッテリーリサイクル施設または家庭から出る有害廃棄物の回収施設にお問い合わせください。

バッテリーから煙が出ている、急速に熱くなっている、シューという音がする、燃えているなど、差し迫った危険がある場合は、デバイスから離れ、地域の緊急通報先に連絡してください。
