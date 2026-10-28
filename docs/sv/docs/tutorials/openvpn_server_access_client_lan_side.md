# Så kommer du åt OpenVPN-klientens LAN från servern {#how-to-access-openvpn-client-lan-side-from-server}

Den här guiden beskriver hur du kommer åt OpenVPN-klientens LAN-subnät, till exempel NAS och IP-kameror, från OpenVPN-serverns sida.

## Topologi {#topology}

I exemplet nedan är GL-AXT1800 en OpenVPN-server och GL-MT2500 en ansluten OpenVPN-klient. Från serversidan kan du komma åt enheter på GL-MT2500:s LAN, till exempel en NAS eller underroutern GL-MT3000.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Lägg till en routningsregel på servern {#1-add-route-rule-on-server}

??? "För firmware v4.7 och tidigare"

    Logga in på webbadministrationspanelen för <u>OpenVPN-servern</u> och gå till **VPN** -> **VPN Dashboard** -> **VPN Server**. Klicka på routningsikonen till höger.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    Klicka på **Add Route Rule** och ange subnätet som du vill komma åt.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    OpenVPN-klienten GL-MT2500:s LAN-subnät är till exempel **192.168.48.0/24**, så Target Address är **192.168.48.0/24**. Gateway är den Client IP som OpenVPN-servern skapade för klienten. Ange här **10.8.0.1** som Gateway och klicka på **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Obs! Om du behöver komma åt LAN-subnäten för flera OpenVPN-klienter ska du först [reservera en Client IP](reserve_fixed_IP_for_ovpn_client.md) för varje klient.

??? "För firmware v4.8 och senare"

    Logga in på webbadministrationspanelen för <u>OpenVPN-servern</u> och gå till **VPN** -> **OpenVPN Server**. Öppna fliken **Route Rules** och klicka på **Add Route Rule**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    Ange subnätet som du vill komma åt i dialogrutan.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    För GL-MT2500 är Target Address i det här exemplet **192.168.48.0/24**. Gateway är den Client IP som servern skapade för klienten. Ange **10.8.0.2** och klicka på **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Obs! Om du behöver komma åt LAN-subnäten för flera OpenVPN-klienter ska du först [reservera en Client IP](reserve_fixed_IP_for_ovpn_client.md) för varje klient.

## 2. Tillåt fjärråtkomst till klientens LAN {#2-allow-remote-access-to-client-lan}

??? "För firmware v4.7 och tidigare"

    Logga in på <u>OpenVPN-klientens</u> webbadministrationspanel och gå till **VPN** -> **VPN Dashboard** -> **VPN Client**. Klicka på kugghjulsikonen, aktivera **Remote Access LAN** och klicka på **Apply**.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "För firmware v4.8"

    Gå till **VPN** -> **VPN Dashboard** på <u>OpenVPN-klienten</u>. Klicka på kugghjulsikonen längst upp till vänster i VPN-tunneln, aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "För firmware v4.9 och senare"

    Gå till **VPN** -> **VPN Dashboard** på <u>OpenVPN-klienten</u>. Klicka på kugghjulsikonen i en tunnelgrupp, välj **Options**, aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}

## 3. Testa anslutningen {#3-test-connection}

I det här exemplet öppnar vi GL-MT3000, en enhet i OpenVPN-klientens LAN, på IP-adressen **192.168.48.211**. Pinga adressen från en enhet som är ansluten till OpenVPN-servern. Om ping-kommandot lyckas är inställningarna korrekta. Åtkomst till tjänster på den här enheten eller andra enheter i OpenVPN-klientens LAN-subnät beror dock också på varje enhets brandväggsinställningar och tjänstekonfiguration.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
