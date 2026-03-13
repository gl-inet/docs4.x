# LAN

ウェブ管理パネルの左側 -> ネットワーク -> LAN

LANは、デバイスがメインWi-Fiまたはイーサネットケーブルで接続されている場合のネットワークです。

基本設定、DHCPサーバー設定、アドレス予約が含まれています。

## 基本設定

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **ルーターIPアドレス**

    ルーターIPアドレスは、ルーターの管理ページにアクセスするためにブラウザのアドレスバーに入力するアドレスです。
    
    デフォルトは**192.168.8.1**です。ネットワークと競合する場合は変更できます。

- **ネットマスク**

    2つのオプションがあります：**255.255.255.0**と**255.255.0.0**

- **AP分離**

    ネットワークのクライアントデバイスを別のネットワーク領域に分離できます。これらのデバイスはネットワーク上の彼のデバイスと通信できません。

## DHCPサーバー

**DHCPサーバー**はデフォルトで有効になっています。DHCPサーバーは各クライアントデバイスにIPアドレスとその彼の通信パラメータを自動的に割り当てます。DHCPサーバーが無効になっている場合は、各クライアントに対して手動で設定する必要があります。[静のIPを手動で設定する方法は？](../tutorials/manually_configure_static_ip.md)

必要に応じて開始IPアドレスと終たIPアドレスを変更できます。例えば、ネットワーク規模が拡大または縮小された場合、ネットワーク内にIPアドレスの競合がある場合、またはサブネットマスクまたはIPアドレス範囲が変更された場合などに使用します。

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

必要な場合は、**詳細設定**をクリックしてさらに設定できます。

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **リース時間**: デバイスがDHCP経由で割り当てられたIPアドレスを使用できる期間。

- **ゲートウェイ**: ローカルネットワークと外部ネットワーク（例：インターネット）間のトラフィックをルーティングするデバイス。

- **DNSサーバー1**: ドメイン名をIPアドレスに変換する主要なサーバー。

- **DNSサーバー2**: プライマリDNSサーバーが失敗した場合にドメイン名解決に使用されるバックアップサーバー。

- **LPRサーバー**: （Line Printer Remote Server）印刷ジョブを管理し、ネットワークデバイスがリモートプリンターに印刷リクエストを送信できるようにするサービス。複数のプリンターのLPRポートを入力できます。

## アドレス予約

LAN内のクライアントに予約IPアドレスを指定すると、そのクライアントはルーターのDHCPサーバーにアクセスするたびに同じIPアドレスを受け取るようになります。永続のなIP設定が必要なコンピュータやサーバーに予約IPアドレスを割り当てることができます。

**注意:** 設定されたクライアントは有効にするためにルーターに再接続する必要があります。

**追加**をクリックしてIPを予約します。

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

ポップアップウィンドウが表示されます。

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

ドロップダウンリストから**MAC**を選択すると、選択したMACに対応する**IP**が自動的に入力されます。説明のな名前を付けます。次に**送信**をクリックします。

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

新しいIPアドレス予約を追加すると、以下のページが表示され、設定が正常に完たしたことを意味します。

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
