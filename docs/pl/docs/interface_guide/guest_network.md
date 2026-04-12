# Sieć gościnna

Ustawienia sieci gościnnej są oddzielone od [LAN](lan.md) od wersji firmware v4.5.

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Guest Network**.

Strona ta obejmuje podstawowe ustawienia sieci gościnnej oraz ustawienia serwera DHCP.

## Ustawienia podstawowe

Możesz ustawić podsieć w zakresie prywatnych adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_1.png){class="glboxshadow"}

Możesz skonfigurować oddzielną, odizolowaną sieć przeznaczoną dla użytkowników tymczasowych, która zapewnia ograniczony dostęp i wyższy poziom bezpieczeństwa dzięki odseparowaniu od sieci głównej.

**Uwaga**: Niektóre modele (np. GL-MT5000, GL-MT2500/GL-MT2500A) nie obsługują Wi-Fi, dlatego ustawienia **Guest Network** nie są dostępne w ich webowym panelu administracyjnym.

- **Gateway**

    **Domyślna brama** sieci gościnnej to **192.168.9.1**. Jeśli powoduje konflikt z Twoją siecią lokalną, zmień ją na inny adres.

- **Netmask**
    
    Domyślnie jest to **255.255.255.0**. Możesz też wybrać **255.255.0.0**, jeśli potrzebujesz większej podsieci z większą liczbą adresów IP.

- **AP Isolation**

    Ta funkcja jest dostępna od firmware v4.5.

    Możesz odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

- **Block WAN Subnets**

    Ta funkcja jest dostępna od firmware v4.8.

    Po włączeniu sieć gościnna nie może uzyskać dostępu do sieci nadrzędnej ani do jej podsieci.

## Serwer DHCP

Jeśli **Guest Network** jest włączona, **DHCP Server** będzie domyślnie również włączony.

Serwer DHCP automatycznie przypisuje adresy IP i inne parametry komunikacyjne każdemu urządzeniu klienckiemu połączonemu z siecią gościnną. Jeśli serwer DHCP jest wyłączony, musisz ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Możesz zmienić początkowy i końcowy adres IP zgodnie ze swoimi potrzebami — na przykład gdy sieć się powiększa lub zmniejsza, występują konflikty adresów IP albo zostaje zmieniony zakres maski podsieci.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/guest_network_2.png){class="glboxshadow"}

Kliknij **Advanced**, aby w razie potrzeby przejść do dalszej konfiguracji.

![dhcp advanced 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced1.png){class="glboxshadow"}

![dhcp advanced 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/guest_network/dhcp_advanced2.png){class="glboxshadow"}

- **Lease Time**: Okres, przez jaki adres IP przypisany przez DHCP pozostaje ważny dla urządzenia.

- **Gateway**: Urządzenie, które kieruje ruch między siecią gościnną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server 1**: Główny serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2**: Zapasowy serwer używany do rozwiązywania nazw domen, gdy główny serwer DNS jest niedostępny.

- **LPR Server**: (Line Printer Remote Server) Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie zleceń druku do drukarek zdalnych. Można skonfigurować wiele portów drukarki LPR.

---

Powiązane artykuły:

- [Jak skonfigurować gościnną sieć Wi-Fi na routerach GL.iNet](../tutorials/how_to_set_up_a_guest_network.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
