# Parametry maskowania AmneziaWG

AmneziaWG to protokół VPN oparty na WireGuard z wbudowanym maskowaniem ruchu. Jego parametry maskowania określają, w jaki sposób ruch jest ukrywany, aby utrudnić jego wykrycie przez restrykcyjne mechanizmy kontroli sieci. Poniżej znajdziesz szczegółowe omówienie różnic między wersjami AmneziaWG, parametrów maskowania, ich ograniczeń oraz zalecanych ustawień.

## AmneziaWG V2.0

W porównaniu z AmneziaWG v1.0, wersja v2.0 zapewnia silniejsze maskowanie dzięki dodaniu nowych parametrów (**S3~S4**) oraz zastosowaniu dynamicznych nagłówków dla typów pakietów (**H1~H4** jako zakresów zamiast stałych wartości). Dodatkowo AmneziaWG 2.0 obsługuje parametry **I1~I5**, które wysyłają sformatowane pakiety UDP przed każdym handshake, aby upodobnić ruch AmneziaWG do zwykłego ruchu spoza VPN, skutecznie omijając głęboką inspekcję pakietów i poprawiając łączność w sieciach o ograniczonym dostępie.

Dzięki tym usprawnieniom ruch VPN jest trudniejszy do wykrycia, przy zachowaniu wysokiej szybkości i niskich opóźnień charakterystycznych dla WireGuard.

Tak można rozpoznać wersję AmneziaWG:

- **V1.0**: Brak parametrów S3~S4; H1~H4 to pojedyncze stałe liczby całkowite.
- **V2.0**: Zawiera parametry **S3~S4**; **H1~H4** są zdefiniowane jako zakresy liczbowe; obsługuje parametry **I1~I5**.

**Uwaga**: Parametry I1-I5 nie są generowane automatycznie. Użytkownicy mogą ręcznie dodać je jako dodatkowe linie w pliku konfiguracji VPN, aby ruch AmneziaWG wyglądał jak inne popularne protokoły, takie jak QUIC lub WebRTC.

## Przegląd parametrów

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Liczba pakietów śmieciowych wysyłanych przed rozpoczęciem handshake przez klienta (w celu zakłócenia wykrywania cech ruchu) | 1~128 | 4~12 |
| Jmin         | Minimalny rozmiar losowych pakietów śmieciowych (bajty); musi być skonfigurowany razem z Jmax, aby określić rozmiar pakietów śmieciowych | 0 ≤ Jmin < Jmax < 65535 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maksymalny rozmiar losowych pakietów śmieciowych | 0 ≤ Jmin < Jmax < 65535        | 0≤ Jmin < Jmax < 1280 |
| S1           | Losowe prefiksy dla pakietów Init         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Losowe prefiksy dla pakietów Response     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Losowe prefiksy dla pakietów Cookie       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Losowe prefiksy dla pakietów Data         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamiczne nagłówki dla typów pakietów; wartości losowe (v1.0) lub zakresy (v2.0)   | 5~2147483647; H1, H2, H3 i H4 muszą się różnić | 5~2147483647 |
| I1~I5        | Pakiety sygnaturowe do imitacji protokołu | dowolny hex-blob             | N/A |

Źródło: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
