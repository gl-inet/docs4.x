# Połączenie z Internetem przez sieć komórkową

**Uwaga**: Ten przewodnik opiera się na firmware v4.8. W przypadku wcześniejszych wersji zapoznaj się z [tym przewodnikiem](internet_cellular_v4.7.md).

---

Większość routerów GL.iNet obsługuje łączność komórkową. Ten przewodnik obejmuje trzy typy modeli:

1. **Modele z wbudowanym modułem 4G i jedną kartą SIM**

    Niektóre modele mają wbudowany moduł 4G z jednym gniazdem karty SIM, na przykład GL-E750 (Mudi). Zobacz [konfigurację modeli z jedną kartą SIM](#setup-for-single-sim-models).

2. **Modele z wbudowanym modułem 5G i dwiema kartami SIM**

    Niektóre modele mają wbudowany moduł 5G z dwoma gniazdami kart SIM, na przykład GL-X3000 (Spitz AX). Ustawienia sieci komórkowej w panelu administracyjnym WWW mogą się nieznacznie różnić. Zobacz [konfigurację modeli z dwiema kartami SIM](#setup-for-dual-sim-models).

3. **Modele zgodne z modemem USB**

    Niektóre modele nie mają wbudowanego gniazda karty SIM, ale są wyposażone w port USB i obsługują połączenie komórkowe przez modem USB, na przykład GL-MT3000 (Beryl AX). Zobacz [konfigurację modemu USB](#setup-for-usb-modem).

**Uwaga:** Niektóre karty SIM wymagają aktywacji przed pierwszym użyciem. Aby zapewnić zgodność, aktywuj kartę SIM w smartfonie przed włożeniem jej do routera.

## Konfiguracja modeli z jedną kartą SIM {#setup-for-single-sim-models}

Poniższe kroki dotyczą modeli z wbudowanym modemem komórkowym i jednym gniazdem karty SIM.

Jako przykład użyjemy **GL-E750 (Mudi)**. 

Zalecamy najpierw wyłączyć router, włożyć do gniazda wcześniej aktywowaną kartę SIM, a następnie go włączyć. Jeśli włożysz kartę SIM po uruchomieniu routera, panel administracyjny WWW może nie odświeżyć się automatycznie. W takim przypadku odśwież stronę lub uruchom router ponownie.

### Konfiguracja automatyczna

Zaloguj się do panelu administracyjnego WWW routera i przejdź do **INTERNET** -> **Cellular**.

1. Gdy nie ma włożonej karty SIM, na stronie wyświetlany jest komunikat "Your SIM card has not been detected".

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Włóż kartę SIM. Urządzenie rozpocznie łączenie, jak pokazano poniżej.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Jeśli połączenie nie rozpocznie się automatycznie, kliknij przycisk **Connect**, jeśli jest dostępny.

    Jeśli karta SIM nie zostanie wykryta, spróbuj ponownie uruchomić router i sprawdź, czy zostanie rozpoznana.
    
3. Gdy sieć komórkowa zostanie połączona, na stronie zostaną wyświetlone szczegóły połączenia z zieloną kropką, co oznacza pomyślne połączenie.
    
    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Jeśli konfiguracja automatyczna się nie powiedzie, wypróbuj [konfigurację ręczną](#manual-setup-single-sim).

### Konfiguracja ręczna {#manual-setup-single-sim}

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**, a następnie kliknij **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Możesz wyświetlić lub zmodyfikować ustawienia komórkowe bieżącej karty SIM. 

**Uwaga**: Niektóre karty SIM mogą wymagać określonego APN. Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić ewentualne ograniczenia. W razie potrzeby skonfiguruj prawidłowy APN na routerze. 

Zastosowanie zmian spowoduje ponowne nawiązanie połączenia.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) to parametr bramy wymagany do połączenia z siecią komórkową. Umożliwia routerowi połączenie z Internetem dostarczanym przez operatora komórkowego. Możesz użyć domyślnego APN albo ustawić własny APN podany przez operatora.

- **Protocol**: Protokół komunikacji komórkowej (np. 3G, QMI lub QCM). Zwykle jest wykrywany automatycznie, ale możesz go zmienić zgodnie z wymaganiami modemu i operatora.

- **Port**: Port szeregowy używany do komunikacji z modemem komórkowym. Zwykle jest wykrywany automatycznie i nie wymaga ręcznej zmiany.

- **TTL**: TTL (Time To Live) określa maksymalny czas, przez jaki pakiety mogą istnieć w sieci. Domyślnie router zmniejsza TTL przychodzących pakietów z urządzeń klienckich o 1 przed ich przekazaniem. Jeśli chcesz to nadpisać, możesz ustawić tutaj stałą wartość. Ustawienie TTL dotyczy tylko IPv4.

- **HL**: W IPv6 parametr HL (Hop Limit) ogranicza liczbę przeskoków transmisji pakietów danych w sieci i pełni rolę odpowiednika TTL w IPv4.

- **MTU**: Domyślna wartość MTU to 1500 bajtów.

- **Authentication**: Wybierz metodę uwierzytelniania wymaganą przez operatora (np. NONE, PAP, CHAP). Zwykle ustawiona jest wartość NONE, jeśli dane logowania nie są wymagane.

- **Band Masking**: Możesz włączyć **Band Masking**, jeśli chcesz zablokować określone pasma lub zezwolić routerowi na używanie tylko wybranych pasm komórkowych. Szczegóły znajdziesz [tutaj](#band-masking).

## Konfiguracja modeli z dwiema kartami SIM {#setup-for-dual-sim-models}

Poniższe kroki dotyczą modeli z wbudowanym modemem komórkowym obsługującym dwie karty SIM. Strony mogą się nieznacznie różnić od modeli z jedną kartą SIM.

Jako przykład użyjemy **GL-X3000 (Spitz AX)**. Model ten obsługuje Dual SIM, Single Standby, co oznacza, że może mieć dwie karty SIM do dostępu komórkowego, ale aktywna może być tylko jedna karta naraz. Między kartami możesz przełączać się ręcznie.

Zalecamy najpierw wyłączyć router, włożyć wcześniej aktywowaną kartę SIM lub karty SIM do gniazd, a następnie go włączyć. Jeśli włożysz kartę SIM po uruchomieniu routera, panel administracyjny WWW może nie odświeżyć się automatycznie. W takim przypadku odśwież stronę lub uruchom router ponownie.

### Konfiguracja automatyczna

Zaloguj się do panelu administracyjnego WWW routera i przejdź do **INTERNET** -> **Cellular**.

1. Gdy nie ma włożonej karty SIM, na stronie wyświetlany jest komunikat "Your SIM card has not been detected". 

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Po włożeniu karty SIM strona będzie wyglądać jak poniżej. Kliknij **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Jeśli karta SIM nie zostanie wykryta, spróbuj ponownie uruchomić router i sprawdź, czy zostanie rozpoznana.

3. Gdy sieć komórkowa zostanie połączona, na stronie zostaną wyświetlone szczegóły połączenia z zieloną kropką, co oznacza pomyślne połączenie.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Kliknij **View More Information**, aby wyświetlić więcej informacji o połączeniu komórkowym, w tym szczegóły modemu, karty SIM, połączenia internetowego i sygnału komórkowego.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Jeśli konfiguracja automatyczna się nie powiedzie, wypróbuj [konfigurację ręczną](#manual-setup-dual-sim).

### Konfiguracja ręczna {#manual-setup-dual-sim}

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**, a następnie kliknij **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Możesz wyświetlić lub zmodyfikować ustawienia komórkowe bieżącej karty SIM. 

**Uwaga**: Niektóre karty SIM mogą wymagać określonego APN. Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić ewentualne ograniczenia. W razie potrzeby skonfiguruj prawidłowy APN na routerze. 

Zastosowanie zmian spowoduje ponowne nawiązanie połączenia.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) to parametr bramy wymagany do połączenia z siecią komórkową. Umożliwia routerowi połączenie z Internetem dostarczanym przez operatora komórkowego. Możesz użyć domyślnego APN albo ustawić własny APN podany przez operatora.

- **Protocol**: Automatycznie wykrywany protokół komunikacji komórkowej (np. QMI lub QCM) na podstawie modemu i operatora.

- **Port**: Automatycznie wykrywany port szeregowy używany do komunikacji z modemem komórkowym. 

- **TTL**: TTL (Time To Live) określa maksymalny czas, przez jaki pakiety mogą istnieć w sieci. Domyślnie router zmniejsza TTL przychodzących pakietów z urządzeń klienckich o 1 przed ich przekazaniem. Jeśli chcesz to nadpisać, możesz ustawić tutaj stałą wartość. Ustawienie TTL dotyczy tylko IPv4.

- **HL**: W IPv6 parametr HL (Hop Limit) ogranicza liczbę przeskoków transmisji pakietów danych w sieci i pełni rolę odpowiednika TTL w IPv4.

- **MTU**: Domyślna wartość MTU to 1500 bajtów.

- **Authentication**: Wybierz metodę uwierzytelniania wymaganą przez operatora (np. NONE, PAP, CHAP). Zwykle ustawiona jest wartość NONE, jeśli dane logowania nie są wymagane.

- **Band Masking**: Możesz włączyć **Band Masking**, jeśli chcesz zablokować określone pasma lub zezwolić routerowi na używanie tylko wybranych pasm komórkowych. Szczegóły znajdziesz [tutaj](#band-masking).

### Ustawienia gniazda karty SIM

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**, a następnie kliknij **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Zostanie wyświetlony przycisk automatycznego przełączania, aktywna karta SIM, ICCID i operator sieci.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Jeśli włożone są dwie karty SIM, możesz włączyć **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: Włącza automatyczne przełączanie między SIM 1 i SIM 2. Metoda wykrywania sieci dla **SIM Auto Switch** jest taka sama jak skonfigurowana na stronie Multi-WAN.

- **Preferred SIM Card Slot**: Ustaw preferowaną kartę SIM jako SIM 1 lub SIM 2.

- **Failover Interval**: Dostępne wartości mieszczą się w zakresie od 5 minut do 24 godzin.

    Jeśli po przełączeniu awaryjnym połączenie internetowe nadal nie jest dostępne, urządzenie przełączy się z powrotem na preferowane gniazdo SIM i odczeka ten interwał przed kolejną próbą przełączenia awaryjnego.

    Ta opcja ma zastosowanie wtedy, gdy zarówno preferowana karta SIM, jak i zapasowa karta SIM nie mają sygnału. Urządzenie będzie przełączać się między kartami SIM, dopóki jedna z nich nie uzyska prawidłowego sygnału.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled** 
    
    Po włączeniu urządzenie będzie codziennie o skonfigurowanej godzinie sprawdzać preferowane gniazdo SIM i podejmować próbę powrotu, jeśli preferowana karta SIM odzyska dostęp do Internetu.
    
    Zapobiega to nadmiernemu zużyciu danych przez kartę zapasową. Jeśli preferowana karta SIM nadal nie ma sygnału, urządzenie będzie nadal korzystać z karty zapasowej.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Uwaga**: Funkcja **Auto Switch** nie przełącza się na inną kartę SIM natychmiast. Po pierwsze, urządzenie potrzebuje czasu, aby potwierdzić, że bieżąca karta SIM nie ma dostępu do Internetu. Po drugie, druga karta SIM nie znajduje się w trybie gotowości i potrzebuje czasu na aktywację.

## Konfiguracja modemu USB {#setup-for-usb-modem}

Poniższe kroki dotyczą modeli bez wbudowanego gniazda karty SIM, ale wyposażonych w port USB do podłączenia zewnętrznego modemu USB.

Jako przykład użyjemy **GL-MT3000 (Beryl AX)** z zewnętrznym modemem USB **SIMPoYo uFi**.

Zalecamy najpierw wyłączyć router, włożyć wcześniej aktywowaną kartę SIM do modemu USB, podłączyć modem do portu USB routera, a następnie włączyć router. Jeśli podłączysz modem USB po uruchomieniu routera, panel administracyjny WWW może nie odświeżyć się automatycznie. W takim przypadku odśwież stronę lub uruchom router ponownie.

### Szybka konfiguracja

1. Najpierw wyłącz router. Włóż kartę SIM do modemu USB, podłącz modem do portu USB routera, a następnie włącz router.

2. Zaloguj się do panelu administracyjnego WWW routera, przejdź do **INTERNET** -> **Tethering**, a następnie kliknij **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Jeśli chcesz skonfigurować ustawienia zaawansowane (np. TTL, HL i MTU), kliknij **Advanced**, dostosuj ustawienia, a następnie kliknij **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    Rozpocznie się łączenie.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Po nawiązaniu połączenia na stronie zostaną wyświetlone szczegóły połączenia z zieloną kropką, co oznacza pomyślne połączenie.
    
    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Uwaga:** Po wstępnej konfiguracji, jeśli uruchomisz router ponownie z podłączonym modemem USB lub podłączysz modem ponownie, zostanie on rozpoznany automatycznie, a połączenie sieciowe zostanie ustanowione bez ponownego klikania przycisku **Connect**.

### Zgodne modemy

Poniżej znajduje się lista obsługiwanych modemów, które zostały wcześniej przetestowane. 

**SIMPoYo uFi** to kompaktowy modem USB typu plug & play z hotspotem Wi-Fi, zaprojektowany z myślą o szybkiej i niezawodnej łączności w dowolnym miejscu. Działa bezproblemowo z większością routerów GL.iNet, a także z laptopami, powerbankami, portami USB w samochodach i innymi źródłami zasilania USB. W zestawie znajduje się 10 GB darmowych danych na 30 dni, ważnych w Wielkiej Brytanii i 34 krajach Europy.

| Model                                  | Sieć komórkowa | Przetestowano | Testował        | Uwagi*    |
| -------------------------------------- | --------------- | ------------- | --------------- | --------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)                        | 5G              | Tak           | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/)               | 4G              | Tak           | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G              | Tak           | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G              | Tak           | GL.iNet         |           |
| Quectel EC200A series                  | 4G              | Tak           | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G              | Tak           | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G              | Tak           | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G              | Tak           | akw2312         |           |
| Quectel RM520N-GL                      | 5G              | Tak           | akw2312         |           |
| Quectel UC20-E                         | 3G              | Tak           | GL.iNet         |           |
| ZTE ME909s-821                         | 4G              | Tak           | GL.iNet         |           |
| Huawei E1550                           | 3G              | Tak           | GL.iNet         |           |
| Huawei E3276                           | 4G              | Tak           | GL.iNet         |           |
| Huawei E3372                           | 4G              | Tak           | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G              | Tak           | anonymous       | Host-less |
| TP-Link MA260                          | 3G              | Tak           | GL.iNet         |           |
| ZTE M823                               | 4G              | Tak           | Arnas Risqianto |           |
| ZTE MF190                              | 3G              | Tak           | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G              | Tak           | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G              | Tak           | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G              | Tak           | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G              | Tak           | anonymous       | Host-less |

- **QMI**: Ten modem obsługuje tryb QMI. Wybierz QMI jako protokół komunikacji komórkowej oraz **/dev/cdc-wdm0** jako port szeregowy w ustawieniach karty SIM.

- **Host-less**: Ten modem obsługuje tryb Tethering. Zarządzaj połączeniem przez interfejs **Tethering** routera, a nie przez interfejs **Cellular**.

## Statystyki ruchu

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**, a następnie kliknij **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Otworzy się strona statystyk ruchu. Wyświetla ona wykorzystanie danych przez kartę SIM lub karty SIM oraz udostępnia ustawienia limitu danych.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Jeśli wartość **Data Used** przekroczy **Data Cap Amount**, zmodyfikuj ręcznie **Data Cap Amount** lub **Data Used**. W przeciwnym razie połączenie sieciowe może zostać rozłączone lub karta SIM może przełączyć się przez **Auto Switch** (w modelach z dwiema kartami SIM).

- **Modyfikacja wartości Data Used**

    Kliknij **Modify** po prawej stronie pola SIM 1/2 **Data Used**. 

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Następnie możesz zmienić lub zresetować zużycie danych. 

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Ustawienie limitu danych SIM**

    Jeśli chcesz ustawić limit danych dla karty SIM, najpierw włącz **Save data when power off**. Oznacza to, że dane będą zapisywane nawet po wyłączeniu urządzenia.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Następnie włącz ustawienia limitu dla SIM 1 lub SIM 2.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

W przypadku modeli z dwiema kartami SIM sugerujemy jednoczesne włączenie **SIM Card Slot Auto Switch**. Jeśli ustawiona jest wartość **SIM 1 Data Cap Amount** i włączono **SIM Card Slot Auto Switch**, karta SIM 1 automatycznie przełączy się na SIM 2 po przekroczeniu **Data Cap Amount**, a SIM 1 zostanie wyłączona.

## Historia sygnału

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**, a następnie kliknij **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Możesz tutaj sprawdzić jakość połączenia komórkowego. Jeśli sygnał jest słaby, spróbuj przełączyć stację bazową, aby uzyskać lepszy sygnał.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Historię siły sygnału można przeglądać, wybierając różne zakresy czasu w prawym górnym rogu.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Maskowanie pasm {#band-masking}

**Band Masking** pozwala blokować określone pasma albo używać wyłącznie preferowanych pasm komórkowych, aby poprawić słaby sygnał komórkowy.

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular** -> **SIM Card Settings** i włącz **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Wybierz **Masking Mode** (Block lub Open), a następnie pasma LTE Bands, 5G NSA Bands i 5G SA Bands.

## SMS

Zapoznaj się z [samouczkiem SMS](sms.md).

## Przekazywanie SMS

Zapoznaj się z [samouczkiem SMS Forwarding](../tutorials/sms_forwarding.md).

## Blokada stacji bazowej

!!! note "Obsługiwane modele"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) obsługuje tę funkcję w firmware w wersji 4.7 lub nowszej.

Jeśli chcesz uzyskać sygnał wysokiej jakości i zapewnić stabilne połączenie komórkowe, możesz spróbować zablokować stację bazową.

**Uwaga:** Zablokowana stacja bazowa musi odpowiadać pasmom częstotliwości obsługiwanym przez operatora i urządzenie, w przeciwnym razie połączenie może się nie powieść.

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**. Kliknij ikonę z trzema kropkami w prawym górnym rogu, a następnie wybierz **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Kliknij **Scan**, aby rozpocząć skanowanie stacji bazowych sygnału komórkowego. Potrwa to kilka minut. Nie odświeżaj strony podczas skanowania. 

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

Zostaną wyświetlone dostępne stacje bazowe.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Kliknij stację bazową, aby wyświetlić jej szczegóły i ją zablokować.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Uwaga**: 

1. Gdy interfejs **Cellular** jest włączony, urządzenie może nie być w stanie przeskanować wszystkich stacji bazowych.

2. Jeśli zablokowana stacja bazowa nie odpowiada parametrom **Band Masking** lub APN w ustawieniach komórkowych, router nie będzie mógł połączyć się z siecią komórkową.

3. Po zablokowaniu stacji bazowej, jeśli przeniesiesz router w inne miejsce, po ponownym uruchomieniu nadal będzie próbował połączyć się z zablokowaną stacją. Może to uniemożliwić automatyczne połączenie routera z siecią komórkową w nowej lokalizacji. W takim przypadku musisz odblokować bieżącą stację bazową albo ręcznie zablokować nową.

## Blokada operatora

Ta funkcja jest dostępna tylko w modelach GL-X3000, GL-XE3000 i GL-X2000 (firmware ver.4.8 lub nowszy).

Po zablokowaniu do konkretnego operatora komórkowego router będzie korzystał wyłącznie z sieci tego operatora, co zapewnia stabilne połączenie i pozwala uniknąć niezamierzonych opłat roamingowych — szczególnie w obszarach przygranicznych, gdzie urządzenie mogłoby w przeciwnym razie łączyć się z zagranicznymi sieciami.

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**. Kliknij ikonę z trzema kropkami w prawym górnym rogu, a następnie wybierz **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Dostępne są trzy tryby blokady: 

- **Auto**: Automatyczne połączenie z dostępną siecią operatora.
- **Manual**: Ręczne zablokowanie wybranego operatora.
- **Manual-Auto**: Automatyczne przełączenie na dostępną sieć operatora, jeśli ręczna blokada się nie powiedzie.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Komendy AT modemu

Komendy AT modemu to standardowe polecenia używane do komunikacji z modemem komórkowym. Dzięki tej funkcji możesz wysyłać polecenia i sprawdzać stan modemu.

W panelu administracyjnym WWW routera przejdź do **INTERNET** -> **Cellular**. Kliknij ikonę z trzema kropkami w prawym górnym rogu, a następnie wybierz **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Otworzy się strona komend AT.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Gdy w polu Shortcut ustawiono **Manual command**, możesz wpisać wybrane polecenie w polu AT Command.

Możesz też kliknąć listę rozwijaną Shortcut, aby wybrać jedną z **preset commands**.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Dostępne są następujące predefiniowane polecenia:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

Jako przykład wybrano tutaj skrót "Request IMEI". Kliknij "Send", a otrzymasz wynik, jak pokazano poniżej.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

W prawym dolnym rogu możesz kliknąć **Export Debug Info**, aby pobrać plik .json.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Rozwiązywanie problemów

Jeśli nie możesz nawiązać połączenia komórkowego, kliknij poniższy komunikat o błędzie, aby zobaczyć odpowiednie rozwiązania.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Oto kilka wskazówek dotyczących rozwiązywania problemów.
    
    1. Odśwież stronę i odczekaj kilka minut, aby sprawdzić, czy karta SIM zostanie wykryta.
    
    2. Upewnij się, że karta SIM jest prawidłowo zainstalowana. Dopasuj wycięcie karty SIM do odpowiedniego oznaczenia na gnieździe karty, aby potwierdzić właściwy kierunek wkładania.
    
    3. Wyłącz router, wyjmij i włóż kartę SIM ponownie, a następnie włącz router.
    
    4. Jeśli to możliwe, spróbuj użyć innej karty SIM.

    Jeśli problem będzie się utrzymywał, pobierz logi i wyślij je na adres [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Ten problem ma dwa rodzaje komunikatów o błędzie:

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed
    
        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Oto kilka wskazówek dotyczących rozwiązywania problemów.

    1. Odśwież stronę i odczekaj kilka minut, aby sprawdzić, czy błąd zniknie.
    
    2. Kliknij **Disconnect**/**Abort**, a następnie kliknij **Connect**, aby spróbować połączyć się ponownie.
    
    3. Uruchom router ponownie.
    
    4. Sprawdź stan karty SIM i upewnij się, że jest aktywna. Przetestuj kartę SIM, wkładając ją do smartfona, aby potwierdzić, że ma normalny dostęp do Internetu przy aktywnym pakiecie danych mobilnych, lub skontaktuj się z operatorem sieci w celu weryfikacji.
    
    5. Niektórzy operatorzy mogą wymagać protokołu 3G do połączenia z siecią. Przejdź do **SIM Card Settings** -> **Protocol**, wybierz **3G**, a następnie kliknij **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Urządzenie połączy się ponownie automatycznie. Odczekaj kilka minut, aby sprawdzić, czy połączenie zakończyło się powodzeniem.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Jeśli połączenie powiedzie się, strona będzie wyglądać jak poniżej.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}
    
    6. Niektóre karty SIM mogą mieć szczególne ograniczenia użytkowania (np. wymagać określonego APN). Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić ewentualne ograniczenia. 
    
        W razie potrzeby przejdź do **SIM Card Settings** -> **APN**, skonfiguruj prawidłowy APN na routerze, a następnie kliknij **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}
    
    7. Kliknij **View More Information**, aby sprawdzić siłę sygnału komórkowego. Jeśli sygnał jest słaby, upewnij się, że antena została prawidłowo zamontowana. Przenieś router w otwarte miejsce bez przeszkód, aby uzyskać lepszy odbiór sygnału.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}
    
    8. Sprawdź, czy **Band Masking** lub **Lock Tower** są włączone. Jeśli tak, wyłącz tę funkcję i spróbuj połączyć się ponownie.

    Jeśli problem będzie się utrzymywał, pobierz logi i wyślij je na adres [support@gl-inet.com](mailto:support@gl-inet.com).

## Certyfikacja IoT {#iot-certification}

### Certyfikacja AT&T

Kliknij link [att device certification](https://iotdevices.att.com/certified-devices.aspx#) i wpisz nazwę urządzenia, aby je znaleźć. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Certyfikacja T-Mobile

Kliknij link [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) i wybierz 5G w polu **Filter**, aby znaleźć urządzenie. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Powiązane artykuły

- [Strona Internet](internet.md)
- [Jak ustawić priorytet poszczególnych metod dostępu do Internetu?](multi-wan.md)
- [Jak ustawić równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu do Internetu?](multi-wan.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
