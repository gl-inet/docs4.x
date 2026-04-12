# Akceleracja sieci

Akceleracja sieci zmniejsza obciążenie procesora i przyspiesza przekazywanie pakietów ruchu sieciowego, jednak może kolidować z niektórymi funkcjami.

Po włączeniu akceleracji sieci następujące funkcje przestają działać prawidłowo: Statystyki prędkości i ruchu klienta, Limit prędkości klienta.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Nieobsługiwane modele"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Konfiguracja

W lewym panelu administratora przejdź do **NETWORK** -> **Network Acceleration**.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Dostępne są trzy tryby.

- **Auto**
    
    Tryb automatyczny przełącza się między dwoma trybami akceleracji w zależności od aktualnego użycia.

- **Hardware Acceleration**

    Akceleracja sprzętowa działa na połączeniach <u>Ethernet</u> i <u>Repeater</u>.
    
    Przekazuje zadania sieciowe o wysokiej częstotliwości (np. NAT, przekazywanie pakietów, weryfikacja sumy kontrolnej) do dedykowanego sprzętu, takiego jak procesory NPU lub układy HWNAT. Działa na połączeniach Ethernet (przewodowy WAN/LAN) i Repeater, zapewniając wysoką przepustowość, niskie opóźnienia i minimalne obciążenie procesora przy transmisji danych z pełną prędkością łącza.

- **Software Acceleration**

    Akceleracja programowa działa na połączeniach <u>Cellular</u>.
    
    Opiera się na procesorze ogólnego przeznaczenia routera wspartym zoptymalizowanymi jądrami lub sterownikami (np. SWNAT). Obsługuje dostęp przez sieć komórkową (4G/5G) – główny scenariusz, w którym akceleracja sprzętowa jest niedostępna – zapewniając szeroką kompatybilność i obsługę złożonych protokołów. Choć elastyczna, może osiągać ograniczenia procesora przy dużym obciążeniu przepustowości, zwłaszcza podczas korzystania z zaawansowanych funkcji takich jak DPI, QoS czy przekierowanie portów.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.