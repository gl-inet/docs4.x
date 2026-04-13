# Multi-WAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

W lewym panelu administratora przejdź do **NETWORK** -> **Multi-WAN**.

Możesz skonfigurować router z wieloma metodami dostępu do Internetu, tak aby w przypadku niedostępności jednej metody router automatycznie przełączył się na inną w krótkim czasie. Możliwe jest też jednoczesne korzystanie z wielu metod dostępu i rozdzielanie ruchu sieciowego między różne połączenia w określonych proporcjach.

Routery GL.iNet mogą łączyć się z Internetem na wiele sposobów, takich jak [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md), [Cellular](internet_cellular.md).

!!! Note

    1. Modele bez funkcji Wi-Fi (np. GL-MT2500/GL-MT2500A) obsługują wyłącznie dostęp przez Ethernet, Tethering i sieć komórkową.

    2. Modele bez portu USB (np. GL-B3000) obsługują wyłącznie dostęp przez Ethernet i Repeater.

    3. Niektóre modele obsługują [podwójny WAN przez Ethernet](dual-ethernet_wan.md), co dodaje dodatkowy interfejs Ethernet w interfejsie użytkownika.

## Interface Status Track

Routery GL.iNet obsługują do 5 wirtualnych interfejsów sieciowych, choć dokładna liczba może się różnić w zależności od modelu. Przykładowo GL-MT6000 ma interfejsy **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** i **Cellular**, z których każdy pełni odrębną funkcję sieciową w konfiguracji definiowanej programowo.

Router używa polecenia **ping** lub **httping** (tylko dla wersji v4.3 i wcześniejszych) do śledzenia stanu połączenia z docelowym adresem IP w celu sprawdzenia dostępności interfejsu.

Jeśli interfejs jest dostępny, po jego lewej stronie wyświetlana jest zielona kropka; w przeciwnym razie jest szara.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Status Track Settings

Kliknij ikonę koła zębatego, aby przejść do ustawień śledzenia stanu danego interfejsu sieciowego.

Poniżej przedstawiono przykład ustawień śledzenia stanu interfejsu Ethernet; to samo dotyczy pozostałych interfejsów.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: Opcja jest domyślnie włączona. Możesz wyłączyć śledzenie stanu interfejsu; wówczas router będzie określał stan interfejsu na podstawie stanu fizycznego (np. tego, czy kabel sieciowy jest podłączony).

- **Detection Mode**: Funkcja ta została wprowadzona jako Low Data Mode w v4.5 i przemianowana na Detection Mode w v4.7. Dostępne są trzy tryby: Normal Mode, Low Data Mode i Strict Mode.

    Domyślnie stosowany jest tryb Normal. Tryb Low Data przeprowadza wykrywanie tylko w przypadku błędu sieciowego interfejsu, natomiast tryb Strict określa stan interfejsu wyłącznie na podstawie wyników polecenia wykrywającego z publicznego adresu IP.

    Low Data Mode warto stosować przy ograniczonym planie danych. Jego wadą jest nieco wolniejsze przywracanie połączenia po jego zerwaniu w porównaniu z trybem normalnym; domyślnie tylko interfejs komórkowy będzie włączony.

- **Track Command**: Do śledzenia stanu połączenia z docelowym adresem IP używane jest polecenie ping. W oprogramowaniu v4.3 i wcześniejszym dostępne jest również polecenie httping.

- **IPv4 Track IP**: Możesz tu dostosować adres IPv4 używany do śledzenia.

!!! Note

    Niektóre starsze wersje oprogramowania, takie jak v4.3, udostępniały ustawienia takie jak **Track Interval**, **Change to Failure Condition** i **Change to Available Condition**. Zostały one usunięte od wersji v4.5 i zastąpione przez Detection Mode oraz opcje czułości.

### Opcje czułości

Funkcja dostępna od wersji v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Czułość określa interwał czasowy wykrywania stanu połączenia z Internetem.

- W przypadku stabilnej sieci i korzystania z takich funkcji jak oglądanie filmów, transmisje na żywo czy gry online zaleca się ustawienie wysokiej czułości, aby umożliwić szybkie przełączanie po zerwaniu połączenia.
- W przypadku niestabilnej sieci i pobierania buforowanych plików zaleca się niską czułość, aby zapobiec ciągłemu przełączaniu sieci i wykrywaniu nieudanych połączeń.

**Wskazówka**: Przełączenie na wysoką czułość może spowodować zerwanie połączenia sieciowego – zmieniaj to ustawienie z ostrożnością.

## Metody Multi-WAN

Dostępne są dwie metody: **Failover** i **Load Balance**. Gdy dostępnych jest kilka połączeń WAN, domyślnie włączony jest tryb Failover.

**Failover** i **Load Balance** wzajemnie się wykluczają – można używać tylko jednej z tych metod.

### Failover (przełączenie awaryjne)

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Możesz ustawić priorytety interfejsów. Gdy aktywny interfejs ulegnie awarii, router automatycznie przełączy się na inny dostępny interfejs o najwyższym priorytecie.

Przykładowo: jeśli router ma skonfigurowane dwa typy dostępu do Internetu – **Ethernet** i **Repeater** – a priorytet Ethernet wynosi 1, a Repeater 2, Ethernet ma wyższy priorytet i router będzie z niego korzystał. Po odłączeniu kabla sieciowego interfejs Ethernet staje się niedostępny i router automatycznie przełącza się na interfejs Repeater.

Po przywróceniu połączenia Ethernet router automatycznie wróci do tego interfejsu, ponieważ ma wyższy priorytet.

### Load Balance (równoważenie obciążenia)

Jednoczesne korzystanie z wielu interfejsów sieciowych zwiększa całkowitą przepustowość routera.

Współczynnik obciążenia określa proporcje między interfejsami; system przydziela interfejsy do nowych połączeń zgodnie z ustawionym współczynnikiem.

Przykładowo: jeśli router jest jednocześnie podłączony do czterech sieci (Ethernet, Repeater, Tethering i Cellular) i wszystkie cztery interfejsy są dostępne, włączenie Load Balance z ustawieniem 1:1:1:1 oznacza, że przepustowość sieciowa zostanie rozłożona równo między cztery interfejsy, ponieważ system przydziela je do nowych połączeń w proporcji 1:1:1:1.

Możesz też dostosować współczynniki obciążenia. Jeśli przepustowość Ethernet wynosi 200 Mbps, Repeater Wi-Fi 100 Mbps, a brak aktywnych połączeń Tethering i Cellular, możesz ustawić: 2 dla Ethernet, 1 dla Repeater i 0 dla Tethering/Cellular. System rozdzieli nowe połączenia w proporcji 2:1, co oznacza, że Ethernet obsłuży około dwukrotnie więcej połączeń niż Repeater. W porównaniu z trybem Failover pozwala to zoptymalizować ogólną przepustowość poprzez równomierne rozłożenie obciążenia.

**Uwaga:** Aktywne połączenia i ruch nie zawsze dokładnie odzwierciedlają ustawiony współczynnik. Im dłużej system jest używany, tym bliżej tej proporcji będą faktyczne wyniki.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

## Scenariusze użycia

* Kasa w sklepie jest podłączona do Internetu kablem sieciowym, a połączenie przez Repeater z siecią Wi-Fi sąsiednich sklepów (lub przez kartę SIM z siecią komórkową) służy jako zapasowy dostęp do Internetu – na wypadek niedostępności kabla podczas realizacji płatności mobilnych.

* Router łączy się przez Repeater z publiczną siecią Wi-Fi, ale prędkość jest niewystarczająca – w takim przypadku można jednocześnie użyć Mobile Tethering w trybie Load Balance, aby zwiększyć ogólną przepustowość.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
