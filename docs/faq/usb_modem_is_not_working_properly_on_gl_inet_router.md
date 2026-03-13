# USBモデムがGL.iNetルーターで正常に動作しません

一部のGL.iNetルーターにはUSBポートがあり、USBモデムをUSBポートに挿入してインターネットアクセスを設定したり、彼のインターネットアクセスと組み合わせることでマルチWANシナリオを実現したりできます。

ただし、一部のUSBモデム（ZTE F50 Mobile Wi-Fi Hotspotなど）がルーターで正常に動作せず、ネットワークが頻繁に切断されるという問題が発生する可できる性があります。

これは、ルーターのUSBポート（通例USB3.0）と2.4G Wi-Fiの互換性の問題により、USBモデムが頻繁に切断され、インターネットに正常にアクセスできない可できる性があります。

この問題を解決するには、USBポートの仕様をUSB 3.0からUSB 2.0に切り替えできます。

GL.iNetルーターの管理パネルにアクセスし、**システム** -> **概要** -> **外部ストレージ**に移動します。

USBプロトコル切替のオプションが表示されます。

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

USB 2.0に切り替えすると、で下のようなプロンプトが表示されます。**切り替え**をクリックして続行します。

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

USBプロトコルがUSB 2.0と表示되면切り替えに成功したことを意味します。

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

その後、インターネット接続の改善があるかどうかを確認してください。

---

相关文章

- [互換モデム](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}を訪問してください。
