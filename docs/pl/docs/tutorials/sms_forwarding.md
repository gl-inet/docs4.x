# Przekazywanie SMS

Routery komórkowe GL.iNet obsługują przekazywanie wiadomości SMS, automatycznie przesyłając przychodzące wiadomości do wyznaczonych odbiorców.

**Uwaga**: Ta funkcja działa tylko na routerach komórkowych GL.iNet z oryginalnym modułem 4G LTE/5G NR i nie jest obsługiwana na innych modułach ani żadnych modułach USB.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Nieobsługiwane modele"
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

## Konfiguracja

Jako przykład użyjemy GL-XE3000 (Puli AX).

Po lewej stronie panelu administracyjnego przejdź do sekcji **INTERNET** -> **Cellular**. 

Kliknij ikonę koperty w prawym górnym rogu, aby wejść na stronę SMS, gdzie znajdziesz ustawienia przekazywania SMS.

![sms setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### Przekazywanie przez e-mail

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: Wstępnie ustawione adresy serwerów dla Gmail, Outlook, iCloud i Yahoo są dostępne na liście rozwijanej. W przypadku innych dostawców poczty zapoznaj się z ich dokumentacją lub skontaktuj się z ich wsparciem.

- **Encryption Method**: Dostępne są trzy opcje: brak, SSL/TLS i STARTTLS.
- **Username**: Wprowadź tutaj adres e-mail.
- **Password**: Użyj hasła specyficznego dla aplikacji lub hasła do konta logowania. W przypadku Gmail, Outlook, iCloud i Yahoo sprawdź poniższy przewodnik.
- **Subject**: Ustaw tutaj temat e-maila.

??? "Gmail"

    W przypadku Gmail musisz zalogować się na swoje konto Google i utworzyć **hasła aplikacji**. Sprawdź oficjalny przewodnik [Logowanie za pomocą haseł aplikacji](https://support.google.com/accounts/answer/185833?hl=pl){target="_blank"}. Przed utworzeniem haseł aplikacji musisz włączyć weryfikację dwuetapową.

    Można używać zarówno portu 465, jak i 587.

??? "Outlook"

    W przypadku Outlook możesz użyć hasła bezpośrednio bez żadnych ustawień i obsługuje port 587. Sprawdź oficjalny przewodnik [Ustawienia POP, IMAP i SMTP dla Outlook.com](https://support.microsoft.com/pl-pl/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}

??? "iCloud"

    W przypadku iCloud musisz utworzyć hasła specyficzne dla aplikacji do logowania i obsługuje port 587. Zapoznaj się z oficjalnym przewodnikiem [Ustawienia serwera poczty iCloud dla innych aplikacji klienckich poczty e-mail](https://support.apple.com/pl-pl/HT202304){target="_blank"} oraz [Generowanie hasła specyficznego dla aplikacji](https://support.apple.com/pl-pl/HT204397){target="_blank"}.

??? "Yahoo"

    W przypadku Yahoo musisz ustawić hasło aplikacji do logowania i obsługuje zarówno port 465, jak i 587. Zapoznaj się z oficjalnym przewodnikiem [Ustawienia dostępu POP i instrukcje dla Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} oraz [Generowanie haseł aplikacji innych firm i zarządzanie nimi](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Uwaga**: Każdy nadawca poczty e-mail może podlegać ograniczeniom wysyłania SMTP, np. dziennemu limitowi liczby wysłanych wiadomości e-mail. Skonsultuj się z dostawcą usług.

Możesz dodać maksymalnie 10 adresów e-mail.

### Przekazywanie przez SMS

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Wybierz kod kraju, wprowadź numer telefonu i kliknij Apply.

Możesz dodać maksymalnie 10 numerów telefonów komórkowych.

---

Powiązane artykuły

- [SMS](../interface_guide/sms.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.