# Dlaczego prędkość mojego VPN jest niższa niż oczekiwano?

Jeśli zauważysz, że prędkość połączenia VPN jest niższa od teoretycznej prędkości maksymalnej testowanej w idealnej sieci lokalnej, w rzeczywistym użyciu jest to całkowicie normalne.

Rozwiązania VPN są projektowane z naciskiem na bezpieczeństwo i prywatność, co naturalnie wpływa na prędkość. W typowych warunkach sieciowych normalne jest, że prędkość VPN wynosi około 30–50% deklarowanej wartości maksymalnej. Ta różnica wynika z wielu czynników wpływających na wydajność, które wyjaśniamy poniżej, wraz z kilkoma wskazówkami pomagającymi poprawić działanie.

**Uwaga**: Poniższe metody mogą pomóc poprawić prędkość VPN, ale nie gwarantują osiągnięcia deklarowanych wartości, ponieważ rzeczywista wydajność zależy od wielu czynników.

## Prędkość procesora routera

VPN szyfruje dane w celu ochrony prywatności, co wymaga dodatkowego przetwarzania. Szyfrowanie i odszyfrowywanie może spowolnić połączenie. Aby uzyskać wyższą prędkość VPN, wybierz router z wydajniejszym procesorem.

Prędkości testowe VPN dla wszystkich modeli podano na naszej [stronie produktów](https://www.gl-inet.com/products/). Pamiętaj jednak, że:

* testy są przeprowadzane w sieci lokalnej. Rzeczywiste prędkości mogą się różnić w zależności od konfiguracji sieci;
* prędkości OpenVPN i WireGuard będą niższe, gdy router działa jako serwer VPN. Powyższe wyniki dotyczą trybu klient VPN.

## Odległość od serwera

Jeśli serwer VPN znajduje się daleko od Twojej fizycznej lokalizacji, dane muszą pokonać większą odległość, co powoduje wyższe opóźnienia i niższą prędkość.

Poniższy przykład pokazuje prędkości klienta VPN podczas łączenia się z serwerami w różnych lokalizacjach o tej samej porze dnia.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Obciążenie serwera

Jeśli z tym samym serwerem VPN łączy się wielu użytkowników, może dojść do przeciążenia, co spowolni połączenie wszystkim.

## Prędkość wysyłania po stronie serwera

Jeśli korzystasz z prywatnego tunelu VPN, prędkość wysyłania po stronie dostawcy internetu (ISP) serwera będzie wąskim gardłem dla prędkości pobierania po stronie klienta VPN, ponieważ klient VPN pobiera dane przez serwer.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Różnice między protokołami

Różne protokoły VPN, takie jak OpenVPN i WireGuard, różnią się pod względem bezpieczeństwa i prędkości. Niektóre mogą być wolniejsze ze względu na stosowane metody szyfrowania.

## Ograniczanie prędkości przez ISP

Niektórzy dostawcy internetu (ISP) mogą ograniczać prędkość użytkownikom korzystającym z VPN, zwłaszcza gdy podejrzewają duże zużycie danych. Jest to szczególnie częste w niektórych krajach rozwijających się lub małych miejscowościach, gdzie wielu użytkowników współdzieli ograniczoną infrastrukturę internetową.

## DNS

Niektórzy dostawcy internetu (ISP) mogą nie rozwiązywać domen VPN. Spróbuj użyć [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) w ustawieniach **Network** routera.

## MTU

Niektórzy dostawcy internetu (ISP), zwłaszcza operatorzy komórkowi, mogą ograniczać rozmiar pakietów danych. Spróbuj zmienić domyślne MTU z 1420 na 1380 lub 1280 w ustawieniach **VPN Client Options**.

Dla firmware v4.8 i nowszego zobacz [tutaj](../interface_guide/vpn_dashboard_v4.8.md/#tunnel-options).

Dla firmware v4.7 i wcześniejszego zobacz [tutaj](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
