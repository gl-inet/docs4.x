# Jak przekierować zapytania DNS klienta VPN do nadrzędnego DNS serwera VPN?

Ten poradnik przedstawia kroki przekierowania wszystkich zapytań DNS od klientów VPN do własnego serwera DNS znajdującego się po stronie LAN routera głównego, powyżej serwera VPN.

## Topologia

W tym poradniku używamy **Flint 3 (GL-BE9300)** i **Slate 7 (GL-BE3600)** jako przykładów.

Flint 3 to serwer VPN, który ma router główny w sieci nadrzędnej, a Slate 7 to klient VPN łączący się z Flint 3.

Gdy tunel VPN zostanie nawiązany między serwerem VPN a klientem, domyślnie zapytania DNS od klienta VPN są najpierw wysyłane do serwera VPN, następnie przekazywane do routera głównego i ostatecznie rozwiązywane przez serwery DNS przypisane przez dostawcę usług internetowych, skonfigurowane w WAN routera głównego.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Jednak jeśli wdrożono własny serwer DNS (adres IP `192.168.1.13`) na routerze głównym, wymagane są dodatkowe konfiguracje, aby przekierować zapytania DNS do własnego serwera DNS.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Konfiguracja

1. Zaloguj się do panelu administratora Flint 3, przejdź do **NETWORK** -> **DNS**. Przełącz tryb serwera DNS na **Manual DNS** i wprowadź adres IP swojego serwera DNS.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Przejdź do **VPN** -> **WireGuard Server** -> zakładka **Configuration**, zanotuj adres IPv4, który zwykle wynosi `10.0.0.1/24` lub `10.1.0.1/24`, w zależności od modelu i wersji firmware.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Przełącz się na zakładkę **Profiles**, dodaj konfigurację klienta i wyeksportuj profil dla Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Otwórz profil, upewnij się, że DNS to adres IP serwera VPN uzyskany w kroku 2. 

    Aby uniknąć błędów rozwiązywania nazw DNS, usuń "64.6.64.6" jeśli występuje, i zapisz zmiany.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. W panelu administratora Flint 3 kliknij przycisk **Start** u góry strony **WireGuard Server**, aby uruchomić serwer.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Zaloguj się do panelu administratora Slate 7, przejdź do **VPN** -> **WireGuard Client**. 

    Kliknij **Add Manually** i prześlij edytowany profil. 

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Kliknij ikonę trzech kropek, aby uruchomić połączenie VPN. Jeśli wskaźnik statusu zmieni kolor na zielony, oznacza to, że połączenie VPN zostało nawiązane pomyślnie.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Weryfikacja rozwiązywania nazw DNS

Uruchom następujące polecenie, aby przechwycić ruch DNS na kliencie VPN. Pokaże to, że cały ruch DNS klienta VPN trafia do serwera VPN (tj. `10.0.0.1` w tym przykładzie).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Uruchom następujące polecenie, aby przechwycić ruch DNS na serwerze VPN. Pokaże to, że cały ruch DNS klienta VPN ostatecznie trafia do własnego serwera DNS (tj. `192.168.1.13` w tym przykładzie).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.