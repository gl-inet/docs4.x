# ExpressVPN-activeringshandleiding {#expressvpn-activation-guide}

**Opmerking:** deze handleiding geldt alleen voor de gezamenlijke GL.iNet x ExpressVPN-router **Fortify (GL-MT6000)**.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} is een toonaangevende premium VPN-dienst die je online privacy en internetverbinding beschermt en veilig streamen vanaf elke locatie mogelijk maakt. De dienst biedt zeer hoge snelheden, krachtige versleuteling en toegang tot servers in meer dan 100 landen. ExpressVPN biedt een snelle en veilige ervaring voor streamen, privé browsen en bescherming op openbare Wi-Fi.

**Fortify (GL-MT6000)** is een router die gezamenlijk door GL.iNet en ExpressVPN wordt uitgebracht. Elk apparaat wordt geleverd met een gratis ExpressVPN-abonnement van één jaar. Je kunt het abonnement activeren en je account rechtstreeks via het webbeheerpaneel verbinden. Wanneer een ExpressVPN-tunnel is verbonden, versleutelt en routeert de router het verkeer volgens je VPN-beleidsinstellingen via die tunnel.

Deze handleiding beschrijft hoe je het ExpressVPN-abonnement van 12 maanden via het webbeheerpaneel activeert. Ook leer je VPN-beleid aan je gebruik en vereisten aan te passen voor een versleutelde, veilige en snelle internetverbinding.

## ExpressVPN-abonnement activeren {#redeem-expressvpn-plan}

Meld je aan bij het webbeheerpaneel van Fortify en ga naar **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Lees **Terms of Service** en **Privacy Policy**, ga ermee akkoord en klik op **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Klik op **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

Voer in het pop-upvenster je **Order ID** in. Als je de router in de GL.iNet Store hebt gekocht, is ook **Order Email** vereist. Klik vervolgens op **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

ExpressVPN Checkout wordt geopend. Rechts is een activeringscode toegepast waarmee je zonder extra kosten een abonnement van 12 maanden activeert.

Voer bovenaan je e-mailadres in en voeg een betaalmethode toe om na de eerste termijn ononderbroken VPN-toegang te behouden. Klik vervolgens op **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Je abonnement is geactiveerd. Ga terug naar het webbeheerpaneel van Fortify en meld je aan met je account.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Aanmelden bij ExpressVPN {#log-in-to-expressvpn}

Ga in het webbeheerpaneel van Fortify naar **VPN** -> **VPN Client Profile**.

Klik op **Log in to ExpressVPN**. De beveiligde aanmeldpagina van ExpressVPN wordt geopend.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Voer je e-mailadres in en klik op **Send Code**. Er wordt een verificatiecode van 6 cijfers naar je e-mailadres gestuurd.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Voer de verificatiecode in en klik op **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Wijzig je wachtwoord om je account te activeren.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

Klik in de volgende stap op **Yes** om ExpressVPN-toegang op je router toe te staan.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Het aanmelden is geslaagd. Je kunt dit browservenster sluiten en teruggaan naar je apparaat.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

Ga in het webbeheerpaneel van Fortify naar **VPN** -> **VPN Client Profile**.

Je bent op deze router aangemeld bij ExpressVPN. Klik op **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Je kunt nu VPN-tunnels toevoegen en VPN-beleid naar behoefte configureren.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## VPN-tunnel toevoegen {#add-vpn-tunnel}

### Algemene stappen {#general-steps}

Volg de onderstaande stappen om een VPN-tunnel toe te voegen en VPN-beleid te configureren. Raadpleeg zo nodig [Voorbeeldsituaties](#case-reference).

1. Ga in het webbeheerpaneel van Fortify naar **VPN** -> **ExpressVPN Dashboard**. Klik op **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Selecteer een VPN-profiel en klik op **Next**.

    Er verschijnt een lijst met ExpressVPN-profielen. Selecteer een of meer profielen en pas zo nodig rechts de prioriteit aan.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        Wanneer meerdere profielen zijn geselecteerd, probeert de tunnel ze op volgorde van prioriteit totdat een verbinding tot stand is gebracht. Als geen enkel profiel in één tunnel verbinding kan maken, bepaalt het systeem op basis van Kill Switch onder [Tunnel Options](#tunnel-options) en [All Other Traffic](#all-other-traffic) of naar het lokale netwerk (WAN) wordt overgeschakeld.

3. Selecteer de clientbron en klik op **Next**.

    Er zijn vier opties:

    - **All Clients**: verkeer van alle apparaten komt met deze regel overeen.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: verkeer van opgegeven verbindingstypen, zoals LAN-subnet, Drop-in Gateway en Guest Network, komt met deze regel overeen.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, komt met deze regel overeen.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: verkeer van opgegeven apparaten, geïdentificeerd via het MAC-adres, komt niet met deze regel overeen.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Selecteer de doelbestemming en klik op **Apply**.

    Er zijn drie opties:

    - **All Targets**: verkeer dat met deze regel overeenkomt, wordt naar alle doelen gerouteerd.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: verkeer dat met deze regel overeenkomt, wordt naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: verkeer dat met deze regel overeenkomt, wordt niet naar opgegeven domeinen of IP-adressen gerouteerd. Je moet deze handmatig invoeren.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. De VPN-tunnel is toegevoegd. **ExpressVPN Dashboard** wordt geopend. Voeg zo nodig meer VPN-tunnels toe.

### Voorbeeldsituaties {#case-reference}

Hieronder staan twee veelvoorkomende VPN-beleidsconfiguraties met stapsgewijze instructies.

??? note "Situatie 1: alleen opgegeven apparaten via VPN routeren"

    **Vereisten:**

    1. Alleen bepaalde apparaten op deze router gebruiken internet via de VPN. Alle andere apparaten gebruiken internet via het lokale WAN.

    2. De geselecteerde apparaten mogen alleen de VPN-verbinding gebruiken. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor deze apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

    **Configuratiestappen:**

    1. Selecteer een VPN-profiel.

        Selecteer een of meer profielen, pas zo nodig rechts de prioriteit aan en klik op **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Selecteer de clientbron.

        Open het tabblad **Specified Devices**, selecteer de apparaten die de VPN moeten gebruiken en klik op **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Selecteer de doelbestemming.

        Open het tabblad **All Targets**, stel dit in als verkeersbestemming en klik op **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

    4. ExpressVPN Dashboard wordt geopend. De VPN-tunnel is toegevoegd.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Controleer of **Kill Switch** voor deze tunnel is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor verkeer dat met deze tunnel overeenkomt geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Controleer of **Allow Non-VPN Traffic** is ingeschakeld. Dit is standaard ingeschakeld zodat verkeer dat niet met de VPN-tunnel overeenkomt via het lokale WAN internet kan gebruiken.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Klik op de middelste knop om deze tunnel te activeren.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Nadat de verbinding tot stand is gebracht, toont de pagina de VPN-verbindingsgegevens, waaronder VPN-beleid, virtueel IP-adres van de client, serveradres, luisterpoort en verkeersstatistieken.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Nu gebruiken alleen de twee opgegeven apparaten internet via de VPN. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor deze apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen. Alle andere apparaten gebruiken het lokale WAN.

??? note "Situatie 2: alle apparaten voor bepaalde websites via VPN 1 routeren en al het overige verkeer via VPN 2"

    **Vereisten:**

    1. Alle apparaten gebruiken VPN Tunnel 1 voor websites van bepaalde sociale media en streamingdiensten en VPN Tunnel 2 voor alle overige internettoegang.

    2. Als de VPN-tunnels onverwacht worden verbroken, wordt internettoegang voor alle apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

    **Configuratiestappen:**

    1. Selecteer een VPN-profiel voor Tunnel 1.

        Selecteer een of meer profielen, pas zo nodig rechts de prioriteit aan en klik op **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Selecteer de clientbron.

        Open het tabblad **All Clients**, stel dit in als clientbron voor Tunnel 1 en klik op **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Selecteer de doelbestemming.

        Open het tabblad **Specified Domain / IP List**, voer domeinen van bepaalde sociale media en streamingdiensten in zoals hieronder en klik op **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. ExpressVPN Dashboard wordt geopend. VPN-tunnel 1 is toegevoegd.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Controleer of **Kill Switch** voor Tunnel 1 is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor overeenkomend verkeer geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Klik op **Add New Tunnel** om Tunnel 2 toe te voegen.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Selecteer een VPN-profiel voor Tunnel 2.

        Selecteer een of meer profielen, pas zo nodig rechts de prioriteit aan en klik op **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

8. Selecteer de clientbron.

        Open het tabblad **All Clients**, stel dit in als clientbron voor Tunnel 2 en klik op **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

9. Selecteer de doelbestemming.

        Open het tabblad **All Targets**, stel dit in als verkeersbestemming voor Tunnel 2 en klik op **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. VPN Dashboard wordt geopend. VPN-tunnel 2 is toegevoegd.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Controleer of **Kill Switch** voor Tunnel 2 is ingeschakeld. Als de VPN onverwacht wordt verbroken, wordt internettoegang voor overeenkomend verkeer geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Klik rechtsboven op het tandwielpictogram, schakel **Enhanced Kill Switch** in en klik op **Apply**. Hierdoor kan al het verkeer internet alleen via VPN bereiken.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        Na toepassing verschijnt **Enhanced Kill Switch** bovenaan de pagina.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Klik op de middelste knop om Tunnel 1 en Tunnel 2 te activeren.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Nadat de verbinding tot stand is gebracht, toont de pagina de VPN-verbindingsgegevens, waaronder VPN-beleid, virtueel IP-adres van de client, serveradres, luisterpoort en verkeersstatistieken.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Alle apparaten gebruiken nu **VPN Tunnel 1** voor de opgegeven domeinen en **VPN Tunnel 2** voor alle overige internettoegang. Als de VPN-tunnels onverwacht worden verbroken, wordt internettoegang voor alle apparaten geblokkeerd om DNS-lekken en IP-tracking te voorkomen.

## Kill Switch {#kill-switch}

Een VPN Kill Switch voorkomt dat verkeer bij een mislukte VPN-verbinding terugvalt op een niet-versleutelde internetverbinding.

Als **Kill Switch** voor een afzonderlijke tunnel is ingeschakeld, wordt internettoegang voor het toegewezen verkeer geblokkeerd wanneer de verbinding mislukt. Ander verkeer volgt de instellingen van **All Other Traffic**.

**Enhanced Kill Switch** blokkeert internetverkeer dat niet met een VPN-tunnel overeenkomt. De instelling **Kill Switch** van afzonderlijke tunnels wordt niet overschreven.

Fortify ondersteunt Kill Switch-configuratie voor de globale VPN-verbinding en elke afzonderlijke VPN-tunnel.

- Raadpleeg [All Other Traffic](#all-other-traffic) om Kill Switch voor de globale VPN-verbinding, Enhanced Kill Switch, in te stellen.

- Raadpleeg [Tunnel Options](#tunnel-options) om Kill Switch voor elke afzonderlijke VPN-tunnel in te stellen.

## All Other Traffic {#all-other-traffic}

Klik rechtsboven op het tandwielpictogram om beleid in te stellen voor verkeer dat niet met een VPN-tunnel overeenkomt.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Dit beleid bepaalt of verkeer dat niet met een VPN-tunnelgroep overeenkomt internet mag gebruiken. Er zijn twee opties: **Allow Non-VPN Traffic** en **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: standaard ingeschakeld voor normale internettoegang voor niet-VPN-verkeer.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: dwingt alle apparaten internet via een VPN te gebruiken. Verkeer dat niet met een VPN-tunnel overeenkomt, wordt geblokkeerd. Deze globale instelling overschrijft de Kill Switch van afzonderlijke VPN-tunnels niet.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Options {#tunnel-options}

Je kunt voor elke VPN-tunnel geavanceerde instellingen configureren, zoals VPN Kill Switch, IP Masquerading en MTU.

Klik in een tunnelgroep op het tandwielpictogram en selecteer **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: wanneer dit is ingeschakeld, wordt verkeer dat met deze VPN-tunnel overeenkomt geblokkeerd als de VPN onverwacht wordt verbroken. Wanneer dit is uitgeschakeld, schakelt dit verkeer over naar de tunnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: wanneer dit is ingeschakeld, verzenden GoodCloud, DDNS en rtty pakketten via VPN-tunnels. Deze optie is standaard uitgeschakeld, omdat deze diensten gewoonlijk het werkelijke IP-adres nodig hebben.

- **Allow Remote Access to the LAN Subnet**: wanneer dit is ingeschakeld, is via de VPN externe toegang tot deze router en de LAN-apparaten toegestaan. De VPN-server moet een route terug naar het LAN-subnet bekendmaken.

- **IP Masquerading**: wanneer dit is ingeschakeld, worden de bron-IP-adressen van LAN-clients herschreven naar het VPN-tunnel-IP van de router. Schakel dit alleen uit voor Site-to-Site-configuraties waarbij de externe peer je LAN-subnets kent.

- **MTU**: de MTU-waarde voor de tunnel overschrijft de MTU-instellingen in het configuratiebestand.

## Tunnelprioriteit {#tunnel-priority}

Klik in een tunnelgroep op het tandwielpictogram en selecteer **Priority** om de tunnelprioriteit aan te passen.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Klik rechts op het pictogram met drie lijnen, houd dit vast om de tunnels te herschikken en klik op **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

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
