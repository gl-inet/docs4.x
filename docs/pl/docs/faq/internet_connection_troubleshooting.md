# FAQ rozwiązywania problemów z połączeniem internetowym {#internet-connection-troubleshooting-faq}

## P1. Co zrobić, jeśli nie mam dostępu do Internetu? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Wykonaj poniższe kroki, aby przeprowadzić podstawowe rozwiązywanie problemów.

1. Sprawdź połączenie fizyczne.

    Upewnij się, że kabel Ethernet jest prawidłowo podłączony między portem WAN routera a urządzeniem nadrzędnym (np. modemem, ONT lub gniazdem Ethernet). Sprawdź diody LED na urządzeniu nadrzędnym i upewnij się, że transmisja jest aktywna.

2. Uruchom ponownie urządzenia.

    Wyłącz urządzenie nadrzędne (np. modem) oraz router. Odczekaj 1–2 minuty. Następnie najpierw włącz modem, poczekaj, aż w pełni się uruchomi, a dopiero potem włącz router.

3. Sprawdź adres IP WAN.

    Zaloguj się do panelu administracyjnego routera i przejdź do sekcji **INTERNET** -> **Ethernet**. Jeśli połączenie utknęło w stanie łączenia, jak pokazano poniżej, przyczyną może być problem z DHCP, wiązanie MAC albo wymagany identyfikator VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Skontaktuj się z dostawcą Internetu i sprawdź, czy do uzyskania dostępu do Internetu potrzebujesz **PPPoE username**, **PPPoE password** oraz **VLAN ID**.

    Jednocześnie sprawdź, czy dostawca wcześniej skonfigurował **MAC binding** na modemie/ONT.

## P2. Kiedy należy sklonować adres MAC? {#q2-when-should-i-clone-a-mac-address}

Niektórzy dostawcy Internetu przypisują połączenie szerokopasmowe do adresu MAC pierwszego podłączonego urządzenia, zwykle starego routera albo komputera. Po wymianie routera trzeba sklonować adres MAC, aby przywrócić dostęp do Internetu.

Wykonaj poniższe kroki, aby sklonować adres MAC do routera GL.iNet.

1. Zanotuj adres MAC starego routera (lub komputera wcześniej powiązanego z łączem).

2. Zaloguj się do panelu administracyjnego routera i przejdź do **NETWORK** -> **Ethernet Port** (w niektórych wersjach firmware sekcja nazywa się **Port Management**). Ustaw **MAC Mode** na **Clone** lub **Manual**, ręcznie wpisz adres MAC, a następnie kliknij **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Uruchom ponownie modem (czyli urządzenie nadrzędne).

## P3. Kiedy trzeba skonfigurować VLAN ID? {#q3-when-do-i-need-to-configure-a-vlan-id}

Niektórzy dostawcy wymagają tagowania VLAN do uwierzytelniania połączenia internetowego lub separacji ruchu, zwłaszcza przy łączach światłowodowych i IPTV. Skontaktuj się z dostawcą i sprawdź, czy wymagany jest VLAN ID.

Wykonaj poniższe kroki, aby skonfigurować VLAN ID.

1. Zaloguj się do routera i przejdź do sekcji **INTERNET** -> **Ethernet**. Kliknij **Modify**.

2. Wprowadź VLAN ID podany przez dostawcę Internetu, a następnie kliknij **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## P4. Co zrobić, jeśli nadal nie działa? {#q4-what-if-it-still-doesnt-work}

Jeśli problem nadal występuje, spróbuj podłączyć komputer stacjonarny lub laptop bezpośrednio do modemu i sprawdź, czy masz dostęp do Internetu.

Jeśli nie masz dostępu do Internetu, problem może leżeć po stronie dostawcy Internetu. Skontaktuj się z nim, aby uzyskać dalszą pomoc.

Jeśli masz dostęp do Internetu, problem może być związany z konfiguracją routera. Skontaktuj się z naszym wsparciem technicznym pod adresem [support@gl-inet.com](mailto:support@gl-inet.com) i podaj następujące informacje:

- Model routera
- Kroki rozwiązywania problemów, które już wykonano
- Nazwę dostawcy Internetu
- Wszelkie inne informacje, które Twoim zdaniem mogą pomóc nam w udzieleniu wsparcia

## Informacje o ISP {#isp-information}

Poniżej znajduje się zestawienie informacji o dostawcach Internetu według regionów, opracowane przez GL.iNet na podstawie opinii klientów, forów i zasobów OpenWrt. Materiał ma wyłącznie charakter informacyjny.

| Kraj/region   | ISP   | Typ połączenia | VLAN ID | Wymagane klonowanie MAC | Dodatkowe wymagania |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| Stany Zjednoczone | AT&T Fiber | DHCP (IP Passthrough) | N/A | Nie | Wymagane włączenie IP Passthrough; konieczne obejście uwierzytelniania EAP |
| Stany Zjednoczone | Spectrum | DHCP | N/A | Tak (w niektórych regionach) | Ścisłe wiązanie MAC (wymagany restart modemu) |
| Stany Zjednoczone | Verizon Fios | DHCP | N/A | Nie | |
| Stany Zjednoczone | Comcast Xfinity | DHCP | N/A | Tak (często) | Po zmianie routera należy zrestartować modem (zwolnienie adresu MAC) |
| Stany Zjednoczone | Cox Communications | DHCP | N/A | Tak | Po zmianie routera należy zrestartować modem (zwolnienie adresu MAC) |
| Stany Zjednoczone | Frontier Fiber | DHCP | N/A | Nie | |
| Stany Zjednoczone | CenturyLink / Lumen | PPPoE | 201 | Nie | W niektórych regionach wymagane są sieci VLAN. |
| Kanada | Bell Canada Fibe | PPPoE | 35 | Nie | |
| Niemcy | Deutsche Telekom | PPPoE | 7 | Nie | VLAN 7 obowiązkowy dla dostępu do Internetu; wymagane dane logowania PPPoE |
| Niemcy | Vodafone (Kabel) | DHCP | N/A | Tak (czasami) | Możliwe wiązanie MAC; po zmianie routera zrestartuj modem |
| Niemcy | 1&1 / O2 (Telekom line) | PPPoE | 7 | Nie | VLAN 7 obowiązkowy dla dostępu do Internetu |
| Niemcy | DNS:NET | PPPoE | 37 | Nie | |
| Niemcy | o2(UGG) | PPPoE | 7 | Nie | |
| Wielka Brytania | BT Broadband | PPPoE | 101 | Nie | Wymagany VLAN 101; konieczne logowanie PPPoE |
| Wielka Brytania | Sky Broadband | DHCP (Option 61) | 101 | Nie | Wymaga DHCP Option 61 (identyfikator klienta) |
| Wielka Brytania | Virgin | DHCP | N/A | Tak | Modem działa w trybie mostu i wymaga klonowania MAC. |
| Francja | Orange | DHCP / PPPoE | 832 | Nie | Wymagany VLAN 832; może być wymagane uwierzytelnianie Option 90 |
| Francja | Free (Freebox) | DHCP | N/A | Nie | |
| Francja | Bouygues Telecom | DHCP | 100 | Tak | Sklonuj adres MAC urządzenia Bbox |
| Hiszpania | Movistar | PPPoE | 6 | Nie | VLAN 6 (Internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Hiszpania | DIGI | PPPoE | 20 | Nie | |
| Hiszpania | Orange | DHCP | 832/835 | Nie | Identyfikatory VLAN mogą się różnić w zależności od regionu |
| Włochy | TIM | PPPoE | 835 | Nie | Wymagany VLAN 835 |
| Włochy | Aruba | PPPoE | 835 | Nie | |
| Holandia | KPN | DHCP | 6 | Nie | VLAN 6 wymagany dla dostępu do Internetu |
| Holandia | Tweak | DHCP | 34 | Tak | Sklonuj adres MAC urządzenia Experia Box |
| Holandia | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | Nie | |
| Holandia | Odido | DHCP | 300 | Nie | |
| Belgia | EDPnet | PPPoE | 10 | Nie | |
| Bośnia i Hercegowina | BH Telecom | PPPoE | 100 | Nie | |
| Chorwacja | Terrakom | PPPoE | 905 | Nie | |
| Czechy | O2 | PPPoE | 848 | Nie | |
| Cypr | Epic | PPPoE | 35 | Nie | |
| Cypr | Cyta | PPPoE | 42 | Nie | |
| Cypr | Cablenet | PPPoE | 42 | Nie | |
| Cypr | Primetel | PPPoE | 42 | Nie | |
| Polska | Orange Polska | PPPoE | 35 | Nie | Wymagany VLAN 35 |
| Polska | T-mobile | PPPoE | 35 | Nie | |
| Irlandia | Vodafone SIRO | PPPoE | 10 | Nie | |
| Irlandia | Pure Telecom | PPPoE | 10 | Nie | |
| Austria | A1 Telekom | PPPoE | 2 | Nie | |
| Austria | Fonira | PPPoE | 31 | Nie | |
| Turcja | Turknet | PPPoE | 35 | Nie | |
| Turcja | Turk Telekom | PPPoE | 35 | Nie | |
| Turcja | Turkcell Superonline | PPPoE | N/A | Tak | |
| Turcja | Turksat Kablonet | DHCP/PPPoE | N/A | Nie | |
| Grecja | Cosmote | PPPoE | 835 | Nie | |
| Grecja | Nova | PPPoE | 835 | Tak | |
| Grecja | DEI/PPC | DHCP | 835 | Nie | |
| Japonia | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | Nie | IPoE wymaga routera zgodnego z MAP-E/DS-Lite |
| Japonia | SoftBank Hikari | PPPoE / IPoE | N/A | Nie | Często używana jest usługa IPoE firmy BBIX |
| Indie | Airtel | PPPoE / DHCP | N/A | Nie | W niektórych regionach wymagane jest PPPoE |
| Indie | JioFiber | DHCP | N/A | Nie | W wielu przypadkach ONT jest zablokowany |
| Singapur | Singtel | PPPoE | 10 | Nie | Wymagany VLAN 10; IPTV w osobnej sieci VLAN |
| Singapur | StarHub | DHCP | N/A | Nie | Połączenie oparte na DHCP |
| Australia | NBN (różni dostawcy) | PPPoE / DHCP | 2 (często) | Tak | VLAN 2 jest powszechny, ale zależy od dostawcy |
