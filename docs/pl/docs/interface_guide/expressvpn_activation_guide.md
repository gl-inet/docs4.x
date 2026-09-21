# Przewodnik aktywacji ExpressVPN

**Uwaga:** Ten przewodnik dotyczy wyłącznie routera **Fortify (GL-MT6000)** pod wspólną marką GL.iNet x ExpressVPN.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} to jedna z wiodących na świecie usług VPN premium, zaprojektowana w celu ochrony Twojej prywatności w Internecie, zabezpieczenia połączenia internetowego i umożliwienia bezpiecznego przesyłania strumieniowego z dowolnego miejsca. Oferuje błyskawiczne prędkości, szyfrowanie na poziomie wojskowym i dostęp do serwerów w ponad 100 krajach. Niezależnie od tego, czy chcesz przesyłać strumieniowo, przeglądać prywatnie, czy chronić swoje dane w publicznej sieci Wi-Fi, ExpressVPN zapewnia szybkie i bezpieczne działanie.

**Fortify (GL-MT6000)** to router pod wspólną marką wydany wspólnie przez GL.iNet i ExpressVPN. Do każdej jednostki dołączona jest bezpłatna roczna subskrypcja ExpressVPN. Użytkownicy mogą wykupić subskrypcję i połączyć swoje konta bezpośrednio w internetowym panelu administracyjnym routera. Po aktywacji cały ruch przechodzący przez router będzie wykorzystywał szybką sieć ExpressVPN i solidne szyfrowanie, aby chronić całe połączenie sieciowe i prywatność w Internecie.

Ten przewodnik przeprowadzi Cię przez proces realizacji 12-miesięcznego planu ExpressVPN w internetowym panelu administracyjnym routera. Obejmuje również dostosowywanie zasad VPN w oparciu o scenariusze użytkowania i wymagania, pomagając Ci bez wysiłku cieszyć się szyfrowaną, bezpieczną i szybką łącznością internetową.

## Wykorzystaj plan ExpressVPN

Zaloguj się do internetowego panelu administracyjnego Fortify i przejdź do **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Przeczytaj i zaakceptuj **Terms of Service** i **Privacy Policy**, a następnie kliknij **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Kliknij **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

W wyskakującym oknie wprowadź swój **Order ID**. Jeśli kupiłeś ten router w sklepie GL.iNet, dodatkowo wymagany jest **Order Email**. Następnie kliknij **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

Zostaniesz przekierowany do kasy ExpressVPN. Po prawej stronie zastosowano kod realizacji, umożliwiający aktywację 12-miesięcznej subskrypcji bez dodatkowych opłat.

Wpisz na górze swój adres e-mail i dodaj metodę płatności, aby zapewnić nieprzerwany dostęp VPN na koniec początkowego okresu. Następnie kliknij **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Twój plan został aktywowany. Wróć do panelu administracyjnego routera Fortify, aby zalogować się na swoje konto.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Zaloguj się do ExpressVPN

W internetowym panelu administracyjnym Fortify przejdź do **VPN** -> **VPN Client Profile**.

Kliknij **Log in to ExpressVPN**, a zostaniesz przekierowany na stronę bezpiecznego logowania ExpressVPN.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Wpisz swój adres e-mail i kliknij **Send Code**. Na Twój adres e-mail zostanie wysłany 6-cyfrowy kod weryfikacyjny.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Wprowadź kod weryfikacyjny i kliknij **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Zmień hasło, aby aktywować konto.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

W następnym kroku kliknij **Yes**, aby autoryzować dostęp do ExpressVPN na swoim routerze.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Logowanie powiodło się. Możesz zamknąć to okno przeglądarki i wrócić do swojego urządzenia.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

W internetowym panelu administracyjnym Fortify przejdź do **VPN** -> **VPN Client Profile**.

Jesteś zalogowany w ExpressVPN na tym routerze. Kliknij **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Teraz możesz dodawać tunele VPN i konfigurować zasady VPN zgodnie ze swoimi potrzebami.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## Dodaj tunel VPN

### Ogólne kroki

Wykonaj poniższe czynności, aby dodać tunel VPN i skonfigurować zasady VPN. Jeśli to konieczne, zobacz [Odniesienie do sprawy](#case-reference).

1. W internetowym panelu administracyjnym Fortify przejdź do **VPN** -> **ExpressVPN Dashboard**. Kliknij **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Wybierz profil VPN, a następnie kliknij **Next**.

    Otrzymasz listę profili ExpressVPN. Wybierz jeden lub wiele profili i w razie potrzeby dostosuj ich priorytet po prawej stronie.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        W przypadku wybrania wielu profili tunel będzie próbował nawiązać połączenie przy użyciu każdego profilu w kolejności priorytetów, aż do pomyślnego nawiązania połączenia. Jeśli nie uda się połączyć wszystkich profili w pojedynczym tunelu, system określi, czy przełączyć się na sieć lokalną routera (WAN), w oparciu o stan wyłącznika awaryjnego w ustawieniach [Opcje tunelu](#tunnel-options) i [Cały inny ruch](#all-other-traffic).

3. Wybierz źródło klienta, a następnie kliknij **Next**.

    Istnieją cztery opcje:

    - **All Clients**: Jeśli ta opcja zostanie wybrana, ruch ze wszystkich urządzeń będzie zgodny z tą regułą.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: po wybraniu tej opcji ruch z określonych typów połączeń (np. podsieci LAN, Drop-in Gateway lub sieci gościnnej) będzie zgodny z tą regułą.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych na podstawie adresu MAC) będzie zgodny z tą regułą.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: po wybraniu tej opcji ruch z określonych urządzeń (identyfikowanych na podstawie adresu MAC) nie będzie zgodny z tą regułą.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Wybierz miejsce docelowe, a następnie kliknij **Apply**.

    Istnieją trzy opcje:

    - **All Targets**: Jeśli wybrano tę opcję, ruch zgodny z tą regułą będzie kierowany do wszystkich celów.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Jeśli ta opcja jest zaznaczona, ruch pasujący do tej reguły będzie kierowany do określonych domen lub adresów IP. Należy je wprowadzić ręcznie.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Jeśli zostanie zaznaczone, ruch pasujący do tej reguły nie będzie kierowany do określonych domen lub adresów IP. Należy je wprowadzić ręcznie.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. Tunel VPN został pomyślnie dodany. Zostaniesz przekierowany do **ExpressVPN Dashboard**. W razie potrzeby dodaj więcej tuneli VPN.

### Odniesienie do sprawy

Oto dwa typowe przypadki konfiguracji zasad VPN wraz z instrukcjami konfiguracji krok po kroku.

??? note "Przypadek 1: kierowanie przez VPN tylko ruchu określonych urządzeń."

    **Wymagania:**

    1. Tylko określone urządzenia podłączone do tego routera uzyskują dostęp do Internetu poprzez VPN. Wszystkie pozostałe urządzenia łączą się z Internetem poprzez lokalną sieć WAN.

    2. Wybrane urządzenia muszą korzystać wyłącznie z połączenia VPN. Jeśli VPN zostanie nieoczekiwanie rozłączony, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

    **Kroki konfiguracji:**

    1. Wybierz profil VPN.

        Wybierz jeden lub wiele profili i w razie potrzeby dostosuj ich priorytet po prawej stronie, a następnie kliknij **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Wybierz źródło klienta.

        Kliknij zakładkę **Specified Devices**, wybierz urządzenia, na których chcesz korzystać z VPN, a następnie kliknij **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Wybierz miejsce docelowe.

        Kliknij zakładkę **All Targets**, ustaw ją jako miejsce docelowe ruchu, a następnie kliknij **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

    4. Zostaniesz przekierowany do Panelu ExpressVPN. Teraz tunel VPN został pomyślnie dodany.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Upewnij się, że **Kill Switch** dla tego tunelu jest włączony. Jeśli VPN zostanie nieoczekiwanie rozłączony, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Upewnij się, że **Allow Non-VPN Traffic** jest włączony. Jest to domyślnie włączone, aby zapewnić, że ruch niepasujący do tunelu VPN będzie nadal mógł uzyskać dostęp do Internetu za pośrednictwem lokalnej sieci WAN.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Kliknij środkowy przycisk, aby aktywować ten tunel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Po nawiązaniu połączenia na stronie zostaną wyświetlone szczegóły połączenia VPN, w tym zasady VPN, wirtualny adres IP klienta, adres serwera, port nasłuchiwania i statystyki ruchu.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Teraz tylko dwa określone urządzenia uzyskują dostęp do Internetu przez VPN. Jeśli VPN zostanie nieoczekiwanie rozłączony, dostęp do Internetu dla tych urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP. Zamiast tego wszystkie pozostałe urządzenia będą miały dostęp do Internetu za pośrednictwem lokalnej sieci WAN.

??? note "Przypadek 2: kierowanie wszystkich urządzeń przez VPN 1 dla określonych witryn, a całego pozostałego ruchu przez VPN 2."

    **Wymagania:**

    1. Wszystkie urządzenia korzystają z tunelu VPN 1 podczas uzyskiwania dostępu do witryn określonych mediów społecznościowych i usług przesyłania strumieniowego, a tunelu VPN 2 w celu uzyskania pozostałego dostępu do Internetu.

    2. Jeśli tunele VPN nieoczekiwanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

    **Kroki konfiguracji:**

    1. Wybierz profil VPN dla Tunelu 1.

        Wybierz jeden lub wiele profili i w razie potrzeby dostosuj ich priorytet po prawej stronie, a następnie kliknij **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Wybierz źródło klienta.

        Kliknij zakładkę **All Clients**, ustaw ją jako źródło klienta dla Tunelu 1, a następnie kliknij **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Wybierz miejsce docelowe.

        Kliknij zakładkę **Specified Domain / IP List**, wprowadź domeny konkretnych mediów społecznościowych i serwisów streamingowych, jak pokazano poniżej, a następnie kliknij **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. Zostaniesz przekierowany do Panelu ExpressVPN. Teraz tunel VPN 1 został pomyślnie dodany.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Upewnij się, że **Kill Switch** dla tunelu 1 jest włączony. Jeśli VPN zostanie nieoczekiwanie rozłączony, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Kliknij **Add New Tunnel**, aby dodać Tunel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Wybierz profil VPN dla Tunelu 2.

        Wybierz jeden lub wiele profili i w razie potrzeby dostosuj ich priorytet po prawej stronie, a następnie kliknij **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

    8. Wybierz źródło klienta.

        Kliknij zakładkę **All Clients**, ustaw ją jako źródło klienta dla Tunelu 2, a następnie kliknij **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    9. Wybierz miejsce docelowe.

        Kliknij zakładkę **All Targets**, ustaw ją jako miejsce docelowe ruchu dla Tunelu 2, a następnie kliknij **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. Zostaniesz przekierowany do Panelu VPN. Teraz tunel VPN 2 został pomyślnie dodany.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Upewnij się, że **Kill Switch** dla Tunelu 2 jest włączony. Jeśli VPN zostanie nieoczekiwanie rozłączony, dostęp do Internetu dla ruchu pasującego do tego tunelu zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Kliknij ikonę koła zębatego w prawym górnym rogu, włącz **Enhanced Kill Switch**, a następnie kliknij **Apply**. Dzięki temu cały ruch będzie docierał do Internetu wyłącznie za pośrednictwem sieci VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        Po zastosowaniu, **Enhanced Kill Switch** pojawi się na górze strony.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Kliknij środkowy przycisk, aby aktywować Tunel 1 i Tunel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Po nawiązaniu połączenia na stronie zostaną wyświetlone szczegóły połączenia VPN, w tym zasady VPN, wirtualny adres IP klienta, adres serwera, port nasłuchiwania i statystyki ruchu.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Teraz wszystkie urządzenia będą używać **VPN Tunnel 1** podczas uzyskiwania dostępu do określonych domen i używać **VPN Tunnel 2** do całego pozostałego dostępu do Internetu. Jeśli tunele VPN nieoczekiwanie się rozłączą, dostęp do Internetu dla wszystkich urządzeń zostanie zablokowany, aby zapobiec wyciekom DNS i śledzeniu adresów IP.

## Kill Switch

Kill Switch to funkcja zabezpieczająca połączenia VPN. Automatycznie odcina cały dostęp do Internetu w Twojej sieci lokalnej, jeśli połączenie VPN nieoczekiwanie zostanie zerwane, zapobiegając ujawnieniu Twojego prawdziwego adresu IP i danych online oraz zapewniając ciągłą prywatność i bezpieczeństwo. Funkcja ta jest szczególnie przydatna w celu zapewnienia bezpiecznego, anonimowego dostępu do Internetu, na przykład podczas korzystania z sieci publicznych, przetwarzania danych wrażliwych lub ukrywania prawdziwego adresu IP.

Po włączeniu blokuje wszelki ruch kliencki próbujący ominąć tunel VPN, skutecznie powstrzymując wycieki VPN spowodowane problemami z konfiguracją DNS, nieoczekiwanymi rozłączeniami, bezpośrednimi żądaniami IP i innymi podobnymi scenariuszami.

Fortify obsługuje konfigurację Kill Switch dla globalnego połączenia VPN, a także dla każdego indywidualnego tunelu VPN.

- Aby skonfigurować Kill Switch dla globalnego połączenia VPN (czyli Enhanced Kill Switch), zapoznaj się z sekcją [Cały pozostały ruch](#all-other-traffic).

- Aby skonfigurować Kill Switch dla każdego tunelu VPN, zapoznaj się z [Opcjami tunelu](#tunnel-options).

## Cały inny ruch

Kliknij ikonę koła zębatego w prawym górnym rogu, aby skonfigurować zasady dla ruchu, który nie pasuje do tunelu VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Ta zasada kontroluje, czy ruch niepasujący do żadnej z grup tuneli VPN może uzyskać dostęp do Internetu, czy nie. Dostępne dwie opcje: **Allow Non-VPN Traffic** i **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Domyślnie włączone, aby zapewnić normalny dostęp do Internetu dla ruchu innego niż VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Wymusza dostęp wszystkich urządzeń do Internetu przez VPN. Każdy ruch, który nie pasuje do tunelu VPN, zostanie zablokowany. To ustawienie globalne nie zastępuje wyłącznika awaryjnego skonfigurowanego dla poszczególnych tuneli VPN.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Opcje tunelu

Możesz skonfigurować zaawansowane ustawienia dla każdego tunelu VPN, takie jak VPN Kill Switch, maskowanie IP i MTU.

Kliknij ikonę koła zębatego w grupie tuneli i wybierz **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: Jeśli ta opcja jest włączona, ruch pasujący do tego tunelu VPN zostanie zablokowany, jeśli połączenie VPN nieoczekiwanie ulegnie awarii. Jeśli ta opcja jest wyłączona, taki ruch będzie przekierowywany awaryjnie do tunelu **All Other Traffic**.

- **Services from GL.iNet Use VPN**: Jeśli ta opcja jest włączona, usługi GoodCloud, DDNS i rtty będą przesyłać pakiety przez tunele VPN. Ta opcja jest domyślnie wyłączona, ponieważ te usługi zwykle wymagają prawdziwego adresu IP urządzenia, aby działać prawidłowo.

- **Allow Remote Access to the LAN Subnet**: Jeśli ta opcja jest włączona, dozwolony będzie zdalny dostęp do tego routera i jego urządzeń LAN poprzez VPN. Wymaga, aby serwer VPN ogłosił trasę z powrotem do swojej podsieci LAN.

- **IP Masquerading**: Jeśli ta opcja jest włączona, źródłowe adresy IP klientów sieci LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w przypadku konfiguracji typu lokacja-lokacja, w których zdalny element równorzędny zna podsieci LAN.

- **MTU**: Wartość MTU ustawiona dla tunelu zastąpi ustawienia MTU w pliku konfiguracyjnym.

## Priorytet tunelu

Aby dostosować priorytet tunelu, kliknij ikonę koła zębatego w grupie tuneli i wybierz **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Kliknij i przytrzymaj ikonę z trzema liniami po prawej stronie, aby zmienić kolejność tuneli, a następnie kliknij **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

**Gdy włączonych jest kilka tuneli, router kieruje ruch zgodnie z następującymi regułami**:

1. Ruch będzie najpierw próbował dopasować regułę tunelu o najwyższym priorytecie. Jeśli zostanie dopasowany, zostanie poprowadzony przez ten tunel; w przeciwnym razie spróbuje skorzystać z tunelu o następnym priorytecie i tak dalej.

2. Każda grupa tuneli działa niezależnie. Gdy ruch będzie zgodny z regułą tunelu, będzie kierowany przez ten tunel i nie będzie przełączany w trybie awaryjnym między grupami tuneli.

3. W każdej grupie tuneli można wybrać wiele profili, aby umożliwić przełączanie awaryjne wewnątrz tunelu. Kiedy profil o najwyższym priorytecie w grupie tuneli ulegnie awarii, tunel automatycznie połączy się przy użyciu profilu o drugim najwyższym priorytecie i tak dalej.

4. Jeśli tunel VPN zostanie nieoczekiwanie rozłączony, system określi, czy przełączyć awaryjnie ruch do tunelu All Other Traffic w oparciu o to, czy w tym tunelu jest włączony **Kill Switch**.

    - Jeśli funkcja Kill Switch jest włączona, ruch zostanie zablokowany i nie zostanie przeniesiony do tunelu All Other Traffic.
    - Jeśli wyłącznik awaryjny jest wyłączony, ruch zostanie przeniesiony awaryjnie do tunelu All Other Traffic.

5. W tunelu **All Other Traffic** różne tryby określają, czy ruch niepasujący do tunelu VPN może uzyskać dostęp do Internetu.

    - **Allow Non-VPN Traffic**: Jest domyślnie włączona, aby zapewnić, że ruch niepasujący do tuneli VPN będzie nadal mógł uzyskać dostęp do Internetu za pośrednictwem lokalnej sieci WAN.

    - **Enhanced Kill Switch**: Wymusza dostęp wszystkich urządzeń do Internetu przez VPN. Każdy ruch, który nie pasuje do tunelu VPN, zostanie zablokowany. To ustawienie globalne nie zastępuje wyłącznika awaryjnego skonfigurowanego dla poszczególnych tuneli VPN. Krótko mówiąc, wzmacnia wyłącznik awaryjny i blokuje regularny dostęp do Internetu, aby zapobiec wyciekom adresów IP.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
