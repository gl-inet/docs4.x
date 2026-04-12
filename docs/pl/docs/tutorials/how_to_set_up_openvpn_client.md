# Jak skonfigurować klienta OpenVPN na routerach GL.iNet

Ten poradnik pokaże, jak skonfigurować klienta OpenVPN na routerach GL.iNet.

Obejrzyj ten film lub zapoznaj się z poniższymi krokami.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Przed rozpoczęciem upewnij się, że posiadasz aktywną subskrypcję u dostawcy usługi VPN obsługującego ręczną konfigurację OpenVPN. Kliknij [tutaj](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, aby sprawdzić dostawców OpenVPN kompatybilnych z GL.iNet.

Poniżej znajdują się kroki konfiguracji klienta OpenVPN przez panel administratora routera.

## 1. Zaloguj się do routera

Otwórz przeglądarkę internetową i uzyskaj dostęp do panelu administratora routera (domyślne IP: 192.168.8.1). Zaloguj się swoim hasłem administratora.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Skonfiguruj klienta VPN

Zapoznaj się z sekcją odpowiadającą dostawcy usługi VPN, którego używasz.

??? "NordVPN"

    1. W panelu administratora routera przejdź do **VPN** > **OpenVPN Client**.

    2. Kliknij **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Wprowadź dane uwierzytelniające usługi, następnie kliknij **Save and Continue**. 

        Uwaga: To NIE są dane logowania do konta (e-mail/hasło), lecz dane uwierzytelniające usługi uzyskane ze strony NordVPN -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. W oknie dialogowym wybierz lokalizacje VPN, z którymi chcesz się połączyć, następnie kliknij **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Wybierz serwer VPN, z którym chcesz się połączyć, kliknij ikonę trzech kropek i **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Inni dostawcy usług VPN (np. Surfshark)"

    1. W panelu administratora routera przejdź do **VPN** > **OpenVPN Client**.

    2. Kliknij **Add Manually**. 

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Ustaw nazwę. Możesz wprowadzić nazwę swojego dostawcy usługi VPN, następnie kliknij ikonę zaznaczenia. 

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Upewnij się, że pobrałeś plik konfiguracyjny dostarczony przez dostawcę usługi VPN oraz dane uwierzytelniające, jeśli są wymagane.  
    5. Prześlij pobrany plik konfiguracyjny. 
    
        Wprowadź dane uwierzytelniające usługi, jeśli są wymagane, następnie kliknij **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Obok adresu serwera VPN kliknij ikonę trzech kropek i **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Sprawdź połączenie VPN

Otwórz przeglądarkę internetową i wyszukaj swój adres IP oraz lokalizację. Jeśli zgadzają się one z adresem IP serwera VPN (zamiast adresu IP dostawcy usług internetowych) oraz lokalizacją, połączenie VPN zostało nawiązane pomyślnie.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.