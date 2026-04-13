# Zbuduj własny serwer domowy WireGuard z dwoma routerami GL.iNet

Ten artykuł przedstawi, jak skonfigurować router domowy jako serwer VPN WireGuard i router podróżny jako klienta VPN WireGuard, aby połączyć się zdalnie, dzięki czemu możesz korzystać z domowego adresu IP z routerem podróżnym w dowolnym miejscu.

Obejrzyj ten film lub zapoznaj się z poniższymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Ten film używa GL-MT5000 (Brume 3) i GL-MT3600BE (Beryl 7) do zademonstrowania konfiguracji VPN.)</small>

W poniższych krokach jako przykłady wykorzystamy GL-MT6000 (Flint 2) i GL-MT3000 (Beryl AX):

- GL-MT6000, router domowy, zostanie skonfigurowany jako serwer VPN WireGuard. Jeśli nie jest wymagana pojemność bezprzewodowa, można również rozważyć naszą bramę bezpieczeństwa GL-MT2500 lub inne modele.

- GL-MT3000, router podróżny, zostanie skonfigurowany jako klient VPN WireGuard do zdalnego połączenia z serwerem VPN w domu.

## Dlaczego warto zbudować własny serwer domowy WireGuard

1. Używaj swojego domowego adresu IP jako adresu internetowego, działając tak, jakbyś był właśnie w domu.
2. Nie trzeba płacić miesięcznej opłaty w porównaniu z usługami VPN od firm trzecich.
3. Kieruj cały ruch internetowy do sieci domowej przez szyfrowany tunel VPN i zabezpiecz swoją prywatność.
4. Łatwy dostęp do wewnętrznych zasobów i lokalnego streamingu.

## Przygotowania

### Sprawdź, czy masz publiczny adres IP

Najpierw upewnij się, że GL-MT6000 ma publiczny adres IP po stronie WAN, aby był dostępny globalnie. W przeciwnym razie router podróżny nie będzie mógł nawiązać połączenia VPN podczas podróży.

Aby sprawdzić, czy masz publiczny adres IP, otwórz przeglądarkę internetową i wpisz [what is my ip](https://whatismyipaddress.com/){target="_blank"} w pasku adresu.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Pokaże Twój publiczny adres IP. Jeśli zgadza się z adresem IP WAN dostarczonym przez Twojego dostawcę internetu dla GL-MT6000, masz publiczny adres IP.

Jeśli nie masz publicznego adresu IP, oto kilka metod dla Ciebie.

1. Jeśli masz router główny, zaloguj się do niego i sprawdź, czy otrzymuje publiczny adres IP od dostawcy internetu.
2. Poproś swojego dostawcę internetu o publiczny adres IP. Może to wymagać dodatkowej opłaty.
3. Jeśli powyższe dwie metody nie działają, na przykład jeśli jesteś w CGNAT, możesz skorzystać z metody odwrotnego proxy, takiej jak [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md). Alternatywnie możesz wypróbować rozwiązanie SDWAN - [AstroWarp](https://www.astrowarp.net/). 

### Sprawdź, czy wymagane jest przekierowanie portów

??? "GL.iNet jako router główny" 

    Jeśli router GL.iNet jest podłączony bezpośrednio do modemu ISP za pomocą kabla Ethernet, router GL.iNet jest routerem głównym.

    **Jak sprawdzić, czy router GL.iNet łączy się bezpośrednio z modemem ISP?**

    Kroki:
    
    1. Zaloguj się do panelu administracyjnego GL.iNet. 

    2. Wybierz INTERNET z lewego paska bocznego. Sprawdź topologię i szczegóły połączenia:

        Jeśli połączony bezpośrednio przez Ethernet, zobaczysz sekcję o nazwie "Ethernet" ze szczegółami takimi jak Protocol, IP address, Gateway itp.

        Biorąc poniższy obrazek jako przykład, zaznaczony adres IP to adres IP WAN dostarczony przez ISP dla tego routera GL.iNet. 

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Ten adres IP WAN jest publicznym adresem IP, więc ten router GL.iNet, działający jako router główny, ma publiczny IP i **nie ma potrzeby konfigurowania przekierowania portów dla niego**.

        Wystarczy skonfigurować ten router GL.iNet jako serwer WireGuard, a router podróżny jako klienta WireGuard łączącego się z serwerem. Wtedy tunel VPN zostanie zbudowany między nimi.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}
    
??? "GL.iNet jako router podrzędny"

    Skonfiguruj **przekierowanie portów** na routerze głównym dla routera GL.iNet, jeśli ten ostatni jest za NAT.

    Topologia

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

## Konfiguracja serwera WireGuard

### Włącz DDNS (opcjonalnie)

Włącz funkcję DDNS, jeśli nie masz statycznego publicznego adresu IP, a tylko dynamiczny publiczny adres IP.

Zaloguj się do panelu administracyjnego GL-MT6000 i przejdź do **APPLICATIONS** -> **Dynamic DNS**. Włącz przełącznik **Enable DDNS**.

Zaznacz pole **Terms of Service & Privacy Policy** i kliknij **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Następnie przejdź do zakładki **WireGuard Server** -> Configuration, upewnij się, że port nasłuchu to 51820, następnie kliknij **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Generowanie konfiguracji

Na tej samej stronie kliknij zakładkę **Profiles** obok zakładki Configuration, następnie kliknij **Add** (oznaczone jako 1 na poniższym obrazku).

Automatycznie wygeneruje konfigurację klienta. Kliknij **ikonę strzałki** (oznaczoną jako 2).

W wyskakującym oknie przesuń, aby włączyć DDNS Domain (oznaczone jako 3, co jest opcjonalne i włącz to tylko wtedy, gdy masz dynamiczny publiczny IP).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Następnie możesz zeskanować kod QR za pomocą [aplikacji mobilnej](https://www.wireguard.com/install/) WireGuard, aby przetestować serwer. Szczegóły kliknij [tutaj](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

Alternatywnie możesz wyeksportować konfigurację w formacie tekstowym dla połączenia klienta VPN.

Przełącz konfigurację z kodu QR na format tekstowy, klikając zakładkę **Configuration File**. 

Skopiuj tekst dla klienta lub kliknij przycisk Download i zapisz go do późniejszego użytku.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Konfiguracja klienta WireGuard

### Zmiana adresu IP LAN

Ponieważ używamy GL-MT6000 i GL-MT3000 jako przykładów w tym samouczku, których domyślne adresy IP LAN to oba **192.168.8.1**, musimy zmienić jeden z nich na inny adres IP LAN, aby uniknąć konfliktu. 

Oto kroki zmiany adresu IP LAN GL-MT3000 (klienta WireGuard).

Zaloguj się do panelu administracyjnego GL-MT3000, następnie przejdź do **NETWORK** z lewego paska bocznego -> **LAN**, aby zmienić adres IP LAN. Na przykład możesz zmienić adres IP LAN z domyślnego 192.168.8.1 na `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Aby uzyskać więcej szczegółów na temat interfejsu LAN, kliknij [tutaj](../interface_guide/lan.md).

### Dodaj konfigurację

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

### Uruchom połączenie

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

## Przygotowanie na zdalne naprawy VPN

W razie nieprzewidzianych problemów podczas podróży, wstępnie powiąż oba routery z kontem GoodCloud w celu zdalnego rozwiązywania problemów z VPN.

Czasami Twój serwer może być wyłączony z powodu awarii zasilania lub innych przyczyn. Aby utrzymać dostępność serwera, powiąż go z GL.iNet GoodCloud. 

---

Powiązane artykuły

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
