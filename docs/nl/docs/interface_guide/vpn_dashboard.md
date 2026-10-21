# VPN Dashboard {#vpn-dashboard}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.9.x en hoger. Als je apparaat een andere firmwareversie gebruikt, kies je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.9 and above" markdown="1">

- [Firmware v4.7 and earlier](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

On the left side of the web Admin Panel, go to **VPN** -> **VPN Dashboard**.

Het VPN-dashboard toont verbindingsgegevens zoals routeringsregels, de verbonden server, verkeersstatistieken, het virtuele client-IP en het verbindingslogboek. Je kunt er ook geavanceerde instellingen zoals VPN Kill Switch, IP Masquerading en MTU configureren.

Compared to firmware v4.8, v4.9 includes the following improvements to the VPN Dashboard:

1. **Allow users to select multiple profiles within a tunnel group and set their priority**. The tunnel will attempt to connect using each profile in priority order until a connection is successfully established.

2. **Elke tunnelgroep werkt onafhankelijk en voert geen failover tussen groepen uit**. Als alle profielen binnen één tunnel geen verbinding kunnen maken, bepaalt het systeem aan de hand van Tunnel Kill Switch en de tunnel All Other Traffic of naar het lokale WAN wordt overgeschakeld.

## Upload VPN Profile {#upload-vpn-profile}

Als je deze pagina voor het eerst opent en nog geen tunnels zijn gemaakt, ziet de pagina er als volgt uit. Klik op **Add VPN Tunnel** om te beginnen.

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Je wordt naar de pagina **VPN Client Profile** geleid. Selecteer een VPN-provider en meld je aan.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. De VPN-providers in de bovenstaande afbeelding zijn geïntegreerd in het webbeheerpaneel van de GL.iNet-router. Met een actief abonnement voer je eenvoudig je aanmeldgegevens in om direct configuratiebestanden voor VPN-verbindingen te verkrijgen.

    2. Als je een abonnement bij een andere VPN-provider hebt of je eigen VPN-configuraties wilt uploaden, klik je op **Add Manually** en upload je de configuraties.

Neem [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als voorbeeld. Klik op PureVPN en meld je aan met geldige gegevens.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Je krijgt een lijst met VPN-profielen. Bij sommige VPN-serviceproviders moet je eerst een VPN-protocol of gewenste servers of steden selecteren voordat de lijst verschijnt.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Klik onderaan op **Go to Dashboard**. Je wordt naar het VPN-dashboard geleid om een VPN-tunnel toe te voegen en VPN-beleid te configureren.

## VPN-tunnel toevoegen {#add-vpn-tunnel}

### Algemene stappen {#general-steps}

Volg de onderstaande stappen om een VPN-tunnel toe te voegen en VPN-beleid te configureren. Raadpleeg zo nodig [Voorbeeldsituaties](#case-reference).

1. Klik op het VPN-dashboard op **Add VPN Tunnel**. Rechts verschijnt een VPN-installatiewizard.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Select VPN profile.

    Selecteer een of meer profielen, pas rechts zo nodig hun prioriteit aan en klik op **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Opmerking**: als je meerdere profielen selecteert, probeert de tunnel deze op volgorde van prioriteit totdat een verbinding tot stand komt. Als alle profielen binnen één tunnel mislukken, bepaalt het systeem aan de hand van Kill Switch onder [Tunnel Options](#tunnel-options) en de instellingen onder [All Other Traffic](#all-other-traffic) of naar het lokale WAN van de router wordt overgeschakeld.

3. Selecteer de clientbron en klik op **Next**.

    Er zijn vier opties:

    - **All Clients**: verkeer van alle apparaten komt met deze regel overeen.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: verkeer van opgegeven verbindingstypen, zoals LAN-subnet, Drop-in Gateway en Guest Network, komt met deze regel overeen.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, komt met deze regel overeen.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, komt niet met deze regel overeen.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Selecteer de doelbestemming en klik op **Apply**.

    Er zijn drie opties:

    - **All Targets**: verkeer dat met deze regel overeenkomt, wordt naar alle doelen gerouteerd.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: verkeer dat met deze regel overeenkomt, wordt naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: verkeer dat met deze regel overeenkomt, wordt niet naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. De VPN-tunnel is toegevoegd. Je wordt naar het **VPN Dashboard** geleid. Voeg zo nodig meer VPN-tunnels toe.

    Controleer om veiligheidsredenen de status van **Kill Switch** onder [All Other Traffic](#all-other-traffic) en [Tunnel Options](#tunnel-options) voordat je de VPN-tunnel inschakelt.

### Voorbeeldsituaties {#case-reference}

Hieronder staan twee veelvoorkomende VPN-beleidsconfiguraties met stapsgewijze instructies.

??? note "Situatie 1: alleen opgegeven apparaten via VPN routeren"

    **Vereisten:**

    1. Alleen bepaalde apparaten op deze router gebruiken internet via de VPN. Alle andere apparaten gebruiken internet via het lokale WAN.

    2. De geselecteerde apparaten mogen alleen de VPN-verbinding gebruiken. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor deze apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

    **Configuratiestappen:**

    1. Selecteer een VPN-profiel.

        Als je je bij een geïntegreerde VPN-dienst hebt aangemeld of een configuratiebestand hebt geüpload, worden de beschikbare profielen hier vermeld. Ga anders naar **VPN Client Profile** om je aan te melden of handmatig een configuratiebestand te uploaden.

        Neem [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als voorbeeld. Selecteer een of meer profielen en pas rechts zo nodig hun prioriteit aan.

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Selecteer de clientbron.

        Open het tabblad **Specified Devices**, selecteer de apparaten die de VPN gebruiken en klik op **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Selecteer de doelbestemming.

        Open het tabblad **All Targets**, stel dit in als verkeersbestemming en klik op **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Je wordt naar het VPN-dashboard geleid. De VPN-tunnel is nu toegevoegd, zoals hieronder weergegeven.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Controleer of **Kill Switch** voor deze tunnel is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor verkeer dat met deze tunnel overeenkomt geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

    6. Controleer of **Allow Non-VPN Traffic** is ingeschakeld. Dit is standaard ingeschakeld zodat verkeer dat niet met de VPN-tunnel overeenkomt via het lokale WAN internettoegang houdt.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Klik op de middelste knop om deze tunnel te activeren.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Zodra de verbinding tot stand is gebracht, toont de pagina de VPN-verbindingsgegevens, waaronder VPN-beleid, verkeersstatistieken, serveradres, luisterpoort en virtueel IP-adres.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Alleen de twee opgegeven apparaten gebruiken nu internet via de VPN. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor deze apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen. Alle overige apparaten gebruiken internet via het lokale WAN.

??? note "Situatie 2: alle apparaten voor bepaalde websites via VPN 1 routeren en al het overige verkeer via VPN 2"

    **Vereisten:**

    1. Alle apparaten gebruiken **VPN Tunnel 1** voor domeinen van bepaalde sociale media en streamingdiensten en **VPN Tunnel 2** voor alle overige internettoegang.

    2. Als de VPN-tunnels onverwacht worden verbroken, wordt internettoegang voor alle apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

    **Configuratiestappen:**

    1. Selecteer het VPN-profiel voor Tunnel 1.

        Als je je bij een geïntegreerde VPN-dienst hebt aangemeld of een configuratiebestand hebt geüpload, worden de beschikbare profielen hier vermeld. Ga anders naar **VPN Client Profile** om je aan te melden of handmatig een configuratiebestand te uploaden.

        Neem [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als voorbeeld. Selecteer een of meer profielen, pas rechts zo nodig hun prioriteit aan en klik op **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Selecteer de clientbron.

        Open het tabblad **All Clients**, stel dit in als clientbron voor Tunnel 1 en klik op **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Selecteer de doelbestemming.

        Open het tabblad **Specified Domain / IP List**, voer domeinen van enkele veelgebruikte sociale media en streamingdiensten in zoals hieronder weergegeven en klik op **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Je wordt naar het VPN-dashboard geleid. VPN-tunnel 1 is nu toegevoegd.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Controleer of **Kill Switch** voor Tunnel 1 is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor overeenkomend verkeer geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

    6. Klik op **Add New Tunnel** om Tunnel 2 toe te voegen.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Selecteer een VPN-profiel voor Tunnel 2.

        Neem [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als voorbeeld. Selecteer een of meer profielen en pas rechts zo nodig hun prioriteit aan.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

8. Selecteer de clientbron.

        Open het tabblad **All Clients**, stel dit in als clientbron voor Tunnel 2 en klik op **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Selecteer de doelbestemming.

        Open het tabblad **All Targets**, stel dit in als verkeersbestemming voor Tunnel 2 en klik op **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Je wordt naar het VPN-dashboard geleid. VPN-tunnel 2 is nu toegevoegd.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Controleer of **Kill Switch** voor Tunnel 2 is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor overeenkomend verkeer geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Klik rechtsboven op het tandwielpictogram en schakel **Enhanced Kill Switch** in. Hierdoor moet al het verkeer internet via de VPN gebruiken.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Klik op de middelste knop om Tunnel 1 en Tunnel 2 te activeren.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Zodra de verbinding tot stand is gebracht, toont de pagina de VPN-verbindingsgegevens, waaronder VPN-beleid, verkeersstatistieken, serveradres, luisterpoort en virtueel IP-adres.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Alle apparaten gebruiken nu **VPN Tunnel 1** voor toegang tot de opgegeven domeinen en **VPN Tunnel 2** voor alle overige internettoegang. Als de VPN-tunnels onverwacht worden verbroken, wordt internettoegang voor alle apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

## Kill Switch {#kill-switch}

!!! Tip "What is Kill Switch?"

    Een VPN Kill Switch voorkomt dat verkeer bij het uitvallen van een VPN-verbinding terugvalt op een niet-versleutelde internetverbinding.

    Als je **Kill Switch** voor een afzonderlijke tunnel inschakelt, wordt internettoegang voor het aan die tunnel toegewezen verkeer geblokkeerd wanneer de verbinding uitvalt. Ander verkeer volgt de instellingen onder **All Other Traffic**.

    **Enhanced Kill Switch** blokkeert internetverkeer dat met geen enkele VPN-tunnel overeenkomt. Deze functie overschrijft de instelling **Kill Switch** van afzonderlijke tunnels niet.

Vanaf firmware v4.8 ondersteunen GL.iNet-routers Kill Switch-configuratie voor de globale VPN-verbinding en voor elke afzonderlijke VPN-tunnel.

- Raadpleeg [All Other Traffic](#all-other-traffic) om Kill Switch voor de globale VPN-verbinding, Enhanced Kill Switch, in te stellen.

- Raadpleeg [Tunnel Options](#tunnel-options) om Kill Switch voor elke afzonderlijke VPN-tunnel in te stellen.

## All Other Traffic {#all-other-traffic}

Klik rechtsboven op het tandwielpictogram om beleid in te stellen voor verkeer dat met geen enkele VPN-tunnel overeenkomt.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Dit beleid bepaalt of verkeer dat met geen van je VPN-tunnelgroepen overeenkomt internettoegang heeft. Er zijn twee opties: **Allow Non-VPN Traffic** en **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: standaard ingeschakeld voor normale internettoegang voor niet-VPN-verkeer.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: dwingt alle apparaten internet via een VPN te gebruiken. Verkeer dat niet met een VPN-tunnel overeenkomt, wordt geblokkeerd. Deze globale instelling overschrijft de Kill Switch van afzonderlijke VPN-tunnels niet.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Options {#tunnel-options}

Je kunt voor elke VPN-tunnel geavanceerde instellingen configureren, zoals VPN Kill Switch, IP Masquerading en MTU.

Klik in een tunnelgroep op het tandwielpictogram en selecteer **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: wanneer dit is ingeschakeld, wordt verkeer dat met deze VPN-tunnel overeenkomt geblokkeerd als de VPN onverwacht wordt verbroken. Wanneer dit is uitgeschakeld, schakelt dit verkeer over naar de tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: wanneer dit is ingeschakeld, verzenden GoodCloud, DDNS en rtty pakketten via VPN-tunnels. Deze optie is standaard uitgeschakeld, omdat deze diensten gewoonlijk het werkelijke IP-adres nodig hebben.

- **Allow Remote Access to the LAN Subnet**: wanneer dit is ingeschakeld, is via de VPN externe toegang tot deze router en de LAN-apparaten toegestaan. De VPN-server moet een route terug naar het LAN-subnet bekendmaken.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

    Als IP Masquerading is ingeschakeld en Laptop (192.168.10.200) op het reis-LAN verkeer naar de thuis-NAS (192.168.8.100) stuurt, herschrijft de reisrouter het bron-IP van `192.168.10.200` naar het tunneladres `10.1.0.2`. De serverzijde ziet het verkeer daardoor als afkomstig van de client.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU**: de MTU-waarde voor de tunnel overschrijft de MTU-instellingen in het configuratiebestand.

## Tunnelprioriteit {#tunnel-priority}

Klik in een tunnelgroep op het tandwielpictogram en selecteer **Priority** om de tunnelprioriteit aan te passen.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Klik rechts op het pictogram met drie lijnen, houd dit vast om de tunnels te herschikken en klik op **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Wanneer meerdere tunnels zijn ingeschakeld, routeert de router verkeer volgens de volgende regels**:

1. Verkeer wordt eerst vergeleken met de tunnelregel met de hoogste prioriteit. Bij een overeenkomst wordt het via die tunnel gerouteerd; anders wordt de volgende tunnel geprobeerd.

2. Elke tunnelgroep werkt onafhankelijk. Zodra verkeer met een tunnelregel overeenkomt, wordt het via die tunnel gerouteerd en vindt geen failover tussen tunnelgroepen plaats.

3. Binnen elke tunnelgroep kun je meerdere profielen selecteren voor failover binnen de tunnel. Als het profiel met de hoogste prioriteit uitvalt, maakt de tunnel automatisch verbinding via het profiel met de op één na hoogste prioriteit.

4. Als een VPN-tunnel onverwacht wordt verbroken, bepaalt het systeem op basis van **Kill Switch** of het verkeer naar de tunnel All Other Traffic overschakelt.

    - Als Kill Switch is ingeschakeld, wordt verkeer geblokkeerd en schakelt het niet over naar All Other Traffic.
    - Als Kill Switch is uitgeschakeld, schakelt verkeer over naar All Other Traffic.

5. In de tunnel **All Other Traffic** bepalen verschillende modi of verkeer dat niet met de VPN-tunnel overeenkomt internet mag gebruiken.

    - **Allow Non-VPN Traffic**: standaard ingeschakeld zodat verkeer dat niet met VPN-tunnels overeenkomt via het lokale WAN internet kan gebruiken.

    - **Enhanced Kill Switch**: dwingt alle apparaten internet via een VPN te gebruiken. Verkeer dat niet met een VPN-tunnel overeenkomt, wordt geblokkeerd. Deze globale instelling overschrijft Kill Switch van afzonderlijke VPN-tunnels niet. De functie versterkt Kill Switch en blokkeert normale internettoegang om IP-lekken te voorkomen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
