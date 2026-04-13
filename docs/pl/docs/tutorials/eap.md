# Jak połączyć routery GL.iNet z siecią EAP

Niektóre routery GL.iNet obsługują łączenie z sieciami Wi-Fi EAP (Extensible Authentication Protocol).

EAP to framework uwierzytelniania powszechnie używany z **uwierzytelnianiem 802.1X** w sieciach **WPA2‑Enterprise / WPA3‑Enterprise**. Typowym przykładem jest **eduroam** — globalna usługa roamingu Wi-Fi dla edukacji i badań, która opiera się na 802.1X oraz EAP.

W tym przewodniku przedstawiamy dwa sposoby połączenia routerów GL.iNet z siecią Wi-Fi EAP: przez Panel Administracyjny oraz przez LuCI.

## Obsługiwane modele

??? "Obsługiwane modele"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-SFT1200 (Opal)

    **Uwaga:** 
    
    1. GL-MT6000 (Flint 2) i GL-MT3000 (Beryl AX) nie obsługują połączeń z sieciami EAP na domyślnym firmware, ale GL.iNet udostępnia dla tych modeli natywny firmware OpenWrt 24, który można zainstalować, aby uzyskać obsługę połączeń z sieciami EAP. Wyszukaj model w [Download Center](https://dl.gl-inet.com/){target="_blank"} i przejdź do zakładki OPENWRT 24, aby uzyskać więcej informacji.

    2. GL-SFT1200 (Opal) obsługuje połączenia z sieciami EAP na firmware v4.8.

??? "Nieobsługiwane modele"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Łączenie przez panel administracyjny

1. Zaloguj się do panelu administracyjnego, przejdź do **INTERNET** -> **Repeater**, a następnie kliknij **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Router przeskanuje dostępne sieci. Znajdź i wybierz SSID EAP, z którym chcesz się połączyć.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Możesz też kliknąć **Join Other Network** w prawym górnym rogu, aby ręcznie dołączyć do sieci EAP.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Wprowadź **SSID**.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Wybierz **Security** jako WPA/WPA2/WPA3 Enterprise.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Wprowadź **Username** i **Password**, a następnie kliknij **Apply**, aby się połączyć.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Łączenie przez LuCI

Panel administracyjny GL.iNet obsługuje tylko ograniczoną liczbę typów EAP.

Jeśli nie możesz połączyć się z docelową siecią EAP przez panel administracyjny, spróbuj skorzystać z interfejsu LuCI.

1. Zaloguj się do panelu administracyjnego, przejdź do **SYSTEM** -> **Advanced Settings**. Zainstaluj LuCI i kliknij **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Zaloguj się do interfejsu LuCI przy użyciu tego samego hasła administratora i przejdź do Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Kliknij **Scan** w sekcji 2.4G lub 5G.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Dołącz do wybranej sieci.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Rozwiązywanie problemów

Jeśli docelowa sieć EAP wymaga dodatkowych parametrów, takich jak typ EAP (np. PEAP, TTLS), dopasowanie sufiksu domeny, tożsamość, anonimowa tożsamość itp., połączenie EAP przez panel administracyjny może się nie powieść.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

Wykonaj poniższe kroki, aby połączyć router GL.iNet z siecią EAP, która wymaga zaawansowanych ustawień, przy użyciu interfejsu LuCI.

1. Uzyskaj konfigurację.

    Przygotuj wcześniej parametry konfiguracyjne docelowej sieci EAP. Na przykład: 

    - Typ EAP (np. PEAP, TTLS, TLS)
    - Sufiks domeny uwierzytelniania (np. @company.com)
    - Tożsamość (zwykle pełna nazwa użytkownika)
    - Anonimowa tożsamość (opcjonalnie)
    - Typ uwierzytelniania wewnętrznego (np. MSCHAPv2, PAP)
    - Certyfikat CA (jeśli jest wymagany, przygotuj plik w formacie .crt)

    To przykład konfiguracji Xfinity Mobile Wi-Fi do celów poglądowych.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Zaloguj się do LuCI.

    Zaloguj się do panelu administracyjnego routera. Jeśli wcześniej próbowano połączyć się z docelową siecią EAP przez WebGUI, ale połączenie się nie powiodło, anuluj to połączenie.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

    Następnie przejdź do **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Zaloguj się do LuCI przy użyciu tego samego hasła administratora.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Skonfiguruj repeater w LuCI.

    W interfejsie LuCI przejdź do Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

    Kliknij przycisk **Scan** w sekcji 5G lub 2.4G, aby wyszukać dostępne sieci Wi-Fi.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

    Znajdź docelową sieć EAP w wynikach skanowania i kliknij **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

    Na stronie "Joining Network" wprowadź **WPA passphrase** i kliknij przycisk **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

    Zostaniesz przekierowany do konfiguracji Wireless Client. 

4. Odszukaj **Interface Configuration** -> **Wireless Security**. 

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

    Wybierz lub wprowadź prawidłowe parametry konfiguracyjne zgodnie z wymaganiami docelowej sieci EAP, jak pokazano poniżej. **Nie klikaj jeszcze Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

5. Przełącz się na kartę **Advanced Settings**, określ nazwę interfejsu, na przykład **wlan0**. Następnie kliknij **Save** w prawym dolnym rogu.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

6. Wrócisz do strony Wireless, na której będą widoczne oczekujące zmiany. Kliknij przycisk **Save & Apply** w prawym dolnym rogu.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

    Router pomyślnie połączy się z docelową siecią EAP.

7. Zweryfikuj połączenie.

    ??? "Sprawdzenie połączenia w WebGUI"

        Gdy router pomyślnie połączy się z docelową siecią EAP, w WebGUI podświetli się ikona repeatera, jak pokazano poniżej.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

        **Uwaga**: Ponieważ konfiguracja w LuCI nie jest synchronizowana z konfiguracją w WebGUI, szczegóły interfejsu repeatera (np. połączony adres IP, brama itp.) nie będą wyświetlane w WebGUI.
        
        Jak widać na ilustracji, sekcja repeatera na dole jest pusta. Router jest jednak już połączony z docelową siecią EAP jako repeater, ponieważ ikona repeatera u góry jest podświetlona.

    ??? "Sprawdzenie połączenia przez SSH"

        1. Zaloguj się do routera przez [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Wpisz **ifconfig** i naciśnij Enter.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

            Będzie można sprawdzić stan interfejsu **wlan0**.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.

