# SQM (Smart Queue Management)

SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i efekt „bufferbloat”, zapewniając płynniejsze granie i rozmowy głosowe.

**Uwaga**:

1. Ta funkcja wpływa tylko na ruch przechodzący przez router, gdy działa on jako brama, w tym ruch lokalnych klientów i ruch klienta VPN. Nie dotyczy ruchu przychodzącego, gdy router działa jako serwer VPN.

2. Ponieważ SQM wymaga sporych zasobów, najlepiej sprawdza się w sieciach o niskiej przepustowości lub dużym obciążeniu. Włączenie go na szybkich łączach może obniżyć maksymalną przepustowość.

3. SQM nie działa, gdy router pracuje w trybie Drop-in Gateway.

4. SQM i QoS nie mogą być włączone jednocześnie.

5. SQM nie współpracuje z funkcją Network Acceleration. Włączenie SQM automatycznie wyłączy Network Acceleration, aby zapewnić stabilną wydajność.

## Obsługiwane modele

!!! note "Obsługiwane modele"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Uwaga: modele oznaczone symbolem ※ obsługują SQM od firmware v4.9.

## Szybka konfiguracja

W lewym panelu webowego panelu administracyjnego przejdź do **FLOW CONTROL** -> **SQM**.

Włącz przełącznik, aby aktywować SQM, a następnie ustaw maksymalną prędkość wysyłania i pobierania (zakres wejściowy: 1–10000) na potrzeby planowania ruchu. Aby uzyskać najlepsze wyniki, dopasuj je do rzeczywistej przepustowości łącza internetowego.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Uwaga**: Wartości wprowadzone w polu wejściowym są podawane w **Mbps** (megabitach na sekundę). Dla ułatwienia wyświetlana jest także równowartość w **MB/s** (megabajtach na sekundę).

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Dla **Queue Rule** dostępne są dwie opcje:

- **cake**: inteligentne, automatyczne kształtowanie ruchu z bardzo dobrą kontrolą opóźnień (zalecane).

- **fq_codel**: proste i wydajne sprawiedliwe kolejkowanie z podstawową redukcją opóźnień.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
