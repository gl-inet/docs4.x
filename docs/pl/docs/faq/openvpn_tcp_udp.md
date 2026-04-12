# OpenVPN, TCP czy UDP

Serwer OpenVPN w routerze GL.iNet obsługuje zarówno protokół TCP, jak i UDP. Jaka jest między nimi różnica?

TCP jest bardziej niezawodny, ale wolniejszy. UDP jest szybszy, ale mniej niezawodny.

Jeśli aplikacja wymaga niskich opóźnień i ciągłej transmisji danych, lepszym wyborem będzie UDP. W przeciwnym razie TCP sprawdzi się jako niezawodny protokół do przesyłania danych bez strat w trakcie transmisji.

UDP lepiej sprawdza się w grach, streamingu i usługach VoIP. TCP lepiej nadaje się do poczty e-mail, przeglądania stron internetowych i transferu plików.

Zalecamy najpierw wypróbować protokół UDP, a na TCP przełączyć się dopiero wtedy, gdy występuje niestabilność połączenia, utrata pakietów lub inne problemy związane z niezawodnością.

---

Masz dodatkowe pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
