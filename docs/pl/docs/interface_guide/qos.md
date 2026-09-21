# QoS (Quality of Service)

**Uwaga**: Ta funkcja została wprowadzona w oprogramowaniu sprzętowym v4.9. Niektóre modele, takie jak Mango 2 (GL-MG1300), nie obsługują QoS ze względu na niewystarczającą ilość pamięci, nawet jeśli działa oprogramowanie sprzętowe w wersji 4.9 lub nowszej.

---

Po lewej stronie panelu administracyjnego przejdź do **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) optymalizuje alokację przepustowości, nadając priorytet krytycznym działaniom (np. rozmowy wideo i gry) podczas przeciążenia sieci, redukując opóźnienia i poprawiając ogólną wydajność sieci.

**Uwaga**:

1. Ta funkcja wpływa tylko na ruch przechodzący przez router, gdy działa on jako brama, w tym na ruch klientów lokalnych i ruch klientów VPN. Nie dotyczy to ruchu przychodzącego, gdy router pełni funkcję serwera VPN.
2. Funkcja QoS nie będzie działać, gdy router znajduje się w trybie bramy typu Drop-in.
3. Nie można jednocześnie włączyć funkcji QoS i SQM.
4. Funkcja QoS nie działa z przyspieszeniem sieci. Włączenie QoS automatycznie wyłączy przyspieszenie sieci, aby zapewnić stabilną wydajność.

## Dla oprogramowania sprzętowego w wersji 4.11 i nowszych

Przełącz przełącznik, aby włączyć funkcję QoS, a następnie zakończ konfigurację, wykonując poniższe czynności.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Wprowadź ręcznie prędkość wysyłania i pobierania danych (zakres: 1–10000) w sieci WAN lub kliknij **Run Speedtest**, aby je zmierzyć i automatycznie wypełnić pola. Do uruchomienia testu prędkości wymagane jest aktywne połączenie internetowe.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Uwaga**: Wartości wprowadzone w polu wejściowym znajdują się w **Mbps** (megabity na sekundę). Odpowiednik **MB/s** (megabajty na sekundę) jest wyświetlany w celach informacyjnych.

2. **Scheduling Policy**

    Możesz wybrać jeden tryb zasad. Reguły zaawansowane zastępują podstawowe zasady dotyczące dopasowanego ruchu.

    - **Device Priority**

        W tym trybie wybrani klienci lokalni otrzymują wyższy priorytet sieci, gdy połączenie WAN jest przeciążone. Kliknij **Add Device** i wybierz urządzenia, aby uzyskać priorytet przepustowości podczas dużego obciążenia sieci WAN.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Możesz wyszukiwać urządzenia według nazwy klienta, adresu MAC lub adresu IP. Wybierz urządzenia docelowe i kliknij **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        W tym trybie możesz ustawić priorytety dla różnych aplikacji. Router odpowiednio przydzieli przepustowość.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Aby dostosować priorytet aplikacji, wybierz **Customize** i kliknij **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        W wyskakującym oknie wszystkie kategorie mają domyślnie ustawiony średni priorytet.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Przeciągnij kategorie, aby w razie potrzeby dostosować ich priorytet, a następnie kliknij **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        W tym trybie możesz tworzyć zaawansowane reguły QoS dla ruchu o wysokim priorytecie. Kliknij **Add Rule**, aby zdefiniować reguły w oparciu o protokół, port i źródłowy adres IP.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Określ nazwę, protokół, adres źródłowy i port docelowy, a następnie kliknij **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Dla oprogramowania sprzętowego v4.9 do v4.10

Przełącz przełącznik, aby włączyć QoS, a strona wyświetli się w następujący sposób.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Ustaw maksymalną prędkość wysyłania i pobierania (zakres: 1–10000) w celu planowania ruchu. Aby uzyskać najlepsze rezultaty, dopasuj je do rzeczywistej przepustowości Internetu.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Uwaga**: Wartości wprowadzone w polu wejściowym znajdują się w **Mbps** (megabity na sekundę). Odpowiednik **MB/s** (megabajty na sekundę) jest wyświetlany w celach informacyjnych.

Następnie ustaw priorytety dla różnych aplikacji. Router odpowiednio przydzieli przepustowość.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Aby dostosować priorytet aplikacji, wybierz **Customize** i kliknij **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

W wyskakującym oknie wszystkie kategorie mają domyślnie ustawiony średni priorytet.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Przeciągnij kategorie, aby w razie potrzeby dostosować ich priorytet, a następnie kliknij **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Nadal masz pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
