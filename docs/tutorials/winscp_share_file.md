# WinSCPを使用して共有ファイルにアクセスする

**WinSCP**を使用して、**GL-Routers**のファイル共有機能で共有ファイルにアクセスできます。

ネットワークストレージタブで**WebDAV**リンクを設定してください。詳細な設定については、[WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav)の設定を参照してください。

## WinSCPでのリンク設定

WebDAVを設定した後、ネットワークストレージの**共有フォルダ**ページに戻ります。

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

**「...」**アイコンを右クリックして、HTTPSリンクをコピーします。

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

WinSCPを起動し、WebDAVを選択し、TLS/SSL暗号化も選択します。その後、リンクを**ホスト名**に貼り付けます。ポート番号は自動的に6008に変更されます。

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

ユーザー名とパスワードを入力し、保存してログインをクリックすると、共有フォルダが開きます。

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}
