# Jak uzyskać z klienta dostęp do urządzeń LAN serwera OpenVPN przy użyciu nazw domen?

Ten samouczek wyjaśnia, jak uzyskać z klienta dostęp do urządzeń domowych (takich jak NAS, kamera IP itp.) w sieci LAN serwera OpenVPN przy użyciu nazw domen.

## Topologia

Jak pokazano poniżej, z komputera w sieci LAN klienta możesz uzyskać dostęp do urządzeń takich jak NAS i kamera IP w sieci LAN serwera OpenVPN, używając ich odpowiednich nazw domen.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Kroki konfiguracji

### 1. Edytuj Hosts na serwerze (opcjonalnie)

Ten krok ma zastosowanie wtedy, gdy serwer VPN nie może prawidłowo rozwiązywać lokalnych nazw domen. Jeśli nie masz pewności, pomiń ten krok.

Zaloguj się do panelu administracyjnego routera pełniącego rolę serwera VPN i przejdź do **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Wprowadź adres IP i nazwę domeny urządzeń domowych, do których chcesz uzyskać dostęp, a następnie kliknij **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Włącz zdalny dostęp do LAN na serwerze

W panelu administracyjnym serwera przejdź do **VPN** -> **OpenVPN Server**. Kliknij **Options** w prawym górnym rogu.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Włącz **Allow Remote Access the LAN Subnet**, a następnie kliknij **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Po włączeniu tej opcji router i urządzenia w sieci LAN będą dostępne zdalnie przez VPN.

### 3. Wyeksportuj konfigurację VPN

W panelu administracyjnym serwera przejdź do **VPN** -> **OpenVPN Server** -> zakładki **Configuration**, a następnie kliknij na dole **Export Client Configuration**. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

W wyskakującym oknie kliknij **Export**. 

**Uwaga**: Jeśli publiczny adres IP na serwerze jest dynamiczny i od czasu do czasu się zmienia, przed wyeksportowaniem konfiguracji klienta przejdź do **APPLICATIONS** -> **Dynamic DNS**, aby włączyć **DDNS**.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Następnie otrzymasz plik **.ovpn**, jak pokazano poniżej.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Jeśli router serwera działa na firmware v4.8 lub nowszym, nie trzeba edytować pliku konfiguracyjnego — przejdź do następnego kroku.

Jeśli router serwera działa na firmware v4.7 lub starszym, otwórz ten plik, dodaj poniższą linię, aby ustawić serwer DNS na adres IP tunelu serwera OpenVPN, a następnie zapisz zmiany.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Wskazówka: Podsieć IPv4 tunelu serwera OpenVPN jest widoczna w zakładce **Configuration** na stronie OpenVPN Server, jak pokazano poniżej. Może się ona różnić w zależności od wersji firmware. Sprawdź adres IP tunelu swojego serwera OpenVPN.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Włącz serwer VPN

Na stronie **OpenVPN Server** kliknij przycisk **Start** w prawym górnym rogu, aby uruchomić serwer.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Prześlij konfigurację VPN

Zaloguj się do panelu administracyjnego routera pełniącego rolę klienta VPN, przejdź do **VPN** -> **OpenVPN Client**, a następnie kliknij **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Utwórz nazwę dla tej grupy i prześlij plik konfiguracyjny.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Przesyłanie zakończyło się pomyślnie. Kliknij **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Plik konfiguracyjny zostanie wyświetlony na liście.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Uruchom połączenie klienta VPN

Kliknij ikonę z trzema kropkami, aby rozpocząć połączenie VPN. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Gdy szara kropka zmieni kolor na zielony, klient OpenVPN został pomyślnie połączony z serwerem.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Teraz możesz uzyskać z komputera w sieci LAN klienta dostęp do urządzeń domowych (takich jak NAS) w sieci LAN serwera, używając ich nazw domen.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

