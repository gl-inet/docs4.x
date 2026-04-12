# Połączenie z Internetem przez Tethering USB

Udostępnianie połączenia sieciowego ze smartfona do routera za pomocą kabla USB nazywa się Tethering. Modem host-less również działa w trybie Tethering podczas konfiguracji modemu.

**Uwaga:** Niektórzy operatorzy komórkowi ograniczają tethering lub pobierają za niego dodatkowe opłaty. Zalecamy sprawdzić to u swojego operatora.

## Konfiguracja

=== "iPhone"

    1. Podłącz iPhone'a do portu USB routera za pomocą kabla USB. Pojawi się okno systemowe z pytaniem, czy zaufać urządzeniu. Stuknij **Trust**, aby kontynuować.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Na iPhonie przejdź do **Settings** -> **Personal Hotspot**. Włącz **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Podłącz komputer lub inny telefon do routera, a następnie zaloguj się do panelu administracyjnego WWW routera, przejdź do **INTERNET** -> **Tethering** i kliknij **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        Jeśli chcesz skonfigurować ustawienia zaawansowane, takie jak TTL, HL i MTU, kliknij **Advanced**, dostosuj te ustawienia, a następnie kliknij **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        Rozpocznie się nawiązywanie połączenia.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Po nawiązaniu połączenia stan hotspotu osobistego, na przykład liczba podłączonych urządzeń, będzie widoczny na pasku stanu u góry ekranu telefonu.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Panel administracyjny WWW również wyświetli stan połączenia Tethering.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Podłącz telefon z Androidem do portu USB routera za pomocą kabla USB. Może pojawić się okno systemowe z pytaniem o preferencje USB. Jeśli zostaniesz o to poproszony, wybierz **USB Tethering** lub **File Transfer**.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. W telefonie przejdź do **Settings** -> **Network & Internet** -> **Personal Hotspot**. Włącz **Personal Hotspot** lub **USB Tethering**.

        (Kroki włączania USB Tethering różnią się w zależności od marki. Sprawdź dokładną lokalizację tej opcji w ustawieniach urządzenia, a w razie potrzeby skontaktuj się ze wsparciem producenta.)

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Podłącz komputer lub inny telefon do routera, a następnie zaloguj się do panelu administracyjnego WWW routera, przejdź do **INTERNET** -> **Tethering** i kliknij **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        Jeśli chcesz skonfigurować ustawienia zaawansowane, takie jak TTL, HL i MTU, kliknij **Advanced**, dostosuj te ustawienia, a następnie kliknij **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        Rozpocznie się nawiązywanie połączenia.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Po nawiązaniu połączenia stan hotspotu osobistego, na przykład liczba podłączonych urządzeń, będzie widoczny na pasku stanu u góry ekranu telefonu.

        Panel administracyjny WWW również wyświetli stan połączenia Tethering.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Oficjalną dokumentację Androida znajdziesz tutaj: [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Ostrzeżenie

Gdy dostęp do Internetu nie jest dostępny, zostanie wyświetlone odpowiednie ostrzeżenie:

**"The interface is connected, but the Internet can't be accessed."**

Rozwiązania:

1. Sprawdź, czy smartfon ma dostęp do Internetu.

2. Przejdź na stronę [Multi-WAN](multi-wan.md), aby sprawdzić, czy dostęp do Internetu jest możliwy.

## Rozwiązywanie problemów

Jeśli połączenie się nie powiedzie, wypróbuj poniższe kroki:

- Użyj oryginalnego zasilacza routera.
- Odłącz kabel USB i podłącz go ponownie.
- Użyj innego kabla USB. Upewnij się, że obsługuje przesył danych, a nie tylko ładowanie.
- Kilka razy wyłącz i włącz opcję "USB Tethering" (na telefonie z Androidem).
- Kilka razy wyłącz i włącz opcję "Allow Others to Join" (na iPhonie).
- Uruchom ponownie smartfon i spróbuj ponownie.

---

Powiązane artykuły

- [Strona Internet](internet.md)
- [Jak ustawić priorytet dla każdej metody dostępu do Internetu?](multi-wan.md)
- [Jak ustawić równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu do Internetu?](multi-wan.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
