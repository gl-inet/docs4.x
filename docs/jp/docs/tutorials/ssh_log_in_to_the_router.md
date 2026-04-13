# ルーターへSSHログインする

Secure Shell（SSH）は、安全でないネットワーク上でもネットワークサービスを安全に利用するための暗号化ネットワークプロトコルです。もっともよく知られている用途は、ユーザーがコンピューターシステムへリモートログインすることです。サーバーへSSH接続するための基本的なツールが必要になることがあります。このガイドでは、GL.iNetルーターへSSHログインする方法を紹介します。

---

## Windowsユーザー向け

Windows では、Windows Cmd、PowerShell、Bitvise、PuTTY などの方法でルーターのターミナルへアクセスできます。

### Windows Cmdを使う

1. Command Prompt を開く

    **Win** + **R**（Windowsキー + Rキー）を押して「ファイル名を指定して実行」を開きます。**cmd** と入力し、Enter を押します。

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    黒いコマンドプロンプトウィンドウが表示されます。

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. ルーターにログインする

    コマンドプロンプトで `ssh root@192.168.8.1` と入力し、Enter を押します。

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Note**: `192.168.8.1` はルーターのデフォルトIPアドレスです。以前に変更している場合は、そのカスタムIPを使用してください。

    次に、ルーターの管理者パスワードを入力して Enter を押します。**セキュリティのため、パスワードは画面に表示されません**。

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    パスワードが正しければ、ルーターへのログインに成功します。

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "トラブルシューティング"

    1. **Error: Connection timed out**

        ノートPCなどのデバイスがルーターに接続されていることを確認してください。ルーターのWi-FiまたはLANポートに再接続して、再試行してください。

    2. **Error: Permission denied**

        正しい管理者パスワードを入力していることを確認してください。パスワードを忘れた場合は、RESET ボタンを10秒間押してルーターをリセットしてください。

### PowerShellを使う

1. Windows PowerShell を開く

    タスクバーの検索アイコンをクリックし、**PowerShell** と入力します。**Windows PowerShell** を選択し、**管理者として実行**します。

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. ルーターにログインする

    PowerShellウィンドウで `ssh root@192.168.8.1` と入力し、Enter を押します。

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Note**: `192.168.8.1` はルーターのデフォルトIPアドレスです。以前に変更している場合は、そのカスタムIPを使用してください。

    接続確認のプロンプトが表示されたら、`yes` と入力して Enter を押します。

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    ルーターの管理者パスワード入力を求められます。正しい管理者パスワードを入力して Enter を押してください。**セキュリティのため、パスワードは画面に表示されません**。

    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

    これでルーターのターミナルへのログインに成功します。

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "トラブルシューティング"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        これは、ルーターのセキュリティキーが変更された場合（工場出荷時リセットやファームウェア更新後など）や、以前に別のルーターへ接続していたためホストキー検証に失敗した場合に発生します。

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        解決するには、File Explorer を開き、`C:\Users\Administrator\.ssh` に移動して **known_hosts** という名前のファイルを探してください。

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        known_hosts ファイルをダブルクリックし、Notepad で開きます。

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        ルーターのIPアドレス（例: 192.168.8.1）に関連するエントリーを削除し、ファイルを保存します。その後 File Explorer を閉じます。

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        PowerShell に戻り、`ssh root@192.168.8.1` で再接続します。接続確認を求められたら `yes` と入力して Enter を押し、その後ルーターのログインパスワードを入力します。これでルーターのターミナルへ正常にログインできます。

    2. **ルーターのSSHポートを変更した場合はどうすればよいですか？**

        ルーターのSSHポートを変更している場合は、sshコマンドで "-p" パラメーターを使ってポートを指定してください。例:

        ``ssh -p [new port number] [username]@[router IP address]``

### Bitviseを使う

Bitvise経由でルーターにログインするには、この動画を参照してください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### PuTTYを使う

1. PuTTYをダウンロードする

    最新版の PuTTY を[こちら](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="_blank"}からダウンロードします。

2. PuTTYをインストールする

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. PuTTYを起動する

    Start Menu から **PuTTY** をクリックします。

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    以下の Configuration Window が表示されます。

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Host Name (or IP address) に `192.168.8.1` を入力し、Port はデフォルトの `22` のまま、connection type は `SSH` を選択します。

    saved sessions に `Your Session` と入力し、内容を `Save` します。

    その後、下部の `Open` をクリックします。

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    以下のようなセキュリティ警告がポップアップ表示されたら、`Yes` をクリックします。

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    その後、管理者パスワードを入力します。**セキュリティのため、パスワードは画面に表示されません**。

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    上の画面のように表示されれば、ルーターへのSSHログインは成功です。

---

## Linux/Macユーザー向け

Linux と Mac OS での手順は概ね同じです。ここでは Ubuntu を例に説明します。

### Ubuntuを使う

1. Terminal を起動する

    Ubuntu を起動し、Terminal アイコンをダブルクリックして Terminal を起動します。

    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. ルーターにログインする

    SSHログインコマンドを入力します: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    接続確認のプロンプトが表示されたら、"yes" と入力して Enter を押します。

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    その後、ルーターの管理者パスワードを入力します。**セキュリティのため、パスワードは画面に表示されません**。

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    上の画面のように表示されれば、ルーターへのログインは成功です。

??? "トラブルシューティング"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        これは、ルーターのセキュリティキーが変更された場合（工場出荷時リセットやファームウェア更新後など）や、以前に別のルーターへ接続していたためホストキー検証に失敗した場合に発生します。

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        この場合は、上の赤枠内に表示されているコマンドを実行してください。端末に表示されたコマンドをそのままコピーすることをおすすめします。

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        その後、再度接続を試してください。

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        接続時にこのエラーが表示される場合があります。これは Openssh パッケージがバージョン 8.8 から変更されたことが原因です。解決するには、テキストエディター（Nano や Vim など）で **~/.ssh/config** ファイルを開き、以下の行を追加します。

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        デフォルト以外のIPを使っている場合は、host のIPアドレスを変更してください。

        この問題に関する詳細は、[こちら](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}を参照してください。

---

ご不明な点がありましたら、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧いただくか、[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
