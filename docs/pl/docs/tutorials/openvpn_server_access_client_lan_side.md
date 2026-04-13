# Jak uzyskać dostęp do podsieci LAN klienta OpenVPN z serwera

Ten samouczek wprowadza kroki umożliwiające dostęp do podsieci LAN klienta OpenVPN (takiego jak NAS, kamera IP itp.) ze strony serwera OpenVPN.

## Topologia

Jak pokazano poniżej, GL-AXT1800 jest serwerem OpenVPN, a GL-MT2500 jest klientem OpenVPN podłączonym do niego. Możesz uzyskać dostęp do urządzeń po stronie LAN GL-MT2500 (takich jak NAS lub GL-MT3000, router podrzędny) ze strony serwera.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Dodaj regułę trasy na serwerze

??? "Dla firmware v4.7 i wcześniejszych"

    Zaloguj się do panelu administracyjnego <u>swojego serwera OpenVPN</u> i przejdź do **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Kliknij ikonę trasy po prawej stronie, aby wejść w regułę trasy.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    W wyskakującym oknie kliknij przycisk **Add Route Rule** po prawej stronie i wprowadź podsieć, do której chcesz uzyskać dostęp.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Na przykład podsieć LAN klienta OpenVPN GL-MT2500 to **192.168.48.0/24**, więc adres docelowy to **192.168.48.0/24**. 
    
    Brama to adres IP klienta, który Twój serwer OpenVPN wygenerował dla tego klienta OpenVPN. Tutaj ustawiamy bramę jako **10.8.0.1**, a następnie klikamy **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Uwaga: Jeśli masz wielu klientów OpenVPN, których podsieci LAN wymagają dostępu, zapoznaj się z [tym linkiem](reserve_fixed_IP_for_ovpn_client.md), aby zarezerwować adres IP klienta dla każdego klienta OpenVPN przed ustawieniem reguł tras.

??? "Dla firmware v4.8 i nowszych"

    Zaloguj się do panelu administracyjnego <u>swojego serwera OpenVPN</u> i przejdź do **VPN** -> **OpenVPN Server**.

    Kliknij zakładkę **Route Rules**, a następnie kliknij przycisk **Add Route Rule** po prawej stronie.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    W wyskakującym oknie wprowadź podsieć, do której chcesz uzyskać dostęp.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Na przykład podsieć LAN klienta OpenVPN GL-MT2500 to **192.168.48.0/24**, więc adres docelowy to **192.168.48.0/24**. 
    
    Brama to adres IP klienta, który Twój serwer OpenVPN wygenerował dla tego klienta OpenVPN. Tutaj ustawiamy bramę jako **10.8.0.2**, a następnie klikamy **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Uwaga: Jeśli masz wielu klientów OpenVPN, których podsieci LAN wymagają dostępu, zapoznaj się z [tym linkiem](reserve_fixed_IP_for_ovpn_client.md), aby zarezerwować adres IP klienta dla każdego klienta OpenVPN przed ustawieniem reguł tras.

## 2. Zezwól na zdalny dostęp do LAN klienta

??? "Dla firmware v4.7 i wcześniejszych"

    Zaloguj się do panelu administracyjnego <u>swojego klienta OpenVPN</u> i przejdź do **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Kliknij ikonę zębatki, aby wejść w opcje klienta.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    W wyskakującym oknie włącz **Remote Access LAN**, a następnie kliknij **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Dla firmware v4.8 i nowszych"

    Zaloguj się do panelu administracyjnego <u>swojego klienta OpenVPN</u> i przejdź do **VPN** -> **VPN Dashboard**.

    W lewym górnym rogu tunelu VPN kliknij ikonę zębatki, aby wejść w opcje tunelu.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    W wyskakującym oknie włącz **Allow Remote Access the LAN Subnet**, a następnie kliknij **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Przetestuj połączenie

Oto przykład uzyskania dostępu do GL-MT3000 (urządzenie w sieci LAN klienta OpenVPN) z adresem IP **192.168.48.211**.

Na urządzeniu podłączonym do serwera OpenVPN wykonaj ping na adres IP GL-MT3000 **192.168.48.211**. To jest adres IP, który klient OpenVPN (GL-MT2500) przypisuje do GL-MT3000 w swojej sieci LAN.

Jeśli możesz wykonać ping pomyślnie, oznacza to, że ustawienia są poprawne. Będziesz mógł uzyskać dostęp do wszystkich innych urządzeń w podsieci LAN klienta OpenVPN za pośrednictwem ich adresów IP.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
