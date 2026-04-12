# Ustawienia przycisku przełącznika

Funkcja **Toggle Button Settings** umożliwia przypisanie określonych funkcji do fizycznego przełącznika w routerze (w niektórych modelach nazywanego także przełącznikiem trybu), dzięki czemu zapewnia wygodne skróty do często wykonywanych operacji.

Zachowanie przełącznika można dostosować w panelu administracyjnym.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-MT1300 (Beryl)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-E750V2 (Mudi V2)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)

??? "Nieobsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Konfiguracja

W lewym panelu bocznym panelu administracyjnego przejdź do **SYSTEM** -> **Toggle Button Settings**.

![toggle button settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

Przed firmware v4.8 dostępne są następujące opcje, które pozwalają dostosować funkcję przycisku przełącznika.

- No Function
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

Od firmware v4.8 dodano kolejne opcje: Repeater, Wi‑Fi i LED. Dzięki temu użytkownik może lepiej dopasować działanie przełącznika do własnych potrzeb.

- No Function
- Repeater
- Wi-Fi (Main/Guest Wi-Fi)
- VPN
- Tor
- AdGuard Home
- LED

![toggle button 4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_4.8.png){class="glboxshadow"}

Podczas stosowania ustawień możesz zdecydować, czy wybrana funkcja ma zostać natychmiast włączona lub wyłączona zgodnie z bieżącą pozycją przełącznika (włączony/wyłączony, lewo/prawo).

**Uwaga**: Po ponownym uruchomieniu urządzenia system automatycznie zastosuje stan funkcji zgodnie z pozycją przełącznika.

Na przykład jeśli skonfigurujesz **WireGuard Client** do sterowania przełącznikiem, to gdy przełącznik jest ustawiony w pozycji LEFT (ON), klient WireGuard uruchomi się automatycznie. Gdy przełącznik jest ustawiony w pozycji RIGHT (OFF), klient WireGuard pozostanie wyłączony.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
