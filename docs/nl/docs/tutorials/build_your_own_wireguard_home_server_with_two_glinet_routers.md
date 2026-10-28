# Je eigen WireGuard-thuisserver bouwen met twee GL.iNet-routers {#build-your-own-wireguard-home-server-with-two-glinet-routers}

In dit artikel lees je hoe je je thuisrouter instelt als WireGuard VPN-server en je reisrouter als WireGuard VPN-client. Zo kun je deze op afstand met elkaar verbinden en overal met de reisrouter je IP-adres thuis gebruiken.

Bekijk deze video of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In deze video worden GL-MT5000 (Brume 3) en GL-MT3600BE (Beryl 7) gebruikt om de VPN-configuratie te demonstreren.)</small>

In de volgende stappen gebruiken we GL-MT6000 (Flint 2) en GL-MT3000 (Beryl AX) als voorbeelden:

- GL-MT6000, een thuisrouter, wordt ingesteld als WireGuard VPN-server. Als draadloze capaciteit niet nodig is, kun je ook onze beveiligingsgateway GL-MT2500 of andere modellen gebruiken.

- GL-MT3000, een reisrouter, wordt ingesteld als WireGuard VPN-client die op afstand verbinding maakt met de VPN-server thuis.

## Waarom je een eigen WireGuard-thuisserver nodig hebt {#why-you-need-to-build-your-own-wireguard-home-server}

1. Gebruik je IP-adres thuis als internetadres, alsof je thuis bent.
2. Je betaalt geen maandelijkse kosten zoals bij een VPN-service van derden.
3. Leid al het internetverkeer via een versleutelde VPN-tunnel naar je thuisnetwerk om je privacy te beschermen.
4. Krijg eenvoudig toegang tot je interne bronnen en lokale streamingdiensten.

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

    Stappen:

    1. Meld je aan bij het GL.iNet Admin Panel.

    2. Selecteer INTERNET in de linkerzijbalk. Controleer de topologie en verbindingsgegevens:

        Bij een rechtstreekse ethernetverbinding zie je een gedeelte met de naam "Ethernet", met gegevens zoals Protocol, IP address en Gateway.

        In de volgende afbeelding is het gemarkeerde IP Address het WAN-IP-adres dat de ISP aan deze GL-iNet-router heeft toegewezen.

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Dit WAN-IP-adres is een openbaar IP-adres. Deze GL.iNet-router fungeert dus als hoofdrouter, heeft een openbaar IP-adres en **hiervoor hoeft geen port forwarding te worden ingesteld**.

        Je hoeft deze GL.iNet-router alleen als WireGuard-server in te stellen en een reisrouter als WireGuard Client die met de server verbinding maakt. Er wordt vervolgens een VPN-tunnel tussen beide routers opgebouwd.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet als subrouter"

    Stel **Port Forwarding** op je hoofdrouter in voor de GL.iNet-router als deze zich achter NAT bevindt.

    Topologie

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

### DDNS inschakelen (optioneel) {#enable-ddns-optional}

Schakel de DDNS-functie in als je geen statisch openbaar IP-adres hebt, maar alleen een dynamisch openbaar IP-adres.

Meld je aan bij het webbeheerpaneel van de GL-MT6000 en ga naar **APPLICATIONS** -> **Dynamic DNS**. Schakel **Enable DDNS** in.

Schakel het selectievakje voor **Terms of Service & Privacy Policy** in en klik op **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Ga vervolgens naar **WireGuard Server** -> het tabblad Configuration, controleer of Listen Port is ingesteld op 51820 en klik op **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Een configuratie genereren {#generate-configuration}

Klik op dezelfde pagina naast het tabblad Configuration op het tabblad **Profiles** en klik vervolgens op **Add** (gemarkeerd met 1 in de onderstaande afbeelding).

Er wordt automatisch een clientconfiguratie gegenereerd. Klik op het **doorstuurpictogram** (gemarkeerd met 2).

Schakel in het pop-upvenster DDNS Domain in (gemarkeerd met 3). Dit is optioneel en mag alleen worden ingeschakeld als je een dynamisch openbaar IP-adres hebt.

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Je kunt vervolgens de QR-code met de WireGuard-[mobiele app](https://www.wireguard.com/install/) scannen om de server te testen. Klik [hier](../interface_guide/wireguard_server.md#check-if-wireguard-server-is-working-properly) voor meer informatie.

Je kunt ook een configuratie in tekstindeling exporteren voor verbinding met een VPN-client.

Schakel de configuratie om van een QR-code naar tekstindeling door op het tabblad **Configuration File** te klikken.

Kopieer de tekst voor de client of klik op Download en sla het bestand op voor later gebruik.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## De WireGuard-client instellen {#set-up-wireguard-client}

### Het LAN-IP-adres wijzigen {#change-the-lan-ip}

In deze handleiding gebruiken we GL-MT6000 en GL-MT3000 als voorbeelden. Beide hebben standaard het LAN-IP-adres **192.168.8.1**. Om conflicten te voorkomen, moeten we het LAN-IP-adres van een van de routers wijzigen.

Volg deze stappen om het LAN-IP-adres van de GL-MT3000, de WireGuard-client, te wijzigen.

Meld je aan bij het webbeheerpaneel van de GL-MT3000 en ga in de linkerzijbalk naar **NETWORK** -> **LAN** om het LAN-IP-adres te wijzigen. Je kunt het LAN-IP-adres bijvoorbeeld wijzigen van de standaardwaarde 192.168.8.1 in `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Klik [hier](../interface_guide/lan.md) voor meer informatie over de LAN-interface.

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

Je server kan soms uitvallen door een stroomstoring of een andere oorzaak. Koppel de server aan GL.iNet GoodCloud om deze toegankelijk te houden.

---

Gerelateerde artikelen

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
