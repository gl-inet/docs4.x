# Ethernet to USB-Aアダプター経由でデュアル有線Ethernet WANを設定する方法

Ethernet to USB-A アダプターを使うことで、WANポートが1つしかないルーターでも、デュアル有線Ethernet WANアクセスを構成できます。

GL.iNetルーターは一般的なEthernet to USB-A アダプターをサポートしています。これにより、ISPルーターからの有線Ethernet接続を、ルーターのUSBポート経由のUSB接続へ変換できます。その結果、WANポートに加えて、追加の有線Ethernet接続を利用できるようになります。

## トポロジー

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## セットアップ手順

1. Ethernet to USB-A アダプターを GL.iNet ルーターのUSBポートへ接続し、もう一方の端を ISP ルーターへ接続します。

2. USBドライバーをインストールします。

   ルーターのWeb管理画面にログインし、**Application** -> **Plug-ins** に移動して、使用しているアダプター向けのUSBネットワークドライバーをインストールします。

   たとえば、Realtek 製アダプターを使用している場合は、**kmod-usb-net-rtl8152** ドライバーをインストールしてください。

   ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

   インストールが完了するまで待ちます。

   ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. USB Tethering で接続します。

   ドライバーのインストールが完了したら、**INTERNET** -> **Tethering** セクションに移動します。

   USB接続が検出され、ISPルーターへ接続できるようになります。

   ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

   **Connect** をクリックして1分ほど待ちます。緑色のドットが点灯し、ページにIPアドレスなどの情報が表示されれば、USB Tethering 接続は成功しています。

   ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
