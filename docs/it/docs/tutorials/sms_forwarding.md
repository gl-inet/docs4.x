# Inoltro SMS {#sms-forwarding}

I router cellulari GL.iNet supportano l'inoltro SMS, inviando automaticamente i messaggi in arrivo ai destinatari designati.

**Nota**: questa funzione funziona solo sui router cellulari GL.iNet con modulo originale 4G LTE/5G NR e non e supportata su altri moduli o su qualsiasi altro modulo USB.

## Modelli supportati {#supported-models}

??? "Modelli supportati"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Modelli non supportati"
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

## Configurazione {#quick-setup}

Prendiamo come esempio il GL-XE3000 (Puli AX).

1. Consulta [questo link](../interface_guide/internet_cellular.md) per configurare prima il router cellulare.

2. Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**. Fai clic sull'icona della busta in alto a destra per entrare nella pagina SMS, dove troverai le impostazioni di inoltro SMS.

    ![sms setting](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms.png){class="glboxshadow"}

### Inoltrare via email {#forward-via-email}

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: Nel menu a discesa sono disponibili indirizzi server preimpostati per Gmail, Outlook, iCloud e Yahoo. Un indirizzo preimpostato non garantisce la compatibilità con i requisiti di autenticazione del provider. Per altri provider di posta, consulta la loro documentazione o contatta la loro assistenza.

- **Encryption Method**: sono disponibili tre opzioni, none, SSL/TLS e STARTTLS.
- **Username**: inserisci qui l'indirizzo email.
- **Password**: Inserisci la password SMTP richiesta dal tuo provider di posta, ad esempio una password specifica per l’app. Consulta i requisiti dei singoli provider riportati di seguito.
- **Subject**: imposta qui l'oggetto dell'email.

??? "Gmail"

    Per Gmail, devi accedere al tuo account Google e creare una voce **App Passwords**. Consulta la guida ufficiale [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Devi abilitare la verifica in due passaggi prima di creare le App Passwords.

    Sono utilizzabili sia la porta 465 sia la 587.

??? "Outlook.com"

    Outlook.com richiede OAuth2 (Modern Authentication) per l’autenticazione SMTP. Il server SMTP è `smtp-mail.outlook.com`, con porta `587` e `STARTTLS`.

    Prima di usare un account Outlook.com per inviare SMS inoltrati, verifica che il firmware del router supporti questo metodo di autenticazione.

    Consulta la documentazione Microsoft sulle [impostazioni POP, IMAP e SMTP per Outlook.com](https://support.microsoft.com/en-us/outlook/pop-imap-and-smtp-settings-for-outlook-com){target="_blank"}.

??? "iCloud"

    Per iCloud, devi creare una password specifica per l'app per effettuare l'accesso e la porta supportata e la 587. Consulta la guida ufficiale [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} e [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Per Yahoo, devi impostare una password per app per effettuare l'accesso e sono supportate sia la porta 465 sia la 587. Consulta la guida ufficiale [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} e [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Nota**: ogni mittente email puo essere soggetto a limiti di invio SMTP, ad esempio un limite giornaliero sul numero di email inviate. Consulta il tuo provider di servizi.

Puoi aggiungere fino a 10 indirizzi email.

### Inoltrare via SMS {#forward-via-sms}

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Seleziona il prefisso nazionale, inserisci il numero di telefono e fai clic su Apply.

Puoi aggiungere fino a 10 numeri di cellulare.

---

Articoli correlati

- [SMS](sms.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
