# Firmware v4.11

Ta wersja koncentruje się na usprawnieniu monitorowania jakości sieci i oceny bezpieczeństwa, pomagając wykrywać problemy z łącznością oraz potencjalne zagrożenia. Wprowadza także nowe funkcje Mesh, konta GL.iNet i VLAN oraz istotne ulepszenia DNS, SQM, QoS i statystyk ruchu.

Najnowsze oprogramowanie układowe można pobrać z [Centrum pobierania oprogramowania](https://dl.gl-inet.com/){target="_blank"}.

## Jakość sieci

[Jakość sieci](../interface_guide/network_quality.md) to nowa funkcja monitorująca połączenie internetowe w czasie rzeczywistym. Ocenia szybkość reakcji, opóźnienia i wydajność DNS oraz wykrywa przerwy w połączeniu i utratę pakietów. Pomaga to identyfikować niestabilność sieci i problemy z łącznością, których same testy przepustowości mogą nie ujawnić.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Skanowanie bezpieczeństwa

[Skanowanie bezpieczeństwa](../interface_guide/security_scan.md) to nowa funkcja oceniająca ustawienia zabezpieczeń routera i przedstawiająca ocenę bezpieczeństwa, ostrzeżenia o zagrożeniach oraz sugestie optymalizacji. Sprawdza między innymi zabezpieczenia Wi-Fi, ping od strony WAN, zdalny dostęp SSH, przekierowanie portów i ochronę treści DPI, pomagając wykrywać i usuwać potencjalne zagrożenia. Skanowanie rozpoczyna się automatycznie po otwarciu strony. Możesz też kliknąć ikonę oceny, aby zresetować skanowanie i uruchomić je ponownie.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md) to funkcja oparta na standardzie Wi-Fi EasyMesh™, która rozszerza zasięg Wi-Fi w całym domu i umożliwia płynny roaming. Jeśli masz kilka routerów GL.iNet, ustaw jeden jako router główny, a pozostałe jako węzły mesh, aby korzystać z płynnego roamingu Wi-Fi w całym domu.

**Uwaga**: Ta funkcja została najpierw udostępniona w wybranych modelach, a w firmware v4.11 rozszerzono jej dostępność na kolejne modele.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## Konto GL.iNet

[Konto GL.iNet](../interface_guide/glinet_account.md) zapewnia jednolity dostęp do urządzeń i usług chmurowych. Jedno konto GL.iNet pozwala wygodnie korzystać z GoodCloud i aplikacji GL.iNet, ułatwiając zarządzanie siecią i urządzeniami. Ponadto dzięki GoodPAS możesz szybko nawiązać bezpieczne połączenie między routerem podróżnym a siecią domową i korzystać ze zdalnego dostępu poza domem.

**Uwaga**: Ta funkcja została najpierw udostępniona w wybranych modelach, a w firmware v4.11 rozszerzono jej dostępność na kolejne modele.

![GL.iNet Account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md) to rozwiązanie do zdalnego dostępu oparte na protokole AmneziaWG z wbudowanym maskowaniem ruchu. Umożliwia bezpieczne połączenie routera podróżnego z siecią domową za pomocą dynamicznego kodu dostępu, bez rejestracji ani logowania.

**Uwaga**: Ta funkcja została najpierw udostępniona w wybranych modelach, a w firmware v4.11 rozszerzono jej dostępność na kolejne modele.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md) umożliwia zdalny dostęp do routerów GL.iNet i ich scentralizowane zarządzanie. Możesz zarządzać urządzeniami zbiorczo, wdrażać konfiguracje sieci, aktualizować firmware oraz uzyskiwać zdalny dostęp do panelu administracyjnego WWW routera lub terminala SSH.

**Uwaga**: Ta funkcja została najpierw udostępniona w wybranych modelach, a w firmware v4.11 rozszerzono jej dostępność na kolejne modele.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Ethernet Port

Strona [Ethernet Port](../interface_guide/ethernet_port_v4.10.md) wyświetla wszystkie interfejsy routera. Możesz sprawdzać stan połączenia każdego interfejsu, zarządzać rolami portów Ethernet (WAN lub LAN) oraz przeglądać szczegóły portów, takie jak adres MAC, wynegocjowana prędkość i bieżący stan łącza. Możesz również przypisywać interfejsy fizyczne do utworzonych podsieci.

**Uwaga**: Ta funkcja została najpierw udostępniona w wybranych modelach, a w firmware v4.11 rozszerzono jej dostępność na kolejne modele.

Poniższa ilustracja przedstawia stronę Ethernet Port na routerze Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

Ta wersja usprawnia konfigurację [DNS](../interface_guide/dns_v4.11.md), łącząc WAN DNS, VPN DNS i Manual DNS na jednej stronie. Możesz łatwo sprawdzać stan DNS dla każdego typu połączenia, konfigurować niestandardowe serwery DNS i wybierać, czy ręczne ustawienia DNS mają być stosowane do tuneli VPN, czy do samego routera.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

W tej wersji firmware ulepszono [QoS](../interface_guide/qos.md) (Quality of Service). Dodano opcję **Run Speedtest** dla przepustowości WAN, która mierzy przepustowość pobierania i wysyłania przez WAN oraz automatycznie wypełnia odpowiednie pola. Dostępne są trzy polityki planowania ruchu, w tym nowo wprowadzone **Device Priority** i **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Wybrane lokalne urządzenia klienckie otrzymują wyższy priorytet sieciowy podczas przeciążenia WAN.

- **Application Priority**: Ustaw niestandardowe priorytety dla różnych aplikacji, a router odpowiednio przydzieli przepustowość.

- **Advanced QoS**: Twórz zaawansowane reguły QoS dla ruchu o wysokim priorytecie.

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) udostępnia opcję **Run Speedtest** dla przepustowości WAN, która mierzy prędkość pobierania i wysyłania oraz automatycznie wypełnia odpowiednie pola. Dla mechanizmu kolejkowania **cake** nowa funkcja **Cake Autorate** dynamicznie dostosowuje skonfigurowaną przepustowość na podstawie RTT pakietów testowych. Korzysta z lekkich testów ping zamiast aktywnych testów prędkości i jest zalecana dla połączeń WAN o zmiennej przepustowości.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## Statystyki danych

[Statystyki danych](../interface_guide/data_statistics.md) obsługują teraz filtrowanie ruchu według urządzenia klienckiego i oferują nowe widoki wykresów, w tym wykresy słupkowe i kołowe. Podczas przeglądania statystyk ruchu aplikacji możesz wybrać konkretne urządzenie klienckie i przełączać widoki wykresów, aby łatwiej analizować zużycie danych.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
