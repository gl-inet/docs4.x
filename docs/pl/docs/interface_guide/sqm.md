# SQM (Smart Queue Management)

**Uwaga**: Ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.9. Niektóre modele, takie jak Mango 2 (GL-MG1300), nie obsługują SQM z powodu niewystarczającej ilości pamięci, nawet jeśli działa oprogramowanie sprzętowe w wersji 4.9 lub nowszej.

Po lewej stronie panelu administracyjnego przejdź do **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „przepełnienie bufora”, zapewniając płynniejszą grę i połączenia głosowe.

**Uwaga**:

1. Ta funkcja wpływa tylko na ruch przechodzący przez router, gdy działa on jako brama, w tym na ruch klientów lokalnych i ruch klientów VPN. Nie dotyczy to ruchu przychodzącego, gdy router pełni funkcję serwera VPN.
2. Ponieważ SQM wymaga dużej ilości zasobów, działa najlepiej w przypadku sieci o niskiej przepustowości lub przeciążonych. Włączenie tej opcji na szybkich połączeniach może zmniejszyć szczytową przepustowość.
3. SQM nie będzie działać, gdy router znajduje się w trybie bramy typu Drop-in.
4. Nie można jednocześnie włączyć funkcji SQM i QoS.
5. SQM nie może współpracować z akceleracją sieci. Włączenie SQM automatycznie wyłączy przyspieszenie sieci, aby zapewnić stabilną wydajność.

## Dla oprogramowania sprzętowego w wersji 4.11 i nowszych

Przełącz przełącznik, aby włączyć SQM, a następnie zakończ konfigurację, wykonując poniższe czynności.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Wprowadź ręcznie prędkość wysyłania i pobierania danych (zakres: 1–10000) w sieci WAN lub kliknij **Run Speedtest**, aby je zmierzyć i automatycznie wypełnić pola. Do uruchomienia testu prędkości wymagane jest aktywne połączenie internetowe.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Uwaga**: Wartości wprowadzone w polu wejściowym znajdują się w **Mbps** (megabity na sekundę). Odpowiednik **MB/s** (megabajty na sekundę) jest wyświetlany w celach informacyjnych.

2. **Queue Discipline**

    Wybierz regułę kolejkowania, aby zarządzać ruchem i zmniejszać opóźnienia pod obciążeniem.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: Inteligentne, automatyczne kształtowanie ruchu z doskonałą ogólną kontrolą opóźnień. (zalecane).

        Jeśli jako dyscyplinę kolejki wybrano **cake**, **Cake Autorate** jest dostępny jako funkcja opcjonalna.

        Cake Autorate to narzędzie kształtujące oparte na opóźnieniach, które zmniejsza lub zwiększa przepustowość CAKE w czasie rzeczywistym w oparciu o sondę RTT. Nie są przeprowadzane żadne aktywne testy prędkości; używane są tylko lekkie pingi. Zalecane w przypadku wahań przepustowości sieci WAN; nie potrzebne na stabilnych łączach.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Uwaga**: Cake Autorate generuje ciągły ruch sondujący w tle. Należy wziąć pod uwagę dodatkowe użycie danych w przypadku korzystania z połączenia taryfowego.

        Ustawienia domyślne są odpowiednie dla większości połączeń. Zmieniaj poniższe parametry tylko wtedy, gdy rozumiesz, jak wpływają one na Autoryzację Ciasto. W razie potrzeby kliknij **Reset to Default**, aby przywrócić domyślne ustawienia sondy i progu.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: Lista adresów IP oddzielonych przecinkami, używana do sprawdzania jakości sieci.

        - **Probe Interval**: Krótsze interwały umożliwiają szybszą reakcję, ale zużywają więcej zasobów procesora.

        - **Concurrent Probes**: Liczba jednoczesnych sond nie może przekraczać liczby serwerów sondujących; wyższe wartości zwiększają obciążenie procesora.

        - **Idle Detection Threshold**: Gdy szybkość transmisji spadnie poniżej tej wartości, połączenie zostanie uznane za bezczynne. Wartość ta nie może przekraczać 25% skonfigurowanego ograniczenia prędkości.

        - **Download Latency Threshold**: Gdy opóźnienie pobierania przekracza ten próg, wyzwalane jest zmniejszanie przepustowości.

        - **Upload Latency Threshold**: Gdy opóźnienie przesyłania przekracza ten próg, wyzwalane jest zmniejszanie przepustowości.

    - **fq_codel**: Proste, wydajne, uczciwe kolejkowanie z podstawową redukcją opóźnień.

## Dla oprogramowania sprzętowego v4.9 do v4.10

Przełącz przełącznik, aby włączyć SQM i ustawić maksymalną prędkość wysyłania i pobierania (zakres: 1–10000) na potrzeby planowania ruchu. Aby uzyskać najlepsze rezultaty, dopasuj je do rzeczywistej przepustowości Internetu.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Uwaga**: Wartości wprowadzone w polu wejściowym znajdują się w **Mbps** (megabity na sekundę). Odpowiednik **MB/s** (megabajty na sekundę) jest wyświetlany w celach informacyjnych.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

W przypadku reguły kolejki dostępne są dwie opcje:

- **cake**: Inteligentne, automatyczne kształtowanie ruchu z doskonałą ogólną kontrolą opóźnień (zalecane).

- **fq_codel**: Proste, wydajne, uczciwe kolejkowanie z podstawową redukcją opóźnień.

!!! tip

    Różnica między ustawieniami QoS i SQM polega na tym, że QoS umożliwia ustawienie priorytetów aplikacji, a router odpowiednio przydziela przepustowość; podczas gdy SQM pozwala wybrać regułę kolejki.

---

Nadal masz pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
