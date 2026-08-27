# WinSCPを使って共有ファイルにアクセスする

**WinSCP** を使うと、**GL-Routers** のファイル共有機能で共有ファイルにアクセスできます。

ネットワークストレージのタブで **WebDAV** リンクを設定してください。設定の詳細については、[WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav) のセットアップを参照してください。

## WinSCPでリンクを設定する

WebDAV の設定が完了したら、ネットワークストレージの **Share Folders** ページに戻ります。

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

**"..."** アイコンを右クリックして HTTPS リンクをコピーします。

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

WinSCP を起動し、WebDAV を選択して TLS/SSL encryption も選択します。次に、リンクを **Host name** に貼り付けます。ポート番号は自動的に 6008 に変わります。

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

ユーザー名とパスワードを入力し、保存してログインすると、共有フォルダが開きます。

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
