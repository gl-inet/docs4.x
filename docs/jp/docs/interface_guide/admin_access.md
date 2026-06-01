# 管理者アクセス

> このページは firmware v4.9 で追加されました。

Web Admin Panel の左側で、**SECURITY** -> **Admin Access** に移動します。

このページでは、不正アクセスからネットワークとルーターを保護するための各種セキュリティ設定を構成できます。

## アクセス制御

Access Control は、firmware v4.7 以前では Local Access Control とも呼ばれ、ルーターの各種管理インターフェースへのアクセスを管理します。

これにより、デフォルトポートへのスキャンや侵入の試みを防ぎ、ポート競合によるネットワーク問題を回避できます。

**注意**: ファームウェアでポート番号を変更した場合、管理パネルへアクセスするには正しいポート番号を入力する必要があります。ポート番号を忘れた場合は、ルーターをデフォルトのポート番号に戻してください。

![security_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/access_control_4.8.png){class="glboxshadow"}

### 管理パネル

- **HTTP Port**: デフォルトは 80 で、Web 管理パネルへの暗号化されていない HTTP アクセスに使用します。

- **HTTPS Port**: デフォルトは 443 で、Web 管理パネルへの安全な HTTPS アクセスに使用します。

- **Force HTTPS**: 有効にすると、Web 管理パネルへのアクセスは必ず安全な HTTPS 接続になります。

- **Auto-Logout Time**: デフォルトは 5 分で、セキュリティのため、この時間アイドル状態が続くと管理者セッションが自動的にログアウトします。1 分〜3 時間の範囲で変更できます。

### LuCI

> 注意: LuCI のアクセス制御を設定する前に、**Advanced Settings** で LuCI をインストールしてください。

- **HTTP Port**: デフォルトは 8080 で、LuCI インターフェースへの暗号化されていない HTTP アクセスに使用します。

- **HTTPS Port**: デフォルトは 8443 で、LuCI インターフェースへの安全な HTTPS アクセスに使用します。

- **Force HTTPS**: 有効にすると、LuCI インターフェースへのアクセスは必ず安全な HTTPS 接続になります。

### SSH

- **Enable SSH**: ルーターへの SSH アクセスを許可するかどうかを制御します。デフォルトで有効です。

- **SSH Port**: デフォルトは 22 で、ルーターへの SSH アクセスに使用するポートです。

### Prohibited Port {#prohibited-port}

予約済みポート、またはブラウザやネットワーク慣例で特定サービス向けに予約されているポートと競合する番号を割り当てると、"This port is forbidden by the browser" というメッセージが表示されます。

![http_https_port_forbidden](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/http_https_port_forbidden.png){class="glboxshadow"}

??? "ブラウザーで使用が禁止されているポート番号一覧"

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

## リモートアクセス制御

リモートアクセスを有効にすると、アクセスを許可する接続元を限定できます。たとえば、利便性と引き換えにセキュリティを高めるため、オフィスからのみ自宅のデバイスへのリモートアクセスを許可する、といった設定が可能です。

![security_remote_access_control](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/security_remote_access_control.png){class="glboxshadow"}

- **Allow Ping from WAN**: ネットワークに問題がある場合、WAN ポートからの Ping を許可すると、ユーザーやネットワーク管理者がルーターの接続状態を確認し、ネットワーク遅延やパケット損失を判断しやすくなります。

- **HTTPS Remote Access**: HTTPS プロトコルは主に Web ブラウザと Web サーバー間の通信に使われ、安全なデータ転送を提供します。Web ブラウザ経由でサーバーをリモート管理したり、Web アプリケーションへアクセスしたりする場合に、データ転送の安全性と信頼性を確保できます。

- **SSH Remote Access**: SSH プロトコルは主に、リモートコンピューターやサーバーへの安全なアクセスと管理、およびファイル転送に使われます。コマンドラインやスクリプトでサーバーにリモートログインし、システム管理やファイル転送を行う場合、SSH を使って安全なトンネルを確立し、データ転送の安全性とプライバシーを確保できます。

- **Allow Remote Access from Specific IPs**: この機能は **Allow Ping from WAN**、**HTTPS Remote Access**、**SSH Remote Access** と組み合わせて使用します。複数の指定 IP アドレスを追加して、それらの IP を持つデバイスからルーターをリモート管理できます。

![add_ip_address_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_1.png){class="glboxshadow"}

![add_ip_address_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_ip_address_2.png){class="glboxshadow"}

---

## ルーターで開いているポート

Web や FTP などのルーターサービスをインターネット上から利用可能にするには、それぞれのポートをルーター上で開放する必要があります。

ポートを開くには、**Add** をクリックします。

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/open_ports_on_router.png){class="glboxshadow"}

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/security/add_new_open_port.png){class="glboxshadow"}

- **Protocol:** `TCP/UDP`、`TCP`、`UDP` からプロトコルを選択します。

- **Port:** 開放したいポート番号を入力します。

- **Description:** このルールの説明を追加します（任意）。

- **Enable:** このルールを有効または無効にします。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。