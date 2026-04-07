# LAN

Web Admin Panel の左側で、**NETWORK** -> **LAN** に移動します。

LAN は、デバイスがメイン Wi-Fi または Ethernet ケーブルで接続されたときに利用するネットワークです。

このページには基本設定、DHCP Server 設定、Address Reservation が含まれます。

## 基本設定

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    これは、ルーターの管理画面にアクセスする際にブラウザーのアドレスバーへ入力するアドレスです。
    
    デフォルトは **192.168.8.1** です。ネットワークと競合する場合は変更できます。

- **Netmask**

    デフォルトは **255.255.255.0** です。より多くの IP アドレスが必要な大きなサブネットが必要な場合は、**255.255.0.0** も選択できます。

- **AP Isolation**

    クライアントデバイスを別のネットワークセグメントに分離できます。これらのデバイスは同じネットワーク上のほかのデバイスと通信できなくなります。

## DHCPサーバー

**DHCP Server** はデフォルトで有効です。DHCP サーバーは各クライアントデバイスに IP アドレスとそのほかの通信パラメーターを自動的に割り当てます。

DHCP サーバーを無効にした場合は、クライアントデバイス側でネットワーク設定を手動で行う必要があります。静的 IP を手動で設定する方法については、[こちら](../tutorials/manually_configure_static_ip.md) を参照してください。

開始 IP アドレスと終了 IP アドレスは、ネットワークの拡大・縮小、IP アドレス競合の発生、サブネットマスク範囲の変更など、必要に応じて変更できます。

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

必要に応じて **Advanced** をクリックすると、さらに詳細な設定を行えます。

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: DHCP で割り当てられた IP アドレスがデバイスに対して有効である期間です。

- **Gateway**: ローカルネットワークとインターネットなどの外部ネットワークの間でトラフィックをルーティングするデバイスです。

- **DNS Server 1**: ドメイン名を IP アドレスへ変換するプライマリサーバーです。

- **DNS Server 2**: プライマリ DNS サーバーが利用できない場合に、名前解決に使用されるセカンダリサーバーです。

- **LPR Server**: （Line Printer Remote Server）印刷ジョブを管理し、ネットワークデバイスからリモートプリンターへ印刷要求を送れるようにするサービスです。複数の LPR プリンターポートを設定できます。

## アドレス予約

LAN 内のクライアントに予約 IP アドレスを指定すると、そのクライアントはルーターの DHCP Server に接続するたびに常に同じ IP アドレスを受け取ります。固定 IP 設定が必要なコンピューターやサーバーに予約 IP アドレスを割り当てられます。

**Note:** 設定したクライアントは反映のためにルーターへ再接続する必要があります。

**Add** をクリックして IP を予約します。

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

ポップアップウィンドウが表示されます。

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

ドロップダウンリストから **MAC** を選択すると、選択した MAC に対応する **IP** が自動入力されます。わかりやすい名前を付けて、**Submit** をクリックします。

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

新しい IP アドレス予約を追加すると、以下の画面が表示され、設定が正常に完了したことを示します。

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
