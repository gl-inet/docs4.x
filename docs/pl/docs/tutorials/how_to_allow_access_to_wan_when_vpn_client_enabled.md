# Jak zezwolić na dostęp do WAN, gdy klient VPN jest włączony?

Gdy klient VPN jest włączony na routerach GL.iNet, w domyślnym trybie globalnym urządzenia LAN nie mogą uzyskać dostępu do lokalnych urządzeń lub usług WAN, ponieważ cały ruch z sieci LAN jest kierowany przez tunel VPN, a nie przez sieć nadrzędną (WAN), aby uniknąć wycieków DNS.

Ten samouczek wprowadza kroki umożliwiające udostępnienie lokalnych usług WAN (np. drukarki, NAS itp.) dla urządzeń LAN klienta VPN.

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Dla firmware v4.7 i wcześniejszych

Zaloguj się do panelu administracyjnego swojego klienta VPN i przejdź do **VPN** -> **VPN Dashboard** -> **VPN Client**. Kliknij **Global Options** w prawym górnym rogu.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Włącz **Allow Access WAN** i kliknij **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Jeśli ta opcja jest włączona, podczas gdy VPN jest podłączony, urządzenia klienckie nadal będą mogły uzyskać dostęp do usług WAN w podsieci nadrzędnej, np. drukarki, NAS itp.

## Dla firmware v4.8 i nowszych

Opcja **Allow Access WAN** została usunięta z VPN Dashboard w firmware v4.8. Ale możesz uzyskać dostęp do lokalnej sieci WAN za pomocą polityki VPN.

Wykonaj poniższe kroki.

1. Zaloguj się do panelu administracyjnego swojego klienta VPN i przejdź do **VPN** -> **VPN Dashboard**. 

    Kliknij tryb w prawym górnym rogu.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Przełącz na **Policy Mode** i kliknij **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    Strona zostanie odświeżona i wyświetlona jak poniżej.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Kliknij środkowe pole, aby ustawić cel tunelu.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Wybierz **Exclude Speficied Domain / IP**, wprowadź podsieć WAN swojego routera, a następnie kliknij **Apply**.

    Zapewnia to, że cały ruch do podsieci WAN jest kierowany przez lokalną sieć WAN, a nie przez tunel VPN.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    Tutaj jako przykład użyjemy podsieci 192.168.0.1/24. Wprowadź tę podsieć i zatwierdź, a tunel VPN zostanie wyświetlony jak poniżej.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Jak sprawdzić podsieć WAN mojego routera GL.iNet?"
    
        Podsieć WAN routera GL.iNet zwykle można znaleźć na stronie INTERNET. Jest ona określana przez urządzenie nadrzędne, do którego podłączony jest interfejs WAN routera (np. modem ISP lub brama nadrzędna).

        Na przykład, jeśli router działa jako router drugorzędny (gdzie jego port WAN jest podłączony do innej sieci lokalnej, takiej jak modem ISP lub port LAN routera głównego), a adres IP WAN routera to 192.168.1.165, brama to 192.168.1.1, a maska podsieci to 255.255.255.0 (powszechna maska dla małych sieci), to odpowiednia podsieć WAN to 192.168.1.0/24. Jest to również podsieć LAN urządzenia nadrzędnego.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Uwaga**: Długość prefiksu 192.168.1.0/24 wynosi 24, co odpowiada masce podsieci 255.255.255.0. Jeśli maska podsieci WAN routera nie jest 255.255.255.0, długość prefiksu podsieci WAN nie wynosi "/24". Potwierdź podsieć WAN na podstawie rzeczywistej konfiguracji WAN.

3. Kliknij prawe pole, aby ustawić działanie tunelu (tj. użyj VPN lub nie używaj VPN).

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Wybierz **Use VPN** i wybierz plik konfiguracyjny VPN. Następnie kliknij **Apply**.
    
    Jeśli nie ma dostępnej konfiguracji, najpierw prześlij jedną, aby ustawić router jako klient VPN. Następnie przejdź do tej strony, wybierz Use VPN i wybierz plik konfiguracyjny VPN. Następnie kliknij Apply.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Przełącz przełącznik w prawym górnym rogu, aby włączyć ten tunel VPN. Rozpocznie się łączenie.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Poczekaj kilka minut. Po pomyślnym połączeniu zmieni się na zielony.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Wyszukaj swój publiczny adres IP, aby przetestować połączenie VPN. Na przykład otwórz przeglądarkę i odwiedź [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Pokaże Twój publiczny adres IP i lokalizację, jak pokazano poniżej. 

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Uzyskaj dostęp do urządzeń lub usług w podsieci WAN i sprawdź, czy możesz uzyskać dostęp pomyślnie.

    Możesz użyć polecenia ping, aby przetestować łączność. 

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.