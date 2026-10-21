# WireGuard Server instellen op GL.iNet-routers {#set-up-wireguard-server-on-glinet-routers}

WireGuard® is een eenvoudige, snelle moderne VPN met geavanceerde cryptografie. Het is sneller, eenvoudiger en lichter dan IPSec en presteert aanzienlijk beter dan OpenVPN.

Bekijk deze video of volg de onderstaande stappen om WireGuard Server op een GL.iNet-router in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Controleren of je een openbaar IP-adres hebt {#make-sure-you-have-a-public-ip-address}

Klik [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om te controleren of je internetprovider een openbaar IP-adres toewijst.

**Zonder openbaar IP-adres kan je router niet als WireGuard Server worden ingesteld.**

Alternatieve methoden:

1. Meld je bij de primaire router aan en controleer of deze een openbaar IP-adres ontvangt.
2. Vraag je internetprovider om een openbaar IP-adres. Hier kunnen kosten aan verbonden zijn.
3. Als dit niet werkt, bijvoorbeeld achter CGNAT, probeer je onze SD-WAN-oplossing [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Controleren of port forwarding vereist is {#confirm-if-port-forwarding-is-required}

**Netwerktopologie**

??? "GL.iNet is de primaire router"

    * Als de GL.iNet-router de primaire router is, is geen port forwarding nodig. Ga naar de [volgende stap](#set-up-wireguard-server).

??? "GL.iNet is de subrouter"

    * Als de GL.iNet-router een secundaire router is, configureer je [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) op de primaire router.

    * Als de GL.iNet-router meerdere niveaus onder de primaire router staat, configureer je [port forwarding](../tutorials/how_to_set_up_port_forwarding.md) op elk tussenniveau.

## WireGuard Server instellen {#set-up-wireguard-server}

Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **WireGuard Server**.

1. Klik bij de eerste installatie op **Generate Configuration**.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Controleer de configuratie.

    De standaardconfiguratie werkt meestal. Wijzig het IPv4-adres niet als er geen conflict met de gateway van de upstream router is.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/check_configuration.png){class="glboxshadow"}

    (IPv6 is standaard uitgeschakeld. Schakel IPv6 in om een IPv6-adres te gebruiken.)

    Het IPv4-adres is het Tunnel IP van WireGuard Server. Wijzig dit bij een conflict, bijvoorbeeld in **10.1.0.1/24**, en klik op **Apply**. Neem CIDR "/24" op.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Een upstream Xfinity-router kan bijvoorbeeld IP 10.0.0.1 gebruiken, dat met Tunnel IP van WireGuard Server conflicteert. Pas het adres dan aan; sla dit over zonder conflict.

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Voeg een profiel toe.

    Open het tabblad **Profiles** en klik op **Add** om een profiel te genereren.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles.png){class="glboxshadow"}

    Stel een beschrijvende naam in en klik op **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Klik voor geavanceerde instellingen op **Set More** en vervolgens op **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Zo nodig routeringsregels toevoegen"

        In de meeste gevallen zijn geen routeringsregels nodig.

        Open het tabblad **Route Rules** op **WireGuard Server** om vanaf de server toegang tot LAN-apparaten van de client in te stellen. Klik [hier](../tutorials/wireguard_server_access_to_client_lan_side.md) voor instructies.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/route_rules.png){class="glboxshadow"}

        Ga anders naar stap 4 om een clientconfiguratie te downloaden.

4. Download de configuratie.

    Na toevoeging van een profiel wordt de configuratie als QR-code, platte tekst en .conf-bestand gegenereerd. Kies de gewenste methode.

    - **QR code**: geschikt voor apparaten met de WireGuard-app. Open de app en scan de code om de configuratie automatisch te importeren.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: bekijk en kopieer configuratiegegevens voor handmatige configuratie in de WireGuard-app of op een GL.iNet-router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: klik op **Download** om het .conf-bestand op te slaan en naar de WireGuard-app of GL.iNet-router te uploaden.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_file.png){class="glboxshadow"}

    Vanaf firmware v4.8 kun je het openbare IP, DDNS-domein of huidige WAN-IP als serveradres kiezen. Het configuratiebestand wordt tegelijk bijgewerkt.

    Schakel bij een vaak wijzigend openbaar IP-adres [DDNS](ddns.md) in en gebruik het DDNS-domein als serveradres.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Start WireGuard Server.

    Klik rechtsboven op **Start** om WireGuard Server te starten.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/start_wgserver.png){class="glboxshadow"}

    De verbindingsstatus wordt op dezelfde pagina weergegeven.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Controleren of WireGuard Server goed werkt {#check-if-wireguard-server-is-working-properly}

### Serverstatus controleren {#verify-server-status}

Vanaf firmware v4.8 kun je de verbindingsstatus op **WireGuard Server** bekijken.

Upload- en downloadstatistieken en online apparaten betekenen dat WireGuard Server actief is en clients verbonden zijn.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

0 verkeer en 0 clients betekent dat geen WireGuard-client verbonden is.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

Controleer in firmware v4.7 en ouder de status op **VPN Dashboard**.

### IP-adres van de client controleren {#verify-clients-ip}

Importeer de WireGuard-configuratie op een apparaat in een ander netwerk. Zoek het IP-adres en de locatie op. Als deze overeenkomen met de VPN-server in plaats van de internetprovider, werkt de verbinding.

Gebruik bijvoorbeeld een smartphone met de officiële [WireGuard App](https://www.wireguard.com/install){target="_blank"}. Schakel Wi-Fi uit, gebruik 4G/5G, importeer het configuratiebestand en maak verbinding. Controleer internettoegang en of het IP-adres overeenkomt met WireGuard Server.

Een mislukte verbinding kan de volgende oorzaken hebben:

* De internetprovider wijst geen openbaar IP-adres toe. Controleer dit [hier](#make-sure-you-have-a-public-ip-address).
* Mogelijk is port forwarding vereist. Controleer dit [hier](#confirm-if-port-forwarding-is-required).
* De provider blokkeert de poort van WireGuard Server. Gebruik een andere poort of neem contact op met de provider.
* Sommige landen of regio's blokkeren VPN-verbindingen.

## Server Options {#server-options}

Server Options bevat geavanceerde serverinstellingen, zoals externe LAN-toegang en IP Masquerading. Configureer ze naar behoefte.

Ga in firmware v4.8 en hoger naar **WireGuard Server** en klik rechtsboven op **Options**.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options1.png){class="glboxshadow"}

Ga in firmware v4.7 en ouder naar **VPN Dashboard** -> **VPN Server** en klik op het tandwielpictogram voor WireGuard Options.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options2.png){class="glboxshadow"}

Het pop-upvenster toont de volgende functies.

![wgserver options](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: bronnen in het LAN-subnet van de server zijn via de VPN-tunnel toegankelijk.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en NAS (192.168.8.100) op het thuis-LAN verkeer naar Laptop (192.168.10.200) stuurt, herschrijft de thuisrouter het bron-IP naar server-tunneladres `10.1.0.1`. De externe zijde ziet het verkeer als afkomstig van de server.

    ![wgserver ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/ip_masquerading.png){class="glboxshadow"}

- **MTU**: afkorting van Maximum Transmission Unit. De ingestelde tunnelwaarde overschrijft de MTU in het configuratiebestand.

- **Client to Client**: clients op deze server kunnen elkaar via hun tunnel-IP-adressen bereiken.

    Client‑to‑Client maakt alleen tunnel-IP-adressen bekend. Voeg serverrouteringsregels toe om toegang tot de LAN-subnets achter clients toe te staan.

## WireGuard-app installeren {#wireguard-app-install}

Download de WireGuard-app via de [officiële WireGuard-website](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® is een geregistreerd handelsmerk van Jason A. Donenfeld.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
