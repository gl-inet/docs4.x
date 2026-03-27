# インターネット

ウェブ管理パネルにログインし、インターネットに移動するとホームページが表示されます。

上半分にはインターネットの状態を示す図が表示され、下半分には最大4タイプのインターネットアクセス方法が表示されます：[イーサネット](internet_ethernet.md)、[リピーター](internet_repeater.md)、[テザリング](internet_tethering.md)、[cellular](internet_cellular.md)。

## ステータス図

![status diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/status_diagram.png){class="glboxshadow"}

図の**左側**は、現在のインターネットの状態を示しています
- 緑色の実線はネットワーク接続が有効であることを示しています。
- グレーの破線はネットワークに接続されていないことを示します。
- 黄色い感嘆符がついた白色の実線は、接続されているものの、インターネットにアクセスできないことを示します。

図の**中央**には、現在のルーターの型番と、[AdGuard Home](adguardhome.md)、[IPv6](ipv6.md)、[VPN](vpn_dashboard.md)、[Tor](tor.md)、[5GメインWi-Fi](wireless.md)、[2.4GメインWi-Fi](wireless.md)、[5GゲストWi-Fi](wireless.md)、[2.4GゲストWi-Fi](wireless.md)のステータスが表示されます。
- 緑色は機能が有効であることを、グレーは無効であることを示します。[VPN](vpn_dashboard.md)および[Tor](tor.md)については、白色が接続中の状態を表します。
- 有効なWi-Fiアイコンにカーソルを合わせると、そのWi-FiのQRコードが表示されます。スマートフォンやタブレットでこのQRコードを読み取ることで、対応するWi-Fiネットワークに素早く接続できます。

 ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/wifi_qrcode.png){class="glboxshadow"}

図の**右側**にはルーターに接続されているデバイス（[クライアント](clients.md)）が表示されます。
- 無線接続のデバイスは上に、有線接続のデバイスは下に表示されます。
- 各セクションの横にある数字は、接続されているデバイスの数を示しています。

## インターネットアクセス方法

インターネットへの接続方法は、最大4種類あります。以下の各チュートリアルをご参照いただくか、[セットアップウィザード](#setup-wizard)から設定を開始してください。

- [イーサネットチュートリアル](internet_ethernet.md)
- [リピーターチュートリアル](internet_repeater.md)
- [テザリングチュートリアル](internet_tethering.md)
- [セルラーチュートリアル](internet_cellular.md)

## セットアップウィザード

セットアップウィザードはファームウェアv4.7以降で利用可能です。

インターネットページで、右上の本のアイコンをクリックします。

![setup wizard 1](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/setup_wizard1.png){class="glboxshadow"}

セットアップウィザードに従ってルーターを設定し、インターネットにアクセスできるようにします。

![setup wizard 2](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/setup_wizard2.png){class="glboxshadow"}

[GL.iNetアプリ](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}を使用する場合は、画面上の指示に従ってインターネットアクセスを設定してください。

[GL.iNet app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}をご利用の場合は、画面の指示に従ってインターネット接続の設定を行ってください。
---

ご不明な点がございましたら、 [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
