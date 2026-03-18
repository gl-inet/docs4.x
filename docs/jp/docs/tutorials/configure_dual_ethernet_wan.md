# Ethernet to USB-A アダプターを使用して有線LAN WANを二重に設定する

単一WANポートルーターで、Ethernet to USB-A アダプターを使用して有線LAN WANアクセスを二重に設定できます。

GL.iNetルーターは、一般的なEthernet to USB-A アダプターをサポートしています。これにより、ISPルーターからの有線LANアクセスをルーターのUSBポート経由でUSB接続に変換し、WANポートに加えてルーターに追加の有線LANアクセスを提供します。

## 構成

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## セットアップ手順

1. Ethernet to USB-A アダプターをGL.iNetルーターのUSBポートに差し込み、もう一方の端をISPルーターに接続します。

2. USBドライバーをインストールします。

    ルーターのWeb管理パネルにログインし、**アプリケーション** -> **プラグイン**に移動して、アダプター用のUSBネットワークドライバーをインストールします。

    例えば、Realtek アダプターを使用する場合は、**kmod-usb-net-rtl8152**ドライバーをインストールしてください。

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    インストールが完たするまでお待ちください。

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. USBテザリングで接続します。

    ドライバーインストールが完了したら、**インターネット** -> **テザリング**セクションに移動します。

    USB接続が検出され、ISPルーターに接続できます。

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    **接続**をクリックして1分待ちます。绿灯が時灯し、ページ上にIPアドレスなどの情報が表示された場合、USBテザリング接続は成功しています。

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
