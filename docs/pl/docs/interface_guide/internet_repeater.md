# Połączenie z Internetem przez istniejącą sieć Wi-Fi w trybie Repeater

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Korzystanie z Repeater oznacza połączenie routera z inną istniejącą siecią bezprzewodową, np. gdy używasz bezpłatnego Wi‑Fi w hotelu lub kawiarni.

Domyślnie działa to w trybie WISP (Wireless Internet Service Provider), co oznacza, że router utworzy własną podsieć i będzie działał jako zapora, aby chronić Cię przed siecią publiczną.

## Podstawowe kroki

Zaloguj się do panelu administracyjnego routera, przejdź do sekcji **INTERNET** -> **Repeater** i kliknij **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Wybierz z listy dostępnych sieci sieć Wi‑Fi, z którą chcesz się połączyć.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Uwaga**: Na stronie są wyświetlane kanały Wi‑Fi obsługiwane przez router. Upewnij się, że sieć Wi‑Fi, z którą chcesz się połączyć, korzysta z jednego z tych kanałów, w przeciwnym razie może nie pojawić się na liście dostępnych sieci.

Wprowadź prawidłowe hasło Wi‑Fi i kliknij **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Jeśli identyfikator SSID sieci Wi‑Fi, z którą chcesz się połączyć, nie znajduje się na liście Available Network, kliknij **Join Other Network** w prawym górnym rogu i ręcznie wpisz SSID oraz inne wymagane informacje. Szczegółowe kroki znajdziesz [tutaj](#join-other-network).

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

W przypadku łączenia się z publicznym hotspotem, takim jak te dostępne w hotelach, na lotniskach lub w centrach handlowych, zobacz sekcję [Publiczny hotspot](#for-public-hotspot).

Pozostałe ustawienia opisano w sekcji [Ustawienia zaawansowane](#advanced-settings).

Po chwili, jeśli hasło zostało wpisane poprawnie, połączenie zostanie nawiązane.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Publiczny hotspot {#for-public-hotspot}

Podczas łączenia routera z publicznym hotspotem z captive portal włączenie poniższych funkcji może pomóc zwiększyć skuteczność połączenia.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Ta funkcja jest dostępna od wersji v4.6.

    Jeśli ta opcja jest włączona, router automatycznie przejdzie do Login Mode for Public Hotspots, gdy pomyślnie połączy się z hotspotem, ale nie z Internetem. **W tym trybie niektóre usługi zostaną zawieszone, a tryb DNS zostanie przełączony na automatyczny**, co może ujawnić aktywność sieciową dostawcy hotspotu (np. hotelowi lub centrum handlowemu).

    Nawet jeśli ta opcja nie jest włączona, router poprosi o przejście do tego trybu, gdy wykryje captive portal w hotspotie i nie uda się zalogować.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Jeśli opcja jest włączona, router będzie podszywał się pod urządzenie klienckie używane do uzyskania dostępu do panelu administracyjnego, emulując adres MAC tego urządzenia.

- **MAC Mode**

    Możesz wybrać, którego adresu MAC router ma używać do łączenia się z publicznym hotspotem.

    - **Factory**: Używa oryginalnego fabrycznego adresu MAC urządzenia.

    - **Clone**: Klonuje adres MAC urządzenia klienckiego na potrzeby połączenia. Jeśli żądanego adresu MAC nie ma na liście, wpisz adres do sklonowania ręcznie. 
    
        Uwaga: Wiele nowoczesnych urządzeń używa losowych adresów MAC (często nazywanych Private Wi‑Fi Address lub random hardware address) podczas łączenia z sieciami Wi‑Fi. Z tego powodu wyświetlany tutaj adres MAC może nie odpowiadać rzeczywistemu fizycznemu adresowi MAC urządzenia.
  
    - **Random**: Automatycznie generuje losowy adres MAC na potrzeby połączenia.

    Podczas zapisywania konfiguracji sieci tryb MAC Mode (w tym sklonowany lub losowy adres MAC) jest przypisywany do konkretnego zapisanego SSID. Ustawienia te można w dowolnym momencie zmienić ręcznie dla każdego SSID.

- **Auto Update MAC**: Jeśli ta opcja jest włączona, adres MAC może być aktualizowany automatycznie.

## Ustawienia zaawansowane {#advanced-settings}

Podczas dołączania do sieci dostępne są dodatkowe opcje.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: Włącz tę opcję, aby zapamiętać bieżącą sieć Wi‑Fi używaną przez repeater.

* **Lock BSSID**: Po włączeniu router będzie łączyć się tylko z określonym punktem dostępowym (AP) odpowiadającym wybranemu BSSID, nawet jeśli inne punkty AP współdzielą ten sam SSID.

* **Manually Set Static IP**: Po włączeniu możesz ręcznie skonfigurować stały adres IPv4, maskę sieci, bramę i serwery DNS dla połączenia repeatera, zamiast pobierać te ustawienia automatycznie.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live) określa maksymalny czas życia pakietów w sieci i jest ustawiany zgodnie z wymaganiami operatora. Domyślnie router przekazuje wartość TTL z urządzenia klienckiego pomniejszoną o jeden. Jeśli chcesz włączyć kamuflaż, możesz ustawić tutaj stałą wartość. TTL dotyczy tylko IPv4.

* **HL**: W IPv6 pole HL (Hop Limit) służy do ograniczania liczby przeskoków transmisji pakietów danych w sieci i jest odpowiednikiem TTL w IPv4.

* **MTU**: Wartość domyślna to 1500.

## Opcje Repeater

Aby wyświetlić opcje repeatera, kliknij ikonę koła zębatego w prawym górnym rogu sekcji połączonego Repeater.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**W przypadku firmware v4.8** strona Repeater Options wygląda następująco.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**: 

    - No Switching mode: Gdy tryb No Switching mode jest włączony, po rozłączeniu bieżącej sieci Wi‑Fi inne zapisane sieci nie będą łączone automatycznie.
  
    - Auto Switching mode: Gdy tryb Auto Switching mode jest włączony, router będzie próbował połączyć się z innymi zapisanymi sieciami po rozłączeniu bieżącej sieci Wi‑Fi.
  
    - Auto Switching Without Network: Gdy tryb Auto Switching Without Network jest włączony, router nie będzie automatycznie skanował sieci, gdy ma już połączenie w trybie innym niż repeater, i będzie próbował automatycznie przełączyć się na inne zapisane sieci dopiero wtedy, gdy router nie ma połączenia z siecią, co może ograniczyć utratę pakietów.

- **Band Selection**: możesz wybrać jedną z trzech opcji: Auto, 5 GHz i 2.4 GHz.

    Jeśli ręcznie wybierzesz pasmo, router nie będzie skanował ani łączył się z żadną siecią Wi‑Fi korzystającą z innego pasma.

**W przypadku firmware v4.7 i starszego** strona Repeater Options wygląda jak poniżej.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. Jeśli opcja jest włączona, router automatycznie połączy się z innymi zapisanymi sieciami, gdy nie będzie mógł połączyć się z bieżącą siecią Wi‑Fi.

* **Band Selection**. Jeśli ręcznie wybierzesz pasmo, router nie będzie skanował ani łączył się z żadną siecią Wi‑Fi w innym paśmie.

## Zarządzanie zapisanymi sieciami

Aby usunąć zapisaną sieć, kliknij **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Jeśli obecnie nie ma połączonej żadnej sieci, kliknij **Connect** w sekcji Repeater.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

W sekcji **Known Networks** kliknij ikonę kosza, aby usunąć zapisaną sieć, albo ikonę koła zębatego, aby skonfigurować sieć.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Dołączanie do innej sieci {#join-other-network}

Jeśli SSID nie znajduje się na liście Available Networks albo jest ukryty, możesz kliknąć **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Wpisz SSID, wybierz Security i wprowadź hasło (jeśli jest wymagane).

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Dla ustawienia **Security** dostępne są dwie lub trzy opcje, w zależności od modelu.

* None, co oznacza brak wymaganego hasła.
* WPA/WPA2/WPA3, czyli najczęściej używaną opcję obsługiwaną przez niemal wszystkie sieci Wi‑Fi.
* WPA/WPA2/WPA3 Enterprise, która wymaga uwierzytelniania przy użyciu Extensible Authentication Protocol (EAP). Do połączenia potrzebne są prawidłowa nazwa użytkownika i hasło (zwykle używane w sieciach firmowych lub kampusowych).

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Szczegółowe wskazówki dotyczące korzystania z repeatera w sieciach EAP znajdziesz [tutaj](../tutorials/eap.md){target="_blank"}.

## Ponowne łączenie

W poniższych przypadkach router będzie co jakiś czas automatycznie próbował ponownie połączyć się z Wi‑Fi. W razie potrzeby możesz to wyłączyć ręcznie. Jeśli występują błędy SSID lub hasła, usuń sieć z listy Known Networks, aby rozwiązać problem.

1. Podczas konfiguracji Repeater wpisano nieprawidłowy SSID lub hasło.

2. Po początkowym połączeniu router znalazł się poza zasięgiem urządzenia nadrzędnego.

3. Urządzenie nadrzędne zmieniło SSID lub hasło albo ograniczyło dostęp po nawiązaniu połączenia.

Proces ponownego łączenia składa się z trzech odrębnych faz: oczekiwania, skanowania i łączenia.

1. Faza oczekiwania: Brak problemów — router czeka na warunki ponownego połączenia.

2. Faza skanowania: W skanowanym paśmie częstotliwości może wystąpić utrata pakietów. Nowe urządzenia mogą mieć problemy z połączeniem. W modelach GL-AXT1800/GL-AX1800 funkcja Guest Wi‑Fi zostanie tymczasowo wyłączona.

3. Faza łączenia: Główna sieć Wi‑Fi w docelowym paśmie może zostać przerwana na kilka sekund podczas ponownego zestawiania połączenia.

**Uwaga**: Problemy zwykle pojawiają się w fazie skanowania i łączenia.

## Rozwiązywanie problemów

Gdy router jest połączony z siecią Wi‑Fi jako repeater, ale Internet nie jest dostępny, pojawi się żółty komunikat pokazany poniżej.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Aby rozwiązać ten problem:

1. Sprawdź, czy urządzenie nadrzędne (czyli sieć Wi‑Fi, z którą połączony jest router) ma dostęp do Internetu.

2. Przejdź na stronę [Multi-WAN](multi-wan.md), aby sprawdzić stan interfejsu repeatera.

## DFS

Podczas łączenia z nadrzędną siecią Wi‑Fi 5G sieć Wi‑Fi routera będzie podążać za siecią nadrzędną i korzystać albo nie korzystać z kanału DFS.

* Jeśli nadrzędna sieć Wi‑Fi korzysta z kanału DFS i można ją zeskanować, sieć Wi‑Fi 5G routera użyje tego samego kanału.

* Sieć Wi‑Fi 5G routera przełączy się na kanał bez DFS, jeśli nadrzędnej sieci Wi‑Fi nie można zeskanować lub jeśli połączenie się nie powiedzie.

??? "Obsługiwane modele"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Nieobsługiwane modele"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Powiązane artykuły

- [Strona Internet](internet.md)
- [Jak ustawić priorytet dla każdej metody dostępu do Internetu?](multi-wan.md)
- [Jak ustawić równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu do Internetu?](multi-wan.md)
- [Jak sprawdzić adresy MAC sieci LAN i Wi‑Fi](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
