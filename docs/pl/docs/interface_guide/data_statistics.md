# Statystyki danych

**Uwaga**: Ta funkcja została wprowadzona w firmware v4.9.

Niektóre modele, takie jak Mango 2 (GL-MG1300), nie obsługują Data Statistics ze względu na zbyt małą ilość pamięci, nawet z firmware v4.9 lub nowszym. Szczegółowe informacje znajdują się w sekcji [Obsługiwane modele](#supported-models).

---

Po lewej stronie panelu administracyjnego przejdź do **FLOW CONTROL** -> **Data Statistics**.

Data Statistics zapewnia intuicyjny pulpit nawigacyjny ruchu, który identyfikuje wykorzystanie sieci według aplikacji i protokołu. Obsługuje przeglądanie trendów historycznych z okresu 1 godziny, 1 dnia i 7 dni, wyświetla rankingi użytkowania, monitoruje ruch na urządzeniu i umożliwia blokowanie niechcianych aplikacji jednym kliknięciem.

**Uwaga**:

1. Statystyki danych nie będą uwzględniane, gdy router znajduje się w trybie bramy typu Drop-in.
2. Statystyki danych nie mogą działać w przypadku przyspieszenia sieci. Włączenie statystyk danych automatycznie wyłączy przyspieszenie sieci, aby zapewnić stabilną wydajność.
3. Statystyki danych śledzą jedynie wykorzystanie ruchu dla urządzeń wymienionych na stronie Klienta. Jeśli urządzenie łączy się z routerem poprzez interfejs tunelowy (np. klient VPN, Tailscale lub AstroWarp), ruch pochodzący z tego urządzenia i przekazywany przez router nie jest uwzględniony w tych statystykach.

## Obsługiwane modele {#supported-models}

??? "Obsługiwane modele"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Nieobsługiwane modele"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Dla oprogramowania sprzętowego w wersji 4.11 i nowszych

Przełącz przełącznik w prawym górnym rogu, aby wyświetlić **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Ta strona składa się z dwóch części:

- **Top 10 Apps by Bandwidth Usage**: Przedstawia oparty na czasie wykres trendów (np. za ostatni dzień) pokazujący wykorzystanie przepustowości 10 najważniejszych aplikacji w wybranym okresie.

    Najedź myszką na wykres, aby wyświetlić wykorzystanie danych przez 10 aplikacji zużywających największą przepustowość w określonym czasie.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Wyświetla szczegółowe wskaźniki ruchu dla każdej aplikacji, w tym pobieranie, przesyłanie i całkowitą przepustowość. W razie potrzeby wyszukaj określone aplikacje na pasku wyszukiwania.

    Kliknij strzałkę sortowania obok nagłówka kolumny, aby posortować listę w kolejności rosnącej lub malejącej.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Zasady przechowywania danych

1. Statystyki ruchu są zapisywane w pamięci RAM co 15 sekund i zapisywane w pamięci flash co 1 godzinę. Aby chronić żywotność pamięci flash, unika się częstych zapisów w pamięci flash.

2. Miękki restart nie spowoduje utraty danych. System najpierw zapisuje dane z pamięci RAM do pamięci flash przed ponownym uruchomieniem.

3. Twardy restart (odłączenie i ponowne podłączenie zasilania) lub aktualizacja oprogramowania sprzętowego (z zachowaniem ustawień) może spowodować utratę danych aż do ostatniej godziny.

### Selektor Klienta

Selektor klientów pozwala wybrać konkretnego klienta lub zachować domyślnych wszystkich klientów. Wykres i tabela statystyk zostaną automatycznie odświeżone, aby wyświetlić dane o ruchu tylko dla wybranego urządzenia.

**Uwaga**: Ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Przełącz widoki wykresów

W razie potrzeby możesz zmienić typ wykresu podczas przeglądania statystyk ruchu w aplikacji.

**Uwaga**: Ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: Wykres śledzi wykorzystanie przepustowości w wybranym zakresie czasu. Ciągłe krzywe pokazują, jak ruch zmienia się w czasie, dzięki czemu idealnie nadają się do wykrywania rosnących i spadających trendów użytkowania.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: Wykres porównuje wykorzystanie przepustowości przez aplikacje obok siebie. Poszczególne paski wyraźnie pokazują, które aplikacje zużywają więcej przepustowości, na pierwszy rzut oka.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: Wykres przedstawia całkowite wykorzystanie przepustowości w procentach. Wycinki wizualizują względną część ruchu wykorzystywanego przez każdą aplikację.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Przełącz zakres czasu

W razie potrzeby możesz przełączać zakres czasu między ostatnią godziną, ostatnim dniem i ostatnim tygodniem.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

Wybrany zakres czasu określa sposób wyświetlania danych:

- **For a closer look (np. Ostatnia godzina)**: Wykres pokazuje szczegółowe wahania w czasie rzeczywistym. Szczyty są wyższe, a spadki bardziej strome, co ułatwia wykrycie nagłych skoków wykorzystania przepustowości.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **For a broad overview (np. Ostatni dzień lub Ostatni tydzień)**: Wykres łączy dane w dłuższą oś czasu. Krzywe stają się gładsze, pokazując ogólny trend w ruchu, a nie każdą małą zmianę.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Wyczyść statystyki

Kliknij ikonę miotły w lewym górnym rogu, aby w razie potrzeby wyczyścić statystyki.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Po wyczyszczeniu strona zostanie zaktualizowana, jak pokazano poniżej. Być może trzeba będzie chwilę poczekać, aż nowe statystyki zaczną się ładować.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Dla oprogramowania sprzętowego v4.9 do v4.10

Przełącz przełącznik w prawym górnym rogu, aby wyświetlić **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Ta strona składa się z dwóch części:

- **Top 10 Apps by Bandwidth Usage**: Przedstawia oparty na czasie wykres trendów (np. za ostatni dzień) pokazujący wykorzystanie przepustowości 10 najważniejszych aplikacji w wybranym okresie.

    Najedź myszką na wykres, aby wyświetlić wykorzystanie danych przez 10 aplikacji zużywających największą przepustowość w określonym czasie.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Wyświetla szczegółowe wskaźniki ruchu dla każdej aplikacji, w tym pobieranie, wysyłanie i całkowitą przepustowość. W razie potrzeby wyszukaj określone aplikacje na pasku wyszukiwania.

    Kliknij strzałkę sortowania obok nagłówka kolumny, aby posortować listę w kolejności rosnącej lub malejącej.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Zasady przechowywania danych

1. Statystyki ruchu są zapisywane w pamięci RAM co 15 sekund i zapisywane w pamięci flash co 1 godzinę. Aby chronić żywotność pamięci flash, unika się częstych zapisów w pamięci flash.

2. Miękki restart nie spowoduje utraty danych. System najpierw zapisuje dane z pamięci RAM do pamięci flash przed ponownym uruchomieniem.

3. Twardy restart (odłączenie i ponowne podłączenie zasilania) lub aktualizacja oprogramowania sprzętowego (z zachowaniem ustawień) może spowodować utratę danych aż do ostatniej godziny.

### Przełącz zakres czasu

W razie potrzeby możesz przełączać zakres czasu między ostatnią godziną, ostatnim dniem i ostatnim tygodniem.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

Wybrany zakres czasu określa sposób wyświetlania danych:

- **For a closer look (np. Ostatnia godzina)**: Wykres pokazuje szczegółowe wahania w czasie rzeczywistym. Szczyty są wyższe, a spadki bardziej strome, co ułatwia wykrycie nagłych skoków wykorzystania przepustowości.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **For a broad overview (np. Ostatni dzień lub Ostatni tydzień)**: Wykres łączy dane w dłuższą oś czasu. Krzywe stają się gładsze, pokazując ogólny trend w ruchu, a nie każdą małą zmianę.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Wyczyść statystyki

Kliknij ikonę miotły w lewym górnym rogu, aby w razie potrzeby wyczyścić statystyki.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Po wyczyszczeniu strona zostanie zaktualizowana, jak pokazano poniżej. Być może trzeba będzie chwilę poczekać, aż nowe statystyki zaczną się ładować.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Nadal masz pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
