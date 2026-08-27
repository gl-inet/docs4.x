# インターネット接続のトラブルシューティングFAQ

## Q1. インターネットに接続できない場合はどうすればよいですか？

基本的なトラブルシューティングとして、以下の手順をお試しください。

1. 物理接続を確認します。

    ルーターの WAN ポートと上位側デバイス（モデム、ONT、Ethernet ジャックなど）の間で、Ethernet ケーブルがしっかり接続されていることを確認してください。上位側デバイスのLEDも確認し、通信が行われていることを確認します。

2. デバイスを再起動します。

    上位側デバイス（モデムなど）とルーターの電源を切ります。1〜2分待ってから、先にモデムの電源を入れ、完全にオンラインになったことを確認してからルーターの電源を入れてください。

3. WAN IPアドレスを確認します。

    ルーターの Web 管理パネルにログインし、**INTERNET** -> **Ethernet** セクションに移動します。下図のように接続中のまま止まっている場合は、DHCP の問題、MAC バインディング、または VLAN ID の設定が必要な可能性があります。

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    ISP に連絡し、インターネット接続に **PPPoE username**、**PPPoE password**、**VLAN ID** が必要か確認してください。

    あわせて、ISP が以前にモデム / ONT に **MAC binding** を設定していないかも確認してください。

## Q2. MACアドレスをクローンするのはどのような場合ですか？

一部の ISP では、回線接続を最初に接続したデバイス（通常は以前使っていたルーターまたはPC）の MAC アドレスに紐付けています。ルーターを交換した場合、インターネット接続を復旧するには MAC アドレスのクローンが必要になります。

GL.iNet ルーターに MAC アドレスをクローンする手順は以下のとおりです。

1. 以前使っていたルーター（または回線に紐付けられていたPC）の MAC アドレスを控えます。

2. ルーターの Web 管理パネルにログインし、**NETWORK** -> **Ethernet Port**（一部のファームウェアでは **Port Management**）に移動します。**MAC Mode** を **Clone** または **Manual** に設定し、MAC アドレスを手動で入力して **Apply** をクリックします。

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. モデム（上位側デバイス）を再起動します。

## Q3. VLAN ID の設定が必要なのはどのような場合ですか？

一部の ISP では、特に光回線や IPTV 接続で、インターネット認証やトラフィック分離のために VLAN タグが必要です。VLAN ID が必要かどうかは ISP に確認してください。

VLAN ID を設定する手順は以下のとおりです。

1. ルーターにログインし、**INTERNET** -> **Ethernet** セクションに移動して **Modify** をクリックします。

2. ISP から提供された VLAN ID を入力し、**Apply** をクリックします。

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. それでも動作しない場合はどうすればよいですか？

問題が解決しない場合は、PC またはノートPC をモデムに直接接続し、インターネットへアクセスできるか確認してください。

インターネットへアクセスできない場合は、問題が ISP 側にある可能性があります。詳細は ISP にお問い合わせください。

インターネットへアクセスできる場合は、ルーターの設定に問題がある可能性があります。[support@gl-inet.com](mailto:support@gl-inet.com) まで以下の情報を添えて技術サポートへご連絡ください。

- ルーターモデル
- すでに試したトラブルシューティング手順
- ご利用の ISP 名
- そのほか、問題解決に役立つと思われる情報

## ISP 情報

以下は、GL.iNet がお客様からのフィードバック、フォーラム、OpenWRT の情報をもとにまとめた地域別 ISP 情報です。参考情報としてご利用ください。

| 国/地域   | ISP   | 接続方式 | VLAN ID | MAC クローン必須 | 追加要件 |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| アメリカ合衆国    | AT&T Fiber | DHCP（IP パススルー） | N/A | いいえ | IP パススルーを有効にする必要があります。EAP 認証のバイパスが必要です。 |
| アメリカ合衆国 | Spectrum | DHCP | N/A | はい（一部地域） | MAC バインドが強く、モデムの再起動が必要です。 |
| アメリカ合衆国 | Verizon Fios | DHCP | N/A | いいえ | |
| アメリカ合衆国 | Comcast Xfinity | DHCP | N/A | はい（一般的） | ルーター変更時はモデムを再起動する必要があります（MAC 解放）。 |
| アメリカ合衆国 | Cox Communications | DHCP | N/A | はい | ルーター変更時はモデムを再起動する必要があります（MAC 解放）。 |
| アメリカ合衆国 | Frontier Fiber | DHCP | N/A | いいえ | |
| アメリカ合衆国 | CenturyLink / Lumen | PPPoE | 201 | いいえ | 一部地域では VLAN が必要です。 |
| カナダ | Bell Canada Fibe | PPPoE | 35 | いいえ | |
| ドイツ | Deutsche Telekom | PPPoE | 7 | いいえ | インターネット接続には VLAN 7 が必須で、PPPoE 認証情報が必要です。 |
| ドイツ | Vodafone (Kabel) | DHCP | N/A | はい（場合あり） | MAC バインドが適用される場合があります。ルーター変更後はモデムを再起動してください。 |
| ドイツ | 1&1 / O2 (Telekom line) | PPPoE | 7 | いいえ | インターネット接続には VLAN 7 が必須です。 |
| ドイツ | DNS:NET | PPPoE | 37 | いいえ | |
| ドイツ | o2(UGG) | PPPoE | 7 | いいえ | |
| イギリス | BT Broadband | PPPoE | 101 | いいえ | VLAN 101 が必要で、PPPoE ログインが必要です。 |
| イギリス | Sky Broadband | DHCP（Option 61） | 101 | いいえ | DHCP Option 61（クライアント識別子）が必要です。 |
| イギリス | Virgin | DHCP | N/A | はい | モデムをブリッジモードにし、MAC クローンが必要です。 |
| フランス | Orange | DHCP / PPPoE | 832 | いいえ | VLAN 832 が必要で、Option 90 認証が必要な場合があります。 |
| フランス | Free (Freebox) | DHCP | N/A | いいえ | |
| フランス | Bouygues Telecom | DHCP | 100 | はい | Bbox の MAC をクローンします。 |
| スペイン | Movistar | PPPoE | 6 | いいえ | VLAN 6（インターネット）、VLAN 2（IPTV）、VLAN 3（VoIP）が必要です。 |
| スペイン | DIGI | PPPoE | 20 | いいえ | |
| スペイン | Orange | DHCP | 832/835 | いいえ | VLAN は地域によって異なる場合があります。 |
| イタリア | TIM | PPPoE | 835 | いいえ | VLAN 835 が必要です。 |
| イタリア | Aruba | PPPoE | 835 | いいえ | |
| オランダ | KPN | DHCP | 6 | いいえ | インターネット接続には VLAN 6 が必要です。 |
| オランダ | Tweak | DHCP | 34 | はい | Experia Box の MAC をクローンします。 |
| オランダ | Telfort / Oxxio / Tweak | DHCP（IPoE） | 34 | いいえ | |
| オランダ | Odido | DHCP | 300 | いいえ | |
| ベルギー | EDPnet | PPPoE | 10 | いいえ | |
| ボスニア・ヘルツェゴビナ | BH Telecom | PPPoE | 100 | いいえ | |
| クロアチア | Terrakom | PPPoE | 905 | いいえ | |
| チェコ共和国 | O2 | PPPoE | 848 | いいえ | |
| キプロス | Epic | PPPoE | 35 | いいえ | |
| キプロス | Cyta | PPPoE | 42 | いいえ | |
| キプロス | Cablenet | PPPoE | 42 | いいえ | |
| キプロス | Primetel | PPPoE | 42 | いいえ | |
| ポーランド | Orange Polska | PPPoE | 35 | いいえ | VLAN 35 が必要です。 |
| ポーランド | T-mobile | PPPoE | 35 | いいえ | |
| アイルランド | Vodafone SIRO | PPPoE | 10 | いいえ | |
| アイルランド | Pure Telecom | PPPoE | 10 | いいえ | |
| オーストリア | A1 Telekom | PPPoE | 2 | いいえ | |
| オーストリア | Fonira | PPPoE | 31 | いいえ | |
| トルコ | Turknet | PPPoE | 35 | いいえ | |
| トルコ | Turk Telekom | PPPoE | 35 | いいえ | |
| トルコ | Turkcell Superonline | PPPoE | N/A | はい | |
| トルコ | Turksat Kablonet | DHCP/PPPoE | N/A | いいえ | |
| ギリシャ | Cosmote | PPPoE | 835 | いいえ | |
| ギリシャ | Nova | PPPoE | 835 | はい | |
| ギリシャ | DEI/PPC | DHCP | 835 | いいえ | |
| 日本 | NTT（フレッツ） | PPPoE / IPoE（MAP-E） | N/A | いいえ | IPoE では MAP-E / DS-Lite 対応ルーターが必要です。 |
| 日本 | SoftBank Hikari | PPPoE / IPoE | N/A | いいえ | BBIX の IPoE サービスが一般的に利用されます。 |
| インド | Airtel | PPPoE / DHCP | N/A | いいえ | 一部地域では PPPoE が必要です。 |
| インド | JioFiber | DHCP | N/A | いいえ | 多くの場合、ONT がロックされています。 |
| シンガポール | Singtel | PPPoE | 10 | いいえ | VLAN 10 が必要で、IPTV は別 VLAN です。 |
| シンガポール | StarHub | DHCP | N/A | いいえ | DHCP ベースの接続です。 |
| オーストラリア | NBN（各種 ISP） | PPPoE / DHCP | 2（一般的） | はい | VLAN 2 が一般的ですが、ISP によって異なります。 |
