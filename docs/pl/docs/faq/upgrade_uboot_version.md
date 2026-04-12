# Aktualizacja wersji U-Boot

## Ostrzeżenie

**Aktualizacja U-Boot jest bardzo ryzykowna i zasadniczo nie jest zalecana. Jeśli się nie powiedzie, urządzenie zostanie uszkodzone i nie będzie możliwości jego przywrócenia. Wykonuj ją tylko wtedy, gdy jest to konieczne lub gdy zaleci to wsparcie GL.iNet**.

**NIE wyłączaj zasilania podczas procesu aktualizacji, ponieważ może to spowodować niepowodzenie aktualizacji i uszkodzenie urządzenia**.

## Przygotowanie

- Komputer z portem Ethernet. Jeśli go nie masz, przygotuj dodatkowy adapter USB Ethernet.
- Kabel Ethernet.
- Pobierz plik U-Boot zgodnie z instrukcjami zespołu wsparcia GL.iNet. Upewnij się, że używasz właściwego pliku U-Boot. Jeśli nie wiesz, jak pobrać plik U-Boot, skontaktuj się z nami mailowo pod adresem support@gl-inet.com.

## Kroki aktualizacji

Wykonaj poniższe czynności, aby przejść do strony aktualizacji U-Boot.

1. Odłącz zasilanie routera. Podłącz komputer do portu **Ethernet LAN** routera. Wszystkie pozostałe porty **MUSZĄ** pozostać **niepodłączone**.

    !!! note

        W niektórych modelach wybrane porty LAN i port WAN są zamienne. Nie używaj tego portu LAN. Na przykład w modelu GL-MT6000 (Flint 2) nie używaj LAN 1. Zamiast tego użyj LAN 2, LAN 3 lub LAN 4.

2. Mocno naciśnij i przytrzymaj przycisk Reset, a jednocześnie włącz zasilanie routera. Jeśli router nie ma przycisku zasilania, podłączenie zasilania włączy go automatycznie.

    Następnie zobaczysz, jak dioda LED kilka razy miga w regularnej sekwencji. Zwolnij przycisk, gdy sekwencja się zmieni.
    
3. Ręcznie ustaw adres IP komputera na **192.168.1.2**. Poniżej znajdziesz instrukcję krok po kroku dla różnych systemów operacyjnych:

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

        14. Ustaw **Subnet mask** na **255.255.255.0**.

        15. Kliknij przycisk **Save**.

    ??? "macOS"

        16. Kliknij ikonę **Apple** w lewym górnym rogu ekranu i wybierz **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Kliknij **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Kliknij **Ethernet** po lewej stronie, a następnie kliknij listę rozwijaną obok **Configure IPv4** i wybierz **Manually**. Jeśli używasz adaptera USB Ethernet, pozycja Ethernet może nie być widoczna i zamiast niej może pojawić się nazwa adaptera USB Ethernet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Wprowadź **IPv4 Address** `192.168.1.2`, **Subnet Mask** `255.255.255.0`, **Router** `192.168.1.1`, a następnie kliknij przycisk Apply w prawym dolnym rogu.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Użyj Google Chrome/Microsoft Edge, aby otworzyć `http://192.168.1.1/uboot.html`**

    **NIE używaj Mozilla/Firefox, ponieważ może to uszkodzić router.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. Kliknij przycisk **Choose file** i wybierz pobrany plik U-Boot.

6. Kliknij przycisk **Update U-Boot**. NIE wyłączaj zasilania podczas procesu aktualizacji. Aktualizacja potrwa kilka minut. 

7. Po pomyślnej aktualizacji router uruchomi się ponownie. Następnie możesz przywrócić ustawienia IP z kroku 3 i spróbować uzyskać dostęp do panelu administracyjnego WWW pod adresem **192.168.8.1**. Jeśli możesz normalnie otworzyć panel administracyjny WWW, oznacza to, że router został ponownie uruchomiony.

    **Uwaga:** Aby uzyskać dostęp do routera, może być konieczne użycie trybu incognito albo usunięcie pamięci podręcznej i plików cookie przeglądarki.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
