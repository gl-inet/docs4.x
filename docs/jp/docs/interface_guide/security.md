# セキュリティ

この機能はファームウェアv4.5で降で利用可能です。

ウェブ管理パネルの左側 -> システム -> セキュリティ

## 管理者パスワード

ここでウェブ管理パネルのログインパスワードを変更できます。

![admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/admin_password.jpg){class="glboxshadow"}

管理者パスワードの要件は以下の通りです。

- 最も小10文字、最大63文字。
- 文字（大文字と小文字を区別）、数字、記号 `` ! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~ `` が使用できます。
- 大文字、小文字、数字、記号のうち少なくとも2つが必要です。

## アクセス制御

アクセス制御は firmware v4.7で前ではローカルアクセス制御とも呼ばれ、ルーターの異なる管理インターフェースのアクセスを管理します。

デフォルトポートでのスキャンや侵入の試みを防ぎ、ポートの競合によるネットワーク問題を回避できます。

**注意**: ファームウェアでポート番号が変更された場合、管理パネルにアクセスするには正しいポート番号を入力する必要があります。ポート番号を忘れた場合は、ルーターをデフォルトのポート番号にリセットしてください。

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### 管理パネル

- **HTTPポート**: デフォルトは80で、ウェブ管理パネルへの暗号化されていないHTTPアクセスに使用されます。

- **HTTPSポート**: デフォルトは443で、ウェブ管理パネルへの安全なHTTPSアクセスに使用されます。

- **HTTPSを強制**: 有効にすると、ウェブ管理パネルへのアクセスは安全なHTTPS接続を使用することが強制されます。

- **から動ログアウト時間**: デフォルトで5分に設定されており、セキュリティのため、この時間後にアイドル状態の管理者セッションが自動的にログアウトされます。から動ログアウト時間は1分から3時間の間でカスタマイズできます。

### LuCI

- **HTTPポート**: デフォルトは8080で、LuCIインターフェースへの暗号化されていないHTTPアクセス用です。

- **HTTPSポート**: デフォルトは8443で、LuCIインターフェースへの安全なHTTPSアクセス用です。

- **HTTPSを強制**: 有効にすると、LuCIインターフェースへのアクセスは安全なHTTPS接続を使用することが強制されます。

### SSH

- **SSHを有効にする**: ルーターへのSSHアクセスが許可されているかどうかを制御します。デフォルトで有効になっています。

- **SSHポート**: デフォルトは22で、ルーターへのSSHアクセスに使用されるポートです。

### 禁止ポート {#prohibited-port}

予約ポート（またはブラウザ/ネットワークの規則で特定のサービスのために予約されているポート）と競合するポート番号を割り当てると、「このポートはブラウザによって禁止されています」というプロンプトが表示されます。

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "ブラウザによって禁止されているポート番号のリスト"

    | ポート | 説明                                      |
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
    | 427   | SLP (Apple Filing Protocolでも使用)     |
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

## リモートアクセス制御

リモートアクセスを有効にした後、特定の場所からのアクセスを許可するように設定できます。例えば、セキュリティをへ上させるために利便性を犠牲にして、オフicesからホームデバイスへのリモートアクセスのみを有効にできます。

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **WANからのPingを許可**: ネットワークに問題がある場合、WANポートからのPingを許可すると、ユーザーが適切に接続されているかどうかを確認したり、ネットワーク遅延やパケット損失を判断したりするのに役立ちます。

- **HTTPSリモートアクセス**: HTTPSプロトコルは主にウェブブラウザとウェブサーバー間の通信に使用され、安全なデータ転送を保証します。ユーザーがウェブブラウザを通じてサーバーをリモート管理したり、ウェブアプリケーションにアクセスしたりする必要がある場合、HTTPSプロトコルを使用することで、データ転送のセキュリティと信頼性を確保できます。

- **SSHリモートアクセス**: SSHプロトコルは主にリモートコンピュータやサーバーへの安全なアクセス管理とファイル転送操作に使用されます。ユーザーはコマンドラインやスクリプトを使用してサーバーにリモートログインし、システム管理、ファイル転送などの操作を行う必要があり、SSHプロトコルを使用して安全なトンネルを確立し、データ転送のセキュリティとプライバシーを確保できます。

- **特定のIPからのリモートアクセスを許可**: この機能は**WANからのPingを許可**、**HTTPSリモートアクセス**、**SSHリモートアクセス**と組み合わせて使用します。複数の指定IPアドレスを追加して、これらの指定IPアドレスを持つデバイスからルーターをリモート管理できます。

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## ルーターのオープンポート

ウェブやFTPなどのルーターのサービスでは、パブリックにアクセスできるようにするために、ルーター上で respective ポートが開かれている必要があります。

ポートを開くには、**追加**をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

**名称:** ユーザーが指定できるルールの名前。

**プロトコル:** 使用するプロトコル。TCP、UDP、またはTCPとUDPの両方を選択できます。

**ポート:** 開きたいポート番号。

**有効にする:** ルールの有効または無効を設定します。

---

まだご質問はありますか？ [コミュニティ・フォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}ください。
