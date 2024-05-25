# GL.iNetルーターで特定のクライアントデバイスをブロックする方法

このチュートリアルでは、GL.iNetルーターで特定のクライアントデバイスをブロックする方法を説明します。クライアントデバイスをブロックすることで、ネットワークへの不正アクセスを防止できます。これにより、ネットワークのセキュリティを強化したり、家族のインターネットアクセスを管理したりすることができます。

GL.iNetルーターは、MACアドレス（ネットワーク上の個々のデバイスに割り当てられた一意の12文字の識別子）に基づいてクライアントデバイスをブロックします。この方法はMACアドレスフィルタリングとも呼ばれます。

GL.iNetルーターでクライアントデバイスをブロックする方法は2つあります：[ルーター管理パネル](#ルーター管理パネルからクライアントデバイスをブロックする)または[GL.iNetモバイルアプリ](#glinetモバイルアプリからクライアントデバイスをブロックする)を使用する方法です。

## ルーター管理パネルからクライアントデバイスをブロックする

### 1. 管理パネルにサインインする

ウェブブラウザに「192.168.8.1」と入力します。パスワードを入力し、**Login**をクリックします。

### 2. クライアントデバイスをブロックする

MACアドレスの有無に応じて、クライアントデバイスをブロックする方法は2つあります：

* MACアドレスがない場合: [最初の方法](#方法1-macアドレスなしでデバイスをブロックする)を使用して、リストに表示されるデバイスをブロックします。
* MACアドレスがある場合: [第二の方法](#方法2-macアドレスを使用してデバイスをブロックする)を使用します。

#### 方法1: MACアドレスなしでデバイスをブロックする

1. 左側のサイドバーで**Clients**をクリックします。
![クライアントをクリック](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. デバイスの横にあるスイッチをオンに切り替えます。
![スイッチを切り替え](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

リストにブロックしたいデバイスが表示されない場合は、[MACアドレスをブロックリストに追加してブロック](#方法2-macアドレスを使用してデバイスをブロックする)する必要があります。

#### 方法2: MACアドレスを使用してデバイスをブロックする

この方法を使用するには、デバイスのMACアドレスを取得する必要があります。デバイスの製造元が提供する指示を参照してください。
デバイスのMACアドレスを取得したら、次の手順に従います：

1. 左側のサイドバーで**Clients**をクリックします。
2. 上部で**Blocklist**をクリックします。
![ブロックリストをクリック](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. 次のいずれかの方法でデバイスをブロックします：
    - MACアドレスを個別に入力する場合: 空のフィールドに入力します。
    - MACアドレスのリストをインポートする場合: **Import Clients**をクリックし、ファイルをインポートしてから**Import**をクリックします。
4. **Apply**をクリックします。
![適用をクリック](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## GL.iNetモバイルアプリからクライアントデバイスをブロックする

**注:** 始める前に、GL.iNetモバイルアプリをデバイスにインスト
# GL.iNetルーターで特定のクライアントデバイスをブロックする方法（モバイルアプリ）

クライアントデバイスをブロックする方法は、MACアドレスの有無に応じて2つあります：

* MACアドレスがない場合: リストに表示されるデバイスをブロックできる[最初の方法](#mobile-1)を使用します。
* MACアドレスがある場合: [第二の方法](#mobile-2)を使用します。

### 方法1: MACアドレスなしでデバイスをブロックする {#mobile-1}

1. メインアプリ画面で、**Connected Clients**または**Office Clients**の下にあるブロックしたいデバイスをタップします。
![デバイスをタップ](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. **Settings**の下で、**Block**スイッチをオンに切り替えます。
![ブロックスイッチを切り替え](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

リストにブロックしたいデバイスが表示されない場合は、[MACアドレスをブロックリストに追加してブロック](#mobile-2)する必要があります。

### 方法2: MACアドレスを使用してデバイスをブロックする {#mobile-2}

この方法を使用するには、ブロックしたいデバイスのMACアドレスを取得する必要があります。デバイスの製造元が提供する指示を参照してください。
デバイスのMACアドレスを取得したら、次の手順に従います：

1. メインアプリ画面で、設定アイコン > **Access Control**をタップします。
![アクセスコントロールをタップ](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. **Block**をタップします。
![ブロックをタップ](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. 次のいずれかの方法でデバイスをブロックします：
    - MACアドレスを個別に入力する場合: **Add MAC address**をタップし、MACアドレスを入力して**Done**をタップします。
    - MACアドレスのリストをインポートする場合: **Import Clients** > **Import Clients**をタップしてファイルを選択します。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com)をご覧ください。