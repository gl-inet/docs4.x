# Så kommer du åt enheter i WireGuard-serverns LAN via domännamn från klienten {#how-to-access-wireguard-server-lan-devices-from-the-client-via-domain-names}

Den här guiden beskriver hur du kommer åt enheter i hemmet, till exempel NAS och IP-kameror, på WireGuard-serverns LAN från en klient med hjälp av domännamn.

## Topologi {#topology}

Som bilden visar kan du använda enheternas respektive domännamn för att komma åt dem från en dator i klientens LAN.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Konfigurationssteg {#setup-steps}

### 1. Redigera Hosts på servern (valfritt) {#1-edit-hosts-on-server-optional}

Det här steget gäller om VPN-servern inte kan matcha lokala domännamn korrekt. Hoppa över steget om du är osäker.

Logga in på VPN-serverrouterns webbadministrationspanel och gå till **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Ange IP-adress och domännamn för de enheter som du vill komma åt och klicka på **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Tillåt fjärråtkomst till LAN på servern {#2-allow-remote-access-lan-on-server}

??? "För en serverrouter med firmware v4.8"

    Gå till **VPN** -> **WireGuard Server** på serverns webbadministrationspanel och klicka på **Options** i det övre högra hörnet.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Aktivera **Allow Remote Access the LAN Subnet** och klicka på **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **När alternativet är aktiverat kan routern och LAN-enheterna nås via VPN på distans.**

??? "För en serverrouter med firmware v4.7 eller tidigare"

    Gå till **VPN** -> **VPN Dashboard** -> avsnittet **VPN Server** och klicka på kugghjulsikonen till höger om WireGuard-servern.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Aktivera **Remote Access LAN** och klicka på **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **När alternativet är aktiverat kan routern och LAN-enheterna nås via VPN på distans.**

### 3. Exportera VPN-konfigurationen {#3-export-vpn-configuration}

Gå till **VPN** -> **WireGuard Server** -> fliken **Profiles** på serverns administrationspanel. Klicka på **Add** för att exportera en konfigurationsprofil.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Du får en **.conf**-fil enligt nedan.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Öppna filen och kontrollera att DNS-fältet pekar på serverns tunnel-IP, som visas på fliken **Configuration** på sidan WireGuard Server. Ta samtidigt bort "64.6.64.6" från DNS-fältet om adressen finns där, så att DNS-upplösningen inte misslyckas.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Obs!** WireGuard-serverns tunnel-IP varierar mellan firmwareversioner. Kontrollera tunnel-IP-adressen på din server.

### 4. Aktivera VPN-servern {#4-enable-vpn-server}

Klicka på **Start** i det övre högra hörnet på sidan **WireGuard Server**.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Ladda upp VPN-konfigurationen {#5-upload-vpn-configuration}

Logga in på VPN-klientrouterns webbadministrationspanel, gå till **VPN** -> **WireGuard Client** och klicka på **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Ange ett namn för gruppen och ladda upp konfigurationsfilen.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Klicka på **Apply** när uppladdningen är klar.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Konfigurationsfilen visas i listan.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Starta VPN-klientanslutningen {#6-start-vpn-client-connection}

Klicka på ikonen med tre punkter för att starta VPN-anslutningen.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

När den grå punkten blir grön har WireGuard-klienten anslutit till servern.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Nu kan du använda domännamnen för att komma åt enheterna på serverns LAN från en dator på klientens LAN.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
