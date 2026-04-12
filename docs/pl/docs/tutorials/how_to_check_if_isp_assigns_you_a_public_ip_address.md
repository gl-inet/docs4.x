# Jak sprawdzić, czy masz publiczny adres IP

Publiczny adres IP, w przeciwieństwie do prywatnego adresu IP, to unikalny identyfikator numeryczny przypisany urządzeniom podłączonym do internetu. Publiczny adres IP będzie potrzebny, jeśli chcesz hostować stronę internetową, skonfigurować serwer VPN lub udostępniać jakiekolwiek usługi online. Zwykle jest on przydzielany przez dostawcę usług internetowych. 

Jeśli nie masz pewności, czy masz publiczny adres IP, skorzystaj z jednej z poniższych metod, aby to sprawdzić. 

**Metoda 1: Skontaktuj się bezpośrednio ze swoim dostawcą usług internetowych**

**Metoda 2: Sprawdź adres IP w panelu administracyjnym routera i w internecie** 

1. Zaloguj się do panelu administracyjnego routera. 
    * W przypadku routerów GL.iNet wpisz `192.168.8.1` w przeglądarce internetowej i zaloguj się.
    * Jeśli w konfiguracji używasz więcej niż jednego routera, zaloguj się do panelu administracyjnego routera głównego. 
2. W panelu administracyjnym routera odszukaj adres IP WAN (np. 42.XXX.XX.)
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. W przeglądarce internetowej wyszukaj hasło „what is my ip”.
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Jeśli oba adresy IP są takie same, masz publiczny adres IP. 
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Jeśli nie masz publicznego adresu IP, możesz rozważyć użycie narzędzia do tunelowania z sieci prywatnej do internetu. Umożliwia ono udostępnienie witryny, serwera VPN lub usług w internecie, nawet jeśli nie masz publicznego adresu IP. 

---

Powiązane artykuły

- [Konfiguracja serwera WireGuard na routerze GL.iNet](../interface_guide/wireguard_server.md)
- [Konfiguracja serwera OpenVPN na routerze GL.iNet](../interface_guide/openvpn_server.md)
- [Przekierowanie portów](../interface_guide/port_forwarding.md)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

