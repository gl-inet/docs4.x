# SMS-Weiterleitung

GL.iNet-Mobilfunkrouter unterstützen die SMS-Weiterleitung und leiten eingehende Nachrichten automatisch an festgelegte Empfänger weiter.

**Hinweis**: Diese Funktion arbeitet nur auf GL.iNet-Mobilfunkroutern mit dem originalen 4G-LTE-/5G-NR-Modul und wird bei anderen Modulen oder beliebigen USB-Modulen nicht unterstützt.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Nicht unterstützte Modelle"
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)

## Einrichtung

Nehmen wir den GL-XE3000 (Puli AX) als Beispiel.

Gehen Sie auf der linken Seite des Web-Admin-Panels zum Bereich **INTERNET** -> **Cellular**.

Klicken Sie oben rechts auf das Umschlag-Symbol, um die SMS-Seite zu öffnen. Dort finden Sie die Einstellungen für SMS Forwarding.

![SMS-Einstellung](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### Über E-Mail weiterleiten

![SMS-Weiterleitung per E-Mail](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: Voreingestellte Serveradressen für Gmail, Outlook, iCloud und Yahoo sind in der Dropdown-Liste verfügbar. Informationen zu anderen E-Mail-Anbietern finden Sie in deren Dokumentation oder beim jeweiligen Support.

- **Encryption Method**: Es stehen drei Optionen zur Verfügung: none, SSL/TLS und STARTTLS.
- **Username**: Geben Sie hier die E-Mail-Adresse ein.
- **Password**: Verwenden Sie ein App-spezifisches Passwort oder das Passwort des Anmeldekontos. Für Gmail, Outlook, iCloud und Yahoo beachten Sie die Hinweise unten.
- **Subject**: Legen Sie hier den Betreff der E-Mail fest.

??? "Gmail"

    Bei Gmail müssen Sie sich in Ihrem Google-Konto anmelden und **App Passwords** erstellen. Bitte beachten Sie die offizielle Anleitung [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Bevor Sie App Passwords erstellen können, müssen Sie die Bestätigung in zwei Schritten aktivieren.

    Sowohl Port 465 als auch Port 587 können verwendet werden.

??? "Outlook"

    Bei Outlook können Sie das Passwort direkt ohne zusätzliche Einstellungen verwenden. Unterstützt wird Port 587. Bitte beachten Sie die offizielle Anleitung [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}

??? "iCloud"

    Bei iCloud müssen Sie für die Anmeldung ein App-spezifisches Passwort erstellen. Unterstützt wird Port 587. Bitte beachten Sie die offiziellen Anleitungen [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} und [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Bei Yahoo müssen Sie für die Anmeldung ein App-Passwort festlegen. Unterstützt werden sowohl Port 465 als auch Port 587. Bitte beachten Sie die offiziellen Anleitungen [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} und [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Hinweis**: Für jeden E-Mail-Absender können SMTP-Sendelimits gelten, zum Beispiel eine tägliche Begrenzung der Anzahl versendeter E-Mails. Bitte erkundigen Sie sich bei Ihrem Dienstanbieter.

Sie können bis zu 10 E-Mail-Adressen hinzufügen.

### Per SMS weiterleiten

![SMS-Weiterleitung per Telefon](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Wählen Sie die Landesvorwahl aus, geben Sie die Telefonnummer ein und klicken Sie auf **Apply**.

Sie können bis zu 10 Mobiltelefonnummern hinzufügen.

---

Verwandte Artikel

- [SMS](../interface_guide/sms.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
