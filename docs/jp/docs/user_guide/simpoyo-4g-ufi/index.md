# SIMPoYo 4G uFi ユーザーガイド

SIMPoYo 4G uFi は、Wi‑Fi ホットスポット機能を備えたコンパクトな Plug & Play USB ドングルシリーズです。ほとんどの GL.iNet ルーターに加え、ノート PC、モバイルバッテリー、車載 USB ポートなど、さまざまな USB 電源で手軽に利用できます。英国およびその他 34 のヨーロッパ諸国で 30 日間有効な 10GB の無料データが付属します。
<br><small>*販売地域: [EU](https://store-eu.gl-inet.com/){target="_blank"} と [UK Stores](https://store-uk.gl-inet.com/){target="_blank"} のみ</small>

このガイドでは、SIMPoYo uFi USB ドングル（SP-N150C4）の使い方を説明します。LED 表示、内蔵 SIM カードのアクティベーション方法、各種デバイスでの利用方法、データのチャージ方法、uFi 設定の管理方法を含みます。

![SIMPoYo uFi](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/sp-n150c4.jpg){class="glboxshadow"}

## LED表示

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>LED表示</title>
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
                <th>LED種類</th>
                <th>色</th>
                <th>説明</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3">4G LED</td>
                <td>緑</td>
                <td>LTE 接続中</td>
            </tr>
            <tr>
                <td>青</td>
                <td>WCDMA 接続中</td>
            </tr>
            <tr>
                <td>赤点滅</td>
                <td>圏外 / SIM カード未挿入 / サービス圏外</td>
            </tr>
            <tr>
                <td rowspan="3">Wi‑Fi LED</td>
                <td>緑</td>
                <td>Wi‑Fi にデバイスが接続中</td>
            </tr>
            <tr>
                <td>青</td>
                <td>Wi‑Fi に接続中のデバイスなし</td>
            </tr>
            <tr>
                <td>消灯</td>
                <td>Wi‑Fi 無効</td>
            </tr>
                <td rowspan="2">4G LED + Wi‑Fi LED</td>
                <td>白</td>
                <td>電源オン</td>
            </tr>
            <tr>
                <td>消灯</td>
                <td>電源オフ</td>
        </tbody>
    </table>
</body>
</html>

## SIMカードをアクティベートする

SIMPoYo uFi には SIM カードがあらかじめ装着されており、使用前にアクティベートする必要があります。

この動画を見るか、以下の手順で SIMPoYo uFi の SIM カードをアクティベートしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/0UokDjzp7Ek" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Step 1**. SIMPoYo uFi 背面の情報ラベルで ICCID 番号を確認します。

**Step 2**. QR コードをスキャンするか、[https://w.simpoyo.com/activate/](https://w.simpoyo.com/activate/){target="_blank"} にアクセスし、ICCID 番号を入力して登録します。

**Step 3**. 10GB の無料データを利用します。新規ユーザーには、英国およびその他 34 のヨーロッパ諸国で 30 日間有効な 10GB の無料 4G データがすぐに付与されます。

## インターネット設定

### GL.iNet ルーターに接続する

SIMPoYo uFi は、ほとんどの GL.iNet トラベルルーターおよびホームルーターでそのまま使えます。ルーターの USB ポートに挿すだけで、いつでもどこでも 4G LTE 接続を利用できます。

この動画を見るか、以下の手順で SIMPoYo uFi を GL.iNet ルーターに接続してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/sU2u4En04so" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Step 1**. SIMPoYo uFi を GL.iNet ルーターの USB ポートに挿します。

![setup1](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup1.png){class="glboxshadow"}

**Step 2**. デバイスをルーターに接続し、ブラウザで `192.168.8.1` にアクセスしてルーターのWeb管理画面にログインします。ルーターの IP アドレスを変更している場合は、新しい IP でログインしてください。

![setup2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup2.png){class="glboxshadow"}

**Step 3**. 管理パネルで **INTERNET** -> **Tethering** に移動し、**Connect** をクリックします。

![setup3](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup3.png){class="glboxshadow"}

**Step 4**. 接続が完了すると、左上に青い点が表示され、ネットワーク詳細を確認できます。

![setup4](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/setup4.png){class="glboxshadow"}

これで、ケーブルまたは Wi‑Fi でルーターにデバイスを接続するか、SIMPoYo uFi の Wi‑Fi へ直接接続してインターネットを利用できます。

- ケーブルでルーターに接続: Ethernet ケーブルをルーターの LAN ポートとデバイスに接続します。有線専用デバイスや、安定して干渉の少ない接続が必要な場合に適しています。

- Wi‑Fi でルーターに接続: ルーター底面ラベルに記載された Wi‑Fi SSID と Key を確認し、デバイスを接続します。複数デバイス（2.4 GHz / 5 GHz）、広いカバレッジ、またはルーター側でのネットワーク設定のカスタマイズが必要な場合に適しています。

- Wi‑Fi で SIMPoYo uFi に接続: SIMPoYo uFi 本体ラベルの Wi‑Fi SSID と Key を確認し、デバイス（最大 8 台）を接続します。必要に応じて、単体の 2.4 GHz ホットスポットとして柔軟に使用できます。

!!! note "トラブルシューティング"

    お使いの uFi が GL.iNet ルーターに認識されない場合は、以下をお試しください。

    1. ルーターの純正電源アダプターを使用してください。**電圧または電流が不足すると USB ポートが正常に動作せず、uFi が検出されない場合があります。**

    2. 純正品と同じ仕様の別の電源アダプターもお試しください。

### コンピューターに接続する

**Step 1**. SIMPoYo uFi をコンピューター（デスクトップ PC やノート PC など）の USB ポートに挿します。USB Ethernet デバイスとして自動認識され、すぐにオンラインになります。

**Step 2**. 他のデバイス（スマートフォン、タブレットなど）も、SIMPoYo uFi の 2.4 GHz Wi‑Fi ネットワークに接続して同時にインターネットを利用できます。

![multi-device](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/multi-device.jpg){class="glboxshadow"}

### USB電源に接続する

**Step 1**. SIMPoYo uFi を AC アダプター、モバイルバッテリー、車載充電器などの USB 電源に挿します。

**Step 2**. 電源が入ると、SIMPoYo uFi は **SIMPoYo-XXX** という SSID の Wi‑Fi ネットワークをブロードキャストします。

**Step 3**. 本体ラベルに記載された Wi‑Fi パスワード（Key）を確認します。このパスワードを使ってスマートフォン、タブレット、ノート PC などを SIMPoYo uFi の Wi‑Fi に接続し、インターネットを利用します。

## SIMPoYoプランをチャージする

データを使い切った場合や有効期限が切れた場合は、SIMPoYo uFi の QR コードをスキャンするか、[https://w.simpoyo.com](https://w.simpoyo.com){target="_blank"} にアクセスしてプランをチャージしてください。

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

1. デバイスを SIMPoYo uFi の Wi‑Fi ネットワークに接続します。

2. ブラウザを開き、`192.168.1.1` を入力して SIMPoYo uFi 管理パネルにアクセスします。

3. 管理者パスワードでログインします（デフォルトでは SIMPoYo uFi の Wi‑Fi パスワードと同じです）。

    ![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/0-simpoyo-login.png){class="glboxshadow"}

**ヒント**: SIMPoYo uFi の管理者パスワードを忘れた場合は、以下の手順でリセットしてください。

1. SIMPoYo uFi をコンピューター、ノート PC、または任意の USB 電源の USB ポートに挿します。自動的に電源が入ります。
2. ピンを Reset ピンホールに約 2 秒間差し込み、その後離します。
3. 8 ～ 10 秒待ちます。LED インジケーターがいったん消灯し、その後 2 つの白色ライトが点灯したら、リセット成功です。

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

### Wi‑Fi設定を変更する

1. 上部メニューから **Settings** を選択し、**Wi‑Fi Settings** に移動します。

    ![wifi settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.1-wifi-settings.png){class="glboxshadow"}

2. SIMPoYo uFi の Wi‑Fi ネットワーク名とパスワードをカスタマイズし、**Apply** をクリックします。

### APNを設定する

SIM カードで手動 APN 設定が必要な場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Cellular Settings** に移動します。

    ![cellular settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.2-cellular-settings.png){class="glboxshadow"}

2. **APN Mode** を **Manual** に切り替えます。

3. モバイル通信事業者から提供された情報を入力し、**Apply** をクリックします。

### ローミングを有効にする

ローミングを有効にすると、SIM カードが他の地域や国の現地通信事業者と接続できるため、ホームネットワーク圏外でも通信を継続できます。

以下の手順でローミングを有効にします。

1. 上部メニューから **Settings** を選択し、**Roaming** に移動します。

    ![roaming](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.3-roaming.png){class="glboxshadow"}

2. **Enable** を選択し、**Apply** をクリックします。

### PINコードを有効にする

PIN コードは SIM カード用の短いセキュリティパスワード（通常 4 ～ 8 桁）で、不正利用を防ぐために SIM カードをロックします。SIM が盗まれたり別のデバイスに挿されたりしても、PIN コードがなければ有効化または利用できません。

以下の手順で PIN コードを有効にします。

1. 上部メニューから **Settings** を選択し、**PIN Settings** に移動します。

    ![pin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.4-pin-settings.png){class="glboxshadow"}

2. **Enable** を選択し、PIN コードを設定して **Apply** をクリックします。

### 管理者パスワードを変更する

デフォルトの管理者パスワードは Wi‑Fi パスワードと同じです。セキュリティのため、初回設定時に変更してください。

1. 上部メニューから **Settings** を選択し、**Admin Settings** に移動します。

    ![admin settings](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.5-admin-settings.png){class="glboxshadow"}

2. Admin Password と Login Timeout をカスタマイズし、**Apply** をクリックします。

3. SIMPoYo uFi を工場出荷時設定に戻したい場合は、**Factory Default Setting** ボタンをクリックしてリセットします。

### 管理者パスワードをリセットする

SIMPoYo uFi の管理者パスワードを忘れた場合は、以下の手順でリセットしてください。

1. SIMPoYo uFi をコンピューター、ノート PC、または任意の USB 電源の USB ポートに挿します。自動的に電源が入ります。
2. ピンを Reset ピンホールに約 2 秒間差し込み、その後離します。
3. 8 ～ 10 秒待ちます。LED インジケーターがいったん消灯し、その後 2 つの白色ライトが点灯したら、リセット成功です。

### DHCP設定

デフォルトでは、SIMPoYo uFi の IP アドレスは `192.168.1.1` で、接続デバイスに IP アドレスを割り当てるための DHCP サーバーが有効になっています。

IP アドレスを変更したり、DHCP 設定をカスタマイズしたりしたい場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Advanced** -> **DHCP** に移動します。

    ![dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-dhcp.jpg){class="glboxshadow"}

2. ここでは、デバイスの IP アドレス変更、DHCP サーバーの有効 / 無効切り替え、IP 範囲やリース時間の設定ができます。DHCP 設定を行い、**Apply** をクリックします。

### MAC Filter

MAC Filter を使うと、MAC アドレスを管理して WLAN へアクセスできるデバイスを制御でき、ネットワークのセキュリティを強化できます。

MAC Filter はデフォルトで無効です。有効にする場合は、以下の手順に従ってください。

1. 上部メニューから **Settings** を選択し、**Advanced** -> **MAC Filter** に移動します。

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-1.png){class="glboxshadow"}

    上部の **User list** には接続中デバイスの詳細が表示されます。制御したいデバイスが一覧にあるか確認してください。ない場合は、SIMPoYo uFi の Wi‑Fi へ再接続してください。

2. **MAC Filter Mode** を **Black List** / **White List** に切り替えます。

    ![mac filter](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/3.6-mac-filter-2.png){class="glboxshadow"}

3. ブロックまたは許可したいデバイスの MAC アドレスを一覧へコピーし、**Apply** をクリックします。

### Upgrade

1. 上部メニューから **Upgrade** を選択し、**Device Info** に移動すると、SIMPoYo uFi のデバイス情報を確認できます。内容は以下を含みます。

    - ハードウェア情報（例: ハードウェアバージョン、MAC アドレス、IMEI、ICCID）
    - ソフトウェア情報（例: ソフトウェアバージョン）
    - WebUI 情報（例: WebUI バージョン）

    ![upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.1-upgrade.jpg){class="glboxshadow"}

2. 利用可能であればソフトウェアをアップグレードできます。

    左側のサイドバーで **Online Update** に切り替え、**Check New Update** ボタンをクリックすると、新しいバージョンの有無を確認できます。

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.2-online-update.png){class="glboxshadow"}

    または、左側のサイドバーで **Local Update** に切り替え、ファイルをアップロードして **Apply** をクリックすると手動アップグレードできます。

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_use_simpoyo_ufi/4.3-local-update.png){class="glboxshadow"}

## 付属アクセサリーガイド

パッケージには次のアクセサリーが含まれています。

- **USB-C to USB-A アダプターケーブル 1 本**: USB Type‑C ポートのみを備えたデバイス（ノート PC など）で SIMPoYo uFi を使用する場合に適しています。

- **USB-A to USB-A アダプターケーブル 1 本**: SIMPoYo uFi を USB ポート（コンピューターや USB 電源など）へ柔軟に接続でき、本体側ポートと接続先ポートの直接接触を避けられます。これにより、急な衝撃による金属インターフェースの損傷を防ぎやすくなります。

- **SIM 取り出しツール（ピン）1 本**: スマートフォンなどから SIM カードを取り出して SIMPoYo uFi へ装着する際や、必要に応じて uFi のリセットピンホールを押す際に使用します。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
