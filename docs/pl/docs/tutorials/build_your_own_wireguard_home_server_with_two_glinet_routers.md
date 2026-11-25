# Zbuduj własny serwer domowy WireGuard z dwoma routerami GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Ten artykuł przedstawi, jak skonfigurować router domowy jako serwer VPN WireGuard i router podróżny jako klienta VPN WireGuard, aby połączyć się zdalnie, dzięki czemu możesz korzystać z domowego adresu IP z routerem podróżnym w dowolnym miejscu.

Obejrzyj ten film lub zapoznaj się z poniższymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Ten film używa GL-MT5000 (Brume 3) i GL-MT3600BE (Beryl 7) do zademonstrowania konfiguracji VPN.)</small>

W poniższych krokach jako przykłady wykorzystamy GL-MT6000 (Flint 2) i GL-MT3000 (Beryl AX):

- GL-MT6000, router domowy, zostanie skonfigurowany jako serwer VPN WireGuard. Jeśli nie jest wymagana pojemność bezprzewodowa, można również rozważyć naszą bramę bezpieczeństwa GL-MT2500 lub inne modele.

- GL-MT3000, router podróżny, zostanie skonfigurowany jako klient VPN WireGuard do zdalnego połączenia z serwerem VPN w domu.

## Dlaczego warto zbudować własny domowy serwer WireGuard {#why-build-your-own-wireguard-home-server}

1. Używaj publicznego adresu IP sieci domowej, aby Twój ruch internetowy wyglądał, jakby pochodził z domu.
2. Uniknij miesięcznych opłat za usługi VPN innych dostawców.
3. Chroń swoją prywatność, przesyłając cały ruch internetowy przez szyfrowany tunel do sieci domowej.
4. Korzystaj z urządzeń w sieci domowej i lokalnych usług streamingowych z dowolnego miejsca.

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

    Zaloguj się do panelu administracyjnego GL.iNet. Wybierz **INTERNET** z menu po lewej stronie. Sprawdź topologię i szczegóły połączenia:

    Przy bezpośrednim połączeniu kablem Ethernet zobaczysz sekcję „Ethernet” ze szczegółami, takimi jak **Protocol**, **IP Address** i **Gateway**.

    Na ilustracji zaznaczono adres IP interfejsu WAN, który dostawca Internetu przydzielił routerowi GL.iNet.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Router GL.iNet pełni tu funkcję routera głównego i ma publiczny adres IP na interfejsie WAN, więc **przekierowanie portów nie jest wymagane**.

    Skonfiguruj router GL.iNet jako serwer WireGuard, a router podróżny jako klienta WireGuard łączącego się z tym serwerem. Między routerami powstanie tunel VPN.

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

1. Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **WireGuard Server**. Kliknij **Generate Configuration** (tylko przy początkowej konfiguracji serwera VPN).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Sprawdź konfigurację.

    Pokazana poniżej konfiguracja domyślna sprawdza się w większości przypadków.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address**: Jest to adres IP tunelu serwera WireGuard. Zmień go tylko w przypadku konfliktu z bramą routera nadrzędnego.

        Jeśli koliduje z bramą routera nadrzędnego, zmień go na inny, na przykład **10.1.0.1/24**, a następnie kliknij **Apply**. Upewnij się, że zapis CIDR „/24” jest zachowany, aby uniknąć problemów z łącznością.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Na przykład nadrzędny router Xfinity może mieć adres IP 10.0.0.1. Na niektórych routerach GL.iNet skonfigurowanych jako serwer WireGuard może on kolidować z adresem IP tunelu. Jeśli wystąpi konflikt, zastosuj powyższą zmianę.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**: Protokół IPv6 jest domyślnie wyłączony w routerach GL.iNet. Aby używać adresu IPv6, włącz [IPv6](../interface_guide/ipv6.md) na routerze.

    - **Listen Port**: Serwer WireGuard domyślnie nasłuchuje na porcie UDP `51820`. Jeśli zmienisz port nasłuchu i korzystasz z przekierowania portów, zaktualizuj regułę na routerze nadrzędnym tak, aby kierowała ruch na nowy port nasłuchu serwera. W parametrze `Endpoint` każdego profilu klienta podaj przekierowywany port zewnętrzny. Jeśli serwer jest dostępny bezpośrednio, użyj jego portu nasłuchu.

    - **Enable Obfuscation**: Po włączeniu tej opcji serwer VPN używa protokołu AmneziaWG do maskowania ruchu VPN. Zalecamy pozostawienie ustawień domyślnych i zmianę ich tylko wtedy, gdy znasz te parametry. Więcej informacji znajdziesz w poniższych artykułach.

        - [Maskowanie AmneziaWG na routerach GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Konfigurowanie maskowania VPN na routerach GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Dodaj profil.

    Przejdź do karty **Profiles** i kliknij przycisk **Add**, aby wygenerować profil dla swojego urządzenia.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Nadaj profilowi rozpoznawalną nazwę i kliknij **Apply**, aby kontynuować.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Jeśli chcesz zmienić ustawienia zaawansowane, kliknij **Set More**. Następnie kliknij **Apply**, aby kontynuować.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Dodaj reguły tras, jeśli to konieczne"

        W większości przypadków dodawanie reguł tras nie jest konieczne.

        Jeśli chcesz uzyskać z serwera dostęp do urządzeń LAN klienta WireGuard, przejdź do karty **Route Rules** na stronie **WireGuard Server** i skonfiguruj reguły tras. Kliknij [tutaj](../tutorials/wireguard_server_access_to_client_lan_side.md), aby uzyskać więcej instrukcji.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        W przeciwnym razie przejdź do kroku 4, aby pobrać konfigurację klienta.

4. Pobierz konfigurację.

    Po dodaniu profilu i kliknięciu **Apply** router udostępnia konfigurację jako kod QR, zwykły tekst lub plik `.conf` do pobrania.

    - **Kod QR**: Zeskanuj kod w aplikacji WireGuard, aby zaimportować standardowy profil WireGuard. Jeśli włączono maskowanie, użyj aplikacji AmneziaWG lub innego klienta obsługującego maskowanie AmneziaWG.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Zwykły tekst**: Możesz przejrzeć ustawienia, a następnie skopiować je i wkleić, aby ręcznie skonfigurować na przykład aplikację WireGuard lub router GL.iNet.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **Plik .conf**: Kliknij **Download**, aby zapisać plik `.conf` na urządzeniu. Plik możesz zaimportować bezpośrednio w aplikacji WireGuard lub na routerze GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    W razie potrzeby możesz wskazać adres serwera, wybierając spośród publicznego adresu IP, domeny DDNS i bieżącego adresu IP interfejsu WAN. Funkcja ta jest dostępna od wersji oprogramowania v4.8. Wybrany adres zostanie od razu zaktualizowany w pliku konfiguracyjnym.

    Na przykład, jeśli publiczny adres IP Twojej sieci często się zmienia, włącz [DDNS](../interface_guide/ddns.md) i użyj domeny DDNS jako adresu serwera.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Kliknij **Start** w prawym górnym rogu, aby uruchomić serwer WireGuard. Stan połączenia pojawi się na tej samej stronie.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Konfiguracja klienta WireGuard {#set-up-wireguard-client}

### Zmiana adresu IP LAN {#change-the-lan-ip}

Ponieważ używamy GL-MT6000 i GL-MT3000 jako przykładów w tym samouczku, których domyślne adresy IP LAN to oba **192.168.8.1**, musimy zmienić jeden z nich na inny adres IP LAN, aby uniknąć konfliktu. 

Poniższe kroki opisują zmianę adresu IP w sieci LAN routera GL-MT3000, który pełni funkcję klienta WireGuard.

Zaloguj się do panelu administracyjnego GL-MT3000 i przejdź do **NETWORK** -> **LAN**. Zmień domyślny adres IP 192.168.8.1 na inny, na przykład `192.168.20.1`.

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
