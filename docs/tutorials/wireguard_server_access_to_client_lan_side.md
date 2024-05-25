# サーバーからWireGuardクライアントLAN側にアクセスする方法

## WireGuardサイト間トンネルのトポロジー

クライアント側の**192.168.8.1** **(GL-AXT1800)**のサブネット（NAS、IPカメラなど）にアクセスしたい場合：

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

### 1. サーバーのVPNダッシュボードに移動する

アイコンをクリックしてカスタムルールページに入ります。
![Custom rule](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Custom%20rule.jpg){class="glboxshadow"}

アクセスしたいサブネットを入力します。この場合は**192.168.8.0/24**で、スコープに**global**を入力します。

ゲートウェイはクライアントルーターのWireGuard IPです。WireGuardサーバーページで確認できます。

![addrule](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/addrule.jpg){class="glboxshadow"}

### 2. **WireGuardサーバー**に移動し、**プロファイル**でクライアントIP（ゲートウェイ）を確認し、修正アイコンをクリックします。

![gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/gateway.jpg){class="glboxshadow"}

**もっと詳しく**をクリックします。

![Setup](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/setup.jpg){class="glboxshadow"}

**+**をクリックして許可するIPを追加し、**適用**をクリックして新しい設定を取得します。

![allowip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/allowip.jpg){class="glboxshadow"}

### 3. 設定をダウンロードする

設定をクライアントルーター**192.168.8.1**にロードします。この場合はGL-AXT1800です。

**GL-MT2500**から**192.168.8.1** **(GL-AXT1800)**にpingを送信してテストできます。

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}