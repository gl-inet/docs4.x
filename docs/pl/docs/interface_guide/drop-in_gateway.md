# Drop-in Gateway

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway to funkcja rozszerzająca możliwości istniejącego routera głównego bez konieczności jego wymiany ani rekonfiguracji. Po podłączeniu routera GL.iNet do routera głównego kablem Ethernet możesz dodać do istniejącej infrastruktury sieciowej zaawansowane funkcje, na przykład:

- filtrowanie reklam za pomocą AdGuard Home;
- korzystanie z klienta VPN;
- używanie szyfrowanego DNS.

Zaleca się użycie wydajniejszego routera lub bramy bezpieczeństwa z odpowiednią ilością pamięci (np. GL-MT2500, GL-MT5000) oraz, w razie potrzeby, zainstalowanie dodatkowych narzędzi do przekazywania i kontroli ruchu.

## Topologia sieci

Drop-in Gateway działa jako pośredni element sieci, kierując ruch danych z urządzeń klienckich przez router GL.iNet do przetworzenia, zanim zostanie on przesłany dalej przez router główny. W tym procesie zachowuje istniejące ustawienia sieciowe (np. SSID i hasło), aby zapewnić nieprzerwaną łączność wszystkim podłączonym urządzeniom, a jednocześnie pozwala zarządzać ruchem dla wszystkich lub wybranych urządzeń klienckich.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Powyższy diagram zawiera dwa typy linii: szare linie oraz zielone linie oznaczone trzema strzałkami, z których każda ma przypisany numer.

1. **Szare linie** przedstawiają topologię połączeń fizycznych: urządzenia klienckie (np. komputer, laptop) łączą się z routerem głównym, a port LAN routera głównego jest połączony kablem Ethernet z portem WAN routera GL.iNet (z włączoną funkcją Drop-in Gateway).

2. **Zielone linie** pokazują kolejność przesyłania danych, gdy funkcja Drop-in Gateway jest aktywna, a ponumerowane strzałki wskazują kolejność przepływu ruchu:

    1. Ruch z urządzeń klienckich jest najpierw kierowany do routera głównego;
    
    2. Router główny przekazuje ruch do routera GL.iNet w celu przetworzenia (np. filtrowania reklam lub szyfrowania VPN);
    
    3. Po przetworzeniu ruch wraca do routera głównego, który następnie dostarcza dane do urządzeń klienckich albo kieruje je do Internetu.

## Konfiguracja

Dostępne są dwa tryby wdrożenia dla różnych scenariuszy użycia: wszystkie urządzenia klienckie korzystają z Drop-in Gateway albo tylko wybrane urządzenia klienckie korzystają z Drop-in Gateway.

W poniższym przykładzie adresem bramy routera głównego jest `192.168.1.1`.

### Wszystkie urządzenia korzystają z Drop-in Gateway {all-devices-managed-by-the-drop-in-gateway}

1. Podłącz port LAN routera głównego do portu WAN routera GL.iNet za pomocą kabla Ethernet.

2. Zaloguj się do webowego panelu administracyjnego routera GL.iNet, włącz Drop-in Gateway, a system automatycznie wygeneruje odpowiednie parametry konfiguracji.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** oznacza adres WAN routera GL.iNet, który jest dynamicznie przydzielany przez router główny. Ten adres WAN możesz sprawdzić w sekcji Ethernet na stronie [INTERNET](internet_ethernet.md).
    
    - Pola **Gateway** i **DNS Server 1** są domyślnie automatycznie wypełniane adresem IP routera głównego. Jeśli te parametry są nieprawidłowe, możesz ręcznie je skorygować.

    Zanotuj ten adres IP, ponieważ będzie potrzebny w kolejnych krokach.

    Wybierz pierwszą metodę konfiguracji i kliknij **Apply**.

3. Zaloguj się do webowego panelu administracyjnego routera głównego.

    ??? "GL.iNet"

        Jeśli routerem głównym jest GL.iNet i działa on na firmware v4.2 lub nowszym, wykonaj poniższe kroki.

        Zaloguj się do webowego panelu administracyjnego i przejdź do **NETWORK** -> **LAN** -> **DHCP Server** -> **Advanced**.

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        W polu **DHCP Gateway** wpisz adres IP z kroku 2, np. `192.168.1.23`, a następnie kliknij **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Jeśli routerem głównym jest TP-Link, wykonaj poniższe kroki (na przykładzie TP-LINK Archer C3150).

        Zaloguj się do panelu administracyjnego TP-Link, przejdź do **Advanced** -> **Network** -> **DHCP Server**, a następnie wyłącz **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Następnie kliknij **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Jeśli routerem głównym jest Linksys, wykonaj poniższe kroki (na przykładzie Linksys WHW01).

        Zaloguj się do panelu administracyjnego Linksys i przejdź do **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Kliknij kartę **Local Network**, wyłącz **DHCP Server**, a następnie kliknij **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Pojawi się ostrzeżenie. Kliknij **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Inne"

        Zaloguj się do panelu administracyjnego routera głównego, aby wyłączyć jego serwer DHCP. Możesz skorzystać z instrukcji producenta lub pomocy technicznej.

4. Wróć do routera GL.iNet i skonfiguruj potrzebne funkcje, takie jak [AdGuard Home](adguardhome.md), [szyfrowany DNS](dns.md), [klient WireGuard](wireguard_client.md) oraz [klient OpenVPN](openvpn_client.md).

### Wybrane urządzenia korzystają z Drop-in Gateway {some-devices-managed-by-the-drop-in-gateway}

1. Podłącz port LAN routera głównego do portu WAN routera GL.iNet za pomocą kabla Ethernet.

2. Zaloguj się do webowego panelu administracyjnego routera GL.iNet, włącz Drop-in Gateway, a system automatycznie wygeneruje odpowiednie parametry konfiguracji.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** oznacza adres WAN routera GL.iNet, który jest dynamicznie przydzielany przez router główny. Ten adres WAN możesz sprawdzić w sekcji Ethernet na stronie [INTERNET](internet_ethernet.md).
    
    - Pola **Gateway** i **DNS Server 1** są domyślnie automatycznie wypełniane adresem IP routera głównego. Jeśli te parametry są nieprawidłowe, możesz ręcznie je skorygować.

    Zanotuj ten adres IP, ponieważ będzie potrzebny w kolejnych krokach.

    Wybierz drugą metodę konfiguracji i kliknij **Apply**.

3. Na urządzeniu, które ma korzystać z funkcji Drop-in Gateway, ustaw bramę i DNS na adres IP widoczny na stronie Drop-in Gateway.

    ??? "Windows"

        Poniżej pokazano przykład dla Windows 11; w Windows 10 procedura jest podobna. Upewnij się, że komputer jest połączony z routerem głównym. W tym przykładzie zakładamy połączenie przewodowe, ale w przypadku połączenia przez Wi-Fi konfiguracja wygląda podobnie.

        1. Otwórz Ustawienia.

        2. Kliknij **Network & Internet**.

        3. Kliknij kartę **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Znajdź adres IP tego komputera. W sekcji **IP assignment** kliknij przycisk **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Wybierz opcję **Manual**. Włącz przełącznik **IPv4**.

        6. Ustaw **IP address** na adres IP widoczny w kroku 4, **Subnet mask** na `255.255.255.0`, a pola **Gateway** i **Preferred DNS** na adres IP widoczny na stronie Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Kliknij przycisk **Save**.

    ??? "Android"

        Poniżej pokazano przykład dla Samsung S21. Upewnij się, że smartfon jest połączony z routerem głównym.

        1. Otwórz Ustawienia i kliknij **Connections**.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Kliknij **Wi-Fi**.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Kliknij ikonę koła zębatego przy aktualnym SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Kliknij **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Kliknij **IP settings** i wybierz **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Ustaw **Gateway** i **DNS 1** na adres IP widoczny na stronie Drop-in Gateway, a następnie kliknij **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Poniżej pokazano przykład dla iOS 16.3 na iPhonie 8. Upewnij się, że smartfon jest połączony z routerem głównym.

        1. Otwórz Ustawienia i kliknij **Wi-Fi**.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Kliknij SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Przewiń w dół, aż zobaczysz, że **Configure IP** ma wartość **Automatic**. Zanotuj **IP Address** i **Subnet Mask**, ponieważ będą potrzebne w następnym kroku.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Zmień **Configure IP** na **Manual**, ustaw **IP Address** i **Subnet Mask** na takie same wartości jak w poprzednim kroku, a **Router** ustaw na adres IP wyświetlany na stronie Drop-in Gateway, po czym kliknij **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Kliknij **Configure DNS** i zmień ustawienie na **Manual**. Kliknij **Add Server**, ustaw adres IP serwera DNS na adres IP wyświetlany na stronie Drop-in Gateway, a następnie kliknij **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Wróć do webowego panelu administracyjnego routera GL.iNet i skonfiguruj potrzebne funkcje, takie jak [AdGuard Home](adguardhome.md), [szyfrowany DNS](dns.md), [klient WireGuard](wireguard_client.md) oraz [klient OpenVPN](openvpn_client.md).

## Uwagi

1. Włączenie Drop-in Gateway zwiększa opóźnienia sieciowe.

2. Gdy Drop-in Gateway jest włączony, transmisja danych między wybranymi urządzeniami LAN również jest kierowana przez Drop-in Gateway. Oznacza to, że przepustowość połączenia między routerem głównym a Drop-in Gateway wpływa na całkowitą przepustowość sieci LAN.

---

Powiązany artykuł:

- [Jak skonfigurować Drop-in Gateway na routerze GL.iNet](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
