# MACアドレス

このガイドはファームウェアv4.5で前に当てはまります。

v4.6で降、イーサネットとリピーターインターフェースのMACアドレス設定はそれぞれ[ポート管理](network_port_management.md)ページと[インターネット](internet_repeater.md)ページにに移行しました。

---

ウェブ管理パネルの左側 -> ネットワーク -> MACアドレス

MACアドレスページはで前はMACクローン」と呼ばれていましたが、v4.2で降MACアドレス」に変よりされました。

このページでは、ルーターのデフォルトMACアドレスを見つけ、クライアントのMACアドレスをクローンしたり、MACアドレスを手動で入力したり、ランダムなMACアドレスを生成したりできます。

デバイスが複数のEthernetポートをWANポートとして使用するように設定することをサポートしている場合、各ポートのMACアドレスを個別に設定できます。MACアドレス設定は、EthernetポートがWANポートとして使用されている場合にのみ有効であることに注意してください。

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* 工場出荷時のデフォルトMACアドレス。

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* クライアントのMACアドレスをクローン。

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **注意:** 多くの新しいデバイスは今、異なるWi-Fiに接続するために異なるランダムなMACアドレスを使用しているため、ここに表示されるMACアドレスはユーザーのデバイスの実際のMACアドレスではない可できる性があります。ランダム化されたMACは、異なるデバイスでプライベートWi-Fiアドレスまたはランダムなハードウェアアドレスと呼ばれることもあります。

* 手動入力またはランダムなMACアドレスを生成。

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## 使用シナリオ

パブリックのホットスポットに接続する際、ホットスポットに実際のMACアドレスを知られたくない場合や、MACアドレスに基づいてインターネットへのアクセスを制限されたくない場合は、ランダムなMACアドレスを使用してください。[キャプティブポータルを使用してホットスポットに接続する](../faq/connect_to_a_hotspot_with_captive_portal.md)ガイドをご覧ください。

---

まだご質問はありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
