# SSH でルーターにログインする

Secure Shell（SSH）は、安全でないネットワーク上でもネットワークサービスを安全に操作するための暗号化ネットワークプロトコルです。最もよく知られている用途は、ユーザーがコンピューターシステムへリモートログインすることです。場合によっては、サーバーへ SSH 接続するための基本的なツールが必要になります。このガイドでは、GL.iNet ルーターに SSH でログインする方法を説明します。

---

## Windows ユーザーの場合

Windows でルーターのターミナルにアクセスする方法として、Windows Cmd、PowerShell、Bitvise、PuTTY があります。

### Windows Cmd を使用する

1. コマンドプロンプトを開く

   **Win** + **R**（Windowsキー + Rキー）を押して実行ボックスを開き、**cmd**と入力してEnterを押します。

   ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

   黒いコマンドプロンプトウィンドウがポップアップします。

   ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. ルーターにログインする

   コマンドプロンプトウィンドウで、`ssh root@192.168.8.1`と入力し、Enterを押します。

   ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

   **注意**: 192.168.8.1 はルーターのデフォルト IP アドレスです。以前に変更している場合は、変更後の IP アドレスを使用してください。

   次に、ルーターの管理パスワードを入力し、Enterを押します。**セキュリティのため、パスワードは画面に表示されません**。

   ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

   パスワードが正しければ、ルーターに正常にログインできます。

   ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "トラブルシューティング"

    1. **エラー: 接続がタイムアウトしました**

        デバイス（ノート PC など）がルーターに接続されていることを確認してください。ルーターの Wi-Fi または LAN ポートへ再接続して、もう一度試してください。

    2. **エラー: 権限がありません**

        正しい管理者パスワードを入力していることを確認してください。パスワードを忘れた場合は、RESET ボタンを 10 秒間押してルーターをリセットしてください。

### PowerShell を使用する

1. Windows PowerShell を開く

   タスクバーの検索アイコンをクリックし、**PowerShell**を入力し、**Windows PowerShell**を選択して**管理者として実行**します。

   ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. ルーターにログインする

   PowerShellウィンドウで、`ssh root@192.168.8.1`と入力し、Enterを押します。

   ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

   **注意**: 192.168.8.1 はルーターのデフォルト IP アドレスです。以前に変更している場合は、変更後の IP アドレスを使用してください。

   接続の確認を求められたら、`yes` と入力して Enter を押します。

   ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

   ルーターの管理パスワードの入力を求められます。正しい管理パスワードを入力し、Enterを押します。**セキュリティのため、パスワードは画面に表示されません**。

   ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

   これで、ルーターのターミナルに正常にログインできます。

   ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "トラブルシューティング"

    1. **警告: リモートホスト識別情報が変更されました！** / **ホスト鍵の検証に失敗しました**

        これは、ルーターのホストキーが変更された場合（例: 工場出荷時リセット後やファームウェア更新後）、または以前に別のルーターへ接続していてホストキー検証が失敗した場合に発生します。

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        修正するには、ファイルエクスプローラーを開き、`C:\Users\Administrator\.ssh` に移動して **known_hosts** という名前のファイルを探します。

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        known_hostsファイルをダブルクリックして、メモ帳で開きます。

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        ルーターの IP アドレス（例: 192.168.8.1）に関連するエントリを削除し、ファイルを保存します。その後、ファイルエクスプローラーを閉じます。

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        PowerShell に戻り、`ssh root@192.168.8.1` を使ってルーターへ再接続します。接続確認を求められたら `yes` と入力して Enter を押し、その後ルーターのログインパスワードを入力してください。これで、ルーターのターミナルに正常にログインできます。

    2. **ルーターの SSH ポートを変更した場合はどうすればよいですか？**

        ルーターの SSH ポートを変更している場合は、ssh コマンドで `-p` パラメータを使ってポート番号を指定します。例:

        `ssh -p [新しいポート番号] [ユーザー名]@[ルーターIPアドレス]`

### Bitvise を使用する

Bitvise 経由でルーターにログインするには、以下の動画をご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### PuTTY を使用する

1. PuTTY をダウンロードする

   [こちら](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"} から最新の PuTTY をダウンロードしてください。

2. PuTTY をインストールする

   ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

   ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

   ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

   ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. PuTTY を起動する

   スタートメニューから**PuTTY**をクリックします。

   ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

   以下の設定ウィンドウが表示されます。

   ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

   Host Name（または IP address）に `192.168.8.1` を入力し、Port はデフォルトの `22` のままにして、Connection type として `SSH` を選択します。

   Saved Sessions に `Your Session` を入力し、`Save` をクリックします。

   その後、下部の `Open` をクリックします。

   ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

   以下のようなセキュリティアラートが表示されたら、`Yes` をクリックします。

   ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

   login as: `root`

   次に管理者パスワードを入力します。**セキュリティ上、パスワードは画面に表示されません**。

   ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

   上の画面が表示されれば、ルーターへの SSH ログインは成功です。

---

## Linux / Mac ユーザーの場合

Linux と Mac OS での手順は概ね同じです。以下では Ubuntu を例に説明します。

### Ubuntu を使用する

1. ターミナルを起動します。

   Ubuntuを実行し、ターミナルアイコンをダブルクリックしてターミナルを起動します。

   ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. ルーターにログインします。

   SSHログインコマンドを入力します：`ssh root@192.168.8.1`

   ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

   接続の確認を求められたら、`yes` と入力して Enter を押します。

   ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

   次にルーターの管理者パスワードを入力します。**セキュリティ上、パスワードは画面に表示されません**。

   ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

   上の画面が表示されれば、ルーターへのログインは成功です。

??? "トラブルシューティング"

    1. **警告: リモートホスト識別情報が変更されました！** / **ホスト鍵の検証に失敗しました**

        これは、ルーターのホストキーが変更された場合（例: 工場出荷時リセット後やファームウェア更新後）、または以前に別のルーターへ接続していてホストキー検証が失敗した場合に発生します。

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        この問題が発生した場合は、上記の赤い枠内に表示されているコマンドを実行してください。ターミナルに表示されているコマンドをそのままコピーすることを推奨します。

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        もう一度接続を試みます。

    2. **10.0.0.1ポート22でネゴシエーションできません: 一致するホスト鍵タイプが見つかりません。提供されたもの: ssh-rsa**

        接続時にこのエラーが表示されることがあります。これは、OpenSSH パッケージの仕様変更（バージョン 8.8 以降）によるものです。解決するには、テキストエディタ（Nano や Vim など）で **~/.ssh/config** ファイルを開き、以下の行を追加します:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        デフォルト以外の IP アドレスを使っている場合は、host の値を実際の IP に変更してください。

        この問題の詳細については、[こちら](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"} を参照してください。

---

まだご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="\_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="\_blank"} をご利用ください。
