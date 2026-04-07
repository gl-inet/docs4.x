# USBモデムがGL.iNetルーターで正常に動作しません

一部のGL.iNetルーターにはUSBポートがあり、USBモデムをUSBポートに挿入してインターネットアクセスを設定したり、他のインターネットアクセスと組み合わせることでマルチWANシナリオを実現したりできます。

ただし、一部のUSBモデム（ZTE F50 Mobile Wi-Fi Hotspotなど）がルーターで正常に動作せず、ネットワークが頻繁に切断されるという問題が発生する可能性があります。

これは、ルーターのUSBポート（通常USB3.0）と2.4G Wi-Fiの互換性の問題により、USBモデムが頻繁に切断され、インターネットに正常にアクセスできない可能性があります。

この問題を解決するには、USBポートの仕様をUSB 3.0からUSB 2.0に切り替えることができます。

GL.iNetルーターの管理パネルにアクセスし、**SYSTEM -> Overview -> External Storage**に移動します。

USBプロトコル切り替えのオプションが表示されます。

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

USB 2.0に切り替えると、以下のようなプロンプトが表示されます。**Switch**をクリックして続行します。

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

USBプロトコルがUSB 2.0と表示されると、切り替えに成功したことを意味します。

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

その後、インターネット接続の改善があるかどうかを確認してください。

---

関連記事

- [互換モデム](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

まだご質問はありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
