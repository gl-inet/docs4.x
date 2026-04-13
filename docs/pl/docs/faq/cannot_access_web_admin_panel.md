# Nie można uzyskać dostępu do web Admin Panel

Czasami dostęp do [http://192.168.8.1](http://192.168.8.1) może być niemożliwy, przez co nie da się zalogować do web Admin Panel. Przyczyn może być kilka.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Możliwe przyczyny

* Komputer lub telefon nie jest połączony z routerem.
* `192.168.8.1` to domyślny adres IP routera. Być może został zmieniony.
* Pamięć podręczna przeglądarki albo rozszerzenie mogą uniemożliwiać dostęp do panelu administracyjnego.
* Oprogramowanie VPN lub proxy przejmuje ruch sieciowy, co może blokować dostęp do panelu administracyjnego.
* Router został uszkodzony programowo.

## Sprawdź podstawowe kroki dostępu do web Admin Panel

1. Włącz router bez podłączania go do innych urządzeń.
2. Połącz telefon lub laptop z Wi-Fi routera i wpisz klucz Wi-Fi wydrukowany na etykiecie routera.
3. Jeśli krok 2 się nie powiedzie, wyłącz Wi-Fi na komputerze lub laptopie. Zamiast tego podłącz go do portu LAN routera kablem Ethernet.
4. Otwórz przeglądarkę, wpisz `192.168.8.1` w pasku adresu i naciśnij Enter. Powinno to otworzyć web Admin Panel GL.iNet.

Możesz też użyć [aplikacji](mobile_app.md), aby uzyskać dostęp do routera.

## Inne sposoby rozwiązania problemu

1. [Sprawdź połączenie](#check-the-connection)
2. [Sprawdź adres IP routera](#check-routers-ip-address)
3. [Uzyskaj dostęp do adresu IP routera](#access-the-routers-ip-address)

---

### Sprawdź połączenie {#check-the-connection}

Jeśli korzystasz z kabla Ethernet, upewnij się, że połączenia z portami WAN/LAN routera są prawidłowe:

- Port WAN jest podłączony do źródła Internetu, takiego jak modem lub główny router.
- Port LAN jest podłączony do urządzenia końcowego, na przykład laptopa.

Jeśli łączysz się przez Wi-Fi, upewnij się, że na urządzeniu wybrano prawidłowy identyfikator SSID i wpisano poprawne hasło.

### Sprawdź adres IP routera {#check-routers-ip-address}

Wykonaj poniższe kroki, aby sprawdzić adres IP routera.

=== "Windows 10 / Windows 11"

    Otwórz **Control Panel** i upewnij się, że w prawym górnym rogu wybrano widok **Large icons** lub **Small icons**.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    **Control Panel** -> **Network and Sharing Center** -> kliknij połączenie. Możesz mieć kilka połączeń, więc wybierz to odpowiadające routerowi, który chcesz sprawdzić.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Otworzy się okno stanu połączenia. Kliknij przycisk **Details**.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    Otworzy się okno ze szczegółami połączenia sieciowego. Adres IP routera to wartość **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**

    Kliknij połączenie prawym przyciskiem myszy -> **Status** -> **Details**
    
    Adres IP routera to **IPv4 Default Gateway**
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. **System Preferences** -> **Network**

    2. W lewej kolumnie kliknij połączenie sieciowe. W przypadku połączenia Ethernet adres IP routera będzie widoczny od razu.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    W przypadku połączenia Wi-Fi kliknij przycisk **Advanced...**, a następnie kartę **TCP/IP** u góry okna. Zobaczysz tam adres IP routera.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. **Settings** -> **Wi-Fi**
    2. Dotknij ikony informacji (niebieskie „i” w kółku) przy aktualnie połączonej sieci Wi-Fi. Zobaczysz tam adres IP routera.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Kroki mogą się różnić w zależności od urządzenia z Androidem.

    1. **Settings** -> **Network & internet**
    2. Dotknij **Wi-Fi**, znajdź sieć, z którą jesteś połączony, i kliknij ikonę ustawień, aby zarządzać jej opcjami.
    3. Rozwiń **Advanced**. Jeśli pojawi się wybór między **Static** i **Dynamic IP**, wybierz **Static**.
    4. Niezależnie od tego adres IP routera powinien być widoczny przy pozycji **Gateway**.

### Uzyskaj dostęp do adresu IP routera {#access-the-routers-ip-address}

1. Aby zapewnić najlepszą zgodność, użyj Chrome/Edge/Safari do otwarcia panelu administracyjnego routera.

2. Aby uniknąć problemów powodowanych przez pamięć podręczną przeglądarki i rozszerzenia, otwórz okno incognito, a następnie spróbuj ponownie wejść na adres IP routera.

3. Wyłącz wszystkie programy VPN i proxy, w tym Tailscale oraz ZeroTier.

4. Jeśli korzystasz z telefonu komórkowego, wyłącz transmisję danych.

    Niektóre smartfony rozłączają się z Wi-Fi routera i przełączają na transmisję danych, gdy wykryją, że router nie ma dostępu do Internetu. Po rozłączeniu z routerem dostęp do web Admin Panel nie będzie możliwy.

5. Jeśli powyższe kroki nie pomogły, spróbuj [zresetować](repair_network_or_reset_firmware.md#reset-to-factory) router do ustawień fabrycznych.

6. Jeśli reset nie pomoże, spróbuj opcji [Unbrick via uboot](debrick.md).

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
