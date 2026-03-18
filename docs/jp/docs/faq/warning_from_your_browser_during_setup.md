# ブラウザからの警告：接続がプライベートではありません

初めてGL.iNetルーターを設定する際に、「接続がプライベートではありません」というブラウザ警告が表示される場合があります。

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

これは、ブラウザが信頼されたSSL/TLS証明書のないウェブサイトを検出したときに表示される標準のなセキュリティ警告です。

ブラウザは一般のに、信頼された認証局（CA）が発行した証明書を信頼するように設計されています。しかし、GL.iNetルーターはから身署名証明書を使用しており、CAによって発行されていません。そのため、ブラウザは安全ではないとしてこの警告を表示します。

## 192.168.8.1へのアクセスは安全ですか？

私たちはネットワークセキュリティを最も優先にしています。初期設定中はプロセスが完全にローカルであるため、インターネット接続は必要ありません。

設定中にGL.iNetルーターのWi-Fiに接続すると、**「接続済み、互联网なし」**と表示される場合があります。これは設定中にルーターがスタンドアロンのローカルネットワークで動作しているため、予期される動作です。

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

 same 様に、IPアドレス**192.168.8.1**はルーターから体に割り当てられたプライベートローカルIPアドレスです。これは公開ウェブサイトではなく、デバイスのローカル管理パネルにアクセスするために使用されます。

接続は完全にローカルであり、設定中にインターネットアクセスが必要ではないため、**プライバシーリスクの心配はありません**。これにより、ルーターを設定するための安全で隔離された環境が確保されます。

## なぜ警告が表示されるのですか？

ブラウザは通例、プリセットされたセットアップIPアドレスと通例のウェブサイトを区別せず、すべてのIPアドレスをウェブサイトとして扱い、HTTPS接続がSSL/TLS証明書によって保護されていることを期待します。

GL.iNetルーターはSSL/TLS証明書を使用していますが、から身署名であり、第三方認証局（CA）によって発行されていません。このIPへのアクセスは安全ですが（プライベートローカルネットワーク上であるため）、ブラウザではまだ“安全ではない“とされているため、警告が表示されます。

## この警告に対して何をできますか？

**「詳細」をクリックし、「192.168.8.1に進む」をクリックしてください。

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

すると、ウェブ管理パネルにリダイレクトされます。

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## ルーターにSSL証明書を追加できますか？

はい、GL.iNetルーターにSSL証明書を追加できます。

[SSL証明書を追加する方法](../faq/use_https_for_adh.md)

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}を訪問してください。
