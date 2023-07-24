# リピーターで既存のWi-Fiを経由してインターネットに接続します。

リピータの使用は、ホテルやカフェで無料Wi-Fiを使用する場合など、ルータを既存の別のワイヤレスネットワークに接続することを意味します。

デフォルトではWISP (Wireless Internet Service Provider) モードで動作します。これは、ルーターが独自のサブネットを作成し、パブリックネットワークからあなたを保護するファイアウォールとして動作することを意味します。

ウェブ管理画面の左側にある  -> インターネット, リピーター セクター.

## 基本的な流れ

![リピーター](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

上の画像の **接続** 

![repeater join wlan](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_wlan.png){class="glboxshadow"}

ドロップダウンリストからSSIDを選択し、そのパスワードを入力します。接続したいSSIDがリストにない場合。下の画像をクリックしてください。 　[Join Other Network](#join-other-network) 　

![repeater join network](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_network.png){class="glboxshadow"}

For [Advanced Settings](#join-network-advanced-setting).

しばらく待って、パスワードが正しければ、接続は成功します。

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

## ジョインネットワークの詳細設定

ネットワークに参加する際、さらに2つのオプションがあります。

![repeater join network advanced setting](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_network_advanced_setting.png){class="glboxshadow"}

* **ロック　BSSID**. このオプションを有効にすると、ルーターはこのSSIDを使用するネットワークに切り替えたときに、選択したBSSIDに対応するAPにのみ接続します。

* **手動で設定する静的IP**.

## リピーターオプション

リピーターオプションのコグアイコンをクリックします。

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

![repeater options](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_options.png){class="glboxshadow"}

* **保存した他のネットワークへの切り替えを許可する**。このオプションを有効にすると、現在のWi-Fiネットワークに接続できない場合、ルーターは自動的に他の保存されたネットワークに接続します。

* **バンド選択**。手動でバンドを選択した場合、ルーターは他のバンドでWi-Fiをスキャンしたり接続したりしません。

* **繰り返しDFSチャネルを許可します**。 このオプションが有効になっている場合、レーダーが現在使用しているチャネルを使用している場合、5GHz Wi-Fiは一時的に利用できません。 それ以外の場合、ルーターはDFSチャネルを使用してWi-Fiに接続しません。
* **2.4G用20MHz帯域の強制使用**。 このオプションを有効にすると、接続速度を下げる代わりに、接続の安定性を促します。2.4GのWi-Fiを繰り返し使用する場合のみ有効です。

## 既知のネットワークを管理する

既知のネットワークを削除するには、 **スイッチネットワーク**をクリックします。

![リピータ接続](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

 または**接続**をクリックします。

![リピータ](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

**既知のネットワーク** セクターで、 [ゴミ箱アイコン]をクリックして既知のネットワークを削除し、[歯車アイコン]をクリックしてネットワークを構成します。

![既知のネットワークのリピーター](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_known_networks.png){class="glboxshadow"}

## 既知のネットワークのリピーター

![](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_other_network.png){class="glboxshadow"}
