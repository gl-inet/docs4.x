# Podsieć

**Uwaga**: Ta strona jest obecnie dostępna na Flint 4 (GL-BE14000) i zostanie udostępniona na innych modelach wraz z firmware v4.10.

---

Po lewej stronie panelu administracyjnego WWW przejdź do **NETWORK** -> **Subnet**.

Strona łączy konfigurację **LAN**, **Guest Network**, **IoT Network** oraz niestandardowych **VLAN Networks** w jednym widoku. Zapewnia centralny interfejs zarządzania wszystkimi ustawieniami związanymi z podsieciami, umożliwiając tworzenie i zarządzanie wieloma podsieciami w celu izolowania różnych typów urządzeń lub ruchu.

## Sieć główna

**Main Network** to sieć, z którą urządzenie jest połączone przez główne Wi-Fi lub kabel Ethernet.

W Main Network można bezpośrednio sprawdzić wszystkie stany interfejsów, VLAN ID, adres IP routera oraz zakres DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu, aby skonfigurować Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

Strona konfiguracji obejmuje ustawienia podstawowe, ustawienia serwera DHCP oraz rezerwację adresów.

### Ustawienia podstawowe

Podsieć można ustawić w prywatnych zakresach adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Jest to adres, który należy wpisać w pasku adresu przeglądarki, aby uzyskać dostęp do strony administracyjnej routera.

    Domyślnie jest to **192.168.8.1**. Można go zmienić, jeśli powoduje konflikt z siecią.

- **Netmask**

    Domyślna wartość to **255.255.255.0**. Można także wybrać **255.255.0.0**, jeśli potrzebna jest większa podsieć z większą liczbą adresów IP.

- **VLAN ID**

    Domyślny VLAN ID dla Main Network to **1** i nie można go zmienić.

- **AP Isolation**

    Można odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

### Serwer DHCP

**DHCP Server** jest domyślnie włączony. Serwer DHCP automatycznie przypisuje adresy IP i inne parametry komunikacji każdemu urządzeniu klienckiemu.

Jeśli serwer DHCP jest wyłączony, trzeba ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Można zmienić początkowy i końcowy adres IP zależnie od potrzeb, na przykład gdy sieć się rozrasta lub zmniejsza, występują konflikty adresów IP albo zmienia się zakres maski podsieci.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

W razie potrzeby kliknij **Advanced**, aby przejść do dalszej konfiguracji.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Okres, przez jaki adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway**: Urządzenie routujące ruch między siecią lokalną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server**: Dostępne są dwa pola serwera DNS do skonfigurowania podstawowego i zapasowego resolvera.

    **Uwaga**: Podstawowy DNS wpisuje się w górnym polu, a zapasowy w dolnym. Jeśli serwer podstawowy będzie niedostępny, urządzenia klienckie automatycznie przełączą się awaryjnie na zapasowy resolver, zapewniając ciągłość rozwiązywania nazw domen.

- **LPR Server** (Line Printer Remote Server): Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie żądań drukowania do zdalnych drukarek. Można skonfigurować wiele portów drukarek LPR.

### Rezerwacja adresów

Po określeniu zarezerwowanego adresu IP dla klienta w sieci LAN klient zawsze otrzymuje ten sam adres IP przy każdym dostępie do serwera DHCP routera. Zarezerwowane adresy IP można przypisywać komputerom lub serwerom wymagającym stałych ustawień IP.

**Uwaga:** Skonfigurowane klienty muszą ponownie połączyć się z routerem, aby ustawienie zaczęło działać.

Kliknij **Add**, aby zarezerwować adres IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Zobaczysz okno podręczne.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Wybierz **MAC** z listy rozwijanej. Odpowiedni dostępny adres **IP** zostanie wypełniony automatycznie. Opcjonalnie można wpisać **hostname** i niestandardowy **name**, aby ułatwić identyfikację. Następnie kliknij **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Po dodaniu nowej rezerwacji adresu IP zostanie wyświetlona poniższa strona, co oznacza, że konfiguracja zakończyła się powodzeniem.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Sieć gościnna

**Guest Network** zapewnia dedykowaną sieć Wi-Fi dla gości. Jest odizolowana od sieci głównej, co zwiększa bezpieczeństwo i jednocześnie zapewnia wygodny dostęp do Internetu.

**Uwaga**: Niektóre modele, np. GL-MT5000 i GL-MT2500/GL-MT2500A, nie mają funkcji Wi-Fi, dlatego ustawienia Guest Network nie są dostępne w ich panelu administracyjnym WWW.

W Guest Network można bezpośrednio sprawdzić stan interfejsu, VLAN ID, Gateway oraz zakres DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu, a panel konfiguracji Guest Network otworzy się po prawej stronie.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

Strona konfiguracji obejmuje ustawienia podstawowe i ustawienia serwera DHCP.

### Ustawienia podstawowe

Podsieć można ustawić w prywatnych zakresach adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/gest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    **Domyślna brama** Guest Network to **192.168.9.1**. Jeśli powoduje konflikt z siecią lokalną, zmień ją na inną.

- **Netmask**

    Domyślna wartość to **255.255.255.0**. Można także wybrać **255.255.0.0**, jeśli potrzebna jest większa podsieć z większą liczbą adresów IP.

- **VLAN ID**

    Domyślny VLAN ID dla Guest Network to **9** i można go zmienić w razie potrzeby.

- **AP Isolation**

    Ta funkcja jest dostępna od firmware v4.5.

    Można odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

- **WAN Access Control**

    WAN Access Control zarządza dostępem lokalnej podsieci do sieci po stronie WAN, w tym do Internetu i innych podsieci WAN.

    Dostępne są trzy tryby kontroli dostępu WAN:

    - **Unrestricted**: Umożliwia tej podsieci dostęp do Internetu i innych podsieci po stronie WAN bez ograniczeń.

    - **Block WAN Subnet**: Blokuje dostęp do innych podsieci po stronie WAN. Dostęp do Internetu pozostaje dostępny.

    - **Block Internet Access**: Blokuje cały dostęp wychodzący, w tym Internet i podsieci po stronie WAN.

### Serwer DHCP

**DHCP Server** jest domyślnie włączony. Serwer DHCP automatycznie przypisuje adresy IP i inne parametry komunikacji każdemu urządzeniu klienckiemu.

Jeśli serwer DHCP jest wyłączony, trzeba ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Można zmienić początkowy i końcowy adres IP zależnie od potrzeb, na przykład gdy sieć się rozrasta lub zmniejsza, występują konflikty adresów IP albo zmienia się zakres maski podsieci.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

W razie potrzeby kliknij **Advanced**, aby przejść do dalszej konfiguracji.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Okres, przez jaki adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway**: Urządzenie routujące ruch między siecią lokalną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server**: Dostępne są dwa pola serwera DNS do skonfigurowania podstawowego i zapasowego resolvera.

    **Uwaga**: Podstawowy DNS wpisuje się w górnym polu, a zapasowy w dolnym. Jeśli serwer podstawowy będzie niedostępny, urządzenia klienckie automatycznie przełączą się awaryjnie na zapasowy resolver, zapewniając ciągłość rozwiązywania nazw domen.

- **LPR Server** (Line Printer Remote Server): Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie żądań drukowania do zdalnych drukarek. Można skonfigurować wiele portów drukarek LPR.

## IoT Network

IoT Network tworzy dedykowaną sieć Wi-Fi dla urządzeń IoT. Jest odizolowana od sieci głównej, zapewniając lepszą zgodność i wyższy poziom bezpieczeństwa.

**Uwaga**: Niektóre modele, np. GL-MT5000 i GL-MT2500/GL-MT2500A, nie mają funkcji Wi-Fi, dlatego ustawienia IoT Network nie są dostępne w ich panelu administracyjnym WWW.

W IoT Network można bezpośrednio sprawdzić stan interfejsu, VLAN ID, Gateway oraz zakres DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Kliknij **Edit** w prawym dolnym rogu, a panel konfiguracji IoT Network otworzy się po prawej stronie. W tym panelu można skonfigurować Basic Settings oraz DHCP Server Settings.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Ustawienia podstawowe

Podsieć można ustawić w prywatnych zakresach adresów IPv4: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    **Domyślna brama** IoT Network to **192.168.10.1**. Jeśli powoduje konflikt z siecią lokalną, zmień ją na inną.

- **Netmask**

    Domyślna wartość to **255.255.255.0**. Można także wybrać **255.255.0.0**, jeśli potrzebna jest większa podsieć z większą liczbą adresów IP.

- **VLAN ID**

    Domyślny VLAN ID dla IoT Network to **10** i można go zmienić w razie potrzeby.

- **AP Isolation**

    Ta funkcja jest dostępna od firmware v4.5.

    Można odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

- **WAN Access Control**

    WAN Access Control zarządza dostępem lokalnej podsieci do sieci po stronie WAN, w tym do Internetu i innych podsieci WAN.

    Dostępne są trzy tryby kontroli dostępu WAN:

    - **Unrestricted**: Umożliwia tej podsieci dostęp do Internetu i innych podsieci po stronie WAN bez ograniczeń.

    - **Block WAN Subnet**: Blokuje dostęp do innych podsieci po stronie WAN. Dostęp do Internetu pozostaje dostępny.

    - **Block Internet Access**: Blokuje cały dostęp wychodzący, w tym Internet i podsieci po stronie WAN.

### Serwer DHCP

**DHCP Server** jest domyślnie włączony. Serwer DHCP automatycznie przypisuje adresy IP i inne parametry komunikacji każdemu urządzeniu klienckiemu.

Jeśli serwer DHCP jest wyłączony, trzeba ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Można zmienić początkowy i końcowy adres IP zależnie od potrzeb, na przykład gdy sieć się rozrasta lub zmniejsza, występują konflikty adresów IP albo zmienia się zakres maski podsieci.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

W razie potrzeby kliknij **Advanced**, aby przejść do dalszej konfiguracji.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Okres, przez jaki adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway**: Urządzenie routujące ruch między siecią lokalną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server**: Dostępne są dwa pola serwera DNS do skonfigurowania podstawowego i zapasowego resolvera.

    **Uwaga**: Podstawowy DNS wpisuje się w górnym polu, a zapasowy w dolnym. Jeśli serwer podstawowy będzie niedostępny, urządzenia klienckie automatycznie przełączą się awaryjnie na zapasowy resolver, zapewniając ciągłość rozwiązywania nazw domen.

- **LPR Server** (Line Printer Remote Server): Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie żądań drukowania do zdalnych drukarek. Można skonfigurować wiele portów drukarek LPR.

## VLAN Networks

U góry strony głównej można w razie potrzeby tworzyć dodatkowe **VLAN networks**, aby izolować różne typy urządzeń lub ruch gości.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Kliknij przycisk **+ Add** po prawej stronie, aby skonfigurować nową sieć.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Ustawienia podstawowe

Na tej stronie można skonfigurować podstawowe informacje dla **VLAN Networks**.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Dostosuj nazwę nowo utworzonej podsieci, aby ułatwić jej identyfikację.

- **Gateway**

    Ręcznie skonfiguruj bramę dla nowej podsieci. Zmień tę bramę, jeśli powoduje konflikt z istniejącym segmentem LAN.

- **Netmask**

    Domyślna wartość to **255.255.255.0**. Można także wybrać **255.255.0.0**, jeśli potrzebna jest większa podsieć z większą liczbą adresów IP.

- **VLAN ID**

    Podczas tworzenia podsieci trzeba przypisać VLAN ID z zakresu od **9** do **4000**. Unikaj używania już zajętego VLAN ID, aby zapobiec konfliktom sieciowym.

- **AP Isolation**

    Ta funkcja jest dostępna od firmware v4.5.

    Można odizolować urządzenia klienckie w osobnym segmencie sieci. Urządzenia te nie będą mogły komunikować się z innymi urządzeniami w tej samej sieci.

- **WAN Access Control**

    WAN Access Control zarządza dostępem lokalnej podsieci do sieci po stronie WAN, w tym do Internetu i innych podsieci WAN.

    Dostępne są trzy tryby kontroli dostępu WAN:

    - **Unrestricted**: Umożliwia tej podsieci dostęp do Internetu i innych podsieci po stronie WAN bez ograniczeń.

    - **Block WAN Subnet**: Blokuje dostęp do innych podsieci po stronie WAN. Dostęp do Internetu pozostaje dostępny.

    - **Block Internet Access**: Blokuje cały dostęp wychodzący, w tym Internet i podsieci po stronie WAN.

### Serwer DHCP

**DHCP Server** jest domyślnie włączony. Serwer DHCP automatycznie przypisuje adresy IP i inne parametry komunikacji każdemu urządzeniu klienckiemu.

Jeśli serwer DHCP jest wyłączony, trzeba ręcznie skonfigurować ustawienia sieciowe urządzeń klienckich. Kliknij [tutaj](../tutorials/manually_configure_static_ip.md), aby dowiedzieć się, jak ręcznie skonfigurować statyczny adres IP.

Można zmienić początkowy i końcowy adres IP zależnie od potrzeb, na przykład gdy sieć się rozrasta lub zmniejsza, występują konflikty adresów IP albo zmienia się zakres maski podsieci.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

W razie potrzeby kliknij **Advanced**, aby przejść do dalszej konfiguracji.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: Okres, przez jaki adres IP przydzielony przez DHCP jest ważny dla urządzenia.

- **Gateway**: Urządzenie routujące ruch między siecią lokalną a sieciami zewnętrznymi, takimi jak Internet.

- **DNS Server**: Dostępne są dwa pola serwera DNS do skonfigurowania podstawowego i zapasowego resolvera.

    **Uwaga**: Podstawowy DNS wpisuje się w górnym polu, a zapasowy w dolnym. Jeśli serwer podstawowy będzie niedostępny, urządzenia klienckie automatycznie przełączą się awaryjnie na zapasowy resolver, zapewniając ciągłość rozwiązywania nazw domen.

- **LPR Server** (Line Printer Remote Server): Usługa zarządzająca zadaniami drukowania i umożliwiająca urządzeniom sieciowym wysyłanie żądań drukowania do zdalnych drukarek. Można skonfigurować wiele portów drukarek LPR.

Po skonfigurowaniu nowa sieć VLAN pojawi się na bieżącej stronie wraz z informacjami o podsieci.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

