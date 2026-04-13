# 既存の Wi-Fi にリピーターで接続してインターネットを利用する

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

リピーターは、ホテルやカフェの無料 Wi-Fi など、既存の無線ネットワークにルーターを接続する機能です。

デフォルトでは WISP（Wireless Internet Service Provider）モードで動作します。つまり、ルーターは独自のサブネットを作成し、ファイアウォールとして機能して公衆ネットワークからユーザーを保護します。

## 基本手順

ルーターの Web 管理パネルにログインし、**INTERNET** -> **Repeater** に移動して **Connect** をクリックします。

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

利用可能なネットワークリストから、接続したい Wi-Fi ネットワークを選択します。

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**注意**: このページには、ルーターがサポートしている Wi-Fi チャネルが表示されます。接続先 Wi-Fi がそのいずれかのチャネルを使用していることを確認してください。対応していないチャネルを使っている場合、利用可能なネットワークリストに表示されないことがあります。

正しい Wi-Fi パスワードを入力して **Apply** をクリックします。

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

接続したい Wi-Fi の SSID が Available Network リストにない場合は、右上の **Join Other Network** をクリックし、Wi-Fi SSID と必要な情報を手動で入力します。詳しい手順は [こちら](#join-other-network) を参照してください。

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

ホテル、空港、ショッピングモールなどの公衆ホットスポットへ接続する場合は、[公衆ホットスポット向け設定](#for-public-hotspot) を参照してください。

その他の設定については、[詳細設定](#advanced-settings) を参照してください。

しばらく待ち、パスワード入力が正しければ接続が完了します。

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## 公衆ホットスポット向け設定 {#for-public-hotspot}

キャプティブポータル付きの公衆ホットスポットにルーターを接続する場合は、以下の機能を有効にすると接続成功率の向上に役立ちます。

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    この機能は v4.6 以降で利用できます。

    このオプションを有効にすると、ホットスポットへの接続には成功したもののインターネットには接続できない場合、自動的に Login Mode for Public Hotspots に入ります。**このモードでは、一部のサービスが停止し、DNS モードが自動に切り替わるため、ネットワークアクティビティがホットスポット提供者（ホテルやショッピングモールなど）に漏れる可能性があります。**

    このオプションを有効にしていなくても、ホットスポット内にキャプティブポータルが検出され、ログインに失敗した場合は、このモードへ切り替えるよう促されます。

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    有効にすると、管理パネルへのアクセスに使用しているクライアントデバイスの MAC アドレスをエミュレートし、そのデバイスになりすまして接続します。

- **MAC Mode**

    ルーターが公衆ホットスポットへ接続するときに使う MAC を選択できます。

    - **Factory**: 工場出荷時に割り当てられた元の MAC アドレスを使用します。

    - **Clone**: クライアントデバイスの MAC アドレスを複製して接続します。目的の MAC がリストにない場合は、複製したいアドレスを手動で入力してください。

        注意: 最近の多くのデバイスは、Wi-Fi へ接続する際にランダム化 MAC アドレス（Private Wi-Fi Address や random hardware address と呼ばれることがあります）を使用します。そのため、ここに表示される MAC アドレスは、デバイスの実際の物理 MAC アドレスと一致しない場合があります。

    - **Random**: 接続用のランダムな MAC アドレスを自動生成します。

    ネットワーク設定を保存すると、MAC Mode（複製またはランダム化した MAC アドレスを含む）は保存した SSID ごとに関連付けられます。これらの設定は、各 SSID に対していつでも手動で変更できます。

- **Auto Update MAC**: このオプションを有効にすると、MAC を自動更新できます。

## 詳細設定 {#advanced-settings}

ネットワークへ参加する際には、追加のオプションも利用できます。

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: 有効にすると、現在中継している Wi-Fi ネットワークを記憶します。

* **Lock BSSID**: 有効にすると、他の AP が同じ SSID を共有していても、選択した BSSID に対応する特定のアクセスポイント（AP）にのみ接続します。

* **Manually Set Static IP**: 有効にすると、自動取得の代わりに、ルーターのリピーター接続に使用する固定 IPv4 アドレス、ネットマスク、ゲートウェイ、DNS サーバーを手動で設定できます。

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL（Time To Live）は、パケットがネットワーク内で生存できる最大時間を定義します。通常は通信事業者の要件に応じて設定します。デフォルトでは、ルーターはクライアントデバイスから受信した TTL から 1 を引いた値を転送します。カモフラージュが必要な場合は、ここで固定値を設定できます。TTL は IPv4 でのみ有効です。

* **HL**: IPv6 では、HL（Hop Limit）フィールドがネットワーク内でのデータパケットの転送ホップ数を制限し、IPv4 の TTL に相当します。

* **MTU**: デフォルト値は 1500 です。

## リピーターオプション

リピーターのオプションを表示するには、接続済みの Repeater セクション右上にある歯車アイコンをクリックします。

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**ファームウェア v4.8** では、Repeater Options ページは次のように表示されます。

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**:

    - No Switching mode: 有効にすると、現在の Wi-Fi が切断されても、他の保存済みネットワークへ自動接続しません。

    - Auto Switching mode: 有効にすると、現在の Wi-Fi が切断されたときに、他の保存済みネットワークへの接続を試みます。

    - Auto Switching Without Network: 有効にすると、ルーターが非リピーターモードで正常にネットワーク接続されている間は自動スキャンを行わず、ルーターがネットワーク未接続のときだけ他の保存済みネットワークへの自動切り替えを試みます。これにより通信パケットの損失を避けられます。

- **Band Selection**: Auto、5 GHz、2.4 GHz の3つから選択できます。

    手動でバンドを選択した場合、ルーターは別のバンドを使用する Wi-Fi をスキャンしたり接続したりしません。

**ファームウェア v4.7 以前** では、Repeater Options ページは次のように表示されます。

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. このオプションを有効にすると、現在の Wi-Fi ネットワークへ接続できなくなった際に、他の保存済みネットワークへ自動的に接続します。

* **Band Selection**. 手動でバンドを選択した場合、別のバンドを使用する Wi-Fi はスキャンも接続もしません。

## 既知のネットワークの管理

既知のネットワークを削除するには、**Switch Network** をクリックします。

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

または、ネットワークが接続されていない場合は Repeater セクションの **Connect** をクリックします。

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

**Known Networks** セクションで、ゴミ箱アイコンをクリックすると既知のネットワークを削除でき、歯車アイコンをクリックするとそのネットワークを設定できます。

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Join Other Network {#join-other-network}

SSID が Available Networks リストにない場合、または SSID が非表示の場合は、**Join Other Network** をクリックします。

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

SSID を入力し、Security を選択して、必要に応じてパスワードを入力します。

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

**Security** の設定は、モデルによって2つまたは3つの選択肢があります。

* None：パスワードは不要です。
* WPA/WPA2/WPA3：一般的で、ほぼすべての Wi-Fi ネットワークでサポートされています。
* WPA/WPA2/WPA3 Enterprise：認証に EAP（Extensible Authentication Protocol）が必要です。接続には有効なユーザー名とパスワードが必要で、通常は企業ネットワークや学校ネットワークで使われます。

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    EAP ネットワークを中継する詳しい手順は、[こちら](../tutorials/eap.md){target="_blank"}を参照してください。

## 再接続

以下のような場合、ルーターは一定間隔で自動的に Wi-Fi への再接続を試みます。必要に応じて手動で無効にすることもできます。SSID やパスワードの誤りが原因の場合は、Known Networks から該当ネットワークを削除して解消してください。

1. Repeater 設定時に誤った SSID/パスワードを入力した場合。

2. 初回接続後に上流ルーターの電波範囲外へ移動した場合。

3. 上流ルーターで SSID/パスワードが変更された、または接続後にアクセス制限がかかった場合。

再接続処理には、待機フェーズ、スキャンフェーズ、接続フェーズの3段階があります。

1. 待機フェーズ: 問題がない状態で、ルーターは再接続条件を待機します。

2. スキャンフェーズ: スキャン対象の周波数帯でパケットロスが発生することがあります。新規デバイスの接続に支障が出る場合があります。GL-AXT1800/GL-AX1800 では、Guest Wi-Fi が一時的に無効になります。

3. 接続フェーズ: 対象バンドのメイン Wi-Fi が再接続の際に数秒間切断される場合があります。

**注意**: 問題が起こりやすいのは、通常スキャンフェーズと接続フェーズです。

## トラブルシューティング

ルーターがリピーターとして Wi-Fi ネットワークに接続されている状態でインターネットを利用できない場合、次のような黄色いメッセージが表示されます。

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

この問題を解決するには、次を確認してください。

1. 上流機器（つまりルーターが接続している Wi-Fi ネットワーク）にインターネットアクセスがあるか確認します。

2. [Multi-WAN](multi-wan.md) ページで Repeater インターフェースの状態を確認します。

## DFS

上流の 5G Wi-Fi に接続すると、ルーターの Wi-Fi も上流 Wi-Fi に合わせて DFS チャネルを使用するかどうかが決まります。

* 上流 Wi-Fi が DFS チャネルを使用していてスキャン可能な場合、ルーターの 5G Wi-Fi も同じチャネルを使用します。

* 上流 Wi-Fi がスキャンできない場合、または接続に失敗した場合は、ルーターの 5G Wi-Fi は非 DFS チャネルへ切り替わります。

??? "対応モデル"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "非対応モデル"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

関連記事

- [インターネットページ](internet.md)
- [各インターネット接続方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネット接続方法を同時に使用する場合、ロードバランスをどのように設定しますか？](multi-wan.md)
- [LAN と Wi-Fi の MAC アドレスを確認する方法](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
