# Set Up WireGuard Server on GL.iNet Routers {#set-up-wireguard-server-on-glinet-routers}

WireGuard® är ett enkelt, snabbt och modernt VPN med avancerad kryptografi och högre prestanda än OpenVPN.

Titta på videon eller följ stegen för att konfigurera WireGuard Server.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Kontrollera att du har en offentlig IP-adress {#make-sure-you-have-a-public-ip-address}

Klicka [här](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) för att kontrollera om internetleverantören tilldelar en offentlig IP-adress.

**If not, your router cannot be set up as a WireGuard Server.**

Alternative methods:

1. Logga in på den primära routern och kontrollera om den får en offentlig IP-adress.
2. Be internetleverantören om en offentlig IP-adress. En extra avgift kan tillkomma.
3. Om metoderna inte fungerar, till exempel bakom CGNAT, kan du prova [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Kontrollera om Port Forwarding krävs {#confirm-if-port-forwarding-is-required}

**Network Topology**

??? "GL.iNet is the primary router"

    * Om GL.iNet är primär router krävs ingen portvidarebefordran. Fortsätt till [nästa steg](#set-up-wireguard-server).

??? " GL.iNet is the sub-router"

    * Om GL.iNet är sekundär router konfigurerar du [portvidarebefordran](../tutorials/how_to_set_up_port_forwarding.md) på den primära routern.

    * Om GL.iNet ligger flera nivåer under den primära routern konfigurerar du [portvidarebefordran](../tutorials/how_to_set_up_port_forwarding.md) på varje mellanliggande nivå.

## Set up WireGuard Server {#set-up-wireguard-server}

Logga in och öppna **VPN** -> **WireGuard Server**.

1. Click **Generate Configuration** (for vpn server initial setup only).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Check the configuration.

    Standardkonfigurationen fungerar oftast. Ändra inte IPv4-adressen om den inte står i konflikt med uppströms gateway.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/check_configuration.png){class="glboxshadow"}

    (IPv6 är inaktiverat som standard. Aktivera IPv6 på routern för att använda en IPv6-adress.)

    IPv4-adressen är serverns Tunnel IP. Vid konflikt ändrar du den, till exempel till **10.1.0.1/24**, och klickar på **Apply**. Ta med `/24`.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/modify_configuration.png){class="glboxshadow"}

    En uppströms Xfinity-router kan till exempel använda 10.0.0.1 och stå i konflikt med Tunnel IP. Ändra endast vid konflikt.

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Add a profile.

    Öppna fliken **Profiles** och klicka på **Add**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles.png){class="glboxshadow"}

    Ange ett namn och klicka på **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Klicka vid behov på **Set More** och sedan på **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Add route rules if needed"

        It is not necessary to add route rules in most cases.

        För åtkomst från servern till klientens LAN anger du regler på fliken **Route Rules** på **WireGuard Server**. Se [guiden](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/route_rules.png){class="glboxshadow"}

        Otherwise, turn to Step 4 to download a client configuration.

4. Download configuration.

    När profilen har lagts till skapas konfigurationen som QR-kod, klartext och .conf-fil. Välj önskat format.

    - **QR code**: För enheter med WireGuard App. Skanna koden för automatisk import.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: Visa och kopiera konfigurationen manuellt till WireGuard App eller en GL.iNet-router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: Klicka på **Download** och ladda upp filen direkt till WireGuard App eller en GL.iNet-router.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_file.png){class="glboxshadow"}

    Från firmware v4.8 kan serveradressen vara offentlig IP, DDNS-domän eller aktuell WAN-IP. Konfigurationsfilen uppdateras samtidigt.

    Vid ofta ändrad offentlig IP rekommenderas [DDNS](ddns.md)-domänen som serveradress.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Start WireGuard server.

    Klicka på **Start** uppe till höger för att starta servern.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/start_wgserver.png){class="glboxshadow"}

    The connection status will be displayed on the same page.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Kontrollera att WireGuard Server fungerar {#check-if-wireguard-server-is-working-properly}

### Verify Server status {#verify-server-status}

Från firmware v4.8 visas serverstatus på sidan **WireGuard Server**.

Om trafikstatistik och anslutna enheter visas körs servern och klienter är anslutna.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

0 trafik och 0 klient betyder att ingen klient är ansluten.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

I firmware v4.7 och tidigare kontrolleras statusen på **VPN Dashboard**.

### Verify Client's IP {#verify-clients-ip}

Verifiera anslutningen genom att importera konfigurationen till en enhet i ett annat nätverk. Om IP-adress och plats motsvarar VPN-servern är anslutningen lyckad.

Använd en smartphone med officiella [WireGuard App](https://www.wireguard.com/install){target="_blank"}. Inaktivera Wi-Fi, använd 4G/5G, importera filen och kontrollera internet och IP-adress.

Vanliga orsaker till misslyckad anslutning:

* Internetleverantören tilldelar ingen offentlig IP-adress. Kontrollera [här](#make-sure-you-have-a-public-ip-address).
* Portvidarebefordran kan krävas. Kontrollera [här](#confirm-if-port-forwarding-is-required).
* WireGuard Server-porten blockeras av internetleverantören. Byt port eller kontakta leverantören.
* Some countries/regions may block the VPN connection.

## Server Options {#server-options}

Server Options innehåller avancerade inställningar som fjärråtkomst till LAN och IP Masquerading.

I firmware v4.8 och senare öppnar du **WireGuard Server** och klickar på **Options**.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options1.png){class="glboxshadow"}

I firmware v4.7 och tidigare öppnar du **VPN Dashboard** -> **VPN Server** och klickar på kugghjulet.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options2.png){class="glboxshadow"}

Popup-fönstret visar följande funktioner.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: Tillåter åtkomst till resurser i serverns LAN-subnät genom tunneln.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver hemroutern om NAS-käll-IP `192.168.8.100` till serverns tunneladress `10.1.0.1` vid trafik till Laptop `192.168.10.200`.

    ![wgserver ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Tunnelns MTU åsidosätter konfigurationsfilens värde.

- **Client to Client**: Låter anslutna VPN-klienter nå varandra via tunnel-IP.

    Client‑to‑Client annonserar endast tunnel-IP. Lägg till serverrutter för åtkomst mellan klienternas LAN-subnät.

## WireGuard App Install {#wireguard-app-install}

Hämta WireGuard App från [WireGuard Official Website](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
