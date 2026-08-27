# HTTPS経由でGL.iNetルーターとAdGuard Homeにアクセスする

HTTPSを使用してGL.iNetルーターとAdGuard Homeにアクセスしたい場合は、以下の手順に従ってください。

## 1. GL.iNetルーターで証明書とキーをアップデートする

最初に、SSL証明書を申請するか、から身署名SSL証明書を入手してください。

次に、GL.iNetルーターにSSH接続するか、WinSCPを使用してアップデートした証明書とキーをGL.iNetルーターにアップロードします。パスは次の通りです：

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. AdGuard Homeを有効にする

GL.iNetウェブ管理パネルにログイン -> **アプリケーション** -> **AdGuard Home**で、AdGuard Homeを有効にします。

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

次に、このページの上部にある**設定ページ**をクリックすると、AdGuard Home設定ページにリダイレクトされます。

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. 暗号化設定を編集する

AdGuard Home設定ページで、**設定** -> **暗号化設定**に移動します。

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

左上にある**暗号化を有効にする**チェックボックスをオンにし、HTTPSポートに3001を入力します。

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

アップデートした証明書とキーのパスを追加し、**保存**をクリックします。

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

すると、HTTPSで**192.168.8.1**または**192.168.8.1:3001**にアクセスできます。

---

まだ質問がありますか？ [コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}を訪問してください。
