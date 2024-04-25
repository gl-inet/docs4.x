# LAN

ウェブ管理画面の左側 -> NETWORK -> LAN

## LAN

LANは、あなたのデバイスがメインWiFiに接続するか、イーサネットケーブルを介して接続する場合のネットワークです。

**ルーターIPアドレス** はデフォルトで**192.168.8.1** です。ネットワークと競合する場合は変更できます。

![lan simple set](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/lan_simple_set.jpg){class="glboxshadow"}

### セキュリティ設定

**クライアントの隔離**: ネットワークのクライアント デバイスを別のネットワーク領域に分離できます。これらのデバイスは、他のデバイスと通信したり、ネットワーク上で相互に通信したりすることはできません。

## DHCPサーバー

*DHCP サーバー**はデフォルトで有効になっています。DHCP サーバーは、各クライアント デバイスに IP アドレスとその他の通信パラメータを自動的に割り当てます。DHCP サーバーが無効になっている場合は、クライアントごとに手動で設定する必要があります。 [静的IPを手動で設定する方法は？](../tutorials/manually_configure_static_ip.md)

例えば、ネットワークの規模が拡大または縮小した場合、ネットワーク内でIPアドレスの競合が発生した場合、サブネットマスクやIPアドレスの範囲が変更された場合など、必要に応じて開始IPアドレスと終了IPアドレスを変更することができます。

![dhcp_simple_set](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_simple_set.jpg){class="glboxshadow"}

### アドバンスト

**アドバンスト**をクリックすると、さらに手動で設定できます。

![lan page, private network advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_set.jpg){class="glboxshadow"}

## アドレス予約

LAN 内のクライアントに予約 IPアドレスを 指定する と 、クライアントは、 ルータ の DHCP サーバーにア クセスするたびに、 常に同じ IP アドレスを受信します。予約 IP アドレスは、 永続的な IP 設定を必要 とするコンピ ュータ またはサーバーに割 り 当てる こ とができます。

**注意:** 設定されたクライアントは、アクティベートするためにルーターに再接続する必要があります。

**追加** をクリックして IP を予約します。

![lan page, Address Reservation](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/reserve_ip.png){class="glboxshadow"}

**MAC** を選択します。MAC を選択すると、**IP** が自動的に入力されます。 わかりやすい名前を付けてください。 次に、**送信** をクリックします。

![lan page, Address Reservation, add a new reservation entry](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/add_a_new_reservation_entry.png){class="glboxshadow"}

新しい IP アドレス予約を追加した後：

![lan page, added reserve ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/reserve_ip_added.png){class="glboxshadow"}
