# Jak skonfigurować maskowanie ruchu VPN na routerach GL.iNet {#how-to-set-up-vpn-obfuscation-on-glinet-routers}

**Uwaga**: routery GL.iNet obsługują AmneziaWG w firmware v4.9 lub nowszym. Najpierw zaktualizuj router do obsługiwanej wersji firmware.

Ten przewodnik przedstawia dwa scenariusze konfiguracji maskowania ruchu AmneziaWG na routerach GL.iNet.

## Korzystanie z dwóch routerów GL.iNet {#using-two-glinet-routers}

W tym scenariuszu używane są dwa routery GL.iNet do ustanowienia połączenia VPN z maskowaniem ruchu przez protokół AmneziaWG.

- Brume 3 (GL-MT5000): serwer VPN do użytku domowego.
- Beryl AX (GL-MT3000): przenośny klient VPN do użytku w podróży.

### Konfiguracja serwera VPN {#set-up-vpn-server}

1. Zaloguj się do panelu administracyjnego Brume 3. 

    Podłącz urządzenie (np. laptop lub komputer) do portu LAN routera Brume 3 za pomocą kabla Ethernet. Otwórz przeglądarkę i wpisz domyślny adres administracyjny (zazwyczaj `192.168.8.1`), następnie zaloguj się hasłem administratora.

2. Ukończ wstępną konfigurację Brume 3 dla dostępu do internetu.

    Jeśli Brume 3 jest używany jako router główny, podłącz jego port WAN do sieci nadrzędnej, takiej jak modem ISP. 
    
    Jeśli nie jest routerem głównym (tj. istnieje inne urządzenie nadrzędne, takie jak router ISP, działające jako router główny), wymagana jest konfiguracja **przekierowania portów** na routerze głównym. Zobacz, jak [skonfigurować przekierowanie portów na routerze głównym](how_to_set_up_port_forwarding.md).

3. Włącz DDNS (opcjonalnie).

    Włącz funkcję DDNS, jeśli Twój publiczny adres IP nie jest statyczny, lecz dynamiczny.
    
    Z lewego paska bocznego przejdź do **APPLICATIONS** -> **Dynamic DNS**. Włącz **Enable DDNS**, zaakceptuj **Terms of Service & Privacy Policy**, następnie kliknij **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/enable_ddns.png){class="glboxshadow"}

4. Włącz maskowanie ruchu.

    Na lewym pasku bocznym przejdź do **VPN** -> **WireGuard Server** i otwórz kartę **Configurations**. Włącz **Enable Obfuscation** i kliknij **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Aby ręcznie ustawić parametry maskowania, kliknij **Set Obfuscation Parameters**, aby wyświetlić pola. Dostosuj wartości i kliknij **Apply**. Zalecamy zachowanie ustawień domyślnych i zmienianie ich tylko wtedy, gdy znasz te parametry. Zobacz [Maskowanie ruchu AmneziaWG na routerach GL.iNet](../faq/amneziawg_obfuscation.md).

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.jpg){class="glboxshadow"}

    Od wersji oprogramowania v4.11.1 możesz także zmienić wersję maskowania. Wybierz odpowiednią wersję z listy rozwijanej, kliknij **Regenerate**, a następnie **Apply**.

    Poniższy film pokazuje, jak to zrobić.

    <video src="https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/select_version.mp4"
        controls playsinline preload="metadata" width="800" style="max-width:100%;height:auto">
    Twoja przeglądarka nie obsługuje osadzonych filmów. Otwórz film demonstracyjny w nowej karcie, korzystając z linku <a href="https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/select_version.mp4" target="_blank" rel="noopener">select_version.mp4</a>.
    </video>

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

    Twój serwer VPN z maskowaniem ruchu AmneziaWG jest teraz włączony. Możesz teraz połączyć się z tym serwerem VPN Brume 3 przez aplikację AmneziaWG lub router GL.iNet z oprogramowaniem obsługującym maskowanie ruchu AmneziaWG.
    
    **Uwaga: Klienci nieobsługujący maskowania ruchu AmneziaWG nie będą mogli się połączyć.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

### Konfiguracja klienta VPN {#set-up-vpn-client}

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

    Połączenie VPN jest ukończone. Wszystkie urządzenia w sieci Beryl AX uzyskują teraz dostęp do internetu przez bramę Brume 3, umożliwiając połączenie VPN z maskowaniem ruchu.

## Korzystanie z jednego routera GL.iNet {#using-a-single-glinet-router}

W tym scenariuszu używany jest pojedynczy router GL.iNet **Brume 3 (GL-MT5000)** jako klient VPN do połączenia z serwerem AmneziaVPN. 

W tym przypadku nie musisz wdrażać własnego serwera. Wystarczy pobrać plik konfiguracyjny AmneziaWG z [oficjalnej strony Amnezia](https://amnezia.org/){target="_blank"} lub od dowolnego dostawcy usług VPN integrującego AmneziaWG, a następnie przesłać plik do routera GL.iNet. Będziesz wtedy mógł nawiązać połączenie VPN z włączonym maskowaniem ruchu.

### Pobieranie konfiguracji {#download-configuration}

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

### Konfiguracja klienta VPN {#set-up-vpn-client_1}

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
    
    Połączenie VPN jest ukończone. Wszystkie urządzenia w sieci Brume 3 uzyskują teraz dostęp do internetu przez serwer AmneziaVPN, umożliwiając połączenie VPN z maskowaniem ruchu.

---

Powiązane artykuły

- [Oficjalna dokumentacja AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}
- [Maskowanie ruchu AmneziaWG na routerach GL.iNet](../faq/amneziawg_obfuscation.md)

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
