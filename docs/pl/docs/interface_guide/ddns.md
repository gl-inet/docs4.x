# Dynamic DNS

Dynamic Domain Name Service (Dynamic DNS lub DDNS) to usługa służąca do mapowania nazwy domeny na dynamiczny adres IP urządzenia sieciowego. Dzięki Dynamic DNS możesz uzyskać zdalny dostęp do routera. Do korzystania z tej funkcji wymagany jest publiczny adres IP.

## Włączanie DDNS

Po lewej stronie panelu administracyjnego WWW przejdź do **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Włącz **Enable DDNS**, zaakceptuj **Terms of Services & Privacy Policy**, a następnie kliknij **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Kliknij **Security Settings** w prawym dolnym rogu.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

W wyskakującym oknie sprawdź, czy protokół zdalnego dostępu, którego chcesz używać, jest włączony. Jeśli nie, przejdź do **SYSTEM** -> **Security** -> **Remote Access Control**, aby go włączyć.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Włącz wybrany protokół zdalnego dostępu i kliknij **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Synchronizacja rekordów między serwerami DNS może opóźnić się nawet o 10 minut. Z tego powodu dostęp przez nazwę domenową DDNS może nie działać od razu po włączeniu usługi lub po zmianie publicznego adresu IP.

**Uwaga**: Jeśli jednocześnie włączysz DDNS i klient VPN, upewnij się, że opcja **Services From GL.iNet Use VPN** jest wyłączona. Tę funkcję znajdziesz w [VPN Client Options](vpn_dashboard.md#tunnel-options) na stronie VPN Dashboard.

## Sprawdzanie, czy DDNS działa

Działanie DDNS możesz sprawdzić za pomocą narzędzia DDNS Test albo ręcznie, używając poleceń.

=== "Korzystanie z narzędzia DDNS Test"

    Na stronie Dynamic DNS kliknij **DDNS Test**.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Upewnij się, że adres IP zwrócony podczas rozwiązywania domeny DDNS jest zgodny z adresem WAN routera. 
    
    Jeśli nie, u góry pojawi się żółty komunikat informujący, że router może znajdować się za NAT-em i trzeba skonfigurować przekierowanie portów na routerze nadrzędnym.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Sprawdzanie ręczne"

    1. Użyj polecenia `nslookup`, aby uzyskać mapowanie między nazwą domeny a adresem IP, jak pokazano poniżej.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Zastąp "xxxxxxx.glddns.com" z powyższego obrazu własną nazwą hosta. 
        
        "8.8.8.8" z powyższego obrazu to Google DNS. Możesz go użyć albo zastąpić innym serwerem DNS, a następnie nacisnąć Enter.

    2. Jeśli w wyniku otrzymasz publiczny adres IP, na przykład "103.81.180.10" jak na obrazie poniżej, oznacza to, że domena DDNS została pomyślnie zmapowana na publiczny adres IP.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        Na urządzeniu podłączonym do routera wyszukaj w przeglądarce frazę "what is my ip address" albo odwiedź stronę taką jak [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. Otrzymasz swój publiczny adres IP. Porównaj dwa adresy IP uzyskane w krokach 1 i 2. Jeśli są takie same, DDNS działa. W przeciwnym razie nie działa.

    3. Jeśli pojawi się komunikat `** server can't find xxxxxxx.glddns.com: NXDOMAIN`, jak pokazano poniżej, oznacza to, że rozwiązywanie domeny nie powiodło się i domena DDNS nie została pomyślnie zmapowana na publiczny adres IP.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## Zdalny dostęp HTTPS

!!! Note

    1. Do zdalnego dostępu HTTPS wymagany jest **Public IP**. 
    
        Kliknij [tutaj](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), aby sprawdzić, czy dostawca usług internetowych (ISP) przydziela Ci publiczny adres IP.
    
    2. Jeśli router znajduje się za NAT-em, skonfiguruj przekierowanie portów (port **443**) na routerze nadrzędnym dla dostępu HTTPS.

Aby włączyć zdalny dostęp HTTPS do routera, wykonaj poniższe kroki.

1. Na stronie Dynamic DNS włącz **Enable DDNS**, zaakceptuj **Terms of Services & Privacy Policy**, a następnie kliknij **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. W panelu administracyjnym WWW przejdź do **SYSTEM** -> **Security** -> **Remote Access Control**.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Włącz **HTTPS Remote Access** i kliknij **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Po włączeniu tej funkcji możesz uzyskać dostęp do panelu administracyjnego routera z dowolnego miejsca, używając nazwy hosta DDNS przez **HTTPS** (np. `https://xxxxxxx.glddns.com`). 

Jeśli skonfigurowano przekierowanie portów, uzyskasz dostęp pod adresem `https://xxxxxxx.glddns.com:external_port ` (zastąp external_port rzeczywistym numerem portu). 

**Uwaga**: Ta funkcja używa certyfikatów samopodpisanych, dlatego przeglądarka wyświetli komunikat **Your connection is not private** podczas uzyskiwania dostępu do panelu administracyjnego routera przez nazwę hosta DDNS i **HTTPS**, jak pokazano poniżej (port 8001 został użyty jako przykład).

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Aby kontynuować zdalny dostęp HTTPS, kliknij na dole **Advanced**.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Następnie kliknij **Proceed to xxxxxxx.glddns.com**, aby kontynuować.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Po wykonaniu tych kroków będzie można uzyskać dostęp do panelu administracyjnego WWW przy użyciu nazwy hosta DDNS przez HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Zdalny dostęp SSH

!!! Note

    1. Do zdalnego dostępu SSH wymagany jest **Public IP**. 
    
        Kliknij [tutaj](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), aby sprawdzić, czy dostawca usług internetowych (ISP) przydziela Ci publiczny adres IP.
    
    2. Jeśli router znajduje się za NAT-em, skonfiguruj przekierowanie portów (port **22**) na routerze nadrzędnym dla dostępu SSH.

Aby włączyć zdalny dostęp SSH do routera, wykonaj poniższe kroki.

1. Na stronie Dynamic DNS włącz **Enable DDNS**, zaakceptuj **Terms of Services & Privacy Policy**, a następnie kliknij **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. W panelu administracyjnym WWW przejdź do **SYSTEM** -> **Security** -> **Remote Access Control**.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Włącz **SSH Remote Access** i kliknij **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Po włączeniu tej funkcji możesz połączyć się z routerem z dowolnego miejsca, używając nazwy hosta DDNS przez **SSH** (np. `ssh root@xxxxxxx.glddns.com`). 

Jeśli skonfigurowano przekierowanie portów, użyj polecenia `ssh root@xxxxxxx.glddns.com:external_port` (zastąp external_port rzeczywistym numerem portu). 

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
