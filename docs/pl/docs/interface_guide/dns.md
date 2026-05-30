# DNS

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **DNS**.

Ustawienia DNS na routerze określają, w jaki sposób nazwy domen są tłumaczone na adresy IP. Ta strona pozwala korzystać z serwerów DNS automatycznie pobranych z urządzeń nadrzędnych albo ustawić własne serwery DNS i skonfigurować ich priorytety.

Jeśli ustawisz własne serwery DNS, wszystkie zapytania DNS będą rozwiązywane przez wskazane serwery zamiast przez serwery DNS uzyskane z poszczególnych interfejsów sieciowych. W przeciwnym razie będą używane ustawienia DNS skonfigurowane dla każdego interfejsu.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Włączenie tej opcji może spowodować problemy z rozwiązywaniem prywatnych nazw DNS. Jeśli w Twojej sieci działa captive portal, wyłącz tę opcję.

- **Override DNS Settings for All Clients:** Po włączeniu tej opcji router będzie nadpisywał nieszyfrowane ustawienia DNS dla wszystkich klientów.

- **Allow Custom DNS to Override VPN DNS:** Po włączeniu tej opcji, jeśli ustawisz własny DNS, pakiety przesyłane przez tunel VPN będą rozwiązywane przy użyciu niestandardowego DNS zamiast ustawień DNS pochodzących z połączeń VPN.

## Ustawienia serwerów DNS

Dostępne są cztery tryby: Automatic, Encrypted DNS, Manual DNS i DNS Proxy.

### Automatic

W tym trybie router będzie automatycznie używał serwera DNS dostarczonego przez urządzenie nadrzędne (np. modem ISP, router główny) albo ustawień DNS odpowiadających poszczególnym interfejsom sieciowym.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS

Zapoznaj się z poniższymi instrukcjami odpowiednimi dla swojej wersji firmware.

!!! note "Dla firmware v4.8 i wcześniejszych"

    Dostępne są cztery typy szyfrowania: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS i Oblivious DNS over HTTPS.

    Najpierw wybierz **Encryption Type**. Pozostałe opcje zmienią się w zależności od wyboru.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - W przypadku **DNS over TLS (DoT)** wybierz dostawcę DNS spośród **Control D**, **NextDNS** i **Cloudflare**.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - W przypadku pozostałych trzech opcji (tj. DNSCrypt-Proxy, DNS over HTTPS i Oblivious DNS over HTTPS) wybierz z repozytorium co najmniej jeden serwer DNS.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "Dla firmware v4.9 i nowszego"

    Oprócz Control D, NextDNS i Cloudflare w trybie Encrypted DNS dostępnych jest teraz więcej dostawców DNS, w tym **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** i **OpenDNS**. W razie potrzeby możesz też ręcznie określić szyfrowany serwer DNS.

    Najpierw wybierz **DNS Provider**. Pozostałe opcje zmienią się w zależności od wyboru.

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - Jeśli wybierzesz konkretnego dostawcę DNS (np. NextDNS), wybierz typ szyfrowania spośród **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** i **DNS over QUIC (DoQ)**. Pamiętaj, że DNS over QUIC (DoQ) wprowadzono w firmware v4.9 i jest dostępny tylko przy korzystaniu z Control D, NextDNS lub AdGuard DNS jako dostawcy DNS.

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - Jeśli jako **DNS Provider** wybierzesz **Manual**, wybierz typ szyfrowania spośród **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** i **DNSCrypt**.

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        Następnie kliknij **Add a Server**, aby dodać co najmniej jeden serwer DNS. Możesz bezpośrednio wprowadzić URL albo format stamp szyfrowanego DNS. Listę publicznych serwerów znajdziesz pod adresem [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Porównanie typów szyfrowania

1. **DNS over TLS (DoT)**

    Szyfruje zapytania DNS przez dedykowany port TLS. Oddziela ruch DNS od zwykłego ruchu webowego i jest łatwy do zidentyfikowania przez operatorów sieci.

2. **DNS over HTTPS (DoH)**

    Przesyła dane DNS wewnątrz standardowego ruchu HTTPS. Miesza żądania DNS ze zwykłym ruchem webowym, zapewniając wysoką prywatność i omijając proste filtrowanie ruchu.

3. **DNS over QUIC (DoQ)**

    Opakowuje DNS w protokół QUIC. Zapewnia niskie opóźnienia, szybkie ponowne łączenie i stabilne działanie w niestabilnych sieciach.

4. **Oblivious DNS over HTTPS (ODoH)**

    Rozszerzona wersja DoH. Oddziela adres IP użytkownika od zapytań DNS, uniemożliwiając zarówno serwerowi, jak i dostawcom sieci śledzenie aktywności przeglądania.

5. **DNSCrypt**

    Dojrzały protokół szyfrowania DNS. Uwierzytelnia i szyfruje ruch DNS, koncentrując się na ochronie przed manipulacją i kompatybilności ze starszymi środowiskami sieciowymi.

### Manual DNS

W tym trybie możesz dostosować serwer DNS routera. Z listy rozwijanej wybierz co najmniej jeden **DNS Server** dla routera.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy

W tym trybie router będzie kierować wszystkie zapytania DNS z sieci LAN na wskazany adres serwera proxy (np. `8.8.8.8#53`). Może to być przydatne, jeśli w Twojej sieci działa inny serwer DNS lub Pi-hole.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Edycja Hosts

Możesz kliknąć przycisk **Edit Hosts** w prawym górnym rogu, aby dostosować statyczne reguły hostów.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Router nadaje priorytet tym regułom hostów podczas rozwiązywania żądań od podłączonych klientów.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
