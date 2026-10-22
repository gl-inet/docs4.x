# ブラウザからの警告：接続がプライベートではありません {#warning-from-your-browser-your-connection-is-not-private}

GL.iNetルーターを初めて設定する際に、「この接続ではプライバシーが保護されません」というブラウザの警告が表示される場合があります。

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

これは、信頼されたSSL/TLS証明書を持たないWebサイトを検出したときにブラウザが表示する標準的なセキュリティ警告です。

ブラウザは通常、第三者の認証局（CA）が発行した証明書を信頼するように設計されています。しかし、GL.iNetルーターはCAが発行したものではない自己署名証明書を使用しています。そのため、ブラウザは安全ではないと判断し、この警告を表示します。

## 192.168.8.1へのアクセスは安全ですか？ {#is-it-safe-to-browse-19216881}

GL.iNetはお客様のネットワークセキュリティを最優先に考えています。初期設定はすべてローカルで行われるため、インターネット接続は必要ありません。

設定中にGL.iNetルーターのWi-Fiに接続すると、**「接続済み、インターネットなし」**（Connected, No internet）と表示される場合があります。設定中のルーターは独立したローカルネットワークで動作しているため、これは想定どおりの動作です。

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

同様に、IPアドレス**192.168.8.1**はルーター自体に割り当てられたプライベートなローカルIPアドレスです。これは公開Webサイトではなく、デバイスのローカル管理パネルにアクセスするために使用されます。

接続は完全にローカルで、設定中にインターネットアクセスは不要なため、**プライバシーが漏えいするリスクはありません**。これにより、安全で隔離された環境でルーターを設定できます。

## なぜ警告が表示されるのですか？ {#why-do-i-still-get-a-warning}

ブラウザは通常、あらかじめ設定されたセットアップ用IPアドレスと一般的なWebサイトを区別しません。すべてのIPアドレスをWebサイトとして扱い、HTTPS接続がSSL/TLS証明書で保護されていることを前提とします。

GL.iNetルーターはSSL/TLS証明書を使用していますが、これは自己署名証明書であり、第三者の認証局（CA）が発行したものではありません。このIPへのアクセスは（プライベートなローカルネットワーク上であるため）安全ですが、ブラウザでは「安全ではない」と判断されるため、警告が表示されます。

## この警告が表示された場合はどうすればよいですか？ {#what-can-i-do-with-this-warning}

**詳細設定**（Advanced）をクリックし、**192.168.8.1 にアクセスする（安全ではありません）**（Continue to 192.168.8.1）をクリックしてください。

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Web管理パネルに移動します。

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## ルーターにSSL証明書を追加できますか？ {#can-i-add-an-ssl-certificate-in-the-router}

はい、GL.iNetルーターにSSL証明書を追加できます。

[SSL証明書を追加する方法](../faq/use_https_for_adh.md)

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
