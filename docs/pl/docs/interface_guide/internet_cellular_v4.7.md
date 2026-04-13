# Połączenie z Internetem przez sieć komórkową (firmware v4.7 i wcześniejsze)

**Uwaga**: Ten przewodnik dotyczy firmware v4.7 i wcześniejszych. W przypadku nowszych wersji zapoznaj się z [tym przewodnikiem](internet_cellular.md).

---

Większość routerów GL.iNet obsługuje łączność komórkową. Ten przewodnik obejmuje trzy typy modeli:

1. **Modele z wbudowanym modułem 4G i jedną kartą SIM**

    Niektóre modele mają wbudowany moduł 4G z jednym gniazdem karty SIM, na przykład GL-XE300 (Puli). Zobacz [konfigurację modeli z jedną kartą SIM](#setup-for-single-sim-models).

2. **Modele zgodne z modemem USB**

    Niektóre modele są wyposażone w port USB i obsługują łączność komórkową za pośrednictwem modemu USB, na przykład GL-AXT1800 (Slate AX). Kroki konfiguracji są podobne do tych dla modeli z wbudowanym modułem 4G i jedną kartą SIM. Zobacz [konfigurację modeli z jedną kartą SIM](#setup-for-single-sim-models).

3. **Modele z wbudowanym modułem 5G i dwiema kartami SIM**

    Niektóre modele mają wbudowany moduł 5G z dwoma gniazdami kart SIM, na przykład GL-X3000 (Spitz AX). Ustawienia sieci komórkowej w panelu administracyjnym WWW mogą się nieznacznie różnić. Zobacz [konfigurację modeli z dwiema kartami SIM](#setup-for-dual-sim-models).

**Uwaga:** Niektóre karty SIM wymagają aktywacji przed pierwszym użyciem. Aby zapewnić zgodność, aktywuj kartę SIM w smartfonie przed włożeniem jej do routera.

## Konfiguracja modeli z jedną kartą SIM {#setup-for-single-sim-models}

Poniższe kroki dotyczą modeli z wbudowanym modemem komórkowym i jednym gniazdem karty SIM (np. GL-XE300 Puli) lub z portem USB do podłączenia zewnętrznego modemu USB (np. GL-AXT1800 Slate AX).

Jako przykład użyjemy **GL-AXT1800 (Slate AX)** z zewnętrznym modemem USB.

Zalecamy najpierw wyłączyć router. Włóż wcześniej aktywowaną kartę SIM do modemu USB, a następnie podłącz modem do portu USB routera. Po tym włącz router.

Jeśli podłączysz modem USB po uruchomieniu routera, panel administracyjny WWW może nie odświeżyć się automatycznie. W takim przypadku odśwież stronę lub uruchom router ponownie.

### Konfiguracja automatyczna

Zaloguj się do panelu administracyjnego WWW routera i przejdź do **INTERNET** -> **Cellular**.

1. Przy pierwszym wejściu połączenie może nie zostać nawiązane automatycznie, ale w lewym górnym rogu powinna być widoczna nazwa operatora oraz numer IMEI. Kliknij **Auto Setup**.

    Zignoruj ostrzeżenie *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Rozpocznie się nawiązywanie połączenia.

    **Uwaga:** Niektóre karty SIM mogą mieć szczególne ograniczenia użytkowania, na przykład wymóg określonego APN. Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić, czy obowiązują specjalne ograniczenia.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Po nawiązaniu połączenia na stronie zostaną wyświetlone szczegóły sieci z zieloną kropką, co oznacza pomyślne połączenie.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Uwaga:** Po wstępnej konfiguracji, jeśli uruchomisz router ponownie z podłączonym modemem USB lub podłączysz modem ponownie, modem USB zostanie rozpoznany automatycznie, a połączenie sieciowe zostanie ustanowione bez ponownego klikania przycisku **Auto Setup**.

Jeśli konfiguracja automatyczna się nie powiedzie, wypróbuj [konfigurację ręczną](#manual-setup).

### Konfiguracja ręczna {#manual-setup}

W sekcji Cellular kliknij **Manual Setup**, aby wyświetlić lub zmodyfikować ustawienia komórkowe bieżącej karty SIM.

**Uwaga**: Niektóre karty SIM mogą wymagać określonego APN. Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić ewentualne ograniczenia. W razie potrzeby skonfiguruj prawidłowy APN na routerze.

Zastosowanie zmian spowoduje ponowne nawiązanie połączenia.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: Protokół komunikacji komórkowej (np. 3G, QMI lub QCM). Zwykle jest wykrywany automatycznie, ale możesz go zmienić zgodnie z wymaganiami modemu i operatora.

- **Port**: Port szeregowy używany do komunikacji z modemem komórkowym. Zwykle jest wykrywany automatycznie i nie wymaga ręcznej zmiany.

- **APN**: APN (Access Point Name) to parametr bramy wymagany do połączenia z siecią komórkową. Umożliwia routerowi połączenie z Internetem dostarczanym przez operatora komórkowego. Możesz użyć domyślnego APN albo ustawić własny APN podany przez operatora.

- **PIN**: Jeśli karta SIM jest chroniona kodem PIN, wprowadź go tutaj. To pole jest opcjonalne, jeśli PIN nie jest ustawiony.

- **TTL**: TTL (Time To Live) określa maksymalny czas, przez jaki pakiety mogą istnieć w sieci. Domyślnie router zmniejsza TTL przychodzących pakietów z urządzeń klienckich o 1 przed ich przekazaniem. Jeśli chcesz to nadpisać, możesz ustawić tutaj stałą wartość. Ustawienie TTL dotyczy tylko IPv4.

- **Service**: Wybierz typ usługi komórkowej, aby określić technologie sieciowe używane przez modem.

- **Dial Number**: Wprowadź numer wybierania podany przez operatora. W nowoczesnych sieciach jest on często wstępnie skonfigurowany i w większości przypadków można pozostawić to pole puste.

- **Authentication**: Wybierz metodę uwierzytelniania wymaganą przez operatora (np. NONE, PAP, CHAP). Zwykle ustawiona jest wartość NONE, jeśli dane logowania nie są wymagane.

### Zgodne modemy

Poniżej znajduje się lista obsługiwanych modemów, które zostały wcześniej przetestowane.

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Yes    | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Yes    | akw2312         |           |
| Quectel UC20-E                         | 3G    | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G    | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G    | Yes    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Yes    | anonymous       | Host-less |

- **QMI**: Ten modem obsługuje tryb QMI. Wybierz QMI jako protokół i **/dev/cdc-wdm0** jako port szeregowy dla routera komórkowego.

- **Host-less**: Ten modem obsługuje tryb Tethering. Zarządzaj połączeniem przez interfejs **Tethering** routera, a nie przez interfejs **Cellular**.

## Konfiguracja modeli z dwiema kartami SIM {#setup-for-dual-sim-models}

Poniższe kroki dotyczą modeli z wbudowanym modemem komórkowym obsługującym dwie karty SIM. Panel administracyjny WWW może nieznacznie różnić się od modeli z jedną kartą SIM.

Jako przykład użyjemy **GL-X3000 (Spitz AX)**. Model ten obsługuje Dual SIM, Single Standby, co oznacza, że może mieć dwie karty SIM do dostępu komórkowego, ale aktywna może być tylko jedna karta naraz. Między kartami możesz przełączać się ręcznie.

Zalecamy najpierw wyłączyć router, włożyć wcześniej aktywowaną kartę SIM lub karty SIM do gniazd, a następnie go włączyć. Jeśli włożysz kartę SIM po uruchomieniu routera, panel administracyjny WWW może nie odświeżyć się automatycznie. W takim przypadku odśwież stronę lub uruchom router ponownie.

### Konfiguracja automatyczna

Zaloguj się do panelu administracyjnego WWW routera i przejdź do **INTERNET** -> **Cellular**.

1. Gdy nie ma włożonej karty SIM, strona wygląda jak poniżej.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Po włożeniu karty SIM router rozpocznie łączenie automatycznie.

    Jeśli połączenie powiedzie się, strona będzie wyglądać jak poniżej.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Jeśli połączenie nie zostanie nawiązane automatycznie, kliknij **Auto Setup** i poczekaj, aż router się połączy, albo wypróbuj **Manual Setup**.

### Konfiguracja ręczna

W sekcji Cellular kliknij **Manual Setup**, aby przejść do ustawień komórkowych.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Możesz wyświetlić lub zmodyfikować ustawienia komórkowe bieżącej karty SIM. Dostępnych jest także kilka wstępnie skonfigurowanych profili, a własne konfiguracje możesz ręcznie dodać do sekcji "Saved Settings".

### Ustawienia gniazd kart SIM

W sekcji Cellular kliknij **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Przejdziesz do **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Jeśli włożone są dwie karty SIM, możesz włączyć **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

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

## Statystyki ruchu

W sekcji Cellular kliknij **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Przejdziesz do strony Traffic Statistics.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Zapoznaj się z [poradnikiem SMS](sms.md).

## Przekazywanie SMS

Zapoznaj się z [poradnikiem SMS Forwarding](../tutorials/sms_forwarding.md).

## Zarządzanie modemem

W sekcji Cellular kliknij przycisk **Tool** w prawym górnym rogu, aby przejść do strony zarządzania modemem.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Zawiera ona dwie sekcje: **Modem Info** i **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

Polecenia AT to standardowe instrukcje używane do komunikacji z modemem komórkowym.

Gdy w polu Shortcut ustawisz **Manual command**, wpisz żądane polecenie w polu AT Command, aby sprawdzić stan modemu.

Możesz też kliknąć listę rozwijaną Shortcut, aby wybrać z listy **preset commands**.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Dostępne są następujące polecenia predefiniowane:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

Jako przykład wybrano tutaj skrót "Request IMEI". Kliknij "Send", a otrzymasz wynik pokazany poniżej.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Profil operatora

Możesz zapisać różne profile dla tego samego lub różnych operatorów.

W sekcji Cellular kliknij przycisk **Profile** w prawym górnym rogu, aby zarządzać profilami.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Dodaj nowy profil albo zapisz bieżący profil.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Utwórz własny profil zgodnie z wymaganiami operatora.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Następnym razem możesz wybrać zapisany profil.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Wybierz potrzebne profile.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Blokowanie stacji bazowej

Ta funkcja jest dostępna tylko w modelach GL-X3000, GL-XE3000 i GL-X2000 (firmware ver.4.7 lub nowszy).

Jeśli chcesz uzyskać sygnał wyższej jakości i zapewnić stabilne połączenie komórkowe, możesz spróbować zablokować stację bazową.

**Uwaga:** Zablokowana stacja bazowa musi odpowiadać pasmom częstotliwości obsługiwanym przez operatora i urządzenie, w przeciwnym razie połączenie może się nie powieść.

W sekcji Cellular kliknij ikonę **Tower** w prawym górnym rogu.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Zostaną wyświetlone dostępne stacje bazowe.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Kliknij stację bazową, aby wyświetlić szczegóły i zablokować połączenie z nią.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

U góry zostanie wyświetlony stan stacji bazowej (np. Locked/Unlocked).

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Uwaga**: 

1. Gdy interfejs Cellular jest włączony, urządzenie może nie być w stanie zeskanować wszystkich stacji bazowych.

2. Jeśli zablokowana stacja bazowa nie odpowiada ustawieniom Band Masking lub parametrom APN w ustawieniach komórkowych, router nie będzie mógł połączyć się z siecią komórkową.

3. Po zablokowaniu stacji bazowej, jeśli przeniesiesz router w inne miejsce, po ponownym uruchomieniu nadal będzie próbował połączyć się z zablokowaną stacją bazową. Może to uniemożliwić automatyczne połączenie z siecią komórkową w nowej lokalizacji. W takim przypadku odblokuj bieżącą stację bazową albo ręcznie zablokuj nową.

## Historia sygnału

W sekcji Cellular kliknij ikonę **Signal** w prawym górnym rogu, aby sprawdzić historię siły sygnału.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Pomaga to ocenić jakość połączenia komórkowego. Jeśli sygnał jest słaby, spróbuj przełączyć stację bazową, aby uzyskać lepszy sygnał.

Możesz wyświetlić historię siły sygnału komórkowego, wybierając różne zakresy czasu.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking

W sekcji Cellular kliknij **View More** i wybierz **Cells Info**, aby sprawdzić szczegóły komórek.

Zobaczysz aktualnie używane pasma oraz stan ich sygnału.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Jeśli sygnał jest słaby, możesz włączyć Band Masking, aby zablokować określone pasma. Jeśli sygnał jest dobry, możesz też pozwolić routerowi korzystać wyłącznie z wybranych pasm komórkowych.

Kliknij **Manual Setup**, aby przejść do strony ustawień komórkowych, a następnie włącz **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Wybierz **Masking Mode** (Block lub Open), a następnie wybierz LTE Bands, 5G NSA Bands i 5G SA Bands.

## Rozwiązywanie problemów

Jeśli nie uda się nawiązać połączenia komórkowego, kliknij poniższy komunikat o błędzie, aby zobaczyć odpowiednie rozwiązania.

??? note "No SIM / Your SIM card has not been detected"
    
    1. Odśwież stronę i odczekaj kilka minut, aby sprawdzić, czy karta SIM zostanie wykryta.
    
    2. Upewnij się, że karta SIM jest włożona prawidłowo. Dopasuj wycięcie na karcie SIM do odpowiedniego oznaczenia przy gnieździe, aby potwierdzić poprawny kierunek włożenia.
    
    3. Wyłącz router, wyjmij i włóż kartę SIM ponownie, a następnie włącz router.
    
    4. Jeśli to możliwe, spróbuj użyć innej karty SIM.

    Jeśli problem nadal występuje, pobierz logi i wyślij je na adres [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Odśwież stronę i odczekaj kilka minut, aby sprawdzić, czy komunikat błędu zniknie.
    
    2. Kliknij **Disconnect**/**Abort**, a następnie kliknij **Connect**, aby spróbować połączyć się ponownie.
    
    3. Uruchom router ponownie.
    
    4. Sprawdź stan karty SIM i upewnij się, że została aktywowana. Przetestuj kartę SIM, wkładając ją do smartfona, aby potwierdzić, że może normalnie łączyć się z Internetem przy aktywnym pakiecie danych, albo skontaktuj się z operatorem sieci w celu weryfikacji.
    
    5. Niektórzy operatorzy sieci mogą wymagać protokołu 3G do połączenia z siecią. Przejdź do **Manual Setup** -> **Cellular Settings** -> **Protocol**, wybierz **3G**, a następnie kliknij **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Urządzenie połączy się ponownie automatycznie. Odczekaj kilka minut, aby sprawdzić, czy połączenie zakończyło się powodzeniem.

    6. Niektóre karty SIM mogą mieć szczególne ograniczenia użytkowania (np. wymagać określonego APN). Jeśli karta SIM nie zarejestruje się w sieci, skontaktuj się z operatorem, aby sprawdzić ewentualne ograniczenia.
    
        W razie potrzeby przejdź do **Manual Setup** -> **Cellular Settings** -> **APN**, skonfiguruj prawidłowy APN na routerze, a następnie kliknij **Apply**.

    7. Kliknij **View More** i wybierz **Cells Info**, aby sprawdzić siłę sygnału komórkowego. Jeśli sygnał jest słaby, upewnij się, że antena jest zamontowana prawidłowo. Przenieś router w otwarte miejsce bez przeszkód, aby poprawić odbiór sygnału.
    
    8. Sprawdź, czy funkcja **Band Masking** lub **Lock Tower** jest włączona. Jeśli tak, wyłącz ją i spróbuj połączyć się ponownie.

    Jeśli problem nadal występuje, pobierz logi i wyślij je na adres [support@gl-inet.com](mailto:support@gl-inet.com).

## IoT Certification

### AT&T Certification

Kliknij link [att device certification](https://iotdevices.att.com/certified-devices.aspx#) i wpisz nazwę urządzenia, aby je znaleźć.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile Certification

Kliknij link [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) i wybierz 5G w polu **Filter**, aby znaleźć urządzenie.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Powiązane artykuły

- [Strona Internet](internet.md)
- [Jak ustawić priorytet każdej metody dostępu do Internetu?](multi-wan.md)
- [Jak ustawić równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu do Internetu?](multi-wan.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
