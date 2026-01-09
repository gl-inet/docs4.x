# SMS Forwarding

GL.iNet cellular routers support SMS forwarding, automatically pushing received messages to designated recipients.

**Note**: This feature only works on GL.iNet cellular routers with the original 4G LTE/5G NR module, and is not supported on other modules or any other USB modules.

There are two methods to forward SMS.

- Forward SMS to emails
- Forward SMS to phones

## Supported models

| Router Model                       | Support   |
| :--------------------------------- | :-------: |
| GL-X2000 (Spitz Plus)              | √         |
| GL-XE3000 (Puli AX)                | √         |
| GL-X3000 (Spitz AX)                | √         |
| GL-E750/GL-E750-V2 (Mudi/Mudi V2)  | √         |
| GL-X750 (Spitz)                    | √         |
| GL-XE300 (Puli)                    | √         |
| GL-X300B (Collie)                  | √         |

## Setup

Take the GL-XE3000 (Puli AX) as an example.

On the left side of web Admin Panel -> INTERNET -> Cellular section. Click the envelope icon in the upper right to enter SMS page, and you will find the SMS Forwarding settings.

![sms setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### Forward via Email

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: Preset server addresses for Gmail, Outlook, iCloud, and Yahoo are available in the dropdown list. For other mail providers, refer to their documentation or contact their support.

- **Encryption Method**: Three options are provided: none, SSL/TLS, and STARTTLS.
- **Username**: Enter the email address here.
- **Password**: Use an app-specific password or the login account password. For Gmail, Outlook, iCloud, and Yahoo, check the guide below.
- **Subject**: Set the email subject here.

??? "Gmail"

    For Gmail, you need to login your google account and create an **App Passwords**. Please check the official guide [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. You need to enable two-steps verification before create the App Passwords.

    Both 465 and 587 ports are useable.

??? "Outlook"

    For Outlook, you can use password directly without any setting, and it supports port 587. Please chck the official guide [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}

??? "iCloud"

    For iCloud, you need to create an app-specific passwords for login, and it supports port 587. Please refer to the official guide [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} and [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    For Yahoo, you need to set an app password for login, and it supports both port 465 and 587. Please refere to the official guide [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} and [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Note**: Each email sender may be subject to SMTP sending limits, e.g., a daily limit on the number of emails sent. Please consult with your service provider.

You can add up to 10 email addresses.

### Forward via SMS

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Choose the National code and input the phone number, and click Apply.

You can add up to 10 cell phone numbers.

---

Related Articles

- [SMS](../interface_guide/sms.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.