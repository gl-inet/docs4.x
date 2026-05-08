# QoS (Quality of Service)

QoS (Quality of Service) optymalizuje przydział przepustowości, nadając priorytet krytycznym działaniom (np. wideorozmowom, grom) podczas przeciążenia sieci, co zmniejsza opóźnienia i poprawia ogólną wydajność sieci.

**Uwaga**:

1. Ta funkcja wpływa tylko na ruch przechodzący przez router, gdy działa on jako brama, w tym ruch lokalnych klientów i ruch klienta VPN. Nie dotyczy ruchu przychodzącego, gdy router działa jako serwer VPN.
2. QoS nie działa, gdy router pracuje w trybie Drop-in Gateway.
3. QoS i SQM nie mogą być włączone jednocześnie.
4. QoS nie współpracuje z funkcją Network Acceleration. Włączenie QoS automatycznie wyłączy Network Acceleration, aby zapewnić stabilną wydajność.

## Obsługiwane modele

!!! note "Obsługiwane modele"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Uwaga: modele oznaczone symbolem ※ obsługują QoS od firmware v4.9.

## Szybka konfiguracja

W lewym panelu webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **QoS**.

Włącz przełącznik, aby aktywować QoS. Strona będzie wyglądać jak poniżej.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Ustaw maksymalną prędkość wysyłania i pobierania (zakres wejściowy: 1–10000) na potrzeby planowania ruchu. Aby uzyskać najlepsze wyniki, dopasuj je do rzeczywistej przepustowości łącza internetowego.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Uwaga**: Wartości wprowadzone w polu wejściowym są podawane w **Mbps** (megabitach na sekundę). Dla ułatwienia wyświetlana jest także równowartość w **MB/s** (megabajtach na sekundę).

Następnie ustaw priorytety dla różnych aplikacji. Router odpowiednio przydzieli przepustowość.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## Dostosowywanie priorytetu aplikacji

Aby dostosować priorytet aplikacji, wybierz **Customize** i kliknij **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

W wyskakującym oknie wszystkie kategorie mają domyślnie ustawiony średni priorytet.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Przeciągnij kategorie, aby ustawić potrzebny priorytet, a następnie kliknij **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
