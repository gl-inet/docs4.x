# VPN Dashboard (Oprogramowanie v4.8)

**Uwaga**: Ten przewodnik dotyczy oprogramowania v4.8. W przypadku wcześniejszych wersji zapoznaj się z dokumentacją [tutaj](vpn_dashboard_v4.7.md).

---

W panelu administracyjnym przejdź do **VPN** -> **VPN Dashboard**.

VPN Dashboard wyświetla szczegóły połączenia VPN, takie jak reguły tunelu, adres serwera, statystyki ruchu, wirtualny adres IP klienta oraz dziennik połączeń. Umożliwia także konfigurację zaawansowanych ustawień, takich jak Kill Switch VPN, maskowanie IP i MTU.

Możesz również aktywować wiele połączeń VPN w scenariuszach z wieloma tunelami.

## Kreator konfiguracji {#vpn-setup-wizard}

Kliknij ikonę książki w lewym górnym rogu i postępuj zgodnie z Kreatorem konfiguracji VPN, aby szybko ukończyć konfigurację VPN.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Uwaga**: Kreator konfiguracji VPN jest przeznaczony wyłącznie dla zintegrowanych usług VPN: AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA i Surfshark. W przypadku innych dostawców VPN pomiń kreator i skonfiguruj VPN ręcznie na stronie [Klient OpenVPN](openvpn_client.md){target="_blank"} lub [Klient WireGuard](wireguard_client.md){target="_blank"}.

Poniżej przedstawiono przykład z usługą **Hide.me**. Zaloguj się za pomocą danych logowania Hide.me.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Wybierz serwer VPN i kliknij **Apply**. Jest to serwer, z którym połączysz się przez ten tunel VPN, a Twój publiczny adres IP będzie widoczny jako adres z lokalizacji wybranego serwera.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

Połączenie zostanie nawiązane automatycznie. Po pomyślnym połączeniu przejdź do VPN Dashboard – zobaczysz, że tunel VPN jest włączony.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Wyświetlany jest aktualnie używany protokół VPN (np. WireGuard), plik konfiguracyjny, adres serwera, port nasłuchu serwera, statystyki ruchu oraz wirtualny adres IP klienta. Dziennik połączenia można wyświetlić w prawym dolnym rogu.

Wszyscy podłączeni klienci będą uzyskiwać dostęp do Internetu przez ten tunel VPN.

Aby skonfigurować politykę VPN, zapoznaj się z sekcją [Tryb polityk](#policy-mode).

## Tryb VPN

Na VPN Dashboard kliknij przycisk w prawym górnym rogu, aby przełączyć tryb VPN.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Dostępne są dwa tryby: tryb globalny (**Global Mode**) i tryb polityk (**Policy Mode**).

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Tryb globalny

W tym trybie cały ruch jest kierowany przez tunel VPN. Może być aktywna tylko jedna instancja klienta VPN.

Jest to idealne rozwiązanie w scenariuszach, gdy cały ruch kliencki ma być kierowany przez jeden serwer VPN, np. w celu ujednolicenia zabezpieczeń sieci lub dostępu do treści z określonego regionu.

W poniższym przykładzie router łączy się z serwerem australijskim za pomocą protokołu WireGuard. Cały ruch z podłączonych klientów będzie kierowany przez ten tunel VPN.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### Tryb polityk {#policy-mode}

W tym trybie router może łączyć się z wieloma serwerami VPN, a użytkownik może definiować niestandardowe reguły routingu dla różnych klientów lub celów ruchu.

Jest to odpowiednie rozwiązanie w scenariuszach wymagających elastycznego zarządzania ruchem, np. kierowania różnego ruchu do różnych celów przez wiele serwerów VPN.

Przełącz tryb VPN na tryb polityk i kliknij **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Po przełączeniu, jeśli VPN nie jest włączone, strona wygląda jak poniżej – zawiera trzy sekcje: Tunel podstawowy, Dodaj tunel oraz Cały pozostały ruch.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Kliknij odpowiednią sekcję, aby dowiedzieć się więcej.

- [Tunel podstawowy](#primary-tunnel)
- [Dodaj tunel](#add-tunnel)
- [Cały pozostały ruch](#all-other-traffic)

#### Tunel podstawowy {#primary-tunnel}

Tunel podstawowy to <u>predefiniowany</u> tunel w trybie polityk. Ma najwyższy priorytet. Jeśli istnieje więcej niż jeden tunel, możesz zmienić [priorytet tuneli](#tunnel-priority).

W tym tunelu możesz dostosować regułę tunelu, ustawiając trzy parametry:

1. **From** (Źródło ruchu): określa źródło ruchu, czyli ruch, który powinien być kierowany przez ten tunel.

    Kliknij wyszarzone pole, aby wybrać źródło ruchu.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}
        
    - **All Clients**: po wybraniu tej opcji ruch ze wszystkich urządzeń będzie pasował do tej reguły.
        
        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: po wybraniu tej opcji ruch z określonych typów połączeń (np. podsieci LAN, bramy drop-in, sieci gościnnej) będzie pasował do tej reguły.
        
        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Jeśli na routerze włączono serwer OpenVPN lub serwer WireGuard, w sekcji **Specified Connection Types** pojawią się dodatkowe opcje. Jest to przydatne przy [kaskadowaniu VPN](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych przez adres MAC) będzie pasował do tej reguły.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych przez adres MAC) **NIE** będzie pasował do tej reguły.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To** (Cel ruchu): określa docelowe miejsca ruchu.

    Kliknij wyszarzone pole, aby wybrać cele ruchu.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}
    
    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do wszystkich celów.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}
    
    - **Specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do określonych domen lub adresów IP. Należy je wprowadzić ręcznie.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Możesz też przełączyć **Input Mode** z trybu Manual na Subscription URL i podać adres URL.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note
        
            - Po wybraniu Subscribe URL nazwa domeny lub adres IP z podanego URL będą automatycznie aktualizowane każdego dnia.

            - Upewnij się, że podany URL jest poprawny. Mechanizm wykrywania URL weryfikuje ważność nazwy domeny lub adresu IP. [Dowiedz się więcej](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły **NIE** będzie kierowany do określonych domen lub adresów IP. Należy je wprowadzić ręcznie.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Możesz też przełączyć **Input Mode** z trybu Manual na Subscription URL i podać adres URL.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"} 

        !!! Note
        
            - Po wybraniu Subscribe URL nazwa domeny lub adres IP z podanego URL będą automatycznie aktualizowane każdego dnia.

            - Upewnij się, że podany URL jest poprawny. Mechanizm wykrywania URL weryfikuje ważność nazwy domeny lub adresu IP. [Dowiedz się więcej](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via** (Metoda routingu): określa metodę routingu ruchu, czyli czy ma być używany VPN.

    Kliknij wyszarzone pole, aby wybrać metodę routingu.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do wybranych celów przez VPN.
        
        Aby rozpocząć, skonfiguruj router jako klienta VPN. Użyj [Kreatora konfiguracji VPN](#vpn-setup-wizard), aby szybko ukończyć konfigurację, lub przejdź do Klienta OpenVPN / Klienta WireGuard na lewym pasku bocznym, aby skonfigurować ją ręcznie.

        Po skonfigurowaniu routera jako klienta VPN wybierz plik konfiguracyjny VPN dla tego tunelu i kliknij **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do wybranych celów przez lokalny interfejs WAN, a nie przez VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Po wybraniu źródła ruchu, celu ruchu i metody routingu konfiguracja reguły tunelu podstawowego jest gotowa.

W poniższym przykładzie reguła tunelu podstawowego jest następująca: wszyscy klienci używają VPN, aby uzyskać dostęp do określonych domen. Ich ruch jest kierowany przez serwer australijski i wychodzi do wybranych domen internetowych przez ten tunel.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Uwaga**: Ze względów bezpieczeństwa przed włączeniem tuneli przejdź do sekcji [Cały pozostały ruch](#all-other-traffic) i [Opcje tunelu](#tunnel-options), aby sprawdzić pozostałe ustawienia.

#### Dodaj tunel {#add-tunnel}

Aby utworzyć dodatkowe tunele dla wielu instancji VPN, kliknij **Add Tunnel** pod tunelem podstawowym i skonfiguruj niestandardowe reguły.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Nadaj tunelowi nazwę.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Na stronie VPN Dashboard pojawi się kolejny tunel.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

W razie potrzeby możesz dodać więcej tuneli. Można utworzyć maksymalnie 5 tuneli (wliczając predefiniowany tunel podstawowy).

Skonfiguruj reguły tunelu, ustawiając źródło ruchu, cele ruchu i metodę routingu. Zapoznaj się z sekcją [Tunel podstawowy](#primary-tunnel).

**Uwaga**: Ze względów bezpieczeństwa przed włączeniem tuneli przejdź do sekcji [Cały pozostały ruch](#all-other-traffic) i [Opcje tunelu](#tunnel-options), aby sprawdzić pozostałe ustawienia.

#### Cały pozostały ruch {#all-other-traffic}

W trybie polityk u dołu VPN Dashboard wyświetlany jest <u>domyślnie włączony</u> tunel.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Ten tunel kontroluje, czy ruch, który nie pasuje do żadnej z powyższych grup tuneli VPN, może uzyskiwać dostęp do Internetu. Jest domyślnie włączony, aby zapewnić normalny dostęp do Internetu dla ruchu niekierowanego przez VPN.

- Gdy jest włączony, ruch niedopasowany nadal może uzyskiwać dostęp do Internetu.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Gdy jest wyłączony, dostęp do Internetu jest dozwolony wyłącznie dla ruchu kierowanego przez VPN. Cały ruch spoza VPN oraz ruch po nieudanym przełączeniu awaryjnym z połączeń VPN zostanie zablokowany. Ta opcja nie nadpisuje indywidualnych ustawień Kill Switch dla każdego tunelu VPN.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Priorytet tunelu {#tunnel-priority}

Domyślnie predefiniowany tunel podstawowy ma najwyższy priorytet, następnie kolejne ręcznie dodane tunele (jeśli istnieją), a na końcu tunel Cały pozostały ruch – zapewniający łączność z siecią lokalną (przez lokalny WAN).

Aby zmienić priorytet tunelu, kliknij **Modify Priority** na górnym pasku informacyjnym lub kliknij **etykietę priorytetu** w lewym górnym rogu dowolnego tunelu (np. Priority 1/Priority 2).

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Kliknij i przytrzymaj ikonę trzech linii po prawej stronie, aby zmienić kolejność tuneli, a następnie kliknij **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Gdy włączonych jest wiele tuneli, router kieruje ruchem w następującej kolejności**:

1. Ruch najpierw próbuje dopasować regułę tunelu o najwyższym priorytecie. Jeśli pasuje, jest kierowany przez ten tunel; w przeciwnym razie próbuje dopasować tunel o następnym priorytecie i tak dalej, aż dopasuje tunel „Cały pozostały ruch".

2. Jeśli tunel VPN rozłączy się niespodziewanie, system na podstawie stanu **Kill Switch** tego tunelu decyduje, czy przekierować ruch do tunelu o kolejnym priorytecie.

    - Jeśli Kill Switch jest włączony, ruch zostanie zablokowany i nie zostanie przekierowany do tunelu o kolejnym priorytecie.
    - Jeśli Kill Switch jest wyłączony, ruch zostanie przekierowany do tunelu o kolejnym priorytecie i spróbuje dopasować jego reguły.

3. Tunel **Cały pozostały ruch** jest domyślnie włączony, aby ruch niedopasowany do tuneli VPN nadal miał dostęp do Internetu.

    - Gdy jest włączony, kieruje niedopasowany ruch lub ruch po przełączeniu awaryjnym przez lokalny WAN.
    - Gdy jest wyłączony, wzmacnia działanie Kill Switch i blokuje zwykły dostęp do Internetu, zapobiegając wyciekom adresu IP.

#### Opcje tunelu {#tunnel-options}

Możesz skonfigurować zaawansowane ustawienia każdego tunelu VPN, takie jak Kill Switch VPN, maskowanie IP i MTU.

Kliknij ikonę koła zębatego obok nazwy tunelu i wybierz **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: jeśli włączony, ruch pasujący do tego tunelu VPN zostanie zablokowany w przypadku niespodziewanego zerwania połączenia VPN. Jeśli wyłączony, taki ruch zostanie przekierowany do tunelu o kolejnym priorytecie lub przez lokalny WAN.

- **Services from GL.iNet Use VPN**: jeśli włączony, usługi GoodCloud, DDNS i rtty będą przesyłać pakiety przez tunele VPN. Opcja jest domyślnie wyłączona, ponieważ usługi te zazwyczaj wymagają prawdziwego adresu IP urządzenia do prawidłowego działania.

- **Allow Remote Access the LAN Subnet**: jeśli włączony, zdalny dostęp do tego routera i jego urządzeń LAN przez VPN będzie dozwolony. Wymaga, aby serwer VPN rozgłaszał trasę powrotną do swojej podsieci LAN.

- **Maskowanie IP**: jeśli włączone, źródłowe adresy IP klientów LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w konfiguracjach site-to-site, gdzie zdalny węzeł zna Twoje podsieci LAN.

- **MTU**: wartość MTU ustawiona dla tunelu nadpisuje ustawienia MTU zawarte w pliku konfiguracyjnym.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
