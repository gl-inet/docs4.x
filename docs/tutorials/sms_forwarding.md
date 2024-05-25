# SMS転送

バージョン4.1以降、ルーターから携帯電話やメールにSMSメッセージを転送する機能が利用可能です。

**注意**：この機能は、オリジナルの4G LTE/5G NRモジュールを搭載したGL.iNetの4G/5Gモデルでのみ動作し、他のモジュールやUSBモジュールではサポートされていません。

SMSを転送する方法は2つあります：

- メールへのSMS転送
- 携帯電話へのSMS転送

## 対応モデル

| ルーターモデル                | サポート |
| :----------------------------- | :------: |
| GL-XE3000 (Puli AX)            | √        |
| GL-X3000 (Spitz AX)            | √        |
| GL-XE300 (Puli)                | √        |
| GL-E750 (Mudi)                 | √        |

## 設定

ここではGL-XE300 (Puli)を例にとります。

Web管理パネルの左側 -> インターネット、セルラーセクター。封筒アイコンをクリックしてSMSページに移動すると、SMS転送設定が見つかります。

![sms setting](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/cellular_sms.png){class="glboxshadow"}

## メールへのSMS転送

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forwarding_email.png){class="glboxshadow"}

- **SMTPサーバーアドレス**、ドロップダウンリストにはGmail、Outlook、iCloud、Yahooのプリセットサーバーアドレスが含まれています。他のメールプロバイダーを使用している場合は、そのドキュメントを確認するかサポートに連絡してください。
- **暗号化方法**、オプションは3つあります：なし、SSL/TLS、STARTTLS。
- **ユーザー名**、メールアドレス。
- **パスワード**、アプリ固有のパスワードまたはログインアカウントのパスワード。Gmail、Outlook、iCloud、Yahooについては、以下のガイドを確認してください。
- **件名**、メールの件名。

??? "Gmail"

    Gmailの場合、Googleアカウントにログインして**アプリパスワード**を作成する必要があります。公式ガイド[アプリパスワードでサインイン](https://support.google.com/accounts/answer/185833?hl=ja){target="_blank"}を確認してください。アプリパスワードを作成する前に、2段階認証を有効にする必要があります。

    465と587の両方のポートが使用可能です。

??? "Outlook"

    Outlookの場合、特別な設定なしに直接パスワードを使用できます。ポート587をサポートしています。公式ガイド[Outlook.comのPOP、IMAP、およびSMTP設定](https://support.microsoft.com/ja-jp/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}を確認してください。

??? "iCloud"

    iCloudを使用する場合、ログインにはアプリケーション固有のパスワードを作成する必要があり、ポート587をサポートしています。公式ガイドを参照してください：[他のメールクライアントアプリ用のiCloudメールサーバー設定](https://support.apple.com/en-hk/HT202304){target="_blank"}および[アプリケーション固有のパスワードの生成](https://support.apple.com/en-gb/HT204397){target="_blank"}。

??? "Yahoo"

    Yahooの場合、ログインにアプリパスワードを設定する必要があります。ポート465と587の両方をサポートしています。公式ガイド[YahooメールのPOPアクセス設定と手順](https://help.yahoo.com/kb/SLN4724.html){target="_blank"}および[サードパーティのアプリパスワードの生成と管理](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}を参照してください。

**注意**：メールサービスによっては、SMTPで送信できるメールの数に1日あたりの制限があります。サービスプロバイダーに相談してください。

最大10件のメールアドレスを追加できます。

## 携帯電話へのSMS転送

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forwarding_phone.png){class="glboxshadow"}

トグルをオンにして、国番号を選択し、電話番号を入力し、最後に適用ボタンをクリックします。

最大10件の携帯電話番号を追加できます。

---

関連する記事

- [SMS](../interface_guide/sms.md)

---

まだ質問がありますか？私たちの[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}をご覧ください。