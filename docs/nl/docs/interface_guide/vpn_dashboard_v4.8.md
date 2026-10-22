# VPN Dashboard (Firmware v4.8) {#vpn-dashboard-firmware-v48}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.8.x. Als je apparaat een andere firmwareversie gebruikt, kies je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.8" markdown="1">

- [Firmware v4.7 and earlier](vpn_dashboard_v4.7.md)
- [Firmware v4.9 en hoger](vpn_dashboard.md)

</div>

On the left side of the web Admin Panel, go to **VPN** -> **VPN Dashboard**.

Het VPN-dashboard toont verbindingsgegevens zoals tunnelregels, serveradres, verkeersstatistieken, virtueel client-IP en verbindingslogboek. Je kunt er ook geavanceerde instellingen zoals VPN Kill Switch, IP Masquerading en MTU configureren.

Je kunt ook meerdere VPN-verbindingen activeren voor scenario's met meerdere tunnels.

## Installatiewizard {#setup-wizard}

Klik linksboven op het boekpictogram en volg de VPN Setup Wizard om de VPN-configuratie snel te voltooien.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Opmerking**: de VPN Setup Wizard is alleen bedoeld voor de geïntegreerde VPN-diensten AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA en Surfshark. Voor andere VPN-diensten sla je de wizard over en ga je naar [OpenVPN Client](openvpn_client.md){target="_blank"} of [WireGuard Client](wireguard_client.md){target="_blank"} om de VPN handmatig in te stellen.

Here's an example with **Hide.me**. Log in with Hide.me credentials.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Selecteer een VPN-server en klik op **Apply**. Je maakt via deze VPN-tunnel verbinding met deze server en je openbare IP-adres lijkt afkomstig te zijn van de locatie van de geselecteerde server.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

De verbinding wordt automatisch tot stand gebracht. Ga daarna naar het VPN-dashboard. Daar zie je dat een VPN-tunnel is ingeschakeld.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Hier zie je het gebruikte VPN-protocol, zoals WireGuard, het configuratiebestand, serveradres, de luisterpoort van de server, verkeersstatistieken en het virtuele client-IP. Rechtsonder kun je het verbindingslogboek bekijken.

Alle verbonden clients gebruiken internet via deze VPN-tunnel.

Raadpleeg [Policy Mode](#policy-mode) om VPN-beleid te configureren.

## VPN Mode {#vpn-mode}

Klik rechtsboven op het VPN-dashboard op de knop om tussen VPN-modi te schakelen.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Two modes are available: **Global Mode** and **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode {#global-mode}

In deze modus wordt al het verkeer via de VPN-tunnel gerouteerd en kan slechts één VPN-clientinstantie worden geactiveerd.

It is ideal for scenarios where all client traffic is routed through a single VPN server, such as unified network security or region‑specific content access.

In het volgende voorbeeld maakt de router via het WireGuard-protocol verbinding met een Australische server. Al het verkeer van verbonden clients wordt via deze VPN-tunnel gerouteerd.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

#### Tunnel Options {#tunnel-options}

Je kunt geavanceerde instellingen voor je VPN-tunnel configureren, zoals VPN Kill Switch, IP Masquerading en MTU.

Klik rechtsboven op het tandwielpictogram.

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options1.png){class="glboxshadow"}

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options2.png){class="glboxshadow"}

- **Kill Switch**: wanneer dit is ingeschakeld, wordt verkeer dat via deze VPN-tunnel wordt gerouteerd automatisch geblokkeerd als de VPN-verbinding uitvalt. Wanneer dit is uitgeschakeld, schakelt het verkeer over naar het lokale WAN en gebruikt het internet zonder de VPN-tunnel.

- **Services from GL.iNet Use VPN**: wanneer dit is ingeschakeld, verzenden GoodCloud, DDNS en rtty pakketten via VPN-tunnels. Deze optie is standaard uitgeschakeld, omdat deze diensten gewoonlijk het werkelijke IP-adres nodig hebben.

- **Allow Remote Access the LAN Subnet**: wanneer dit is ingeschakeld, is externe toegang tot deze router en de LAN-apparaten via VPN toegestaan. De VPN-server moet een route naar het LAN-subnet van deze router bekendmaken.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en Laptop (192.168.10.200) op het reis-LAN verkeer naar de thuis-NAS (192.168.8.100) stuurt, herschrijft de reisrouter het bron-IP van `192.168.10.200` naar het tunneladres `10.1.0.2`. De serverzijde ziet het verkeer daardoor als afkomstig van de client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: afkorting van Maximum Transmission Unit. De MTU-waarde die je voor de tunnel instelt, overschrijft de waarde in het configuratiebestand.

### Policy Mode {#policy-mode}

In deze modus kan de router verbinding maken met meerdere VPN-servers en kun je routeringsregels aanpassen voor verschillende clients of verkeersbestemmingen.

It is suitable for use cases requiring flexible traffic management, such as routing different traffic to different destinations through multiple VPN servers.

Stel VPN Mode in op Policy Mode en klik op **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Als de VPN na het omschakelen niet is ingeschakeld, bevat de pagina de drie onderstaande gedeelten: Primary Tunnel, Add Tunnel en All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Klik op een gedeelte voor meer informatie.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel {#primary-tunnel}

De primaire tunnel is een <u>vooraf ingestelde</u> tunnel in Policy Mode. Deze heeft de hoogste prioriteit. Als er meerdere tunnels zijn, kun je de [tunnelprioriteit](#tunnel-priority) wijzigen.

Je kunt de tunnelregel aanpassen door drie factoren in te stellen:

1. **From**: de verkeersbron, oftewel het verkeer dat via deze tunnel moet worden gerouteerd.

    Klik op het grijze vak om de verkeersbron te selecteren.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: verkeer van alle apparaten komt met deze regel overeen.

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: verkeer van opgegeven verbindingstypen, zoals LAN-subnet, Drop-in Gateway en Guest Network, komt met deze regel overeen.

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Als je de OpenVPN-server of WireGuard-server op deze router hebt ingeschakeld, verschijnen er meer opties onder Specified Connection Types. Dit is nuttig voor [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, komt met deze regel overeen.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: als je dit selecteert, komt verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, **NIET** met deze regel overeen.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: It refers to the traffic destinations.

    Klik op het grijze vak om de verkeersbestemmingen te selecteren.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: verkeer dat met deze regel overeenkomt, wordt naar alle doelen gerouteerd.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: als je dit selecteert, wordt verkeer dat met deze regel overeenkomt naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.

        Een <u>hoofddomein</u> omvat alle subdomeinen. Als je bijvoorbeeld `archive.ubuntu.com`, `security.ubuntu.com` en `old-releases.ubuntu.com` in een tunnel wilt opgeven, hoef je alleen het hoofddomein `ubuntu.com` op te geven.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Je kunt **Input Mode** ook van Manual naar Subscription URL wijzigen en de URL invoeren.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specifying a root domain will cover all its subdomains.

            - Als je Subscribe URL selecteert, wordt de domeinnaam of het IP-adres in de URL dagelijks automatisch bijgewerkt.

            - Make sure to enter the correct URL. The URL detection will verify the validity of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: als je dit selecteert, wordt verkeer dat met deze regel overeenkomt **NIET** naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.

        Een <u>hoofddomein</u> omvat alle subdomeinen. Als je bijvoorbeeld `archive.ubuntu.com`, `security.ubuntu.com` en `old-releases.ubuntu.com` in een tunnel wilt opgeven, hoef je alleen het hoofddomein `ubuntu.com` op te geven.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Je kunt **Input Mode** ook van Manual naar Subscription URL wijzigen en de URL invoeren.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specifying a root domain will cover all its subdomains.

            - Als je Subscribe URL selecteert, wordt de domeinnaam of het IP-adres in de URL dagelijks automatisch bijgewerkt.

            - Make sure to enter the correct URL. The URL detection will verify the validity of the domain name or IP address. [Learn More](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: It refers to the traffic routing method, i.e., whether to use VPN.

    Klik op het grijze vak om de routeringsmethode te selecteren.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: als je dit selecteert, wordt verkeer dat met deze regel overeenkomt via de VPN naar de geselecteerde bestemmingen gerouteerd.

        Configureer je router eerst als VPN-client. Gebruik de [VPN Setup Wizard](#setup-wizard) om de configuratie snel te voltooien of ga in de linkerzijbalk naar OpenVPN Client of WireGuard Client om deze handmatig uit te voeren.

        Nadat je de router als VPN-client hebt ingesteld, selecteer je een VPN-configuratiebestand voor deze tunnel en klik je op **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: als je dit selecteert, wordt verkeer dat met deze regel overeenkomt via het lokale WAN in plaats van via de VPN naar de geselecteerde bestemmingen gerouteerd.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Nadat je de verkeersbron, bestemming en routeringsmethode hebt geselecteerd, is de regel voor de primaire tunnel voltooid.

In het volgende voorbeeld luidt de regel voor Primary Tunnel: alle clients gebruiken de VPN voor toegang tot opgegeven domeinen. Hun verkeer wordt via de Australische server en deze tunnel naar de geselecteerde internetdomeinen gerouteerd.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Opmerking**: controleer om veiligheidsredenen de overige instellingen onder [All Other Traffic](#all-other-traffic) en [Tunnel Options](#tunnel-options_1) voordat je de tunnels inschakelt.

#### Add Tunnel {#add-tunnel}

Klik onder Primary Tunnel op **Add Tunnel** en configureer aangepaste regels om extra tunnels voor meerdere VPN-instanties te maken.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Name the tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Er wordt een extra tunnel aan het VPN-dashboard toegevoegd.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Je kunt zo nodig meer tunnels toevoegen. Je kunt maximaal 5 tunnels maken, inclusief de vooraf ingestelde primaire tunnel.

Pas de tunnelregels aan door de verkeersbron, bestemmingen en routeringsmethode in te stellen. Raadpleeg [Primary Tunnel](#primary-tunnel).

**Opmerking**: controleer om veiligheidsredenen de overige instellingen onder [All Other Traffic](#all-other-traffic) en [Tunnel Options](#tunnel-options_1) voordat je de tunnels inschakelt.

#### All Other Traffic {#all-other-traffic}

In Policy Mode, a <u>pre-enabled</u> tunnel is displayed at the bottom of the VPN Dashboard.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Deze tunnel bepaalt of verkeer dat met geen van de bovenstaande VPN-tunnelgroepen overeenkomt internettoegang krijgt. De tunnel is standaard ingeschakeld zodat verkeer dat niet via VPN wordt gerouteerd normale internettoegang heeft.

- Wanneer dit is ingeschakeld, heeft niet-overeenkomend verkeer nog steeds internettoegang.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Wanneer dit is uitgeschakeld, heeft alleen verkeer dat via VPN wordt gerouteerd internettoegang. Al het niet-VPN-verkeer en verkeer dat na een mislukte VPN-verbinding overschakelt, wordt geblokkeerd. Deze optie overschrijft de afzonderlijke Kill Switch van een VPN-tunnel niet.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority {#tunnel-priority}

Standaard heeft de vooraf ingestelde Primary Tunnel de hoogste prioriteit, gevolgd door eventueel handmatig toegevoegde tunnels en daarna de tunnel All Other Traffic voor lokale netwerkverbinding via het lokale WAN.

Klik op **Modify Priority** in de bovenste informatiebalk of op het **prioriteitslabel** linksboven in een tunnel, zoals Priority 1 of Priority 2, om de tunnelprioriteit te wijzigen.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Klik rechts op het pictogram met drie lijnen, houd dit vast om de tunnels te herschikken en klik op **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router will route traffic in the following order**:

1. Verkeer wordt eerst vergeleken met de tunnelregel met de hoogste prioriteit. Bij een overeenkomst wordt het via die tunnel gerouteerd. Anders wordt de volgende tunnel geprobeerd totdat het verkeer overeenkomt met de tunnel "All Other Traffic".

2. Als een VPN-tunnel onverwacht wordt verbroken, bepaalt het systeem aan de hand van **Kill Switch** voor deze tunnel of het verkeer naar de tunnel met de volgende prioriteit overschakelt.

    - Als Kill Switch is ingeschakeld, wordt het verkeer geblokkeerd en schakelt het niet over naar de tunnel met de volgende prioriteit.
    - Als Kill Switch is uitgeschakeld, schakelt het verkeer over naar de tunnel met de volgende prioriteit en wordt het met de regels van die tunnel vergeleken.

3. De tunnel **All Other Traffic** is standaard ingeschakeld zodat verkeer dat niet met de VPN-tunnels overeenkomt nog steeds internettoegang heeft.

    - Als dit is ingeschakeld, wordt niet-overeenkomend of overgeschakeld verkeer via het lokale WAN gerouteerd.
    - Als dit is uitgeschakeld, wordt Kill Switch versterkt en normale internettoegang geblokkeerd om IP-lekken te voorkomen.

#### Tunnel Options {#tunnel-options_1}

Je kunt voor elke VPN-tunnel geavanceerde instellingen configureren, zoals VPN Kill Switch, IP Masquerading en MTU.

Klik op het tandwielpictogram naast een tunnelnaam en selecteer **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: wanneer dit is ingeschakeld, wordt verkeer dat via deze VPN-tunnel wordt gerouteerd automatisch geblokkeerd als de VPN-verbinding uitvalt. Wanneer dit is uitgeschakeld, schakelt het verkeer over naar de tunnel met de volgende prioriteit of naar het lokale WAN.

- **Services from GL.iNet Use VPN**: wanneer dit is ingeschakeld, verzenden GoodCloud, DDNS en rtty pakketten via VPN-tunnels. Deze optie is standaard uitgeschakeld, omdat deze diensten gewoonlijk het werkelijke IP-adres nodig hebben.

- **Allow Remote Access the LAN Subnet**: wanneer dit is ingeschakeld, is externe toegang tot deze router en de LAN-apparaten via VPN toegestaan. De VPN-server moet een route naar het LAN-subnet van deze router bekendmaken.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en Laptop (192.168.10.200) op het reis-LAN verkeer naar de thuis-NAS (192.168.8.100) stuurt, herschrijft de reisrouter het bron-IP van `192.168.10.200` naar het tunneladres `10.1.0.2`. De serverzijde ziet het verkeer daardoor als afkomstig van de client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: afkorting van Maximum Transmission Unit. De MTU-waarde die je voor de tunnel instelt, overschrijft de waarde in het configuratiebestand.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
