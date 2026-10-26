# Så kommer du åt WireGuard-klientens LAN från servern {#how-to-access-wireguard-client-lan-side-from-server}

Den här guiden beskriver hur du kommer åt WireGuard-klientens LAN-subnät, till exempel IP-kameror och NAS, från WireGuard-serverns sida.

## Topologi {#topology}

I exemplet nedan är GL-MT2500 en WireGuard-server och GL-AXT1800 en ansluten WireGuard-klient. Från serversidan kan du komma åt enheter på GL-AXT1800:s LAN.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Lägg till en routningsregel på servern {#1-add-route-rule-on-server}

??? "För firmware v4.7 och tidigare"

    Logga in på <u>WireGuard-serverns</u> webbadministrationspanel och gå till **VPN** -> **VPN Dashboard** -> **VPN Server**. Klicka på routningsikonen till höger.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Klicka på **Add Route Rule** och ange subnätet som du vill komma åt.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    GL-AXT1800:s LAN-subnät är i exemplet **192.168.8.0/24**, så Target Address är **192.168.8.0/24**. Gateway är den klient-IP som WireGuard-servern skapade. Den visas under fliken **Profiles** på sidan **WireGuard Server**; här är den **10.0.0.4**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Ange **10.0.0.4** som Gateway och **global** som Scope och klicka på **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "För firmware v4.8 och senare"

    Gå till **VPN** -> **WireGuard Server** på servern. Öppna fliken **Route Rules**, klicka på **Add Route Rule** och ange subnätet.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Ange **192.168.8.0/24** som Target Address. Klient-IP-adressen under fliken **Profiles** är **10.1.0.2** i exemplet.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Ange **10.1.0.2** som Gateway och klicka på **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Tillåt fjärråtkomst till klientens LAN {#2-allow-remote-access-to-client-lan}

??? "För firmware v4.7 och tidigare"

    Gå till **VPN** -> **VPN Dashboard** -> **VPN Client** på <u>WireGuard-klienten</u>. Klicka på kugghjulsikonen, aktivera **Remote Access LAN** och klicka på **Apply**.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "För firmware v4.8"

    Gå till **VPN** -> **VPN Dashboard** på klienten. Klicka på kugghjulet längst upp till vänster i tunneln, aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "För firmware v4.9 och senare"

    Gå till **VPN** -> **VPN Dashboard** på klienten. Klicka på kugghjulet i en tunnelgrupp, välj **Options**, aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}

## 3. Testa anslutningen {#3-test-connection}

Testa att du kan nå en LAN-enhet hos WireGuard-klienten från serversidan. Pinga till exempel IP-adressen för en enhet i GL-AXT1800:s LAN från en enhet som är ansluten till WireGuard-servern GL-MT2500.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
