# Używanie WinSCP do uzyskiwania dostępu do udostępnionych plików

Możesz używać **WinSCP** do uzyskiwania dostępu do udostępnionych plików za pomocą funkcji udostępniania plików w **GL-Routers**.

Skonfiguruj linki **WebDAV** na karcie pamięci sieciowej. Szczegółowe instrukcje konfiguracji znajdziesz w przewodniku [WebDAV](https://docs.gl-inet.com/router/en/4/interface_guide/network_storage/#set-up-webdav)

## Konfiguracja linków w WinSCP

Po skonfigurowaniu WebDAV wróć do strony **Share Folders** w pamięci sieciowej.

![webdav1](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Kliknij prawym przyciskiem ikonę **"..."** i skopiuj link HTTPS.

![webdav2](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Uruchom WinSCP i wybierz WebDAV, a następnie wybierz szyfrowanie TLS/SSL. Następnie wklej link do pola **Host name**; numer portu automatycznie zmieni się na 6008.

![webdav3](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Wprowadź nazwę użytkownika i hasło, a następnie kliknij **Save** i **Login** — udostępniony folder zostanie otwarty.

![webdav4](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

