# Serwer WireGuard na moim routerze GL.iNet nie działa prawidłowo

Istnieje kilka powodów, dla których serwer WireGuard skonfigurowany na routerze GL.iNet może nie działać prawidłowo.

Jeśli napotkasz problem, wykonaj poniższe kroki diagnostyczne odpowiednio do swojej sytuacji.

#### Sytuacja 1: Serwer WireGuard uruchamia się, ale nie można się z nim połączyć

??? "Wykonaj te kroki"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Przekierowanie portów skonfigurowane na routerze głównym podłączonym do routera dodatkowego (GL.iNet) może nie działać prawidłowo. 
    Aby sprawdzić, czy przekierowanie portów działa poprawnie, spróbuj przekierować port HTTPS routera głównego do serwera WireGuard. Wykonaj poniższe kroki:

    1. Przekieruj port HTTPS routera głównego do serwera WireGuard

        1. Zaloguj się do panelu administracyjnego routera głównego. 
        2. Przejdź do ekranu przekierowania portów. 
        3. Utwórz nowy port i nazwij go **HTTPS**. 
        4. Wprowadź następujące informacje:
            * **External port/Internal port:** wpisz **443**. 
            * **Protocol:** wybierz **All** lub **UDP/TCP**.
            * **Internal IP** (lub widoczne jako **Host IP**): wpisz adres WAN IP routera dodatkowego albo wybierz router dodatkowy z listy rozwijanej, jeśli taka opcja jest dostępna.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Włącz DDNS i zdalny dostęp HTTPS (na routerze GL.iNet)

        1. W przeglądarce wpisz adres URL panelu administracyjnego routera GL.iNet (np. 192.168.8.1) i zaloguj się.
        2. Na lewym pasku bocznym kliknij **Applications** > **Dynamic DNS**. 
        3. Włącz **Enable DDNS** i zaznacz pole **I have read and agree to the Terms of Service & Privacy Policy**. 
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Zapisz gdzieś nazwę hosta, ponieważ będzie potrzebna później, a następnie kliknij **Apply**. 
        5. Na lewym pasku bocznym kliknij **System** > **Security**. 
        6. W sekcji **Remote Access Control** włącz **HTTPS Remote Access**.  
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Kliknij **Apply**. 

    3. Sprawdź, czy możesz uzyskać dostęp do panelu administracyjnego routera GL.iNet 

        1. Na innym urządzeniu (np. laptopie lub telefonie) połącz się z inną siecią Wi-Fi albo z siecią komórkową. 
        2. W pasku adresu przeglądarki wpisz wcześniej zapisaną nazwę hosta (abcd123.glddns.com). 
        3. Kliknij **Advanced**. 
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Kliknij **Proceed to abcd123.glddns.com(unsafe)**. 
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Jeśli zobaczysz ekran logowania routera GL.iNet (routera dodatkowego), oznacza to, że przekierowanie portów skonfigurowane na routerze głównym działa prawidłowo.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Jeśli nie widzisz ekranu logowania routera GL.iNet (routera dodatkowego), przekierowanie portów nie działa prawidłowo. Skonfiguruj je ponownie albo upewnij się, że jako router główny używasz urządzenia z poprawnie działającą funkcją przekierowania portów. 

#### Sytuacja 2: Serwer WireGuard pokazuje, że klient VPN jest połączony, ale klient VPN nie ma dostępu do Internetu

??? "Wykonaj te kroki"

    Wykonaj poniższe kroki dla każdej możliwej przyczyny i sprawdzaj, czy problem został rozwiązany. Jeśli problem zniknie, możesz pominąć resztę sekcji. 

    **Możliwa przyczyna 1: Twój dostawca usług internetowych może nie być w stanie rozwiązywać serwerów DNS GL.iNet**

    Spróbuj ręcznie skonfigurować adresy serwerów DNS, wykonując poniższe kroki: 

    1. W przeglądarce wpisz adres URL panelu administracyjnego routera GL.iNet (np. 192.168.8.1) i zaloguj się.
    2. Na lewym pasku bocznym kliknij **Network** > **DNS**. 
    3. Dla **Mode** wybierz **Manual DNS**. 
    4. Dla **DNS Server 1** wybierz **Google Public DNS**. 
    5. Kliknij **Apply**. 

    **Możliwa przyczyna 2: Adres IP bramy routera głównego koliduje z adresem IP serwera WireGuard**

    Spróbuj zmienić adres IPv4, wykonując poniższe kroki: 

    1. W przeglądarce wpisz adres URL panelu administracyjnego routera GL.iNet (np. 192.168.8.1) i zaloguj się.
    2. Na lewym pasku bocznym kliknij **VPN** > **WireGuard Server**. 
    3. Na karcie **Configuration** w polu **IPv4 Address** wpisz nowy adres IP (np. 10.1.0.1/24). 
    4. Kliknij **Apply**. 

    **Możliwa przyczyna 3: Jeśli zarówno serwer WireGuard, jak i klient WireGuard zostały skonfigurowane na routerach GL.iNet, ich adresy LAN IP kolidują ze sobą**

    Spróbuj zmienić adres LAN IP na jednym z routerów, wykonując poniższe kroki:     

    1. W przeglądarce zaloguj się do panelu administracyjnego jednego z routerów GL.iNet (np. 192.168.8.1). 
    2. Na lewym pasku bocznym kliknij **Network** > **LAN**. 
    3. W polu **Router IP address** wpisz nowy adres LAN IP (np. 192.168.10.1). 
    4. Kliknij **Apply**. 

    **Możliwa przyczyna 4: Adres IP serwera WireGuard został zaktualizowany, ale brakuje maski podsieci**

    Dodaj maskę podsieci do adresu IP serwera WireGuard, wykonując poniższe kroki: 

    1. W przeglądarce wpisz adres URL panelu administracyjnego routera GL.iNet (np. 192.168.8.1) i zaloguj się.
    2. Na lewym pasku bocznym kliknij **VPN** > **WireGuard Server**. 
    3. Na karcie **Configuration** w polu **IPv4 Address** dodaj **/24** po **10.0.0.1**. 
    4. Kliknij **Apply**. 

#### Sytuacja 3: Serwer WireGuard działa, ale nie mogę połączyć z nim klienta VPN

??? "Wykonaj te kroki"

    Wykonaj poniższe kroki dla każdej możliwej przyczyny i sprawdzaj, czy problem został rozwiązany. Jeśli problem zniknie, możesz pominąć resztę sekcji. 

    **Możliwa przyczyna 1: Przekierowanie portów skonfigurowane na routerze głównym może nie działać prawidłowo**

    Aby sprawdzić, czy działa poprawnie, spróbuj przekierować port HTTPS do serwera WireGuard, wykonując kroki rozwiązania opisane w Sytuacji 1. 

    **Możliwa przyczyna 2: Możesz nie mieć publicznego adresu IP**

    Aby to sprawdzić, skorzystaj z instrukcji na tej [stronie](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/). 

    **Możliwa przyczyna 3: Jeśli zarówno serwer WireGuard, jak i klient WireGuard zostały skonfigurowane na routerach GL.iNet, ich adresy LAN IP kolidują ze sobą**

    Zmień adres LAN IP na jednym z routerów, wykonując poniższe kroki: 

    1. W przeglądarce zaloguj się do panelu administracyjnego jednego z routerów GL.iNet (np. 192.168.8.1). 
    2. Na lewym pasku bocznym kliknij **Network** > **LAN**. 
    3. W polu **Router IP address** wpisz nowy adres LAN IP (np. 192.168.10.1). 
    4. Kliknij **Apply**. 

    **Możliwa przyczyna 4: Urządzenie, którego używasz do połączenia z serwerem WireGuard, jest podłączone do jego sieci Wi-Fi albo do jego portu LAN** 

    Podłącz urządzenie do innej sieci Wi-Fi albo do sieci komórkowej. 

    **Możliwa przyczyna 5: W pliku konfiguracyjnym przesłanym na urządzenie klienckie mogą brakować niektórych wierszy**

    Wgraj ponownie dane konfiguracyjne. 

#### Sytuacja 4: Serwer WireGuard jest połączony, ale połączenie nie jest stabilne

??? "Wykonaj te kroki"

    Wykonuj poniższe kroki po kolei, aby rozwiązać problem. Po każdym kroku sprawdzaj, czy problem został rozwiązany. Jeśli tak się stanie, możesz pominąć dalsze kroki.

    1. Na urządzeniu klienta VPN zmień wartość MTU z **1420** na mniejszą (np. **1380**).
    2. Na routerze głównym włącz funkcję VPN passthrough, jeśli jest dostępna. 
    3. Spróbuj ręcznie skonfigurować serwery DNS na routerze GL.iNet, wykonując poniższe kroki: 
        1. W przeglądarce wpisz adres URL panelu administracyjnego routera GL.iNet (np. 192.168.8.1) i zaloguj się.
        2. Na lewym pasku bocznym kliknij **Network** > **DNS**. 
        3. Dla **Mode** wybierz **Manual DNS**. 
        4. Dla **DNS Server 1** wybierz **Google Public DNS**. 
        5. Kliknij **Apply**. 

#### Sytuacja 5: Serwer WireGuard nagle przestał działać

??? "Wykonaj te kroki"

    Wykonaj poniższe kroki dla każdej możliwej przyczyny i sprawdzaj, czy problem został rozwiązany. Jeśli problem zniknie, możesz pominąć resztę sekcji. 

    **Możliwa przyczyna 1: W miejscu, w którym skonfigurowano serwer WireGuard, mogła wystąpić przerwa w dostawie prądu**

    Sprawdź, czy serwer WireGuard nadal jest online, wykonując kroki rozwiązania z Sytuacji 1 lub przez [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/) (jeśli wcześniej połączono z nim router).

    **Możliwa przyczyna 2: Nie włączono Dynamic DNS (DDNS)**

    Jeśli masz dynamiczny adres IP (co jest bardzo prawdopodobne), musisz włączyć DDNS. [Włącz DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) i wykonaj pozostałe kroki, aby ponownie skonfigurować serwer WireGuard. 

    **Możliwa przyczyna 3: Przekierowanie portów przestało działać z nieznanych przyczyn**

    Skonfiguruj [przekierowanie portów](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) ponownie, używając innego portu. 

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
