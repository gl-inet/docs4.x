# Sms doorsturen {#sms-forwarding}

GL.iNet-cellulaire routers ondersteunen het doorsturen van sms-berichten en sturen inkomende berichten automatisch naar opgegeven ontvangers.

**Opmerking**: deze functie werkt alleen op GL.iNet-cellulaire routers met de oorspronkelijke 4G LTE/5G NR-module. Andere modules en alle andere USB-modules worden niet ondersteund.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Niet-ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
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

## Snelle configuratie {#quick-setup}

We gebruiken de GL-XE3000 (Puli AX) als voorbeeld.

1. Volg eerst [deze handleiding](../interface_guide/internet_cellular.md) om je cellulaire router te configureren.

2. Meld je aan bij het webbeheerpaneel van de router en ga naar **INTERNET** -> **Cellular**. Klik rechtsboven op het enveloppictogram om de sms-pagina te openen. Hier vind je de instellingen voor het doorsturen van sms-berichten.

    ![sms setting](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms.png){class="glboxshadow"}

### Doorsturen via e-mail {#forward-via-email}

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: de vervolgkeuzelijst bevat vooraf ingestelde serveradressen voor Gmail, Outlook, iCloud en Yahoo. Een vooraf ingesteld serveradres garandeert geen compatibiliteit met de verificatievereisten van de provider. Raadpleeg voor andere e-mailproviders hun documentatie of neem contact op met hun ondersteuning.

- **Encryption Method**: er zijn drie opties: none, SSL/TLS en STARTTLS.
- **Username**: voer hier het e-mailadres in.
- **Password**: voer het SMTP-wachtwoord in dat je e-mailprovider vereist, bijvoorbeeld een app-specifiek wachtwoord. Raadpleeg hieronder de vereisten per provider.
- **Subject**: stel hier het onderwerp van de e-mail in.

??? "Gmail"

    Voor Gmail moet je je aanmelden bij je Google-account en een **App Password** maken. Raadpleeg de officiële handleiding [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Je moet verificatie in twee stappen inschakelen voordat je het App Password maakt.

    Zowel poort 465 als 587 kan worden gebruikt.

??? "Outlook.com"

    Outlook.com vereist OAuth2 (Modern Authentication) voor SMTP-verificatie. De SMTP-server is `smtp-mail.outlook.com` en gebruikt poort `587` met `STARTTLS`.

    Controleer voordat je een Outlook.com-account gebruikt om doorgestuurde sms-berichten te verzenden of de firmware van je router deze verificatiemethode ondersteunt.

    Raadpleeg Microsofts [POP-, IMAP- en SMTP-instellingen voor Outlook.com](https://support.microsoft.com/en-us/outlook/pop-imap-and-smtp-settings-for-outlook-com){target="_blank"}.

??? "iCloud"

    Voor iCloud moet je een app-specifiek wachtwoord voor aanmelding maken. Poort 587 wordt ondersteund. Raadpleeg de officiële handleidingen [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} en [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Voor Yahoo moet je een app-wachtwoord voor aanmelding instellen. Zowel poort 465 als 587 wordt ondersteund. Raadpleeg de officiële handleidingen [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} en [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Opmerking**: voor iedere afzender kunnen SMTP-verzendlimieten gelden, zoals een dagelijkse limiet voor het aantal verzonden e-mails. Raadpleeg je serviceprovider.

Je kunt maximaal 10 e-mailadressen toevoegen.

### Doorsturen via sms {#forward-via-sms}

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Selecteer de landcode, voer het telefoonnummer in en klik op Apply.

Je kunt maximaal 10 mobiele telefoonnummers toevoegen.

---

Gerelateerde artikelen

- [Sms](sms.md)

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
