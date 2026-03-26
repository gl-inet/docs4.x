# リピーター経由で既存のWi-Fiに接続

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

リピーターを使用するということは、ホテルやカフェで無料Wi-Fiを使用する場合など、既存の彼の無線ネットワークにルーターを接続することです。

デフォルトではWISP（Wireless Internet Service Provider）モードで動作します。これは、ルーターが独からのサブネットを作成し、ファイアウォールとして機能してパブリックネットワークからあなたを保護することを意味します。

## 基本のな手順

ルーターのウェブ管理パネルにログインし、**インターネット** -> **リピーター**セクションに移動し、**接続**をクリックします。

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

利用可能なネットワークリストから接続したいWi-Fiネットワークを選択します。

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**注意**: ページにはルーターがサポートするWi-Fiチャンネルが表示されます。接続先のWi-Fiネットワークがこれらのチャンネルのいずれかを使用していることを確認してください。 そうでない場合は、利用可能なネットワークリストに表示されない場合があります。

正しいWi-Fiパスワードを入力し、**適用**をクリックします。

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

接続したいWi-Fi SSIDが利用可能なネットワークリストにない場合は、右上の**彼のネットワークに参加**をクリックし、Wi-Fi SSIDと必要なその彼の情報を手動で入力します。詳細な手順については[こちら](#join-other-network)をご覧ください。

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

ホテル/空港/モールなどで提供されるパブリックホットスポットへの接続については、[パブリックホットスポットへけ](#for-public-hotspot)をご覧ください。

その彼の設定については、[詳細設定](#advanced-settings)をご覧ください。

しばらくすると、パスワード入力が正しければ接続が成功します。

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## パブリックホットスポットへけ

キャプティブポータル付きのパブリックホットスポットにルーターを接続する場合、以下の機能を有効にすると接続成功率をへ上させることができます。

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **パブリックホットスポットのログインモードをから動有効にする**

  この機能はv4.6で降で利用可能です

  このオプションが有効な場合、このルーターはホットスポットには接続されているがインターネットには接続されていないとき、自動的にパブリックホットスポットのログインモードに入ります。**このモードでは、いくつかのサービスが一時停止され、DNSモードは自動的に切り替わります**。これにより、ネットワークアクティビティがホットスポットプロバイダー（例：ホテルやショッピングセンター）に漏れる可能性があります。

  このオプションが有効になっていない場合でも、ルーターはホットスポットでキャプティブポータルを検出し正常にログインできない場合に、このモードに入るように促します。

  ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **カモフラージュを有効にする**

  有効にすると、ルーターは管理パネルにアクセスするために使用するクライアントデバイスのMACアドレスを模倣することで、そのMACアドレスを伪装します。

- **MACモード**

  ルーターがパブリックホットスポットへの接続に使用するMACを選択できます。
  - **工場**: デバイスに割り当てられた元のMACアドレスを使用します。

  - **クローン**: 接続のためにクライアントデバイスのMACアドレスをクローンします。希望のMACがリストに存在しない場合、クローンしたいアドレスを手動で入力します。

    注意: 多くの 最新 デバイスはWi-Fiネットワークに接続るときにランダム化されたMACアドレス（しばしばプライベートWi-Fiアドレスまたはランダムハードウェアアドレスと呼ばれる）を使用します。このため、ここに表示されるMACアドレスがデバイスの実際の物理MACと一致しない場合があります。

  - **ランダム**: 接続のためにランダムなMACアドレスを自動的に生成します。

  ネットワーク設定を保存のとき、MACモード（クローン/ランダム化されたMACアドレスを含む）は 保存する特定のSSIDに紐付けられます。各SSIDの設定はいつでも手動で変更できます。

- **MACをから動アップデート**: このオプションが有効な場合、MACは自動的にアップデートできます。

## 詳細設定

ネットワークに参加するとき、いくつかの追加オプションがあります。

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

- **記憶**: これにより、現にの重复Wi-Fiネットワークを記憶します。

- **BSSIDを固定**: 有効にすると、彼のAPが同じSSIDを共有している場合でも、ルーターは選択したBSSIDに対応する特定のアクセスポイントにのみ接続します。

- **手動で静のIPを設定**: 有効にすると、ルーターのリピーター接続に対してIPv4アドレス、ネットマスク、ゲートウェイ、DNSサーバーを手動で設定でき、これらの設定自動的に取なければならないするのではなくなります。

  ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

- **TTL**: TTL（Time To Live）はパケットがネットワークで生存できる最大時間を設定し、運用商の要件に従って入力されます。デフォルトでは、ルーターは着信クライアントデバイスのTTLを1減衰させて転送します。伪装する必要がある場合は、ここで固定値を設定できます。TTLはIPv4のみ有効です。

- **HL**: IPv6では、HL（Hop Limit）フィールドはネットワーク内のデータパケットの伝送ホップ数を制限するために使用され、IPv4のTTLに相当します。

- **MTU**: デフォルト値は1500です。

## リピーターオプション

接続されたリピーターセクションの右上の歯車アイコンをクリックして、リピーターオプションを表示します。

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

** firmware v4.8の場合**、リピーターオプションページは以下のようになります。

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **彼のネットワークへの切り替えを許可**:
  - 切り替えなしモード: 切り替えなしモードが有効な場合、現にのWi-Fiが切断されても彼の保存されたネットワークには自動的に接続しません。

  - から動切り替えモード: から動切り替えモードが有効な場合、現にのWi-Fiが切断されるとルーターは彼の保存されたネットワークへの接続を試みます。

  - ネットワークなしから動切り替え: ネットワークなしから動切り替えモードが有効な場合、ルーターは非リピーターモードで正常にネットワーク化されている間は自動的にネットワークをスキャンせず、ルーターがネットワークがないときにのみ彼の保存されたネットワークへのから動切り替えを試みます。これにより通信パケットの損失を避けることができます。

- **バンド選択**: 3つのオプションから選択できます：から動、5 GHz、2.4 GHz。

  バンドを手動で選択すると、ルーターは彼のバンドを使用しているWi-Fiをスキャンまたは接続しません。

** firmware v4.7で前の場合**、リピーターオプションページは以下のようになります。

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

- **彼の保存されたネットワークへの切り替えを許可**: このオプションが有効な場合、ルーターは現にのWi-Fiネットワークに接続できない場合、彼の保存されたネットワークに自動的に接続します。

- **バンド選択**: バンドを手動で選択すると、ルーターは彼のバンドのWi-Fiをスキャンまたは接続しません。

## 既知のネットワークを管理

既知のネットワークを削除するには、**ネットワークを切り替え**をクリックします。

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

または、接続されていない場合は**接続**をクリックします。

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

**既知のネットワーク**セクションで、ごみ箱アイコンをクリックして既知のネットワークを削除するか歯車アイコンをクリックしてネットワークを設定します。

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## 彼のネットワークに参加

SSIDが利用可能なネットワークリストにない場合、またはSSIDが非表示になっている場合は、**彼のネットワークに参加**をクリックします。

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

SSIDを入力し、セキュリティを選択してパスワードを入力します（必要な場合）。

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

**セキュリティ**設定には、モデルに応じて2つまたは3つのオプションがあります。

- なし：パスワードが不要であることを意味します。
- WPA/WPA2/WPA3：一般のでほとんどすべてのWi-Fiネットワークでサポートされています。
- WPA/WPA2/WPA3 Enterprise：認証にExtensible Authentication Protocol（EAP）が必要です。接続するには有効なユーザー名とパスワードが必要です（通例、ビジネスまたはキャンパスネットワークで使用）。

  ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

  EAPネットワークのリピーティングの詳細なガイドについては、[こちら](../tutorials/eap.md){target="\_blank"}をクリックしてください。

## 再接続

次の場合、ルーターは定期のにWi-Fiへの再接続を試みます。必要に応じて手動でこれを無効にできます。SSID/パスワードエラーの場合は、既知のネットワークからネットワークを削除して解決してください。

1. リピーター設定中に正しくないSSID/パスワードを入力した。

2. 最も初の接続後、上ストリームルーターのWi-Fi圏外に移動した。

3. 上ストリームルーターがSSID/パスワードを変更したか、接続後にアクセスを制限した。

再接続プロセスには3つの異なるフェーズがあります：待機フェーズ、スキャンフェーズ、接続フェーズ。

1. 待機フェーズ: 問題なし - ルーターは再接続条件を待機します。

2. スキャンフェーズ: スキャンされた周波数帯でパケット損失が発生する可能性があります。新しいデバイスは接続の問題に直面する可能性があります。モデルGL-AXT1800/GL-AX1800の場合、ゲストWi-Fiは一時的に無効になります。

3. 接続フェーズ: ターゲットバンドのメインビジネスWi-Fiは、再確立中に数秒間切断される場合があります。

**注意**: 問題は通例、スキャンおよび接続フェーズで発生します。

## トラブルシューティング

ルーターがリピーターとしてWi-Fiネットワークに接続されているときに、インターネットが利用できない場合、以下の黄色のメッセージが表示されます。

**「インターフェースは接続されていますが、インターネットにアクセスできません。」**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

この問題を解決するには：

1. 上ストリームデバイス（つまり、ルーターが接続されているWi-Fiネットワーク）にインターネットアクセスがあるか確認します。

2. [マルチWAN](multi-wan.md)ページに移動してリピーターインターフェースのステータスを確認します。

## DFS

上游5G Wi-Fiに接続するとき、ルーターのWi-Fiは上游Wi-Fiに従ってDFSチャンネルの使用するかどうかを決定します。

- 上游Wi-FiがDFSチャンネルをしておりスキャン可能の場合、ルーターの5G Wi-Fiは同じチャンネルを 使用します。

- 上游Wi-Fiがスキャン不できるまたは接続に失敗した場合、ルーターの5G Wi-Fiは非DFSチャンネルに切り替わります。

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
- [各インターネットアクセス方法の優先順位を設定するには？](multi-wan.md)
- [複数のインターネットアクセス方式を同時に使用する場合のロードバランスを設定するには？](multi-wan.md)
- [LANとWi-FiのMACアドレスを知る方法は？](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}ください。
