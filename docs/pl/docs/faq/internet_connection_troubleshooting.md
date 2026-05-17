# FAQ rozwiązywania problemów z połączeniem internetowym

## P1. Co zrobić, jeśli nie mam dostępu do Internetu?

Wykonaj poniższe kroki, aby przeprowadzić podstawowe rozwiązywanie problemów.

1. Sprawdź połączenie fizyczne.

    Upewnij się, że kabel Ethernet jest prawidłowo podłączony między portem WAN routera a urządzeniem nadrzędnym (np. modemem, ONT lub gniazdem Ethernet). Sprawdź diody LED na urządzeniu nadrzędnym i upewnij się, że transmisja jest aktywna.

2. Uruchom ponownie urządzenia.

    Wyłącz urządzenie nadrzędne (np. modem) oraz router. Odczekaj 1–2 minuty. Następnie najpierw włącz modem, poczekaj, aż w pełni się uruchomi, a dopiero potem włącz router.

3. Sprawdź adres IP WAN.

    Zaloguj się do panelu administracyjnego routera i przejdź do sekcji **INTERNET** -> **Ethernet**. Jeśli połączenie utknęło w stanie łączenia, jak pokazano poniżej, przyczyną może być problem z DHCP, wiązanie MAC albo wymagany identyfikator VLAN.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Skontaktuj się z dostawcą Internetu i sprawdź, czy do uzyskania dostępu do Internetu potrzebujesz **PPPoE username**, **PPPoE password** oraz **VLAN ID**.

    Jednocześnie sprawdź, czy dostawca nie skonfigurował wcześniej **MAC binding** na modemie/ONT.

## P2. Kiedy należy sklonować adres MAC?

Niektórzy dostawcy Internetu przypisują połączenie szerokopasmowe do adresu MAC pierwszego podłączonego urządzenia, zwykle starego routera albo komputera. Po wymianie routera trzeba sklonować adres MAC, aby przywrócić dostęp do Internetu.

Wykonaj poniższe kroki, aby sklonować adres MAC do routera GL.iNet.

1. Zanotuj adres MAC starego routera (lub komputera wcześniej powiązanego z łączem).

2. Zaloguj się do panelu administracyjnego routera i przejdź do **NETWORK** -> **Ethernet Port** (w niektórych wersjach firmware sekcja nazywa się **Port Management**). Ustaw **MAC Mode** na **Clone** lub **Manual**, ręcznie wpisz adres MAC, a następnie kliknij **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Uruchom ponownie modem (czyli urządzenie nadrzędne).

## P3. Kiedy trzeba skonfigurować VLAN ID?

Niektórzy dostawcy wymagają tagowania VLAN do uwierzytelniania połączenia internetowego lub separacji ruchu, zwłaszcza przy łączach światłowodowych i IPTV. Skontaktuj się z dostawcą i sprawdź, czy wymagany jest VLAN ID.

Wykonaj poniższe kroki, aby skonfigurować VLAN ID.

1. Zaloguj się do routera i przejdź do sekcji **INTERNET** -> **Ethernet**. Kliknij **Modify**.

2. Wprowadź VLAN ID podany przez dostawcę Internetu, a następnie kliknij **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## P4. Co zrobić, jeśli nadal nie działa?

Jeśli problem nadal występuje, spróbuj podłączyć komputer stacjonarny lub laptop bezpośrednio do modemu i sprawdź, czy masz dostęp do Internetu.

Jeśli nie masz dostępu do Internetu, problem może leżeć po stronie dostawcy Internetu. Skontaktuj się z nim, aby uzyskać dalszą pomoc.

Jeśli masz dostęp do Internetu, problem może być związany z konfiguracją routera. Skontaktuj się z naszym wsparciem technicznym pod adresem [support@gl-inet.com](mailto:support@gl-inet.com) i podaj następujące informacje:

- Model routera
- Kroki rozwiązywania problemów, które już wykonano
- Nazwę dostawcy Internetu
- Wszelkie inne informacje, które Twoim zdaniem mogą pomóc nam w udzieleniu wsparcia

## Informacje o ISP

Poniżej znajduje się zestawienie informacji o dostawcach Internetu według regionów, opracowane przez GL.iNet na podstawie opinii klientów, forów i zasobów OpenWrt. Materiał ma wyłącznie charakter informacyjny.

| Kraj/region   | ISP   | Connection Type | VLAN ID | MAC Clone Required | Additional Requirements |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| United States    | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Must enable IP Passthrough; EAP authentication bypass needed |
| United States | Spectrum | DHCP | N/A | Yes (in some areas) | Strong MAC binding (modem reboot required) |
| United States | Verizon Fios | DHCP | N/A | No | | 
| United States | Comcast Xfinity | DHCP | N/A | Yes (common) | Must reboot modem when changing router (MAC release) |
| United States | Cox Communications | DHCP | N/A | Yes | Must reboot modem when changing router (MAC release) |
| United States | Frontier Fiber | DHCP | N/A | No | |
| United States | CenturyLink / Lumen | PPPoE | 201 | No | VLANs are required in certain areas. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germany | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 mandatory for internet; PPPoE credentials required |
| Germany | Vodafone (Kabel) | DHCP | N/A | Yes (sometimes) | MAC binding may apply; reboot modem after router change |
| Germany | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 mandatory for internet |
| Germany | DNS:NET | PPPoE | 37 | No | |
| Germany | o2(UGG) | PPPoE | 7 | No | |
| United Kingdom | BT Broadband | PPPoE | 101 | No | VLAN 101 required; PPPoE login needed |
| United Kingdom | Sky Broadband | DHCP (Option 61) | 101 | No | Requires DHCP Option 61 (client identifier) |
| United Kingdom | Virgin | DHCP | N/A | Yes | The modem is in bridged mode and requires MAC cloning. |
| France | Orange | DHCP / PPPoE | 832 | No | VLAN 832 required; may require Option 90 authentication |
| France | Free (Freebox) | DHCP | N/A | No | |
| France | Bouygues Telecom | DHCP | 100 | Yes | Clone Bbox MAC |
| Spain | Movistar | PPPoE | 6 | No | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spain | DIGI | PPPoE | 20 | No | |
| Spain | Orange | DHCP | 832/835 | No | VLANs may vary by region |
| Italy | TIM | PPPoE | 835 | No | VLAN 835 required |
| Italy | Aruba | PPPoE | 835 | No | |
| Netherlands | KPN | DHCP | 6 | No | VLAN 6 required for internet |
| Netherlands | Tweak | DHCP | 34 | Yes | Cloning Experia Box MAC |
| Netherlands | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Netherlands | Odido | DHCP | 300 | No | |
| Belgium | EDPnet | PPPoE | 10 | No | |
| Bosnia and Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croatia | Terrakom | PPPoE | 905 | No | |
| Czech Republic | O2 | PPPoE | 848 | No | |
| Cyprus | Epic | PPPoE | 35 | No | |
| Cyprus | Cyta | PPPoE | 42 | No | |
| Cyprus | Cablenet | PPPoE | 42 | No | |
| Cyprus | Primetel | PPPoE | 42 | No | |
| Poland | Orange Polska | PPPoE | 35 | No | VLAN 35 required |
| Poland | T-mobile | PPPoE | 35 | No | |
| Ireland | Vodafone SIRO | PPPoE | 10 | No | |
| Ireland | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Yes | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Greece | Cosmote | PPPoE | 835 | No | |
| Greece | Nova | PPPoE | 835 | Yes | |
| Greece | DEI/PPC | DHCP | 835 | No | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requires MAP-E/DS-Lite compatible router |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | No | BBIX IPoE service commonly used |
| India | Airtel | PPPoE / DHCP | N/A | No | Some regions require PPPoE |
| India | JioFiber | DHCP | N/A | No | Locked ONT in many cases |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 required; IPTV separate VLAN |
| Singapore | StarHub | DHCP | N/A | No | DHCP-based connection |
| Australia | NBN (various ISPs) | PPPoE / DHCP | 2 (common) | Yes | VLAN 2 common but ISP-dependent |
