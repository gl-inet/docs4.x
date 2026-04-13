# Jak uzyskać dostęp do podsieci LAN klienta WireGuard z serwera

Ten samouczek wprowadza kroki umożliwiające dostęp do podsieci LAN klienta WireGuard (takiego jak kamera IP, NAS itp.) ze strony serwera WireGuard.

## Topologia

Jak pokazano poniżej, GL-MT2500 jest serwerem WireGuard, a GL-AXT1800 jest klientem WireGuard podłączonym do niego. Możesz uzyskać dostęp do urządzeń po stronie LAN GL-AXT1800 (takich jak kamera IP lub NAS) ze strony serwera.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Dodaj regułę trasy na serwerze

??? "Dla firmware v4.7 i wcześniejszych"

    Zaloguj się do panelu administracyjnego <u>swojego serwera WireGuard</u>, a następnie przejdź do **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Kliknij ikonę trasy po prawej stronie, aby wejść w regułę trasy.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Kliknij **Add Route Rule** w prawym górnym rogu i wprowadź podsieć, do której chcesz uzyskać dostęp.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Na przykład podsieć LAN klienta WireGuard GL-AXT1800 to **192.168.8.0/24**, więc adres docelowy to **192.168.8.0/24**. 
    
    Brama to adres IP klienta, który Twój serwer WireGuard wygenerował dla tego klienta WireGuard. Możesz go znaleźć w zakładce **Profiles** na stronie **WireGuard Server**. Jak pokazano poniżej, adres IP klienta dla klienta WireGuard GL-AXT1800 to **10.0.0.4**.
    
    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}
    
    Więc ustaw bramę jako **10.0.0.4**, a zakres jako **global**, następnie kliknij **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Dla firmware v4.8 i nowszych"

    Zaloguj się do panelu administracyjnego <u>swojego serwera WireGuard</u>, a następnie przejdź do **VPN** -> **WireGuard Server**.

    Kliknij zakładkę **Route Rules** i kliknij **Add Route Rule** po prawej stronie.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    W wyskakującym oknie wprowadź podsieć, do której chcesz uzyskać dostęp.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Na przykład podsieć LAN klienta WireGuard GL-AXT1800 to **192.168.8.0/24**, więc adres docelowy to **192.168.8.0/24**. 
    
    Brama to adres IP klienta, który Twój serwer WireGuard wygenerował dla tego klienta WireGuard. Możesz go znaleźć w zakładce **Profiles** na tej samej stronie. Jak pokazano poniżej, adres IP klienta dla klienta WireGuard GL-AXT1800 to **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Więc ustaw bramę jako **10.1.0.2**, a następnie kliknij **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Zezwól na zdalny dostęp do LAN klienta

??? "Dla firmware v4.7 i wcześniejszych"

    Zaloguj się do panelu administracyjnego <u>swojego klienta WireGuard</u> i przejdź do **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Kliknij ikonę zębatki po prawej stronie WireGuard.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    W wyskakującym oknie włącz **Remote Access LAN**, a następnie kliknij **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Dla firmware v4.8 i nowszych"

    Zaloguj się do panelu administracyjnego <u>swojego klienta WireGuard</u> i przejdź do **VPN** -> **VPN Dashboard**.

    W lewym górnym rogu tunelu VPN kliknij ikonę zębatki, aby wejść w opcje tunelu.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    W wyskakującym oknie włącz **Allow Remote Access the LAN Subnet**, a następnie kliknij **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Przetestuj połączenie

Sprawdź, czy możesz uzyskać dostęp do urządzeń LAN klienta WireGuard ze strony serwera.

Możesz przetestować połączenie za pomocą polecenia ping. Na przykład na urządzeniu podłączonym do serwera WireGuard (GL-MT2500) wykonaj ping na adres IP urządzenia w sieci LAN klienta WireGuard (GL-AXT1800) i sprawdź, czy ping zakończy się powodzeniem.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
