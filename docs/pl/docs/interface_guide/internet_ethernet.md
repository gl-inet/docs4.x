# Połączenie z Internetem przez kabel Ethernet

Podłącz router do sieci szerokopasmowej za pomocą kabla Ethernet wpiętego do portu WAN. Zwykle adres IP jest pobierany automatycznie (DHCP). Użytkownicy mogą też ręcznie skonfigurować statyczny adres IP lub PPPoE. Ta metoda zapewnia wysoką stabilność i dużą prędkość, dlatego idealnie sprawdza się w domu i biurze z przewodowym dostępem szerokopasmowym.

Wykonaj poniższe kroki, aby połączyć router z Internetem za pomocą kabla Ethernet.

1. Podłącz port WAN routera do urządzenia nadrzędnego (np. modemu operatora, routera, przełącznika sieciowego lub gniazda Ethernet) za pomocą kabla Ethernet. 

2. Zaloguj się do panelu administracyjnego routera i przejdź do sekcji **INTERNET** -> **Ethernet**. 

    Jeśli połączenie powiedzie się, w sekcji Ethernet zostaną wyświetlone szczegóły sieci, w tym Protocol, IP Address, Gateway i DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Wskazówka**: Przed podłączeniem kabla Ethernet do portu WAN routera możesz kliknąć **Change to LAN**, aby [ustawić port WAN jako port LAN](../faq/change_wan_to_lan.md). Jest to przydatne, gdy używasz routera jako [repeatera](internet_repeater.md), ponieważ fizyczny port WAN pozostaje wtedy nieużywany. Dzięki temu możesz wykorzystać nieużywany port WAN jako port LAN i zyskać dodatkowy port LAN.

## Protocol

Dostępne są 3 typy protokołów: DHCP, Static i PPPoE. Kliknij **Modify**, aby je zmienić.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP to domyślny i najczęściej używany protokół, który automatycznie przypisuje urządzeniom sieciowym adresy IP oraz inne parametry komunikacyjne w architekturze klient-serwer w sieciach IP.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static jest wymagany, jeśli dostawca usług internetowych (ISP) przydziela stały adres IP albo chcesz ręcznie skonfigurować informacje sieciowe, takie jak adres IP, Gateway i Netmask.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE to protokół używany przez większość dostawców usług internetowych. Zwykle dostarczają oni modem oraz nazwę użytkownika i hasło potrzebne do skonfigurowania dostępu do Internetu.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Advanced

Oprócz podstawowych ustawień dostępne są także opcjonalne ustawienia zaawansowane dla trzech powyższych protokołów.

* **VLAN ID**: To ustawienie jest wymagane tylko wtedy, gdy serwer dostawcy wymaga, aby interfejs używał określonego oznaczonego identyfikatora VLAN.

* **TTL**: TTL (Time To Live) określa maksymalny czas, przez jaki pakiety mogą istnieć w sieci. Domyślnie router zmniejsza wartość TTL pakietów przychodzących z urządzeń klienckich o 1 przed ich przekazaniem dalej. Jeśli chcesz ją nadpisać, możesz ustawić tutaj stałą wartość. Ustawienie TTL dotyczy tylko IPv4.

* **HL**: W IPv6 pole HL (Hop Limit) ogranicza liczbę przeskoków transmisji pakietów danych w sieci i jest odpowiednikiem TTL w IPv4.

* **MTU**: Domyślna wartość MTU wynosi 1500 bajtów.

## Ethernet Port

Kliknij ikonę koła zębatego w prawym górnym rogu, aby przejść do [Ethernet Port](ethernet_port.md).

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

Na stronie **WAN** są wyświetlane funkcja portu (czyli użycie jako WAN lub LAN), tryb MAC i adres MAC oraz wynegocjowana prędkość portu sieciowego. 

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

Na stronie **LAN** są wyświetlane funkcja portu oraz wynegocjowana prędkość portu sieciowego.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

Szczegółowe informacje znajdziesz pod tym [linkiem](ethernet_port.md). 

## Rozwiązywanie problemów

Jeśli kabel Ethernet jest podłączony do portu WAN, ale Internet nie jest dostępny, pojawi się żółty komunikat pokazany poniżej.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Aby rozwiązać ten problem:

1. Sprawdź, czy urządzenie nadrzędne ma dostęp do Internetu.

2. Przejdź na stronę [Multi-WAN](multi-wan.md), aby sprawdzić stan interfejsu Ethernet.

---

Powiązane artykuły

- [Strona Internet](internet.md)
- [Jak ustawić priorytet dla każdej metody dostępu do Internetu?](multi-wan.md)
- [Jak ustawić równoważenie obciążenia, gdy jednocześnie używanych jest kilka metod dostępu do Internetu?](multi-wan.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
