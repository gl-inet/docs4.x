# Tailscale

Tailscale to usługa VPN umożliwiająca bezpieczny i bezproblemowy dostęp do posiadanych urządzeń i aplikacji z dowolnego miejsca na świecie. Więcej informacji na temat Tailscale znajdziesz na [oficjalnej stronie Tailscale](https://tailscale.com/).

Funkcja Tailscale w routerach GL.iNet, dostępna od wersji oprogramowania v4.2, umożliwia routerowi dołączenie do wirtualnej sieci Tailscale. Po nawiązaniu połączenia możesz zdalnie uzyskiwać dostęp do routera, w tym do jego zasobów WAN i LAN.

**Uwaga**:

1. Ponieważ Tailscale jest oparty na WireGuard, nie zaleca się jednoczesnego używania Tailscale z żadną z poniższych funkcji ani usług, gdyż może to powodować konflikty routingu: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp.

2. Ta funkcja jest obecnie w wersji beta i może zawierać błędy.

3. Niektóre modele, mimo że działają na oprogramowaniu v4.2 lub nowszym, nie obsługują Tailscale z powodu niewystarczającej ilości pamięci.

## Obsługiwane modele
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Nieobsługiwane modele"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Konfiguracja sieci Tailscale

Poniżej pokazano przykład z użyciem modelu GL-MT2500.

1. Powiąż urządzenia.

    Najpierw zarejestruj konto Tailscale, a następnie powiąż jedno lub dwa urządzenia (np. smartfon, laptop) ze swoim kontem Tailscale do celów testowych.

    Po powiązaniu zobaczysz urządzenia i ich stan w konsoli administracyjnej Tailscale.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Włącz Tailscale na routerze GL.iNet.

    Zaloguj się do panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Włącz Tailscale przełącznikiem, a następnie kliknij **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Po krótkiej chwili interfejs wyświetli **Device Bind Link**. Kliknij Device Bind Link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    W wyskakującym oknie pojawi się link Tailscale. Kliknij go, aby przejść na stronę Tailscale i się zalogować.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Po zalogowaniu zostaniesz poproszony o potwierdzenie urządzenia, z którym chcesz się połączyć. Kliknij **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Po pomyślnym nawiązaniu połączenia zostaniesz automatycznie przekierowany do konsoli administracyjnej Tailscale. Zobaczysz, że adres IP modelu GL-MT2500 to `100.88.54.21`. Teraz możesz używać tego adresu IP do uzyskiwania dostępu do routera.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Przetestuj łączność.

    Na urządzeniach podłączonych do tej samej sieci Tailscale możesz przetestować łączność na trzy sposoby.

    * Użyj polecenia ping

        ![ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * Połącz się z routerem przez SSH

        ![ssh](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Uzyskaj dostęp do panelu administracyjnego w przeglądarce

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Zezwalanie na zdalny dostęp do WAN

> W firmware v4.9 i nowszych funkcja ta została przemianowana na **Advertise WAN Subnets**.

Po włączeniu tej opcji zasoby po stronie WAN urządzenia są dostępne przez wirtualną sieć Tailscale. Trasy zaczynają działać dopiero po zatwierdzeniu w Tailscale Admin Console.

Na przykład, jak pokazano w topologii poniżej, po włączeniu tej funkcji możesz uzyskać dostęp do `GL-AXT1800` za pośrednictwem jego adresu IP (`192.168.29.1`) z urządzenia `leo-phone`. Wynika to z tego, że GL-AXT1800 jest urządzeniem nadrzędnym względem `GL-MT2500`, a ten ostatni jest podłączony do tej samej sieci Tailscale co leo-phone.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Kroki konfiguracji są następujące.

1. Zaloguj się do panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **Tailscale**.

    Włącz **Allow Remote Access WAN** i kliknij **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Przejdź do konsoli administracyjnej Tailscale. Pojawi się alert informujący, że GL-MT2500 ma podsieci.

    Kliknij ikonę trzech kropek po prawej stronie GL-MT2500 i wybierz **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Włącz trasy podsieci.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Teraz możesz uzyskać dostęp do GL-AXT1800 za pośrednictwem jego adresu IP (`192.168.29.1`) z innych urządzeń. W praktyce możesz uzyskać dostęp do wszystkich urządzeń w podsieci `192.168.29.0/24`.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Zezwalanie na zdalny dostęp do LAN

> W firmware v4.9 i nowszych funkcja ta została przemianowana na **Advertise LAN Subnets**.

Po włączeniu tej opcji zasoby po stronie LAN urządzenia są dostępne przez wirtualną sieć Tailscale. Trasy zaczynają działać dopiero po zatwierdzeniu w Tailscale Admin Console.

Na przykład, jak pokazano w topologii poniżej, po włączeniu tej funkcji możesz zalogować się przez SSH do `Ubuntu` za pośrednictwem jego adresu IP (`192.168.8.110`) z urządzenia `leo-phone`. Wynika to z tego, że `Ubuntu` jest urządzeniem podrzędnym względem `GL-MT2500`, a ten ostatni jest podłączony do tej samej sieci Tailscale co leo-phone.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Kroki konfiguracji są następujące.

1. Zaloguj się do panelu administracyjnego routera i przejdź do **APPLICATIONS** -> **Tailscale**.

    Włącz **Allow Remote Access LAN** i kliknij **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Przejdź do konsoli administracyjnej Tailscale. Pojawi się alert informujący, że GL-MT2500 ma podsieci.

    Kliknij ikonę trzech kropek po prawej stronie GL-MT2500 i wybierz **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Włącz trasy podsieci.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Teraz możesz wysyłać ping lub logować się przez SSH do Ubuntu przy użyciu jego adresu IP (`192.168.8.110`) z innych urządzeń. W praktyce możesz uzyskać dostęp do wszystkich urządzeń w podsieci `192.168.8.0/24`.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Własne węzły wyjściowe

Domyślnie Tailscale działa jako sieć nakładkowa: kieruje ruch wyłącznie między urządzeniami z uruchomionym Tailscale i nie przetwarza publicznego ruchu internetowego — na przykład podczas przeglądania witryn takich jak Google.

Mogą jednak zaistnieć sytuacje, w których chcesz, aby Tailscale kierował Twój publiczny ruch internetowy. Na przykład, gdy jesteś poza domem lub podróżujesz za granicę i potrzebujesz dostępu do usług online (np. bankowości) dostępnych wyłącznie w Twoim kraju, możesz ustawić domowy komputer stacjonarny z publicznym adresem IP jako Exit Node, a następnie skonfigurować inne urządzenia w tej samej sieci Tailnet — takie jak GL-AXT1800 i GL-MT3000 widoczne na poniższym obrazku — aby kierowały przez niego swój ruch. Dzięki temu cały publiczny ruch internetowy będzie przekazywany przez Exit Node.

![exitnode](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Gdy cały ruch jest kierowany przez Exit Node, efektywnie korzystasz z domyślnych tras (0.0.0.0/0, ::/0), co działa podobnie jak zwykłe połączenie VPN.

Podsumowując, Exit Node kieruje wychodzący ruch internetowy z urządzeń w sieci Tailnet, działając w praktyce jak serwer VPN. Po połączeniu z Exit Node cały ruch internetowy niebędący ruchem Tailscale wygląda tak, jakby pochodził z jego lokalizacji, co pomaga uzyskać dostęp do treści ograniczonych geograficznie i zwiększa prywatność online. Urządzenie obsługujące to przekazywanie ruchu jest określane jako „Exit Node”.

**Uwaga**: Jeśli serwer DNS routera używa prywatnego adresu IP dostępnego wyłącznie w sieci lokalnej, po uruchomieniu Exit Node możesz utracić dostęp do Internetu. Aby rozwiązać ten problem, zaloguj się do routera, przejdź do **NETWORK** -> **DNS** i ręcznie ustaw publiczny serwer DNS, na przykład 8.8.8.8.

---

W poniższym przykładzie router GL.iNet **GL-MT2500** i **Leo-Desktop** znajdują się w tej samej sieci Tailnet. Poniżej opisano kroki konfiguracji Leo-Desktop jako Exit Node.

1. Włącz trasy podsieci dla GL-MT2500 w konsoli administracyjnej Tailscale.

    Przejdź do konsoli administracyjnej Tailscale, kliknij ikonę trzech kropek po prawej stronie GL-MT2500 i wybierz **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    W wyskakującym oknie włącz trasy podsieci.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Na urządzeniu, które ma pełnić rolę Exit Node, takim jak Leo-Desktop w tym przykładzie, wybierz **Run exit node**. Poniżej przykład dla systemu Windows.

    ![tailscale windows run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Następnie kliknij **Yes**.

    ![tailscale windows run exit ndoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. W konsoli administracyjnej Tailscale skonfiguruj Leo-Desktop jako Exit Node.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Zaloguj się do panelu administracyjnego GL-MT2500, przejdź do **APPLICATIONS** -> **Tailscale** i włącz **Custom Exit Nodes**. Kliknij przycisk odświeżania, wybierz adres IP Leo-Desktop z menu rozwijanego, a następnie kliknij **Apply**.

    ![glinet tailscale custom exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Urządzenia podłączone do routera będą wtedy kierować swój ruch przez Exit Node, aby uzyskać dostęp do Internetu, a cały ruch internetowy będzie wyglądał tak, jakby pochodził z lokalizacji Exit Node.

5. **Rozwiązywanie problemów**: Jeśli po włączeniu **Custom Exit Node** urządzenia podłączone do routera GL.iNet nie mają dostępu do Internetu, sprawdź, czy w konsoli administracyjnej Tailscale włączono trasy podsieci routera.

    W panelu administracyjnym routera może pojawić się odpowiedni komunikat, jak pokazano poniżej.

    ![exit node troubleshooting](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Aby rozwiązać problem, włącz trasy podsieci routera w konsoli administracyjnej Tailscale zgodnie z **Krokiem 1** powyżej.

## Run Exit Node

> Ta funkcja została wprowadzona w firmware v4.9.

Uruchomienie węzła wyjściowego na routerze pozwala innym urządzeniom w tailnet kierować cały wychodzący ruch internetowy przez publiczny adres IP tego routera.

W poniższej topologii laptop znajduje się w Bostonie, a router GL-BE9300 w Hongkongu. Oba urządzenia zostały dodane do tego samego tailnet Tailscale. Po ustawieniu GL-BE9300 jako węzła wyjściowego cały ruch wychodzący laptopa będzie wychodził do Internetu przez ten router w Hongkongu, a zewnętrzny publiczny adres IP laptopa będzie rozpoznawany jako adres IP z Hongkongu, a nie z Bostonu.

![topology run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Wskazówka**: Zalecamy wyłączenie wygasania klucza dla węzła wyjściowego, aby uniknąć przerw w łączności po wygaśnięciu klucza uwierzytelniania.*

Wykonaj te kroki, aby skonfigurować GL-BE9300 jako Exit Node.

1. Dodaj GL-BE9300 i laptop podróżny do tego samego tailnet Tailscale.

    ![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. W Web Admin Panel urządzenia GL-BE9300 włącz **Run Exit Node** i kliknij **Apply**.

    ![run exit node1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. W Tailscale Admin Console pod GL-BE9300 pojawi się etykieta "Exit Node".

    ![run exit node2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Kliknij ikonę trzech kropek obok GL-BE9300 i wybierz **Edit route settings**.

    ![run exit node3](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. Zaznacz **Use as exit node** i kliknij **Save**.

    ![run exit node4](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Wyłącz wygasanie klucza.

    Ze względów bezpieczeństwa użytkownicy muszą okresowo ponownie uwierzytelniać się na każdym ze swoich urządzeń. Aby uniknąć przerw w łączności po wygaśnięciu klucza uwierzytelniania węzła wyjściowego, zalecamy wyłączenie wygasania klucza dla węzła wyjściowego. Kliknij [tutaj](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"}, aby dowiedzieć się więcej o wygasaniu kluczy.

    Kliknij ikonę trzech kropek po prawej stronie GL-BE9300 i wybierz **Disable key expiry**.

    ![disable key expiry1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    Następnie pojawi się etykieta "Expiry disabled".

    ![disable key expiry2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Wybierz GL-BE9300 jako węzeł wyjściowy dla laptopa podróżnego.

    Uruchom Tailscale na laptopie podróżnym. Ikona Tailscale pojawi się w zasobniku systemowym w prawym dolnym rogu.

    Kliknij ikonę prawym przyciskiem myszy, kliknij **Exit nodes** i wybierz **gl-be9300**.

    ![run exit node5](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    Od tej chwili cały ruch wychodzący z tego laptopa podróżnego będzie wychodził do Internetu przez GL-BE9300.

8. Przetestuj łączność.

    1. Na laptopie podróżnym otwórz przeglądarkę i odwiedź [ipcheck.ing](https://ipcheck.ing/){target="_blank"} lub inną stronę do sprawdzania IP. Strona wyświetli publiczny adres IP należący do węzła wyjściowego Tailscale, potwierdzając, że laptop uzyskuje dostęp do Internetu przez ten węzeł wyjściowy, w tym przykładzie przez GL-BE9300 w Hongkongu.

        ![ip hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Naciśnij `Win+R`, wpisz `cmd`, aby uruchomić Wiersz polecenia, a następnie uruchom `tracert google.com`, aby prześledzić trasy ruchu wychodzącego. Wynik polecenia pokazuje wszystkie przeskoki routingu dla ruchu internetowego. Jeśli konfiguracja jest poprawna, pierwszy zewnętrzny przeskok będzie prowadził przez węzeł wyjściowy, jak pokazano poniżej.

        ![tracert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Odłącz węzeł wyjściowy, aby wykonać test porównawczy.

        Kliknij prawym przyciskiem myszy ikonę Tailscale w zasobniku systemowym w prawym dolnym rogu, kliknij **Exit nodes**, a następnie wybierz **None**, aby przestać używać węzła wyjściowego.

        ![comparative test](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Otwórz nową kartę przeglądarki i odwiedź [ipcheck.ing](https://ipcheck.ing/){target="_blank"} lub inny serwis sprawdzania IP. Teraz zostanie pokazany natywny publiczny adres IP laptopa, co dowodzi, że urządzenie używa lokalnego połączenia internetowego, w tym przykładzie z Bostonu.

        ![ip boston](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}

---

Odniesienia: [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
