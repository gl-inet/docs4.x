# Port Ethernet (oprogramowanie sprzętowe v4.10)

**Uwaga**: treść tej strony jest obecnie dostępna w routerze Flint 4 (GL-BE14000) i zostanie udostępniona dla innych modeli wraz z oprogramowaniem sprzętowym v4.10.

Jeśli urządzenie korzysta z innej wersji oprogramowania sprzętowego, użyj poniższego selektora, aby przejść do odpowiedniego przewodnika.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Oprogramowanie sprzętowe v4.9 i starsze](ethernet_port.md)

</div>

---

W panelu administracyjnym po lewej stronie przejdź do **NETWORK** -> **Ethernet Port**.

Na tej stronie są wyświetlane wszystkie interfejsy routera. Można sprawdzić stan połączenia każdego interfejsu, zarządzać rolami portów Ethernet (WAN lub LAN) oraz wyświetlać szczegóły portu, takie jak adres MAC, wynegocjowana prędkość i bieżący stan łącza. Można również przypisać interfejsy fizyczne do dowolnej utworzonej podsieci.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: niebieskie podświetlenie ikony portu oznacza aktywne łącze fizyczne.

- **Link Down**: szara ikona portu oznacza nieaktywne łącze fizyczne.

- **Speed**: wynegocjowana szybkość transmisji portu Ethernet.

- **MAC**: adres MAC portu.

- **VLAN Mode**: tryb działania portów LAN można ustawić na Standard lub Multiple VLANs.

- **Native Network**: domyślna nieoznaczona podsieć przypisana do portu LAN.

- **Allowed VLANs**: określa oznaczone sieci VLAN, które mogą przechodzić przez port w trybie Multiple VLANs.

- **Settings**: kliknij, aby otworzyć stronę konfiguracji danego portu.

## WAN

W tej sekcji są wyświetlane: tryb portu (WAN lub LAN), adres MAC i wynegocjowana prędkość.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: bieżący tryb działania fizycznego portu WAN. W razie potrzeby można ustawić go jako LAN.

- **MAC Mode**: domyślnie ustawiony jest Factory Mode. Można przełączyć na Clone Mode lub Random Mode.

- **MAC Address**: adres MAC interfejsu WAN.

- **Negotiated Network Port Rate**: wynegocjowana prędkość łącza interfejsu WAN, wyświetlana wyłącznie po wykryciu prawidłowego połączenia.

## LAN

W tej sekcji jest wyświetlana konfiguracja portu LAN. Tryb Ethernet Mode można ustawić na **Standard** lub **Multiple VLANs**.

### Tryb Standard

Tryb Standard zezwala tylko na jedną sieć VLAN (Untagged) i służy do podłączania urządzeń końcowych.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: wynegocjowana prędkość łącza interfejsu LAN, wyświetlana wyłącznie po wykryciu prawidłowego połączenia.

- **Ethernet Mode**: domyślnie ustawiony jest Standard Mode.
  
- **Access Network**: umożliwia izolację sieci przez przypisanie portów LAN do różnych podsieci.

Po skonfigurowaniu można wrócić do strony Ethernet Port, aby sprawdzić ustawienia.

### Tryb Multiple VLANs

Tryb Multiple VLANs zezwala na wiele sieci VLAN (Tagged) na jednym porcie i jest zwykle używany do podłączania punktów dostępowych lub innych przełączników.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: wynegocjowana prędkość łącza interfejsu LAN, wyświetlana wyłącznie po wykryciu prawidłowego połączenia.

- **VLAN Mode**: aby przełączyć na tryb Multiple VLANs, kliknij kartę Multiple VLANs.

- **Untagged Traffic Handling**: skonfiguruj obsługę nieoznaczonych pakietów na porcie. Można je bezpośrednio odrzucać albo przekazywać do innej podsieci jako natywnej sieci PVID.

- **Allowed Tagged Networks**: określa sieci VLAN, które mogą przechodzić przez port w trybie oznaczonym. Z listy można wybrać sieci VLAN; przekazywany będzie tylko pasujący ruch.

Po skonfigurowaniu można wrócić do strony Ethernet Port, aby sprawdzić ustawienia.

Niektóre modele umożliwiają przełączenie LAN 1 na port WAN w konfiguracji Dual-Ethernet WAN. Szczegółowe informacje zawiera sekcja [Dual-Ethernet WAN](#dual-ethernet-wan).

## Dual-Ethernet WAN

Funkcja Dual-Ethernet WAN umożliwia przełączenie domyślnego portu Ethernet LAN na dodatkowy port WAN i korzystanie z dwóch połączeń Ethernet z Internetem. Zapewnia niezawodne połączenie zapasowe i, w zgodnych konfiguracjach, agregację przepustowości na potrzeby zadań wymagających dużego pasma. Pozwala także jednocześnie łączyć się z dwiema niezależnymi sieciami, na przykład służbową i prywatną, zwiększając elastyczność bez dodatkowego sprzętu.

??? "Obsługiwane modele"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Uwaga**: GL-E5800 (Mudi 7) jest wyposażony w jeden port Ethernet (domyślnie LAN, z możliwością przełączenia na WAN) oraz **port USB-C z obsługą OTG**. Aby dodać drugi port Ethernet dla funkcji Dual-Ethernet WAN, podłącz do portu USB‑C sprzedawany oddzielnie adapter USB‑C do Ethernet.

??? "Nieobsługiwane modele"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Poniżej opisano sposób przełączenia portu LAN na WAN na przykładzie Flint 3 (GL-BE9300).

1. Na stronie **Ethernet Port** kliknij ustawienie **LAN1**, aby otworzyć stronę Configuration. Następnie przełącz rolę portu na WAN i kliknij **Apply**.
   
    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Wróć do strony Ethernet Port i sprawdź, czy rola portu została przełączona na WAN.
   
    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. Wybrany port będzie teraz działać jako port WAN. Następnie można skonfigurować Multi-WAN [tutaj](multi-wan.md).

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
