# Pierwsza konfiguracja

Pierwsza konfiguracja routerów GL.iNet wygląda bardzo podobnie na różnych modelach. Większość modeli ma moduł Wi-Fi, ale nie wszystkie.

Dlatego poniższe wskazówki zostały podzielone na dwa przypadki w zależności od obecności modułu Wi-Fi.

* [Dla modeli z Wi-Fi](#dla-modeli-z-wi-fi)
* [Dla modeli bez Wi-Fi](#dla-modeli-bez-wi-fi)

## Dla modeli z Wi-Fi {#dla-modeli-z-wi-fi}

Poniższe kroki wykorzystują GL-MT3000 (Beryl AX) jako przykład.

Przygotuj następujące elementy znajdujące się w opakowaniu.

- Router GL-MT3000 (Beryl AX)
- Zasilacz
- Kabel Ethernet

Obejrzyj ten poradnik wideo lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. **Włącz zasilanie**

    Podłącz jedną końcówkę zasilacza do routera, a drugą do gniazdka elektrycznego. Router włączy się automatycznie.
    
    Niektóre modele (takie jak Slate AX) są wyposażone w gniazdo karty TF. Jeśli chcesz użyć karty TF, włóż ją przed włączeniem routera. Wymiana karty TF podczas pracy urządzenia nie jest obsługiwana.

2. **Połącz się z routerem**

    Połącz urządzenie (np. smartfon, laptop lub komputer) z routerem kablem Ethernet albo przez Wi-Fi.

    * Połączenie przez Ethernet: Podłącz urządzenie do portu LAN routera za pomocą kabla Ethernet.

    * Połączenie przez Wi-Fi: Znajdź SSID Wi-Fi i Wi-Fi Key na etykiecie na spodzie routera. Wyszukaj SSID routera na swoim urządzeniu, a następnie wprowadź Wi-Fi Key.

        !!! tip
        
            1. Kod QR na etykiecie na spodzie urządzenia zawiera domyślne informacje Wi-Fi. Możesz szybko się połączyć, skanując go skanerem kodów QR.
            2. W przypadku niektórych starszych modeli, jeśli Wi-Fi Key nie znajduje się na etykiecie, spróbuj użyć "goodlife".
        
    Po połączeniu z Wi-Fi możesz nie uzyskać natychmiastowego dostępu do Internetu. Najpierw wykonaj następny krok, aby skonfigurować sieć, a dopiero potem korzystaj z Internetu.

3. **Zaloguj się do panelu administracyjnego WWW**

    Otwórz przeglądarkę internetową (Chrome, Edge i Safari są zalecane dla lepszej zgodności) i przejdź do [http://192.168.8.1](http://192.168.8.1). Zostaniesz przekierowany do strony logowania GL.iNet. Jeśli nie możesz uzyskać dostępu do panelu administracyjnego WWW, kliknij [tutaj](cannot_access_web_admin_panel.md), aby skorzystać z pomocy w rozwiązywaniu problemów.

    Ustaw hasło administratora, a następnie kliknij **Next**.

    ![mt3000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_password.png){class="glboxshadow"}

    Skonfiguruj Wi-Fi. Jeśli zmienisz informacje Wi-Fi, upewnij się, że ponownie połączysz się ze zaktualizowaną siecią, a następnie kliknij **Next**

    ![mt3000 set up wifi](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_set_up_wifi.png){class="glboxshadow"}

    Poczekaj, aż router zakończy inicjalizację.

    ![mt3000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_initializing.png){class="glboxshadow"}

    Następnie uzyskasz dostęp do panelu administracyjnego WWW routera.

    ![mt3000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_panel.png){class="glboxshadow"}

4. **Połącz się z Internetem**

    * [Połącz się z Internetem przez kabel Ethernet](../interface_guide/internet_ethernet.md)
    * [Połącz się z Internetem przez istniejącą sieć Wi-Fi](../interface_guide/internet_repeater.md)
    * [Połącz się z Internetem przez tethering USB](../interface_guide/internet_tethering.md)
    * [Połącz się z Internetem przez modem USB](../interface_guide/internet_cellular.md)

## Dla modeli bez Wi-Fi {#dla-modeli-bez-wi-fi}

Poniższe kroki wykorzystują GL-MT5000 (Brume 3) jako przykład.

1. **Włącz zasilanie**

    Podłącz jedną końcówkę zasilacza do routera, a drugą do gniazdka elektrycznego. Router włączy się automatycznie.

2. **Połącz się z routerem**

    Połącz urządzenie (np. laptop lub komputer) z portem LAN routera za pomocą kabla Ethernet.

3. **Zaloguj się do panelu administracyjnego WWW**

    Otwórz przeglądarkę internetową (Chrome, Edge i Safari są zalecane dla lepszej zgodności) i przejdź do [http://192.168.8.1](http://192.168.8.1). Zostaniesz przekierowany do strony logowania GL.iNet. Jeśli nie możesz uzyskać dostępu do panelu administracyjnego WWW, kliknij [tutaj](cannot_access_web_admin_panel.md), aby skorzystać z pomocy w rozwiązywaniu problemów.

    Ustaw hasło administratora, a następnie kliknij **Next**.

    ![mt5000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_password.png){class="glboxshadow"}

    Poczekaj, aż router zakończy inicjalizację.

    ![mt5000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_initializing.png){class="glboxshadow"}

    Następnie uzyskasz dostęp do panelu administracyjnego WWW routera.

    ![mt5000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_panel.png){class="glboxshadow"}

4. **Połącz się z Internetem**

    * [Połącz się z Internetem przez kabel Ethernet](../interface_guide/internet_ethernet.md)
    * [Połącz się z Internetem przez tethering USB](../interface_guide/internet_tethering.md)
    * [Połącz się z Internetem przez modem USB](../interface_guide/internet_cellular.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
