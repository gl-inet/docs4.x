# Jak skonfigurować serwer OpenVPN przez AstroRelay?

Ten poradnik przedstawia kroki konfiguracji serwera OpenVPN przez AstroRelay na routerze GL.iNet, co jest idealne dla użytkowników, którzy potrzebują zdalnego dostępu do swoich lokalnych usług domowych lub biurowych, ale nie posiadają publicznego adresu IP od swojego dostawcy usług internetowych.

[AstroRelay](https://www.astrorelay.com){target="_blank"} zapewnia bezpieczny tunel odwrotnego proxy, przez który można bezpiecznie uzyskać dostęp do zasobów znajdujących się za NAT i zaporami sieciowymi.

1. Postępuj zgodnie z [tym przewodnikiem](../interface_guide/openvpn_server.md), aby skonfigurować serwer OpenVPN na routerze GL.iNet, nawet jeśli nie masz publicznego adresu IP. 

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Następnie wyeksportuj konfigurację OpenVPN. Oto przykładowy plik konfiguracyjny.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. (Opcjonalnie) Jeśli potrzebujesz zdalnego dostępu do sieci LAN serwera VPN, włącz **Allow Remote Access LAN**. W przeciwnym razie pomiń ten krok.

    ??? "Dla firmware v4.7 i wcześniejszych"

        1. Na pasku bocznym po lewej stronie kliknij **VPN** > **VPN Dashboard**. 
        2. Kliknij ikonę Options.
        3. Przełącz przełącznik na włączony dla **Remote Access LAN**.
        4. Kliknij **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "Dla firmware v4.8 i nowszych"

        1. Na pasku bocznym po lewej stronie kliknij **VPN** > **OpenVPN Server**.
        2. Kliknij **Options** w prawym górnym rogu.
        3. Przełącz przełącznik na włączony dla **Allow Remote Access the LAN Subnet**.
        4. Kliknij **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3. Załóż konto AstroRelay i postępuj zgodnie z tym [poradnikiem](https://www.astrorelay.com/tutorial.html){target="_blank"}, aby ukończyć początkową konfigurację.

    Podczas dodawania nowej domeny wybierz serwer najbliższy routerowi.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Podczas dodawania nowego linku wprowadź **adres IP LAN** routera w pole **Destination Host IP** i wprowadź **1194** w pole **Destination Port**.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Otrzymasz wtedy link, taki jak **testforx3000.arlab1.cc:37202**. Kliknij go, aby skopiować link.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4. Otwórz plik konfiguracyjny OpenVPN i zamień wartość po **Remote** na link uzyskany w poprzednim kroku. W poniższym przykładzie "42.200.00.00 1194" zostaje zastąpiony linkiem "testforx3000.arlab1.cc:37202". Następnie zastąp dwukropek ":" spacją i zastosuj zmiany.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5. Zainstaluj [aplikację OpenVPN Connect](https://openvpn.net/client/){target="_blank"} na urządzeniu, którego chcesz użyć jako klient OpenVPN. Następnie prześlij zmodyfikowany plik konfiguracyjny do aplikacji i uruchom połączenie. Alternatywnie prześlij go na inny router GL.iNet, aby skonfigurować go jako klienta OpenVPN.

    Po połączeniu będziesz mógł zdalnie uzyskać dostęp do lokalnych usług domowych lub biurowych.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.