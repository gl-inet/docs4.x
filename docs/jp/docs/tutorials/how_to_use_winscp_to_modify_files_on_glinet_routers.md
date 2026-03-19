# WinSCP を使って GL.iNet ルーター上のファイルを編集する方法

WinSCP は、ルーター上のファイルやディレクトリを簡単に編集、コピー、ダウンロードできるツールです。FTP、SCP、SFTP、WebDAV、S3 などのファイル転送プロトコルを使って、ローカルコンピューターとルーターの間でファイルをやり取りできます。このガイドは Windows 向けです。

---

1. [こちら](https://winscp.net/eng/download.php){target="\_blank"} から WinSCP をダウンロードし、Windows にインストールします。

2. ルーターに接続した状態で WinSCP を起動します。

   ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}
   - ファイルプロトコル: `SCP` を選択します。
   - ホスト名: ルーターの IP アドレスを入力します。変更していない場合は `192.168.8.1` です。
   - ポート番号: `22`
   - ユーザー名とパスワード: ユーザー名に `root` を入力し、パスワードを入力します。

   入力後、`Login` ボタンをクリックします。

3. ログインすると、ルーター上のファイルを自由に操作できるようになります。

   ルーターからファイルやディレクトリを選択、表示、編集、転送できます。

   ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

   たとえば、ファイアウォール設定を編集したい場合は、`/etc/config` に移動し、`firewall` ファイルを見つけて右クリックし、**Edit** を選択します。

   ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

   これでファイル内容を編集できます。設定を壊さないよう注意してください。

   ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
