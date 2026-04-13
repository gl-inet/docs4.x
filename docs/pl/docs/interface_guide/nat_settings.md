# Ustawienia NAT

Funkcja dostępna od wersji v4.5.16.

W lewym panelu administratora przejdź do **NETWORK** -> **NAT Settings**.

Ta strona umożliwia włączenie **Full Cone NAT** w celu poprawy stabilności połączeń peer-to-peer w aplikacjach takich jak gry czy transmisje strumieniowe, oraz **SIP ALG** w celu rozwiązania problemów ze zgodnością usług telefonicznych VoIP/SIP.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

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
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Uwaga**: GL-SFT1200 (Opal) i GL-E750/E750V2 (Mudi) obsługują tę funkcję od wersji oprogramowania v4.7 i nowszych.

??? "Nieobsługiwane modele"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT

Full Cone NAT działa jak „bezpośredni skrót" dla urządzeń takich jak konsole do gier lub telefony podczas łączenia się z innymi urządzeniami online (np. w grach wieloosobowych lub połączeniach wideo).

Dzięki umożliwieniu zewnętrznym urządzeniom bezpośredniego docierania do urządzeń lokalnych przez router – zamiast ukrywania ich za wieloma warstwami NAT – poprawia stabilność połączeń peer-to-peer (P2P), zmniejsza opóźnienia i eliminuje błędy połączeń w aplikacjach P2P.

**Uwaga**: Włączenie tej funkcji może obniżyć poziom bezpieczeństwa w porównaniu z innymi typami NAT, ponieważ udostępnia porty urządzenia sieci publicznej.

## SIP ALG

SIP ALG (Application Layer Gateway) działa jako „tłumacz" routera dla usług komunikacyjnych VoIP/SIP, takich jak biurowe telefony stacjonarne lub połączenia przez aplikacje.

Zaprojektowany z myślą o rozwiązywaniu problemów z przechodzeniem przez NAT, dostosowuje dane połączeń tak, aby zapewnić ich prawidłowe przesyłanie przez wiele warstw NAT – typowe w sieciach z wieloma routerami (np. router główny i router GL.iNet) – ograniczając konflikty i zapobiegając przerywaniu połączeń.

**Uwaga**: Niezgodna lub nieprawidłowo zaimplementowana funkcja SIP ALG może pogorszyć jakość połączeń, powodując m.in. jednostronny dźwięk, brak sygnału dzwonienia, zrywanie połączeń lub przekierowanie połączeń bezpośrednio na pocztę głosową.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.