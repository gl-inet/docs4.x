# Ethernet to USB-Aアダプター経由でデュアル有線Ethernet WANを設定する方法

Ethernet to USB-A アダプターを使用すると、WAN ポートが1つしかないルーターでも、デュアル有線Ethernet WANアクセスを構成できます。

GL.iNetルーターは一般的な Ethernet to USB-A アダプターをサポートしています。これにより、ISPルーターからの有線Ethernet接続を、ルーターの USB ポート経由で USB 接続に変換でき、WAN ポートに加えて追加の有線Ethernetアクセスを利用できます。

## トポロジー

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## セットアップ手順

1. Ethernet to USB-A アダプターを GL.iNetルーターの USB ポートに差し込み、もう一方を ISPルーターに接続します。

2. USB ドライバーをインストールします。

    ルーターの Web 管理画面にログインし、**Application** -> **Plug-ins** に移動して、お使いのアダプター用の USB ネットワークドライバーをインストールします。

    たとえば Realtek アダプターを使用している場合は、**kmod-usb-net-rtl8152** ドライバーをインストールしてください。

    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    インストールが完了するまで待ちます。

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. USB Tethering で接続します。

    ドライバーのインストールが完了したら、**INTERNET** -> **Tethering** に移動します。

    USB 接続が検出され、ISPルーターへ接続できるようになります。

    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    **Connect** をクリックして1分ほど待ちます。緑色のドットが点灯し、IP アドレスなどの情報がページに表示されたら、USB Tethering 接続は成功です。

    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="_blank"} からお問い合わせください。
