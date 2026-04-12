# Dostęp do routera GL.iNet i AdGuard Home przez HTTPS

Jeśli chcesz używać HTTPS do uzyskiwania dostępu do routera GL.iNet i AdGuard Home, wykonaj poniższe kroki.

## 1. Zaktualizuj certyfikat i klucz w routerze GL.iNet

Najpierw uzyskaj certyfikat SSL lub użyj samopodpisanego certyfikatu SSL.

Następnie połącz się z routerem GL.iNet przez SSH albo użyj WinSCP, aby przesłać zaktualizowany certyfikat i klucz do routera GL.iNet. Ścieżki to:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Włącz AdGuard Home

Zaloguj się do panelu administracyjnego WWW GL.iNet -> APPLICATIONS -> AdGuard Home i włącz AdGuard Home.

![enableadh](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Następnie kliknij **Settings Page** u góry tej strony, a zostaniesz przekierowany do strony ustawień AdGuard Home.

![gosettings](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Edytuj ustawienia szyfrowania

Na stronie ustawień AdGuard Home przejdź do Settings -> Encryption settings.

![encryption](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Zaznacz pole Enable Encryption w lewym górnym rogu i wpisz 3001 w polu HTTPS port.

![3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Dodaj ścieżki do zaktualizowanego certyfikatu i klucza, a następnie kliknij Save.

![addcertpath](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Następnie możesz używać HTTPS, aby otworzyć **192.168.8.1** lub **192.168.8.1:3001**.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
