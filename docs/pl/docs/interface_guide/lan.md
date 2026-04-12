# LAN

Po lewej stronie panelu administracyjnego WWW przejdź do **NETWORK** -> **LAN**.

LAN to sieć, z którą urządzenie jest połączone, gdy korzysta z głównej sieci Wi‑Fi lub kabla Ethernet.

Ta strona obejmuje ustawienia podstawowe, ustawienia serwera DHCP oraz rezerwację adresów.

## Ustawienia podstawowe

Możesz ustawić podsieć w obrębie prywatnych zakresów adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    To adres, który należy wpisać w pasku adresu przeglądarki, aby uzyskać dostęp do strony administracyjnej routera.

    Domyślnie jest to **192.168.8.1**. Możesz go zmienić, jeśli powoduje konflikt w sieci.

- **Netmask**

    Domyślna wartość to **255.255.255.0**. Możesz też wybrać **255.255.0.0**, jeśli potrzebujesz większej podsieci z większą liczbą adresów IP.

- **AP Isolation**

    Możesz odizolować urządzenia klienckie w oddzielnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

## Serwer DHCP

**DHCP Server** jest włączony domyślnie. Serwer DHCP automatycznie przydziela każdemu urządzeniu klienckiemu adresy IP oraz inne parametry komunikacyjne.

Jeśli serwer DHCP jest wyłączony, konieczna będzie ręczna konfiguracja ustawień sieciowych urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Możesz zmienić początkowy i końcowy adres IP zgodnie ze swoimi potrzebami — na przykład gdy sieć się rozrasta lub zmniejsza, pojawiają się konflikty adresów IP albo zmienia się zakres maski podsieci.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Jeśli potrzebujesz dodatkowej konfiguracji, kliknij **Advanced**.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: Okres, przez który adres IP przydzielony przez DHCP pozostaje ważny dla urządzenia.

- **Gateway**: Urządzenie kierujące ruchem między siecią lokalną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server 1**: Główny serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2**: Zapasowy serwer używany do rozwiązywania nazw domen, jeśli podstawowy serwer DNS jest niedostępny.

- **LPR Server**: (Line Printer Remote Server) Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie żądań drukowania do drukarek zdalnych. Można skonfigurować wiele portów drukarki LPR.

## Rezerwacja adresów

Po określeniu zarezerwowanego adresu IP dla klienta w sieci LAN klient będzie zawsze otrzymywał ten sam adres IP przy każdym połączeniu z serwerem DHCP routera. Możesz przypisać zarezerwowane adresy IP komputerom lub serwerom, które wymagają stałych ustawień IP.

**Uwaga:** Aby aktywować ustawienie, skonfigurowane urządzenia klienckie muszą ponownie połączyć się z routerem.

Kliknij **Add**, aby zarezerwować adres IP.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Pojawi się wyskakujące okno.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Wybierz **MAC** z listy rozwijanej, a **IP** odpowiadający wybranemu adresowi MAC zostanie uzupełniony automatycznie. Nadaj wpisowi opisową nazwę. Następnie kliknij **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Po dodaniu nowej rezerwacji adresu IP zobaczysz stronę jak poniżej, co oznacza, że konfiguracja zakończyła się powodzeniem.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
