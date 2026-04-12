# SQM (Smart Queue Management)

SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, minimalizując opóźnienia i efekt „bufferbloat", zapewniając płynniejsze działanie gier i połączeń głosowych.

**Uwaga**:

1. Ta funkcja jest obecnie dostępna wyłącznie na **GL-MT5000 (Brume 3)**.
    
2. Funkcja ta wpływa na ruch przechodzący przez router działający jako brama (w tym ruch lokalnych klientów oraz ruch klientów VPN), ale nie na ruch przychodzący, gdy router działa jako serwer VPN.

3. Ponieważ SQM wymaga dużych zasobów, najlepiej sprawdza się w sieciach o niskiej przepustowości lub dużym obciążeniu. Włączenie go na szybkich łączach może obniżyć maksymalną przepustowość.

---

W lewym panelu bocznym panelu administracyjnego przejdź do **FLOW CONTROL** > **SQM**. 

Najpierw ustaw maksymalne prędkości przesyłania i pobierania (zakres: 1–10000) na potrzeby planowania ruchu. Dopasuj je do rzeczywistej przepustowości łącza internetowego, aby uzyskać najlepsze wyniki.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Dla reguły kolejkowania (Queue Rule) dostępne są dwie opcje:

- **cake**: Inteligentne, automatyczne kształtowanie ruchu z doskonałą kontrolą opóźnień (zalecane).

- **fq_codel**: Proste, wydajne kolejkowanie uczciwe z podstawową redukcją opóźnień.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.