# Dual-Ethernet WAN

Funkcja Dual-Ethernet WAN umożliwia przełączenie domyślnego portu LAN1 na drugi port WAN, aby zapewnić podwójny dostęp Ethernet. Zapewnia to niezawodne łącze zapasowe i obsługuje agregację przepustowości (jeśli jest obsługiwana) w zastosowaniach o dużym zapotrzebowaniu. Pozwala też jednocześnie połączyć się z dwiema oddzielnymi sieciami (np. służbową i prywatną), zwiększając elastyczność bez dodatkowego sprzętu.

## Obsługiwane modele

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

    **Uwaga**: GL-E5800 (Mudi 7) jest wyposażony w jeden port Ethernet (domyślnie LAN, z możliwością przełączenia na WAN) oraz **port USB-C z obsługą OTG**. Aby dodać drugi port Ethernet do Dual-Ethernet WAN, podłącz do portu USB-C sprzedawany oddzielnie adapter USB‑C‑to‑Ethernet.

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

## Konfiguracja

1. Zaloguj się do webowego panelu administracyjnego routera.

2. Przejdź do **NETWORK** -> **Port Management** -> zakładki **LAN**, zmień rolę portu na WAN i kliknij **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_1.png){class="glboxshadow"}

3. W wyskakującym oknie kliknij **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_2.png){class="glboxshadow"}

4. Po włączeniu Dual-Ethernet WAN możesz skonfigurować funkcje Multi-WAN [tutaj](../interface_guide/multi-wan.md).

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
