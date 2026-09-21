# Jakość sieci

**Uwaga**: ta funkcja została wprowadzona w firmware v4.11.

---

W panelu administracyjnym WWW przejdź po lewej stronie do **FLOW CONTROL** -> **Network Quality**.

Pulpit jakości sieci monitoruje jakość połączenia internetowego w czasie rzeczywistym. Ocenia responsywność, opóźnienia i działanie DNS, a także wykrywa przerwy w połączeniu i utratę pakietów. Te wskaźniki pomagają zidentyfikować niestabilność sieci i problemy z łącznością, których same testy przepustowości mogą nie wykazać.

Na tej stronie można ocenić połączenie internetowe na podstawie wskaźnika jakości sieci i w razie potrzeby uruchomić lokalne testy prędkości.

**Uwaga**:

1. Ogólny wskaźnik jakości sieci GL.iNet jest obliczany według wzoru ważonego:

    `Wynik ogólny = wynik responsywności × 60% + wynik niezawodności × 40%`.

2. Speedtest jest lokalnym testem prędkości wykonywanym na routerze i podlega regułom ograniczania prędkości przez takie funkcje, jak SQM i QoS.

## Wskaźnik jakości sieci

Ta sekcja wyświetla ogólny wskaźnik jakości sieci, obliczany na podstawie wyniku responsywności i wyniku niezawodności. Każdy z tych wyników można wyświetlić osobno. Panel pokazuje również powiązane wskaźniki, takie jak opóźnienie, jitter i utrata pakietów, a także prędkości pobierania i wysyłania w czasie rzeczywistym w KB/s. Domyślnie pulpit używa domeny `google.com` jako celu testów łączności internetowej i rozpoznawania DNS.

Kliknij ikonę ustawień, aby skonfigurować cele sondowania.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Jako cele testów dostępności Internetu i rozpoznawania DNS można wybrać Baidu, Tencent, Alibaba, Google, Microsoft lub Cloudflare. Można także ręcznie wpisać własną domenę.

Skonfigurowane cele są używane do wykonywania testów łączności i DNS oraz obliczania wskaźnika jakości sieci.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: służy do sprawdzania łączności internetowej i pomiaru opóźnienia od końca do końca (cel ping Hop2).

- **DNS Resolution Target**: domena rozpoznawana podczas testów DNS. Odpytywane są zarówno rekordy A (IPv4), jak i AAAA (IPv6).

## Speedtest

Wbudowany test prędkości używa Cloudflare Speed Test do pomiaru prędkości pobierania i wysyłania, opóźnienia ping oraz bufferbloat. Podczas testu wyświetlane są wykresy prędkości w czasie rzeczywistym.

Kliknij **Run Speedtest**, aby rozpocząć test prędkości.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Po zakończeniu testu strona wyświetli wyniki.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
