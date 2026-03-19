# SMS Forwarding

GL.iNet のセルラールーターは SMS Forwarding をサポートしており、受信したSMSメッセージを指定した宛先へ自動転送できます。

**Note**: この機能は、オリジナルの 4G LTE / 5G NR モジュールを搭載した GL.iNet のセルラールーターでのみ利用できます。他のモジュールやUSBモジュールではサポートされません。

## 対応モデル

??? "Supported Models" - GL-E5800 (Mudi 7) - GL-X2000 (Spitz Plus) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-E750 / E750V2 (Mudi) - GL-X750 / GL-X750V2 (Spitz) - GL-XE300 (Puli) - GL-X300B (Collie)

??? "Unsupported Models" - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-AX1800 (Flint) - GL-MT2500 / GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-SFT1200 (Opal) - GL-A1300 (Slate Plus) - GL-MT1300 (Beryl) - GL-AR750S (Slate) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus)

## 設定

ここでは GL-XE3000 (Puli AX) を例に説明します。

Web管理画面の左側で **INTERNET** -> **Cellular** に移動します。

右上の封筒アイコンをクリックして SMS ページを開くと、SMS Forwarding の設定項目が表示されます。

![sms setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### メールで転送する

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: ドロップダウンリストには Gmail、Outlook、iCloud、Yahoo のプリセットサーバーアドレスがあります。他のメールプロバイダーを使用する場合は、その公式ドキュメントを確認するか、サポートへ問い合わせてください。
- **Encryption Method**: `none`、`SSL/TLS`、`STARTTLS` の3種類があります。
- **Username**: メールアドレスを入力します。
- **Password**: アプリ専用パスワード、またはログイン用アカウントのパスワードを入力します。Gmail、Outlook、iCloud、Yahoo については以下の案内を参照してください。
- **Subject**: メールの件名を設定します。

??? "Gmail"

    Gmail を使用する場合は、Google アカウントへログインして **App Passwords** を作成する必要があります。公式ガイド [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"} を参照してください。App Passwords を作成する前に、2段階認証を有効にする必要があります。

    ポート 465 と 587 の両方を使用できます。

??? "Outlook"

    Outlook では特別な設定なしで通常のパスワードを使用でき、ポート 587 をサポートしています。公式ガイド [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"} を参照してください。

??? "iCloud"

    iCloud を使用する場合は、ログイン用に app-specific password を作成する必要があり、ポート 587 をサポートしています。公式ガイド [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} と [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"} を参照してください。

??? "Yahoo"

    Yahoo を使用する場合は、ログイン用に app password を設定する必要があり、ポート 465 と 587 の両方をサポートしています。公式ガイド [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} と [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"} を参照してください。

**Note**: 各メール送信元には SMTP の送信制限がある場合があります。たとえば、1日に送信できるメール数に上限があることがあります。詳細は利用中のサービスプロバイダーへ確認してください。

メールアドレスは最大 10 件まで追加できます。

### SMSで転送する

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

国番号を選択し、電話番号を入力して **Apply** をクリックします。

携帯電話番号は最大 10 件まで追加できます。

---

関連記事

- [SMS](../interface_guide/sms.md)

---

ご不明な点がある場合は、[Community Forum](https://forum.gl-inet.com){target="\_blank"} をご利用いただくか、[Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} からお問い合わせください。
