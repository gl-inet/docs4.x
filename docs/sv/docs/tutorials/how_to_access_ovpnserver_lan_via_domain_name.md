# Öppna enheter i OpenVPN-serverns LAN från klienten via domännamn {#how-to-access-openvpn-server-lan-devices-from-the-client-via-domain-names}

Den här guiden beskriver hur du använder domännamn för att komma åt enheter i hemmet, till exempel NAS och IP-kameror, i OpenVPN-serverns LAN från en klient.

## Topologi {#topology}

Enligt bilden nedan kan du använda en dator i klientens LAN för att komma åt enheter som NAS och IP-kameror i OpenVPN-serverns LAN via deras respektive domännamn.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Konfigurationssteg {#setup-steps}

### 1. Redigera Hosts på servern (valfritt) {#1-edit-hosts-on-server-optional}

Steget gäller när VPN-servern inte kan slå upp lokala domännamn korrekt. Hoppa över steget om du är osäker.

Logga in på webbadministrationspanelen för VPN-serverroutern och gå till **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Ange IP-adressen och domännamnet för enheterna i hemmet som du vill komma åt och klicka sedan på **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Tillåt fjärråtkomst till LAN på servern {#2-allow-remote-access-lan-on-server}

Gå till **VPN** -> **OpenVPN Server** i serverns webbadministrationspanel. Klicka på **Options** i det övre högra hörnet.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

När alternativet är aktiverat kan routern och LAN-enheterna nås via fjärråtkomst genom VPN.

### 3. Exportera VPN-konfigurationen {#3-export-vpn-configuration}

Gå till **VPN** -> **OpenVPN Server** -> fliken **Configuration** i serverns administrationspanel och klicka på **Export Client Configuration** längst ned.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

Klicka på **Export** i dialogrutan.

**Obs!** Om serverns offentliga IP-adress är dynamisk och ändras då och då går du till **APPLICATIONS** -> **Dynamic DNS** och aktiverar **DDNS** innan du exporterar klientkonfigurationen.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Du får därefter en **.ovpn**-fil enligt nedan.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Om serverroutern kör firmware v4.8 eller senare behöver du inte redigera konfigurationsfilen. Fortsätt till nästa steg.

Om serverroutern kör firmware v4.7 eller tidigare öppnar du filen, lägger till följande rad för att ange OpenVPN-serverns tunnel-IP-adress som DNS-server och sparar sedan ändringarna.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Tips: OpenVPN-serverns virtuella IPv4-subnät för tunneln visas på fliken **Configuration** på sidan OpenVPN Server enligt nedan. Det varierar mellan firmwareversioner. Kontrollera OpenVPN-serverns tunnel-IP-adress.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Aktivera VPN-servern {#4-enable-vpn-server}

Klicka på knappen **Start** i det övre högra hörnet på sidan **OpenVPN Server** för att starta servern.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Ladda upp VPN-konfigurationen {#5-upload-vpn-configuration}

Logga in på webbadministrationspanelen för VPN-klientroutern, gå till **VPN** -> **OpenVPN Client** och klicka sedan på **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Ange ett namn för gruppen och ladda upp konfigurationsfilen.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Uppladdningen är klar. Klicka på **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Konfigurationsfilen visas i listan.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Starta VPN-klientanslutningen {#6-start-vpn-client-connection}

Klicka på ikonen med tre punkter för att initiera VPN-anslutningen.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

När den grå punkten blir grön har OpenVPN-klienten anslutits till servern.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Nu kan du använda datorn i klientens LAN för att komma åt enheterna i hemmet, till exempel NAS, i serverns LAN via deras domännamn.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
