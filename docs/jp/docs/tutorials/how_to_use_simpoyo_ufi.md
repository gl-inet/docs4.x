# SIMPoYo uFiの使い方

SIMPoYo uFi は、Wi-Fiホットスポット機能を備えたコンパクトな Plug & Play USB ドングルシリーズです。外出先でも高速かつ安定した通信を利用できるように設計されており、多くのGL.iNetルーターに加えて、ノートPC、モバイルバッテリー、車載USBポート、そのほかのUSB電源でも使用できます。イギリスおよびヨーロッパ34か国で利用できる、30日間有効の無料データ 10GB が付属します。
<br><small>\*販売地域: [EU](https://store-eu.gl-inet.com/) & [UK Stores](https://store-uk.gl-inet.com/)</small>

このガイドでは、SIMPoYo uFi USB ドングル（SP-N150C4）の使い方、LED表示、内蔵SIMカードの有効化方法、各種機器での利用方法、データのトップアップ、uFi の設定管理について説明します。

![SIMPoYo uFi](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/sp-n150c4.jpg){class="glboxshadow"}

## LED表示

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LED Indication</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            vertical-align: middle;
        }
        th {
            background-color: #f2f2f2;
            text-align: left;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>LEDタイプ</th>
                <th>色</th>
                <th>説明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3">4G LED</td>
                <td>Green</td>
                <td>LTE接続中</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>WCDMA接続中</td>
            </tr>
            <tr>
                <td>Red Blinking</td>
                <td>圏外 / SIMカード未挿入 / サービス圏外</td>
            </tr>
            <tr>
                <td rowspan="3">Wi-Fi LED</td>
                <td>Green</td>
                <td>Wi-Fiに端末が接続中</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>Wi-Fiに端末が未接続</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>Wi-Fi無効</td>
            </tr>
            <tr>
                <td rowspan="2">4G LED + Wi-Fi LED</td>
                <td>White</td>
                <td>電源オン</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>電源オフ</td>
            </tr>
        </tbody>
    </table>
</body>
</html>

## SIMカードを有効化する

SIMPoYo uFi には SIM カードがあらかじめ取り付けられています。使用前に有効化してください。

以下の動画を見るか、手順に従って SIMPoYo uFi の SIM カードを有効化してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/0UokDjzp7Ek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**ステップ1**。SIMPoYo uFi 背面の情報ラベルに記載されている ICCID 番号を確認します。

**ステップ2**。QRコードをスキャンするか、[https://w.simpoyo.com/activate/](https://w.simpoyo.com/activate/){target="\_blank"} にアクセスし、ICCID 番号を入力して登録します。

**ステップ3**。無料データ 10GB を利用します。新規ユーザーには、イギリスおよびヨーロッパ34か国で使える、30日間有効の無料4Gデータ 10GB が即時付与されます。

## インターネットの設定

### GL.iNetルーターに接続する

SIMPoYo uFi は、多くのGL.iNetのトラベルルーターやホームルーターでそのまま利用できます。ルーターのUSBポートに挿すだけで、いつでもどこでも4G LTE接続を使えます。

以下の動画を見るか、手順に従って SIMPoYo uFi を GL.iNet ルーターに接続してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/sU2u4En04so" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**ステップ1**。SIMPoYo uFi を GL.iNet ルーターの USB ポートに挿します。

![setup1](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup1.png){class="glboxshadow"}

**ステップ2**。端末をルーターに接続し、ブラウザで `192.168.8.1` を開いてルーターの Web 管理パネルにログインします。ルーターの IP アドレスを変更している場合は、その新しいアドレスを使用してください。

![setup2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup2.png){class="glboxshadow"}

**ステップ3**。管理パネルで **INTERNET** -> **Tethering** に移動し、**Connect** をクリックします。

![setup3](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup3.png){class="glboxshadow"}

**ステップ4**。接続に成功すると、左上に青いドットが付いたネットワーク情報が表示されます。

![setup4](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup4.png){class="glboxshadow"}

これで、ルーターに有線またはWi-Fiで接続するか、SIMPoYo uFi の Wi-Fi に直接接続してインターネットを利用できます。

- ルーターに有線接続する: Ethernet ケーブルでルーターの LAN ポートと端末を接続します。有線専用の機器や、安定した干渉の少ない通信が必要な場合に適しています。

- ルーターに Wi-Fi 接続する: ルーター底面のラベルに記載された Wi-Fi SSID と Key を確認して接続します。複数端末の接続、2.4 GHz / 5 GHz の利用、より広いカバー範囲、ルーター側の細かいネットワーク設定が必要な場合に適しています。

- SIMPoYo uFi に Wi-Fi 接続する: SIMPoYo uFi 本体ラベルの Wi-Fi SSID と Key を確認し、端末を接続します。最大8台まで接続でき、必要に応じて独立した 2.4 GHz ホットスポットとして使えます。

### コンピューターに接続する

**ステップ1**。SIMPoYo uFi をデスクトップPCやノートPCなどの USB ポートに挿します。USB Ethernet デバイスとして自動認識され、すぐにインターネットへ接続できます。

**ステップ2**。スマートフォンやタブレットなどほかの端末も、SIMPoYo uFi の 2.4 GHz Wi-Fi に接続して同時にインターネットを利用できます。

![multi-device](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/multi-device.jpg){class="glboxshadow"}

### USB電源に接続する

**ステップ1**。SIMPoYo uFi を USB 電源に挿します。壁面充電器、モバイルバッテリー、車載充電器などが利用できます。

**ステップ2**。電源が入ると、SIMPoYo uFi は SSID **SIMPoYo-XXX** の Wi-Fi ネットワークをブロードキャストします。

**ステップ3**。本体ラベルの Wi-Fi パスワード（Key）を確認し、そのパスワードでスマートフォン、タブレット、ノートPCなどの端末を SIMPoYo uFi の Wi-Fi に接続します。

## SIMPoYoプランをトップアップする

データ容量を使い切った場合や有効期限が切れた場合は、SIMPoYo uFi の QR コードをスキャンするか、[https://w.simpoyo.com](https://w.simpoyo.com){target="\_blank"} にアクセスしてプランをトップアップしてください。

!!! note "対応国と地域"

    - **イギリス**

    - **ヨーロッパ**

        アンドラ、オーストリア、ベルギー、ブルガリア、クロアチア、キプロス、チェコ、デンマーク、エストニア、フィンランド、フランス、ドイツ、ジブラルタル（UK）、ギリシャ、ハンガリー、アイスランド、アイルランド、イタリア、ラトビア、リヒテンシュタイン、リトアニア、ルクセンブルク、マルタ、オランダ、ノルウェー、ポーランド、ポルトガル、レユニオン（フランス）、ルーマニア、スロバキア、スロベニア、スペイン、スウェーデン、スイス。

    - **中東・北アフリカ**

        エジプト、イラン、イスラエル、クウェート、カタール、サウジアラビア、アラブ首長国連邦。

    - **アジア**

        インドネシア、日本、パキスタン、フィリピン、シンガポール、韓国、トルコ、ベトナム、中国本土、香港（中国）、台湾（中国）。

## SIMPoYo uFiを管理する

SIMPoYo uFi の管理パネルにログインすると、ネットワーク設定を管理できます。

### 管理パネルにログインする

1. 端末を SIMPoYo uFi の Wi-Fi ネットワークに接続します。

2. ブラウザを開き、`192.168.1.1` を入力して SIMPoYo uFi の管理パネルにアクセスします。

3. 管理者パスワードでログインします。デフォルトでは、Wi-Fi パスワードと同じです。

   ![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/0-simpoyo-login.png){class="glboxshadow"}

### ネットワークの詳細を確認する

1. 上部メニューで **Status** を選択し、**Device & Network** に移動します。端末のネットワーク状態が表示されるホーム画面が開きます。

   ![network status](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/1.1-device-network.png){class="glboxshadow"}

2. 左側のサイドバーで **Cellular Network** に切り替えると、電波強度などのモバイルネットワーク情報を確認できます。

   ![cellular network](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/1.2-cellular-network.png){class="glboxshadow"}

### データ使用量を確認する

1. 上部メニューで **Data Usage** を選択すると、ダウンロード量、アップロード量、合計使用量、利用期間が表示されます。

   ![data usage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/2-data-usage.png){class="glboxshadow"}

   注意: 表示されるデータ量は参考値です。正確な請求情報は契約先の明細を参照してください。

2. 使用量をリセットしたい場合は、**Clear History** をクリックします。

### Wi-Fi設定を変更する

1. 上部メニューで **Settings** を選択し、**Wi-Fi Settings** に移動します。

   ![wifi settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.1-wifi-settings.png){class="glboxshadow"}

2. SIMPoYo uFi の Wi-Fi 名とパスワードを変更し、**Apply** をクリックします。

### APNを設定する

SIMカードで手動のAPN設定が必要な場合は、以下の手順で設定します。

1. 上部メニューで **Settings** を選択し、**Cellular Settings** に移動します。

   ![cellular settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.2-cellular-settings.png){class="glboxshadow"}

2. **APN Mode** を **Manual** に切り替えます。

3. 通信事業者から提供された情報を入力し、**Apply** をクリックします。

### ローミングを有効にする

ローミングを有効にすると、SIMカードは他の地域や国でも現地通信事業者のネットワークを利用できるため、ホームネットワークの圏外でも接続を維持できます。

1. 上部メニューで **Settings** を選択し、**Roaming** に移動します。

   ![roaming](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.3-roaming.png){class="glboxshadow"}

2. **Enable** を選択し、**Apply** をクリックします。

### PINコードを有効にする

PINコードは、SIMカードを保護するための短いセキュリティコードです。通常は4〜8桁で構成され、無断使用を防ぐためにSIMカードをロックします。SIMカードが盗難に遭ったり他の端末に挿し替えられたりした場合でも、PINコードがなければ有効化や利用ができません。

1. 上部メニューで **Settings** を選択し、**PIN Settings** に移動します。

   ![pin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.4-pin-settings.png){class="glboxshadow"}

2. **Enable** を選択し、PINコードを設定して **Apply** をクリックします。

### 管理者パスワードを変更する

デフォルトの管理者パスワードは Wi-Fi パスワードと同じです。セキュリティのため、初期設定時に変更することをおすすめします。

1. 上部メニューで **Settings** を選択し、**Admin Settings** に移動します。

   ![admin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.5-admin-settings.png){class="glboxshadow"}

2. 管理者パスワードとログインタイムアウトを設定し、**Apply** をクリックします。

3. 工場出荷時設定に戻す場合は、**Factory Default Setting** をクリックします。

### DHCP設定

デフォルトでは、SIMPoYo uFi の IP アドレスは `192.168.1.1` で、DHCPサーバーが有効になっており、接続した端末にIPアドレスを割り当てます。

IPアドレスを変更したい場合やDHCP設定をカスタマイズしたい場合は、以下の手順に従ってください。

1. 上部メニューで **Settings** を選択し、**Advanced** -> **DHCP** に移動します。

   ![dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-dhcp.jpg){class="glboxshadow"}

2. 端末のIPアドレス変更、DHCPサーバーの有効化または無効化、IP範囲、リース時間の設定ができます。設定後、**Apply** をクリックします。

### MACフィルター

MACフィルターを使用すると、MACアドレスでWLANへの接続可否を制御でき、ネットワークのセキュリティを高められます。

MACフィルターはデフォルトで無効です。有効にする場合は以下の手順に従ってください。

1. 上部メニューで **Settings** を選択し、**Advanced** -> **MAC Filter** に移動します。

   ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-1.png){class="glboxshadow"}

   上部の **User list** には接続中の端末情報が表示されます。制御したい端末が一覧に表示されているか確認してください。表示されていない場合は、SIMPoYo uFi の Wi-Fi に再接続してください。

2. **MAC Filter Mode** を **Black List** または **White List** に切り替えます。

   ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-2.png){class="glboxshadow"}

3. ブロックまたは許可したい端末の MAC アドレスをリストに追加し、**Apply** をクリックします。

### アップグレード

1. 上部メニューで **Upgrade** を選択し、**Device Info** に移動すると、SIMPoYo uFi の端末情報を確認できます。
   - ハードウェア情報（ハードウェアバージョン、MACアドレス、IMEI、ICCID）
   - ソフトウェア情報（ソフトウェアバージョン）
   - WebUI情報（WebUIバージョン）

   ![upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.1-upgrade.jpg){class="glboxshadow"}

2. 新しいバージョンがあれば、ソフトウェアをアップグレードできます。

   左側のサイドバーで **Online Update** に切り替え、**Check New Update** をクリックすると、新しいバージョンがあるか確認できます。

   ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.2-online-update.png){class="glboxshadow"}

   または、左側のサイドバーで **Local Update** に切り替え、ファイルをアップロードして **Apply** をクリックすると、手動アップグレードが行えます。

   ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.3-local-update.png){class="glboxshadow"}

## 付属アクセサリー

パッケージには以下のアクセサリーが含まれています。

- **1 USB-C to USB-A adapter cable**: USB Type-C ポートしかない端末（ノートPCなど）に SIMPoYo uFi を接続する際に使用します。

- **1 USB-A to USB-A adapter cable**: コンピューターやUSB電源などのUSBポートへ、SIMPoYo uFi を柔軟に接続できます。本体ポートと接続先ポートが直接ぶつかるのを避けられるため、衝撃による金属端子の損傷防止にも役立ちます。

- **1 SIM eject tool (a pin)**: スマートフォンなどからSIMカードを取り出して SIMPoYo uFi に装着する際、または必要に応じて uFi のリセット用ピンホールを押す際に使用します。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"}をご覧ください。
