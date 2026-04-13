# DPI Engine

DPI (Deep Packet Inspection) to podstawowa technologia inteligentnego zarządzania siecią. W przeciwieństwie do tradycyjnych routerów, które identyfikują tylko adresy źródłowe i docelowe, DPI analizuje ładunek pakietów i precyzyjnie rozpoznaje aplikacje oraz strony internetowe dzięki bibliotece dopasowywania sygnatur, co umożliwia szczegółową klasyfikację i kontrolę ruchu.

GL.iNet DPI Engine działa lokalnie na routerze, zapewniając inteligentne zarządzanie siecią z pełnym poszanowaniem prywatności. Umożliwia pełny dostęp do statystyk danych, filtra treści i QoS, zapewniając kompleksową kontrolę ruchu.

Zintegrowany z [Netify](https://www.netify.ai/){target="_blank"}, GL.iNet DPI wykorzystuje lekką osadzoną wtyczkę do wydajnego wdrożenia. Dzięki internetowo aktualizowanej bazie sygnatur Netify umożliwia niezawodne zarządzanie, dzięki czemu kontrola sieci jest dokładniejsza i bardziej efektywna.

**Uwaga**:

1. Funkcje DPI nie działają, gdy router pracuje w trybie Drop-in Gateway.

2. Po włączeniu DPI funkcja Network Acceleration zostanie automatycznie wyłączona, aby zapewnić stabilne działanie.

## Obsługiwane modele

!!! note "Obsługiwane modele"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Szybka konfiguracja

W lewym panelu webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **DPI Engine** i kliknij **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

W wyskakującym oknie przeczytaj i zaakceptuj **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Poczekaj, aż router wykona operacje systemowe. Wyłączy wtedy funkcję Network Acceleration oraz włączy Data Statistics i Content Filter.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Po aktywacji kliknij **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Zostaniesz przeniesiony do **DPI Engine Version Center**, gdzie możesz sprawdzić wersję programu DPI oraz wersję bazy danych.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Uwaga**: Ta strona wyświetla wyłącznie podstawowe wskaźniki stanu systemu. Przetwarzanie ruchu rozpocznie się po włączeniu odpowiednich funkcji.

## Aktualizacja bazy danych

Jeśli dostępna jest nowsza wersja bazy danych, kliknij **Upgrade**, aby ją zaktualizować.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
