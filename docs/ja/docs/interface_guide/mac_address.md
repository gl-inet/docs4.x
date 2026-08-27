# MACアドレス

このガイドはファームウェア v4.5 以前に適用されます。

MAC Address ページは以前は MAC Clone という名称で、v4.2 以降は MAC Address に変更されました。

v4.6 以降、Ethernet と Repeater インターフェースの MAC アドレス設定は、それぞれ [Ethernet Port](ethernet_port.md) と [Repeater](internet_repeater.md) に移動しました。

---

Web Admin Panel の左側で、**NETWORK** -> **MAC Address** に移動します。

このページでは、ルーターのデフォルト MAC アドレスの確認、クライアントの MAC アドレスのクローン、MAC アドレスの手動入力、ランダムな MAC アドレスの生成ができます。

デバイスが複数の Ethernet ポートを WAN ポートとして使用できる場合は、各ポートごとに MAC アドレスを個別に設定できます。MAC アドレス設定は、その Ethernet ポートが WAN ポートとして使われている場合にのみ有効です。

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* 工場出荷時のデフォルト MAC アドレス。

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* クライアントの MAC アドレスをクローンします。

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Note:** 多くの新しいデバイスでは、接続先 Wi-Fi ごとに異なるランダム MAC アドレスを使用します。そのため、ここに表示される MAC アドレスは、実際のデバイスの MAC アドレスではない可能性があります。ランダム化された MAC は、デバイスによっては Private Wi-Fi Address や random hardware address と呼ばれることもあります。

* 手動入力、またはランダムな MAC アドレスの生成。

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## 使用シナリオ

パブリックホットスポットへ接続する際、実際の MAC アドレスを知られたくない場合や、MAC アドレスに基づいてインターネットアクセスを制限されたくない場合は、ランダムな MAC アドレスを使用してください。詳しくは、[Connect to a Hotspot with a Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md) を参照してください。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
