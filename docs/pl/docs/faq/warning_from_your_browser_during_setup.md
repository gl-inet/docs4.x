# Ostrzeżenie przeglądarki: Your Connection is not Private

Jeśli konfigurujesz router GL.iNet po raz pierwszy, możesz zobaczyć w przeglądarce ostrzeżenie: Your Connection is not Private.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Jest to standardowe ostrzeżenie bezpieczeństwa wyświetlane przez przeglądarkę, gdy wykryje stronę bez zaufanego certyfikatu SSL/TLS.

Przeglądarki zazwyczaj ufają certyfikatom wydanym przez zewnętrzne urzędy certyfikacji (CA). Routery GL.iNet używają jednak certyfikatów samopodpisanych, które nie są wydawane przez CA. Dlatego przeglądarka oznacza je jako niezaufane i wyświetla to ostrzeżenie.

## Czy przeglądanie 192.168.8.1 jest bezpieczne?

Bezpieczeństwo sieci jest dla nas priorytetem. Podczas początkowej konfiguracji połączenie z internetem nie jest potrzebne, ponieważ cały proces odbywa się lokalnie.

Podczas łączenia się z Wi-Fi routera GL.iNet w trakcie konfiguracji możesz zobaczyć komunikat **"Connected, No internet"**. To normalne, ponieważ podczas konfiguracji router działa jako niezależna sieć lokalna.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Podobnie adres IP **192.168.8.1** jest prywatnym lokalnym adresem IP przypisanym samemu routerowi. Służy do uzyskania dostępu do lokalnego panelu administracyjnego urządzenia, a nie do publicznej strony internetowej.

Ponieważ połączenie jest całkowicie lokalne, a podczas konfiguracji nie jest wymagany dostęp do internetu, **nie ma ryzyka wycieku prywatnych danych**. Zapewnia to bezpieczne, odizolowane środowisko do konfiguracji routera.

## Dlaczego nadal widzę ostrzeżenie?

Przeglądarki zazwyczaj nie rozróżniają wstępnie ustawionego adresu IP używanego do konfiguracji od zwykłych stron internetowych; traktują wszystkie adresy IP jak strony WWW i oczekują, że połączenia HTTPS będą zabezpieczone certyfikatami SSL/TLS.

Routery GL.iNet korzystają z certyfikatów SSL/TLS, ale są to certyfikaty samopodpisane, a nie wystawione przez zewnętrzne urzędy certyfikacji (CA). Mimo że dostęp do tego adresu IP jest bezpieczny, ponieważ odbywa się w prywatnej sieci lokalnej, przeglądarka nadal uznaje go za „niezaufany”, dlatego wyświetla ostrzeżenie.

## Co zrobić z tym ostrzeżeniem?

Kliknij **Advanced** i **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Następnie zostaniesz przekierowany do panelu administracyjnego WWW.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Czy mogę dodać certyfikat SSL do routera?

Tak, możesz dodać własny certyfikat SSL do routerów GL.iNet.

[Jak dodać certyfikat SSL](../faq/use_https_for_adh.md)

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
