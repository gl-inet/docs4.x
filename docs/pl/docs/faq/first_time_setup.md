# Pierwsza konfiguracja

Pierwsza konfiguracja routera GL.iNet wygląda bardzo podobnie na różnych modelach. Większość modeli ma moduł Wi-Fi, ale nie wszystkie. 

Dlatego poniższe wskazówki zostały podzielone na dwa przypadki w zależności od obecności modułu Wi-Fi.

* [Dla modeli z Wi-Fi](#dla-modeli-z-wi-fi)
* [Dla modeli bez Wi-Fi](#dla-modeli-bez-wi-fi)

## Dla modeli z Wi-Fi {#dla-modeli-z-wi-fi}

Poniżej jako przykład pokazano GL-AXT1800 (Slate AX).

Przygotuj następujące elementy znajdujące się w opakowaniu.

- GL-AXT1800
- Zasilacz
- Kabel Ethernet

Obejrzyj ten poradnik wideo lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(W tym filmie do demonstracji konfiguracji użyto innego routera GL.iNet, ponieważ kroki są takie same dla większości modeli.)</small>

1. Włącz zasilanie

    Jeśli chcesz użyć karty TF, włóż ją przed włączeniem routera. Wymiana karty TF podczas pracy urządzenia nie jest obsługiwana.

    Podłącz jedną końcówkę zasilacza do routera, a drugą do gniazdka elektrycznego. Router włączy się automatycznie.

2. Połącz się z routerem

    Możesz połączyć się z routerem kablem Ethernet lub przez Wi-Fi.

    * Połączenie kablowe

        Podłącz komputer do portu LAN routera za pomocą kabla Ethernet.

    * Połączenie przez Wi-Fi

        SSID sieci Wi-Fi jest wydrukowany na etykiecie na spodzie routera w jednym z poniższych formatów:

        **GL-AXT1800-XXX** lub **GL-AXT1800-XXX-5G**

        Domyślny **Wi-Fi Key** znajduje się pod nazwą SSID. 

        Wyszukaj SSID routera na komputerze, telefonie lub tablecie, a następnie wprowadź **Wi-Fi Key**. W przypadku niektórych modeli, jeśli hasła Wi-Fi nie ma na etykiecie, spróbuj użyć "**goodlife**".

        **Wskazówka:** Kod QR na etykiecie na spodzie urządzenia zawiera domyślne informacje o Wi-Fi. Możesz szybko się połączyć, skanując go skanerem kodów QR w telefonie.

        **Uwaga:** Po połączeniu z Wi‑Fi możesz nie uzyskać natychmiastowego dostępu do Internetu. Najpierw wykonaj następny krok, aby skonfigurować sieć, a dopiero potem korzystaj z Internetu.

3. Zaloguj się do panelu administracyjnego WWW

    Otwórz przeglądarkę internetową (zalecamy Chrome, Edge lub Safari) i przejdź do [http://192.168.8.1](http://192.168.8.1). Zostaniesz przekierowany do wstępnej konfiguracji panelu administracyjnego WWW. 
    
    Jeśli nie możesz uzyskać dostępu do panelu administracyjnego WWW, sprawdź [ten artykuł](cannot_access_web_admin_panel.md).

    Wybierz język i kliknij **Next**, aby kontynuować.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Ustaw hasło administratora. Zalecamy użycie silnego hasła. Kliknij **Apply**, aby kontynuować.

    **Uwaga**: Podczas inicjalizacji Wi‑Fi może zostać wyłączone, więc upewnij się, że ponownie połączysz się z routerem.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Po zakończeniu wstępnej konfiguracji wejdziesz do panelu administracyjnego WWW routera.

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Połącz się z Internetem

    * [Połącz się z Internetem przez kabel Ethernet](../interface_guide/internet_ethernet.md)
    * [Połącz się z Internetem przez istniejącą sieć Wi-Fi](../interface_guide/internet_repeater.md)
    * [Połącz się z Internetem przez tethering USB](../interface_guide/internet_tethering.md)
    * [Połącz się z Internetem przez modem USB](../interface_guide/internet_cellular.md)

## Dla modeli bez Wi-Fi {#dla-modeli-bez-wi-fi}

Poniżej jako przykład pokazano GL-MT2500A (Brume 2).

1. Włącz zasilanie

    Podłącz jedną końcówkę zasilacza do routera, a drugą do gniazdka elektrycznego. Router włączy się automatycznie.

2. Połącz się z routerem

    Z routerem można połączyć się kablem Ethernet lub przez Wi-Fi.

    * Bezpośrednie połączenie kablem Ethernet

        Podłącz komputer do portu LAN routera za pomocą kabla Ethernet. To zalecana metoda konfiguracji, ponieważ jest prosta i bezpośrednia.

    * Połączenie przez Wi-Fi innego routera

        Ponieważ GL-MT2500A nie ma wbudowanego modułu Wi-Fi, do wstępnej konfiguracji GL-MT2500A można użyć innego routera z obsługą Wi-Fi.

        * Metoda 1: Ustaw drugi router w trybie AP (Access Point), a następnie podłącz port LAN GL-MT2500A do portu WAN drugiego routera.

        * Metoda 2: Pozostaw drugi router w domyślnym trybie routera, ale ustaw na nim inny adres IP routera, który nie koliduje z 192.168.8.1/24, na przykład 192.168.10.1. Następnie podłącz port LAN GL-MT2500A do portu WAN drugiego routera.

        Użyj komputera lub smartfona, aby połączyć się z Wi-Fi drugiego routera.

        !!! Note
        
            Wspomniany tutaj drugi router to zwykły router, taki jak GL.iNet GL-AXT1800, TP-LINK lub Netgear. Modemy, optyczne terminale sieciowe lub urządzenia dostarczane przez dostawców Internetu mogą nie działać w tym scenariuszu.

3. Otwórz panel administracyjny WWW

    Otwórz przeglądarkę internetową (zalecamy Chrome, Edge lub Safari) i przejdź do [http://192.168.8.1](http://192.168.8.1). Zostaniesz przekierowany do wstępnej konfiguracji panelu administracyjnego WWW. Jeśli nie możesz uzyskać dostępu do panelu administracyjnego WWW, sprawdź [ten artykuł](cannot_access_web_admin_panel.md).

    Wybierz język i kliknij **Next**, aby kontynuować.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Ustaw hasło administratora. Zalecamy użycie silnego hasła. Kliknij **Submit**, aby kontynuować.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Po zakończeniu wstępnej konfiguracji wejdziesz do panelu administracyjnego WWW routera.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Połącz się z Internetem

    * [Połącz się z Internetem przez kabel Ethernet](../interface_guide/internet_ethernet.md)
    * [Połącz się z Internetem przez tethering USB](../interface_guide/internet_tethering.md)
    * [Połącz się z Internetem przez modem USB](../interface_guide/internet_cellular.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
