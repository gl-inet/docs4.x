# LAN {#lan}

**Uwaga**: Ta instrukcja dotyczy wersji v4.11 i nowszych wersji oprogramowania sprzętowego. Jeśli urządzenie ma inną wersję, wybierz poniżej odpowiednią instrukcję.

<div class="gl-link-select" data-label="Wersja oprogramowania sprzętowego" data-placeholder="Wersja v4.11 i nowsze" markdown="1">

- [Wersja v4.9 i starsze](lan.md)

</div>

---

Po lewej stronie panelu administracyjnego WWW przejdź do **NETWORK** -> **LAN**.

Na tej stronie możesz konfigurować sieć główną (**Main Network**), sieć gościnną (**Guest Network**), sieć IoT (**IoT Network**) i niestandardowe sieci VLAN (**VLAN Networks**) oraz nimi zarządzać. Możesz tworzyć wiele podsieci, aby oddzielić poszczególne typy urządzeń lub ruchu.

## Sieć główna {#main-network}

Sieć główna (**Main Network**) to sieć, z którą urządzenie łączy się przez główną sieć Wi-Fi lub kabel Ethernet.

W sekcji **Main Network** możesz sprawdzić stan wszystkich interfejsów, identyfikator VLAN, adres IP routera i zakres DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu, aby skonfigurować sieć główną.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

Strona konfiguracji obejmuje ustawienia podstawowe, ustawienia serwera DHCP oraz rezerwację adresów.

### Ustawienia podstawowe {#basic-settings}

Możesz skonfigurować podsieć w obrębie prywatnych zakresów adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Wpisz ten adres w pasku adresu przeglądarki, aby otworzyć panel administracyjny routera.

    Domyślny adres to **192.168.8.1**. Możesz go zmienić, jeśli powoduje konflikt w sieci.

- **Netmask**

    Domyślna maska podsieci to **255.255.255.0**. Jeśli potrzebujesz większej podsieci z większą liczbą adresów IP, wybierz **255.255.0.0**.

- **VLAN ID**

    Domyślny identyfikator VLAN sieci głównej to **1**. Nie można go zmienić.

- **AP Isolation**

    Możesz odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

    **Uwaga:** Izolacja AP dotyczy wyłącznie urządzeń połączonych przez Wi-Fi.

### Serwer DHCP {#dhcp-server}

Serwer DHCP (**DHCP Server**) jest domyślnie włączony. Automatycznie przydziela każdemu urządzeniu klienckiemu adres IP i inne parametry komunikacji.

Jeśli serwer DHCP jest wyłączony, musisz ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Zobacz, jak [ręcznie skonfigurować statyczny adres IP](../tutorials/manually_configure_static_ip.md).

Możesz zmienić początkowy i końcowy adres IP zakresu DHCP, na przykład gdy zmienia się rozmiar sieci, występują konflikty adresów IP lub zmieniasz maskę podsieci.

![main network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Kliknij **Advanced**, aby w razie potrzeby zmienić ustawienia zaawansowane.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** określa czas, przez który adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway** to urządzenie kierujące ruchem między siecią lokalną a sieciami zewnętrznymi, takimi jak internet.

- **DNS Server 1** to podstawowy serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2** to zapasowy serwer używany do rozwiązywania nazw domen, gdy podstawowy serwer DNS jest niedostępny.

- **LPR Server** (Line Printer Remote Server) to usługa, która zarządza zadaniami drukowania i umożliwia urządzeniom sieciowym wysyłanie ich do drukarek zdalnych. Możesz skonfigurować wiele portów drukarek LPR.

### Rezerwacja adresów {#address-reservation}

Po zarezerwowaniu adresu IP dla urządzenia w sieci LAN urządzenie to będzie otrzymywać ten sam adres IP za każdym razem, gdy połączy się z serwerem DHCP routera. Adresy IP możesz rezerwować dla komputerów lub serwerów wymagających stałych ustawień IP.

**Uwaga:** Aby rezerwacja zaczęła obowiązywać, urządzenie klienckie musi ponownie połączyć się z routerem.

Kliknij **Add**, aby zarezerwować adres IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Otworzy się okno konfiguracji.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Wybierz adres **MAC** z listy rozwijanej. Pole **IP** zostanie automatycznie uzupełnione odpowiednim dostępnym adresem. Możesz wpisać nazwę hosta w polu **hostname** i własną nazwę w polu **name**, aby ułatwić identyfikację. Następnie kliknij **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Po zapisaniu rezerwacji adresu IP zobaczysz ją na stronie, jak pokazano poniżej.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Sieć gościnna {#guest-network}

Sieć gościnna (**Guest Network**) zapewnia gościom dostęp do internetu przez osobną sieć Wi-Fi. Odizolowanie od sieci głównej zwiększa bezpieczeństwo.

**Uwaga**: Niektóre modele, np. GL-MT5000 i GL-MT2500/GL-MT2500A, nie obsługują Wi-Fi. Ich panel administracyjny WWW nie udostępnia ustawień sieci gościnnej.

W sekcji **Guest Network** możesz sprawdzić stan interfejsu, identyfikator VLAN, bramę i zakres DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu. Panel konfiguracji sieci gościnnej otworzy się po prawej stronie.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

Strona konfiguracji obejmuje ustawienia podstawowe i ustawienia serwera DHCP.

### Ustawienia podstawowe {#guest-network-basic-settings}

Możesz skonfigurować podsieć w obrębie prywatnych zakresów adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    **Brama domyślna** sieci gościnnej ma adres **192.168.9.1**. Jeśli ten adres powoduje konflikt w sieci lokalnej, zmień go.

- **Netmask**

    Domyślna maska podsieci to **255.255.255.0**. Jeśli potrzebujesz większej podsieci z większą liczbą adresów IP, wybierz **255.255.0.0**.

- **VLAN ID**

    Domyślny identyfikator VLAN sieci gościnnej to **9**. W razie potrzeby możesz go zmienić.

- **Associated LAN Ports**

    Wybierz porty LAN, które chcesz przypisać do tej podsieci. Urządzenia podłączone przewodowo do tych portów dołączą do tej sieci.

- **AP Isolation**

    Możesz odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

    **Uwaga:** Izolacja AP dotyczy wyłącznie urządzeń połączonych przez Wi-Fi.

- **WAN Access Control**

    Opcja **WAN Access Control** pozwala określić, czy podsieć lokalna ma dostęp do internetu i innych podsieci po stronie WAN.

    Dostępne są trzy tryby kontroli dostępu WAN.

    - **Unrestricted** pozwala tej podsieci na nieograniczony dostęp do internetu i innych podsieci po stronie WAN.

    - **Block WAN Subnet** blokuje dostęp do innych podsieci po stronie WAN. Dostęp do internetu pozostaje możliwy.

    - **Block Internet Access** blokuje cały dostęp wychodzący, w tym dostęp do internetu i podsieci po stronie WAN.

### Serwer DHCP {#guest-network-dhcp-server}

Serwer DHCP (**DHCP Server**) jest domyślnie włączony. Automatycznie przydziela każdemu urządzeniu klienckiemu adres IP i inne parametry komunikacji.

Jeśli serwer DHCP jest wyłączony, musisz ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Zobacz, jak [ręcznie skonfigurować statyczny adres IP](../tutorials/manually_configure_static_ip.md).

Możesz zmienić początkowy i końcowy adres IP zakresu DHCP, na przykład gdy zmienia się rozmiar sieci, występują konflikty adresów IP lub zmieniasz maskę podsieci.

![guest network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Kliknij **Advanced**, aby w razie potrzeby zmienić ustawienia zaawansowane.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** określa czas, przez który adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway** to urządzenie kierujące ruchem między siecią lokalną a sieciami zewnętrznymi, takimi jak internet.

- **DNS Server 1** to podstawowy serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2** to zapasowy serwer używany do rozwiązywania nazw domen, gdy podstawowy serwer DNS jest niedostępny.

- **LPR Server** (Line Printer Remote Server) to usługa, która zarządza zadaniami drukowania i umożliwia urządzeniom sieciowym wysyłanie ich do drukarek zdalnych. Możesz skonfigurować wiele portów drukarek LPR.

## Sieć IoT {#iot-network}

Sieć IoT (**IoT Network**) zapewnia urządzeniom IoT osobną sieć Wi-Fi. Odizolowanie od sieci głównej poprawia zgodność urządzeń i zwiększa bezpieczeństwo.

**Uwaga**: Niektóre modele, np. GL-MT5000 i GL-MT2500/GL-MT2500A, nie obsługują Wi-Fi. Ich panel administracyjny WWW nie udostępnia ustawień sieci IoT.

W sekcji **IoT Network** możesz sprawdzić stan interfejsu, identyfikator VLAN, bramę i zakres DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu. Panel konfiguracji sieci IoT otworzy się po prawej stronie. Możesz w nim zmieniać ustawienia podstawowe i ustawienia serwera DHCP.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Ustawienia podstawowe {#iot-network-basic-settings}

Możesz skonfigurować podsieć w obrębie prywatnych zakresów adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    **Brama domyślna** sieci IoT ma adres **192.168.10.1**. Jeśli ten adres powoduje konflikt w sieci lokalnej, zmień go.

- **Netmask**

    Domyślna maska podsieci to **255.255.255.0**. Jeśli potrzebujesz większej podsieci z większą liczbą adresów IP, wybierz **255.255.0.0**.

- **VLAN ID**

    Domyślny identyfikator VLAN sieci IoT to **10**. W razie potrzeby możesz go zmienić.

- **Associated LAN Ports**

    Wybierz porty LAN, które chcesz przypisać do tej podsieci. Urządzenia podłączone przewodowo do tych portów dołączą do tej sieci.

- **AP Isolation**

    Możesz odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

    **Uwaga:** Izolacja AP dotyczy wyłącznie urządzeń połączonych przez Wi-Fi.

- **WAN Access Control**

    Opcja **WAN Access Control** pozwala określić, czy podsieć lokalna ma dostęp do internetu i innych podsieci po stronie WAN.

    Dostępne są trzy tryby kontroli dostępu WAN.

    - **Unrestricted** pozwala tej podsieci na nieograniczony dostęp do internetu i innych podsieci po stronie WAN.

    - **Block WAN Subnet** blokuje dostęp do innych podsieci po stronie WAN. Dostęp do internetu pozostaje możliwy.

    - **Block Internet Access** blokuje cały dostęp wychodzący, w tym dostęp do internetu i podsieci po stronie WAN.

### Serwer DHCP {#iot-network-dhcp-server}

Serwer DHCP (**DHCP Server**) jest domyślnie włączony. Automatycznie przydziela każdemu urządzeniu klienckiemu adres IP i inne parametry komunikacji.

Jeśli serwer DHCP jest wyłączony, musisz ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Zobacz, jak [ręcznie skonfigurować statyczny adres IP](../tutorials/manually_configure_static_ip.md).

Możesz zmienić początkowy i końcowy adres IP zakresu DHCP, na przykład gdy zmienia się rozmiar sieci, występują konflikty adresów IP lub zmieniasz maskę podsieci.

![iot network dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Kliknij **Advanced**, aby w razie potrzeby zmienić ustawienia zaawansowane.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** określa czas, przez który adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway** to urządzenie kierujące ruchem między siecią lokalną a sieciami zewnętrznymi, takimi jak internet.

- **DNS Server 1** to podstawowy serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2** to zapasowy serwer używany do rozwiązywania nazw domen, gdy podstawowy serwer DNS jest niedostępny.

- **LPR Server** (Line Printer Remote Server) to usługa, która zarządza zadaniami drukowania i umożliwia urządzeniom sieciowym wysyłanie ich do drukarek zdalnych. Możesz skonfigurować wiele portów drukarek LPR.

## Sieci VLAN {#vlan-networks}

U góry strony głównej możesz tworzyć dodatkowe sieci VLAN, aby w razie potrzeby oddzielić różne typy urządzeń lub ruch gości.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Kliknij **+ Add** po prawej stronie, aby skonfigurować nową sieć.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Ustawienia podstawowe {#vlan-networks-basic-settings}

Na tej stronie możesz zmienić podstawowe ustawienia sieci VLAN (**VLAN Networks**).

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Nadaj nowej podsieci nazwę, która ułatwi jej identyfikację.

- **Gateway**

    Skonfiguruj ręcznie bramę nowej podsieci. Zmień jej adres, jeśli powoduje konflikt z istniejącym segmentem LAN.

- **Netmask**

    Domyślna maska podsieci to **255.255.255.0**. Jeśli potrzebujesz większej podsieci z większą liczbą adresów IP, wybierz **255.255.0.0**.

- **VLAN ID**

    Podczas tworzenia podsieci przypisz jej identyfikator VLAN z zakresu od **9** do **4000**. Aby uniknąć konfliktów w sieci, wybierz identyfikator, który nie jest jeszcze używany.

- **Associated LAN Ports**

    Wybierz porty LAN, które chcesz przypisać do tej podsieci. Urządzenia podłączone przewodowo do tych portów dołączą do tej sieci.

- **AP Isolation**

    Możesz odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

    **Uwaga:** Izolacja AP dotyczy wyłącznie urządzeń połączonych przez Wi-Fi.

- **WAN Access Control**

    Opcja **WAN Access Control** pozwala określić, czy podsieć lokalna ma dostęp do internetu i innych podsieci po stronie WAN.

    Dostępne są trzy tryby kontroli dostępu WAN.

    - **Unrestricted** pozwala tej podsieci na nieograniczony dostęp do internetu i innych podsieci po stronie WAN.

    - **Block WAN Subnet** blokuje dostęp do innych podsieci po stronie WAN. Dostęp do internetu pozostaje możliwy.

    - **Block Internet Access** blokuje cały dostęp wychodzący, w tym dostęp do internetu i podsieci po stronie WAN.

### Serwer DHCP {#vlan-networks-dhcp-server}

Serwer DHCP (**DHCP Server**) jest domyślnie włączony. Automatycznie przydziela każdemu urządzeniu klienckiemu adres IP i inne parametry komunikacji.

Jeśli serwer DHCP jest wyłączony, musisz ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Zobacz, jak [ręcznie skonfigurować statyczny adres IP](../tutorials/manually_configure_static_ip.md).

Możesz zmienić początkowy i końcowy adres IP zakresu DHCP, na przykład gdy zmienia się rozmiar sieci, występują konflikty adresów IP lub zmieniasz maskę podsieci.

![vlan networks dhcp basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Kliknij **Advanced**, aby w razie potrzeby zmienić ustawienia zaawansowane.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** określa czas, przez który adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway** to urządzenie kierujące ruchem między siecią lokalną a sieciami zewnętrznymi, takimi jak internet.

- **DNS Server 1** to podstawowy serwer tłumaczący nazwy domen na adresy IP.

- **DNS Server 2** to zapasowy serwer używany do rozwiązywania nazw domen, gdy podstawowy serwer DNS jest niedostępny.

- **LPR Server** (Line Printer Remote Server) to usługa, która zarządza zadaniami drukowania i umożliwia urządzeniom sieciowym wysyłanie ich do drukarek zdalnych. Możesz skonfigurować wiele portów drukarek LPR.

Po skonfigurowaniu nowa sieć VLAN pojawi się na tej stronie wraz z informacjami o podsieci.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
