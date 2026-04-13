# Konfiguracja klienta WireGuard na routerach GL.iNet

**Uwaga**: Ten przewodnik dotyczy oprogramowania v4.7 i nowszego. W przypadku wcześniejszych wersji zapoznaj się z dokumentacją [tutaj](wireguard_client_v4.6.md).

---

WireGuard® to niezwykle prosty, szybki i nowoczesny protokół VPN wykorzystujący najnowocześniejszą kryptografię. Jest szybszy, prostszy i bardziej przydatny niż IPsec, a przy tym znacznie wydajniejszy niż OpenVPN.

Aby skonfigurować klienta WireGuard na routerze GL.iNet, obejrzyj poniższy film lub postępuj zgodnie z opisanymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Przed rozpoczęciem upewnij się, że masz aktywną subskrypcję u dostawcy usług VPN obsługującego ręczną konfigurację WireGuard. Kliknij [tutaj](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, aby sprawdzić dostawców WireGuard kompatybilnych z routerami GL.iNet.

Zazwyczaj musisz najpierw odwiedzić oficjalną stronę subskrybowanego dostawcy VPN, pobrać plik konfiguracyjny i przesłać go do routera, aby skonfigurować go jako klienta WireGuard. Jeśli nie wiesz, jak pobrać plik konfiguracyjny, zapoznaj się z [tym przewodnikiem](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) lub skontaktuj się z pomocą techniczną dostawcy.

Klienta WireGuard możesz skonfigurować za pomocą panelu administracyjnego lub [aplikacji mobilnej](../faq/mobile_app.md).

- **Aplikacja mobilna** jest zintegrowana z niektórymi dostawcami usług WireGuard, takimi jak AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN itp., co oznacza, że możesz łatwo przeprowadzić konfigurację, podając jedynie dane logowania subskrybowanej usługi WireGuard. Otwórz aplikację i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

- **Panel administracyjny** nie tylko obsługuje wybrane usługi WireGuard, ale także udostępnia możliwość ręcznej konfiguracji. Możesz wprowadzić dane logowania subskrybowanej usługi WireGuard, aby szybko zakończyć konfigurację, lub ręcznie przesłać plik konfiguracyjny.

Poniżej opisano kroki konfiguracji za pomocą panelu administracyjnego. Wybierz odpowiedniego dostawcę usług WireGuard, aby szybko przejść do instrukcji krok po kroku.

* [Konfiguracja AzireVPN](#set-up-azirevpn)
* [Konfiguracja Hide.me](#set-up-hideme)
* [Konfiguracja IPVanish](#set-up-ipvanish)
* [Konfiguracja Mullvad](#set-up-mullvad)
* [Konfiguracja NordVPN](#set-up-nordvpn)
* [Konfiguracja PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Konfiguracja PureVPN](#set-up-purevpn)
* [Konfiguracja Surfshark](#set-up-surfshark)
* [Ręczna konfiguracja klienta WireGuard (dla innych dostawców)](#set-up-wireguard-client-manually-for-other-providers)

## Konfiguracja AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} to usługa VPN nastawiona na prywatność, oferująca bezpieczne, nowoczesne i wydajne tunele, takie jak WireGuard.

Obejrzyj ten film, aby skonfigurować AzireVPN na routerach GL.iNet za pomocą panelu administracyjnego lub aplikacji mobilnej.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Możesz też wykonać poniższe kroki, aby skonfigurować AzireVPN za pomocą panelu administracyjnego.

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}
    
    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![azirevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn4.png){class="glboxshadow"}

3. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Odnawianie subskrypcji.

    Kliknięcie **Go Renew** spowoduje przekierowanie na oficjalną stronę w celu odnowienia subskrypcji.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Konfiguracja Hide.me {#set-up-hideme}

[Oficjalna strona](https://www.hideipvpn.com/){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![hideme connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme4.png){class="glboxshadow"}

3. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Konfiguracja IPVanish {#set-up-ipvanish}

[Oficjalna strona](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![ipvanish connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish5.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Konfiguracja Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} to usługa VPN, która chroni Twoją aktywność online, tożsamość i lokalizację.

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Wprowadź **Account**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}
    
    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![mullvad connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad5.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Odnawianie subskrypcji.

    Kliknięcie **Go Renew** spowoduje przekierowanie na oficjalną stronę w celu odnowienia subskrypcji.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Konfiguracja NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} to internetowa usługa VPN łącząca szybkość i bezpieczeństwo.

1. Kliknij [tutaj](https://my.nordaccount.com/){target="_blank"}, aby zalogować się na swoje konto NordVPN.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}
    
    Po zalogowaniu się do panelu Nord kliknij NordVPN po lewej stronie, a następnie kliknij **Set up NordVPN manually**.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_dashboard.png){class="glboxshadow"}

    Znajdziesz tam **Access token**.

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/manual_setup.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/generate_new_token.png){class="glboxshadow"}

    ![nordvpn get credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/copy_access_token.png){class="glboxshadow"}

2. Zaloguj się do panelu administracyjnego routera i przejdź do **VPN** -> **WireGuard Client** -> **NordVPN**.

    Wprowadź **Token**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![nordvpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn5.png){class="glboxshadow"}

5. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Konfiguracja PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Oficjalna strona](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **PIA**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![pia connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia5.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Konfiguracja PureVPN {#set-up-purevpn}

[Oficjalna strona](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **PureVPN**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Zostaną wygenerowane wszystkie dostępne pliki konfiguracyjne.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

2. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![purevpn connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn5.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Konfiguracja Surfshark {#set-up-surfshark}

[Oficjalna strona](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![surfshark connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark5.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Odśwież.

    Możesz kliknąć **Refresh**, aby zaktualizować klucz publiczny, gdy nie można połączyć się z serwerem VPN.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Konfiguracja Windscribe {#set-up-windscribe}

[Oficjalna strona](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**. Zostaną wygenerowane pliki konfiguracyjne dla każdego serwera.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Wybierz serwery.

    Wybierz serwery, z którymi chcesz się połączyć, i kliknij **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Zostanie wyświetlona lista plików konfiguracyjnych odpowiadających wybranym serwerom.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Uruchom połączenie.

    Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Szczegóły połączenia VPN będą wyświetlane na **VPN Dashboard**.

    ![windscribe connection status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe6.png){class="glboxshadow"}

4. Aktualizacja serwerów.

    Możesz kliknąć **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów, unikając błędów połączenia spowodowanych konserwacją lub wyłączeniem serwerów.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Edycja danych logowania lub wylogowanie.

    Kliknij ikonę koła zębatego, aby edytować dane logowania lub się wylogować.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Odśwież.

    Możesz kliknąć **Refresh**, aby zaktualizować klucz publiczny, gdy nie można połączyć się z serwerem VPN.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Usuń wszystko.

    Możesz kliknąć **Delete All**, aby usunąć wszystkie pliki konfiguracyjne jednym kliknięciem, i wybrać, czy jednocześnie usunąć klucz prywatny i klucz publiczny.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Ręczna konfiguracja klienta WireGuard (dla innych dostawców) {#set-up-wireguard-client-manually-for-other-providers}

Jeśli korzystasz z innego dostawcy usług WireGuard, możesz pobrać pliki konfiguracyjne WireGuard i wykonać poniższe kroki, aby skonfigurować klienta WireGuard. Jeśli nie wiesz, jak pobrać pliki konfiguracyjne, zapoznaj się z [tym przewodnikiem](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) lub skontaktuj się z pomocą techniczną dostawcy.

W panelu administracyjnym przejdź do **VPN** -> **WireGuard Client**.

1. Kliknij **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Na lewym pasku bocznym zostanie utworzona grupa.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Nadaj grupie opisową nazwę (np. azirevpn). Następnie prześlij plik konfiguracyjny (obsługiwane formaty: zip, tar, gz, conf, txt) lub ręcznie wprowadź szczegóły konfiguracji (w formie tekstowej).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Prześlij plik konfiguracyjny**.

        Kliknij obszar przesyłania, aby przesłać plik konfiguracyjny WireGuard, a następnie kliknij **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Ręczne dodanie konfiguracji**.
    
        Kliknij **Manually Add Configuration** u dołu obszaru przesyłania.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Podaj opisową nazwę i wklej konfigurację w pole tekstowe. Następnie kliknij **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Jeśli chcesz zweryfikować poszczególne elementy, możesz przełączyć się do trybu Item i sprawdzić szczegóły konfiguracji. Następnie kliknij **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Kliknij ikonę trzech kropek po prawej stronie, aby uruchomić połączenie.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

5. Po nawiązaniu połączenia możesz sprawdzić jego stan na stronie **VPN Dashboard**.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

## Konfiguracja serwera WireGuard na routerze GL.iNet

Nie chcesz subskrybować zewnętrznych usług VPN? Możesz zakupić dwa routery GL.iNet – jeden skonfigurować jako serwer WireGuard, a drugi jako klienta WireGuard.

Jest to szczególnie przydatne w scenariuszach, w których dostawca internetu przydziela Twojej sieci domowej publiczny adres IP i chcesz łączyć się z siecią domową przez VPN podczas pobytu poza domem, aby zapewnić bezpieczeństwo i dostęp do zasobów sieci wewnętrznej. Eliminuje to koszty i niedogodności związane z ciągłą subskrypcją komercyjnych usług VPN.

Aby skonfigurować serwer WireGuard, zapoznaj się z dokumentacją [tutaj](wireguard_server.md).

---

WireGuard® jest zarejestrowanym znakiem towarowym Jason A. Donenfeld.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
