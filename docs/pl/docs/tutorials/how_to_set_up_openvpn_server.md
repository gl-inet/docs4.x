# Jak skonfigurować serwer OpenVPN na routerach GL.iNet

Ten poradnik pokaże Ci, jak skonfigurować serwer OpenVPN na routerach GL.iNet. Serwer VPN pozwala nawiązać bezpieczne połączenie ze swoją siecią domową lub biurową zdalnie. Za pomocą routera GL.iNet możesz skonfigurować serwer OpenVPN w kilka minut.

!!! note "Przed rozpoczęciem upewnij się, że spełniasz poniższe wymagania"
    
    **Publiczny adres IP**

    Konfiguracja serwera OpenVPN wymaga publicznego adresu IP. Aby sprawdzić, czy go masz, zapoznaj się z [tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Przekierowanie portów**

    Jeśli router GL.iNet jest podłączony za głównym routerem, [skonfiguruj przekierowanie portów na głównym routerze](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Zaloguj się do routera

Otwórz przeglądarkę internetową i przejdź do panelu administracyjnego routera (domyślne IP: 192.168.8.1). Zaloguj się swoim hasłem administratora.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Włącz dynamiczny DNS (opcjonalnie)

Konfiguracja serwera OpenVPN zazwyczaj wymaga **statycznego publicznego adresu IP**, który zapewnia stały punkt końcowy dla innych urządzeń łączących się z serwerem VPN. 

Jeśli jednak nie masz statycznego publicznego adresu IP, np. masz adres dynamiczny, możesz włączyć **dynamiczny DNS (DDNS)** na swoim routerze GL.iNet. Umożliwia to ciągłe połączenie z serwerem OpenVPN, nawet gdy publiczny adres IP zmienia się dynamicznie.

Wykonaj poniższe kroki, aby włączyć dynamiczny DNS.

1. W panelu administracyjnym routera przejdź do **APPLICATIONS** > **Dynamic DNS**. 
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Włącz przełącznik **Enable DDNS**, przeczytaj i zaakceptuj **Terms of Service & Privacy Policy**, a następnie kliknij **Apply**. 
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Pobierz plik konfiguracyjny

1. W panelu administracyjnym routera przejdź do **VPN** > **OpenVPN Server**.
2. Kliknij **Generate Configuration**. 
3. Pozostaw domyślne ustawienia bez zmian, a następnie kliknij **Export Client Configuration**. 
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. W wyświetlonym oknie włącz przełącznik **Use DDNS Domain**, jeśli wcześniej skonfigurowałeś **Dynamic DNS**. 
5. Kliknij **Download**, a następnie zapisz plik. 
6. U góry strony **OpenVPN Server** kliknij **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Opcjonalnie) Aby uzyskać dostęp do sieci lokalnej serwera VPN, włącz te ustawienia:"
    
    Dla oprogramowania układowego v4.7 i wcześniejszych:

    1. Na lewym pasku bocznym kliknij **VPN** > **VPN Dashboard**. 
    2. Kliknij ikonę Options.
    3. Włącz przełącznik **Remote Access LAN**.
    4. Kliknij **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Dla oprogramowania układowego v4.8 i nowszych:

    1. Na lewym pasku bocznym kliknij **VPN** > **OpenVPN Server**.
    2. Kliknij **Options** w prawym górnym rogu.
    3. Włącz przełącznik **Allow Remote Access the LAN Subnet**.
    4. Kliknij **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Połącz się z serwerem OpenVPN

Aby połączyć się z serwerem OpenVPN, potrzebujesz klienta OpenVPN. Możesz go skonfigurować korzystając z jednej z poniższych metod:

??? "Metoda 1: Aplikacja klienta OpenVPN strony trzeciej (użyj tej metody, jeśli nie masz dodatkowego routera obsługującego konfigurację klienta OpenVPN)" 

    W tym poradniku użyjemy aplikacji OpenVPN Connect, oficjalnej aplikacji opracowanej przez OpenVPN Inc, jako przykładu. 

    1. Na innym urządzeniu połącz się z inną siecią Wi-Fi (lub połącz się z siecią komórkową, jeśli używasz urządzenia mobilnego).
    2. Wyślij pobrany wcześniej plik konfiguracyjny (np. e-mailem) na urządzenie, a następnie pobierz go na nie. 
    3. Pobierz OpenVPN Connect dla systemu operacyjnego swojego urządzenia:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. W aplikacji przeczytaj warunki użytkowania, a następnie wybierz **Agree**. 
    5. Wybierz **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Wybierz **Browse**, a następnie wybierz pobrany wcześniej plik konfiguracyjny. 
    7. Wybierz **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"} 
    8. Wybierz **Connect** > **OK** > **Allow**. 

    U góry profilu VPN zobaczysz słowo „Connected". 
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Metoda 2: Router obsługujący konfigurację klienta OpenVPN"

    Możesz użyć dowolnego routera obsługującego ręczną konfigurację klienta OpenVPN. W tym poradniku użyjemy routera podróżnego GL.iNet [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) jako przykładu. 

    1. Na innym urządzeniu połącz się z inną siecią Wi-Fi (lub połącz się z siecią komórkową, jeśli używasz urządzenia mobilnego). 
    2. W pasku adresu przeglądarki wprowadź adres URL do panelu administracyjnego routera (np. 192.168.8.1).
    3. Wprowadź hasło, a następnie kliknij **Login**. 
    4. Na lewym pasku bocznym kliknij **VPN** > **OpenVPN Client**. 
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"} 
    5. Kliknij **Add Manually**. 
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"} 
    6. Wprowadź nazwę w polu, a następnie kliknij ikonę zaznaczenia. 
    7. Prześlij pobrany wcześniej plik konfiguracyjny. 
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"} 
    8. Kliknij **Apply**. 
    9. Kliknij ikonę trzech kropek, a następnie kliknij **Start**. 
    10. Podłącz urządzenie do routera, na którym działa klient OpenVPN. 

## 5. Zweryfikuj połączenie VPN

Otwórz przeglądarkę internetową i wyszukaj swój adres IP oraz lokalizację. Jeśli zgadzają się one z adresem IP serwera VPN (zamiast adresu IP dostawcy internetowego) i lokalizacją, połączenie VPN działa pomyślnie.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
