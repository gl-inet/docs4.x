# VPN Dashboard (Oprogramowanie v4.7 i wcześniejsze)

**Uwaga**: Ten przewodnik dotyczy oprogramowania v4.7 i wcześniejszego. W przypadku nowszych wersji zapoznaj się z dokumentacją [tutaj](vpn_dashboard.md).

---

Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **VPN Dashboard**.

Strona VPN Dashboard przedstawia stan i ustawienia VPN. Zawiera dwie sekcje: [Klient VPN](#vpn-client) i [Serwer VPN](#vpn-server).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_1.png){class="glboxshadow"}

## Klient VPN

Na początku nie ma dostępnej konfiguracji dla OpenVPN ani WireGuard. Kliknij **Set Up Now**, aby przejść odpowiednio do stron [Klient OpenVPN](openvpn_client.md) i [Klient WireGuard](wireguard_client.md).

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_set_up_now.png){class="glboxshadow"}

Po zakończeniu konfiguracji możesz wybrać plik konfiguracyjny w kolumnie Plik konfiguracyjny.

![glinet vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_configuration_file.png){class="glboxshadow"}

### Opcje klienta VPN

Kliknij ikonę koła zębatego przy OpenVPN lub WireGuard.

![glinet vpn dashboard, vpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_client_options.png){class="glboxshadow"}

Opcje klienta OpenVPN.

![glinet vpn dashboard, openvpn client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_client_options.png){class="glboxshadow"}

Opcje klienta WireGuard.

![glinet vpn dashboard, wireguard client options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_client_options.png){class="glboxshadow"}

* Zezwalaj na zdalny dostęp do LAN

    Jeśli ta opcja jest włączona, urządzenia podłączone do routera mogą uzyskiwać dostęp do sieci LAN po stronie serwera VPN, co wymaga również odpowiednich ustawień po stronie serwera VPN.

    Na przykład na poniższym rysunku, gdy ta opcja jest włączona, oznacza to, że *Twoje urządzenie* może uzyskiwać dostęp do *NAS*, lecz nadal wymaga to, aby *serwer VPN* zezwolił na dostęp do NAS w swojej podsieci.

    ![allow remote access LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow"}

* Maskowanie IP

    Jeśli ta opcja jest włączona, gdy urządzenia klienckie w sieci LAN wysyłają pakiety IP, router zastępuje źródłowy adres IP swoim własnym adresem, a następnie przekazuje je do tunelu VPN.

* MTU

    Skrót od Maximum Transmission Unit (maksymalna jednostka transmisji). Wartość MTU ustawiona dla instancji nadpisuje parametr MTU zawarty w pliku konfiguracyjnym.

### Tryb proxy

![vpn proxy](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_proxy.png){class="glboxshadow"}

Jak na powyższym rysunku, aktualny tryb proxy to tryb globalny. Kliknij **Global Proxy**, aby przełączyć się na inny tryb. Dostępne są 3 typy: **Global Proxy**, **Policy Mode** i **Route Mode**.

1. Global Proxy

    Cały ruch będzie przesyłany przez VPN. Może być aktywna tylko jedna instancja klienta VPN.

2. Policy Mode

    1. Na podstawie docelowej domeny lub adresu IP.
    
        W tym trybie przez VPN będzie przesyłany tylko ruch określonych witryn, zdefiniowanych według adresu IP lub nazwy domeny. Może być aktywna tylko jedna instancja klienta VPN.

    2. Na podstawie urządzenia klienckiego.

        W tym trybie przez VPN będzie przesyłany tylko ruch wybranych lokalnych urządzeń klienckich, zidentyfikowanych według adresu MAC. Może być aktywna tylko jedna instancja klienta VPN.

    3. Na podstawie sieci VLAN.

        W tym trybie przez VPN może przechodzić tylko ruch z określonej sieci VLAN. Może być aktywna tylko jedna instancja klienta VPN.

3. Route Mode

    1. Automatyczne wykrywanie

        Stosowane są reguły routingu zdefiniowane w każdym pliku konfiguracyjnym klienta VPN lub wydane przez serwer VPN.
    
    2. Niestandardowe reguły routingu

        Możesz ręcznie skonfigurować reguły routingu dla każdej instancji klienta VPN.

### Opcje globalne klienta VPN

Kliknij **Global Options**, aby otworzyć okno dialogowe opcji globalnych.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_1.png){class="glboxshadow"}

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_client_2.png){class="glboxshadow"}

1. Blokuj ruch spoza VPN

    Jeśli ta opcja jest włączona, cały ruch urządzeń klienckich próbujący ominąć tunel VPN zostanie zablokowany. Skutecznie zapobiega to wyciekom VPN spowodowanym konfiguracją DNS klienta, zerwaniem połączenia VPN, żądaniami aplikacji klienckich bezpośrednio po adresie IP itp.

    Funkcja ta jest znana również jako [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Jej zadaniem jest ochrona danych przed wyciekiem do sieci. Większość dostawców VPN oferuje funkcję Kill Switch, która automatycznie odłącza komputer, telefon lub tablet od internetu w przypadku zerwania połączenia VPN. Funkcja blokowania ruchu spoza VPN w routerach GL.iNet obsługuje więcej scenariuszy naruszenia bezpieczeństwa, w tym poniższe sześć przypadków:

    1. Wyciek DNS

    2. Wyciek IPv6

    3. Wyciek WebRTC

    4. Zerwanie połączenia VPN

    5. Programy uruchamiane przed nawiązaniem połączenia VPN

    6. Wycieki specyficzne dla aplikacji

2. Zezwól na dostęp do WAN

    Jeśli ta opcja jest włączona, podczas aktywnego połączenia VPN urządzenia klienckie nadal będą mogły uzyskiwać dostęp do WAN, np. do drukarki lub NAS w nadrzędnej podsieci.

    ![vpn dashboard allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Jak pokazano powyżej, po włączeniu tej funkcji urządzenie zyska dostęp do urządzeń w podsieci nadrzędnej, takich jak drukarka czy NAS.

    Głównym zastosowaniem jest umożliwienie klientom dostępu do urządzeń w podsieci nadrzędnej. Router nie jest jednak w stanie rozróżnić podsieci nadrzędnej od Internetu, dlatego jeśli ruch z urządzeń klienckich jest kierowany bezpośrednio przez adres IP, może wystąpić ryzyko wycieku. Z tego powodu ta opcja i blokowanie ruchu spoza VPN wzajemnie się wykluczają.

3. Usługi GL.iNet używają VPN

    Jeśli ta opcja jest włączona, usługi routera, które zazwyczaj wymagają prawdziwego adresu IP, będą korzystać z VPN. Dotyczy to usług GoodCloud, DDNS i rtty. Rtty obejmuje funkcje **Remote SSH** i **Remote Web Access** dostępne na stronie [GoodCloud](cloud.md#enable-goodcloud-on-router).

    Głównym zastosowaniem jest jednoczesne używanie klienta VPN i usług [GoodCloud](cloud.md) / [DDNS](ddns.md). Zaleca się wyłączenie tej opcji, jeśli chcesz korzystać z GoodCloud – w przeciwnym razie stabilność GoodCloud będzie zależeć od stanu połączenia VPN. Jeśli chcesz używać DDNS, musisz wyłączyć tę opcję, gdyż w przeciwnym razie DDNS będzie wskazywał adres IP serwera VPN.

## Serwer VPN

Na początku oba serwery VPN nie są jeszcze skonfigurowane. Kliknij **Set Up Now**, aby przejść odpowiednio do stron [Serwer OpenVPN](openvpn_server.md) i [Serwer WireGuard](wireguard_server.md).

![vpn dashboard vpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server.png){class="glboxshadow"}

Po uruchomieniu serwera OpenVPN i serwera WireGuard:

![vpn dashboard vpn server started](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_vpn_server_started.png){class="glboxshadow"}

### Opcje serwera OpenVPN

Kliknij ikonę koła zębatego serwera OpenVPN.

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options_btn.png){class="glboxshadow"}

![openvpn server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_options.png){class="glboxshadow"}

* **Zezwalaj na zdalny dostęp do LAN**

    Jeśli ta opcja jest włączona, zasoby w podsieci LAN są dostępne przez tunel VPN.

* **Maskowanie IP**

    Jeśli ta opcja jest włączona, gdy urządzenia klienckie w sieci LAN wysyłają pakiety IP, router zastępuje źródłowy adres IP swoim własnym adresem, a następnie przekazuje je do tunelu VPN.

* **MTU**

    Wartość MTU ustawiona dla instancji nadpisuje parametr MTU zawarty w pliku konfiguracyjnym.

### Reguła routingu serwera OpenVPN

Kliknij ikonę sieci serwera OpenVPN.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule_btn.png){class="glboxshadow"}

W trybie niestandardowych tras klient VPN zignoruje plik konfiguracyjny oraz konfigurację routingu wydaną przez serwer. To, czy do uzyskania dostępu do danego segmentu sieci zostanie użyty szyfrowany tunel VPN, jest określane przez ręcznie zdefiniowane reguły routingu.

![openvpn server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/openvpn_server_route_rule.png){class="glboxshadow"}

### Opcje serwera WireGuard

Kliknij ikonę koła zębatego serwera WireGuard.

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options_btn.png){class="glboxshadow"}

![wireguard server options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_options.png){class="glboxshadow"}

* **Zezwalaj na zdalny dostęp do LAN**

    Jeśli ta opcja jest włączona, zasoby w podsieci LAN są dostępne przez tunel VPN.

* **Maskowanie IP**

    Jeśli ta opcja jest włączona, gdy urządzenia klienckie w sieci LAN wysyłają pakiety IP, router zastępuje źródłowy adres IP swoim własnym adresem, a następnie przekazuje je do tunelu VPN.

* **MTU**

    Wartość MTU ustawiona dla instancji nadpisuje parametr MTU zawarty w pliku konfiguracyjnym.

* **Client to Client**

    Klienci WireGuard mogą wymieniać dane między sobą, bez potrzeby stosowania połączeń lokacja–lokacja. Użytkownicy mogą zdalnie uzyskiwać dostęp do urządzeń w sieci domowej lub biurowej. Transfer danych przez serwer WireGuard jest bezpieczniejszy niż przekierowanie portów dzięki procesowi szyfrowania, a po nawiązaniu połączenia jest ono bardziej stabilne i szybsze.

### Reguła routingu serwera WireGuard

Kliknij ikonę sieci serwera WireGuard.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule_btn.png){class="glboxshadow"}

W trybie niestandardowych tras klient VPN zignoruje plik konfiguracyjny oraz konfigurację routingu wydaną przez serwer. To, czy do uzyskania dostępu do danego segmentu sieci zostanie użyty szyfrowany tunel VPN, jest określane przez ręcznie zdefiniowane reguły routingu.

![wireguard server route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/wireguard_server_route_rule.png){class="glboxshadow"}

### Opcje globalne serwera VPN

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_1.png){class="glboxshadow"}

![Global Options of VPN Server](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/global_options_of_vpn_server_2.png){class="glboxshadow"}

- **Kaskadowanie VPN** – jeśli ta opcja jest włączona, a na routerze działają jednocześnie serwer VPN i klient VPN, klienci podłączeni do serwera VPN będą dalej kierowani przez tunel klienta VPN. [Dowiedz się więcej o kaskadowaniu VPN](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
