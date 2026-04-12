# VPN Dashboard (Oprogramowanie v4.9)

**Uwaga**: Ten przewodnik dotyczy oprogramowania v4.9. W przypadku wcześniejszych wersji zapoznaj się z dokumentacją [tutaj](vpn_dashboard.md).

---

W webowym panelu administracyjnym przejdź do **VPN** -> **VPN Dashboard**.

VPN Dashboard wyświetla szczegóły połączenia VPN, takie jak reguły routingu, połączony serwer, statystyki ruchu, wirtualny adres IP klienta i dziennik połączeń. Umożliwia także konfigurację zaawansowanych ustawień, takich jak Kill Switch, maskowanie IP i MTU.

W porównaniu z oprogramowaniem v4.8 wersja v4.9 wprowadza następujące ulepszenia w VPN Dashboard:

1. **Umożliwia wybór wielu profili w grupie tunelu i ustawienie ich priorytetu**. Tunel będzie próbował łączyć się z użyciem kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane.

2. **Każda grupa tuneli działa niezależnie i nie wykonuje przełączenia awaryjnego między grupami**. Jeśli wszystkie profile w pojedynczym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu Kill Switch dla tunelu i tunelu **Cały pozostały ruch**.

## Pierwsze kroki {#getting-started}

Przy pierwszym wejściu na tę stronę, jeśli nie utworzono jeszcze żadnych tuneli, strona będzie wyglądać jak poniżej. Kliknij **Add VPN Tunnel**, aby rozpocząć.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Wybierz dostawcę VPN**. Dostawcy VPN wyświetlani na liście są zintegrowani z panelem administracyjnym routera GL.iNet. Jeśli masz aktywną subskrypcję, wystarczy wprowadzić dane logowania, aby od razu się zalogować i pobrać pliki konfiguracyjne do połączeń VPN.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

Jeśli korzystasz z innego dostawcy VPN lub chcesz przesłać własne konfiguracje VPN, przejdź do **VPN Client Profile**, aby skonfigurować je ręcznie.

Poniżej pokazano przykład z **Hide.me**. Zaloguj się przy użyciu danych logowania Hide.me.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Wybierz serwer VPN**. Jest to serwer, z którym połączy się ten tunel VPN, a Twój publiczny adres IP będzie widoczny tak, jakby pochodził z lokalizacji wybranego serwera. Kliknij **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

Połączenie zostanie nawiązane automatycznie. Kliknij **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

Zostaniesz przeniesiony do VPN Dashboard, gdzie **VPN Tunnel 1** będzie włączony i połączony.

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**W tym przykładzie wszyscy klienci podłączeni do tego routera uzyskują dostęp do Internetu przez ten tunel VPN.**

Jeśli chcesz skonfigurować politykę VPN, zapoznaj się z sekcją [Polityka VPN](#vpn-policy).

Tunel **Cały pozostały ruch** jest domyślnie włączony i wyświetlany na dole strony VPN Dashboard. Szczegóły znajdziesz [tutaj](#all-other-traffic).

## Szczegóły tunelu {#tunnel-details}

Na stronie VPN Dashboard każdy pojedynczy tunel VPN jest wyświetlany jak poniżej. Pokazuje on szczegółowe informacje o tunelu VPN, takie jak reguły routingu, połączony serwer, statystyki ruchu, adres serwera, port nasłuchu, wirtualny adres IP klienta i dziennik połączeń. W górnej części grupy tunelu możesz włączyć lub wyłączyć tunel VPN oraz skonfigurować ustawienia tunelu.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## Polityka VPN {#vpn-policy}

Polityka VPN określa, w jaki sposób ruch sieciowy jest kierowany przez tunele VPN, czyli które połączenia trafiają do docelowych miejsc przez VPN, a które uzyskują bezpośredni dostęp do Internetu przez lokalny WAN.

Pozwala to wszystkim klientom lub wybranym urządzeniom uzyskiwać dostęp do wskazanych stron internetowych albo do całego Internetu przez połączenie VPN, zapewniając elastyczne i bezpieczne zarządzanie siecią.

### Szybka konfiguracja

Na stronie VPN Dashboard kliknij **Add New Tunnel** albo środkowy obszar istniejącego tunelu VPN.

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Następnie postępuj zgodnie z kreatorem konfiguracji, aby ustawić politykę VPN, w tym wybrać profil VPN, źródło ruchu i cel ruchu.

1. **Wybierz profil VPN.**

    Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

    Weźmy jako przykład [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"}. Zaloguj się przy użyciu danych usługi, a zobaczysz listę profili VPN. Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Uwaga**: Gdy wybrano wiele profili, tunel będzie próbował łączyć się z użyciem kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane. Jeśli wszystkie profile w jednym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu Kill Switch dla tunelu oraz tunelu [Cały pozostały ruch](#all-other-traffic).

2. **Wybierz źródło ruchu klienta.**

    Dostępne są cztery opcje:

    - **All Clients**: po wybraniu tej opcji ruch ze wszystkich urządzeń będzie pasować do tej reguły.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: po wybraniu tej opcji ruch z określonych typów połączeń (np. podsieć LAN, Drop-in Gateway, Guest Network) będzie pasować do tej reguły.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych po adresie MAC) będzie pasować do tej reguły.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych po adresie MAC) nie będzie pasować do tej reguły.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Wybierz cel ruchu.**

    Dostępne są trzy opcje:

    - **All Targets**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do wszystkich celów.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły będzie kierowany do określonych domen lub adresów IP. Trzeba je wprowadzić ręcznie.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: po wybraniu tej opcji ruch pasujący do tej reguły nie będzie kierowany do określonych domen ani adresów IP. Trzeba je wprowadzić ręcznie.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Przykładowe scenariusze

Poniżej znajdują się dwa scenariusze z instrukcjami krok po kroku.

**Scenariusz 1**

**Cele**:

1. Tylko wybrane urządzenia podłączone do tego routera mają uzyskiwać dostęp do Internetu przez VPN. Wszystkie pozostałe urządzenia mają korzystać z lokalnego WAN.

2. Wybrane urządzenia mają korzystać wyłącznie z połączenia VPN. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

**Wykonaj poniższe kroki, aby skonfigurować politykę VPN.**

1. Wybierz profil VPN.

    Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

    Weźmy jako przykład [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"}. Zaloguj się przy użyciu danych usługi, a zobaczysz listę profili VPN.

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

    **Uwaga**: Gdy wybrano wiele profili, tunel będzie próbował łączyć się z użyciem kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane. Jeśli wszystkie profile w jednym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu Kill Switch dla tunelu oraz tunelu [Cały pozostały ruch](#all-other-traffic).

2. Wybierz **Specified Devices** jako źródło ruchu klienta, następnie zaznacz urządzenia, które mają korzystać z VPN, i kliknij **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Wybierz **All Targets** jako cel ruchu, a następnie kliknij **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Zostaniesz przeniesiony do VPN Dashboard, gdzie zostanie dodany tunel VPN.

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Upewnij się, że dla tego tunelu włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}
    
6. Upewnij się, że **Cały pozostały ruch** jest włączony, a tryb ustawiono na **Allow Non-VPN Traffic**. Dzięki temu ruch, który nie pasuje do powyższych tuneli VPN, nadal może uzyskiwać dostęp do Internetu przez lokalny WAN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Przełącz przełącznik, aby aktywować ten tunel.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Po nawiązaniu połączenia strona wyświetli szczegóły połączenia VPN, w tym politykę VPN, statystyki ruchu, adres serwera, port nasłuchu i wirtualny adres IP.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    Od tej chwili tylko dwa wskazane urządzenia uzyskują dostęp do Internetu przez VPN. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP. Wszystkie pozostałe urządzenia będą korzystać z lokalnego WAN.

**Scenariusz 2**

**Cele:**

1. Wszystkie urządzenia mają korzystać z **VPN Tunnel 1** podczas uzyskiwania dostępu do domen określonych serwisów społecznościowych i usług streamingowych, a z **VPN Tunnel 2** przy całej pozostałej aktywności internetowej.

2. Jeśli tunele VPN niespodziewanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

**Wykonaj poniższe kroki, aby skonfigurować politykę VPN.**

1. Wybierz profil VPN dla Tunnel 1.

    Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

    Weźmy jako przykład [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"}. Zaloguj się przy użyciu danych usługi, a zobaczysz listę profili VPN.

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}
    
    Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

    **Uwaga**: Gdy wybrano wiele profili, tunel będzie próbował łączyć się z użyciem kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane. Jeśli wszystkie profile w jednym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu Kill Switch dla tunelu oraz tunelu [Cały pozostały ruch](#all-other-traffic).

2. Wybierz **All Clients** jako źródło ruchu klienta dla Tunnel 1, a następnie kliknij **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Wybierz **Specified Domain / IP List** jako cel ruchu dla Tunnel 1. Wprowadź domeny kilku popularnych serwisów społecznościowych i usług streamingowych, jak pokazano poniżej, a następnie kliknij **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. Zostaniesz przeniesiony do VPN Dashboard, gdzie Tunnel 1 zostanie dodany.

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Upewnij się, że dla Tunnel 1 włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}
    
6. Kliknij **Add New Tunnel**, aby dodać Tunnel 2.

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Wybierz profil VPN dla Tunnel 2.

    Jeśli zalogowano się przy użyciu danych dowolnej zintegrowanej usługi VPN lub przesłano plik konfiguracyjny, dostępne profile zostaną wyświetlone tutaj. W przeciwnym razie przejdź do **VPN Client Profile**, aby zalogować się przy użyciu danych logowania lub ręcznie przesłać plik konfiguracyjny.

    Weźmy jako przykład [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Zaloguj się przy użyciu danych usługi, a zobaczysz listę profili VPN.
    
    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}
    
    Wybierz jeden albo kilka profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

    **Uwaga**: Gdy wybrano wiele profili, tunel będzie próbował łączyć się z użyciem kolejnych profili zgodnie z kolejnością priorytetów, aż połączenie zostanie nawiązane. Jeśli wszystkie profile w jednym tunelu nie połączą się, system zdecyduje, czy przełączyć ruch na lokalny WAN, na podstawie stanu Kill Switch dla tunelu oraz tunelu [Cały pozostały ruch](#all-other-traffic).

8. Wybierz **All Clients** jako źródło ruchu klienta dla Tunnel 2, a następnie kliknij **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Wybierz **All Targets** jako cel ruchu dla Tunnel 2, a następnie kliknij **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. Zostaniesz przeniesiony do VPN Dashboard, gdzie Tunnel 2 zostanie dodany.

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Upewnij się, że dla Tunnel 2 włączono **Kill Switch**. Jeśli VPN niespodziewanie się rozłączy, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Wyłącz **Cały pozostały ruch**. Upewnij się, że tryb jest ustawiony na **Enhanced Kill Switch**. Dzięki temu cały ruch będzie musiał uzyskiwać dostęp do Internetu przez VPN.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Przełącz przełącznik, aby aktywować Tunnel 1 i Tunnel 2.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Po nawiązaniu połączenia strona wyświetli szczegóły połączenia VPN, w tym politykę VPN, statystyki ruchu, adres serwera, port nasłuchu i wirtualny adres IP.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Teraz wszystkie urządzenia będą korzystać z **VPN Tunnel 1** podczas uzyskiwania dostępu do określonych domen oraz z **VPN Tunnel 2** przy całej pozostałej aktywności internetowej. Jeśli tunele VPN niespodziewanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresu IP.

## Cały pozostały ruch {#all-other-traffic}

Ta opcja określa, czy ruch, który nie pasuje do żadnej z powyższych grup tuneli VPN, może uzyskiwać dostęp do Internetu. Domyślnie jest włączona, aby zapewnić normalny dostęp do Internetu ruchowi, który nie jest kierowany przez VPN.

Gdy opcja jest włączona, niedopasowany ruch nadal może uzyskiwać dostęp do Internetu.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

Gdy opcja jest wyłączona, dostęp do Internetu jest dozwolony tylko dla ruchu kierowanego przez VPN. Cały ruch spoza VPN oraz ruch po przełączeniu awaryjnym z połączeń VPN zostaną zablokowane. Ta opcja nie zastępuje indywidualnego ustawienia **Kill Switch** dla każdego tunelu VPN.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Priorytet tunelu {#tunnel-priority}

Aby zmienić priorytet tunelu, kliknij ikonę koła zębatego w grupie tunelu i wybierz **Sort**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Kliknij i przytrzymaj ikonę trzech linii po prawej stronie, aby zmienić kolejność tuneli, a następnie kliknij **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Gdy włączonych jest wiele tuneli, router kieruje ruch zgodnie z następującymi regułami**:

1. Ruch najpierw spróbuje dopasować się do reguły tunelu o najwyższym priorytecie. Jeśli dopasowanie powiedzie się, ruch zostanie skierowany przez ten tunel; w przeciwnym razie zostanie sprawdzony tunel o następnym priorytecie i tak dalej.

2. Każda grupa tuneli działa niezależnie. Gdy ruch dopasuje się do reguły tunelu, zostanie skierowany przez ten tunel i nie nastąpi przełączenie awaryjne między grupami tuneli.

3. W każdej grupie tuneli można wybrać wiele profili, aby umożliwić przełączenie awaryjne wewnątrz tunelu. Gdy profil o najwyższym priorytecie w grupie tunelu przestanie działać, tunel automatycznie połączy się przy użyciu profilu o kolejnym priorytecie i tak dalej.

4. Jeśli tunel VPN niespodziewanie się rozłączy, system zdecyduje, czy przełączyć ruch do tunelu **Cały pozostały ruch**, na podstawie tego, czy dla tego tunelu włączono **Kill Switch**.

    - Jeśli **Kill Switch** jest włączony, ruch zostanie zablokowany i nie zostanie przełączony do tunelu **Cały pozostały ruch**.
    - Jeśli **Kill Switch** jest wyłączony, ruch zostanie przełączony do tunelu **Cały pozostały ruch**.

5. Tunel **Cały pozostały ruch** jest domyślnie włączony, aby zapewnić dostęp do Internetu także ruchowi, który nie pasuje do tuneli VPN.

    - Gdy jest włączony, kieruje niedopasowany ruch lub ruch po przełączeniu awaryjnym przez lokalny WAN.
    - Gdy jest wyłączony, wzmacnia działanie Kill Switch i blokuje zwykły dostęp do Internetu, aby zapobiec wyciekom IP.

## Opcje tunelu {#tunnel-options}

Możesz skonfigurować zaawansowane ustawienia każdego tunelu VPN, takie jak Kill Switch, maskowanie IP i MTU.

Kliknij ikonę koła zębatego w grupie tunelu i wybierz **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: jeśli opcja jest włączona, ruch pasujący do tego tunelu VPN zostanie zablokowany, jeśli połączenie VPN niespodziewanie się zerwie. Jeśli opcja jest wyłączona, taki ruch zostanie przełączony do tunelu **Cały pozostały ruch**.

- **Services from GL.iNet Use VPN**: jeśli opcja jest włączona, usługi GoodCloud, DDNS i rtty będą przesyłać pakiety przez tunele VPN. Domyślnie ta opcja jest wyłączona, ponieważ usługi te zwykle wymagają prawdziwego adresu IP urządzenia, aby działać poprawnie.

- **Allow Remote Access to the LAN Subnet**: jeśli opcja jest włączona, zdalny dostęp do tego routera i jego urządzeń LAN przez VPN będzie dozwolony. Wymaga to, aby serwer VPN rozgłaszał trasę powrotną do swojej podsieci LAN.

- **IP Masquerading**: jeśli opcja jest włączona, źródłowe adresy IP klientów LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w konfiguracjach site-to-site, w których zdalny węzeł zna Twoje podsieci LAN.

- **MTU**: wartość MTU ustawiona dla tunelu zastąpi ustawienia MTU w pliku konfiguracyjnym.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

