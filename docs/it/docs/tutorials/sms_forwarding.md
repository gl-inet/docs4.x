# Inoltro SMS

I router cellulari GL.iNet supportano l'inoltro SMS, inviando automaticamente i messaggi in arrivo ai destinatari designati.

**Nota**: questa funzione funziona solo sui router cellulari GL.iNet con modulo originale 4G LTE/5G NR e non e supportata su altri moduli o su qualsiasi altro modulo USB.

## Modelli supportati

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

## Configurazione

Prendiamo come esempio il GL-XE3000 (Puli AX).

Nel lato sinistro del pannello di amministrazione web, vai alla sezione **INTERNET** -> **Cellular**.

Fai clic sull'icona della busta in alto a destra per entrare nella pagina SMS, dove troverai le impostazioni di inoltro SMS.

![sms setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### Inoltrare via email

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: nel menu a discesa sono disponibili indirizzi server preimpostati per Gmail, Outlook, iCloud e Yahoo. Per altri provider email, consulta la loro documentazione o contatta il supporto.

- **Encryption Method**: sono disponibili tre opzioni, none, SSL/TLS e STARTTLS.
- **Username**: inserisci qui l'indirizzo email.
- **Password**: usa una password specifica per l'app oppure la password dell'account di accesso. Per Gmail, Outlook, iCloud e Yahoo, consulta la guida sotto.
- **Subject**: imposta qui l'oggetto dell'email.

??? "Gmail"

    Per Gmail, devi accedere al tuo account Google e creare una voce **App Passwords**. Consulta la guida ufficiale [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Devi abilitare la verifica in due passaggi prima di creare le App Passwords.

    Sono utilizzabili sia la porta 465 sia la 587.

??? "Outlook"

    Per Outlook, puoi usare direttamente la password senza configurazioni aggiuntive e la porta supportata e la 587. Consulta la guida ufficiale [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}

??? "iCloud"

    Per iCloud, devi creare una password specifica per l'app per effettuare l'accesso e la porta supportata e la 587. Consulta la guida ufficiale [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} e [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Per Yahoo, devi impostare una password per app per effettuare l'accesso e sono supportate sia la porta 465 sia la 587. Consulta la guida ufficiale [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} e [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Nota**: ogni mittente email puo essere soggetto a limiti di invio SMTP, ad esempio un limite giornaliero sul numero di email inviate. Consulta il tuo provider di servizi.

Puoi aggiungere fino a 10 indirizzi email.

### Inoltrare via SMS

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Seleziona il prefisso nazionale, inserisci il numero di telefono e fai clic su Apply.

Puoi aggiungere fino a 10 numeri di cellulare.

---

Articoli correlati

- [SMS](../interface_guide/sms.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
