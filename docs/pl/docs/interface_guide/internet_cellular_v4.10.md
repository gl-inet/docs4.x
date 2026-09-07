# Połączenie z Internetem przez sieć komórkową (v4.10)

Treść tej strony dotyczy firmware w wersji v4.10 i nowszych. Jeśli urządzenie korzysta z innej wersji firmware, użyj poniższego selektora, aby przejść do odpowiedniego przewodnika.

<div class="gl-link-select" data-label="Wersja firmware" data-placeholder="Firmware v4.10 i nowsze" markdown="1">

- [Firmware v4.8 - v4.9](internet_cellular.md)
- [Firmware v4.7 i wcześniejsze](internet_cellular_v4.7.md)

</div>

---

Większość routerów GL.iNet obsługuje łączność komórkową. Ten przewodnik opisuje połączenia komórkowe dla dwóch typów routerów:

1. **Routery komórkowe**

    Routery komórkowe GL.iNet mają wbudowany moduł 4G/5G oraz jedno lub dwa gniazda kart SIM, na przykład Spitz AX (GL-X3000) i Mudi 7 (GL-E5800). Ustawienia sieci komórkowej w webowym panelu administracyjnym mogą się nieznacznie różnić w zależności od modelu i wersji firmware. Aby skonfigurować połączenie w tych modelach, zobacz [Routery komórkowe](#cellular-routers).

2. **Routery bez modemu komórkowego**

    Są to inne typy routerów, takie jak routery domowe, podróżne i miniaturowe oraz bramy bezpieczeństwa. Zwykle mają port USB, do którego można podłączyć modem USB (brak w zestawie), aby korzystać z sieci komórkowej. Aby skonfigurować połączenie w tych modelach, zobacz [Routery bez modemu komórkowego](#non-cellular-routers).

**Uwaga:** niektóre karty SIM wymagają aktywacji przed pierwszym użyciem. Aby zapewnić zgodność, aktywuj kartę SIM w smartfonie przed włożeniem jej do routera.

## Routery komórkowe {#cellular-routers}

W tej sekcji użyto modelu **Mudi 7 (GL-E5800)** jako przykładu do opisania konfiguracji połączenia komórkowego i powiązanych funkcji.

Mudi 7 ma wbudowaną kartę eSIM i dwa gniazda Nano-SIM oraz obsługuje Dual SIM Dual Standby. Dlatego jego webowy panel administracyjny może się nieznacznie różnić od panelu innych routerów komórkowych, zwłaszcza modeli z jednym gniazdem SIM.

### Konfiguracja sieci

Zaloguj się do webowego panelu administracyjnego routera i przejdź do **INTERNET** -> **Cellular**.

1. Gdy nie ma włożonej karty SIM, na stronie wyświetlany jest komunikat "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Włóż kartę SIM. Router automatycznie rozpocznie nawiązywanie połączenia. Po połączeniu na stronie zostaną wyświetlone operator karty SIM, siła sygnału, pasmo, wykorzystanie danych i dodatkowe opcje.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Jeśli karta SIM nie zostanie wykryta, włóż ją ponownie do routera albo uruchom router ponownie i spróbuj jeszcze raz.

3. Aby wyświetlić szczegóły sieci, kliknij **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    W sekcji **Network Information** można sprawdzić SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address i IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Czym jest Max Bit Rate (AMBR)?"

        Max Bit Rate (AMBR) oznacza Aggregate Maximum Bit Rate. Określa zagregowany górny limit szybkości transmisji dla wszystkich nośników non-GBR operatora. Ten parametr jest konfigurowany przez operatora sieci komórkowej.

4. Aby ręcznie skonfigurować sieć, kliknij **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    W sekcji **Network Settings** można skonfigurować parametry sieciowe, takie jak APN.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: ustawienia APN są zwykle automatycznie pobierane z karty SIM. Niektóre karty wymagają określonego APN. Jeśli nie znasz prawidłowego APN, skontaktuj się z operatorem.

    - **IP Type**: jest wykrywany automatycznie. Możesz wybrać IPv4, IPv6 lub oba typy. Upewnij się, że wybrana opcja odpowiada typowi IP obsługiwanemu przez kartę SIM. Jeśli karta nie obsługuje bieżącego typu IP albo wybrano IPv6, ale jest on wyłączony w routerze, mogą wystąpić problemy z połączeniem.

    - **International Data Roaming**: jest domyślnie włączony, aby ułatwić korzystanie z danych podczas podróży zagranicznych. Możesz go wyłączyć, jeśli nie jest potrzebny, lub aby uniknąć wysokich opłat roamingowych.

    - **TTL**: niektórzy operatorzy odczytują wartość TTL, aby określić, czy karta SIM jest używana w routerze. Jeśli karta nie działa w routerze, spróbuj ustawić TTL na wartość inną niż 64 i 128, na przykład 65.

    - **HL**: w IPv6 pole HL (Hop Limit) ogranicza liczbę przeskoków transmisji pakietów w sieci i jest odpowiednikiem TTL w IPv4.

    - **MTU**: ustaw wartość MTU odpowiednią do zastosowania. Nieprawidłowe ustawienia mogą przerwać połączenie z Internetem. Po zmianie MTU uruchom urządzenie ponownie, aby zastosować ustawienie.

    - **Authentication**: jeśli dane logowania nie są wymagane, zwykle ustawiona jest wartość NONE. Możesz wybrać PAP, CHAP lub PAP/CHAP.

### Statystyki ruchu

Aby wyświetlić statystyki ruchu, kliknij **Data Usage**.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Aby ustawić Data Cap Amount dla karty SIM lub harmonogram okresowego zerowania danych, włącz **SIM Limit Settings**.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Ustaw Data Cap Amount, Data Reset Period, Start Day i Start Hour, a następnie kliknij **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Uwaga**:

1. Jeśli Data Used przekroczy Data Cap Amount, zmień Data Cap Amount lub Data Used. W przeciwnym razie sieć może zostać rozłączona albo router może przełączyć się na inną kartę SIM, ale tylko wtedy, gdy włączono [przełączenie awaryjne SIM](#sim-failover).

2. Jeśli ustawiono SIM 1 Data Cap Amount i włączono SIM Auto Switch, po przekroczeniu Data Cap Amount przez SIM 1 router automatycznie przełączy się na SIM 2, a SIM 1 zostanie wyłączona.

3. Start Day: maksymalna liczba dni odpowiada rzeczywistej liczbie dni w bieżącym miesiącu.

### Szczegóły połączenia komórkowego

Aby wyświetlić szczegóły połączenia komórkowego, kliknij **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

W sekcji **Cellular Information** można sprawdzić Network Type, TAC, Cell ID, Band i Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: jest wykrywany automatycznie. Aby go określić, przejdź do karty **Cellular Settings** i wybierz typ sieci z listy rozwijanej.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Wybierz 5G, aby uzyskać większą szybkość (wymagany sygnał 5G), albo 4G, aby zwiększyć stabilność.

    Po zablokowaniu stacji bazowej typ sieci jest stały i nie można go zmienić.

- **TAC**: skrót od Tracking Area Code. Jest to identyfikator przypisywany przez sieć, który oznacza obszar śledzenia używany do zarządzania mobilnością w sieci komórkowej. Jest automatycznie wykrywany ze stacji bazowej.

- **Cell ID**: unikatowy identyfikator służący do rozróżniania poszczególnych komórek stacji bazowej. Jest również automatycznie wykrywany ze stacji bazowej.

- **Band Information**: kliknij, aby wyświetlić dodatkowe parametry pasma komórkowego.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: kliknij, aby wyświetlić historię siły sygnału. Możesz jej użyć do monitorowania jakości połączenia komórkowego.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Maskowanie pasm

Band Masking pozwala używać określonych pasm komórkowych w celu poprawy sygnału.

Aby włączyć Band Masking, kliknij **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

W sekcji **Cellular Settings** włącz **Band Masking**, wybierz pasma, których chcesz używać, a następnie kliknij **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Blokada operatora

!!! note "Obsługiwane modele"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) obsługuje tę funkcję w firmware v4.8 lub nowszym.

Po zablokowaniu konkretnego operatora komórkowego router korzysta tylko z jego sieci. Zapewnia to stabilne połączenie i pozwala uniknąć niezamierzonych opłat roamingowych, zwłaszcza na obszarach przygranicznych, gdzie urządzenie mogłoby połączyć się z siecią zagraniczną.

Aby zablokować operatora, kliknij **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

W sekcji **Cellular Settings** kliknij **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Przed skanowaniem sieci możesz wybrać **Lock Mode**.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: ręcznie zablokuj konkretnego operatora.

- **Manual-Auto**: automatycznie przełącz się na dostępną sieć operatora, jeśli ręczna blokada się nie powiedzie.

Następnie kliknij **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Odczekaj około minuty. Zostaną wyświetleni dostępni operatorzy. Wybierz jednego i kliknij **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Sygnał komórkowy zostanie zablokowany na wybranym operatorze.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Blokada stacji bazowej

!!! note "Obsługiwane modele"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) obsługuje tę funkcję w firmware v4.7 lub nowszym.

Aby uzyskać sygnał wysokiej jakości i zapewnić stabilne połączenie komórkowe, możesz spróbować zablokować stację bazową. Musi ona jednak odpowiadać pasmom częstotliwości obsługiwanym przez operatora i urządzenie. W przeciwnym razie połączenie może się nie powieść.

Aby zablokować stację bazową, kliknij **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

W sekcji **Cellular Settings** kliknij **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

W oknie podręcznym kliknij **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Odczekaj około minuty. Zostaną wyświetlone dostępne stacje bazowe.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Wybierz jedną, aby wyświetlić szczegóły, a następnie kliknij **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Sygnał komórkowy zostanie zablokowany na wybranej stacji bazowej.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Uwaga**:

1. Gdy interfejs Cellular jest włączony, urządzenie może nie być w stanie przeskanować wszystkich stacji bazowych.

2. Jeśli zablokowana stacja bazowa nie odpowiada włączonemu Band Masking lub parametrom APN w ustawieniach komórkowych, router nie będzie mógł połączyć się z siecią komórkową.

3. Jeśli po zablokowaniu stacji bazowej przeniesiesz router w inne miejsce, po ponownym uruchomieniu nadal będzie próbował połączyć się z zablokowaną stacją. Może to uniemożliwić automatyczne połączenie z siecią komórkową w nowej lokalizacji. W takim przypadku odblokuj bieżącą stację albo ręcznie zablokuj nową.

### SMS

Zapoznaj się z [SMS](../tutorials/sms.md).

### Przekazywanie SMS

Zapoznaj się z [Przekazywaniem SMS](../tutorials/sms_forwarding.md).

### Tryb samolotowy

Aby włączyć Airplane Mode, kliknij ikonę koła zębatego w prawym górnym rogu i włącz **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Informacje o modemie

Aby wyświetlić szczegóły modemu, kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Przełączenie awaryjne SIM {#sim-failover}

Ta funkcja jest dostępna tylko w routerach komórkowych obsługujących Dual-SIM.

SIM Failover umożliwia routerowi automatyczne przełączanie między SIM 1 i SIM 2. Gdy wykorzystanie danych karty o najwyższym priorytecie przekroczy Data Cap Amount albo karta nie może połączyć się z Internetem, router przełącza się na zapasową kartę SIM, aby utrzymać połączenie sieciowe.

Aby włączyć SIM Failover, kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

W oknie podręcznym włącz **Auto Switch**. Możesz przeciągnąć przycisk po prawej stronie, aby zmienić priorytet kart SIM.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Aby router wracał do preferowanej karty SIM o określonej porze dnia, włącz **Scheduled Switch to Preferred SIM**, ustaw **Daily Execution Time**, a następnie kliknij **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### Polecenia AT

Polecenia AT to standardowe instrukcje używane do komunikacji z modemem komórkowym. Ta funkcja umożliwia wysyłanie poleceń i sprawdzanie stanu modemu.

Kliknij ikonę koła zębatego w prawym górnym rogu i wybierz **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: gdy Shortcut ma wartość **Manual command**, wprowadź wybrane polecenie w polu **AT Command** i kliknij **Send** u dołu. Wynik zostanie wyświetlony w polu poniżej.

    Możesz również kliknąć pole i wybrać **preset command** z listy rozwijanej.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Na przykład wybierz skrót "Request SIM card status" oraz gniazdo SIM1, a następnie kliknij "Send", aby uzyskać wynik pokazany poniżej.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: wybierz, czy polecenie ma dotyczyć SIM1, czy SIM2.

- **AT Command**: gdy Shortcut ma wartość "Manual command", wpisz w tym polu wybrane polecenie.

## Routery bez modemu komórkowego {#non-cellular-routers}

W tej sekcji użyto routera **Flint 3 (GL-BE9300)** i zewnętrznego modemu USB [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} jako przykładu do opisania konfiguracji połączenia komórkowego.

**Uwaga**:

1. Niektóre komórkowe modemy USB, w tym SIMPoYo uFi, działają w **trybie host-less**. W tym trybie modem sam nawiązuje połączenie komórkowe i udostępnia routerowi wirtualny interfejs USB Ethernet. Router traktuje go jako połączenie WAN przez tethering, a nie jako sterowalny modem komórkowy. Dlatego połączenie jest nawiązywane przez interfejs Tethering, a nie Cellular.

2. W trybie tetheringu host-less router nie ma dostępu do niskopoziomowych parametrów sieci komórkowej, takich jak siła sygnału, Cell ID i TAC, ani nie może sterować APN lub parametrami karty SIM. Skonfiguruj te ustawienia we wbudowanym interfejsie WWW modemu.

---

Wykonaj poniższe czynności, aby skonfigurować połączenie komórkowe.

1. Podłącz modem USB do portu USB routera.

2. Zaloguj się do webowego panelu administracyjnego routera, przejdź do **INTERNET** -> **Tethering**, a następnie kliknij **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Jeśli musisz ustawić opcje zaawansowane, takie jak TTL, HL i MTU, przed kliknięciem **Connect** wybierz **Advanced** i dostosuj ustawienia.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Po nawiązaniu połączenia na stronie zostaną wyświetlone szczegóły sieci i zielona kropka wskazująca pomyślne połączenie.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

Po wstępnej konfiguracji modem zostanie rozpoznany automatycznie po ponownym uruchomieniu routera z podłączonym modemem lub po ponownym podłączeniu modemu. Połączenie sieciowe zostanie ustanowione bez ponownego klikania przycisku Connect.
