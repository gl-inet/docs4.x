# SMS Forwarding

Since version 4.1, forwarding SMS messages from the router to mobile phones and emails is available.

**Note**: This feature only works on GL.iNet 4G/5G models with original 4G LTE/5G NR module, not support with other modules or any other USB modules.

There are two methods to forward SMS, 

- Forward SMS to emails
- Forward SMS to phones

## Supported models

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-XE3000 (Puli AX)            | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE300 (Puli)                | √         |
| GL-E750 (Mudi)                 | √         |

## Setup

Here take the GL-XE300 (Puli) as an example.

On the left side of web Admin Panel -> INTERNET, Cellular sector. Click the envelope icon to go to SMS page, you will find the SMS Forwarding settings.

![sms setting](https://static.gl-inet.com/docs/en/4/tutorials/sms_forwarding/cellular_sms.png){class="glboxshadow"}

## SMS Forwarding to email

![sms forwarding email](https://static.gl-inet.com/docs/en/4/tutorials/sms_forwarding/sms_forwarding_email.png){class="glboxshadow"}

- **SMTP Server Address**, dropdown list has preset Server Address for Gmail, Outlook, iCloud and Yahoo. If you using other mail providers, please check out their document or contact the support.
- **Encryption Method**, has three options: none, SSL/TLS and STARTTLS.
- **Username**, the email address.
- **Password**, app-specific passwords or the password for login account. For Gmail, Outlook, iCloud and Yahoo, please check the guide below.
- **Subject**, the email subject.

??? "Gmail"

    For Gmail, you need to login your google account and create an **App Passwords**. Please check the official guide [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. You need to enable two-steps verification before create the App Passwords.

    Both 465 and 587 ports are useable.

??? "Outlook"

    For Outlook, you can use password directly without any setting, and it supports port 587. Please chck the official guide [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}

??? "iCloud"

    For iCloud, you need to create an app-specific passwords for login, and it supports port 587. Please refer to the official guide [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} and [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    For Yahoo, you need to set an app password for login, and it supports both port 465 and 587. Please refere to the official guide [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} and [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Note**: Each emailer may has a limit on SMTP, limiting the number of emails that can be sent per day. Please consult with your service provider.

You can add up to 10 email addreses.

## SMS Forwarding to phone

![sms forwarding phone](https://static.gl-inet.com/docs/en/4/tutorials/sms_forwarding/sms_forwarding_phone.png){class="glboxshadow"}

Toggle to enable it, choose the National code and input the phone number, finally, click the apply button.

You can add up to 10 cell phone numbers.

---

Related Articles

- [SMS](../interface_guide/sms.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
