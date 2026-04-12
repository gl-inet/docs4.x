# Jak uzyskać z klienta dostęp do urządzeń LAN serwera WireGuard przy użyciu nazw domen?

Ten samouczek wyjaśnia, jak uzyskać z klienta dostęp do urządzeń domowych (takich jak NAS, kamera IP itp.) w sieci LAN serwera WireGuard przy użyciu nazw domen.

## Topologia

Jak pokazano poniżej, z komputera w sieci LAN klienta możesz uzyskać dostęp do urządzeń takich jak NAS i kamera IP w sieci LAN serwera WireGuard, używając ich odpowiednich nazw domen.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Kroki konfiguracji

### 1. Edytuj Hosts na serwerze (opcjonalnie)

Ten krok ma zastosowanie wtedy, gdy serwer VPN nie może prawidłowo rozwiązywać lokalnych nazw domen. Jeśli nie masz pewności, pomiń ten krok.

Zaloguj się do panelu administracyjnego routera pełniącego rolę serwera VPN i przejdź do **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Wprowadź adres IP i nazwę domeny urządzeń domowych, do których chcesz uzyskać dostęp, a następnie kliknij **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Włącz zdalny dostęp do LAN na serwerze

??? "Dla routera serwera z firmware v4.8"

    W panelu administracyjnym serwera przejdź do **VPN** -> **WireGuard Server**. Kliknij **Options** w prawym górnym rogu.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Włącz **Allow Remote Access the LAN Subnet**, a następnie kliknij **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Po włączeniu tej opcji ten router i urządzenia w sieci LAN będą dostępne zdalnie przez VPN.**
 
??? "Dla routera serwera z firmware v4.7 i starszym"

    W panelu administracyjnym serwera przejdź do **VPN** -> **VPN Dashboard** -> sekcji **VPN Server**. Kliknij ikonę zębatki po prawej stronie serwera WireGuard.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Włącz **Remote Access LAN**, a następnie kliknij **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Po włączeniu tej opcji ten router i urządzenia w sieci LAN będą dostępne zdalnie przez VPN.**

### 3. Wyeksportuj konfigurację VPN

W panelu administracyjnym serwera przejdź do **VPN** -> **WireGuard Server** -> zakładki **Profiles** i kliknij **Add**, aby wyeksportować profil konfiguracyjny. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Następnie otrzymasz plik **.conf**, jak pokazano poniżej.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Otwórz ten plik. Upewnij się, że pole DNS w pliku wskazuje adres IP tunelu serwera, który jest wyświetlany w zakładce **Configuration** na stronie **WireGuard Server**, jak pokazano poniżej. Jednocześnie usuń z pola DNS wartość "64.6.64.6", jeśli występuje, aby uniknąć problemów z rozwiązywaniem DNS.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Uwaga**: Adres IP tunelu serwera WireGuard różni się w zależności od wersji firmware. Sprawdź adres IP tunelu swojego serwera.

### 4. Włącz serwer VPN

Na stronie **WireGuard Server** kliknij przycisk **Start** w prawym górnym rogu, aby uruchomić serwer.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Prześlij konfigurację VPN

Zaloguj się do panelu administracyjnego routera pełniącego rolę klienta VPN, przejdź do **VPN** -> **WireGuard Client**, a następnie kliknij **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Utwórz nazwę dla tej grupy i prześlij plik konfiguracyjny.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Przesyłanie zakończyło się pomyślnie. Kliknij **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Plik konfiguracyjny zostanie wyświetlony na liście.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Uruchom połączenie klienta VPN

Kliknij ikonę z trzema kropkami, aby rozpocząć połączenie VPN. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Gdy szara kropka zmieni kolor na zielony, klient WireGuard został pomyślnie połączony z serwerem.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Teraz możesz uzyskać z komputera w sieci LAN klienta dostęp do urządzeń domowych (takich jak NAS) w sieci LAN serwera, używając ich nazw domen.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

