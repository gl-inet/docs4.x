# SSHでルーターにログインする

Secure Shell（SSH）は、安全でないネットワーク上でネットワークサービスを安全に操作するための暗号化されたネットワークプロトコルです。最もも有名なアプリケーションの例は、ユーザーがコンピュータシステムにリモートログインすることです。場合によっては、SSHでサーバーに接続するための基本のなツールが必要です。このガイドでは、GL.iNetルー器にSSHログインする方法について説明します。

---

## Windowsユーザーの場合

Windowsでルー器のターミナルにアクセスする方法には、Windows Cmd、PowerShell、Bitvise、またはPuTTYがあります。

### Windows Cmdを使用

1. コマンドプロンプトを開く

    **Win** + **R**（Windowsキー + Rキー）を押して実行ボックスを開き、**cmd**と入力してEnterを押します。

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    黒いコマンドプロンプトウィンドウがポップアップします。

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. ルーターにログインする

    コマンドプロンプトウィンドウで、`ssh root@192.168.8.1`と入力し、Enterを押します。

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **注意**: 192.168.8.1はルー器のデフォルトIPアドレスです。前にに変更した場合は、カスタムIPを使用してください。

    次に、ルーターの管理パスワードを入力し、Enterを押します。**セキュリティのため、パスワードは画面に表示されません**。

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    パスワードが正しければ、ルーターに正常にログインできます。

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "トラブルシューティング"

    1. **エラー: 接続がタイムアウトしました**
    
        デバイス（ノートパソコンなど）がルー器に接続されていることを確認してください。ルー器のWi-FiまたはLANポートに再接続して再試行してください。

    2. **エラー: 権限がありません**

        正しい管理パスワードを入力していることを確認してください。パスワードを忘れた場合は、RESETボタンを10秒间押してルー器官翠复位してください。

### PowerShellを使用

1. Windows PowerShellを開く

    タスクバーの検索アイコンをクリックし、**PowerShell**を入力し、**Windows PowerShell**を選択して**管理者として実行**します。

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. ルーターにログインする

    PowerShellウィンドウで、`ssh root@192.168.8.1`と入力し、Enterを押します。

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **注意**: 192.168.8.1はルー器のデフォルトIPアドレスです。前にに変更した場合は、カスタムIPを使用してください。

    システムが接続を確認する求められます。`yes`と入力し、Enterを押します。

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    ルーターの管理パスワードの入力を求められます。正しい管理パスワードを入力し、Enterを押します。**セキュリティのため、パスワードは画面に表示されません**。
    
    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}
    
    すると、ルー器官のターミナルに正常にログインできます。

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "トラブルシューティング"

    1. **警告: リモートホスト識別情報が変更されました！** / **ホスト鍵の検証に失敗しました**

        これは、ルー器のセキュリティ键が変更された場合（例：出厂复位またはファームウェアアップデート後）、またはで前別のルー器に接続したことがあり、ホスト键の検証が失敗した場合に発生します。

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        修正するには、ファイルエクスプローラーを開き、`C:\Users\Administrator\.ssh`に移動し、**known_hosts**という名前のファイルを見つけます。

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        known_hostsファイルをダブルクリックして、メモ帳で開きます。

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        ルー器IPアドレス（例：192.168.8.1）に関連するエントリを削除し、ファイルを保存します。ファイルエクスプローラーを終たします。

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        PowerShellに戻り、コマンド`ssh root@192.168.8.1`を使用してルー器官に再接続します。接続を確認する求められます。`yes`と入力してEnterを押し、その後ルー器官のログインパスワードを入力します。これで、ルー器官のターミナルに正常にログインできます。

    2. **ルー器官のSSHポートを変更した場合はどうすればよいですか？**
    
        ルー器官のSSHポートを変更した場合は、sshコマンドで"-p"パラメータを使用してポートを指定します。例：
        
        ``ssh -p [新しいポート番号] [ユーザー名]@[ルー器官IPアドレス]``

### Bitviseを使用

Bitvise経由でルー器官にログインするには、この動画を見てください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### PuTTYを使用

1. PuTTYをダウンロード

    [ここ](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}から最も新のPuTTYバージョンをダウンロードしてください。

2. PuTTYをインストール

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. PuTTYを起動

    スタートメニューから**PuTTY**をクリックします。

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    以下の設定ウィンドウが表示されます。

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    ホスト名（またはIPアドレス）`192.168.8.1`を入力しポートはデフォルト`22`のままにし、接続タイプとして`SSH`を選択します。

    保存されたセッションに`Your Session`を入力し、コンテンツを`Save`します。

    その後底部クリック`Open`。

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    以下のようなセキュリティアラートがポップアップします。`Yes`をクリックします。

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    その後入力あなたの管理者パスワード。**安全のため，パスワード不ことになる表示に画面上**。

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    上記の画像が表示された場合、ルー器官にSSHログインできたことを意味します。

---

## Linux / Macユーザーの場合

LinuxとMac OSの手順は概ね同じです。以下ではUbuntuを例として使用します。

### Ubuntuを使用

1. ターミナルを起動します。

    Ubuntuを実行し、ターミナルアイコンをダブルクリックしてターミナルを起動します。
    
    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. ルーターにログインします。

    SSHログインコマンドを入力します：`ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    システムが接続を確認する求められます。"yes"と入力してEnterを押します。

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    その後入力あなたのルー器管理者パスワード。**安全のため，パスワード不ことになる表示に画面上**。

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    上記の画像が表示された場合、ルー器官にログインできたことを意味します。

??? "トラブルシューティング"

    1. **警告: リモートホスト識別情報が変更されました！** / **ホスト鍵の検証に失敗しました**

        これは、ルー器官のセキュリティ键が変更された場合（例：出厂复位またはファームウェアアップデート後）、またはで前別のルー器に接続したことがあり、ホスト键の検証が失敗した場合に発生します。

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        このが発生した場合は、上記の赤いボックス内のコマンドを実行してください。ターミナルに表示されている正確なコマンドをコピーしてください。

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        もう一度接続を試みます。

    2. **10.0.0.1ポート22でネゴシエーションできません: 一致するホスト鍵タイプが見つかりません。提供されたもの: ssh-rsa**
    
        接続時にこのエラーが発生する場合があります。このエラーは、Opensshパッケージがバージョン8.8から変更されたためです。解決これ个問題するには、テキストエディタ（例：NanoまたはVim）を使用して**~/.ssh/config**ファイルを開き、以下の行を追加します：

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        デフォルトでない場合は、ホストIPを変更してください。

        この問題の詳細については、[ここ](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}を参照してください。

---

まだ質問がありますか？[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご覧ください。
