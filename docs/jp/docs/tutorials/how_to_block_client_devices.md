# GL.iNet ルーターで特定のクライアントデバイスをブロックする方法

このチュートリアルでは、GL.iNet ルーターで特定のクライアントデバイスをブロックする方法を説明します。クライアントデバイスをブロックすることで、ネットワークへの不正アクセスを防げます。これにより、ネットワークセキュリティの強化や、家族のインターネット利用の管理に役立ちます。

GL.iNet ルーターは、クライアントデバイスの MAC アドレス（ネットワーク上の各デバイスに割り当てられた 12 文字の一意の識別子）に基づいてデバイスをブロックします。この方法は MAC アドレスフィルタリングとも呼ばれます。

GL.iNet ルーターでクライアントデバイスをブロックする方法は 2 つあります。[ルーターの管理画面](#管理画面からクライアントデバイスをブロックする)を使う方法と、[GL.iNet モバイルアプリ](#glinet-モバイルアプリからクライアントデバイスをブロックする)を使う方法です。

## 管理画面からクライアントデバイスをブロックする

### 1. 管理画面にサインインする

Web ブラウザで `192.168.8.1` を入力します。パスワードを入力し、**Login** をクリックします。

### 2. クライアントデバイスをブロックする

MAC アドレスを把握しているかどうかによって、次の 2 通りの方法があります。

* MAC アドレスがわからない場合: 一覧に表示されているデバイスをブロックできる[方法 1](#方法-1-mac-アドレスがわからないデバイスをブロックする)を使用します。
* MAC アドレスがわかっている場合: [方法 2](#方法-2-mac-アドレスがわかっているデバイスをブロックする)を使用します。

#### 方法 1: MAC アドレスがわからないデバイスをブロックする

1. 左側のサイドバーで **Clients** をクリックします。
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. 対象デバイスの横にあるスイッチをオンにします。
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

一覧にブロックしたいデバイスが表示されない場合は、[MAC アドレスを blocklist に追加する方法](#方法-2-mac-アドレスがわかっているデバイスをブロックする)でブロックしてください。

#### 方法 2: MAC アドレスがわかっているデバイスをブロックする

この方法を使うには、デバイスの MAC アドレスを確認する必要があります。確認方法については、デバイスメーカーが案内している手順を参照してください。
デバイスの MAC アドレスを確認したら、次の手順に従います。

1. 左側のサイドバーで **Clients** をクリックします。
2. 上部の **Blocklist** をクリックします。
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. 次のいずれかの方法でデバイスをブロックします。
    - MAC アドレスを個別に入力する場合: 空欄に入力します。
    - MAC アドレスの一覧をインポートする場合: **Import Clients** をクリックします。ファイルをインポートしてから **Import** をクリックします。
4. **Apply** をクリックします。
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## GL.iNet モバイルアプリからクライアントデバイスをブロックする

**Note:** 開始する前に、デバイスに GL.iNet モバイルアプリをインストールして初期設定を完了してください。

MAC アドレスを把握しているかどうかによって、次の 2 通りの方法があります。

* MAC アドレスがわからない場合: 一覧に表示されているデバイスをブロックできる[方法 1](#mobile-1)を使用します。
* MAC アドレスがわかっている場合: [方法 2](#mobile-2)を使用します。

### 方法 1: MAC アドレスがわからないデバイスをブロックする {#mobile-1}

1. アプリのメイン画面で、**Connected Clients** と **Office Clients** の下にあるブロックしたいデバイスをタップします。
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. **Settings** の下で **Block** スイッチをオンにします。
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

一覧にブロックしたいデバイスが表示されない場合は、[MAC アドレスを blocklist に追加する方法](#mobile-2)でブロックしてください。

### 方法 2: MAC アドレスがわかっているデバイスをブロックする {#mobile-2}

この方法を使うには、ブロックしたいデバイスの MAC アドレスを確認する必要があります。確認方法については、メーカーが案内している手順を参照してください。
デバイスの MAC アドレスを確認したら、次の手順に従います。

1. アプリのメイン画面で、Settings アイコン > **Access Control** をタップします。
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. **Block** をタップします。
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. 次のいずれかの方法でデバイスをブロックします。
    - MAC アドレスを個別に入力する場合: **Add MAC address** をタップします。MAC アドレスを入力して、**Done** をタップします。
    - MAC アドレスの一覧をインポートする場合は、**Import Clients** > **Import Clients** をタップします。次にファイルをタップします。

---

まだご不明な点がありますか？ [Community Forum](https://forum.gl-inet.com){target="_blank"} または [Contact us](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
