# インターネット

Web管理パネルにログインし、**INTERNET** に移動します。

上部にはインターネットの状態を示す図が表示され、下部には4つまたは5つのインターネット接続方法が表示されます（利用できる方法はモデルによって異なります）。

## ステータス図

![status diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/status_diagram.png){class="glboxshadow"}

**図の左側**には、現在のインターネットの状態が表示されます。

- 緑色の実線は、ネットワーク接続が有効であることを示します。
- 灰色の破線は、ネットワーク接続がないことを示します。
- 黄色の感嘆符が付いた白い実線は、接続はされているもののインターネットにアクセスできないことを示します。

**図の中央**には、現在のルーターモデルと、[AdGuard Home](adguardhome.md)、[IPv6](ipv6.md)、[VPN](vpn_dashboard.md)、[Tor](tor.md)、[5G メインWi-Fi](wireless.md)、[2.4G メインWi-Fi](wireless.md)、[5G ゲストWi-Fi](wireless.md)、[2.4G ゲストWi-Fi](wireless.md) の状態が表示されます。

- 緑は有効、灰色は無効を示します。VPN と Tor では、白は接続中を示します。
- 有効な Wi‑Fi アイコンにカーソルを合わせると、その Wi‑Fi の QR コードが表示されます。スマートフォンやタブレットで読み取ることで、対応する Wi‑Fi ネットワークにすばやく接続できます。

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/wifi_qrcode.png){class="glboxshadow"}

**図の右側**には、ルーターに接続されているデバイス（[クライアント](clients.md)）が表示されます。

- 無線接続のデバイスは上段に、有線接続のデバイスは下段に表示されます。
- 各セクションの横にある数字は、接続中のデバイス数を示します。

## インターネット接続方法

利用できるインターネット接続方法は最大4種類です。以下の各チュートリアルを参照するか、[セットアップウィザード](#setup-wizard)から開始してください。

- [イーサネット](internet_ethernet.md)
- [リピーター](internet_repeater.md)
- [テザリング](internet_tethering.md)
- [セルラー](internet_cellular.md)

## セットアップウィザード {#setup-wizard}

セットアップウィザードはファームウェア v4.7 以降で利用できます。

**INTERNET** ページで、右上の本のアイコンをクリックします。

![setup wizard 1](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/setup_wizard1.png){class="glboxshadow"}

セットアップウィザードに従って、ルーターがインターネットに接続できるよう設定します。

![setup wizard 2](https://static.gl-inet.com/docs/router/en/4/tutorials/internet/setup_wizard2.png){class="glboxshadow"}

[GL.iNet app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} を使用する場合は、画面の案内に従ってインターネット接続を設定してください。

---

ご不明な点がありましたら、[コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
