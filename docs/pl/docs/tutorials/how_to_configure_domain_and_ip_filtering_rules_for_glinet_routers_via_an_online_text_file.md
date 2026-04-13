# Jak skonfigurować reguły filtrowania domen i IP dla routerów GL.iNet za pomocą pliku tekstowego online

Od firmware v4.7 następujące funkcje obsługują import reguł z adresu URL pliku tekstowego online:

- VPN Policy Based on Target Domains or IP Addresses (w sekcji VPN)
- Add a New Ruleset (w sekcji Parental Control)

Ten poradnik wyjaśnia, jak używać internetowego pliku tekstowego do importowania reguł filtrowania domen i adresów IP dla routerów GL.iNet.

## Obsługiwane formaty adresów URL i plików

Obsługiwane są następujące formaty adresów URL:

- Adresy URL zwykłych plików tekstowych (HTTP/HTTPS)
- GitHub Raw content URL

Obsługiwane typy plików to `.txt`, `.conf`, `.log` oraz inne formaty zwykłego tekstu.

**Uwaga**: Pliki binarne nie są obsługiwane, na przykład `.exe`, `.zip`, `.jpg`, `.png` itd.

## Używanie GitHub do hostowania pliku tekstowego

Jeśli hostujesz plik tekstowy w publicznym repozytorium GitHub, pamiętaj, aby używać adresu raw content URL zamiast zwykłego adresu GitHub.

Na przykład poniższy adres GitHub wskazuje zawartość strony, a nie surową zawartość pliku:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Aby router pobrał prawidłową zawartość, użyj adresu raw content URL w następującym formacie:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Dzięki temu router będzie mógł pobrać zwykłą tekstową zawartość pliku.

## Formaty filtrów dla VPN Policy (domena/IP)

Funkcja **VPN Policy Based on Target Domain or IP Address** obsługuje w internetowym pliku tekstowym następujące formaty filtrów:

* Nazwa domeny: użyj nazwy domeny, np. `netflix.com` (dopasowuje wszystkie subdomeny).
* Subdomena: podaj pełną subdomenę, np. `www.netflix.com` (dopasowuje tylko tę subdomenę).
* Zakres CIDR: użyj notacji CIDR do określenia zakresów adresów IP, np. `192.168.10.0/24`.
* Adres IPv4: podaj pojedynczy adres IPv4, np. `192.168.10.10`.

## Formaty filtrów dla Parental Control (Ruleset)

Funkcja **Add a New Ruleset** w Parental Control obsługuje w internetowym pliku tekstowym następujące formaty filtrów:

* Nazwa domeny: użyj nazwy domeny, np. `instagram.com` (dopasowuje wszystkie subdomeny).
* Subdomena: podaj pełną subdomenę, np. `www.instagram.com` (dopasowuje tylko tę subdomenę).

Podczas tworzenia internetowego pliku tekstowego używaj jednego filtra w każdym wierszu. Router przetworzy każdą linię zgodnie z określonym formatem i zastosuje odpowiednie reguły do funkcji VPN lub Parental Control.

Stosując te formaty filtrów, możesz łatwo tworzyć i utrzymywać internetowy plik tekstowy do konfigurowania funkcji VPN i Parental Control na routerze.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
