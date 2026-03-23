# MACアドレス

このガイドはファームウェア v4.5 以前に適用されます。

MAC Address ページは以前は MAC Clone という名称で、v4.2 以降は MAC Address に変更されました。

v4.6 以降、Ethernet と Repeater インターフェースの MAC アドレス設定は、それぞれ [Ethernet Port](ethernet_port.md) ページと [Repeater](internet_repeater.md) ページに移動しました。

---

Web 管理画面の左側で **NETWORK** -> **MAC Address** に移動します。

このページでは、ルーターのデフォルト MAC アドレスの確認、クライアントの MAC アドレスのクローン、MAC アドレスの手動入力、ランダムな MAC アドレスの生成ができます。

デバイスが複数の Ethernet ポートを WAN ポートとして使用できる場合は、各ポートごとに MAC アドレスを個別に設定できます。MAC アドレス設定は、その Ethernet ポートが WAN ポートとして使用されている場合にのみ有効です。

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* 工場出荷時のデフォルトMACアドレス。

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* クライアントのMACアドレスをクローン。

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **注意:** 多くの新しいデバイスは今、異なるWi-Fiに接続するために異なるランダムなMACアドレスを使用しているため、ここに表示されるMACアドレスはユーザーのデバイスの実際のMACアドレスではない可能性があります。ランダム化されたMACは、異なるデバイスでプライベートWi-Fiアドレスまたはランダムなハードウェアアドレスと呼ばれることもあります。

* 手動入力またはランダムなMACアドレスを生成。

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## 使用シナリオ

パブリックのホットスポットに接続する際、ホットスポットに実際のMACアドレスを知られたくない場合や、MACアドレスに基づいてインターネットへのアクセスを制限されたくない場合は、ランダムなMACアドレスを使用してください。[キャプティブポータルを使用してホットスポットに接続する](../faq/connect_to_a_hotspot_with_captive_portal.md)ガイドをご覧ください。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
