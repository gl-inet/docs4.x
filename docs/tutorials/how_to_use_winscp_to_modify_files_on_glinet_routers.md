# WinSCPを使用してGL.iNetルー器のファイルを変よりする方法

WinSCPは、ルー器のファイルやディレクトリを簡単に編集、コピー、ダウンロードできるツールです。FTP、SCP、SFTP、WebDAV、またはS3ファイル転送プロトコルを使用して、ローカルコンピュータとルー器の間でファイルをコピーできます。Windowsオペレーティングシステムに適用されます。

---

1. [これ里](https://winscp.net/eng/download.php){target="_blank"}からWinSCPをダウンロードしてWindowsにインストールします。

2. ルー器に接続し、WinSCPを実行します。

    ![WinSCP login](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * ファイルプロトコル：プロトコルとして`SCP`を選択してください。
    * ホスト名：ルー器のIPを入力します。ルー器のIPを変よりしていない場合は`192.168.8.1`である必要があります
    * ポート番号：`22`
    * ユーザー名とパスワード：ユーザー名として`root`を入力し、パスワードを入力します。

    次に`Login`ボタンをクリックします。

3. ログイン後、ルー器の完全なコントロールが表示されます。

    ルー器から/へファイル/ディレクトリを選択、表示、編集、または転送できます。

    ![WinSCP panel](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    例えば、ファイアウォール設定を変よりしたい場合は、/etc/configに移動し、ファイアウォールファイルを見つけ、右クリックして**Edit**を選択できます。

    ![WinSCP edit 1](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    これでファイルのコンテンツをからよりに編集できます。設定をめないよう注意してください。

    ![WinSCP edit 2](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

ご不明な時がございましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
