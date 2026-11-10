# Maskowanie AmneziaWG {#amneziawg-obfuscation}

AmneziaWG to protokół VPN oparty na WireGuard z wbudowanym maskowaniem ruchu. Jego parametry maskowania określają, w jaki sposób ruch jest ukrywany, aby utrudnić jego wykrycie przez restrykcyjną inspekcję sieciową.

Poniżej znajdziesz szczegółowe omówienie AmneziaWG i różnic między wersjami.

## Dlaczego AmneziaWG? {#why-amneziawg}

Poprzednik AmneziaWG, czyli WireGuard, ugruntował swoją pozycję jako szybki i niezawodny protokół VPN dzięki zwartej bazie kodu i wysokiej wydajności. Jednak jego stałe nagłówki pakietów i przewidywalne rozmiary pakietów tworzą łatwo rozpoznawalną sygnaturę. Systemy DPI mogą bez trudu identyfikować takie pakiety i natychmiast zrywać połączenia – co jest krytycznym problemem w krajach objętych ścisłą cenzurą internetu.

AmneziaWG zachowuje prostotę architektury i wysoką wydajność oryginalnej implementacji WireGuard, dodając dedykowany moduł maskowania wzorców ruchu VPN. Pomaga to użytkownikom indywidualnym i firmowym chronić prywatność online oraz utrzymywać stabilne połączenia w restrykcyjnych środowiskach sieciowych.

W skrócie:

- Maskuje cechy VPN, aby zapobiec wykryciu przez dostawców Internetu, zapory sieciowe lub systemy DPI.
- Sprawia, że połączenie VPN wygląda jak standardowy ruch sieciowy, zwiększając stabilność i skuteczność połączenia w sieciach z ograniczeniami.

## AmneziaWG V2.0 {#amneziawg-v20}

### Przegląd {#amneziawg-v20-overview}

<font color="red">**Uwaga**: Routery GL.iNet obsługują AmneziaWG 2.0 od wersji oprogramowania v4.9.0.</font>

AmneziaWG 2.0 zachowuje mechanizmy maskowania z wersji v1.0: serię pakietów śmieciowych (**Jc**, **Jmin**, **Jmax**) i losowe prefiksy pakietów Init i Response (**S1–S2**). Wprowadza też następujące mechanizmy, aby ukryć cechy połączenia, które dotychczas były przewidywalne:

* **S3–S4**: losowe prefiksy pakietów Cookie i Data. W wersji v1.0 dopełniano tylko pakiety Init i Response, więc pakiety Cookie miały dokładnie 64 bajty, a długość pakietów Data była równa długości danych użytecznych.

* **H1–H4 jako zakresy**: wartość nagłówka każdego typu pakietu jest wybierana z zakresu, zamiast mieć jedną stałą wartość. Przy odbiorze akceptowana jest każda wartość z odpowiedniego zakresu. Cztery zakresy nie mogą się pokrywać.

* **I1–I5**: pakiety UDP definiowane przez użytkownika i wysyłane przed każdym uzgadnianiem połączenia. Dzięki temu sesja rozpoczyna się od ruchu przypominającego popularny protokół UDP, co maskuje uzgadnianie połączenia WireGuard.

Dzięki tym usprawnieniom ruch VPN jest trudniejszy do wykrycia, przy zachowaniu wysokiej szybkości i niskich opóźnień charakterystycznych dla WireGuard.

!!! Tip "Jak odróżnić AmneziaWG 1.0 od 2.0?"

    **V1.0**: Brak parametrów S3-S4; H1-H4 to pojedyncze stałe liczby całkowite.
    
    **V2.0**: Jest to V2.0, jeśli spełniony jest dowolny z poniższych warunków:
            
    - Zawiera parametry S3-S4
    - H1-H4 są ustawione jako zakresy liczbowe
    - Zawiera niestandardowe parametry I1-I5.
            
    > Uwaga: I1-I5 nie są generowane automatycznie. Użytkownicy mogą ręcznie dodać je jako dodatkowe linie w pliku konfiguracji, aby ruch AmneziaWG wyglądał jak inne popularne protokoły, takie jak QUIC lub WebRTC.

### Parametry {#amneziawg-v20-parameters}

| Parametr | Opis | Ograniczenia | Generowane automatycznie |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Liczba pakietów śmieciowych wysyłanych przed rozpoczęciem uzgadniania połączenia przez klienta (w celu zakłócenia wykrywania cech ruchu) | 1~128 | 4~12 |
| Jmin         | Minimalny rozmiar losowych pakietów śmieciowych (bajty); musi być skonfigurowany razem z Jmax, aby określić rozmiar pakietów śmieciowych | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maksymalny rozmiar losowych pakietów śmieciowych | 0 ≤ Jmin < Jmax < 1280        | 0≤ Jmin < Jmax < 1280 |
| S1           | Losowe prefiksy dla pakietów Init         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Losowe prefiksy dla pakietów Response     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Losowe prefiksy dla pakietów Cookie       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Losowe prefiksy dla pakietów Data         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamiczne nagłówki dla typów pakietów; wartości losowe (v1.0) lub zakresy (v2.0)   | 5~2147483647; H1, H2, H3 i H4 muszą się różnić | 5~2147483647 |
| I1~I5        | Pakiety sygnaturowe do imitacji protokołu | dowolne dane w zapisie szesnastkowym             | Nie dotyczy |

Przykładowa sekcja parametrów maskowania w wersji v2.0:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Źródła: [Oficjalna dokumentacja AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Przegląd {#amneziawg-v31-overview}

<font color="red">**Uwaga**: Routery GL.iNet obsługują AmneziaWG 3.1 od wersji oprogramowania v4.11.1.</font>

AmneziaWG 3.1 zachowuje wszystkie mechanizmy maskowania z wersji v2.0: losowe prefiksy dla każdego typu pakietu (**S1–S4**), dynamiczne nagłówki (**H1–H4**), pakiety sygnaturowe wysyłane przed uzgadnianiem połączenia (**I1–I5**) i serię pakietów śmieciowych (**Jc**, **Jmin**, **Jmax**). Wprowadza też następujące mechanizmy, które utrudniają rozpoznawanie ruchu na podstawie jego cech:

- **Ochrona nagłówków**: Ukrywa za pomocą ChaCha20 pola nagłówków pakietów WireGuard, które w przeciwnym razie pozostałyby niezaszyfrowane.
- **Dopełnianie danych**: Dodaje do pakietów danych transportowych losową liczbę bajtów dopełnienia w granicach MTU.
- **Konfigurowalne parametry czasowe**: Umożliwia ustawienie wartości lub zakresów dotyczących zmiany klucza, ponawiania prób uzgadniania połączenia, pakietów podtrzymujących i powiązanych mechanizmów połączenia. Zalecane jest użycie wartości generowanych automatycznie zarówno na serwerze, jak i na kliencie.
- **Losowe zakończenia pakietów**: Dołącza dane o zmiennej długości na końcu pakietów uzgadniania połączenia i pakietów danych transportowych, aby bardziej zróżnicować ich rozmiary.
- **Wyłączenie odpowiedzi Cookie**: Pozwala urządzeniu przestać wysyłać odpowiedzi Cookie podczas uzgadniania połączenia. Nadal może ono odbierać takie odpowiedzi i wykonywać pozostałe etapy uzgadniania.

### Parametry {#amneziawg-v31-parameters}

Wersja AmneziaWG V3.1 wprowadza następujące parametry.

| Parametr | Opis | Ograniczenia | Zakres lub wartość GL.iNet |
| -------- | ---- | ------------ | -------------------------- |
| `HeaderProtectionKey` | Włącza ochronę pól nagłówka pakietu, które normalnie nie są szyfrowane, przy użyciu ChaCha20 | Dokładnie 32 bajty. Po włączeniu ochrony trzeba ustawić wszystkie parametry S1, S2, S3 i S4, każdy na wartość ≥ 12. Zalecane ustawienie to `H1=1`, `H2=2`, `H3=3`, `H4=4`: wyłącza ono niestandardowe nagłówki, a typ komunikatu ukrywa mechanizm ochrony nagłówków | Klucz 32-bajtowy |
| `ContentPaddingAddition` | Dodaje do każdego pakietu danych transportowych losową liczbę bajtów z ustawionego zakresu | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` wyłącza funkcję | 0–65535 (przykład: `10-50`) |
| `RekeyAfterTime` | Czas używania bieżącego klucza do rozpoczęcia aktywnej zmiany klucza (w sekundach) | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` przywraca wartość domyślną WireGuard | 100–150 (domyślna wartość WireGuard: 120) |
| `RekeyTimeout` | Czas oczekiwania na odpowiedź przed ponowieniem żądania uzgodnienia połączenia (w sekundach) | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` przywraca wartość domyślną WireGuard | 4–7 (domyślna wartość WireGuard: 5) |
| `RejectAfterTime` | Czas bez odbioru danych, po którym rozpoczyna się nowe uzgadnianie połączenia (w sekundach) | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` przywraca wartość domyślną WireGuard | 180–240 (domyślna wartość WireGuard: 180) |
| `KeepaliveTimeout` | Czas bez wysyłania danych, po którym wysyłany jest wewnętrzny pakiet podtrzymujący połączenie (w sekundach) | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` przywraca wartość domyślną WireGuard | 8–20 (domyślna wartość WireGuard: 10) |
| `MaxHandshakeAttempts` | Maksymalna liczba ponowień próby uzgodnienia połączenia | `range<uint16>`, 0–65535, min ≤ max; `0` lub `0-0` przywraca wartość domyślną WireGuard | 12–18 (domyślna wartość WireGuard: 18) |
| `RandomTrailers` | Dodaje zmienną liczbę bajtów na końcu pakietów: losowe dane w pakietach uzgadniania połączenia i zera za wewnętrznym pakietem IP w pakietach transportowych. Długość jest dobierana dynamicznie tak, aby nie przekroczyć MTU żadnej ze stron | `off` wyłącza funkcję. Po jej włączeniu zalecane jest ustawienie `S1 = S2 = S3 = S4`, aby zmniejszyć ryzyko błędnego rozpoznania typu pakietu z powodu losowych rozmiarów | `on` / `off` |
| `DisableCookies` | Uniemożliwia urządzeniu lokalnemu wysyłanie odpowiedzi Cookie podczas uzgadniania połączenia. Nie wpływa na odbiór odpowiedzi Cookie od drugiej strony ani na pozostałe etapy uzgadniania | `off` wyłącza funkcję. Parametry S3/H3 nadal muszą mieć prawidłowe wartości, ponieważ mogą być używane przy odbiorze | `on` / `off` |

**Uwagi**

* Wartości z zakresów podanych w ostatniej kolumnie może wygenerować router. Parametry `RandomTrailers` i `DisableCookies` ustawia się osobno na każdym urządzeniu.
* Wartość `HeaderProtectionKey` musi być taka sama na kliencie i serwerze.
* Wartości parametrów czasowych spoza podanych zakresów są podczas pracy zastępowane losowymi wartościami z odpowiednich zakresów. Własna wartość może więc nie zostać zastosowana w podanej postaci.
* Zarówno `ContentPaddingAddition`, jak i `S4` zmieniają długość pakietów transportowych, ale działają na różne części pakietu i można ich używać jednocześnie.
* Ochrona nagłówków i dynamiczne wartości `H` mogą działać jednocześnie. Parametry `H1–H4` mogą pozostać dynamiczne, choć zalecane ustawienie to `1/2/3/4`.

---

Przykładowa sekcja parametrów maskowania w wersji v3.1:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Źródła: [Oficjalna dokumentacja AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Powiązany artykuł:

- [Jak skonfigurować maskowanie VPN na routerach GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Nadal masz pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
