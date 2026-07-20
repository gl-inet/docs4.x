---
title: Zrozumienie zasięgu Wi-Fi, punktów dostępowych i mocy nadawania
---

# Zrozumienie zasięgu Wi-Fi, punktów dostępowych i mocy nadawania

Wielu użytkowników zakłada, że zwiększenie mocy nadawania routera zawsze poprawia zasięg i wydajność Wi-Fi.

Chociaż wyższa moc nadawania zwykle zwiększa zasięg pojedynczego routera, maksymalna moc nadawania nie zawsze jest idealna w sieciach z wieloma punktami dostępowymi (AP), węzłami mesh lub wdrożeniami Wi-Fi klasy korporacyjnej.

Zrozumienie komórek zasięgu, roamingu, planowania kanałów i mocy nadawania może pomóc poprawić wydajność sieci bezprzewodowej.

## Pojedynczy router a wiele punktów dostępowych

### Pojedynczy router

Jeśli tylko jeden router zapewnia zasięg Wi-Fi:

- Wyższa moc nadawania zwykle zwiększa zasięg.
- Urządzenia klienckie mogą utrzymać użyteczne połączenie z większej odległości.
- Obniżenie mocy nadawania zwykle zmniejsza odbierany sygnał i stosunek sygnału do szumu (SNR) w kierunku pobierania.

Dla większości użytkowników z jednym routerem zaleca się pozostawienie mocy nadawania na ustawieniu domyślnym lub automatycznym.

Obniżenie mocy nadawania routera nie zmniejsza energii RF nadawanej przez sąsiednie sieci Wi-Fi. Ich routery i AP nadal nadają z tą samą mocą.

### Wiele punktów dostępowych

Gdy wdrażanych jest wiele AP, celem nie musi być maksymalizacja obszaru zasięgu każdego AP.

Celem jest raczej utworzenie kilku mniejszych, dobrze zdefiniowanych komórek zasięgu, które nakładają się tylko na tyle, aby zapewnić ciągły zasięg i niezawodny roaming.

Odpowiednie rozmieszczenie AP, moc nadawania i dobór kanałów są istotne.

## Nakładanie się komórek zasięgu

Jeśli każdy AP nadaje z maksymalną mocą, ich obszary zasięgu mogą nadmiernie się nakładać.

Urządzenie klienckie może pozostać połączone z odległym AP, nawet gdy bliższy AP zapewnia silniejszy sygnał. Jest to powszechnie nazywane **sticky client**.

Klient połączony z niewłaściwym AP może doświadczać:

- Niższego SNR
- Niższych szybkości modulacji i kodowania
- Większej liczby retransmisji
- Zmniejszonej przepustowości
- Zwiększonego opóźnienia

Zmniejszenie mocy nadawania AP może ograniczyć rozmiar komórek zasięgu i zachęcić urządzenia klienckie do wcześniejszego roamingu.

## Zrozumienie roamingu klientów

W większości sieci Wi-Fi to urządzenie klienckie decyduje, kiedy wykonać roaming.

Router lub AP może zapewniać wsparcie roamingu, ale telefon, laptop, tablet lub inne urządzenie klienckie zwykle podejmuje ostateczną decyzję o opuszczeniu jednego AP i połączeniu z innym.

Różne urządzenia klienckie używają różnych progów i algorytmów roamingu. Urządzenie może więc pozostać połączone z AP tak długo, jak uznaje połączenie za użyteczne, nawet jeśli inny AP oferuje silniejszy sygnał.

Zmniejszenie nadmiernego nakładania się zasięgu może pomóc klientom podejmować lepsze decyzje roamingowe.

## Ponowne wykorzystanie przestrzenne

Wi-Fi jest medium współdzielonym.

Przed nadawaniem urządzenia Wi-Fi nasłuchują, aby ustalić, czy kanał jest już używany. Jeśli AP używające tego samego kanału słyszą się nawzajem na dużym obszarze, mogą spędzać więcej czasu, czekając na dostępność kanału.

Zmniejsza to użyteczny czas antenowy i ogólną przepustowość.

Odpowiednie zmniejszenie mocy nadawania może pozwolić AP używającym tego samego kanału w różnych fizycznych obszarach działać bardziej niezależnie. Jest to znane jako **ponowne wykorzystanie przestrzenne**.

Ponowne wykorzystanie przestrzenne nie oznacza, że obniżenie mocy nadawania AP zmniejsza zakłócenia nadawane przez sąsiednie sieci. Zamiast tego prawidłowo dobrane komórki zasięgu mogą ograniczyć niepotrzebną rywalizację o kanał i umożliwić ponowne użycie tego samego kanału w wystarczająco oddalonych obszarach.

## Planowanie kanałów

Moc nadawania i dobór kanałów należy rozpatrywać razem.

### 2,4 GHz

Pasmo 2,4 GHz ma stosunkowo niewiele kanałów nienakładających się.

W wielu regionach regulacyjnych kanały 1, 6 i 11 są powszechnie używane z szerokością kanału 20 MHz.

Gdy to możliwe, pobliskie AP powinny używać różnych, nienakładających się kanałów.

### 5 GHz i 6 GHz

Pasma 5 GHz i 6 GHz zapewniają więcej dostępnych kanałów, co ułatwia przypisanie różnych kanałów pobliskim AP.

Używanie nienakładających się kanałów zmniejsza rywalizację współkanałową, chociaż nadmierne nakładanie się zasięgu nadal może wpływać na zachowanie roamingu.

Dostępne kanały zależą od modelu routera, kraju lub regionu, szerokości kanału oraz lokalnych przepisów.

## Przewodowe AP i sieci mesh

### Przewodowe punkty dostępowe

Przewodowe połączenie Ethernet między routerem głównym a dodatkowymi AP jest zazwyczaj preferowanym wdrożeniem.

Ponieważ połączenie przewodowe przenosi ruch backhaul, moc nadawania Wi-Fi można dostosować głównie pod kątem zasięgu klientów, roamingu i ponownego wykorzystania przestrzennego.

### Mesh z przewodowym backhaul

Węzły mesh używające przewodowego backhaul można optymalizować podobnie jak przewodowe AP.

Moc nadawania można dostosować, aby zmniejszyć nadmierne nakładanie się komórek przy zachowaniu ciągłego zasięgu.

### Mesh z bezprzewodowym backhaul

W bezprzewodowym wdrożeniu mesh moduły radiowe Wi-Fi mogą również przenosić ruch między węzłami mesh.

Zbyt agresywne zmniejszenie mocy nadawania może osłabić bezprzewodowe połączenie backhaul i obniżyć ogólną wydajność.

Korzystając z bezprzewodowego backhaul, upewnij się, że węzły mesh utrzymują ze sobą silne i stabilne połączenie.

## Przykładowe wdrożenie z wieloma AP

Rozważ dwa routery GL.iNet połączone przez Ethernet:

- Router główny zapewnia routing, DHCP, NAT i usługi zapory.
- Drugi router działa w trybie Access Point.
- Oba urządzenia nadają tę samą nazwę sieci Wi-Fi i te same ustawienia zabezpieczeń.
- Pobliskie AP używają różnych, nienakładających się kanałów.
- Moc nadawania jest dostosowana tak, aby komórki zasięgu nakładały się wystarczająco dla roamingu, ale nie nadmiernie.

Idealna moc nadawania zależy od materiałów budowlanych, rozmieszczenia AP, urządzeń klienckich, sąsiednich sieci Wi-Fi i pożądanego obszaru zasięgu.

Nie istnieje jedna wartość mocy nadawania odpowiednia dla każdego wdrożenia.

## Częste nieporozumienia

### Maksymalna moc nadawania zawsze zapewnia najlepsze Wi-Fi

Maksymalna moc zwykle zapewnia największy obszar zasięgu, ale we wdrożeniach z wieloma AP może powodować nadmierne nakładanie się zasięgu i słabe zachowanie roamingu.

### Niższa moc nadawania zmniejsza przychodzące zakłócenia

Obniżenie mocy nadawania AP zmniejsza sygnał generowany przez własny AP. Nie zmniejsza mocy nadawanej przez sąsiednie routery lub AP.

### Niższa moc nadawania zwiększa czułość odbiornika AP

Moc nadawania i czułość odbiornika to oddzielne cechy. Obniżenie mocy nadawania samo w sobie nie poprawia zdolności AP do odbierania transmisji od klientów.

### Urządzenia klienckie zawsze łączą się z najbliższym AP

Urządzenia klienckie zwykle wybierają AP i wykonują roaming między nimi za pomocą własnych algorytmów wewnętrznych. Mogą pozostać połączone z bardziej odległym AP, nawet gdy bliższy AP jest dostępny.

## Zalecane punkty wyjścia

| Wdrożenie | Zalecenie |
| --- | --- |
| Pojedynczy router | Pozostaw moc nadawania na ustawieniu domyślnym lub automatycznym. |
| Dwa lub więcej przewodowych AP | Użyj nienakładających się kanałów i dostosuj moc nadawania, aby zmniejszyć nadmierne nakładanie się zasięgu. |
| Mesh z przewodowym backhaul | Zoptymalizuj komórki zasięgu pod kątem niezawodnego roamingu. |
| Mesh z bezprzewodowym backhaul | Unikaj zmniejszania mocy na tyle, aby osłabić połączenie backhaul. |

Po wprowadzeniu zmian przetestuj wydajność w kilku lokalizacjach i sprawdź:

- Siłę sygnału
- Przepustowość wysyłania i pobierania
- Opóźnienie
- Roaming między AP
- Jakość bezprzewodowego backhaul, jeśli dotyczy

Zmieniaj po jednym ustawieniu naraz, aby dokładnie zmierzyć jego wpływ.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com) lub [Skontaktuj się z nami](https://www.gl-inet.com/contact-us/).
