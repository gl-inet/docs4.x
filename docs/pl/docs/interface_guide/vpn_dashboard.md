# VPN Dashboard {#vpn-dashboard}

Treść tej strony dotyczy wersji firmware v4.9.x i nowszych. Jeśli urządzenie używa innej wersji firmware, użyj poniższego selektora, aby przejść do odpowiedniego przewodnika.

<div class="gl-link-select" data-label="Wersja firmware" data-placeholder="Firmware v4.9 i nowsze" markdown="1">

- [Firmware v4.7 i wcześniejsze](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

W lewym panelu webowego panelu administracyjnego przejdź do **VPN** -> **VPN Dashboard**.

VPN Dashboard wyświetla szczegóły połączenia VPN, takie jak reguły routingu, połączony serwer, statystyki ruchu, wirtualny adres IP klienta i dziennik połączeń, a także umożliwia konfigurację zaawansowanych ustawień, takich jak VPN Kill Switch, maskowanie IP i MTU.

W porównaniu z firmware v4.8 wersja v4.9 wprowadza następujące ulepszenia w VPN Dashboard:

1. **Umożliwia wybór wielu profili w grupie tunelu i ustawienie ich priorytetu**. Tunel będzie próbował połączyć się przy użyciu kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane.

2. **Każda grupa tuneli działa niezależnie i nie wykonuje przełączenia awaryjnego między grupami**. Jeśli wszystkie profile w pojedynczym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu funkcji Kill Switch tunelu oraz tunelu All Other Traffic.

## Prześlij profil VPN {#upload-vpn-profile}

Przy pierwszym wejściu na tę stronę, jeśli nie utworzono jeszcze żadnych tuneli, strona będzie wyglądać jak poniżej. Kliknij **Add VPN Tunnel**, aby rozpocząć.

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Zostaniesz przeniesiony na stronę **VPN Client Profile**. Wybierz dostawcę VPN i zaloguj się.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. Dostawcy VPN widoczni na powyższym zrzucie ekranu są zintegrowani z webowym panelem administracyjnym routera GL.iNet. Jeśli masz aktywną subskrypcję, wystarczy wprowadzić dane logowania, aby natychmiast się zalogować i pobrać pliki konfiguracyjne do połączeń VPN.

    2. Jeśli korzystasz z innego dostawcy VPN lub chcesz przesłać własne konfiguracje VPN, kliknij **Add Manually** i prześlij swoje konfiguracje.

Weźmy jako przykład [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Kliknij PureVPN i zaloguj się przy użyciu poprawnych danych logowania.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Otrzymasz listę profili VPN. W przypadku niektórych dostawców usług VPN przed wyświetleniem listy profili może być konieczne wybranie protokołu VPN lub preferowanych serwerów/miast.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Kliknij **Go to Dashboard** na dole strony. Zostaniesz przeniesiony do VPN Dashboard, gdzie możesz dodać tunel VPN i skonfigurować polityki VPN.

## Dodaj tunel VPN {#add-vpn-tunnel}

### Ogólne kroki {#general-steps}

Wykonaj poniższe kroki, aby dodać tunel VPN i skonfigurować polityki VPN. W razie potrzeby zapoznaj się z sekcją [Przykłady konfiguracji](#case-reference).

1. W VPN Dashboard kliknij **Add VPN Tunnel**. Po prawej stronie pojawi się kreator konfiguracji VPN.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Wybierz profil VPN.

    Wybierz jeden albo kilka profili, w razie potrzeby dostosuj ich priorytet po prawej stronie, a następnie kliknij **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Uwaga**: Gdy wybrano wiele profili, tunel będzie próbował połączyć się przy użyciu kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane. Jeśli wszystkie profile w jednym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN routera, na podstawie stanu funkcji Kill Switch w sekcji [Opcje tunelu](#tunnel-options) oraz ustawień [Cały pozostały ruch](#all-other-traffic).

3. Wybierz źródło ruchu klienta, a następnie kliknij **Next**.

    Dostępne są cztery opcje:

    - **All Clients**: po wybraniu tej opcji ruch ze wszystkich urządzeń będzie pasował do tej reguły.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: po wybraniu tej opcji ruch z określonych typów połączeń (np. podsieć LAN, Drop-in Gateway, Guest Network) będzie pasował do tej reguły.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych po adresie MAC) będzie pasował do tej reguły.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych po adresie MAC) nie będzie pasował do tej reguły.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Wybierz cel ruchu, a następnie kliknij **Apply**.

    Dostępne są trzy opcje:

    - **All Targets**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do wszystkich celów.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do określonych domen lub adresów IP. Trzeba je wprowadzić ręcznie.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły nie będzie kierowany do określonych domen lub adresów IP. Trzeba je wprowadzić ręcznie.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Tunel VPN został dodany. Zostaniesz przeniesiony do **VPN Dashboard**. W razie potrzeby dodaj kolejne tunele VPN.

    Ze względów bezpieczeństwa przed włączeniem tunelu VPN sprawdź stan funkcji **Kill Switch** w sekcjach [Cały pozostały ruch](#all-other-traffic) i [Opcje tunelu](#tunnel-options).

### Przykłady konfiguracji {#case-reference}

Poniżej znajdziesz dwa typowe przykłady konfiguracji polityk VPN wraz z instrukcjami krok po kroku.

??? note "Przypadek 1: kierowanie przez VPN ruchu tylko z określonych urządzeń."

    **Wymagania:**

    1. Tylko określone urządzenia podłączone do tego routera mają uzyskiwać dostęp do Internetu przez VPN. Wszystkie pozostałe urządzenia mają korzystać z lokalnego WAN.

    2. Wybrane urządzenia mają korzystać wyłącznie z połączenia VPN. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

    **Kroki konfiguracji:**

    1. Wybierz profil VPN.

        Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

        Weźmy jako przykład [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Wybierz źródło ruchu klienta.

        Kliknij kartę **Specified Devices**, wybierz urządzenia, które mają korzystać z VPN, a następnie kliknij **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Wybierz cel ruchu.

        Kliknij kartę **All Targets**, ustaw ją jako cel ruchu, a następnie kliknij **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Zostaniesz przeniesiony do VPN Dashboard. Tunel VPN został dodany, jak pokazano poniżej.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Upewnij się, że dla tego tunelu włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

    6. Upewnij się, że opcja **Allow Non-VPN Traffic** jest włączona. Jest ona domyślnie włączona, aby ruch niepasujący do tunelu VPN nadal mógł uzyskiwać dostęp do Internetu przez lokalny WAN.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Kliknij środkowy przycisk, aby aktywować ten tunel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Po nawiązaniu połączenia strona wyświetli szczegóły połączenia VPN, w tym politykę VPN, statystyki ruchu, adres serwera, port nasłuchu i wirtualny adres IP.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Od tej chwili tylko dwa wskazane urządzenia uzyskują dostęp do Internetu przez VPN. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP. Wszystkie pozostałe urządzenia będą uzyskiwać dostęp do Internetu przez lokalny WAN.

??? note "Przypadek 2: kierowanie ruchu wszystkich urządzeń do określonych witryn przez VPN 1, a całego pozostałego ruchu przez VPN 2."

    **Wymagania:**

    1. Wszystkie urządzenia mają korzystać z **VPN Tunnel 1** podczas uzyskiwania dostępu do domen określonych serwisów społecznościowych i usług streamingowych oraz z **VPN Tunnel 2** przy całym pozostałym dostępie do Internetu.

    2. Jeśli tunele VPN niespodziewanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

    **Kroki konfiguracji:**

    1. Wybierz profil VPN dla Tunnel 1.

        Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

        Weźmy jako przykład [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Wybierz jeden albo kilka profili, w razie potrzeby dostosuj ich priorytet po prawej stronie, a następnie kliknij **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Wybierz źródło ruchu klienta.

        Kliknij kartę **All Clients**, ustaw ją jako źródło ruchu klienta dla Tunnel 1, a następnie kliknij **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Wybierz cel ruchu.

        Kliknij kartę **Specified Domain / IP List**, wprowadź domeny kilku popularnych serwisów społecznościowych i usług streamingowych, jak pokazano poniżej, a następnie kliknij **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Zostaniesz przeniesiony do VPN Dashboard. Tunel VPN 1 został dodany.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Upewnij się, że dla Tunnel 1 włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

    6. Kliknij **Add New Tunnel**, aby dodać Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Wybierz profil VPN dla Tunnel 2.

        Weźmy jako przykład [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Wybierz źródło ruchu klienta.

        Kliknij kartę **All Clients**, ustaw ją jako źródło ruchu klienta dla Tunnel 2, a następnie kliknij **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Wybierz cel ruchu.

        Kliknij kartę **All Targets**, ustaw ją jako cel ruchu dla Tunnel 2, a następnie kliknij **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Zostaniesz przeniesiony do VPN Dashboard. Tunel VPN 2 został dodany.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Upewnij się, że dla Tunnel 2 włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Kliknij ikonę koła zębatego w prawym górnym rogu i włącz **Enhanced Kill Switch**. Dzięki temu cały ruch będzie musiał uzyskiwać dostęp do Internetu przez VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Kliknij środkowy przycisk, aby aktywować Tunnel 1 i Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Po nawiązaniu połączenia strona wyświetli szczegóły połączenia VPN, w tym politykę VPN, statystyki ruchu, adres serwera, port nasłuchu i wirtualny adres IP.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Teraz wszystkie urządzenia będą korzystać z **VPN Tunnel 1** podczas uzyskiwania dostępu do określonych domen oraz z **VPN Tunnel 2** przy całym pozostałym dostępie do Internetu. Jeśli tunele VPN niespodziewanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

## Kill Switch {#kill-switch}

!!! Tip "Czym jest Kill Switch?"

    Kill Switch VPN pomaga zapobiegać przełączeniu ruchu na nieszyfrowane połączenie internetowe w razie awarii połączenia VPN.

    Włączenie **Kill Switch** dla pojedynczego tunelu blokuje dostęp do Internetu dla ruchu przypisanego do tego tunelu, jeśli jego połączenie ulegnie awarii. Pozostały ruch podlega ustawieniom **All Other Traffic**.

    **Enhanced Kill Switch** blokuje ruch internetowy, który nie pasuje do żadnego tunelu VPN. Nie zastępuje ustawienia **Kill Switch** poszczególnych tuneli.

Od firmware v4.8 routery GL.iNet obsługują konfigurację funkcji Kill Switch dla globalnego połączenia VPN, a także dla każdego pojedynczego tunelu VPN.

- Aby skonfigurować Kill Switch dla globalnego połączenia VPN (czyli Enhanced Kill Switch), zobacz [Cały pozostały ruch](#all-other-traffic).

- Aby skonfigurować Kill Switch dla poszczególnych tuneli VPN, zobacz [Opcje tunelu](#tunnel-options).

## Cały pozostały ruch {#all-other-traffic}

Kliknij ikonę koła zębatego w prawym górnym rogu, aby skonfigurować politykę dla ruchu, który nie pasuje do tunelu VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Ta polityka określa, czy ruch, który nie pasuje do żadnej grupy tuneli VPN, może uzyskiwać dostęp do Internetu. Dostępne są dwie opcje: **Allow Non-VPN Traffic** i **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: opcja domyślnie włączona, aby zapewnić normalny dostęp do Internetu ruchowi spoza VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: wymusza, aby wszystkie urządzenia korzystały z Internetu przez VPN. Każdy ruch, który nie pasuje do tunelu VPN, zostanie zablokowany. To ustawienie globalne nie zastępuje ustawienia Kill Switch skonfigurowanego dla poszczególnych tuneli VPN.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Opcje tunelu {#tunnel-options}

Możesz skonfigurować zaawansowane ustawienia każdego tunelu VPN, takie jak VPN Kill Switch, maskowanie IP i MTU.

Kliknij ikonę koła zębatego w grupie tunelu i wybierz **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: jeśli opcja jest włączona, ruch pasujący do tego tunelu VPN zostanie zablokowany, jeśli połączenie VPN niespodziewanie się zerwie. Jeśli opcja jest wyłączona, taki ruch zostanie przełączony do tunelu **All Other Traffic**.

- **Services from GL.iNet Use VPN**: jeśli opcja jest włączona, usługi GoodCloud, DDNS i rtty będą przesyłać pakiety przez tunele VPN. Domyślnie ta opcja jest wyłączona, ponieważ usługi te zwykle wymagają prawdziwego adresu IP urządzenia do poprawnego działania.

- **Allow Remote Access to the LAN Subnet**: jeśli opcja jest włączona, zdalny dostęp do tego routera i jego urządzeń LAN przez VPN będzie dozwolony. Wymaga to, aby serwer VPN rozgłaszał trasę powrotną do swojej podsieci LAN.

- **IP Masquerading**: jeśli opcja jest włączona, źródłowe adresy IP klientów LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w konfiguracjach site-to-site, w których zdalny węzeł zna Twoje podsieci LAN.

    Jak pokazano poniżej, jeśli maskowanie IP jest włączone, gdy laptop (192.168.10.200) w sieci LAN routera podróżnego wysyła ruch przez tunel do domowego serwera NAS (192.168.8.100), router podróżny przepisuje źródłowy adres IP z `192.168.10.200` na adres tunelu klienta VPN `10.1.0.2`. Dzięki temu strona serwera widzi ruch jako pochodzący od klienta, a nie z lokalnej sieci LAN klienta.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU**: wartość MTU ustawiona dla tunelu zastąpi ustawienia MTU w pliku konfiguracyjnym.

## Priorytet tunelu {#tunnel-priority}

Aby dostosować priorytet tunelu, kliknij ikonę koła zębatego w grupie tunelu i wybierz **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Kliknij i przytrzymaj ikonę trzech linii po prawej stronie, aby zmienić kolejność tuneli, a następnie kliknij **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Gdy włączonych jest wiele tuneli, router kieruje ruch zgodnie z następującymi regułami**:

1. Ruch najpierw próbuje dopasować się do reguły tunelu o najwyższym priorytecie. Jeśli pasuje, zostanie skierowany przez ten tunel; w przeciwnym razie spróbuje dopasować się do tunelu o kolejnym priorytecie i tak dalej.

2. Każda grupa tuneli działa niezależnie. Gdy ruch dopasuje się do reguły tunelu, zostanie skierowany przez ten tunel i nie nastąpi przełączenie awaryjne między grupami tuneli.

3. W każdej grupie tuneli można wybrać wiele profili, aby umożliwić przełączenie awaryjne wewnątrz tunelu. Gdy profil o najwyższym priorytecie w grupie tunelu przestanie działać, tunel automatycznie połączy się przy użyciu profilu o drugim w kolejności priorytecie i tak dalej.

4. Jeśli tunel VPN niespodziewanie się rozłączy, system zdecyduje, czy przełączyć ruch do tunelu All Other Traffic, na podstawie tego, czy dla tego tunelu włączono **Kill Switch**.

    - Jeśli Kill Switch jest włączony, ruch zostanie zablokowany i nie zostanie przełączony do tunelu All Other Traffic.
    - Jeśli Kill Switch jest wyłączony, ruch zostanie przełączony do tunelu All Other Traffic.

5. W tunelu **All Other Traffic** różne tryby określają, czy ruch niepasujący do tunelu VPN może uzyskiwać dostęp do Internetu.

    - **Allow Non-VPN Traffic**: opcja domyślnie włączona, aby ruch niepasujący do tuneli VPN nadal mógł uzyskiwać dostęp do Internetu przez lokalny WAN.

    - **Enhanced Kill Switch**: wymusza, aby wszystkie urządzenia korzystały z Internetu przez VPN. Każdy ruch, który nie pasuje do tunelu VPN, zostanie zablokowany. To ustawienie globalne nie zastępuje ustawienia Kill Switch skonfigurowanego dla poszczególnych tuneli VPN. Krótko mówiąc, wzmacnia działanie Kill Switch i blokuje zwykły dostęp do Internetu, aby zapobiec wyciekom IP.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
