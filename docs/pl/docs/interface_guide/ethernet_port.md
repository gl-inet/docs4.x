# Port Ethernet

**Uwaga**: Ta strona była dostępna jako **Port Management** od firmware v4.7, a w firmware v4.8.3 zmieniono jej nazwę na **Ethernet Port**.

---

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Port Management** lub **Ethernet Port**.

Ta strona umożliwia zarządzanie rolami portów Ethernet (WAN/LAN) oraz wyświetlanie szczegółów portów, takich jak adres MAC i wynegocjowana prędkość.

## WAN

Ta sekcja wyświetla rolę portu (WAN lub LAN), adres MAC oraz wynegocjowaną prędkość.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN**: Bieżący tryb pracy fizycznego portu WAN. W razie potrzeby możesz ustawić go jako LAN.

- **MAC Mode**: Domyślnie ustawiony jest **Factory Mode**. Możesz przełączyć go na **Clone Mode** lub **Random Mode**.

- **Mac Address**: Adres MAC interfejsu WAN.

- **Negotiated Network Port Rate**: Wynegocjowana prędkość łącza interfejsu WAN. Jest wyświetlana tylko wtedy, gdy wykryto prawidłowe połączenie.

## LAN

Ta sekcja wyświetla wynegocjowaną prędkość portu LAN. Jest ona widoczna tylko wtedy, gdy wykryto prawidłowe połączenie.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Niektóre modele obsługują przełączenie LAN 1 na port WAN w scenariuszu Dual-Ethernet WAN. Szczegóły znajdziesz w sekcji [Dual-Ethernet WAN](#dual-ethernet-wan).

## Dual-Ethernet WAN

Funkcja Dual-Ethernet WAN pozwala przełączyć domyślny port Ethernet LAN na dodatkowy port WAN, aby korzystać z podwójnego dostępu do Internetu przez Ethernet. Zapewnia to niezawodne łącze zapasowe i obsługuje agregację przepustowości (jeśli jest obsługiwana) w zastosowaniach wymagających dużej przepustowości. Pozwala też jednocześnie połączyć się z dwiema niezależnymi sieciami, np. służbową i prywatną, zwiększając elastyczność bez dodatkowego sprzętu.

??? "Obsługiwane modele"
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

    **Uwaga**: GL-E5800 (Mudi 7) jest wyposażony w jeden port Ethernet (domyślnie LAN, z możliwością przełączenia na WAN) oraz **port USB-C z obsługą OTG**. Aby dodać drugi port Ethernet do Dual-Ethernet WAN, podłącz do portu USB-C sprzedawany oddzielnie adapter USB-C-to-Ethernet.

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

Wykonaj poniższe kroki, aby przełączyć port LAN na port WAN.

1. Na stronie **Port Management** lub **Ethernet Port** kliknij kartę **LAN**, zmień rolę portu na WAN, a następnie kliknij **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. W wyskakującym oknie kliknij **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. Wybrany port będzie teraz działać jako port WAN. Następnie możesz skonfigurować Multi-WAN [tutaj](multi-wan.md).

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
