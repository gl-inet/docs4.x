# OpenVPN Server instellen op GL.iNet-routers {#set-up-openvpn-server-on-glinet-routers}

OpenVPN is een opensource-VPN-protocol voor beveiligde site-to-site- of point-to-pointverbindingen.

Bekijk deze video of volg de onderstaande stappen om OpenVPN Server op een GL.iNet-router in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Controleren of je een openbaar IP-adres hebt {#make-sure-you-have-a-public-ip-address}

Klik [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om te controleren of je internetprovider een openbaar IP-adres toewijst.

**Zonder openbaar IP-adres kan je router niet als OpenVPN Server worden ingesteld.**

Alternatieve methoden:

1. Meld je bij de primaire router aan en controleer of deze een openbaar IP-adres ontvangt.
2. Vraag je internetprovider om een openbaar IP-adres. Hier kunnen kosten aan verbonden zijn.
3. Als dit niet werkt, bijvoorbeeld achter CGNAT, probeer je onze SD-WAN-oplossing [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

## Controleren of port forwarding vereist is {#confirm-if-port-forwarding-is-required}

**Netwerktopologie**

??? "GL.iNet is de primaire router"

    * Als de GL.iNet-router de primaire router is, is geen port forwarding nodig. Ga naar de [volgende stap](#set-up-openvpn-server).

??? "GL.iNet is de subrouter"

    * Als de GL.iNet-router een secundaire router is, configureer je [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) op de primaire router.

    * Als de GL.iNet-router meerdere niveaus onder de primaire router staat, configureer je [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) op elk tussenniveau.

## OpenVPN Server instellen {#set-up-openvpn-server}

Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **OpenVPN Server**.

1. Klik bij de eerste installatie op **Generate Configuration**.

    ![ovpnserver generate config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_generate.png){class="glboxshadow"}

2. Pas de configuratie toe.

    De standaardconfiguratie werkt in de meeste situaties.

    Klik onderaan op **Export Client Configuration** en ga naar stap 3 als geen wijziging nodig is.

    Klik na wijzigingen op **Apply** voordat je de clientconfiguratie exporteert.

    ![openvpnserver configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S of Tun. Klik [hier](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md#tap-s2s-vs-tun-mode) voor de verschillen.

    * **Protocol:** UDP of TCP. Klik [hier](../faq/openvpn_tcp_udp.md) voor de verschillen.

    * **Authentication Mode:** bepaalt de verificatiemethode bij verbinding van de client. Er zijn drie opties.

        - **Certificate Only**: de router genereert server- en clientcertificaten en voegt clientcertificaat en sleutel aan het configuratiebestand toe. Er zijn geen extra aanmeldingsgegevens nodig.

        - **Username/Password Only**: genereert een clientconfiguratie zonder certificaatsleutels. Voeg vóór export een gebruikersnaam en wachtwoord toe onder Users en voer deze bij de client in.

        - **Username/Password and Certificate**: voeg vóór export een gebruikersnaam en wachtwoord toe. De router genereert certificaten en voegt het clientcertificaat en de sleutel toe. Eerst wordt de certificaatsleutel gecontroleerd en daarna gebruikersnaam en wachtwoord.

        Hieronder wordt een gebruiker gemaakt.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: wijzig zo nodig meer serverinstellingen.

        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Exporteer de clientconfiguratie.

    Klik onderaan Configuration op **Export Client Configuration**. Het onderstaande venster verschijnt.

    ![openvpn export config](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_export_config.png){class="glboxshadow"}

    - Schakel bij een vaak wijzigend openbaar IP-adres [DDNS](ddns.md) in om het DDNS-domein als serveradres te gebruiken.

    - Vanaf firmware v4.8 kun je het openbare IP, DDNS-domein of huidige WAN-IP als serveradres kiezen. Het configuratiebestand wordt tegelijk bijgewerkt.

    Klik op **Download** om de configuratie te exporteren.

4. Start OpenVPN Server.

    Klik rechtsboven op **Start** om de server te starten. Controleer status en instellingen in VPN Dashboard.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Controleren of OpenVPN Server goed werkt {#check-if-openvpn-server-is-working-properly}

### Serverstatus controleren {#verify-server-status}

Vanaf firmware v4.8 kun je de verbindingsstatus op **OpenVPN Server** bekijken.

Upload- en downloadstatistieken betekenen dat de OpenVPN-server actief is.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

Controleer in firmware v4.7 en ouder de status op **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/openserverup.jpg){class="glboxshadow"}

### IP-adres van de client controleren {#verify-clients-ip}

Importeer de OpenVPN-configuratie op een apparaat in een ander netwerk. Zoek het IP-adres en de locatie op. Als deze overeenkomen met de VPN-server in plaats van de internetprovider, werkt de verbinding.

Gebruik bijvoorbeeld een smartphone met de officiële [OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"}. Schakel Wi-Fi uit, gebruik 4G/5G, importeer het configuratiebestand en maak verbinding. Controleer internettoegang en of het IP-adres overeenkomt met OpenVPN Server.

Bij import kan de onderstaande melding verschijnen. Klik op **CONTINUE**; het certificaat zit al in het bestand.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Een mislukte verbinding kan de volgende oorzaken hebben:

* De internetprovider wijst geen openbaar IP-adres toe. Controleer dit [hier](#make-sure-you-have-a-public-ip-address).
* Mogelijk is port forwarding vereist. Controleer dit [hier](#confirm-if-port-forwarding-is-required).
* De provider blokkeert de poort van OpenVPN Server. Gebruik een andere poort of neem contact op met de provider.
* Sommige landen of regio's blokkeren VPN-verbindingen.

## Server Options {#server-options}

Server Options bevat geavanceerde serverinstellingen, zoals externe LAN-toegang en IP Masquerading. Configureer ze naar behoefte.

Ga in firmware v4.8 en hoger naar **OpenVPN Server** en klik rechtsboven op **Options**.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options1.png){class="glboxshadow"}

Ga in firmware v4.7 en ouder naar **VPN Dashboard** -> **VPN Server** en klik op het tandwielpictogram voor OpenVPN Options.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options2.jpg){class="glboxshadow"}

Het pop-upvenster toont de volgende functies.

![ovpnserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: bronnen in het LAN-subnet van de server zijn via de VPN-tunnel toegankelijk.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en NAS (192.168.8.100) op het thuis-LAN verkeer naar Laptop (192.168.10.200) stuurt, herschrijft de thuisrouter het bron-IP naar server-tunneladres `10.1.0.1`. De externe zijde ziet het verkeer als afkomstig van de server.

    ![ovpnserver ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ip_masquerading.png){class="glboxshadow"}

- **MTU**: afkorting van Maximum Transmission Unit. De ingestelde tunnelwaarde overschrijft de MTU in het configuratiebestand.

## Client to Client {#client-to-client}

Client‑to‑Client is een serverfunctie waarmee verbonden VPN-clients via hun tunnel-IP-adressen communiceren.

De netwerktopologie is als volgt.

![client-to-client topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Volg zo nodig de onderstaande stappen om Client to Client op OpenVPN Server in te schakelen.

1. Klik op de pagina **OpenVPN Server** rechtsonder op **Advanced Configuration**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_config_advanced.png){class="glboxshadow"}

2. Schakel **Client to Client** in, klik op **Apply**, exporteer een nieuwe configuratie en upload deze naar de clients.

    ![client to client](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/client-to-client.png){class="glboxshadow"}

**Tip**: Client‑to‑Client maakt alleen tunnel-IP-adressen bekend. Voeg serverrouteringsregels toe om toegang tot de LAN-subnets achter clients toe te staan.

## OpenVPN-app installeren {#openvpn-app-install}

Download de OpenVPN-app via de [officiële OpenVPN-website](https://openvpn.net/vpn-client/){target="_blank"}.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
