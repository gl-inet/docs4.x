# Transfert de SMS {#sms-forwarding}

Les routeurs cellulaires GL.iNet prennent en charge le transfert de SMS, en envoyant automatiquement les messages entrants vers des destinataires désignés.

**Remarque** : cette fonctionnalité ne fonctionne qu'avec les routeurs cellulaires GL.iNet équipés du module 4G LTE/5G NR d'origine, et n'est pas prise en charge avec d'autres modules ou modules USB.


## Modèles pris en charge {#supported-models}

??? "Modèles pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Modèles non pris en charge"
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

## Configuration {#quick-setup}

Prenons le GL-XE3000 (Puli AX) comme exemple.

1. Consultez [ce lien](../interface_guide/internet_cellular.md) pour configurer d'abord votre routeur cellulaire.

2. Connectez-vous au panneau d'administration web du routeur et accédez à **INTERNET** -> **Cellular**. Cliquez sur l'icône d'enveloppe en haut à droite pour accéder à la page SMS, où vous trouverez les paramètres de transfert de SMS (**SMS Forwarding**).

    ![sms setting](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms.png){class="glboxshadow"}

### Transfert par e-mail {#forward-via-email}

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address** : Des adresses de serveur prédéfinies pour Gmail, Outlook, iCloud et Yahoo sont disponibles dans la liste déroulante. Une adresse prédéfinie ne garantit pas la compatibilité avec les exigences d’authentification du fournisseur. Pour les autres fournisseurs de messagerie, consultez leur documentation ou contactez leur assistance.

- **Encryption Method** : trois options sont proposées : none, SSL/TLS et STARTTLS.
- **Username** : saisissez l'adresse e-mail ici.
- **Password** : Saisissez le mot de passe SMTP requis par votre fournisseur de messagerie, par exemple un mot de passe spécifique à une application. Consultez les exigences de chaque fournisseur ci-dessous.
- **Subject** : définissez l'objet de l'e-mail ici.

??? "Gmail"

    Pour Gmail, vous devez vous connecter à votre compte Google et créer un mot de passe d'application (**App Passwords**). Consultez le guide officiel [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Vous devez activer la validation en deux étapes avant de créer le mot de passe d'application.

    Les ports 465 et 587 peuvent tous deux être utilisés.

??? "Outlook.com"

    Outlook.com exige OAuth2 (Modern Authentication) pour l’authentification SMTP. Son serveur SMTP est `smtp-mail.outlook.com`, sur le port `587` avec `STARTTLS`.

    Avant d’utiliser un compte Outlook.com pour envoyer des SMS transférés, vérifiez que le firmware de votre routeur prend en charge cette méthode d’authentification.

    Consultez la documentation Microsoft sur les [paramètres POP, IMAP et SMTP pour Outlook.com](https://support.microsoft.com/en-us/outlook/pop-imap-and-smtp-settings-for-outlook-com){target="_blank"}.

??? "iCloud"

    Pour iCloud, vous devez créer un mot de passe spécifique à l'application pour vous connecter, et le port 587 est pris en charge. Consultez les guides officiels [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} et [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Pour Yahoo, vous devez définir un mot de passe d'application pour vous connecter, et les ports 465 et 587 sont tous deux pris en charge. Consultez les guides officiels [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} et [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Remarque** : chaque expéditeur d'e-mail peut être soumis à des limites d'envoi SMTP, par exemple une limite quotidienne du nombre d'e-mails envoyés. Veuillez consulter votre fournisseur de services.

Vous pouvez ajouter jusqu'à 10 adresses e-mail.

### Transfert par SMS {#forward-via-sms}

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Choisissez l'indicatif national, saisissez le numéro de téléphone, puis cliquez sur Apply.

Vous pouvez ajouter jusqu'à 10 numéros de téléphone mobile.

---

Articles connexes

- [SMS](sms.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
