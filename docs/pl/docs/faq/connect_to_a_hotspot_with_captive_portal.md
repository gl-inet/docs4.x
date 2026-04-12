# Jak podłączyć router GL.iNet do publicznych hotspotów z captive portal

## Czym jest captive portal?

Captive portal to strona WWW, z którą użytkownicy publicznych hotspotów muszą się zapoznać i wejść z nią w interakcję, zanim uzyskają dostęp do Internetu.

## Dlaczego warto używać routera do publicznych hotspotów?

* Publiczne Wi-Fi nie jest bezpieczne

    Trudno przecenić ryzyko związane z publicznym Wi-Fi. Podłączając router GL.iNet do publicznej sieci Wi-Fi, możesz zalogować się do swojego konta VPN bezpośrednio w panelu administracyjnym routera. Router automatycznie zaszyfruje ruch wszystkich podłączonych urządzeń w sieci lokalnej, dzięki czemu nie trzeba konfigurować VPN osobno na każdym urządzeniu.

* Użyj routera jako repeatera, aby połączyć wiele urządzeń

    Ponadto niektóre publiczne sieci Wi-Fi (np. hotelowe Wi-Fi) ograniczają liczbę urządzeń, które mogą się połączyć, na przykład do dwóch. W podróży grupowej jest to bardzo niewygodne. Zamiast tego możesz podłączyć router podróżny do hotelowego Wi-Fi i użyć go jako repeatera do rozgłaszania sygnału Wi-Fi dla wszystkich swoich urządzeń, w tym laptopów, smartfonów, tabletów itd. Hotelowe Wi-Fi rozpozna wtedy router podróżny jako jedno urządzenie, a Ty będziesz mógł podłączyć do darmowego Wi-Fi tyle urządzeń, ile chcesz.

## Jak podłączyć router do publicznych hotspotów z captive portal?

Obejrzyj ten film lub wykonaj poniższe kroki.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Podłącz smartfon lub komputer do routera.

    Włącz router. Na smartfonie lub komputerze wyszukaj SSID routera i wpisz hasło Wi-Fi. Domyślny identyfikator SSID i hasło są wydrukowane na spodzie routera.

2. Zaloguj się do panelu administracyjnego WWW routera.

    Na smartfonie lub komputerze otwórz przeglądarkę i wpisz w pasku adresu adres IP routera (domyślny adres IP: `192.168.8.1`). Otworzy się panel administracyjny WWW routera.
    
    Jeśli logujesz się po raz pierwszy, wybierz język i utwórz hasło logowania do panelu administracyjnego WWW routera.

3. Podłącz router do publicznego hotspotu. Zapoznaj się z poradnikiem [Repeater](../interface_guide/internet_repeater.md/).

## Rozwiązywanie problemów

Jeśli nie możesz otworzyć captive portal, router może nie mieć dostępu do Internetu. Wypróbuj poniższe metody rozwiązywania problemów.

### Metoda 1: Włącz Public Hotspot Login Mode i Camouflage

**Uwaga**: Te dwie funkcje są dostępne tylko w firmware v4.6 i nowszym.

Podczas łączenia routera z publicznym hotspotem włączenie poniższych funkcji na stronie **Join Network** może zwiększyć skuteczność połączenia.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    Jeśli ta opcja jest włączona, router automatycznie przejdzie do Login Mode for Public Hotspots, gdy połączy się z hotspotem, ale nie z Internetem. W tym trybie część usług zostanie zawieszona, a tryb DNS zostanie przełączony na automatyczny, co może ujawnić dostawcy hotspotu (np. hotelowi lub centrum handlowemu) Twoją aktywność sieciową.

- Enable Camouflage

    Po włączeniu router będzie podszywał się pod urządzenie klienckie używane do dostępu do panelu administracyjnego, emulując adres MAC tego urządzenia.

---

### Metoda 2: Zmień ustawienia routera

1. Zaloguj się do panelu administracyjnego WWW i przejdź do **NETWORK** -> **DNS**. Upewnij się, że **DNS Rebinding Attack Protection** jest wyłączone, a **Mode** ustawiono na **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. W panelu administracyjnym WWW przejdź do **VPN** -> **VPN Dashboard**. Upewnij się, że wszystkie połączenia VPN są wyłączone.

    **Dla firmware v4.7 i starszego** strona wygląda jak poniżej.
    
    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}
    
    **Dla firmware v4.8 i nowszego** strona wygląda jak poniżej.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. W panelu administracyjnym WWW przejdź do **APPLICATIONS** -> **AdGuard Home**. Upewnij się, że AdGuard Home jest wyłączony.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Otwórz przeglądarkę i ponownie wpisz adres strony captive portal albo odśwież stronę. Odczekaj chwilę i sprawdź, czy nastąpi automatyczne przekierowanie do strony uwierzytelniania captive portal.

    Jeśli używasz smartfona, a przeglądarka nie przekierowuje do captive portal, wyłącz i włącz ponownie Wi-Fi w telefonie, a następnie połącz się ponownie z Wi-Fi routera. Captive portal powinien wyświetlić się od razu po wpisaniu hasła Wi-Fi.

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Metoda 3：Klonowanie MAC

Niektóre hotele ograniczają liczbę urządzeń, które każdy klient może podłączyć do hotelowego Wi-Fi, identyfikując je po adresach MAC. Adres MAC urządzenia jest zapisywany przy pierwszym połączeniu. W takiej sytuacji możesz sklonować do routera adres MAC używany przez telefon do łączenia z hotelowym Wi-Fi, aby router mógł używać tego samego adresu MAC do uzyskania dostępu do sieci hotelowej.

1. Połącz telefon z hotelowym Wi-Fi. Znajdź adres MAC, którego telefon używa do łączenia z hotelowym Wi-Fi.

    Oto przykład dla iPhone'a (iOS 16.1.2): przejdź do **Settings** -> **Wi-Fi** -> wybierz hotelowe Wi-Fi, a znajdziesz tam **Wi-Fi Address**. Zapisz ten adres.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    W niektórych starszych modelach adres MAC może nie być widoczny w ustawieniach Wi-Fi. W takim przypadku urządzenie może używać rzeczywistego adresu MAC podczas łączenia z publicznym Wi-Fi. Taki adres można znaleźć w **Settings** > **About** (lub **About Phone**).

2. Podłącz telefon lub komputer do routera. Zaloguj się do panelu administracyjnego WWW routera, a następnie sklonuj ten adres MAC lub wpisz go ręcznie.

    **Dla firmware v4.5 i starszego** wybierz po lewej stronie **NETWORK** -> **MAC Address**.

    Wybierz **Manual Mode**, wpisz adres MAC uzyskany w kroku 1 i kliknij **Apply**.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **Dla firmware v4.6 i nowszego** wybierz po lewej stronie **INTERNET** -> sekcję **Repeater**, a następnie kliknij **Modify**.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    W wyskakującym oknie ustaw **MAC Mode** na **Clone**, ręcznie wpisz adres MAC i kliknij **Apply**.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Aby zmiany zaczęły działać, może być konieczne ponowne uruchomienie routera.

---

### Metoda 4：Poproś o pomoc personel hotelu

Niektóre hotele stosują bardzo rygorystyczne zasady weryfikacji w swoich sieciach. Jeśli żadna z powyższych metod nie działa, poproś personel hotelu o bezpośrednie dodanie adresu MAC routera (użyj fabrycznego adresu MAC, a nie losowego) do białej listy sieci hotelowej.

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
