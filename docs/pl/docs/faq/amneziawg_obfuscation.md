# Maskowanie AmneziaWG

AmneziaWG to protokół VPN oparty na WireGuard z wbudowanym maskowaniem ruchu. Jego parametry maskowania określają, w jaki sposób ruch jest ukrywany, aby utrudnić jego wykrycie przez restrykcyjną inspekcję sieciową.

Poniżej znajdziesz szczegółowe omówienie AmneziaWG, różnic między wersjami, działania AmneziaWG na routerach GL.iNet oraz przegląd parametrów.

## Dlaczego AmneziaWG?

Poprzednik AmneziaWG, czyli WireGuard, ugruntował swoją pozycję jako szybki i niezawodny protokół VPN dzięki zwartej bazie kodu i wysokiej wydajności. Jednak jego stałe nagłówki pakietów i przewidywalne rozmiary pakietów tworzą łatwo rozpoznawalną sygnaturę. Systemy DPI mogą bez trudu identyfikować takie pakiety i natychmiast zrywać połączenia – co jest krytycznym problemem w krajach objętych ścisłą cenzurą internetu.

AmneziaWG dziedziczy prostotę architektury i wysoką wydajność oryginalnej implementacji, ale usuwa rozpoznawalne sygnatury sieciowe, które sprawiają, że WireGuard jest łatwy do wykrycia przez systemy głębokiej inspekcji pakietów (DPI).

W skrócie:

- Maskuje cechy VPN, aby zapobiec wykryciu przez dostawców Internetu, zapory sieciowe lub systemy DPI.
- Sprawia, że połączenie VPN wygląda jak standardowy ruch sieciowy, zwiększając stabilność i skuteczność połączenia w sieciach z ograniczeniami.

## AmneziaWG V2.0

W porównaniu z AmneziaWG v1.0, wersja v2.0 zapewnia silniejsze maskowanie dzięki dodaniu nowych parametrów (**S3~S4**) oraz zastosowaniu dynamicznych nagłówków dla typów pakietów (**H1~H4** jako zakresów zamiast stałych wartości). Dodatkowo AmneziaWG 2.0 obsługuje parametry **I1~I5**, które wysyłają sformatowane pakiety UDP przed każdym handshake, aby upodobnić ruch AmneziaWG do zwykłego ruchu spoza VPN, skutecznie omijając głęboką inspekcję pakietów i poprawiając łączność w sieciach o ograniczonym dostępie. 

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

Dzięki tym usprawnieniom ruch VPN jest trudniejszy do wykrycia, przy zachowaniu wysokiej szybkości i niskich opóźnień charakterystycznych dla WireGuard.

!!! Tip "Jak rozpoznać wersję AmneziaWG?"

    **V1.0**: Brak parametrów S3-S4; H1-H4 to pojedyncze stałe liczby całkowite.
    
    **V2.0**: Jest to V2.0, jeśli spełniony jest dowolny z poniższych warunków:
            
    - Zawiera parametry S3-S4
    - H1-H4 są ustawione jako zakresy liczbowe
    - Zawiera niestandardowe parametry I1-I5.
            
    > Uwaga: I1-I5 nie są generowane automatycznie. Użytkownicy mogą ręcznie dodać je jako dodatkowe linie w pliku konfiguracji, aby ruch AmneziaWG wyglądał jak inne popularne protokoły, takie jak QUIC lub WebRTC.

## AmneziaWG na routerach GL.iNet

Obecnie kilka routerów GL.iNet (np. Brume 3, Flint 3, Flint 2 i Beryl AX) obsługuje protokół AmneziaWG w wybranych wersjach oprogramowania. Pełne oficjalne wsparcie będzie dostępne w oprogramowaniu w wersji 4.9 i stopniowo rozszerzane na kolejne modele.

Aby skonfigurować maskowanie VPN na routerach GL.iNet, zobacz [tutaj](../tutorials/vpn_obfuscation.md).

## Przegląd parametrów

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Liczba pakietów śmieciowych wysyłanych przed rozpoczęciem handshake przez klienta (w celu zakłócenia wykrywania cech ruchu) | 1~128 | 4~12 |
| Jmin         | Minimalny rozmiar losowych pakietów śmieciowych (bajty); musi być skonfigurowany razem z Jmax, aby określić rozmiar pakietów śmieciowych | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maksymalny rozmiar losowych pakietów śmieciowych | 0 ≤ Jmin < Jmax < 1280        | 0≤ Jmin < Jmax < 1280 |
| S1           | Losowe prefiksy dla pakietów Init         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Losowe prefiksy dla pakietów Response     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Losowe prefiksy dla pakietów Cookie       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Losowe prefiksy dla pakietów Data         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamiczne nagłówki dla typów pakietów; wartości losowe (v1.0) lub zakresy (v2.0)   | 5~2147483647; H1, H2, H3 i H4 muszą się różnić | 5~2147483647 |
| I1~I5        | Pakiety sygnaturowe do imitacji protokołu | dowolny hex-blob             | N/A |

Źródła: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Powiązany artykuł:

- [Jak skonfigurować maskowanie VPN na routerach GL.iNet](../tutorials/vpn_obfuscation.md){target="_blank"}

---

Nadal masz pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
