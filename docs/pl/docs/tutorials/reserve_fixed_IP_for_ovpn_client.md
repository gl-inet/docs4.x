# Jak zarezerwować stały adres IP dla klienta OpenVPN w samodzielnie utworzonym połączeniu OpenVPN?

Ten przewodnik pokaże, jak zarezerwować stały adres IP dla klienta OpenVPN łączącego się z serwerem. Przed wykonaniem poniższych kroków skonfiguruj router GL.iNet jako serwer OpenVPN.

1. Zaloguj się do panelu administracyjnego serwera OpenVPN, z lewego paska bocznego przejdź do **VPN** -> **OpenVPN Server**.

    W zakładce **Configuration** zanotuj **IPv4 subnet** (np. 10.8.0.0/24 jak na poniższym obrazku) i przełącz Authentication Mode na **Username and Password Only**.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Przejdź do zakładki **Users**, utwórz nazwę użytkownika i hasło, jak pokazano poniżej.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Zaloguj się do routera przez SSH i uruchom następujące polecenie, aby otworzyć plik skryptu konfiguracyjnego serwera OpenVPN:

    `vi /lib/netifd/proto/openserver.sh`

    W otwartym pliku sprawdź, czy w skrypcie istnieje linia "*client-config-dir /etc/openvpn/ccd*". 

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Jeśli nie, dodaj ją ręcznie, a następnie zapisz i zamknij plik.

4. Przejdź do `/etc/openvpn/`, dodaj folder ccd poleceniem `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Dodaj plik "GLsupport", wpisz `ifconfig-push 10.8.0.10 255.255.255.0`, następnie zapisz i zamknij plik.

    Zweryfikuj zawartość poleceniem `cat GLsupport`

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Gdy używasz konta GLsupport do połączenia z serwerem OpenVPN, zostanie mu przypisany stały adres IP 10.8.0.10. 
    
    - "255.255.255.0" to maska podsieci i możesz ją zastąpić maską podsieci swojego serwera OpenVPN.

    **Uwaga**: Jeśli chcesz przypisać stałe adresy IP dla wielu klientów OpenVPN, utwórz wiele nazw użytkownika i haseł w kroku 2, następnie powtórz krok 5, dodając pliki do folderu CCD w kolejności użytkowników, takich jak user_1, user_2, user_3, a następnie polecenie "ifconfig push" z odpowiadającymi im stałymi adresami IP i maskami podsieci. 
    
    Na przykład: `ifconfig-push 10.8.0.20 225.225.225.0`, `ifconfig-push 10.8.0.30 225.225.225.0`, `ifconfig-push 10.8.0.40 225.225.225.0`

6. Na koniec przetestuj z klientem OVPN i sprawdź, czy wirtualny adres IP klienta (IPv4) jest tym zarezerwowanym. 

    Na przykład, jeśli Twoim klientem OpenVPN jest router GL.iNet, możesz zalogować się do panelu administracyjnego routera klienta OpenVPN, przejść do VPN Dashboard i zweryfikować wirtualny adres IP klienta (IPv4).

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard w firmware v4.7 i wcześniejszych)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard w firmware v4.8)</small>

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
