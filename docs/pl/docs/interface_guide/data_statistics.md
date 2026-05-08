# Statystyki danych

Statystyki danych udostępniają intuicyjny panel ruchu, który identyfikuje wykorzystanie sieci według aplikacji i protokołu. Umożliwiają przegląd trendów historycznych z 1 godziny, 1 dnia i 7 dni, pokazują rankingi wykorzystania, monitorują ruch dla poszczególnych urządzeń i pozwalają jednym kliknięciem blokować niechciane aplikacje.

**Uwaga**:

1. Statystyki danych nie działają, gdy router pracuje w trybie Drop-in Gateway.
2. Statystyki danych nie współpracują z funkcją Network Acceleration. Włączenie statystyk danych automatycznie wyłączy Network Acceleration, aby zapewnić stabilną wydajność.

## Obsługiwane modele

!!! note "Obsługiwane modele"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Uwaga: modele oznaczone symbolem ※ obsługują Data Statistics od firmware v4.9.

## Szybka konfiguracja

W lewym panelu webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **Data Statistics**.

Włącz przełącznik w prawym górnym rogu, aby wyświetlić **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Ta strona składa się z dwóch części:

- **Top 10 Apps by Bandwidth Usage**: wyświetla wykres trendów w czasie (np. z ostatniego dnia), pokazujący zużycie pasma przez 10 aplikacji o największym użyciu w wybranym okresie.

    Najedź kursorem na wykres, aby sprawdzić zużycie danych przez 10 aplikacji o największym wykorzystaniu pasma w określonym momencie.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: wyświetla szczegółowe statystyki ruchu dla każdej aplikacji, w tym Download, Upload i Total Bandwidth. W razie potrzeby wyszukaj konkretne aplikacje za pomocą paska wyszukiwania.

    Kliknij strzałkę sortowania obok nagłówka kolumny, aby posortować listę rosnąco lub malejąco.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Zasady przechowywania danych

1. Statystyki ruchu są zapisywane do pamięci RAM co 15 sekund i do pamięci flash co 1 godzinę. Częste zapisy do pamięci flash są ograniczane, aby chronić jej żywotność.

2. Miękki restart nie powoduje utraty danych. System najpierw zapisuje dane z RAM do pamięci flash, a dopiero potem uruchamia się ponownie.

3. Twardy restart (odłączenie i ponowne podłączenie zasilania) lub aktualizacja firmware z zachowaniem ustawień mogą spowodować utratę danych z maksymalnie ostatniej godziny.

## Zmiana zakresu czasu

W razie potrzeby możesz przełączać zakres czasu między **Past hour**, **Past day** i **Past week**.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

Wybrany zakres czasu wpływa na sposób prezentacji danych:

- **Dla bliższego podglądu (np. Past Hour)**: wykres pokazuje bardziej szczegółowe, bieżące wahania. Szczyty są wyższe, a spadki wyraźniejsze, dzięki czemu łatwo zauważyć nagłe skoki zużycia pasma.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Dla szerszego przeglądu (np. Past Day lub Past Week)**: wykres kondensuje dane na dłuższej osi czasu. Krzywe stają się gładsze i pokazują ogólny trend ruchu zamiast każdej drobnej zmiany.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

## Czyszczenie statystyk

Kliknij ikonę miotły w lewym górnym rogu, aby w razie potrzeby wyczyścić statystyki.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Po wyczyszczeniu strona zaktualizuje się, jak pokazano poniżej. Rozpoczęcie ładowania nowych statystyk może potrwać chwilę.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
