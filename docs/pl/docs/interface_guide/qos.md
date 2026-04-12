# QoS (Quality of Service)

QoS (Quality of Service) optymalizuje alokację przepustowości, nadając priorytet krytycznym działaniom (np. rozmowom wideo, grom) podczas przeciążenia sieci, zmniejszając opóźnienia i poprawiając ogólną wydajność sieci.

**Uwaga**: 

1. Ta funkcja jest obecnie dostępna wyłącznie na **GL-MT5000 (Brume 3)**.

2. Funkcja ta wpływa na ruch przechodzący przez router działający jako brama (w tym ruch lokalnych klientów oraz ruch klientów VPN), ale nie na ruch przychodzący, gdy router działa jako serwer VPN.

---

W lewym panelu bocznym panelu administracyjnego przejdź do **FLOW CONTROL** > **QoS**. 

Najpierw ustaw maksymalne prędkości przesyłania i pobierania (zakres: 1–10000) na potrzeby planowania ruchu. Dopasuj je do rzeczywistej przepustowości łącza internetowego, aby uzyskać najlepsze wyniki.

Następnie ustaw priorytety dla różnych aplikacji – router przydzieli im przepustowość odpowiednio.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.