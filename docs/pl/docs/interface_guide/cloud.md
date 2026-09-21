# GL.iNet GoodCloud

## Wprowadzenie

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} to platforma zaprojektowana w celu uproszczenia zdalnego wdrażania i zarządzania podłączonymi urządzeniami. Zapewnia łatwy sposób zdalnego dostępu i zarządzania routerami GL.iNet. Centralizując urządzenia sieciowe w chmurze, użytkownicy mogą efektywnie wykonywać zadania zarządzania zbiorczego, takie jak wdrażanie konfiguracji sieci i przeprowadzanie aktualizacji oprogramowania. Mogą także uzyskać zdalny dostęp do internetowego panelu administracyjnego routera lub połączyć się z terminalem routera za pośrednictwem SSH, uzyskując ponadregionalne i kompleksowe zarządzanie urządzeniami sieciowymi.

Dzięki GoodCloud możesz:

1. Sprawdź status routera w czasie rzeczywistym
    - Monitoruj status online-offline
    - Przeglądaj w czasie rzeczywistym zużycie pamięci RAM i średnie obciążenie
    - Otrzymuj powiadomienia e-mail o zmianach statusu online-offline

2. Skonfiguruj routery zdalnie
    - skonfiguruj ustawienia routera (np. SSID i hasło)
    - Zdalny dostęp SSH
    - Zdalny dostęp do WebUI
    - Udostępnij dostęp do routera innym osobom

3. Monitoruj zdalnie podłączonych klientów
    - Wyświetl urządzenia podłączone do Twojej sieci
    - Monitoruj ruch w czasie rzeczywistym i blokuj klientów
    - Otrzymuj powiadomienia e-mail o nowych połączeniach i blokowaniu wydarzeń

4. Wykonuj operacje wsadowe
    - Ponowne uruchomienie wsadowe
    - Zbiorcza aktualizacja oprogramowania sprzętowego

5. Nawiąż łączność typu site-to-site
    - Wirtualne biuro: Rozszerz swoją sieć biurową na inne oddziały
    - Podróże służbowe: zdalny dostęp do systemów biurowych (np. OA, CRM i MySQL)
    - Inteligentny dom: zdalny dostęp do urządzeń domowych (np. kamery IP i NAS)

Jeśli chcesz zarządzać wieloma urządzeniami i odblokować zaawansowane funkcje, takie jak operacje zbiorcze, zarządzanie wieloma kontami i rozwiązania niestandardowe, wybierz nasze plany z wartością dodaną. Kliknij [here](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}, aby uzyskać szczegółowe informacje i skontaktuj się z [support@gl-inet.com](mailto:support@gl-inet.com).

## Powiąż urządzenia z chmurą

Wybierz odpowiednią sekcję, aby zapoznać się z krokami wiązania urządzenia w oparciu o wersję oprogramowania sprzętowego urządzenia.

### Dla oprogramowania sprzętowego w wersji 4.10 i nowszych

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego routera, przejdź do **CLOUD SERVICE** -> **GoodCloud** i kliknij **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Zostaniesz przekierowany na stronę **GL.iNet Account**. Kliknij **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    W wyskakującym oknie kliknij **Continue**. Zostaniesz przekierowany na stronę GoodCloud, aby dokończyć wiązanie.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Zaloguj się, aby powiązać swoje urządzenie.

    Zaloguj się na swoje konto GL.iNet. Jeśli nie masz konta, załóż je i zaloguj się.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Po zalogowaniu potwierdź informacje o swoim koncie i urządzeniu, w tym identyfikator urządzenia, model i adres MAC. Dostosuj nazwę urządzenia i kliknij **Bind**, a router zostanie powiązany z Twoim kontem.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Jeśli nie otrzymasz e-maila weryfikacyjnego, sprawdź folder ze spamem lub poczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com).

3. Szczegóły wiązania.

    Po pomyślnym powiązaniu wróć do panelu administracyjnego routera i przejdź do **CLOUD SERVICES** -> **GoodCloud**. Na tej stronie wyświetlany jest wpis przekierowania do platformy GoodCloud, szczegóły tożsamości urządzenia i najnowsze dzienniki chmury.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Dostęp zdalny.

    W oprogramowaniu sprzętowym v4.10 zdalny dostęp do panelu administracyjnego routera i terminala będzie domyślnie włączony, gdy router zostanie powiązany z GoodCloud.

5. Odłącz urządzenie.

    Jeśli chcesz odłączyć swój router, zaloguj się do internetowego panelu administracyjnego routera i przejdź do **CLOUD SERVICES** -> **GL.iNet Account**. Kliknij **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    Alternatywnie możesz usunąć urządzenie z listy Powiązanych urządzeń na platformie GoodCloud. Panel administracyjny routera zostanie zsynchronizowany i wyświetli najnowszy stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com) w celu uzyskania pomocy.

### Dla oprogramowania sprzętowego v4.7 do v4.9

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego routera i przejdź do **CLOUD SERVICE** -> **GoodCloud**.

    Kliknij przycisk **Get Started**, a w prawym górnym rogu pojawi się wyskakujące okno usługi w chmurze. Kliknij **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

2. Zaloguj się, aby powiązać swoje urządzenie.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Jeśli nie masz konta, załóż je i zaloguj się. Po zakończeniu rejestracji router zostanie automatycznie powiązany z Twoim kontem.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Jeśli nie otrzymasz e-maila weryfikacyjnego, sprawdź folder ze spamem lub poczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com).

3. Szczegóły wiązania.

    Po pomyślnym powiązaniu wróć do internetowego panelu administracyjnego routera, kliknij ikonę Chmura w prawym górnym rogu, a zobaczysz szczegóły powiązania, w tym nazwę użytkownika, czas powiązania, identyfikator urządzenia, adres MAC urządzenia i numer seryjny urządzenia.

    ![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

4. Włącz dostęp zdalny.

    W internetowym panelu administracyjnym przejdź do **CLOUD SERVICES** -> **GoodCloud** i możesz włączyć zdalny dostęp do swojego routera.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

    - **Remote SSH**: Do zdalnego dostępu do terminala routera przez SSH z platformy GoodCloud.

    - **Remote Web Access**: Do zdalnego dostępu do internetowego panelu administracyjnego routera poprzez HTTP/HTTPS z platformy GoodCloud.

    - **View Logs**: Wyświetli dzienniki połączeń API przez GoodCloud.

5. Odłącz urządzenie.

    Jeśli chcesz odłączyć router, zaloguj się do internetowego panelu administracyjnego routera. Kliknij ikonę chmury w prawym górnym rogu i kliknij **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    Alternatywnie możesz usunąć urządzenie z listy Powiązanych urządzeń na platformie GoodCloud. Panel administracyjny routera zostanie zsynchronizowany i wyświetli najnowszy stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com) w celu uzyskania pomocy.

### Dla oprogramowania sprzętowego w wersji 4.6 lub wcześniejszej

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Przełącz przełącznik, aby włączyć GoodCloud.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    W razie potrzeby włącz **Remote SSH** i **Remote Web Access**, wybierz najbliższy serwer, przeczytaj i zaakceptuj **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: Do zdalnego dostępu do terminala routera przez SSH z platformy GoodCloud.

    - **Remote Web Access**: Do zdalnego dostępu do internetowego panelu administracyjnego routera poprzez HTTP/HTTPS z platformy GoodCloud.

    - **Data Server**: Wybierz serwer najbliższy lokalizacji Twojego urządzenia. Dostępne są trzy opcje: Azja i Pacyfik (Japan), Ameryka (Oregon) i Europa (Ireland).

2. Zarejestruj konto.

    Odwiedź [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, zarejestruj się i zaloguj.

    Jeśli nie otrzymasz e-maila weryfikacyjnego, sprawdź folder ze spamem lub poczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com).

3. Dodaj urządzenia.

    Na platformie Cloud przejdź do **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Istnieją trzy metody powiązania urządzenia z kontem GoodCloud: automatyczne wykrywanie, dodawanie ręczne i import zbiorczy.

    ??? "Auto Discover"

        Możesz wypróbować **Auto discover**, jeśli router i urządzenie używane do uzyskiwania dostępu do witryny GoodCloud znajdują się w tej samej sieci.

        Wybierz swoje urządzenie z listy rozwijanej i wpisz **DDNS / Device ID**, który można znaleźć na dole routera lub na stronie GoodCloud w internetowym panelu administracyjnym.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Aby znaleźć identyfikator urządzenia, zapoznaj się z [this link](../faq/where_to_find_the_device_id_mac_sn.md).

    ??? "Manually Add"

        Jeśli Twojego urządzenia nie ma na liście, kliknij **Manually add** i wprowadź szczegóły swojego routera. Wszystkie wymagane informacje można znaleźć na dole routera lub na stronie GoodCloud w internetowym panelu administracyjnym.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** przeznaczony jest dla użytkowników zarządzających dużą liczbą urządzeń. Możesz zaimportować wiele urządzeń za pomocą pliku Microsoft Excel.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Szczegóły wiązania.

    Po pomyślnym powiązaniu wróć do panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Na tej stronie wyświetlane są szczegóły wiązania, w tym nazwa użytkownika i czas wiązania.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

5. Odłącz urządzenie.

    Jeśli chcesz odłączyć swój router, zaloguj się do internetowego panelu administracyjnego routera, przejdź do **APPLICATION** -> **GoodCloud** i kliknij **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    Alternatywnie możesz usunąć urządzenie z listy Powiązanych urządzeń na platformie GoodCloud. Panel administracyjny routera zostanie zsynchronizowany i wyświetli najnowszy stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij e-mail do [support@gl-inet.com](mailto:support@gl-inet.com) w celu uzyskania pomocy.
