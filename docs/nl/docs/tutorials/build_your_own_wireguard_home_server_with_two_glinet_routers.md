# Je eigen WireGuard-thuisserver bouwen met twee GL.iNet-routers {#build-your-own-wireguard-home-server-with-two-glinet-routers}

In dit artikel lees je hoe je je thuisrouter instelt als WireGuard VPN-server en je reisrouter als WireGuard VPN-client. Zo kun je deze op afstand met elkaar verbinden en overal met de reisrouter je IP-adres thuis gebruiken.

Bekijk deze video of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In deze video worden GL-MT5000 (Brume 3) en GL-MT3600BE (Beryl 7) gebruikt om de VPN-configuratie te demonstreren.)</small>

In de volgende stappen gebruiken we GL-MT6000 (Flint 2) en GL-MT3000 (Beryl AX) als voorbeelden:

- GL-MT6000, een thuisrouter, wordt ingesteld als WireGuard VPN-server. Als draadloze capaciteit niet nodig is, kun je ook onze beveiligingsgateway GL-MT2500 of andere modellen gebruiken.

- GL-MT3000, een reisrouter, wordt ingesteld als WireGuard VPN-client die op afstand verbinding maakt met de VPN-server thuis.

## Voordelen van een eigen WireGuard-thuisserver {#why-build-your-own-wireguard-home-server}

1. Gebruik het openbare IP-adres van je thuisverbinding, zodat je verkeer van thuis lijkt te komen.
2. Bespaar de maandelijkse kosten van een externe VPN-dienst.
3. Bescherm je privacy door al je internetverkeer via een versleutelde tunnel naar je thuisnetwerk te sturen.
4. Krijg overal toegang tot je apparaten thuis en lokale streamingdiensten.

## Voorbereidingen {#preparations}

### Controleren of je een openbaar IP-adres hebt {#check-if-you-have-a-public-ip}

Controleer eerst of de GL-MT6000 aan de WAN-zijde een openbaar IP-adres heeft, zodat deze wereldwijd toegankelijk is. Anders kan je reisrouter onderweg geen VPN-verbinding met de router tot stand brengen.

Open een webbrowser en voer [what is my ip](https://whatismyipaddress.com/){target="_blank"} in de adresbalk in om te controleren of je een openbaar IP-adres hebt.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Je openbare IP-adres wordt weergegeven. Als dit overeenkomt met het WAN-IP-adres dat je ISP aan de GL-MT6000 heeft toegewezen, heb je een openbaar IP-adres.

Als je geen openbaar IP-adres hebt, kun je de volgende methoden proberen.

1. Als je een hoofdrouter hebt, meld je daar dan bij aan en controleer of deze het openbare IP-adres van je ISP ontvangt.
2. Vraag je ISP om een openbaar IP-adres. Hiervoor kunnen extra kosten gelden.
3. Als de bovenstaande twee methoden niet werken, bijvoorbeeld omdat je netwerk zich achter CGNAT bevindt, kun je onze SD-WAN-oplossing [AstroWarp](../interface_guide/astrowarp.md){target="_blank"} proberen.

### Controleren of port forwarding vereist is {#check-if-port-forwarding-is-required}

??? "GL.iNet als hoofdrouter"

    Als je GL.iNet-router met een ethernetkabel rechtstreeks op een ISP-modem is aangesloten, is de GL.iNet-router de hoofdrouter.

    **Hoe controleer je of je GL.iNet-router rechtstreeks met het ISP-modem is verbonden?**

    Meld je aan bij het webbeheerpaneel van de GL.iNet-router. Selecteer **INTERNET** in de linkerzijbalk en controleer de netwerktopologie en de verbindingsgegevens.

    Bij een rechtstreekse ethernetverbinding zie je een gedeelte met de naam "Ethernet", met gegevens zoals het protocol, het IP-adres en de gateway.

    In de volgende afbeelding is het gemarkeerde IP-adres het WAN-IP-adres dat de ISP aan deze GL.iNet-router heeft toegewezen.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Dit WAN-IP-adres is een openbaar IP-adres. Deze GL.iNet-router fungeert dus als hoofdrouter, heeft een openbaar IP-adres en **hiervoor hoeft geen port forwarding te worden ingesteld**.

    Je hoeft deze GL.iNet-router alleen als WireGuard-server in te stellen en een reisrouter als WireGuard-client die verbinding maakt met de server. Er wordt vervolgens een VPN-tunnel tussen beide routers opgebouwd.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet als subrouter"

    Stel **Port Forwarding** op je hoofdrouter in voor de GL.iNet-router als deze zich achter NAT bevindt.

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Voorbeeld: een TP-Link-router als hoofdrouter thuis.

    Maak verbinding met het Wi-Fi-netwerk of LAN van je thuisrouter. Meld je vervolgens aan bij het webbeheerpaneel. Controleer welk WAN-IP-adres de router van je ISP ontvangt. In de onderstaande afbeelding is je openbare IP-adres **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Voordat je port forwarding instelt, raden we aan op je hoofdrouter een IP-adres voor de GL.iNet-router te reserveren. Zo wordt een vast IP-adres aan de GL.iNet-router toegewezen.** Anders kan de hoofdrouter na het opnieuw opstarten van de hoofdrouter of GL.iNet-router een ander IP-adres aan de GL.iNet-router toewijzen, waardoor de port-forwardingregel niet meer werkt.

    Stel vervolgens Port Forwarding op je hoofdrouter in voor de GL.iNet-router.

    1. Ga naar “Advanced”, klik op “virtual Server” en vervolgens op “Add”.

    2. Internal IP (Device IP): dit is het IP-adres dat aan de GL.iNet-router is toegewezen. Je vindt dit in de clientlijst van TP-Link.

    3. External/Internal port: voer voor beide "51820" in.

    4. Protocol: selecteer "All or UDP or TCP/UDP".

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Meer voorbeelden van [Port Forward](how_to_set_up_port_forwarding.md)**

## De WireGuard-server instellen {#set-up-wireguard-server}

1. Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **WireGuard Server**. Klik bij de eerste configuratie van de VPN-server op **Generate Configuration**.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Controleer de configuratie.

    De onderstaande standaardconfiguratie werkt in de meeste gevallen.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** is het IP-adres van de WireGuard-tunnel. Laat het adres staan zolang het niet conflicteert met de gateway van je upstream router.

        Wijzig het adres bij een conflict in bijvoorbeeld **10.1.0.1/24** en klik op **Apply**. Voeg de CIDR-notatie ‘/24’ toe om verbindingsproblemen te voorkomen.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Een upstream Xfinity-router kan bijvoorbeeld het IP-adres 10.0.0.1 hebben. Op sommige GL.iNet-routers kan dit adres conflicteren met het IP-adres van de WireGuard-tunnel. Wijzig het tunneladres alleen bij een conflict.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 is standaard uitgeschakeld op GL.iNet-routers. Schakel [IPv6](../interface_guide/ipv6.md) in op je router als je een IPv6-adres wilt gebruiken.

    - **Listen Port**. De WireGuard-server luistert standaard op UDP-poort `51820`. Als je deze poort wijzigt en port forwarding gebruikt, pas dan de regel op de upstream router aan zodat deze verkeer doorstuurt naar de nieuwe luisterpoort van de server. Gebruik de externe poort van de portforwardingregel in het veld `Endpoint` van elk clientprofiel. Gebruik de luisterpoort van de server als die rechtstreeks bereikbaar is.

    - **Enable Obfuscation**. Als deze optie is ingeschakeld, gebruikt de VPN-server het AmneziaWG-protocol om VPN-verkeer te verhullen. We raden aan de standaardinstellingen te behouden en ze alleen te wijzigen als je bekend bent met deze parameters.

        - [AmneziaWG-obfuscatie op GL.iNet-routers](../faq/amneziawg_obfuscation.md)
        - [VPN-obfuscatie instellen op GL.iNet-routers](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Voeg een profiel toe.

    Open het tabblad **Profiles** en klik op **Add** om een profiel voor je apparaat te maken.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Geef het profiel een herkenbare naam en klik op **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Klik zo nodig op **Set More** om de geavanceerde instellingen te openen. Klik daarna op **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Zo nodig routeringsregels toevoegen"

        In de meeste gevallen hoef je geen routeringsregels toe te voegen.

        Wil je vanaf de server toegang tot apparaten op het LAN van de WireGuard-client? Open dan het tabblad **Route Rules** op de pagina **WireGuard Server** en stel de regels in. Volg de [instructies voor toegang tot het LAN van de client](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Ga anders verder naar stap 4 om een clientconfiguratie te downloaden.

4. Download de configuratie.

    Nadat je een profiel hebt toegevoegd en op **Apply** hebt geklikt, is de configuratie beschikbaar als QR-code, platte tekst of downloadbaar `.conf`-bestand.

    - **QR-code**. Scan de code in de WireGuard-app om een standaard WireGuard-profiel te importeren. Als je obfuscatie hebt ingeschakeld, gebruik dan de AmneziaWG-app of een andere client die AmneziaWG-obfuscatie ondersteunt.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Platte tekst**. Bekijk de configuratiegegevens en kopieer ze als je de WireGuard-app of een GL.iNet-router handmatig wilt configureren.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf-bestand**. Klik op **Download** om het bestand op je apparaat op te slaan. Je kunt het rechtstreeks importeren in de WireGuard-app of uploaden naar een GL.iNet-router.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    Vanaf firmware v4.8 kun je als serveradres het openbare IP-adres, het DDNS-domein of het huidige WAN-IP-adres opgeven. Als je een ander adres kiest, wordt het serveradres in het configuratiebestand meteen bijgewerkt.

    Als het openbare IP-adres van je netwerk bijvoorbeeld vaak wijzigt, schakel dan [DDNS](../interface_guide/ddns.md) in en gebruik het DDNS-domein als serveradres.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Klik rechtsboven op **Start** om de WireGuard-server te starten. De verbindingsstatus verschijnt op dezelfde pagina.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## De WireGuard-client instellen {#set-up-wireguard-client}

### Het LAN-IP-adres wijzigen {#change-the-lan-ip}

In deze handleiding gebruiken we GL-MT6000 en GL-MT3000 als voorbeelden. Beide hebben standaard het LAN-IP-adres **192.168.8.1**. Om conflicten te voorkomen, moeten we het LAN-IP-adres van een van de routers wijzigen.

Volg de onderstaande stappen om het LAN-IP-adres van de GL-MT3000 te wijzigen. Dit apparaat dient als WireGuard-client.

Meld je aan bij het webbeheerpaneel van de GL-MT3000 en ga naar **NETWORK** -> **LAN**. Wijzig het LAN-IP-adres bijvoorbeeld van de standaardwaarde 192.168.8.1 in `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### De configuratie toevoegen {#add-the-configuration}

Ga in het webbeheerpaneel van de GL-MT3000 naar **VPN** -> **WireGuard Client** en klik op **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Maak links een groep en geef deze een naam. Selecteer vervolgens het configuratiebestand dat je wilt uploaden of sleep het naar het uploadvak rechts.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Klik op **Apply** nadat het bestand is geverifieerd.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Je kunt ook op **Manually Add Configuration** klikken, de configuratietekst plakken en vervolgens op **Apply** klikken.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Nadat het configuratiebestand is geüpload, wordt het op de pagina WireGuard Client weergegeven.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### De verbinding starten {#start-the-connection}

Klik op het pictogram met drie stippen en vervolgens op **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Wacht enkele minuten. Na een geslaagde verbinding licht een groene stip op.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Ga naar **VPN Dashboard**. Je ziet dat je client verbinding maakt met de server via je openbare IP-adres thuis. De pagina kan per firmwareversie enigszins verschillen.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Meld je opnieuw aan bij het webbeheerpaneel van de GL-MT6000, de WireGuard-server, en ga naar **VPN** -> **WireGuard Server**. Als je firmware v.4.7 of ouder gebruikt, ga je naar **VPN** -> **VPN Dashboard**. Hier zie je ook aan de verbindingsstatus dat de client is verbonden.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(De pagina WireGuard Server in FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(De pagina VPN Dashboard in FW v4.7 en ouder)</small>

## Voorbereidingen voor VPN-probleemoplossing op afstand {#prep-for-remote-vpn-fixes-ahead}

Koppel beide routers vóór vertrek aan je GoodCloud-account. Zo kun je op afstand problemen oplossen als de VPN-verbinding uitvalt door configuratieproblemen of andere netwerkproblemen. Externe toegang werkt alleen zolang de routers ingeschakeld blijven en met internet verbonden zijn.

---

Gerelateerde artikelen

- [Een WireGuard-server instellen op GL.iNet-routers](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
