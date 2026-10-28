# Firmware v4.11 {#firmware-v411}

Ta wersja koncentruje się na usprawnieniu monitorowania jakości sieci i oceny bezpieczeństwa, pomagając wykrywać problemy z łącznością oraz potencjalne zagrożenia. Usprawnia także DNS, QoS, SQM i statystyki danych, zapewniając bardziej elastyczne zarządzanie siecią i kontrolę ruchu.

Najnowsze oprogramowanie układowe można pobrać z [Centrum pobierania oprogramowania](https://dl.gl-inet.com/){target="_blank"}.

## Jakość sieci {#network-quality}

[Jakość sieci](../interface_guide/network_quality.md) to nowa funkcja monitorująca połączenie internetowe w czasie rzeczywistym. Ocenia szybkość reakcji, opóźnienia i wydajność DNS oraz wykrywa przerwy w połączeniu i utratę pakietów. Pomaga to identyfikować niestabilność sieci i problemy z łącznością, których same testy przepustowości mogą nie ujawnić.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Skanowanie bezpieczeństwa {#security-scan}

[Skanowanie bezpieczeństwa](../interface_guide/security_scan.md) to nowa funkcja oceniająca ustawienia zabezpieczeń routera i przedstawiająca ocenę bezpieczeństwa, ostrzeżenia o zagrożeniach oraz sugestie optymalizacji. Sprawdza między innymi zabezpieczenia Wi-Fi, ping od strony WAN, zdalny dostęp SSH, przekierowanie portów i ochronę treści DPI, pomagając wykrywać i usuwać potencjalne zagrożenia. Skanowanie rozpoczyna się automatycznie po otwarciu strony. Możesz też kliknąć ikonę oceny, aby zresetować skanowanie i uruchomić je ponownie.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

[UPnP](../interface_guide/upnp.md) pozwala zgodnym urządzeniom LAN i aplikacjom automatycznie żądać mapowania portów bez ręcznej konfiguracji przekierowania portów. Ułatwia to połączenia w grach online, udostępnianiu plików peer-to-peer i dostępie zdalnym. Na stronie UPnP można wyświetlać aktywne mapowania, sprawdzać pozostały czas dzierżawy i usuwać mapowania w razie potrzeby.

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

Ta wersja usprawnia konfigurację [DNS](../interface_guide/dns_v4.11.md), łącząc WAN DNS, VPN DNS i Manual DNS na jednej stronie. Możesz łatwo sprawdzać stan DNS dla każdego typu połączenia, konfigurować niestandardowe serwery DNS i wybierać, czy ręczne ustawienia DNS mają być stosowane do tuneli VPN, czy do samego routera.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) udostępnia opcję **Run Speedtest** dla przepustowości WAN, która mierzy prędkości pobierania i wysyłania oraz automatycznie wypełnia odpowiednie pola. Oprócz Application Priority ta wersja dodaje dwie polityki planowania ruchu: **Device Priority** i **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Wybrane lokalne urządzenia klienckie otrzymują wyższy priorytet sieciowy podczas przeciążenia WAN.

- **Application Priority**: Ustaw niestandardowe priorytety dla różnych aplikacji, a router odpowiednio przydzieli przepustowość.

- **Advanced QoS**: Twórz zaawansowane reguły QoS dla ruchu o wysokim priorytecie.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) udostępnia opcję **Run Speedtest** dla przepustowości WAN, która mierzy prędkości pobierania i wysyłania oraz automatycznie wypełnia odpowiednie pola. Dostępne są dwa mechanizmy kolejkowania: **cake** i **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: inteligentne, automatyczne kształtowanie ruchu zapewniające najlepszą ogólną kontrolę opóźnień (zalecane).

    W tym mechanizmie nowa funkcja **Cake Autorate** dynamicznie dostosowuje skonfigurowaną przepustowość na podstawie RTT pakietów testowych. Korzysta z lekkich testów ping zamiast aktywnych testów prędkości i jest zalecana dla połączeń WAN o zmiennej przepustowości.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: proste i wydajne sprawiedliwe kolejkowanie z podstawową redukcją opóźnień.

## Statystyki danych {#data-statistics}

[Statystyki danych](../interface_guide/data_statistics.md) obsługują teraz filtrowanie ruchu według urządzenia klienckiego i oferują nowe widoki wykresów, w tym wykresy słupkowe i kołowe. Podczas przeglądania statystyk ruchu aplikacji możesz wybrać konkretne urządzenie klienckie i przełączać widoki wykresów, aby łatwiej analizować zużycie danych.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
