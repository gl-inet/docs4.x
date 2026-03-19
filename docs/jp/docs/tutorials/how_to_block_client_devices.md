# GL.iNetルーターで特定のクライアントデバイスをブロックする方法

このチュートリアルでは、GL.iNetルーターで特定のクライアントデバイスをブロックする方法を説明します。クライアントデバイスをブロックすると、ネットワークへの不正アクセスを防止できます。これにより、ネットワークのセキュリティ向上や、家族のインターネット利用管理に役立ちます。

GL.iNetルーターでは、MACアドレスをもとにクライアントデバイスをブロックします。MACアドレスは、ネットワーク上の各デバイスに割り当てられた12文字の固有識別子です。この方式はMACアドレスフィルタリングとも呼ばれます。

クライアントデバイスをブロックする方法は2つあります。ルーターの[管理画面](#管理画面からクライアントデバイスをブロックする)を使う方法と、[GL.iNetモバイルアプリ](#glinetモバイルアプリからクライアントデバイスをブロックする)を使う方法です。

## 管理画面からクライアントデバイスをブロックする

### 1. 管理画面にサインインする

Webブラウザーで `192.168.8.1` を開きます。パスワードを入力し、**Login** をクリックします。

### 2. クライアントデバイスをブロックする

MACアドレスを把握しているかどうかによって、手順が異なります。

- MACアドレスがわからない場合: [方法1](#方法1-macアドレスがわからないデバイスをブロックする)を使うと、一覧に表示されているデバイスをブロックできます。
- MACアドレスがわかっている場合: [方法2](#方法2-macアドレスがわかっているデバイスをブロックする)を使います。

#### 方法1: MACアドレスがわからないデバイスをブロックする

1. 左側のサイドバーで **Clients** をクリックします。
   ![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. 対象デバイスの横にあるスイッチをオンにします。
   ![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

一覧にブロックしたいデバイスが表示されない場合は、[MACアドレスをブロックリストへ追加する方法](#方法2-macアドレスがわかっているデバイスをブロックする)を使用してください。

#### 方法2: MACアドレスがわかっているデバイスをブロックする

この方法では、ブロックしたいデバイスのMACアドレスが必要です。確認方法は、デバイスメーカーが案内している手順を参照してください。
MACアドレスを確認したら、次の手順を実行します。

1. 左側のサイドバーで **Clients** をクリックします。
2. 上部で **Blocklist** をクリックします。
   ![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. 次のいずれかの方法でデバイスをブロックします。
   - MACアドレスを個別に入力する場合: 空欄にMACアドレスを入力します。
   - MACアドレスの一覧をインポートする場合: **Import Clients** をクリックし、ファイルを読み込んでから **Import** をクリックします。
4. **Apply** をクリックします。
   ![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## GL.iNetモバイルアプリからクライアントデバイスをブロックする

**Note:** 開始前に、端末へGL.iNetモバイルアプリをインストールし、初期設定を済ませてください。

MACアドレスを把握しているかどうかによって、手順が異なります。

- MACアドレスがわからない場合: [方法1](#mobile-1)を使うと、一覧に表示されているデバイスをブロックできます。
- MACアドレスがわかっている場合: [方法2](#mobile-2)を使います。

### 方法1: MACアドレスがわからないデバイスをブロックする {#mobile-1}

1. アプリのメイン画面で、**Connected Clients** または **Office Clients** の一覧から、ブロックしたいデバイスをタップします。
   ![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. **Settings** 内にある **Block** スイッチをオンにします。
   ![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

一覧にブロックしたいデバイスが表示されない場合は、[MACアドレスを使ってブロックリストへ追加する方法](#mobile-2)を使用してください。

### 方法2: MACアドレスがわかっているデバイスをブロックする {#mobile-2}

この方法では、ブロックしたいデバイスのMACアドレスが必要です。確認方法は、デバイスメーカーが案内している手順を参照してください。
MACアドレスを確認したら、次の手順を実行します。

1. アプリのメイン画面で、設定アイコン > **Access Control** をタップします。
   ![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. **Block** をタップします。
   ![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. 次のいずれかの方法でデバイスをブロックします。
   - MACアドレスを個別に入力する場合: **Add MAC address** をタップし、MACアドレスを入力して **Done** をタップします。
   - MACアドレスの一覧をインポートする場合: **Import Clients** > **Import Clients** をタップし、ファイルを選択します。

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
