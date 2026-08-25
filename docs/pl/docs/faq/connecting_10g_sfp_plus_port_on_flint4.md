# Podłączanie portu 10G SFP+ w routerze Flint 4

Router Flint 4 (GL‑BE14000) jest wyposażony w port 10G SFP+, którego rolę można przełączać między WAN i LAN. Port współpracuje z różnymi modułami i kablami SFP+ do optycznych i miedzianych połączeń Ethernet. Pozwala to spełnić różne wymagania sieciowe, w tym dostęp światłowodowy na duże odległości, tradycyjne okablowanie skrętką oraz zaawansowane zakończenie światłowodu PON.

Poniżej szczegółowo opisano trzy sposoby podłączenia portu SFP+ w routerze Flint 4 (GL-BE14000), wraz ze scenariuszami zastosowania, topologią, zaletami i wadami, środkami ostrożności oraz zgodnymi modelami podanymi wyłącznie jako punkt odniesienia.

## Rozwiązanie 1. Transceiver optyczny + kabel światłowodowy

### 1.1 Scenariusze

To rozwiązanie jest przeznaczone do stabilnych sieci Ethernet 10G działających na duże odległości. Główne zastosowania obejmują:

- połączenie ze światłowodowym łączem Ethernet 10G operatora w celu zapewnienia bardzo szybkiego dostępu szerokopasmowego w domu lub firmie;  
- tworzenie długodystansowych połączeń sieciowych wewnątrz i na zewnątrz budynków, na przykład połączenie Flint 4 ze zdalnym przełącznikiem 10G, okablowanie między piętrami domu lub wdrożenie sieci szkieletowej w małym biurze.

### 1.2 Topologia

Port 10G SFP+ routera Flint 4 → Standardowy transceiver optyczny 10G SFP+ (SR/MR/LR) → Kabel światłowodowy → Zdalny przełącznik sieciowy 10G / terminal światłowód-Ethernet operatora

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology1.png){class="glboxshadow"}

### 1.3 Zalety i wady

Poniższa tabela ocenia najważniejsze parametry wydajności i użyteczności rozwiązania z transceiverem optycznym i kablem światłowodowym. Oceny w postaci gwiazdek i szczegółowe uwagi służą jako punkt odniesienia.

|Parametr|Ocena|Uwagi|
|---|---|---|
|Odległość transmisji|★★★★★|Obsługuje do 300m (światłowód wielomodowy) lub ponad 10km (światłowód jednomodowy), przekraczając ograniczenia odległości kabli miedzianych. Nadaje się do sieci dalekiego zasięgu.|
|Odporność na zakłócenia|★★★★★|Transmisja sygnału optycznego jest odporna na zakłócenia elektromagnetyczne, elektryczność statyczną i przesłuchy, co zapewnia stabilną pracę w złożonych środowiskach.|
|Energooszczędność|★★★★★|Niskie zużycie energii i mała emisja ciepła; dojrzała konstrukcja układu umożliwia długotrwałą, stabilną pracę pod pełnym obciążeniem bez ryzyka przegrzania.|
|Zgodność|★★★★★|Pełna oficjalna obsługa i zgodność ze standardowymi protokołami Ethernet 10G, bez ryzyka związanego z dostosowaniem oprogramowania sprzętowego.|
|Łatwość wdrożenia|★★★☆☆|Wymaga podstawowej znajomości specyfikacji łączenia światłowodów. Nieprawidłowe wykonanie może powodować tłumienie sygnału, dlatego próg wdrożenia jest nieco wyższy niż w przypadku okablowania miedzianego.|
|Koszt|★★★☆☆|Wymaga dodatkowych transceiverów optycznych i kabli światłowodowych, dlatego całkowity koszt jest wyższy niż w przypadku tradycyjnych rozwiązań opartych na skrętce.|

### 1.4 Środki ostrożności

- Obsługiwane są wyłącznie standardowe transceivery optyczne Ethernet 10G. Moduły optyczne wykorzystujące protokół PON nie nadają się do tego rozwiązania.

- Dobierz moduły jednomodowe lub wielomodowe oraz kable światłowodowe do rzeczywistej odległości transmisji, aby uniknąć spadku szybkości lub utraty łącza.

- Rozwiązanie obsługuje wyłącznie usługi operatora Ethernet 10G przez światłowód. Nie można go podłączyć bezpośrednio do tradycyjnych domowych linii światłowodowych GPON/XGS-PON.

### 1.5 Zgodne modele

Poniżej wymieniono niektóre standardowe transceivery optyczne, których zgodność z Flint 4 została sprawdzona przez GL.iNet i użytkowników. Lista służy wyłącznie jako punkt odniesienia.

|Model|Tester|
|---|---|
|ipolex AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|ipolex CAB-10GSFP-P1.5M 10G SFP+ DAC 1.5m, 30AWG|Użytkownik|
|QSFPTEK QT-SFP+SR CO SFP+ 10G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP-2.5G-0401D SFP 2.5G 850nm 300m|GL.iNet|
|QSFPTEK QT-SFP+-SR CO SFP+ 10G 850nm 300m|Użytkownik|
|QINIYEK BJ-SFP+SR AR 10G 850nm 300m|GL.iNet|
|QINIYEK BJ-SFP+-SR CI SFP+ 10G 850nm 300m|Użytkownik|
|XZSNET SFP10G-SR|GL.iNet|
|10Gtek AXS85-192-M3 10GBase-SR 850nm 300m|GL.iNet|
|10Gtek AZS85-192-M1 25G SFP28-SR 850nm 100m|GL.iNet|
|10Gtek ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|10Gtek ASF85-24-X2-D 1.25G SFP-SX 850nm 550m|GL.iNet|
|FS Cisco SFP-10G-SR Compatible 10GBASE-SR|GL.iNet|
|FS Juniper EX-SFP-10GE-SR 10GBASE-SR SFP+|GL.iNet|
|FS Arista SFP-10G-SR 10GBASE-SR SFP+|GL.iNet|
|FS Brocade 10G-SFPP-SR 10GBASE-SR SFP+|GL.iNet|
|HUAWEI 6G-850nm-120m-MM-SFP+ MTRS-6A11-01|GL.iNet|
|HUAWEI 2.5G-1310nm-SM-ESFP MXPD-483II|GL.iNet|
|netLINK 10G/850nm/300m/DDM HTB-10G-SR|GL.iNet|
|H!Fiber ASF-GE2-T 10/100/1000Base-T SFP SGMII RJ-45 100m|GL.iNet|
|H!Fiber ASF85-24-X2-D 1000Base-SX 850nm 550m|GL.iNet|
|Cisco GLC-SX-MMD 10-2626-01 CLASS 1 21CFR1040.10 LN#50|Użytkownik|
|ONTI OBT-C2GE-R10 SFP 2500Base-TX RJ45 100m|Użytkownik|

## Rozwiązanie 2. Moduł SFP+ do RJ45 (SFP‑10G‑T)

### 2.1 Scenariusze

Moduł SFP‑10G‑T przekształca gniazdo optyczne SFP+ w standardowy interfejs RJ45 do skrętki. Jest przeznaczony do sieci 10G na krótkie odległości, wykorzystujących tradycyjne kable sieciowe. Typowe zastosowania obejmują krótkie połączenie między Flint 4 a przełącznikiem 10G lub urządzeniem NAS, szybkie dodanie portu 10G RJ45 bez ponownego układania światłowodu oraz szybką sieć LAN w domu lub małym biurze z zachowaniem tradycyjnego okablowania skrętką. Jest to odpowiednia alternatywa dla użytkowników, którzy potrzebują Ethernet 10G, ale nie mają instalacji światłowodowej.

### 2.2 Topologia

Port 10G SFP+ routera Flint 4 → Moduł SFP+ do RJ45 (SFP‑10G‑T) → Kabel skrętkowy CAT6A/CAT7 → Przełącznik 10G / przewodowe urządzenie końcowe 10G

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology2.png){class="glboxshadow"}

### 2.3 Zalety i wady

Poniższa tabela ocenia najważniejsze parametry wydajności i użyteczności rozwiązania z modułem SFP+ do RJ45 (SFP‑10G‑T). Oceny w postaci gwiazdek i szczegółowe uwagi służą jako punkt odniesienia.

|Parametr|Ocena|Uwagi|
|---|---|---|
|Odległość transmisji|★★☆☆☆|Ograniczenia sprzętowe układu PHY pozwalają na stabilną transmisję na odległość najwyżej 30 metrów. Rozwiązanie nie nadaje się do okablowania dalekiego zasięgu.|
|Odporność na zakłócenia|★★★☆☆|Tradycyjna transmisja skrętką jest podatna na zakłócenia elektromagnetyczne i przesłuchy w złożonych instalacjach kablowych.|
|Energooszczędność|★★☆☆☆|Duże zużycie energii i wyraźna emisja ciepła przy ciągłym wysokim obciążeniu. Długotrwała praca wymaga odpowiedniego odprowadzania ciepła.|
|Zgodność|★★★★☆|Zgodność ze wszystkimi standardowymi urządzeniami końcowymi 10G RJ45. Stabilną transmisję 10G zapewniają wyłącznie kable CAT6A/CAT7.|
|Łatwość wdrożenia|★★★★★|Działanie plug-and-play bez potrzeby regulacji toru optycznego. Rozwiązanie jest zgodne z tradycyjnymi metodami układania kabli sieciowych i bardzo proste w obsłudze.|
|Koszt|★★★★☆|Wykorzystuje istniejące okablowanie RJ45, bez kosztu przebudowy instalacji na światłowodową. Należy jedynie oddzielnie kupić moduł 10G-T.|

### 2.4 Środki ostrożności

- Stabilna transmisja 10G wymaga kabli CAT6A lub wyższej kategorii. Kable CAT6 i niższych kategorii powodują spadek szybkości i utratę pakietów.

- Długość okablowania nie może przekraczać 30 metrów. Przekroczenie limitu prowadzi do niestabilności łącza, spadku szybkości lub rozłączenia.

- Pozostaw wokół modułu SFP‑10G‑T miejsce umożliwiające odprowadzanie ciepła, aby zapobiec awarii spowodowanej przegrzaniem.

### 2.5 Zgodne modele

Poniżej wymieniono niektóre moduły SFP+ do RJ45, których zgodność z Flint 4 została sprawdzona przez GL.iNet i użytkowników. Lista służy wyłącznie jako punkt odniesienia.

|Model|Tester|
|---|---|
|ipolex 10G Base-T RJ45 30m|GL.iNet|
|ipolex ASF-GE-T 1000Base-T SFP RJ-45 100m|GL.iNet|
|QSFPTEK QT-SFP-10G-T UB RJ45 30m|GL.iNet|
|XZSNET-SFP10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-10G-T RJ45 30m|GL.iNet|
|10Gtek ASF-2G-T 2.5GBase-T SFP RJ-45 100m|GL.iNet|
|10Gtek ASF-10G2-T 1G/2.5G/5G/10GBase-T RJ-45 30m|Użytkownik|
|HUAWEI SFP-1000BASE-T-RJ45-100m SFP-1000Base-T|Użytkownik|
|Xicom SFP-2.5G-T 100/1000M/2.5G RJ45 100m|Użytkownik|

## Rozwiązanie 3. Moduł PON‑ONU SFP+

### 3.1 Scenariusze

Moduł PON‑ONU SFP+ integruje wszystkie funkcje modemu optycznego ONU i umożliwia bezpośrednie zakończenie tradycyjnej domowej linii światłowodowej GPON/XGS-PON w porcie SFP+ routera Flint 4. Eliminuje to potrzebę stosowania oddzielnego zewnętrznego modemu optycznego, łącząc dostęp światłowodowy i routing w jednym urządzeniu. Rozwiązanie jest przeznaczone dla zaawansowanych użytkowników, zwłaszcza tych, którzy chcą ograniczyć liczbę urządzeń w sieci domowej i bezpośrednio podłączyć linię PON operatora do routera.

### 3.2 Topologia

Port 10G SFP+ routera Flint 4 → Moduł PON‑ONU SFP+ → Linia światłowodowa GPON/XGS-PON operatora (w tym kabel przyłączeniowy, rozdzielacz PON i OLT operatora)

![](https://static.gl-inet.com/docs/router/en/4/faq/connecting_10g_sfp+_port_on_flint4/topology3.png){class="glboxshadow"}

### 3.3 Zalety i wady

Poniższa tabela ocenia najważniejsze parametry wydajności i użyteczności rozwiązania z modułem PON‑ONU SFP+. Oceny w postaci gwiazdek i szczegółowe uwagi służą jako punkt odniesienia.

|Parametr|Ocena|Uwagi|
|---|---|---|
|Odległość transmisji|★★★★★|Obsługuje standardową odległość transmisji światłowodu PON, spełniając wymagania wszystkich typowych domowych i komercyjnych zastosowań dostępu światłowodowego.|
|Odporność na zakłócenia|★★★★★|Transmisja światłowodowa zapewnia wysoką odporność na zakłócenia i stabilny sygnał, zgodnie z powszechnymi standardami dostępu światłowodowego PON.|
|Energooszczędność|★★☆☆☆|Podczas szybkiej pracy moduł wytwarza dużo ciepła. Dodatkowe chłodzenie jest konieczne, aby zapobiec spadkom wydajności i rozłączeniom.|
|Zgodność|★★☆☆☆|Nieoficjalnie sprawdzone rozwiązanie dla zaawansowanych użytkowników. Zgodność zależy od listy dozwolonych urządzeń operatora i modelu modułu, a długotrwała praca może być niestabilna.|
|Łatwość wdrożenia|★★☆☆☆|Wymaga wcześniejszego potwierdzenia przez operatora, skonfigurowania uwierzytelniania SN/PLOAM i zoptymalizowania odprowadzania ciepła. Ogólny próg wdrożenia jest wysoki.|
|Koszt|★★★☆☆|Eliminuje koszt oddzielnego modemu optycznego, ale wiąże się z ryzykiem niedostępności usług IPTV lub głosowych oraz brakiem oficjalnego wsparcia technicznego.|

### 3.4 Środki ostrożności

- **Uzyskaj wcześniej zgodę operatora**: sprawdź, czy operator zezwala na podłączenie do sieci PON urządzenia ONU innej firmy należącego do klienta, i uzyskaj wymagane parametry uwierzytelniania, w tym kod rejestracyjny SN oraz hasło PLOAM.

- **Odprowadzanie ciepła jest obowiązkowe**: zastosuj dodatkowe chłodzenie modułu PON‑ONU, aby zapobiec obniżeniu częstotliwości, utracie pakietów i rozłączeniom spowodowanym wysoką temperaturą.

- **Brak gwarancji działania usługi**: GL.iNet nie zapewnia wsparcia technicznego dla tego rozwiązania. Problemów takich jak niestabilność sieci, wahania szybkości i nieprawidłowe działanie usług dodatkowych nie można rozwiązać za pomocą oficjalnego oprogramowania sprzętowego ani wsparcia posprzedażowego.

- Operatorzy stosują różne listy dozwolonych modeli modułów. Przed zakupem sprawdź, które modele modułów PON są obsługiwane przez operatora.

### 3.5 Zgodne modele

Poniżej wymieniono niektóre moduły PON-ONU SFP+, których zgodność z Flint 4 została sprawdzona przez GL.iNet i użytkowników. Lista służy wyłącznie jako punkt odniesienia.

|Model|Tester|
|---|---|
|HUAWEI MA5671A 2.5G ONU stick|GL.iNet|
|NOKIA GPON ONT SFP Class I Laser G-010S-A|Użytkownik|

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
