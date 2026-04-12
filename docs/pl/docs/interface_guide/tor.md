# Tor

Tor (od **The Onion Router**) to darmowe oprogramowanie open-source umożliwiające anonimową komunikację. Pozwala użytkownikom przeglądać internet z zachowaniem prywatności. [Dowiedz się więcej o sieci Tor](https://www.torproject.org/){target="_blank"}.

**Uwaga**: Ta funkcja jest aktualnie w wersji beta i może działać nieprawidłowo w niektórych krajach. Po włączeniu Tor następujące funkcje nie będą działać poprawnie:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Uwaga**: Modele oznaczone gwiazdką (*) nie obsługują natywnie Tor, ale użytkownicy mogą zainstalować Tor ręcznie za pomocą wtyczki. Kliknij [tutaj](#manual-install), aby uzyskać szczegółowe informacje.

??? "Nieobsługiwane modele"
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Szybka konfiguracja

W lewym panelu bocznym interfejsu administracyjnego przejdź do **VPN** -> **Tor**.

W przypadku oprogramowania układowego w wersji 4.8.4 i nowszej przejdź do **APPLICATIONS** -> **Tor**.

Włącz Tor przełącznikiem. W razie potrzeby aktywuj również **Custom Exit Nodes**, a następnie kliknij **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

Zostanie nawiązane połączenie. Jeśli sieć spełnia wymagania, pojawi się informacja o nawiązaniu połączenia.

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## Ręczna instalacja {#manual-install}

**Uwaga**: Na niektórych modelach Tor można zainstalować ręcznie za pomocą wtyczki, jednak może to zwiększyć obciążenie procesora i spowolnić odpowiedź systemu.

W lewym panelu bocznym interfejsu administracyjnego przejdź do **APPLICATIONS** -> **Plug-ins**.

Wyszukaj **gl-sdk4-ui-torview** i zainstaluj.

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
