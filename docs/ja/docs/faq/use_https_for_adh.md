# HTTPS経由でGL.iNetルーターとAdGuard Homeにアクセスする {#access-glinet-router-and-adguard-home-via-https}

HTTPSを使用してGL.iNetルーターとAdGuard Homeにアクセスしたい場合は、以下の手順に従ってください。

## 1. GL.iNetルーターの証明書とキーを更新する {#1-update-certificate-and-key-in-glinet-router}

まず、SSL証明書を申請するか、自己署名SSL証明書を使用してください。

次に、GL.iNetルーターにSSHで接続するか、WinSCPを使用して、更新した証明書とキーをGL.iNetルーターにアップロードします。パスは次のとおりです。

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. AdGuard Homeを有効にする {#2-enable-adguard-home}

GL.iNetのWeb管理パネルにログインし、APPLICATIONS -> AdGuard Home に移動して、AdGuard Homeを有効にします。

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

次に、このページの上部にある **Settings Page** をクリックすると、AdGuard Homeの設定ページに移動します。

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. 暗号化設定を編集する {#3-edit-encryption-settings}

AdGuard Homeの設定ページで、Settings -> Encryption settings に移動します。

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

左上にある Enable Encryption のチェックボックスをオンにし、HTTPSポートに3001を入力します。

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

更新した証明書とキーのパスを追加し、Save をクリックします。

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

これで、HTTPSで **192.168.8.1** または **192.168.8.1:3001** にアクセスできるようになります。

---

ご不明な点がある場合は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} をご利用ください。
