# Jak skonfigurować Urban Shield VPN na routerze GL.iNet

[Urban Shield VPN](https://urbanshieldvpn.com/) to dostawca VPN, który oferuje użytkownikom na całym świecie rozwiązania VPN o wysokim poziomie bezpieczeństwa i wydajności. Udostępnia wstępnie skonfigurowane routery VPN GL.iNet oraz elastyczne plany subskrypcji, zapewniając bezpieczne i prywatne przeglądanie sieci. Wystarczy aktywować Urban Shield VPN na routerze, aby uzyskać ochronę i dostęp do globalnych serwerów, co pozwala spokojnie przeglądać Internet i korzystać ze streamingu.

## Przewodnik konfiguracji

Poniżej pokazano przykład aktywacji Urban Shield VPN na modelu GL-B3000 poprzez ustawienie go jako klienta WireGuard. 

### 1. Rejestracja w Urban Shield VPN

Wejdź na [oficjalną stronę Urban Shield VPN](https://urbanshieldvpn.com/){class="_blank"} lub kliknij [tutaj](https://payment.urbanshieldvpn.com/sign-up), aby utworzyć konto Urban Shield VPN.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Włącz router i połącz urządzenie

Włącz router. Podłącz urządzenie do routera za pomocą kabla Ethernet lub przez Wi-Fi.

### 3. Otwórz panel administracyjny WWW

Wykonaj poniższe kroki, aby uzyskać dostęp do panelu administracyjnego WWW. Jeśli jesteś już zalogowany, przejdź do [kolejnej części](#4-network-setup).

Otwórz przeglądarkę internetową (zalecane są Chrome, Edge lub Safari) i przejdź do [192.168.8.1](http://192.168.8.1){target="_blank"}. Zostaniesz przekierowany do wstępnej konfiguracji panelu administracyjnego WWW, jak pokazano poniżej. Ustaw hasło administratora i kliknij **Next**, aby kontynuować.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Skonfiguruj sieć Wi-Fi. Na stronie wyświetlane są fabryczne dane Wi-Fi, w tym nazwa sieci (SSID) i hasło, które możesz zmienić lub pozostawić bez zmian. Jeśli zmienisz dowolne ustawienie Wi-Fi, ponownie połącz urządzenie z zaktualizowaną siecią Wi-Fi.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Następnie kliknij **Next**, aby zalogować się przy użyciu hasła administratora.

### 4. Konfiguracja sieci {#4-network-setup}

W prawym górnym rogu znajduje się **Network Setup Wizard** (dostępny od firmware v4.7). Przed konfiguracją VPN skorzystaj z kreatora, aby skonfigurować router do dostępu do Internetu.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Aktywacja Urban Shield VPN

Wybierz z menu po lewej stronie **VPN** -> **WireGuard Client**. Zobaczysz wbudowaną stronę logowania Urban Shield VPN.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Wpisz **Email** i **Password**, a następnie kliknij **Save And Continue**. Zostaną wygenerowane pliki konfiguracyjne dla poszczególnych serwerów.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Wybierz preferowany serwer i kliknij **Apply**. 

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Dostępne serwery pojawią się następnie na liście.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Kliknij ikonę z trzema kropkami, aby rozpocząć połączenie.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Po nawiązaniu połączenia pojawi się niebieska kropka, wskazująca pomyślne połączenie.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Stan połączenia możesz także sprawdzić na stronie VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Edycja danych konta lub wylogowanie

Kliknij ikonę koła zębatego, aby edytować informacje o koncie lub się wylogować.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Go Renew

Jeśli klikniesz **Go Renew**, zostaniesz przeniesiony na oficjalną stronę, aby odnowić subskrypcję.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Delete 

Jednym kliknięciem możesz usunąć wszystkie pliki konfiguracyjne, a także klucz prywatny i klucz publiczny.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
