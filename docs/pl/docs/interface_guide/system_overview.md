# Przegląd systemu

W lewym panelu bocznym panelu administracyjnego przejdź do **SYSTEM** -> **Overview**.

Strona **Overview** wyświetla stan wybranych elementów sprzętowych i udostępnia podstawowe funkcje sterowania, w tym:

- Stan procesora (CPU), pamięci (Memory), pamięci flash (Flash) oraz zewnętrznych nośników pamięci.
- Stan elementów sprzętowych, takich jak wentylator (Fan) i bateria (Battery).
- Sterowanie diodami LED i wentylatorem.
- Informacje o urządzeniu.

Poniżej znajduje się przykład dla modelu GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## Średnie obciążenie procesora (CPU)

W większości modeli bez wentylatora średnie obciążenie procesora jest wyświetlane jak poniżej.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

W niektórych modelach z wbudowanym wentylatorem średnie obciążenie procesora jest wyświetlane jak poniżej.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Najedź kursorem na wykres, aby wyświetlić szczegółowe wartości.

Kliknij wartość temperatury po prawej stronie, aby przełączyć między stopniami Celsjusza i Fahrenheita.

Kliknij ikonę wentylatora w prawym górnym rogu, aby przejść do **Fan Settings**.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Modele z wbudowanym wentylatorem"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Użycie pamięci

Najedź kursorem na wykres, aby wyświetlić szczegółowe wartości.

**Uwaga**: Wyświetlana tutaj pamięć to pamięć dostępna dla systemu Linux. Jej łączna wartość będzie mniejsza niż fizyczna pamięć urządzenia, ponieważ część jest przydzielona do podsystemu Wi‑Fi i innych obszarów rozruchowych.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Kliknij ikonę koła zębatego, aby przejść do sekcji [Zaplanowane zadania](scheduled_tasks.md) dla diody LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

Wyświetla całkowitą pamięć flash, w tym przestrzeń zajętą przez system (System), aplikacje (Apps) oraz pozostałą dostępną przestrzeń (Available).

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Informacje o urządzeniu

Ta sekcja wyświetla podstawowe informacje o urządzeniu.

Identyfikator urządzenia (Device ID), adres MAC urządzenia oraz numer seryjny (S/N) zostały dodane w firmware v4.7 i nowszym.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Pamięć zewnętrzna

Ta sekcja, dostępna od wersji v4.5, wyświetla całkowitą i dostępną pojemność dysku USB.

Niektóre modele z firmware v4.7 i nowszym obsługują przełączanie protokołu USB.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
