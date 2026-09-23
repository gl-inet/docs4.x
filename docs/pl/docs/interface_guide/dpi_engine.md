# DPI Engine

**Uwaga**: Ta funkcja została wprowadzona w firmware v4.9.

Niektóre modele, takie jak Mango 2 (GL-MG1300), nie obsługują DPI Engine ze względu na zbyt małą ilość pamięci, nawet z firmware v4.9 lub nowszym. Szczegółowe informacje znajdują się w sekcji [Obsługiwane modele](#supported-models).

---

DPI (Deep Packet Inspection) to podstawowa technologia inteligentnego zarządzania siecią. W przeciwieństwie do tradycyjnych routerów, które identyfikują tylko adresy źródłowe i docelowe, DPI analizuje ładunek pakietów i precyzyjnie rozpoznaje aplikacje oraz strony internetowe dzięki bibliotece dopasowywania sygnatur, co umożliwia szczegółową klasyfikację i kontrolę ruchu.

GL.iNet DPI Engine działa lokalnie na routerze, zapewniając inteligentne zarządzanie siecią z pełnym poszanowaniem prywatności. Umożliwia pełny dostęp do statystyk danych, filtra treści i QoS, zapewniając kompleksową kontrolę ruchu.

Zintegrowany z [Netify](https://www.netify.ai/){target="_blank"}, GL.iNet DPI wykorzystuje lekką osadzoną wtyczkę do wydajnego wdrożenia. Dzięki internetowo aktualizowanej bazie sygnatur Netify umożliwia niezawodne zarządzanie, dzięki czemu kontrola sieci jest dokładniejsza i bardziej efektywna.

**Uwaga**:

1. Gdy router pracuje w trybie Drop-in Gateway, funkcje DPI (w tym Data Statistics, Content Filter i QoS) oraz SQM nie działają.

2. Po włączeniu DPI funkcja Network Acceleration zostanie automatycznie wyłączona, aby zapewnić stabilną wydajność.

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
