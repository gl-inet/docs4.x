# Jak skonfigurować zaciemnianie VPN na routerach GL.iNet

## Czym jest zaciemnianie VPN

Zaciemnianie VPN to technika maskująca ruch VPN tak, aby wyglądał jak zwykły ruch internetowy. Pomaga ona użytkownikom omijać ograniczenia sieciowe i censurę, szczególnie w regionach o rygorystycznych przepisach internetowych.

- Maskuje charakterystykę VPN, aby zapobiec wykryciu przez dostawców internetu, zapory sieciowe lub Deep Packet Inspection (DPI).

- Sprawia, że połączenie VPN wygląda jak standardowy ruch sieciowy, poprawiając stabilność połączenia i skuteczność w sieciach z ograniczeniami.

## Czym jest AmneziaWG

AmneziaWG to protokół VPN zbudowany na bazie WireGuard, z wbudowanym zaciemnianiem ruchu. Zachowuje podstawowe zalety WireGuard, takie jak wysoka prędkość, lekka konstrukcja i niskie opóźnienie, jednocześnie dodając dedykowany moduł zaciemniania. Moduł ten skutecznie ukrywa wzorce ruchu VPN, umożliwiając zarówno użytkownikom indywidualnym, jak i firmowym ochronę prywatności online, omijanie ograniczeń regionalnych i unikanie przerw w połączeniu spowodowanych rygorystycznymi kontrolami sieciowymi.

AmneziaWG jest kompatybilny z szeroką gamą urządzeń, w tym Windows, macOS, iOS, Android, Linux i routerów, zapewniając niezawodne zaciemnione połączenia VPN we wszystkich scenariuszach.

Obecnie kilka routerów GL.iNet (np. **Brume 3**, **Flint 3**, **Flint 2** i **Beryl AX**) obsługuje protokół AmneziaWG w wybranych wersjach oprogramowania. Pełna oficjalna obsługa będzie dostępna w oprogramowaniu ver.4.9 i stopniowo rozszerzona na kolejne modele.

## Szybka konfiguracja

Poniżej przedstawiono dwa typowe scenariusze konfiguracji zaciemniania VPN AmneziaWG na routerach GL.iNet.

### Scenariusz 1. Korzystanie z dwóch routerów GL.iNet

W tym scenariuszu używane są dwa routery GL.iNet do ustanowienia połączenia VPN z zaciemnianiem przez protokół AmneziaWG.

- **Brume 3 (GL-MT5000)**: Działa jako serwer VPN do użytku domowego.
- **Beryl AX (GL-MT3000)**: Działa jako przenośny klient VPN do użytku w podróży. 

#### Konfiguracja serwera VPN

1. Zaloguj się do panelu administracyjnego Brume 3. 

    Podłącz urządzenie (np. laptop lub komputer) do portu LAN routera Brume 3 za pomocą kabla Ethernet. Otwórz przeglądarkę i wpisz domyślny adres administracyjny (zazwyczaj `192.168.8.1`), następnie zaloguj się hasłem administratora.

2. Ukończ wstępną konfigurację Brume 3 dla dostępu do internetu.

    Jeśli Brume 3 jest używany jako router główny, podłącz jego port WAN do sieci nadrzędnej, takiej jak modem ISP. 
    
    Jeśli nie jest routerem głównym (tj. istnieje inne urządzenie nadrzędne, takie jak router ISP, działające jako router główny), wymagana jest konfiguracja **przekierowania portów** na routerze głównym. Zapoznaj się z [tym linkiem](how_to_set_up_port_forwarding.md).

3. Włącz DDNS (opcjonalnie).

    Włącz funkcję DDNS, jeśli Twój publiczny adres IP nie jest statyczny, lecz dynamiczny.
    
    Z lewego paska bocznego przejdź do **APPLICATIONS** -> **Dynamic DNS**. Włącz **Enable DDNS**, zaakceptuj **Terms of Service & Privacy Policy**, następnie kliknij **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. Włącz zaciemnianie VPN. 

    Z lewego paska bocznego przejdź do **VPN** > **WireGuard Server** -> zakładka **Configurations**, włącz **Enable Obfuscation**, następnie kliknij **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Możesz dostosować parametry zaciemniania według potrzeb. Zalecamy pozostawienie ustawień domyślnych.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Eksportuj plik konfiguracyjny.

    Na stronie **WireGuard Server** przejdź do zakładki **Profiles**, kliknij przycisk **Add**, aby utworzyć plik konfiguracyjny dla połączenia Beryl AX.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Ustaw opisową nazwę (np. Travel Router), następnie kliknij **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    W wyskakującym oknie kliknij **Export**, aby pobrać konfigurację lokalnie, która będzie użyta później.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Uruchom serwer VPN. 

    U góry strony **WireGuard Server** kliknij przycisk **Start**, aby uruchomić serwer. 

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    Twój serwer VPN z zaciemnianiem AmneziaWG jest teraz włączony. Możesz teraz połączyć się z tym serwerem VPN Brume 3 przez aplikację AmneziaWG lub router GL.iNet z oprogramowaniem obsługującym zaciemnianie AmneziaWG. 
    
    **Uwaga: Klienci nie obsługujący zaciemniania AmneziaWG nie będą mogli się połączyć.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### Konfiguracja klienta VPN

1. Zaloguj się do panelu administracyjnego Beryl AX. 

    Podłącz urządzenie (np. laptop lub komputer) do sieci Wi-Fi lub portu LAN routera Beryl AX za pomocą kabla Ethernet. Otwórz przeglądarkę i wpisz domyślny adres administracyjny (zazwyczaj `192.168.8.1`), następnie zaloguj się hasłem administratora.

2. Ukończ wstępną konfigurację Beryl AX dla dostępu do internetu.

    **Wskazówka**: Połącz Beryl AX z siecią inną niż Brume 3. Możesz na przykład włączyć hotspot mobilny, aby Beryl AX się połączył.

3. Prześlij plik konfiguracyjny. 

    Z lewego paska bocznego przejdź do **VPN** > **WireGuard Client**. Dodaj nową grupę i ustaw opisową nazwę (np. Home Router).

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Prześlij wcześniej wyeksportowany plik konfiguracyjny po prawej stronie.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Po przesłaniu i weryfikacji pliku konfiguracyjnego kliknij **Apply**.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    Strona zostanie odświeżona, a na liście pojawi się jeden plik konfiguracyjny. 
    
4. Uruchom połączenie VPN.

    Kliknij ikonę trzech kropek, a następnie wybierz **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Odczekaj około 1 minuty. Jeśli wskaźnik statusu zmieni kolor na zielony, oznacza to, że połączenie VPN zostało nawiązane pomyślnie.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Przejdź do **VPN Dashboard**, gdzie zobaczysz, że Beryl AX został połączony z routerem domowym Brume 3.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Podwójna weryfikacja (opcjonalnie).

    Zaloguj się do panelu administracyjnego Brume 3, przejdź do **VPN** -> **WireGuard Server**. Zobaczysz także klienta online, którym jest Beryl AX, obecnie połączony z tym serwerem VPN Brume 3.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    Połączenie VPN jest ukończone. Wszystkie urządzenia w sieci Beryl AX uzyskują teraz dostęp do internetu przez bramę Brume 3, umożliwiając połączenie VPN z zaciemnianiem.

### Scenariusz 2. Korzystanie z pojedynczego routera GL.iNet

W tym scenariuszu używany jest pojedynczy router GL.iNet **Brume 3 (GL-MT5000)** jako klient VPN do połączenia z serwerem AmneziaVPN. 

W tym przypadku nie musisz wdrażać własnego serwera. Wystarczy pobrać plik konfiguracyjny AmneziaWG z [oficjalnej strony Amnezia](https://amnezia.org/){target="_blank"} lub od dowolnego dostawcy usług VPN integrującego AmneziaWG, a następnie przesłać plik do routera GL.iNet. Będziesz wtedy mógł nawiązać połączenie VPN z włączonym zaciemnianiem.

#### Pobieranie konfiguracji

<u>Opcja 1</u>: Pobierz konfigurację z oficjalnej Amnezia (wymagana subskrypcja Premium).

1. Zaloguj się do [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} przy użyciu klucza subskrypcji.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Na panelu Amnezia przejdź do **Connection Assets** -> **Configuration Files**, wybierz kraj i pobierz plik konfiguracyjny lokalnie do późniejszego użytku.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Opcja 2</u>: Pobierz konfigurację od innego dostawcy VPN integrującego AmneziaWG.

Weźmy jako przykład StarVPN.

1. Przejdź do [planów cenowych StarVPN](https://www.starvpn.com/#pricing){target="_blank"} i wybierz plan VPN odpowiadający Twoim potrzebom. Możesz zarejestrować konto StarVPN przy kasie lub bezpośrednio [tutaj](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

2. Zaloguj się do [panelu StarVPN](https://www.starvpn.com/dashboard){target="_blank"}, znajdź **VPN Configuration** i kliknij **AmneziaWG Config**, aby pobrać plik konfiguracyjny.
    
    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. Konfiguracja może zawierać adres IPv6. Aby uniknąć problemów z kompatybilnością i łącznością, otwórz plik .conf i usuń adres IPv6, jak pokazano poniżej.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Następnie wykonaj poniższe kroki, aby skonfigurować klienta VPN.

#### Konfiguracja klienta VPN

1. Zaloguj się do panelu administracyjnego Brume 3. 

    Podłącz urządzenie (np. laptop lub komputer) do portu LAN routera Brume 3 za pomocą kabla Ethernet. Otwórz przeglądarkę i wpisz domyślny adres administracyjny (zazwyczaj `192.168.8.1`), następnie zaloguj się hasłem administratora.

2. Ukończ wstępną konfigurację Brume 3 dla dostępu do internetu.

3. Prześlij plik konfiguracyjny. 

    Z lewego paska bocznego przejdź do **VPN** > **WireGuard Client**. Dodaj nową grupę i ustaw opisową nazwę (np. AmneziaVPN).

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Prześlij wcześniej wyeksportowany plik konfiguracyjny AmneziaVPN po prawej stronie.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Po przesłaniu i weryfikacji pliku konfiguracyjnego kliknij **Apply**.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    Strona zostanie odświeżona, a na liście pojawi się jeden plik konfiguracyjny. 
    
4. Uruchom połączenie VPN.

    Kliknij ikonę trzech kropek, a następnie wybierz **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Odczekaj około 1 minuty. Jeśli wskaźnik statusu zmieni kolor na zielony, oznacza to, że połączenie VPN zostało nawiązane pomyślnie.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Przejdź do **VPN Dashboard**, gdzie zobaczysz, że Brume 3 został połączony z serwerem AmneziaVPN.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}
    
    Połączenie VPN jest ukończone. Wszystkie urządzenia w sieci Brume 3 uzyskują teraz dostęp do internetu przez serwer AmneziaVPN, umożliwiając połączenie VPN z zaciemnianiem.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
