# Użycie U-Boot do odbrickowania routera

Jeśli router został uszkodzony po własnych modyfikacjach lub wgraniu niewłaściwego firmware, dostęp do niego może być niemożliwy. W takim przypadku możesz ponownie zainstalować firmware za pomocą trybu awaryjnego U-Boot.

**Uwaga:** Operacja U-Boot usunie ustawienia routera i zainstalowane wtyczki.

---

## Przygotowanie

Przygotuj komputer stacjonarny lub laptop z portem Ethernet. Jeśli komputer nie ma portu Ethernet, potrzebny będzie dodatkowy adapter USB-Ethernet.

**Uwaga**: GL-E5800 (Mudi 7) obecnie nie obsługuje wgrywania firmware przez U-Boot.

## Kroki odbrickowania

Obejrzyj ten samouczek wideo lub wykonaj poniższe czynności, aby uzyskać dostęp do interfejsu U-Boot Web UI i ponownie zainstalować firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Kroki użycia U-Boot do ponownej instalacji firmware są zasadniczo takie same; w tym filmie jako przykład pokazano Mudi/Mudi V2. W przypadku innych modeli możesz wykonać procedurę opisaną poniżej.</small>

1. Pobierz firmware U-Boot [tutaj](https://dl.gl-inet.com/){target="_blank"} na swój komputer.

    Niektóre modele oferują dwa warianty firmware. Pobierz wersję zgodną z U‑Boot.

2. Wyłącz router. Podłącz komputer do **portu Ethernet LAN** routera i pozostaw wszystkie pozostałe porty niepodłączone.

    !!! note

        W niektórych modelach określony port LAN można przełączyć na WAN. Nie używaj tego portu LAN do wgrywania firmware. Na przykład w modelu GL-MT6000 (Flint 2) nie używaj portu LAN 1. Zamiast tego użyj LAN 2, LAN 3 lub LAN 4.

3. Naciśnij i mocno przytrzymaj przycisk Reset, **jednocześnie włączając router**. Jeśli router nie ma przycisku zasilania, podłączenie zasilania automatycznie go uruchomi.

    Poczekaj, aż dioda LED kilka razy zamiga w regularnej sekwencji. Zwolnij przycisk Reset **po** zmianie wzoru migania.

    !!! note "Sekwencje migania LED według modelu urządzenia"

        **Uwaga:** Identyczne modele routerów z różnych partii produkcyjnych mogą mieć inne kolory diod LED lub sekwencje migania. Nie wpływa to na proces odzyskiwania przez U-Boot. Zwróć uwagę przede wszystkim na zmianę stanu migania diody LED.
        
        - Dla **GL-MT3600BE (Beryl 7)**: niebieska dioda LED miga 7 razy, a następnie świeci ciągłym białym światłem.
        
        - Dla **GL-MT5000 (Brume 3)**: dioda Power miga na niebiesko 7 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-BE6500 (Flint 3e)**: niebieska dioda LED miga 6 razy, a następnie świeci ciągłym białym światłem.
        
        - Dla **GL-BE9300 (Flint 3)**: niebieska dioda LED miga 6 razy, a następnie świeci ciągłym białym światłem.
        
        - Dla **GL-BE3600 (Slate 7)**: po przytrzymaniu przycisku Reset przez około 5 sekund na ekranie dotykowym pojawi się 5-sekundowe odliczanie. Nadal przytrzymuj przycisk Reset, aż na ekranie pojawi się kolejny komunikat, np. aby ręcznie ustawić adres IP komputera na 192.168.1.2 i odwiedzić w przeglądarce adres http://192.168.1.1. Następnie przejdź do kroku 4.

        - Dla **GL-X2000 (Spitz Plus)**: dioda Internet miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.

        - Dla **GL-B3000 (Marble)**: niebieska dioda LED miga 7 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-MT6000 (Flint 2)**: niebieska dioda LED miga 6 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-MT3000 (Beryl AX)**: niebieska dioda LED miga 6 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-MT2500/GL-MT2500A (Brume 2)**: dioda Power miga na niebiesko 5 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-X3000 (Spitz AX)**: dioda Internet miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.

        - Dla **GL-XE3000 (Puli AX)**: dioda Internet miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.
            
        - Dla **GL-XE300 (Puli)**: dioda LAN miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.

        - Dla **GL-E750 (Mudi)**: na ekranie najpierw zostanie wyświetlone „Booting”, następnie „Reset Counting 1 to 4”, a na końcu „Please Open Web 192.168.1.1”.

        - Dla **GL-X750 (Spitz)**: dioda Internet miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.

        - Dla **GL-AX1800 (Flint)**: niebieska dioda LED miga 5 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-AXT1800 (Slate AX)**: niebieska dioda LED miga 5 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-SFT1200 (Opal)**: niebieska dioda LED miga 5 razy, a następnie świeci ciągłym białym światłem.

        - Dla **GL-MT1300 (Beryl)**: niebieska dioda LED najpierw miga dwa razy wolno, następnie 5 razy szybciej i potem świeci ciągłym białym światłem.

        - Dla **GL-A1300 (Slate Plus)**: dioda LED miga wolno 5 razy, następnie przez chwilę świeci, po czym zaczyna stale szybko migać.

        - Dla **GL-MT300N-V2 (Mango)** i **GL-AR300M (Shadow)**: dioda LED miga 5 razy. 

        - Dla **GL-X300B (Collie)**: dioda WAN miga 5 razy, a następnie dioda Wi-Fi pozostaje włączona.

        - Dla **GL-AP1300 (Cirrus)**: dioda zasilania miga wolno 5 razy, następnie przez chwilę świeci, po czym zaczyna stale szybko migać.

        - Dla **GL-B1300 (Convexa-B)** i **GL-S1300 (Convexa-S, EOL)**: dioda LED miga 4 razy.
            
            Skrajna lewa dioda Power przez cały czas pozostaje włączona, podczas gdy skrajna prawa dioda Wi-Fi miga 4 razy, a następnie środkowa dioda Mesh zaczyna świecić światłem ciągłym.
            
            (W przypadku niektórych starszych egzemplarzy GL-B1300 skrajna lewa dioda Power przez cały czas pozostaje włączona, a zarówno środkowa dioda, jak i skrajna prawa dioda migają jednocześnie 5 razy, po czym pozostają włączone.)

        - Dla **GL-B2200 (Velica)**: obie diody początkowo świecą na niebiesko, następnie zmieniają kolor na biały i migają 5 razy, po czym znów świecą ciągłym niebieskim światłem.

        - Dla **GL-SF1200**: dioda 5G miga 5 razy, a następnie pozostaje włączona.

        - Dla **GL-S200**: cyjanowa dioda LED miga 5 razy, następnie na krótko zmienia kolor na fioletowy, po czym świeci ciągłym cyjanowym światłem.
        
        - Dla **GL-AR750 (Creta)** i **GL-AR750S-EXT (Slate)**: dioda LED miga 5 razy. 
        
        - Dla **GL-USB150 (Microuter)**, **microuter-N300** i **GL-AR150 (White)**: dioda LED miga 5 razy.

        - Dla **GL-MV1000/GL-MV1000W (Brume)**: brak powtarzającego się sygnału migania diody LED. Diody Power i WAN pozostają przez cały czas włączone.
        
        - Dla **GL-MiFi**: dioda LED miga 6 razy.

        - Dla **GL-MT300N** i **GL-MT300A**: dioda LED miga 3 razy.

4. Ręcznie ustaw adres IP komputera na **192.168.1.2**. Poniżej znajdziesz instrukcje krok po kroku dla różnych systemów operacyjnych:

    ??? "Windows 7 / Windows 10"

        1. Przejdź do **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Kliknij prawym przyciskiem myszy **Local Area Connection** -> **Properties**.

        3. Kliknij **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Ręcznie ustaw **IP adress** na `192.168.1.2`.

        5. Ustaw **Subnet mask** na `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Kliknij przycisk **OK**.

    ??? "Windows 11"

        7. Otwórz Settings.

        8. Kliknij **Network & Internet**.

        9. Kliknij kartę **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. W sekcji "IP assignment" kliknij przycisk **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Wybierz opcję **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Włącz przełącznik **IPv4**.

        13. Ustaw statyczny **IP address** na **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Określ **Subnet mask** jako **255.255.255.0**.

        15. Kliknij przycisk **Save**.

    ??? "macOS"
    
        16. Kliknij ikonę **Apple** w lewym górnym rogu ekranu i wybierz **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Kliknij **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Kliknij po lewej stronie **Ethernet**, a następnie kliknij listę rozwijaną obok **Configure IPv4** i wybierz **Manually**. Jeśli używasz adaptera USB-Ethernet, pozycja Ethernet może nie być widoczna i zamiast niej może pojawić się nazwa tego adaptera.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Wprowadź **IPv4 Address** jako `192.168.1.2`, **Subnet Mask** jako `255.255.255.0`, **Router** jako `192.168.1.1`, a następnie kliknij przycisk Apply w prawym dolnym rogu.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. W przeglądarce odwiedź adres **http://192.168.1.1**. To jest interfejs U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note 
    
        - Jeśli nie możesz uzyskać dostępu do interfejsu U-Boot Web UI, sprawdź, czy nie działa u Ciebie oprogramowanie VPN lub proxy. Wyłącz wszelkie programy VPN i proxy, w tym Tailscale i ZeroTier.
    
        - Powyższy interfejs U-Boot Web UI może nie wyglądać dokładnie tak samo jak u Ciebie, ponieważ wersja U-Boot różni się w zależności od daty produkcji. W niektórych skrajnych przypadkach zalecamy aktualizację wersji U-Boot. Zapoznaj się z samouczkiem [tutaj](upgrade_uboot_version.md).

6. Kliknij przycisk **Choose file**, aby wskazać plik firmware. Następnie kliknij przycisk **Update firmware**.

7. Poczekaj około 3 minut. Nie odłączaj zasilania urządzenia podczas aktualizacji firmware. 

    Router jest gotowy, gdy dioda LED nadal miga na niebiesko; w przypadku niektórych modeli komórkowych jest gotowy wtedy, gdy zarówno dioda Power, jak i Wi‑Fi świecą światłem ciągłym.

8. Przywróć ustawienia IP zmienione w kroku 4 i połącz komputer z routerem przez LAN lub Wi-Fi. Ponownie uzyskasz dostęp do panelu administracyjnego routera pod adresem **192.168.8.1**.

    **Uwaga:** Aby uzyskać dostęp do routera, może być konieczne użycie trybu incognito albo usunięcie pamięci podręcznej i plików cookie przeglądarki.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
