# Jak skonfigurować drop-in gateway na routerze GL.iNet

GL.iNet oferuje funkcję drop-in gateway, która rozszerza możliwości głównego routera o funkcje, których może on nie mieć, w tym AdGuard Home, szyfrowany DNS i VPN. Dzięki tej funkcji możesz nadal korzystać z głównego routera jak zwykle, jednocześnie zyskując dodatkowe możliwości. 

Możesz włączyć drop-in gateway dla [wszystkich urządzeń](#włącz-drop-in-gateway-dla-wszystkich-urządzeń) lub [wybranych urządzeń](#włącz-drop-in-gateway-dla-wybranych-urządzeń) podłączonych do głównego routera. Postępuj zgodnie z odpowiednią sekcją dla swojej konfiguracji.

**Uwaga**: Modele z wersją firmware poniżej v4.5.0 obsługują tylko włączenie drop-in gateway dla wszystkich urządzeń. Gdy drop-in gateway jest włączone, wszystkie urządzenia klienckie są obsługiwane przez drop-in gateway, co oznacza, że cały ruch z podłączonych klientów jest najpierw przetwarzany przez ten router.

---

## Włącz drop-in gateway dla wszystkich urządzeń

### 1. Podłącz router GL.iNet do głównego routera

Podłącz port WAN routera GL.iNet do portu LAN głównego routera za pomocą kabla Ethernet.

### 2. Włącz drop-in gateway 

Są dwie metody włączenia drop-in gateway: przez panel administracyjny routera lub aplikację mobilną GL.iNet. 

??? "Korzystanie z panelu administracyjnego WWW"

    1. W przeglądarce internetowej wpisz `192.168.8.1`.  

    2. Wprowadź hasło, a następnie kliknij **Login**. 

    3. Na lewym pasku bocznym kliknij **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Obok **Enable Drop-in Gateway Mode** przestaw przełącznik na włączony. 

    5. Wybierz **All devices are networked through drop-in gateway**. 

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Kliknij **Apply**. 

??? "Korzystanie z aplikacji mobilnej GL.iNet"

    **Uwaga:** Przed rozpoczęciem zainstaluj aplikację mobilną GL.iNet na swoim urządzeniu. 

    1. Na ekranie głównym aplikacji stuknij kartę **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Stuknij **Enable**. 

    3. W pozycji **Devices are networked via drop-in gateway** stuknij **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Stuknij **Done**. 

### 3. Wyłącz serwer DHCP na głównym routerze

Zaloguj się do głównego routera, aby wyłączyć serwer DHCP. Możesz skorzystać z instrukcji dostarczonych przez producenta routera lub skontaktować się z jego wsparciem technicznym. 

### 4. Skonfiguruj AdGuard, DNS, VPN i inne funkcje

Skorzystaj z poniższych przewodników, aby włączyć wybrane funkcje na routerze GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Szyfrowany DNS](../interface_guide/dns.md){target="_blank"}
* [Kontrola rodzicielska](../interface_guide/parental_control.md){target="_blank"}
* [Klient WireGuard](../interface_guide/wireguard_client.md){target="_blank"}
* [Klient OpenVPN](../interface_guide/openvpn_client.md){target="_blank"}

---

## Włącz drop-in gateway dla wybranych urządzeń

### 1. Podłącz router GL.iNet do głównego routera

Podłącz port WAN routera GL.iNet do portu LAN głównego routera za pomocą kabla Ethernet.

### 2. Włącz drop-in gateway

Są dwie metody włączenia drop-in gateway: przez [panel administracyjny routera](#korzystanie-z-panelu-administracyjnego-www) lub [aplikację mobilną GL.iNet](#korzystanie-z-aplikacji-mobilnej-glinet). 

??? "Korzystanie z panelu administracyjnego WWW"

    1. W przeglądarce internetowej wpisz `192.168.8.1`. 

    2. Wprowadź hasło, a następnie kliknij **Login**. 

    3. Na lewym pasku bocznym kliknij **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Obok **Enable Drop-in Gateway Mode** przestaw przełącznik na włączony. 
    
    5. Wybierz **Some devices select their own networking gateway**. 

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Kliknij **Apply**. 

    **Uwaga:** NIE zamykaj tej karty. W następnym kroku będzie trzeba wprowadzić adres IP wyświetlony na ekranie.

??? "Korzystanie z aplikacji mobilnej GL.iNet"

    **Uwaga:** Przed rozpoczęciem zainstaluj aplikację mobilną GL.iNet na swoim urządzeniu. 

    1. Na ekranie głównym aplikacji stuknij kartę **System** > **Drop-in Gateway**.
    
        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
    
    2. Stuknij **Enable**. 
    
    3. W pozycji **Devices are networked via drop-in gateway** stuknij **part**.
    
        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Stuknij **Done**. 

    **Uwaga:** NIE zamykaj tej karty. W następnym kroku będzie trzeba wprowadzić adres IP wyświetlony na ekranie. 

### 3. Ustaw bramę i DNS na wybranym urządzeniu

??? "Windows"
    
    1. Podłącz urządzenie do głównego routera. 
    2. W systemie Windows otwórz **Settings** > **Network & Internet**.
    3. W zależności od sposobu połączenia wykonaj odpowiednie kroki: 
        * Ethernet: kliknij **Ethernet**. 
        * Wi-Fi: kliknij **Wi-Fi**, a następnie nazwę sieci Wi-Fi. 
    4. Skopiuj adres IPv4. Obok **IP assignment** kliknij **Edit**. 
    5. Kliknij **Manual**. 
    6. Przestaw **IPv4** na włączony.
    7. Wprowadź następujące informacje: 
        * **IP address:** Wklej adres IP skopiowany w kroku 4. 
        * **Subnet mask:** Wpisz **255.255.255.0**. 
        * **Gateway:** Wpisz adres IP wyświetlony na stronie **Drop-in Gateway**. 
        * **Preferred DNS:**  Wpisz adres IP wyświetlony na stronie **Drop-in Gateway**. 
    8. Kliknij **Save**. 

??? "Android"
    1. Podłącz urządzenie do głównego routera. 
    2. Na urządzeniu z Androidem otwórz **Settings**. 
    3. Stuknij **Connections** > **Wi-Fi**.
    4. Stuknij ikonę **Settings** obok sieci, z którą jesteś połączony. 
    5. Stuknij **View more**. 
    6. Stuknij **IP settings** > **Static**. 
    7. W polach **Gateway** i **DNS 1** wpisz adres IP wyświetlony na ekranie **Drop-in Gateway**. 
    8. Stuknij **Save**. 

??? "iOS"
    1. Podłącz urządzenie do głównego routera. 
    2. Na urządzeniu z iOS otwórz **Settings**.
    3. Stuknij **Wi-Fi**.
    4. Stuknij sieć Wi-Fi, z którą jesteś połączony. 
    5. W sekcji **IPv4 Address** zapisz wartości **IP Address** i **Subnet Mask**.
    6. Stuknij **Configure IP** > **Manual**. 
    7. Wprowadź następujące informacje: 
        * **IP Address:** Wpisz **IP Address** zapisany w kroku 5. 
        * **Subnet Mask:** Wpisz **Subnet Mask** zapisany w kroku 5. 
        * **Router:** Wpisz adres IP wyświetlony na ekranie **Drop-in Gateway**. 
    8. Stuknij **Save**.
    9. Stuknij **Configure DNS**, a następnie **Manual**. 
    10. Stuknij **Add Server**, a następnie wpisz adres IP wyświetlony na ekranie **Drop-in Gateway**.
    11. Stuknij **Save**.

??? "Mac"
    1. Podłącz urządzenie do głównego routera.
    2. Na komputerze Mac kliknij ikonę Apple > **System Settings**, 
    3. Na lewym pasku bocznym kliknij **Network**.
    4. Obok sieci, z którą jesteś połączony, kliknij **Details**.
    5. Kliknij **TCP/IP**.
    6. Zapisz wartości **IP Address** i **Subnet Mask**.
    7. Obok **Configure IPv4** kliknij **Manually**.
    8. Wprowadź następujące informacje: 
        * **IP address:** Wpisz **IP Address** zapisany w kroku 6. 
        * **Subnet mask:** Wpisz **Subnet Mask** zapisany w kroku 6. 
        * **Router:** Wpisz adres IP wyświetlony na stronie **Drop-in Gateway**. 
    9. Kliknij **OK** > **OK**. 

### 4. Skonfiguruj AdGuard, DNS, VPN i inne funkcje

Skorzystaj z poniższych przewodników, aby włączyć wybrane funkcje na routerze GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Szyfrowany DNS](../interface_guide/dns.md){target="_blank"}
* [Kontrola rodzicielska](../interface_guide/parental_control.md){target="_blank"}
* [Klient WireGuard](../interface_guide/wireguard_client.md){target="_blank"}
* [Klient OpenVPN](../interface_guide/openvpn_client.md){target="_blank"}

---

Powiązany artykuł:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
