# Statystyki danych

Statystyki danych udostępniają inteligentny panel analizy ruchu, który kategoryzuje i wizualizuje użycie sieci według aplikacji. Pomaga to monitorować ruch w czasie rzeczywistym i historyczny, zapewniając lepszą widoczność i kontrolę nad siecią.

**Uwaga**:

1. Ta funkcja jest obecnie dostępna tylko na **GL-MT5000 (Brume 3)**.

2. Ta funkcja nie działa z Network Acceleration. Jej włączenie automatycznie wyłączy Network Acceleration, aby zapewnić prawidłowe działanie.

---

## Szybka konfiguracja

Po lewej stronie panelu administracyjnego WWW przejdź do **FLOW CONTROL** > **Data Statistics**.

Włącz przełącznik w prawym górnym rogu, aby wyświetlić **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: Ta sekcja przedstawia wykres trendu w czasie (np. z ostatniego dnia), pokazujący zużycie pasma przez 10 najważniejszych aplikacji w wybranym okresie.

    W razie potrzeby przełącz oś czasu między Past Hour, Past Day i Past Week.

- **App Traffic Statistics**: Ta sekcja wyświetla szczegółowe statystyki ruchu dla każdej aplikacji, w tym dane Download, Upload i Total Bandwidth.

    W razie potrzeby wyszukaj konkretne aplikacje za pomocą paska wyszukiwania.

## Zasady przechowywania danych

1. Statystyki ruchu są zapisywane w RAM co 15 sekund i w pamięci flash co 1 godzinę. Częstych zapisów do pamięci flash unika się, aby chronić jej żywotność.

2. Miękki restart nie powoduje utraty danych. Przed ponownym uruchomieniem system najpierw zapisuje dane z RAM do pamięci flash.

3. Twardy restart (odłączenie i ponowne podłączenie zasilania) lub aktualizacja firmware z zachowaniem ustawień mogą spowodować utratę danych z maksymalnie ostatniej godziny.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
