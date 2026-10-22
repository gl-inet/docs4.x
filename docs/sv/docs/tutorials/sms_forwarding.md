# SMS-vidarebefordran {#sms-forwarding}

GL.iNets mobilroutrar stöder SMS-vidarebefordran och skickar automatiskt inkommande meddelanden till angivna mottagare.

**Obs!** Funktionen fungerar endast på GL.iNet-mobilroutrar med den ursprungliga 4G LTE-/5G NR-modulen. Den stöds inte på andra moduler eller USB-moduler.

## Modeller som stöds {#supported-models}

??? "Modeller som stöds"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Modeller som inte stöds"
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

## Snabbkonfiguration {#quick-setup}

GL-XE3000 (Puli AX) används som exempel.

1. Följ [den här länken](../interface_guide/internet_cellular.md) för att först konfigurera mobilroutern.

2. Logga in på routerns webbadministrationspanel och gå till **INTERNET** -> **Cellular**. Klicka på kuvertikonen i det övre högra hörnet för att öppna SMS-sidan. Där finns inställningarna för SMS Forwarding.

    ![sms setting](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms.png){class="glboxshadow"}

### Vidarebefordra via e-post {#forward-via-email}

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: Förinställda serveradresser för Gmail, Outlook, iCloud och Yahoo finns i listrutan. En förinställd serveradress garanterar inte kompatibilitet med leverantörens autentiseringskrav. För andra e-postleverantörer följer du deras dokumentation eller kontaktar deras support.
- **Encryption Method**: Tre alternativ finns: none, SSL/TLS och STARTTLS.
- **Username**: Ange e-postadressen här.
- **Password**: Ange SMTP-lösenordet som e-postleverantören kräver, till exempel ett appspecifikt lösenord. Se leverantörskraven nedan.
- **Subject**: Ange e-postmeddelandets ämne här.

??? "Gmail"

    För Gmail måste du logga in på Google-kontot och skapa ett **App Passwords**. Följ den officiella guiden [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Du måste aktivera tvåstegsverifiering innan du skapar applösenordet.

    Både port 465 och 587 kan användas.

??? "Outlook.com"

    Outlook.com kräver OAuth2 (Modern Authentication) för SMTP-autentisering. SMTP-servern är `smtp-mail.outlook.com` och använder port `587` med `STARTTLS`.

    Bekräfta att routerns firmware stöder autentiseringsmetoden innan du använder ett Outlook.com-konto för att skicka vidarebefordrade SMS.

    Se Microsofts [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/outlook/pop-imap-and-smtp-settings-for-outlook-com){target="_blank"}.

??? "iCloud"

    För iCloud måste du skapa ett appspecifikt lösenord för inloggning. Tjänsten stöder port 587. Se de officiella guiderna [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} och [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    För Yahoo måste du ange ett applösenord för inloggning. Tjänsten stöder både port 465 och 587. Se de officiella guiderna [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} och [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Obs!** Varje e-postavsändare kan omfattas av SMTP-gränser, till exempel en daglig gräns för antalet skickade e-postmeddelanden. Kontakta tjänsteleverantören.

Du kan lägga till högst 10 e-postadresser.

### Vidarebefordra via SMS {#forward-via-sms}

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Välj landskod, ange telefonnumret och klicka på Apply.

Du kan lägga till högst 10 mobiltelefonnummer.

---

Relaterade artiklar

- [SMS](sms.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
