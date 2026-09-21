# DNS

**Uwaga**: zawartość tej strony została po raz pierwszy wprowadzona w firmware v4.11.

Jeśli urządzenie korzysta z innej wersji firmware, użyj poniższego selektora, aby przejść do odpowiedniego przewodnika.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 i wcześniejsze](dns.md)

</div>

---

W panelu administracyjnym WWW przejdź po lewej stronie do **DNS**.

Ustawienia DNS routera określają sposób tłumaczenia nazw domen na adresy IP. Na tej stronie można korzystać z serwerów DNS uzyskanych automatycznie z urządzeń nadrzędnych lub skonfigurować własne. Można także ustawić opcje DNS i edytować statyczne reguły hostów.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

Domyślnie zapytania DNS dla ruchu zgodnego z polityką VPN korzystają z serwerów DNS udostępnionych przez tunel VPN. Zapytania DNS spoza VPN korzystają z serwerów uzyskanych z aktywnego interfejsu WAN. Własne serwery DNS można zastosować do tuneli VPN, do samego routera lub do obu tych zakresów. Po włączeniu tych opcji zapytania DNS w wybranym zakresie są rozwiązywane przez określone serwery zamiast serwerów uzyskanych z odpowiednich interfejsów sieciowych. Jeśli nie ustawiono własnych serwerów DNS, router korzysta z serwerów uzyskanych z odpowiednich interfejsów sieciowych.

## DNS WAN

Sekcja DNS WAN wyświetla serwery DNS pobrane z każdego łącza WAN, w tym Ethernet, Repeater, Tethering i Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Jeśli łącze WAN jest aktywne, jego adresy serwerów DNS są wyświetlane po prawej stronie, jak pokazano poniżej.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## DNS VPN

Sekcja DNS VPN pokazuje serwery DNS uzyskane z każdego aktywnego tunelu VPN.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Jeśli tunel VPN jest aktywny, zapytania DNS z ruchu VPN są obsługiwane zgodnie z konfiguracją DNS VPN, jak pokazano poniżej.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## Ręczny DNS

Ręczny DNS obsługuje dwa typy konfiguracji: **Static DNS** i **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: po włączeniu tej opcji pakiety przesyłane przez tunel VPN będą korzystać z niestandardowego ręcznego DNS zamiast ustawień DNS sieci VPN.

- **Apply Manual DNS to Router Itself**: ta opcja jest domyślnie włączona. Po jej włączeniu wbudowane usługi routera, takie jak GoodCloud, korzystają z niestandardowych ręcznych ustawień DNS.

### Statyczny DNS

Statyczny DNS umożliwia ręczne wprowadzenie adresów serwerów DNS IPv4 lub IPv6. Adresy można wpisać bezpośrednio albo wybrać gotowe publiczne serwery DNS z listy rozwijanej.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Można wprowadzić maksymalnie cztery adresy serwerów DNS. Kliknij **Apply**, aby zapisać zmiany.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Szyfrowany DNS

Tryb szyfrowanego DNS obsługuje wielu dostawców, w tym Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS i OpenDNS. W razie potrzeby można także ręcznie określić szyfrowany serwer DNS.

Najpierw wybierz dostawcę DNS. Pozostałe opcje zmienią się zależnie od wyboru.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Po wybraniu konkretnego dostawcy DNS, np. NextDNS, wybierz typ szyfrowania: DNS over TLS (DoT), DNS over HTTPS (DoH) lub DNS over QUIC (DoQ). DNS over QUIC (DoQ) został wprowadzony w firmware v4.9 i jest dostępny tylko w przypadku dostawców Control D, NextDNS lub AdGuard DNS.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Jeśli jako dostawcę DNS wybierzesz Manual, wybierz typ szyfrowania: DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS lub DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Następnie kliknij **Add a Server**, aby dodać co najmniej jeden serwer DNS. Można bezpośrednio wprowadzić adres URL lub znacznik szyfrowanego DNS. Lista serwerów publicznych jest dostępna na stronie [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Porównanie typów szyfrowania"

    1. **DNS over TLS (DoT)**

        Szyfruje zapytania DNS przez dedykowany port TLS. Oddziela ruch DNS od zwykłego ruchu WWW i jest łatwy do rozpoznania przez operatorów sieci.

    2. **DNS over HTTPS (DoH)**

        Przesyła dane DNS wewnątrz standardowego ruchu HTTPS. Łączy zapytania DNS ze zwykłym ruchem WWW, zapewniając wysoki poziom prywatności i omijając proste filtrowanie ruchu.

    3. **DNS over QUIC (DoQ)**

        Enkapsuluje DNS w protokole QUIC. Zapewnia niskie opóźnienia, szybkie ponowne łączenie i stabilne działanie w niestabilnych sieciach.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Rozszerzona wersja DoH. Oddziela adres IP użytkownika od zapytań DNS, uniemożliwiając serwerowi i dostawcom sieci śledzenie aktywności przeglądania.

    5. **DNSCrypt**

        Dojrzały protokół szyfrowania DNS. Uwierzytelnia i szyfruje ruch DNS, koncentrując się na ochronie przed manipulacją i zgodności ze starszymi środowiskami sieciowymi.

## Opcje DNS

Kliknij **Options** w prawym górnym rogu, aby skonfigurować zaawansowane ustawienia DNS.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

W razie potrzeby można włączać i wyłączać poniższe opcje.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: włączenie tej opcji może powodować błędy prywatnych zapytań DNS. Jeśli sieć korzysta z portalu przechwytującego, wyłącz tę opcję.

- **Override DNS Settings of All Clients**: po włączeniu router zastępuje nieszyfrowane ustawienia DNS wszystkich klientów.

## Edycja hostów

Kliknij przycisk **Edit Hosts** w prawym górnym rogu, aby dostosować statyczne reguły hostów.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Router nadaje tym regułom priorytet podczas rozwiązywania żądań od podłączonych klientów.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
