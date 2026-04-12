# Jak ręcznie skonfigurować statyczny adres IP na urządzeniach klienckich?

=== "Windows 11"

    W systemie Windows 11 możesz ustawić konfigurację statycznego adresu IP z aplikacji Settings dla adapterów bezprzewodowych i przewodowych.

    **Ustawianie statycznego adresu IP na adapterze Wi-Fi**

    Aby przypisać konfigurację statycznego adresu IP do adaptera Wi-Fi, wykonaj następujące kroki:

    1. Otwórz Settings w Windows 11 -> Network & Internet ->  zakładka Wi-Fi ->  Wybierz bieżące połączenie sieciowe.

    2. W sekcji "IP settings" kliknij przycisk Edit.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class=`"glboxshadow`"}

    3. Wykonaj poniższe kroki, aby skonfigurować:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class=`"glboxshadow`"}

        - Wybierz opcję Manual, włącz przełącznik IPv4.

        - Ustaw statyczny adres IP dla Windows 11 – na przykład 10.1.4.119.

        - Określ maskę podsieci (Subnet mask) – na przykład 255.255.255.0.

        - Określ adres bramy domyślnej (Default Gateway).

        - Określ preferowany adres DNS (Preferred DNS) (wymagane).

        - (Opcjonalnie) Określ alternatywny adres DNS (Alternate DNS).

        - Użyj menu rozwijanego "DNS over HTTPS" i wybierz opcję Off dla preferowanych i alternatywnych adresów, ale możesz włączyć DoH za pomocą tych opcji:

            - Off: Przesyła cały ruch DNS bez szyfrowania.

            - On (automatic template): Wysyła cały ruch DNS z szyfrowaniem.

            - On (manual template): Pozwala określić konkretny szablon. Jest to wymagane tylko wtedy, gdy usługa DNS nie działa automatycznie lub ma szablon, który działa zgodnie z oczekiwaniami.

        - Wyłącz przełącznik "Fallback to plaintext" (jeśli włączysz DoH).

            - Szybka wskazówka: Jeśli włączysz tę funkcję, system będzie szyfrował ruch DNS, ale pozwoli na wysyłanie zapytań bez szyfrowania.

    4. Kliknij przycisk Save.

        Po wykonaniu kroków zostanie zastosowana statyczna konfiguracja sieciowa na komputerze. Możesz przetestować nowe ustawienia, otwierając przeglądarkę internetową i ładując stronę internetową.


    ## **Ustawianie statycznego adresu IP na adapterze Ethernet**

    Aby przypisać statyczny adres IP do adaptera Ethernet (przewodowego) w Windows 11, wykonaj następujące kroki:

    1. Otwórz Settings -> Network & Internet ->  zakładka Ethernet.
    
    2. W sekcji "IP settings" kliknij przycisk Edit.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class=`"glboxshadow`"}

    3. Wykonaj poniższe kroki, aby skonfigurować:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class=`"glboxshadow`"}
        
        - Wybierz opcję Manual.

        - Włącz przełącznik IPv4.

        - Ustaw statyczny adres IP dla Windows 11 – na przykład 10.1.4.119.

        - Określ maskę podsieci (Subnet mask) – na przykład 255.255.255.0.

        - Określ adres bramy domyślnej (Default Gateway).

        - Określ preferowany adres DNS (Preferred DNS) (wymagane).

        - (Opcjonalnie) Określ alternatywny adres DNS (Alternate DNS).

        - Użyj menu rozwijanego "DNS over HTTPS" i wybierz opcję Off dla preferowanych i alternatywnych adresów, ale możesz włączyć DoH za pomocą tych opcji:

            * Off: Przesyła cały ruch DNS bez szyfrowania.

            * On (automatic template): Wysyła cały ruch DNS z szyfrowaniem.

            * On (manual template): Pozwala określić konkretny szablon. Jest to wymagane tylko wtedy, gdy usługa DNS nie działa automatycznie lub ma szablon, który działa zgodnie z oczekiwaniami.
            
        - Wyłącz przełącznik "Fallback to plaintext" (jeśli włączysz DoH).

    4. Kliknij przycisk Save.

        Po wykonaniu kroków możesz przetestować ustawienia za pomocą przeglądarki internetowej, aby otworzyć stronę internetową.


=== "macOS"

    Oto jak ustawić statyczny adres IP w macOS:

    Jeśli posiadasz MacBooka, możesz utworzyć nową lokalizację sieciową. Pozwoli to na użycie statycznego adresu IP dla niektórych sieci, a nie dla innych. 

    Z menu Apple wybierz System Preferences.

    Wybierz Network. Pojawi się okno pokazane poniżej.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class=`"glboxshadow`"}

    Z paska bocznego wybierz aktywny interfejs sieciowy. W tym przykładzie jestem połączony z siecią bezprzewodową, więc wybiorę Wi-Fi.

    Zanotuj bieżący adres IP przypisany do Twojego Mac. Musisz wybrać nowy adres IP z zakresu prywatnych adresów IP wymienionych. Więcej na ten temat za chwilę.

    Kliknij Advanced.

    Wybierz TCP/IP. Pojawi się okno pokazane poniżej.
    
    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class=`"glboxshadow`"}

    Z menu Configure IPv4 wybierz Manually.

    Wprowadź statyczny adres IP w polu IPv4 Address. Jaki numer powinieneś wprowadzić? Jedną z metod jest wzięcie bieżącego adresu IP i zmiana ostatniej części numeru. W tym przykładzie mogłem wybrać dowolny adres między 192.168.7.0 a 192.168.7.255, o ile adres nie był już przypisany do innego urządzenia.

    Kliknij OK -> Kliknij Apply.
   

=== "Android"

    Kroki będą się różnić w zależności od wersji Androida. Ta dokumentacja oparta jest na wersji Androida 11.

    1. Przejdź do Settings -> Wybierz Network & Internet, następnie Wi-Fi -> Dotknij sieci aktualnie połączonej, aby otworzyć menu ustawień.
    
    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class=`"gl-50-desktop`"}
    {class=`"glboxshadow`"}

    2. Aby ustawić statyczny adres IP, wykonaj następujące czynności:

    - Wybierz ikonę ołówka w prawym górnym rogu, aby uzyskać dostęp do ustawień sieciowych.
        
        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class=`"gl-50-desktop`"}
        {class=`"glboxshadow`"}

    - Wybierz Advanced Options.
        
        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class=`"gl-50-desktop`"}
        {class=`"glboxshadow`"}

    - Wybierz IP Settings.
        
    - Zmień ustawienie z DHCP na Static.
        
        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class=`"gl-50-desktop`"}
        {class=`"glboxshadow`"}

    - Przy używaniu statycznych adresów IP w sieciach domowych i innych sieciach prywatnych, powinny być wybrane z standardowych zakresów prywatnych adresów IP wymienionych: 10.0.0.0 do 10.255.255.255, 172.16.0.0 do 172.31.255.255, 192.168.0.0 do 192.168.255.255

    - Teraz wprowadź adres IP.
        - Ten krok jest specyficzny dla każdej sieci. np.: 192.168.1.128
        
    - Gateway powinien wypełnić się automatycznie na podstawie adresu IP. Jeśli nie, skopiuj adres IP i zamień ostatnią liczbę na 1. 
        - np. Na podstawie poprzedniego przykładu: 192.168.1.1

    3. Dotknij Save i pozwól sieci ponownie się połączyć.

=== "iOS"

    Przy używaniu statycznych adresów IP w sieciach domowych i innych sieciach prywatnych, powinny być wybrane z standardowych zakresów prywatnych adresów IP wymienionych:

    10.0.0.0 do 10.255.255.255
    172.16.0.0 do 172.31.255.255
    192.168.0.0 do 192.168.255.255

    Aby ustawić statyczny adres IP, wykonaj następujące czynności:

    - Dotknij ikony Settings.

    - Przejdź do Wi-Fi.

    - Dotknij niebieskiej ikony informacji (i) obok nazwy sieci Wi-Fi
         - Może to być niebieski błąd, jeśli używasz czegoś starszego niż iOS 7.

    - Przejdź do zakładki Static, pokazanej poniżej.

        
    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class=`"glboxshadow`"}

    - Dotknij pola IP Address.

    - Wprowadź statyczny adres IP, którego chcesz użyć na swoim iPhone/iPad.

    - Dotknij pola Router.

    - Wprowadź adres IP routera.
        
    - Dotknij Subnet Mask i wprowadź swoje informacje

        - Zazwyczaj będzie to 225.225.0.0.

    - Dotknij przycisku Wi-Fi w lewym górnym rogu ekranu, aby zapisać ustawienia.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
