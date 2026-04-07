# SIMPoYo uFiの使い方

SIMPoYo uFi は、どこでもすばやく安定した接続を実現する、Wi-Fiホットスポット機能付きのコンパクトな Plug & Play USBドングルシリーズです。ほとんどのGL.iNetルーターに加え、ノートPC、モバイルバッテリー、車載USBポートなど、各種USB電源でシームレスに利用できます。英国およびその他34のヨーロッパ諸国で30日間有効な10GBの無料データが付属します。
<br><small>*販売地域: [EU](https://store-eu.gl-inet.com/){target="_blank"} と [UK Stores](https://store-uk.gl-inet.com/){target="_blank"} のみ</small>

このガイドでは、SIMPoYo uFi USBドングル（SP-N150C4）の使い方を紹介します。LED表示、内蔵SIMカードのアクティベーション方法、各種デバイスでの利用方法、データのチャージ方法、uFi設定の管理方法を含みます。

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
                <th>LED Type</th>
                <th>Color</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3">4G LED</td>
                <td>Green</td>
                <td>LTE Connected</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>WCDMA Connected</td>
            </tr>
            <tr>
                <td>Red Blinking</td>
                <td>No Signal / No SIM Card / Out of Service</td>
            </tr>
            <tr>
                <td rowspan="3">Wi-Fi LED</td>
                <td>Green</td>
                <td>Device(s) connected to Wi-Fi</td>
            </tr>
            <tr>
                <td>Blue</td>
                <td>No device connected to Wi-Fi</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>Wi-Fi is Disabled</td>
            </tr>
                <td rowspan="2">4G LED + Wi-Fi LED</td>
                <td>White</td>
                <td>Device Powered On</td>
            </tr>
            <tr>
                <td>OFF</td>
                <td>Device Powered Off</td>
        </tbody>
    </table>
</body>
</html>

## SIMカードをアクティベートする

SIMPoYo uFi にはSIMカードがあらかじめ装着されており、使用前にアクティベートする必要があります。

この動画を見るか、以下の手順でSIMPoYo uFiのSIMカードをアクティベートしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/0UokDjzp7Ek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Step 1**. SIMPoYo uFi背面の情報ラベルで ICCID 番号を確認します。

**Step 2**. QRコードをスキャンするか、[https://w.simpoyo.com/activate/](https://w.simpoyo.com/activate/){target="_blank"} にアクセスし、ICCID 番号を入力して登録します。

**Step 3**. 10GB の無料データを利用します。新規ユーザーには、英国およびその他34のヨーロッパ諸国で30日間有効な 10GB の無料4Gデータがすぐに付与されます。

## インターネット設定

### GL.iNetルーターに接続する

SIMPoYo uFi はほとんどのGL.iNetトラベルルーターおよびホームルーターでそのまま使えます。ルーターのUSBポートに挿すだけで、いつでもどこでも4G LTE接続を利用できます。

この動画を見るか、以下の手順でSIMPoYo uFiをGL.iNetルーターに接続してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/sU2u4En04so" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Step 1**. SIMPoYo uFi をGL.iNetルーターのUSBポートに挿します。

![setup1](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup1.png){class="glboxshadow"}

**Step 2**. デバイスをルーターに接続し、ブラウザで `192.168.8.1` にアクセスしてルーターのWeb管理パネルにログインします。ルーターのIPアドレスを変更している場合は、新しいIPでログインしてください。

![setup2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup2.png){class="glboxshadow"}

**Step 3**. 管理パネルで **INTERNET** -> **Tethering** に移動し、**Connect** をクリックします。

![setup3](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup3.png){class="glboxshadow"}

**Step 4**. 接続が完了すると、左上に青い点が表示され、ネットワーク詳細を確認できます。

![setup4](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup4.png){class="glboxshadow"}

これで、ケーブルまたはWi-Fiでルーターにデバイスを接続するか、SIMPoYo uFi のWi-Fiへ直接接続してインターネットを利用できます。

- ケーブルでルーターに接続: EthernetケーブルをルーターのLANポートとデバイスに接続します。有線専用デバイスや、安定して干渉の少ない接続が必要な場合に適しています。

- Wi-Fiでルーターに接続: ルーター底面ラベルに記載されたWi-Fi SSIDとKeyを確認し、デバイスを接続します。複数デバイス（2.4 GHz / 5 GHz）、広いカバレッジ、またはルーター側でのネットワーク設定のカスタマイズが必要な場合に適しています。

- Wi-FiでSIMPoYo uFiに接続: SIMPoYo uFi本体ラベルのWi-Fi SSIDとKeyを確認し、デバイス（最大8台）を接続します。必要に応じて、単体の2.4 GHzホットスポットとして柔軟に使用できます。

### コンピューターに接続する

**Step 1**. SIMPoYo uFi をコンピューター（デスクトップPCやノートPCなど）のUSBポートに挿します。USB Ethernetデバイスとして自動認識され、すぐにオンラインになります。

**Step 2**. 他のデバイス（スマートフォン、タブレットなど）も、SIMPoYo uFi の2.4 GHz Wi-Fiネットワークに接続して同時にインターネットを利用できます。

![multi-device](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/multi-device.jpg){class="glboxshadow"}

### USB電源に接続する

**Step 1**. SIMPoYo uFi をACアダプター、モバイルバッテリー、車載充電器などのUSB電源に挿します。

**Step 2**. 電源が入ると、SIMPoYo uFi は **SIMPoYo-XXX** というSSIDのWi-Fiネットワークをブロードキャストします。

**Step 3**. 本体ラベルに記載されたWi-Fiパスワード（Key）を確認します。このパスワードを使ってスマートフォン、タブレット、ノートPCなどをSIMPoYo uFiのWi-Fiに接続し、インターネットを利用します。

## SIMPoYoプランをチャージする

データを使い切った場合や有効期限が切れた場合は、SIMPoYo uFi のQRコードをスキャンするか、[https://w.simpoyo.com](https://w.simpoyo.com){target="_blank"} にアクセスしてプランをチャージしてください。

!!! note "対応国・地域"

    - **United Kingdom**

    - **Europe**

        Andorra, Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar (UK), Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Réunion (France), Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland.

    - **Middle East & North Africa**

        Egypt, Iran, Israel, Kuwait, Qatar, Saudi Arabia, United Arab Emirates.

    - **Asia**

        Indonesia, Japan, Pakistan, Philippines, Singapore, South Korea, Turkey, Vietnam, China Mainland, Hong Kong (China), Taiwan (China).

## SIMPoYo uFiを管理する

SIMPoYo uFi 管理パネルにログインすると、ネットワーク設定を管理できます。

### 管理パネルにログインする

1. デバイスをSIMPoYo uFi のWi-Fiネットワークに接続します。

2. ブラウザを開き、`192.168.1.1` を入力してSIMPoYo uFi管理パネルにアクセスします。

3. 管理者パスワードでログインします（デフォルトではSIMPoYo uFiのWi-Fiパスワードと同じです）。

    ![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/0-simpoyo-login.png){class="glboxshadow"}

### ネットワーク詳細を確認する

1. 上部メニューから **Status** を選択し、**Device & Network** に移動します。デバイスのネットワーク状態が表示されるホームページに入ります。

    ![network status](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/1.1-device-network.png){class="glboxshadow"}

2. 左側のサイドバーで **Cellular Network** に切り替えると、信号強度などのセルラーネットワーク詳細を確認できます。

    ![cellular network](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/1.2-cellular-network.png){class="glboxshadow"}

### データ使用量を確認する

1. 上部メニューから **Data Usage** を選択すると、ダウンロード量、アップロード量、総使用量、利用時間を確認できます。

    ![data usage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/2-data-usage.png){class="glboxshadow"}

    注: データ量は参考値です。正確な情報は請求内容を参照してください。

2. データ使用量をリセットしたい場合は、**Clear History** ボタンをクリックします。

### Wi-Fi設定を変更する

1. 上部メニューから **Settings** を選択し、**Wi-Fi Settings** に移動します。

    ![wifi settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.1-wifi-settings.png){class="glboxshadow"}

2. SIMPoYo uFi のWi-Fiネットワーク名とパスワードをカスタマイズし、**Apply** をクリックします。

### APNを設定する

SIMカードで手動APN設定が必要な場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Cellular Settings** に移動します。

    ![cellular settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.2-cellular-settings.png){class="glboxshadow"}

2. **APN Mode** を **Manual** に切り替えます。

3. モバイル通信事業者から提供された情報を入力し、**Apply** をクリックします。

### ローミングを有効にする

ローミングを有効にすると、SIMカードが他の地域や国の現地通信事業者と接続できるため、ホームネットワーク圏外でも通信を継続できます。

以下の手順でローミングを有効にします。

1. 上部メニューから **Settings** を選択し、**Roaming** に移動します。

    ![roaming](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.3-roaming.png){class="glboxshadow"}

2. **Enable** を選択し、**Apply** をクリックします。

### PINコードを有効にする

PINコードはSIMカード用の短いセキュリティパスワード（通常4～8桁）で、不正利用を防ぐためにSIMカードをロックします。SIMが盗まれたり別のデバイスに挿されたりしても、PINコードがなければ有効化または利用できません。

以下の手順でPINコードを有効にします。

1. 上部メニューから **Settings** を選択し、**PIN Settings** に移動します。

    ![pin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.4-pin-settings.png){class="glboxshadow"}

2. **Enable** を選択し、PINコードを設定して **Apply** をクリックします。

### 管理者パスワードを変更する

デフォルトの管理者パスワードはWi-Fiパスワードと同じです。セキュリティのため、初回設定時に変更してください。

1. 上部メニューから **Settings** を選択し、**Admin Settings** に移動します。

    ![admin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.5-admin-settings.png){class="glboxshadow"}

2. Admin Password と Login Timeout をカスタマイズし、**Apply** をクリックします。

3. SIMPoYo uFi を工場出荷時設定に戻したい場合は、**Factory Default Setting** ボタンをクリックしてリセットします。

### DHCP設定

デフォルトでは、SIMPoYo uFi のIPアドレスは `192.168.1.1` で、接続デバイスにIPアドレスを割り当てるためのDHCPサーバーが有効になっています。

IPアドレスを変更したり、DHCP設定をカスタマイズしたりしたい場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Advanced** -> **DHCP** に移動します。

    ![dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-dhcp.jpg){class="glboxshadow"}

2. ここでは、デバイスのIPアドレス変更、DHCPサーバーの有効/無効切り替え、IP範囲やリース時間の設定ができます。DHCP設定を行い、**Apply** をクリックします。

### MAC Filter

MAC Filter を使うと、MACアドレスを管理してWLANへアクセスできるデバイスを制御でき、ネットワークのセキュリティを強化できます。

MAC Filter はデフォルトで無効です。有効にする場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Advanced** -> **MAC Filter** に移動します。

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-1.png){class="glboxshadow"}

    上部の **User list** には接続中デバイスの詳細が表示されます。制御したいデバイスが一覧にあるか確認してください。ない場合は、SIMPoYo uFi のWi-Fiへ再接続してください。

2. **MAC Filter Mode** を **Black List** / **White List** に切り替えます。

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-2.png){class="glboxshadow"}

3. ブロックまたは許可したいデバイスのMACアドレスを一覧へコピーし、**Apply** をクリックします。

### Upgrade

1. 上部メニューから **Upgrade** を選択し、**Device Info** に移動すると、SIMPoYo uFi のデバイス情報を確認できます。内容は以下を含みます。

    - ハードウェア情報（例: ハードウェアバージョン、MACアドレス、IMEI、ICCID）
    - ソフトウェア情報（例: ソフトウェアバージョン）
    - WebUI情報（例: WebUIバージョン）

    ![upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.1-upgrade.jpg){class="glboxshadow"}

2. 利用可能であればソフトウェアをアップグレードできます。

    左側のサイドバーで **Online Update** に切り替え、**Check New Update** ボタンをクリックすると、新しいバージョンの有無を確認できます。

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.2-online-update.png){class="glboxshadow"}

    または、左側のサイドバーで **Local Update** に切り替え、ファイルをアップロードして **Apply** をクリックすると手動アップグレードできます。

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.3-local-update.png){class="glboxshadow"}

## 付属アクセサリーガイド

パッケージには次のアクセサリーが含まれています。

- **USB-C to USB-A アダプターケーブル 1本**: USB Type-Cポートのみを備えたデバイス（ノートPCなど）でSIMPoYo uFiを使用する場合に適しています。

- **USB-A to USB-A アダプターケーブル 1本**: SIMPoYo uFi をUSBポート（コンピューターやUSB電源など）へ柔軟に接続でき、本体側ポートと接続先ポートの直接接触を避けられます。これにより、急な衝撃による金属インターフェースの損傷を防ぎやすくなります。

- **SIM取り出しツール（ピン）1本**: スマートフォンなどからSIMカードを取り出してSIMPoYo uFiへ装着する際や、必要に応じてuFiのリセットピンホールを押す際に使用します。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
