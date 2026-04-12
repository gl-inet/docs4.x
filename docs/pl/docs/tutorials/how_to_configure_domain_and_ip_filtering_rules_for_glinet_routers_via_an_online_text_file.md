# Jak skonfigurować reguły filtrowania domen i IP dla routerów GL.iNet za pomocą pliku tekstowego online

Począwszy od firmware v4.7.0, funkcja "VPN Policy Based on the Target Domain or IP" w VPN oraz funkcja "Add a New Ruleset" w Kontroli rodzicielskiej obsługują importowanie reguł z linku do pliku tekstowego online. Ten artykuł przedstawia format tego pliku tekstowego.

## Opis formatu URL

### Obsługiwane i nieobsługiwane formaty URL

- Obsługiwane formaty plików dla pliku tekstowego: .txt, .conf, .log, itp.
- Nieobsługiwane formaty plików: pliki binarne takie jak .exe, .zip, .jpg, itp.

### Używanie GitHub do hostowania pliku tekstowego

Jeśli hostujesz plik tekstowy w publicznym repozytorium GitHub, upewnij się, że używasz surowego URL zawartości zamiast zwykłego URL GitHub.

Na przykład, poniższy URL GitHub wskazuje na zawartość internetową, a nie surową zawartość:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Aby router pobrał prawidłową zawartość, użyj surowego URL zawartości w następującym formacie:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

W ten sposób router będzie mógł pobrać czystą tekstową zawartość pliku.

## Formaty filtrów dla VPN Policy Based on the Target Domain or IP

Funkcja "VPN Policy Based on the Target Domain or IP" obsługuje następujące formaty filtrów w pliku tekstowym online:

* Format nazwy domeny: Użyj nazwy domeny, takiej jak `netflix.com`, aby dopasować wszystkie poddomeny `netflix.com`.
* Format poddomeny: Określ pełną poddomenę, taką jak `www.netflix.com`, aby dopasować tylko określoną poddomenę.
* Format CIDR: Użyj notacji CIDR, aby określić zakresy adresów IP, takie jak `192.168.10.0/24`.
* Format adresu IPv4: Określ pojedyncze adresy IPv4, takie jak `192.168.10.10`.

## Formaty filtrów dla Parental Control Add a New Ruleset

Funkcja "Add a New Ruleset" w Kontroli rodzicielskiej obsługuje następujące formaty filtrów w pliku tekstowym online:

* Format nazwy domeny: Użyj nazwy domeny, takiej jak `instagram.com`, aby dopasować wszystkie poddomeny `instagram.com`.
* Format poddomeny: Określ pełną poddomenę, taką jak `www.instagram.com`, aby dopasować tylko określoną poddomenę.

Podczas tworzenia pliku tekstowego online użyj jednego filtra na linię. Router przetworzy każdą linię zgodnie z określonym formatem i zastosuje odpowiednie reguły do funkcji VPN lub Kontroli rodzicielskiej.

## Przykłady

Dla "VPN Policy Based on the Target Domain or IP":

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

Dla "Parental Control Add a New Ruleset":

```
instagram.com
facebook
x.com
snapchat
```

Postępując zgodnie z tymi formatami filtrów, możesz łatwo tworzyć i utrzymywać plik tekstowy online do konfigurowania funkcji VPN i Kontroli rodzicielskiej na routerze.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.