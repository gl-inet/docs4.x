# DNS

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **DNS**.

Ustawienia DNS na routerze określają, w jaki sposób nazwy domen są tłumaczone na adresy IP. Ta strona pozwala korzystać z serwerów DNS automatycznie pobranych z urządzeń nadrzędnych albo ustawić własne serwery DNS i skonfigurować ich priorytety.

Jeśli ustawisz własne serwery DNS, wszystkie zapytania DNS będą rozwiązywane przez wskazane serwery zamiast przez serwery DNS uzyskane z poszczególnych interfejsów sieciowych. W przeciwnym razie będą używane ustawienia DNS skonfigurowane dla każdego interfejsu.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Włączenie tej opcji może spowodować problemy z rozwiązywaniem prywatnych nazw DNS. Jeśli w Twojej sieci działa captive portal, wyłącz tę opcję.

- **Override DNS Settings for All Clients:** Po włączeniu tej opcji router będzie nadpisywał nieszyfrowane ustawienia DNS dla wszystkich klientów.

- **Allow Custom DNS to Override VPN DNS:** Po włączeniu tej opcji, jeśli ustawisz własny DNS, pakiety przesyłane przez tunel VPN będą rozwiązywane przy użyciu niestandardowego DNS zamiast ustawień DNS pochodzących z połączeń VPN.

## Ustawienia serwerów DNS

Dostępne są cztery tryby: **Automatic**, **Encrypted DNS**, **Manual DNS** i **DNS Proxy**.

- **Automatic**: Router będzie automatycznie korzystał z serwera DNS udostępnionego przez urządzenie nadrzędne (np. modem dostawcy Internetu lub router główny) albo z ustawień DNS przypisanych do poszczególnych interfejsów sieciowych.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: Dostępne są cztery typy szyfrowania: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS i Oblivious DNS over HTTPS.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - W przypadku DNS over TLS wybierz dostawcę DNS spośród Control D, NextDNS i Cloudflare.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - W przypadku pozostałych trzech opcji (DNSCrypt-Proxy, DNS over HTTPS i Oblivious DNS over HTTPS) wybierz z repozytorium co najmniej jeden serwer DNS.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: Wybierz z listy rozwijanej co najmniej jeden serwer DNS dla routera.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: Router będzie kierować wszystkie zapytania DNS z sieci LAN na wskazany adres serwera proxy, np. `8.8.8.8#53`. Może to być przydatne, jeśli w sieci działa inny serwer DNS lub Pi-hole.

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Edycja Hosts

Żądania od klientów będą w pierwszej kolejności rozwiązywane z użyciem statycznych reguł DNS zapisanych w sekcji Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
