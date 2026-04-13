# Jak skonfigurować i używać Spitz AX (GL-X3000) w pojeździe rekreacyjnym

W tym przewodniku pokazujemy, jak skonfigurować i używać Spitz AX w pojeździe rekreacyjnym. Przed rozpoczęciem przygotuj następujące dodatkowe wyposażenie i usługi, jeśli będą potrzebne: 

- karta SIM / karty SIM lub kabel USB (do tetheringu), w zależności od wybranej metody połączenia z internetem. Jeśli korzystasz z kart SIM, poproś operatora o APN. 
- antena dachowa, jeśli chcesz uzyskać lepszy zasięg. 
- [Subskrypcja Starlink](https://www.starlink.com/roam), jeśli podróżujesz do obszarów bez zasięgu sieci komórkowej. 

---

## 1. Zainstaluj Spitz AX i pozostałe wyposażenie

Przed rozpoczęciem podróży skonfiguruj Spitz AX, wykonując poniższe kroki.

### Krok 1: Wybierz miejsce dla Spitz AX 

Zalecamy wybrać centralne, nieosłonięte miejsce, aby uzyskać maksymalny zasięg. Upewnij się, że wybrane miejsce znajduje się w odległości do 1 metra od źródła zasilania, ponieważ taka jest długość przewodu zasilacza. 

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Spitz AX możesz postawić na płaskiej powierzchni albo zamontować na ścianie. Jeśli wybierzesz montaż na ścianie, wykonaj kolejny krok. 

### (Opcjonalnie) Krok 2: Zamontuj Spitz AX na ścianie 

Istnieją dwa sposoby montażu Spitz AX na ścianie:
- użycie dołączonej podkładki samoprzylepnej
- użycie uchwytów ściennych

Uchwyty ścienne znajdują się w zestawie. Aby zamontować Spitz AX na ścianie, wykonaj poniższe kroki:

1. Przymocuj uchwyt do ściany za pomocą śrub.
2. Zatrzaśnij Spitz AX na uchwycie. 

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Opcjonalnie) Krok 3: Zainstaluj dachową antenę do pojazdu rekreacyjnego

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Aby uzyskać lepszy sygnał, użyj anteny dachowej do Spitz AX. Zalecamy [wielopasmową antenę MobileMark LTMG942](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/), która zapewnia optymalny sygnał sieciowy. Jeśli chcesz używać anten dachowych innych marek, upewnij się, że spełniają następujące wymagania: 

- 4 anteny komórkowe, zakres odbieranych częstotliwości 600M~6GHz.
- 2 anteny Wi-Fi, zakres odbieranych częstotliwości: 2.4G~2.5GHz, 5.15~5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Uwaga:** Możesz użyć anteny 7-w-1 (zawierającej antenę GPS), ale do Spitz AX trzeba podłączyć tylko sześć anten. Interfejs DIV/GNSS w Spitz AX obsługuje sygnały GPS, ponieważ antena komórkowa (o zakresie odbieranych częstotliwości 600M~6GHz) obejmuje częstotliwość GPS. Spitz AX obsługuje wyświetlanie lokalizacji GPS za pomocą wiersza poleceń, ale obecnie nie obsługuje pokazywania lokalizacji na mapie.

Aby uniknąć tłumienia sygnału, kabel radiowy łączący antenę dachową ze Spitz AX nie powinien przekraczać 5 metrów. (Na przykład gdy kabel radiowy MobileMark ma długość 5 metrów, odbiór sygnału przy 3000MHz spada o 3dB, czyli do połowy mocy. Im wyższa częstotliwość sygnału, tym większe tłumienie).

[Dowiedz się, jak wymienić anteny w Spitz AX.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/) 

---

## 2. Skonfiguruj internet dla Spitz AX 

Aby mieć dostęp do internetu podczas podróży, skonfiguruj połączenie internetowe z użyciem kart SIM. 

Spitz AX ma wbudowany moduł 5GNR i obsługuje dwie karty SIM. Różni operatorzy sieci komórkowych oferują różne pakiety danych dla kart SIM i korzystają z różnych APN. Trzeba wpisać APN w ustawieniach, dlatego potwierdź u operatora, jaki APN należy wprowadzić. 

Aby skonfigurować karty SIM, wykonaj poniższe kroki: 

1. Włóż kartę SIM / karty SIM. 
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Podłącz zasilacz i włącz router. 

Aby wprowadzić APN, wykonaj poniższe kroki: 

1. Wpisz `192.168.8.1` w przeglądarce internetowej i zaloguj się. 
2. W lewym górnym rogu powinieneś zobaczyć nazwę operatora. Kliknij **Manual Setup**.
3. Obok **APN** wpisz APN. 
4. Kliknij **Apply**. 

Jeśli korzystasz z dwóch kart SIM, pamiętaj, że w danym momencie działa tylko jedna karta SIM. Za każdym razem możesz ręcznie wybrać, której karty SIM chcesz używać. Możesz też włączyć funkcję [Auto Switch](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models). Jeśli router wykryje, że jedna z kart SIM nie ma prawidłowego dostępu do internetu, automatycznie przełączy się na drugą kartę SIM. Przełączenie trwa około 1 minuty. 

---

## 3. Używaj Spitz AX w różnych scenariuszach

### W trasie

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Podczas jazdy powinieneś mieć możliwość połączenia z internetem za pomocą kart SIM skonfigurowanych w poprzednim kroku.

### Na kempingu

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Jeśli podczas podróży zatrzymasz się na kempingu, możesz skorzystać z publicznej sieci Wi-Fi udostępnianej na miejscu i oszczędzać dane komórkowe. [Dowiedz się, jak połączyć się z istniejącą siecią Wi-Fi.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/) 

Po jednorazowym połączeniu z siecią Wi-Fi Spitz AX zapamięta nazwę sieci i hasło. Następnym razem, gdy znajdziesz się w pobliżu, połączy się z nią automatycznie.

### W obszarach bez zasięgu sieci komórkowej

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Jeśli zamierzasz pojechać do obszaru bez zasięgu sieci komórkowej (np. słabo zaludnionego obszaru pustynnego), użyj Starlink, czyli satelitarnej usługi internetowej. W ten sposób w miejscach z dobrym zasięgiem sieci komórkowej będziesz korzystać z sygnału 5G odbieranego przez Spitz AX, a w miejscach bez zasięgu przełączysz się na Starlink.

Podczas ustawiania anteny Starlink upewnij się, że nic jej nie zasłania. Przeszkody po obu stronach drogi (np. drzewa) wpływają na odbiór, dlatego staraj się parkować z dala od wszelkich przeszkód. 

---

## 4. Ustaw priorytety przełączenia awaryjnego 
Spitz AX obsługuje multi-WAN (przełączenie awaryjne i równoważenie obciążenia). Możesz ustawić priorytety przełączenia awaryjnego dla różnych sieci zależnie od swojego scenariusza. 

| Scenariusz| Priorytet |
| --------| ------- |
| Na kempingu (połączenie z jego siecią Wi-Fi przez repeater)    | <p> Ustaw repeater z wyższym priorytetem niż sieć komórkową.</p> <p>Gdy tylko opuścisz kemping, router automatycznie przełączy się na sieć komórkową.</p>|
| Starlink (ethernet) + sieć komórkowa | Ustaw sieć komórkową z wyższym priorytetem niż ethernet. <p>W obszarach z zasięgiem sieci komórkowej router będzie korzystał z sieci komórkowej.</p> <p>Gdy dotrzesz do obszarów bez zasięgu sieci komórkowej, router automatycznie przełączy się na Starlink przez ethernet.</p>|

Aby skonfigurować przełączenie awaryjne, przeczytaj sekcję [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
