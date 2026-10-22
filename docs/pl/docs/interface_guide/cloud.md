# GL.iNet GoodCloud {#glinet-goodcloud}

## Wprowadzenie {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} to platforma zaprojektowana w celu uproszczenia zdalnego wdrażania podłączonych urządzeń i zarządzania nimi. Zapewnia łatwy sposób zdalnego dostępu do routerów GL.iNet i zarządzania nimi. Dzięki scentralizowaniu urządzeń sieciowych w chmurze użytkownicy mogą efektywnie wykonywać zadania zarządzania zbiorczego, takie jak wdrażanie konfiguracji sieci i aktualizacja oprogramowania. Mogą także zdalnie uzyskać dostęp do panelu administracyjnego WWW routera lub połączyć się z terminalem routera przez SSH, co umożliwia kompleksowe zarządzanie urządzeniami sieciowymi, również w różnych regionach.

Dzięki GoodCloud możesz:

1. Sprawdzać stan routera w czasie rzeczywistym
    - Monitorować stan online/offline
    - Wyświetlać w czasie rzeczywistym użycie pamięci RAM i średnie obciążenie
    - Otrzymywać powiadomienia e-mail o zmianach stanu online/offline

2. Zdalnie konfigurować routery
    - Konfigurować ustawienia routera (np. SSID i hasło)
    - Zdalny dostęp przez SSH
    - Zdalny dostęp do WebUI
    - Udostępniać dostęp do routera innym osobom

3. Zdalnie monitorować podłączonych klientów
    - Wyświetlać urządzenia podłączone do Twojej sieci
    - Monitorować ruch w czasie rzeczywistym i blokować klientów
    - Otrzymywać powiadomienia e-mail o nowych połączeniach i zdarzeniach blokowania

4. Wykonywać operacje zbiorcze
    - Zbiorczy restart
    - Zbiorcza aktualizacja firmware

5. Nawiązywać łączność site-to-site
    - Wirtualne biuro: rozszerzenie sieci biurowej na inne oddziały
    - Podróże służbowe: zdalny dostęp do systemów biurowych (np. OA, CRM, MySQL)
    - Inteligentny dom: zdalny dostęp do urządzeń domowych (np. kamer IP, NAS)

Jeśli chcesz zarządzać wieloma urządzeniami i odblokować zaawansowane funkcje, takie jak operacje zbiorcze, zarządzanie wieloma kontami i rozwiązania niestandardowe, wybierz jeden z naszych planów z wartością dodaną. Kliknij [tutaj](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}, aby uzyskać szczegółowe informacje, i skontaktuj się z nami pod adresem [support@gl-inet.com](mailto:support@gl-inet.com).

## Powiązywanie urządzeń z chmurą {#bind-devices-to-cloud}

Wybierz sekcję odpowiadającą wersji firmware urządzenia, aby zapoznać się z krokami powiązania.

### Dla firmware v4.10 i nowszego {#for-firmware-v410-and-above}

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego WWW routera, przejdź do **CLOUD SERVICE** -> **GoodCloud** i kliknij **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Zostaniesz przekierowany na stronę **GL.iNet Account**. Kliknij **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    W wyskakującym oknie kliknij **Continue**. Zostaniesz przekierowany na stronę GoodCloud, aby dokończyć powiązanie.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Zaloguj się, aby powiązać urządzenie.

    Zaloguj się na swoje konto GL.iNet. Jeśli nie masz konta, załóż je i zaloguj się.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Po zalogowaniu potwierdź informacje o koncie i urządzeniu, w tym Device ID, model i adres MAC. Nadaj urządzeniu własną nazwę i kliknij **Bind** – router zostanie powiązany z Twoim kontem.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Jeśli nie otrzymasz wiadomości weryfikacyjnej, sprawdź folder spamu lub odczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com).

3. Szczegóły powiązania.

    Po pomyślnym powiązaniu wróć do panelu administracyjnego WWW routera i przejdź do **CLOUD SERVICES** -> **GoodCloud**. Na tej stronie wyświetlany jest odnośnik przekierowujący do platformy GoodCloud, dane identyfikacyjne urządzenia oraz najnowsze logi chmury.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Zdalny dostęp.

    W firmware v4.10 zdalny dostęp do panelu administracyjnego WWW i terminala routera jest domyślnie włączany po powiązaniu routera z GoodCloud.

5. Usuń powiązanie urządzenia.

    Jeśli chcesz usunąć powiązanie routera, zaloguj się do panelu administracyjnego WWW routera i przejdź do **CLOUD SERVICES** -> **GL.iNet Account**. Kliknij **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    Możesz też usunąć urządzenie z listy Bound Devices na platformie GoodCloud. Panel administracyjny WWW routera zsynchronizuje się i wyświetli aktualny stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com), aby uzyskać pomoc.

### Dla firmware od v4.7 do v4.9 {#for-firmware-v47-to-v49}

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego WWW routera i przejdź do **CLOUD SERVICE** -> **GoodCloud**.

    Kliknij przycisk **Get Started** – w prawym górnym rogu pojawi się wyskakujące okno Cloud Service. Kliknij **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. Zaloguj się, aby powiązać urządzenie.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Jeśli nie masz konta, załóż je i zaloguj się. Po zakończeniu rejestracji router zostanie automatycznie powiązany z Twoim kontem.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Jeśli nie otrzymasz wiadomości weryfikacyjnej, sprawdź folder spamu lub odczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com).

3. Szczegóły powiązania.

    Po pomyślnym powiązaniu wróć do panelu administracyjnego WWW routera i kliknij ikonę chmury w prawym górnym rogu. Zostaną wyświetlone szczegóły powiązania, w tym nazwa użytkownika, czas powiązania, Device ID, Device MAC i Device S/N.

    ![binding details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. Włącz zdalny dostęp.

    W panelu administracyjnym WWW przejdź do **CLOUD SERVICES** -> **GoodCloud**, gdzie możesz włączyć zdalny dostęp do routera.

    ![enable remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: umożliwia zdalny dostęp do terminala routera przez SSH z platformy GoodCloud.

    - **Remote Web Access**: umożliwia zdalny dostęp do panelu administracyjnego WWW routera przez HTTP/HTTPS z platformy GoodCloud.

    - **View Logs**: wyświetla logi wywołań API wykonanych przez GoodCloud.

5. Usuń powiązanie urządzenia.

    Jeśli chcesz usunąć powiązanie routera, zaloguj się do panelu administracyjnego WWW routera. Kliknij ikonę chmury w prawym górnym rogu, a następnie kliknij **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    Możesz też usunąć urządzenie z listy Bound Devices na platformie GoodCloud. Panel administracyjny WWW routera zsynchronizuje się i wyświetli aktualny stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com), aby uzyskać pomoc.

### Dla firmware v4.6 lub starszego {#for-firmware-v46-or-earlier}

1. Włącz GoodCloud.

    Zaloguj się do panelu administracyjnego WWW routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Włącz przełącznik, aby uruchomić GoodCloud.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    W razie potrzeby włącz **Remote SSH** i **Remote Web Access**, wybierz najbliższy serwer, przeczytaj i zaakceptuj **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: umożliwia zdalny dostęp do terminala routera przez SSH z platformy GoodCloud.

    - **Remote Web Access**: umożliwia zdalny dostęp do panelu administracyjnego WWW routera przez HTTP/HTTPS z platformy GoodCloud.

    - **Data Server**: wybierz serwer położony najbliżej lokalizacji urządzenia. Dostępne są trzy opcje: Azja i Pacyfik (Japonia), Ameryka (Oregon) i Europa (Irlandia).

2. Zarejestruj konto.

    Odwiedź [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, zarejestruj się i zaloguj.

    Jeśli nie otrzymasz wiadomości weryfikacyjnej, sprawdź folder spamu lub odczekaj kilka minut i spróbuj ponownie. Aby uzyskać dalszą pomoc, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com).

3. Dodaj urządzenia.

    Na platformie chmurowej przejdź do **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Istnieją trzy metody powiązania urządzenia z kontem GoodCloud: Auto Discover, Manually Add i Bulk Import.

    ??? "Auto Discover"

        Możesz użyć opcji **Auto discover**, jeśli router i urządzenie, z którego otwierasz stronę GoodCloud, znajdują się w tej samej sieci.

        Wybierz urządzenie z listy rozwijanej i wpisz **DDNS / Device ID**, który znajdziesz na spodzie routera lub na stronie GoodCloud w panelu administracyjnym WWW.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Informacje o tym, gdzie znaleźć Device ID, znajdziesz pod [tym linkiem](../faq/where_to_find_the_device_id_mac_sn.md).

    ??? "Manually Add"

        Jeśli urządzenia nie ma na liście, kliknij **Manually add** i wprowadź dane routera. Wszystkie wymagane informacje znajdziesz na spodzie routera lub na stronie GoodCloud w panelu administracyjnym WWW.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** jest przeznaczony dla użytkowników zarządzających dużą liczbą urządzeń. Możesz zaimportować wiele urządzeń za pomocą pliku Microsoft Excel.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Szczegóły powiązania.

    Po pomyślnym powiązaniu wróć do panelu administracyjnego WWW routera i przejdź do **APPLICATIONS** -> **GoodCloud**. Na tej stronie wyświetlane są szczegóły powiązania, w tym nazwa użytkownika i czas powiązania.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. Usuń powiązanie urządzenia.

    Jeśli chcesz usunąć powiązanie routera, zaloguj się do panelu administracyjnego WWW routera, przejdź do **APPLICATION** -> **GoodCloud** i kliknij **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    Możesz też usunąć urządzenie z listy Bound Devices na platformie GoodCloud. Panel administracyjny WWW routera zsynchronizuje się i wyświetli aktualny stan powiązania.

    Jeśli napotkasz jakiekolwiek trudności, wyślij wiadomość na adres [support@gl-inet.com](mailto:support@gl-inet.com), aby uzyskać pomoc.

## Zarządzanie urządzeniami {#manage-devices}

### Informacje o systemie i działania {#system-info-and-actions}

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** możesz wyświetlić informacje o systemie (np. model, wersję, adres MAC, adres IP) oraz stan (np. online, offline) wszystkich urządzeń powiązanych z Twoim kontem.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Po wybraniu urządzenia możesz w prawym górnym rogu wykonywać działania, takie jak zmiana ustawień, aktualizacja firmware, zdalny dostęp do urządzenia, ponowne uruchomienie lub reset.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Kliknij ikonę koła zębatego po prawej stronie nagłówka listy, aby dostosować wyświetlane kolumny i ich kolejność oraz skupić się na najważniejszych informacjach o urządzeniach.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Szczegóły urządzenia {#device-details}

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kliknij nazwę urządzenia, aby przejść do strony szczegółów urządzenia. Wyświetlane są na niej m.in. podstawowe informacje o routerze, dane statystyczne, ustawienia sieci i lista klientów.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Podstawowe informacje {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statystyki {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Ustawienia sieci {#network-settings}

Na tej stronie wyświetlana jest konfiguracja sieci i ustawienia Wi-Fi routera.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Lista klientów {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Zdalny dostęp {#remote-access}

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kliknij nazwę urządzenia, do którego chcesz uzyskać dostęp, aby otworzyć stronę szczegółów. Działania zdalne są dostępne w prawym górnym rogu.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

Kliknij **Remote GUI**, aby zdalnie uzyskać dostęp do panelu administracyjnego WWW routera.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Jeśli ta opcja jest wyszarzona lub niedostępna, prawdopodobnie funkcja jest wyłączona. Najpierw włącz ją w panelu administracyjnym WWW routera, a dopiero potem uzyskaj dostęp przez GoodCloud.

Jeśli opcję można kliknąć, ale nie reaguje, spróbuj użyć trybu incognito/InPrivate przeglądarki.

### Remote SSH {#remote-ssh}

Kliknij **Remote SSH**, aby zdalnie uzyskać dostęp do terminala routera przez SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Jeśli ta opcja jest wyszarzona lub niedostępna, prawdopodobnie funkcja jest wyłączona. Najpierw włącz ją w panelu administracyjnym WWW routera, a dopiero potem uzyskaj dostęp przez GoodCloud.

Jeśli opcję można kliknąć, ale nie reaguje, spróbuj użyć trybu incognito/InPrivate przeglądarki.

## Zmiana ustawień {#modify-settings}

Możesz skonfigurować wiele parametrów dla pojedynczego urządzenia lub dla wielu urządzeń jednocześnie.

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** wybierz urządzenie, które chcesz skonfigurować, a następnie w prawym górnym rogu kliknij **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

W tym miejscu możesz sprawdzić i zmienić ustawienia sieciowe routera, w tym ustawienia sieci bezprzewodowej, Ethernet, zabezpieczeń, przekierowania portów, sieci LAN i systemu.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Powiadomienia e-mail {#email-alarm}

Możesz skonfigurować powiadomienie e-mail wysyłane, gdy zmieni się stan urządzenia (online/offline) lub połączą się nowi klienci.

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** kliknij przycisk **Add Rule** w prawym górnym rogu.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Wybierz urządzenie, które chcesz monitorować, i kliknij **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Wybierz zdarzenie wyzwalające, np. zmianę stanu online/offline urządzenia, i kliknij **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Sprawdź ustawienia reguły i kliknij **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Na liście Notifications możesz przeglądać utworzone reguły powiadomień. Użytkownicy indywidualni mogą utworzyć tylko jedną regułę powiadomień. Jeśli potrzebujesz zbiorczego zarządzania urządzeniami, skontaktuj się z nami, aby rozszerzyć swój plan.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site-to-site {#site-to-site}

Zapoznaj się z artykułem [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud i VPN {#goodcloud-and-vpn}

Jeśli na routerze jednocześnie włączysz **GoodCloud** i **klienta VPN**, połączenie między routerem a serwerem GoodCloud domyślnie nie przechodzi przez VPN. Zapewnia to stabilniejsze połączenie z usługami GoodCloud.

Jeśli jednak chcesz, aby połączenie z GoodCloud przechodziło przez VPN, możesz zmienić to ustawienie w panelu administracyjnym WWW routera. Przejdź do VPN -> VPN Dashboard -> VPN Client -> Options i włącz opcję „Services from GL.iNet Use VPN”.

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Pamiętaj, że kierowanie ruchu GoodCloud przez VPN może obniżyć stabilność połączenia z chmurą, zwłaszcza jeśli:

* Połączenie VPN jest niestabilne
* Dostawca VPN filtruje lub blokuje ruch GoodCloud
* VPN znacząco zwiększa opóźnienie połączenia

Zasadniczo zaleca się pozostawienie ustawień domyślnych, w których ruch GoodCloud omija VPN, aby zapewnić optymalną wydajność i niezawodność.

## Wyświetlanie logów {#view-logs}

W razie potrzeby możesz przeglądać logi GoodCloud, w tym Activity Logs, Device Logs, Upgrade Logs, Alert Logs i Device Settings Logs.

W [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** wybierz z listy rozwijanej logi, które chcesz wyświetlić.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Wyłączanie chmury {#disable-cloud}

Jeśli nie chcesz już, aby urządzenie było połączone z platformą chmurową, możesz wyłączyć usługę chmurową w panelu administracyjnym WWW routera.

??? "Dla firmware v4.6 lub starszego"

    Zaloguj się do panelu administracyjnego WWW routera, przejdź do **APPLICATIONS** -> **GoodCloud**, wyłącz przełącznik GoodCloud i kliknij **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Po wyłączeniu interfejs będzie wyglądał następująco.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Dla firmware v4.7 lub nowszego"

    Zaloguj się do panelu administracyjnego WWW routera i kliknij ikonę chmury w prawym górnym rogu. W wyskakującym oknie **Cloud Service** kliknij ikonę koła zębatego i wybierz **Disable**.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Po wyłączeniu interfejs będzie wyglądał następująco.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Usuwanie konta {#delete-account}

Ze względów bezpieczeństwa możesz usunąć konto, jeśli nie jest już używane.

Na platformie [GoodCloud](https://www.goodcloud.xyz){target="_blank"} kliknij nazwę użytkownika w prawym górnym rogu i wybierz **Personal Center**. Przewiń na dół strony i kliknij **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Usunięcie konta spowoduje trwałe usunięcie wszystkich powiązanych usług, danych i informacji osobistych bez możliwości ich odzyskania.

    Jeśli Twoje konto należy do jakiejkolwiek organizacji, przed usunięciem konta opuść wszystkie organizacje.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
