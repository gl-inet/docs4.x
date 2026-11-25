# Zbuduj własny serwer domowy WireGuard z dwoma routerami GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Ten artykuł przedstawi, jak skonfigurować router domowy jako serwer VPN WireGuard i router podróżny jako klienta VPN WireGuard, aby połączyć się zdalnie, dzięki czemu możesz korzystać z domowego adresu IP z routerem podróżnym w dowolnym miejscu.

Obejrzyj ten film lub zapoznaj się z poniższymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Ten film używa GL-MT5000 (Brume 3) i GL-MT3600BE (Beryl 7) do zademonstrowania konfiguracji VPN.)</small>

W poniższych krokach jako przykłady wykorzystamy GL-MT6000 (Flint 2) i GL-MT3000 (Beryl AX):

- GL-MT6000, router domowy, zostanie skonfigurowany jako serwer VPN WireGuard. Jeśli nie jest wymagana pojemność bezprzewodowa, można również rozważyć naszą bramę bezpieczeństwa GL-MT2500 lub inne modele.

- GL-MT3000, router podróżny, zostanie skonfigurowany jako klient VPN WireGuard do zdalnego połączenia z serwerem VPN w domu.

## Dlaczego warto zbudować własny serwer domowy WireGuard {#why-build-your-own-wireguard-home-server}

1. Używaj domowego adresu IP jako publicznego adresu IP, aby ruch wyglądał tak, jakby pochodził z domu.
2. Uniknij miesięcznych opłat pobieranych przez dostawców usług VPN.
3. Chroń swoją prywatność, szyfrując cały ruch internetowy przesyłany tunelem do sieci domowej.
4. Korzystaj z urządzeń domowych i lokalnych usług streamingowych z dowolnego miejsca.

## Przygotowania {#preparations}

### Sprawdź, czy masz publiczny adres IP {#check-if-you-have-a-public-ip}

Najpierw upewnij się, że GL-MT6000 ma publiczny adres IP po stronie WAN, aby był dostępny globalnie. W przeciwnym razie router podróżny nie będzie mógł nawiązać połączenia VPN podczas podróży.

Aby sprawdzić, czy masz publiczny adres IP, otwórz przeglądarkę internetową i wpisz [what is my ip](https://whatismyipaddress.com/){target="_blank"} w pasku adresu.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Pokaże Twój publiczny adres IP. Jeśli zgadza się z adresem IP WAN dostarczonym przez Twojego dostawcę internetu dla GL-MT6000, masz publiczny adres IP.

Jeśli nie masz publicznego adresu IP, oto kilka metod dla Ciebie.

1. Jeśli masz router główny, zaloguj się do niego i sprawdź, czy otrzymuje publiczny adres IP od dostawcy internetu.
2. Poproś swojego dostawcę internetu o publiczny adres IP. Może to wymagać dodatkowej opłaty.
3. Jeśli powyższe dwie metody nie działają (np. sieć znajduje się za CGNAT), możesz wypróbować nasze rozwiązanie SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Sprawdź, czy wymagane jest przekierowanie portów {#check-if-port-forwarding-is-required}

??? "GL.iNet jako router główny" 

    Jeśli router GL.iNet jest podłączony bezpośrednio do modemu ISP za pomocą kabla Ethernet, router GL.iNet jest routerem głównym.

    **Jak sprawdzić, czy router GL.iNet łączy się bezpośrednio z modemem ISP?**

    Zaloguj się do panelu administracyjnego GL.iNet. Wybierz **INTERNET** na lewym pasku bocznym i sprawdź topologię oraz szczegóły połączenia.

    Jeśli router jest podłączony bezpośrednio przez Ethernet, zobaczysz sekcję **Ethernet** z informacjami o protokole, adresie IP i bramie.

    Na poniższym zrzucie oznaczony adres IP to adres IP WAN przydzielony routerowi GL.iNet przez dostawcę internetu.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    W tym przykładzie adres IP WAN routera głównego GL.iNet jest publiczny, więc **przekierowanie portów nie jest potrzebne**.

    Wystarczy skonfigurować ten router GL.iNet jako serwer WireGuard, a router podróżny jako klienta WireGuard łączącego się z serwerem. Routery nawiążą tunel VPN.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet jako router podrzędny"

    Skonfiguruj **przekierowanie portów** na routerze głównym dla routera GL.iNet, jeśli ten ostatni jest za NAT.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Przykład: Router TP-Link jako Twój domowy router główny.

    Podłącz się do Wi-Fi lub LAN routera domowego. Następnie zaloguj się do panelu administracyjnego. Sprawdź adres IP WAN, który otrzymuje od Twojego ISP. Na poniższym obrazku widać, że Twój publiczny IP to **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Przed skonfigurowaniem przekierowania portów zalecamy zarezerwowanie adresu IP dla routera GL.iNet na routerze głównym, aby stały adres IP mógł być przypisany routerowi GL.iNet.** W przeciwnym razie, gdy router główny lub router GL.iNet uruchomi się ponownie, router główny może przypisać inny adres IP routerowi GL.iNet, powodując niepowodzenie reguły przekierowania portów.

    Następnie skonfiguruj przekierowanie portów na routerze głównym dla routera GL.iNet.

    1. Przejdź do "Advanced" i kliknij "virtual Server", następnie "Add".
    
    2. Internal IP (Device IP): To jest adres IP przypisany routerowi GL.iNet, możesz go znaleźć na liście klientów TP-Link
    
    3. External/Internal port:  Proszę wypełnić obie jako "51820"
    
    4. Protocol:  Możesz wybrać "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Więcej przykładów [przekierowania portów](how_to_set_up_port_forwarding.md)**

## Konfiguracja serwera WireGuard {#set-up-wireguard-server}

1. Zaloguj się do panelu administracyjnego w przeglądarce i przejdź do **VPN** -> **WireGuard Server**. Kliknij **Generate Configuration** tylko podczas pierwszej konfiguracji serwera VPN.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Sprawdź konfigurację.

    Pokazana poniżej konfiguracja domyślna sprawdza się w większości przypadków.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address**. To adres IP tunelu serwera WireGuard. Możesz go zachować, jeśli nie koliduje z adresem bramy routera nadrzędnego.

        Jeśli występuje konflikt, zmień adres na inny, na przykład **10.1.0.1/24**, i kliknij **Apply**. Uwzględnij prefiks CIDR `/24`, aby uniknąć problemów z łącznością.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Na przykład router Xfinity działający przed routerem GL.iNet może mieć adres IP 10.0.0.1. Ten adres może kolidować z adresem tunelu w niektórych modelach GL.iNet skonfigurowanych jako serwer WireGuard. Jeśli występuje konflikt, zmień adres zgodnie z instrukcją powyżej. W przeciwnym razie zachowaj adres domyślny.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. Na routerach GL.iNet protokół IPv6 jest domyślnie wyłączony. Aby użyć adresu IPv6, włącz [IPv6](../interface_guide/ipv6.md) na routerze.

    - **Listen Port**. Serwer WireGuard domyślnie nasłuchuje na porcie UDP `51820`. Jeśli zmienisz port i korzystasz z przekierowania portów, zaktualizuj regułę na routerze nadrzędnym, aby kierowała ruch na nowy port nasłuchu serwera. W polu `Endpoint` każdego profilu klienta wpisz port zewnętrzny wskazany w regule. Jeśli serwer jest dostępny bezpośrednio, użyj jego portu nasłuchu.

    - **Enable Obfuscation**. Po włączeniu tej opcji serwer VPN używa protokołu AmneziaWG do maskowania ruchu VPN. Zalecamy zachowanie ustawień domyślnych i zmienianie ich tylko wtedy, gdy znasz te parametry. Zobacz poniższe instrukcje.

        - [Maskowanie ruchu AmneziaWG na routerach GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Jak skonfigurować maskowanie ruchu VPN na routerach GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Dodaj profil.

    Przejdź do karty **Profiles** i kliknij **Add**, aby utworzyć profil dla urządzenia.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Wpisz nazwę ułatwiającą identyfikację i kliknij **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Aby zmienić ustawienia zaawansowane, kliknij **Set More**. Następnie kliknij **Apply**, aby kontynuować.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Dodaj reguły routingu w razie potrzeby"

        W większości przypadków nie trzeba dodawać reguł routingu.

        Aby uzyskać z serwera dostęp do urządzeń w sieci LAN klienta WireGuard, skonfiguruj reguły na karcie **Route Rules** na stronie **WireGuard Server**. Zobacz instrukcję [dostępu do sieci LAN klienta z serwera WireGuard](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Jeśli nie potrzebujesz dodatkowych reguł, przejdź do kroku 4, aby pobrać konfigurację klienta.

4. Pobierz konfigurację.

    Po dodaniu profilu i kliknięciu **Apply** router udostępnia konfigurację jako kod QR, zwykły tekst lub plik `.conf` do pobrania.

    - **QR code**. Zeskanuj kod w aplikacji WireGuard, aby zaimportować standardowy profil WireGuard. Jeśli włączono maskowanie ruchu, użyj aplikacji AmneziaWG lub innego klienta obsługującego maskowanie ruchu AmneziaWG.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**. Możesz przejrzeć szczegóły konfiguracji w formacie tekstowym i skopiować je do ręcznej konfiguracji, na przykład w aplikacji WireGuard lub na routerze GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**. Kliknij **Download**, aby zapisać plik .conf na swoim urządzeniu. Możesz go zaimportować bezpośrednio do aplikacji WireGuard lub przesłać na router GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    W razie potrzeby jako adres serwera możesz wybrać publiczny adres IP, domenę DDNS lub bieżący adres IP WAN. Ta funkcja jest dostępna od wersji oprogramowania v4.8. Po zmianie adres zostanie również zaktualizowany w pliku konfiguracyjnym.

    Jeśli na przykład publiczny adres IP sieci często się zmienia, włącz [DDNS](../interface_guide/ddns.md) i użyj domeny DDNS jako adresu serwera.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Kliknij **Start** w prawym górnym rogu, aby uruchomić serwer WireGuard. Stan połączenia pojawi się na tej samej stronie.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Konfiguracja klienta WireGuard {#set-up-wireguard-client}

### Zmiana adresu IP LAN {#change-the-lan-ip}

Ponieważ używamy GL-MT6000 i GL-MT3000 jako przykładów w tym samouczku, których domyślne adresy IP LAN to oba **192.168.8.1**, musimy zmienić jeden z nich na inny adres IP LAN, aby uniknąć konfliktu. 

Poniżej opisano, jak zmienić adres IP LAN routera GL-MT3000 działającego jako klient WireGuard.

Zaloguj się do panelu administracyjnego GL-MT3000 i przejdź do **NETWORK** -> **LAN**, aby zmienić adres IP LAN. Na przykład zamiast domyślnego adresu 192.168.8.1 możesz użyć adresu `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Dodaj konfigurację {#add-the-configuration}

W panelu administracyjnym GL-MT3000 przejdź do **VPN** -> **WireGuard Client** i kliknij **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Utwórz grupę po lewej stronie i ustaw nazwę, następnie wybierz plik konfiguracyjny do przesłania lub przeciągnij go do pola przesyłania po prawej stronie.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Po pomyślnej weryfikacji pliku kliknij **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Możesz także kliknąć **Manually Add Configuration** i wkleić tekst konfiguracji, następnie kliknij **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Plik konfiguracyjny zostanie wyświetlony na stronie WireGuard Client po pomyślnym przesłaniu.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Uruchom połączenie {#start-the-connection}

Kliknij ikonę trzech kropek i kliknij **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Odczekaj kilka minut. Po pomyślnym połączeniu zaświeci się zielona kropka.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Przejdź do **VPN Dashboard** i zobaczysz, że Twój klient łączy się z serwerem z Twoim domowym publicznym IP. Strona może się nieznacznie różnić w zależności od wersji oprogramowania.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Zaloguj się z powrotem do panelu administracyjnego GL-MT6000 (serwera WireGuard), przejdź do **VPN** -> **WireGuard Server** (lub przejdź do **VPN** -> **VPN Dashboard**, jeśli używasz oprogramowania v.4.7 i wcześniejszych), a także zobaczysz status połączenia, wskazujący, że klient jest połączony.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Strona WireGuard Server w FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Strona VPN Dashboard w FW v4.7 i wcześniejszych)</small>

## Przygotowanie na zdalne naprawy VPN {#prep-for-remote-vpn-fixes-ahead}

Przed podróżą powiąż oba routery z kontem GoodCloud. Umożliwi to zdalne rozwiązywanie problemów, jeśli połączenie VPN przestanie działać z powodu konfiguracji lub innych problemów sieciowych. Zdalny dostęp działa tylko wtedy, gdy routery pozostają włączone i połączone z Internetem.

---

Powiązane artykuły

- [Konfiguracja serwera WireGuard na routerach GL.iNet](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
