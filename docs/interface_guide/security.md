# セキュリティ

この機能はv4.5から利用できます。

ウェブ管理画面の左側 -> システム -> セキュリティ

## 管理者パスワード

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.png){class="glboxshadow"}

管理画面にログインする際のパスワードを変更します。変更するには、現在のパスワードを入力する必要があります。

セキュリティ上の理由から、**弱いパスワードの防止**をオンにすることをお勧めします。

 **弱いパスワードの防止** がオンの場合、新しいパスワードの条件は以下の通り。

- 5文字以上63文字以内。
- 文字（大文字と小文字を区別）、数字、記号 `` ！@ # $ % ^ & * ( ) _ + - = , . > < | ? / [ ] { } : ; " ' ` ~ `` が使用できます。
- 大文字、小文字、数字、記号のうち少なくとも2つは必須。

## ローカル・アクセス・コントロール

ローカル・コントロール機能は、デフォルト・ポートでのスキャンや侵入の試みを防ぎ、ポートの競合によるネットワーク問題を回避することができます。

**注意**:  ファームウェアでポート番号が変更された場合、管理パネルに入るにはスマートフォンで正しいポート番号を入力する必要があります。ポート番号を忘れた場合は、ルーターをデフォルトのポート番号にリセットしてください。

![security_default_local_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_default_local_access_control.png){class="glboxshadow"}

**自動ログアウト時間**： ブラウザページを閉じるか休止状態にしてからログアウトするまでの間隔。

### 禁止ポート

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "ブラウザが禁止するポート番号のリストは以下の通り。:"

    | Port  | Description                              |
    | :-----| :--------------------------------------: |
    | 1     | tcpmux                                   |
    | 7     | echo                                     |
    | 9     | discard                                  |
    | 11    | systat                                   |
    | 13    | daytime                                  |
    | 15    | netstat                                  |
    | 17    | qotd                                     |
    | 19    | chargen                                  |
    | 20    | ftp data                                 |
    | 21    | ftp access                               |
    | 22    | ssh                                      |
    | 23    | telnet                                   |
    | 25    | smtp                                     |
    | 37    | time                                     |
    | 42    | name                                     |
    | 43    | nicname                                  |
    | 53    | domain                                   |
    | 69    | tftp                                     |
    | 77    | priv-rjs                                 |
    | 79    | finger                                   |
    | 87    | ttylink                                  |
    | 95    | supdup                                   |
    | 101   | hostriame                                |
    | 102   | iso-tsap                                 |
    | 103   | gppitnp                                  |
    | 104   | acr-nema                                 |
    | 109   | pop2                                     |
    | 110   | pop3                                     |
    | 111   | sunrpc                                   |
    | 113   | auth                                     |
    | 115   | sftp                                     |
    | 117   | uucp-path                                |
    | 119   | nntp                                     |
    | 123   | NTP                                      |
    | 135   | loc-srv /epmap                           |
    | 137   | netbios                                  |
    | 139   | netbios                                  |
    | 143   | imap2                                    |
    | 161   | snmp                                     |
    | 179   | BGP                                      |
    | 389   | ldap                                     |
    | 427   | SLP (Also used by Apple Filing Protocol) |
    | 465   | smtp+ssl                                 |
    | 512   | print / exec                             |
    | 513   | login                                    |
    | 514   | shell                                    |
    | 515   | printer                                  |
    | 526   | tempo                                    |
    | 530   | courier                                  |
    | 531   | chat                                     |
    | 532   | netnews                                  |
    | 540   | uucp                                     |
    | 548   | AFP (Apple Filing Protocol)              |
    | 554   | rtsp                                     |
    | 556   | remotefs                                 |
    | 563   | nntp+ssl                                 |
    | 587   | smtp (rfc6409)                           |
    | 601   | syslog-conn (rfc3195)                    |
    | 636   | ldap+ssl                                 |
    | 989   | ftps-data                                |
    | 990   | ftps                                     |
    | 993   | ldap+ssl                                 |
    | 995   | pop3+ssl                                 |
    | 1719  | h323gatestat                             |
    | 1720  | h323hostcall                             |
    | 1723  | pptp                                     |
    | 2049  | nfs                                      |
    | 3659  | apple-sasl / PasswordServer              |
    | 4045  | lockd                                    |
    | 5060  | sip                                      |
    | 5061  | sips                                     |
    | 6000  | X11                                      |
    | 6566  | sane-port                                |
    | 6665  | Alternate IRC [Apple addition]           |
    | 6666  | Alternate IRC [Apple addition]           |
    | 6667  | Standard IRC [Apple addition]            |
    | 6668  | Alternate IRC [Apple addition]           |
    | 6669  | Alternate IRC [Apple addition]           |
    | 6697  | IRC + TLS                                |
    | 10080 | Amanda                                   |

## リモート・アクセス・コントロール

リモートアクセスを有効にした後、特定の場所からのアクセスを許可するように設定することができます。例えば、オフィスから自宅のデバイスにのみリモートアクセスを許可し、利便性を犠牲にしてセキュリティを向上させることができます。

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **WANからのPingを許可する**: ネットワークに問題がある場合、WAN ポートからの Ping を許可すると、ユーザーまたはネットワーク管理者がルーターが適切に接続されているかどうかを確認したり、ネットワーク遅延やパケット損失を判断したりするのに役立ちます。

- **HTTPS リモート アクセス**: HTTPSプロトコルは主にウェブブラウザとウェブサーバ間の通信に使用され、安全なデータ伝送を保証します。そのため、ユーザーがウェブブラウザを通じてサーバーをリモート管理したり、ウェブアプリケーションにアクセスしたりする必要がある場合、HTTPSプロトコルを使用することで、データ伝送の安全性と信頼性を確保することができます。

- **SSHリモートアクセス**: SSHプロトコルは主にリモートコンピュータやサーバーに安全にアクセスしたり、管理したり、ファイル転送操作を実行するために使用されます。ユーザがシステム管理、ファイル転送、その他の操作のためにコマンドラインやスクリプトを使ってサーバにリモートログインする必要がある場合、セキュアなトンネルを確立してデータ転送のセキュリティとプライバシーを確保するためにSSHプロトコルを使用することができます。

- **特定のIPからのリモートアクセスを許可する**: この機能は、**HTTPSリモートアクセス**または**SSHリモートアクセス**と組み合わせて使用します。複数の指定IPアドレスを追加して、これらの指定IPアドレスを持つデバイスからルーターをリモート管理することができます。

![add_ip_address](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address.png){class="glboxshadow"}

![add_ip_address_list](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_list.png){class="glboxshadow"}


---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。