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

Click the cog icon for Repeater options.

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

![repeater options](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Network**. If the option is enabled, the router will automatically connect to other saved networks when it is unable to connect to the current Wi-Fi network.

* **Band Selection**. If you manually select a band, the router will not scan or connect to any Wi-Fi with another band.

* **Allow Repeat DFS Channels**. If the option is enabled, 5GHz Wi-Fi will be temporarily unavailable when a radar is using the channel which is currently router using; Otherwise, the router will not connect to any Wi-Fi using DFS channels.

* **Force 20MHz Bandwith For 2.4G**. If the option is enabled, The device will prompting the stability of the connection in exchange of reducing the connection speed. It only works when repeating 2.4G Wi-Fi.

## Manage known network

To delete known network, click **Switch Network**.

![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_connected.png){class="glboxshadow"}

Or click **Connect**.

![repeater](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_sector.png){class="glboxshadow"}

On the **Knows Network** sector, click trash icon to delete a known network, click cog icon to config the network.

![repeater known network](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_known_networks.png){class="glboxshadow"}

## Join other network

![](https://static.gl-inet.com/docs/en/4/tutorials/internet_repeater/repeater_join_other_network.png){class="glboxshadow"}
