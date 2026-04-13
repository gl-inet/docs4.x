# Jak skonfigurować serwer WireGuard przez AstroRelay?

Ten poradnik przedstawia kroki konfiguracji serwera WireGuard przez AstroRelay na routerze GL.iNet, co jest idealne dla użytkowników, którzy potrzebują zdalnego dostępu do swoich lokalnych usług domowych lub biurowych, ale nie posiadają publicznego adresu IP od swojego dostawcy usług internetowych.

[AstroRelay](https://www.astrorelay.com){target="_blank"} zapewnia bezpieczny tunel odwrotnego proxy, przez który można bezpiecznie uzyskać dostęp do zasobów znajdujących się za NAT i zaporami sieciowymi.

1. Postępuj zgodnie z [tym przewodnikiem](../interface_guide/wireguard_server.md), aby skonfigurować serwer WireGuard na routerze GL.iNet, nawet jeśli nie masz publicznego adresu IP. 

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Następnie kliknij **Profiles**, aby wyeksportować konfigurację WireGuard. Oto przykładowy plik konfiguracyjny.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. (Opcjonalnie) Jeśli potrzebujesz zdalnego dostępu do sieci LAN serwera VPN, włącz **Allow Remote Access LAN**. W przeciwnym razie pomiń ten krok.

    ??? "Dla firmware v4.7 i wcześniejszych"

        W panelu administratora serwera przejdź do **VPN** -> **VPN Dashboard** -> sekcja **VPN Server**. Kliknij ikonę koła zębatego po prawej stronie serwera WireGuard.

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        Włącz **Remote Access LAN** i kliknij **Apply**.

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **Gdy włączone, ten router i urządzenia LAN mogą być dostępne zdalnie przez VPN.**

    ??? "Dla firmware v4.8 i nowszych"

        W panelu administratora serwera przejdź do **VPN** -> **WireGuard Server**. Kliknij **Options** w prawym górnym rogu.

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        Włącz **Allow Remote Access the LAN Subnet** i kliknij **Apply**.

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **Gdy włączone, ten router i urządzenia LAN mogą być dostępne zdalnie przez VPN.**

3. Załóż konto AstroRelay i postępuj zgodnie z tym [poradnikiem](https://www.astrorelay.com/tutorial.html){target="_blank"}, aby ukończyć początkową konfigurację.

    Podczas dodawania nowej domeny wybierz serwer najbliższy routerowi.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Podczas dodawania nowego linku wprowadź **adres IP LAN** routera w pole **Destination Host IP** i wprowadź **51820** w pole **Destination Port**.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Otrzymasz wtedy link, taki jak **wg_server_test.arlab1.cc:33331**. Kliknij go, aby skopiować link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4. Otwórz plik konfiguracyjny WireGuard, zamień wartość po **Endpoint** na link uzyskany w poprzednim kroku i zastosuj zmiany.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5. Zainstaluj [aplikację WireGuard](https://www.wireguard.com/install/){target="_blank"} na urządzeniu, którego chcesz użyć jako klient WireGuard. Następnie prześlij zmodyfikowany plik konfiguracyjny do aplikacji i uruchom połączenie. Alternatywnie prześlij go na inny router GL.iNet, aby skonfigurować go jako klienta WireGuard.

    Po połączeniu będziesz mógł zdalnie uzyskać dostęp do lokalnych usług domowych lub biurowych.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.