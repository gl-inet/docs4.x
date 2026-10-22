# デバイスのすべての MAC アドレスを確認するには？ {#how-can-i-find-all-mac-addresses-of-my-device}

## 使用シナリオ {#usage-scenario}

GL.iNet デバイスの MAC アドレスは、WAN 1、WAN 2、LAN ポート、2.4G Wi-Fi、5G Wi-Fi など、ネットワークインターフェースごとに一意です。

ホテル、キャンプ場、キャンパスなどのネットワークに接続する場合、インターネットへアクセスする前に、ネットワーク管理者からデバイスの MAC アドレスをホワイトリストへ登録するよう求められることがあります。

次の方法で、デバイスの正確な MAC アドレスを確認できます。

## 方法 1. 製品ラベルで確認する（WAN MAC のみ） {#method-1-via-product-label-for-wan-mac-only}

底面ラベルで **WAN MAC address** を確認します。

たとえば、下の画像では WAN MAC は E4:95:6E:40:DB:A9 です。

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/wan_lan_wifi.png){class="glboxshadow"}

## 方法 2. SSH で確認する {#method-2-via-ssh}

SSH の使用方法については、[こちら](../tutorials/ssh_log_in_to_the_router.md)を参照してください。

SSH で **ifconfig** を入力すると、br-lan、ethx、wlanx などのインターフェースが順に表示されます。

### Ethernet ポートの MAC を確認する {#find-the-mac-of-ethernet-ports}

次の画像を例にします。

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwan.jpg){class="glboxshadow"}

- **eth0** は WAN ポートで、MAC アドレスは **94:83:C4:19:19:08** です。

    WAN ポートがもう 1 つある場合（例：GL-MT6000）、WAN MAC アドレスももう 1 つあります。

- **eth1**、**eth2** などは LAN ポートで、MAC アドレスは **94:83:C4:19:19:09** です。

    LAN ポートが複数あっても、LAN の MAC アドレスは 1 つだけです。

### 無線ポートの MAC を確認する {#find-the-mac-of-wireless-ports}

次の画像を例にします。

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** は 2.4G Wi-Fi で、MAC アドレスは **96:83:C4:19:19:0B** です。

- **wlan1** は 5G Wi-Fi で、MAC アドレスは **94:83:C4:19:19:0A** です。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
