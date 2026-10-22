# Set Up OpenVPN Server on GL.iNet Routers {#set-up-openvpn-server-on-glinet-routers}

OpenVPN is an open‑source VPN protocol that uses virtual private network techniques to establish secure site‑to‑site or point‑to‑point connections.

Titta på videon eller följ stegen nedan för att konfigurera OpenVPN Server.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Kontrollera att du har en offentlig IP-adress {#make-sure-you-have-a-public-ip-address}

Klicka [här](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) för att kontrollera om internetleverantören tilldelar en offentlig IP-adress.

**If not, your router cannot be set as an OpenVPN Server.**

Alternative methods:

1. Logga in på den primära routern och kontrollera om den får en offentlig IP-adress.
2. Be internetleverantören om en offentlig IP-adress. En extra avgift kan tillkomma.
3. Om metoderna inte fungerar, till exempel bakom CGNAT, kan du prova [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

## Kontrollera om Port Forwarding krävs {#confirm-if-port-forwarding-is-required}

**Network Topology**

??? "GL.iNet is the primary router"

    * Om GL.iNet är primär router krävs ingen portvidarebefordran. Fortsätt till [nästa steg](#set-up-openvpn-server).

??? " GL.iNet is the sub-router"

    * Om GL.iNet är sekundär router konfigurerar du [portvidarebefordran](../tutorials/how_to_set_up_port_forwarding.md) på den primära routern.

    * Om GL.iNet ligger flera nivåer under den primära routern konfigurerar du [portvidarebefordran](../tutorials/how_to_set_up_port_forwarding.md) på varje mellanliggande nivå.

## Set up OpenVPN Server {#set-up-openvpn-server}

Logga in och öppna **VPN** -> **OpenVPN Server**.

1. Click **Generate Configuration** (for vpn server initial setup only).

    ![ovpnserver generate config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_generate.png){class="glboxshadow"}

2. Apply the configuration.

    The default configuration works for most cases.

    Om konfigurationen inte behöver ändras klickar du på **Export Client Configuration** och fortsätter till steg 3.

    Om konfigurationen har ändrats klickar du på **Apply** före export.

    ![openvpnserver configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S or Tun. Click [here](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md#tap-s2s-vs-tun-mode) to check the differences.

    * **Protocol:** UDP or TCP. Click [here](../faq/openvpn_tcp_udp.md) to check the differences.

    * **Authentication Mode:** Anger autentiseringsmetod. Tre alternativ finns.

        - **Certificate Only**: Routern skapar server- och klientcertifikat och bäddar in klientcertifikat och nyckel i filen. Inga ytterligare uppgifter krävs.

        - **Username/Password Only**: Skapar konfiguration utan certifikatnycklar. Lägg först till användarnamn och lösenord på fliken Users; uppgifterna krävs på klienten.

        - **Username/Password and Certificate**: Lägg först till användarnamn och lösenord. Routern skapar och bäddar in certifikat och nyckel. Klienten verifierar först certifikatnyckeln och sedan inloggningsuppgifterna.

        Here is an example of creating a user.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: Ändra fler serverinställningar vid behov.

        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Export Client Configuration.

    Klicka på **Export Client Configuration** längst ned på fliken Configuration. Följande fönster visas.

    ![openvpn export config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_export_config.png){class="glboxshadow"}

    - Om den offentliga IP-adressen ändras ofta kan [DDNS](ddns.md)-domänen användas som serveradress.

    - Från firmware v4.8 kan serveradressen vara offentlig IP, DDNS-domän eller aktuell WAN-IP. Konfigurationsfilen uppdateras samtidigt.

    Klicka på **Download** för att exportera konfigurationen.

4. Start OpenVPN server.

    Klicka på **Start** uppe till höger på OpenVPN Server och kontrollera statusen på VPN Dashboard.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Kontrollera att OpenVPN Server fungerar {#check-if-openvpn-server-is-working-properly}

### Verify Server status {#verify-server-status}

Från firmware v4.8 visas serverstatus på sidan **OpenVPN Server**.

Om uppladdnings- och nedladdningsstatistik visas körs servern.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

I firmware v4.7 och tidigare kontrolleras statusen på **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Verify Client's IP {#verify-clients-ip}

Verifiera anslutningen genom att importera konfigurationen till en enhet i ett annat nätverk. Kontrollera IP-adress och plats. Om de motsvarar VPN-servern är anslutningen lyckad.

En enkel metod är en smartphone med officiella [OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"}. Inaktivera Wi-Fi, använd 4G/5G, importera filen och anslut. Kontrollera internet och IP-adressen.

Vid import kan följande meddelande visas. Klicka på **CONTINUE** eftersom certifikatet redan finns i filen.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Vanliga orsaker till misslyckad anslutning:

* Internetleverantören tilldelar ingen offentlig IP-adress. Kontrollera [här](#make-sure-you-have-a-public-ip-address).
* Portvidarebefordran kan krävas. Kontrollera [här](#confirm-if-port-forwarding-is-required).
* OpenVPN Server-porten blockeras av internetleverantören. Byt port eller kontakta leverantören.
* Some countries/regions may block the VPN connection.

## Server Options {#server-options}

Server Options innehåller avancerade inställningar som fjärråtkomst till LAN och IP Masquerading.

I firmware v4.8 och senare öppnar du **OpenVPN Server** och klickar på **Options** uppe till höger.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options1.png){class="glboxshadow"}

I firmware v4.7 och tidigare öppnar du **VPN Dashboard** -> **VPN Server** och klickar på kugghjulet.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options2.jpg){class="glboxshadow"}

Popup-fönstret visar följande funktioner.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: Tillåter åtkomst till resurser i serverns LAN-subnät genom tunneln.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver hemroutern om NAS-käll-IP `192.168.8.100` till serverns tunneladress `10.1.0.1` vid trafik till Laptop `192.168.10.200`.

    ![ovpnserver ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Tunnelns MTU åsidosätter konfigurationsfilens värde.

## Client to Client {#client-to-client}

Client‑to‑Client låter anslutna VPN-klienter kommunicera via sina tunnel-IP-adresser.

The network topology is as follows.

![client-to-client topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Följ stegen för att aktivera Client to Client.

1. Klicka på **Advanced Configuration** nere till höger på **OpenVPN Server**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_config_advanced.png){class="glboxshadow"}

2. Aktivera **Client to Client**, klicka på **Apply**, exportera en ny konfiguration och ladda upp den till klienterna.

    ![client to client](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/client-to-client.png){class="glboxshadow"}

**Tips!** Client‑to‑Client annonserar endast klienternas tunnel-IP. Lägg till routningsregler på servern för åtkomst mellan klienternas LAN-subnät.

## OpenVPN App Install {#openvpn-app-install}

Hämta OpenVPN App från [OpenVPN Official Website](https://openvpn.net/vpn-client/){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
