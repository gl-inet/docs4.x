# Jak ręcznie skonfigurować statyczny adres IP na urządzeniach klienckich? {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    W systemie Windows 11 możesz ustawić statyczny adres IP dla adapterów bezprzewodowych i przewodowych.

    **Ustawianie statycznego adresu IP na adapterze Wi-Fi**

    1. Na komputerze z systemem Windows 11 przejdź do **Settings** -> **Network & internet** -> **Wi-Fi** i wybierz bieżące połączenie Wi-Fi.

    2. Znajdź **IP assignment** i kliknij przycisk **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. W wyskakującym oknie wybierz **Manual** i włącz **IPv4**.

        ![Ręczna konfiguracja IP](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Wykonaj poniższe kroki, aby edytować ustawienia IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: ustaw statyczny adres IP, na przykład `10.1.4.119`.

        - Subnet mask: określ maskę podsieci, na przykład `255.255.255.0`.

        - Gateway: wprowadź adres bramy, zwykle adres IP LAN routera w tej samej podsieci. Na przykład, jeśli adres IP to `10.1.4.119`, adres bramy to zazwyczaj `10.1.4.1`.

        - Preferred DNS: określ preferowany adres DNS (wymagany). Możesz użyć publicznego serwera DNS, na przykład serwera DNS Google `8.8.8.8`.

        - Alternate DNS: określ alternatywny adres DNS (opcjonalny).

        - DNS over HTTPS: wybierz "Off". Dostępne są trzy opcje:

            - Off: przesyła cały ruch DNS bez szyfrowania.

            - On (automatic template): wysyła cały ruch DNS z szyfrowaniem.

            - On (manual template): pozwala określić konkretny szablon. Jest to wymagane tylko wtedy, gdy usługa DNS nie działa automatycznie lub ma szablon, który działa zgodnie z oczekiwaniami.

        - Wyłącz przełącznik "Fallback to plaintext", jeśli włączysz DNS over HTTPS.

            **Wskazówka**: jeśli włączysz tę funkcję, system będzie szyfrował ruch DNS, ale pozwoli na wysyłanie zapytań bez szyfrowania.

    5. Kliknij **Save**, aby zastosować ustawienia.

        Po wykonaniu tych kroków statyczna konfiguracja sieciowa zostanie zastosowana na komputerze. Możesz przetestować nowe ustawienia, otwierając przeglądarkę internetową i ładując stronę internetową.

    ---

    **Ustawianie statycznego adresu IP na adapterze Ethernet**

    1. Na komputerze z systemem Windows 11 przejdź do **Settings** -> **Network & internet** -> **Ethernet**.

    2. Znajdź **IP assignment** i kliknij przycisk **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. W wyskakującym oknie wybierz **Manual** i włącz **IPv4**.

        ![Ręczna konfiguracja IP](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Wykonaj poniższe kroki, aby edytować ustawienia IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: ustaw statyczny adres IP, na przykład `10.1.4.119`.

        - Subnet mask: określ maskę podsieci, na przykład `255.255.255.0`.

        - Gateway: wprowadź adres bramy, zwykle adres IP LAN routera w tej samej podsieci. Na przykład, jeśli adres IP to `10.1.4.119`, adres bramy to zazwyczaj `10.1.4.1`.

        - Preferred DNS: określ preferowany adres DNS (wymagany). Możesz użyć publicznego serwera DNS, na przykład serwera DNS Google `8.8.8.8`.

        - Alternate DNS: określ alternatywny adres DNS (opcjonalny).

        - DNS over HTTPS: wybierz "Off". Dostępne są trzy opcje:

            - Off: przesyła cały ruch DNS bez szyfrowania.

            - On (automatic template): wysyła cały ruch DNS z szyfrowaniem.

            - On (manual template): pozwala określić konkretny szablon. Jest to wymagane tylko wtedy, gdy usługa DNS nie działa automatycznie lub ma szablon, który działa zgodnie z oczekiwaniami.

        - Wyłącz przełącznik "Fallback to plaintext", jeśli włączysz DNS over HTTPS.

            **Wskazówka**: jeśli włączysz tę funkcję, system będzie szyfrował ruch DNS, ale pozwoli na wysyłanie zapytań bez szyfrowania.

    5. Kliknij **Save**, aby zastosować ustawienia.

        Po wykonaniu tych kroków statyczna konfiguracja sieciowa zostanie zastosowana na komputerze. Możesz przetestować nowe ustawienia, otwierając przeglądarkę internetową i ładując stronę internetową.

=== "macOS"

    Oto jak ustawić statyczny adres IP w macOS.

    Z menu Apple wybierz **System Preferences**.

    Wybierz **Network**, aby wyświetlić poniższą stronę. Z paska bocznego wybierz aktywny interfejs sieciowy, na przykład **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Zanotuj bieżący adres IP przypisany do Maca. Musisz wybrać nowy adres IP z podanego zakresu prywatnych adresów IP.

    Kliknij **Advanced** w prawym dolnym rogu.

    Następnie wybierz **TCP/IP**, aby wyświetlić poniższą stronę.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: wybierz "Manually".

    - IPv4 Address: wprowadź statyczny adres IP. Zachowaj pierwsze trzy oktety bieżącego adresu IP i zmień ostatni oktet na nieużywaną wartość. Na przykład w sieci `192.168.7.0/24` wybierz nieużywany adres od `192.168.7.2` do `192.168.7.254` (unikaj `.1`, czyli adresu routera). Nie używaj `192.168.7.0` ani `192.168.7.255`.

    - Subnet Mask: wprowadź `255.255.255.0` (lub maskę podsieci podaną przez administratora sieci).

    - Router: wprowadź adres IP LAN routera, na przykład `192.168.7.1`.

    Kliknij **OK**, a następnie **Apply**.

=== "iOS"

    Kroki mogą się różnić w zależności od wersji iOS. Poniższe kroki dotyczą systemu iOS 26.2.2.

    1. Przejdź do **Settings** -> **WLAN**. Dotknij niebieskiej ikony informacji (i) obok aktualnie połączonej sieci Wi-Fi.

        ![Statyczny adres IP w iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Przewiń w dół do **IPv4 Address** i ustaw **Configure IP** na **Manual**.

        ![Statyczny adres IP w iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Określ wartości **IP Address**, **Subnet Mask** i **Router IP**, których chcesz używać na iPhonie/iPadzie, a następnie dotknij **Save** w prawym górnym rogu.

        ![Statyczny adres IP w iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Kroki mogą się różnić w zależności od wersji Androida. Poniższe kroki dotyczą systemu Android 11.

    1. Przejdź do **Settings** -> **Network & Internet** -> **Wi-Fi**. Dotknij aktualnie połączonej sieci, aby otworzyć menu ustawień.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Dotknij ikony ołówka w prawym górnym rogu, aby uzyskać dostęp do ustawień sieciowych.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Dotknij **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Dotknij **IP Settings** i wybierz **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Wprowadź **IP address**. Pole **Gateway** powinno zostać uzupełnione automatycznie na podstawie adresu IP. Jeśli tak się nie stanie, wprowadź bramę sieciową. Jest to zwykle adres IP LAN routera w tej samej podsieci.

        **Wskazówka**: używając statycznych adresów IP w sieciach domowych i innych sieciach prywatnych, wybierz nieużywany adres hosta w bieżącej podsieci. Standardowe zakresy prywatnych adresów IP to:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Dotknij **Save** i poczekaj, aż sieć ponownie się połączy.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
