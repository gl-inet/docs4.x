# Jak połączyć się z NordVPN z dedykowanym IP na routerach GL.iNet?

Ten artykuł przedstawia kroki konfiguracji połączenia NordVPN z dedykowanym IP na routerach GL.iNet.

Używamy GL-AXT1800 jako przykładu.

1. Zaloguj się do swojego konta Nord i sprawdź szczegóły dedykowanego IP. Jak pokazano poniżej, przypisany adres IP to **193.32.211.142**, a serwer to **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Przejdź do [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) i znajdź plik konfiguracyjny dla **United Kingdom #1625**. Pobierz plik konfiguracyjny UDP lub TCP.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Wróć do strony swojego konta Nord, przejdź do **Manual Setup** i kliknij **Set up NordVPN Manually**, aby uzyskać dane logowania do usługi.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Zaloguj się do panelu administracyjnego routera i przejdź do **VPN** > **OpenVPN Client**. Utwórz nową grupę, aby przesłać plik konfiguracyjny pobrany w kroku 2. Następnie wprowadź dane logowania do usługi, które uzyskałeś w kroku 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    Wykryto 1 prawidłowy plik konfiguracyjny. Wprowadź nazwę użytkownika i hasło. Jeśli te konfiguracje używają różnych haseł, musisz wprowadzić odpowiednie hasło dla każdego pliku konfiguracyjnego.

5. Kliknij ikonę trzech kropek po prawej stronie, aby się połączyć. Możesz również przejść do **VPN Dashboard**, wybrać plik konfiguracyjny i kliknąć **Apply**, aby nawiązać połączenie.

6. Po połączeniu sprawdź swój publiczny adres IP [tutaj](https://whatismyipaddress.com/) i potwierdź, czy pasuje do Twojego dedykowanego IP od NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
