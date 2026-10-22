# Wat moet ik doen als de WireGuard-server niet goed werkt? {#what-should-i-do-if-the-wireguard-server-is-not-working-properly}

Er zijn verschillende mogelijke oorzaken als de WireGuard-server op je GL.iNet-router niet goed werkt.

Volg de stappen die bij jouw probleem horen.

## Situatie 1. De WireGuard-server start, maar er kan geen verbinding worden gemaakt {#situation-1-the-wireguard-server-is-starting-but-cant-be-connected}

??? "Volg deze stappen"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Port forwarding op de primaire router naar de secundaire GL.iNet-router werkt mogelijk niet goed.
    Stuur de HTTPS-poort van de primaire router door naar de WireGuard-server om port forwarding te controleren:

    1. Stuur de HTTPS-poort van de primaire router door naar de WireGuard-server

        1. Meld je aan bij het beheerpaneel van de primaire router.
        2. Ga naar het scherm voor port forwarding.
        3. Maak een nieuwe poortregel aan en noem deze **HTTPS**.
        4. Voer de volgende gegevens in:
            * **External port/Internal port:** voer **443** in.
            * **Protocol:** kies **All** of **UDP/TCP**.
            * **Internal IP** (of **Host IP**): voer het WAN-IP-adres van de secundaire router in of selecteer deze in de keuzelijst.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. DDNS en externe HTTPS-toegang inschakelen op de GL.iNet-router

        1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
        2. Klik links op **Applications** > **Dynamic DNS**.
        3. Schakel **Enable DDNS** in en selecteer **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Noteer de hostnaam voor later gebruik en klik op **Apply**.
        5. Klik links op **System** > **Security**.
        6. Schakel onder **Remote Access Control** de optie **HTTPS Remote Access** in.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Klik op **Apply**.

    3. Controleren of je het beheerpaneel van de GL.iNet-router kunt openen

        1. Verbind een ander apparaat (bijvoorbeeld een laptop of mobiel apparaat) met een ander Wi-Fi-netwerk of met het mobiele netwerk.
        2. Voer in de adresbalk de eerder opgeslagen hostnaam in, bijvoorbeeld abcd123.glddns.com.
        3. Klik op **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Klik op **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Als het aanmeldscherm van de secundaire GL.iNet-router verschijnt, werkt port forwarding op de primaire router goed.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Als het aanmeldscherm niet verschijnt, werkt port forwarding niet goed. Configureer het opnieuw of gebruik een primaire router die port forwarding ondersteunt.

## Situatie 2. De WireGuard-server toont een verbonden client, maar de VPN-client heeft geen internet {#situation-2-the-wireguard-server-shows-connected-client-but-the-vpn-client-cannot-access-the-internet}

??? "Volg deze stappen"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Mogelijke oorzaak 1: je internetprovider kan de DNS-servers van GL.iNet mogelijk niet omzetten**

    Probeer de DNS-serveradressen handmatig in te stellen met de volgende stappen:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **Network** > **DNS**.
    3. Selecteer bij **Mode** de optie **Manual DNS**.
    4. Selecteer bij **DNS Server 1** de optie **Google Public DNS**.
    5. Klik op **Apply**.

    **Mogelijke oorzaak 2: het gateway-IP van je primaire router conflicteert met het IP-adres van de WireGuard-server**

    Probeer het IPv4-adres te wijzigen met de volgende stappen:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **VPN** > **WireGuard Server**.
    3. Voer op het tabblad **Configuration** bij **IPv4 Address** een nieuw IP-adres in, bijvoorbeeld 10.1.0.1/24.
    4. Klik op **Apply**.

    **Mogelijke oorzaak 3: als zowel de WireGuard-server als de WireGuard-client op GL.iNet-routers zijn ingesteld, conflicteren hun LAN-IP-adressen**

    Probeer het LAN-IP-adres van een van beide routers te wijzigen met de volgende stappen:

    1. Meld je in een webbrowser aan bij het beheerpaneel van een van beide GL.iNet-routers (bijvoorbeeld 192.168.8.1).
    2. Klik links op **Network** > **LAN**.
    3. Voer in het veld **Router IP address** een nieuw LAN-IP-adres in (bijvoorbeeld 192.168.10.1).
    4. Klik op **Apply**.

    **Mogelijke oorzaak 4: het IP-adres van de WireGuard-server is gewijzigd, maar het subnet ontbreekt**

    Voeg met de volgende stappen een subnet toe aan het IP-adres van de WireGuard-server:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **VPN** > **WireGuard Server**.
    3. Voeg op het tabblad **Configuration** bij **IPv4 Address** **/24** toe na **10.0.0.1**.
    4. Klik op **Apply**.

## Situatie 3. De WireGuard-server draait, maar de VPN-client kan geen verbinding maken {#situation-3-the-wireguard-server-is-running-but-vpn-client-cannot-connect-to-it}

??? "Volg deze stappen"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Mogelijke oorzaak 1: port forwarding op je primaire router werkt mogelijk niet goed**

    Controleer port forwarding door de HTTPS-poort naar de WireGuard-server door te sturen volgens de stappen in situatie 1.

    **Mogelijke oorzaak 2: je hebt mogelijk geen openbaar IP-adres**

    Volg [deze pagina](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om dit te controleren.

    **Mogelijke oorzaak 3: als zowel de WireGuard-server als de WireGuard-client op GL.iNet-routers zijn ingesteld, conflicteren hun LAN-IP-adressen**

    Wijzig het LAN-IP-adres van een van beide routers met de volgende stappen:

    1. Meld je in een webbrowser aan bij het beheerpaneel van een van beide GL.iNet-routers (bijvoorbeeld 192.168.8.1).
    2. Klik links op **Network** > **LAN**.
    3. Voer in het veld **Router IP address** een nieuw LAN-IP-adres in (bijvoorbeeld 192.168.10.1).
    4. Klik op **Apply**.

    **Mogelijke oorzaak 4: het apparaat waarmee je verbinding maakt met de WireGuard-server, is verbonden met het Wi-Fi-netwerk of een LAN-poort van die server**

    Verbind je apparaat met een ander Wi-Fi-netwerk of met het mobiele netwerk.

    **Mogelijke oorzaak 5: er ontbreken mogelijk regels in het configuratiebestand dat je naar je clientapparaat hebt geüpload**

    Upload je configuratiegegevens opnieuw.

## Situatie 4. De WireGuard-server is verbonden, maar de verbinding is instabiel {#situation-4-the-wireguard-server-is-connected-but-the-connection-is-not-stable}

??? "Volg deze stappen"

    Volg de onderstaande stappen en controleer na elke stap of het probleem is opgelost. Sla daarna de overige stappen over.

    1. Verlaag op de VPN-client de MTU van **1420** naar bijvoorbeeld 1380.
    2. Schakel VPN passthrough op de primaire router in als dit beschikbaar is.
    3.  Probeer de DNS-servers op je GL.iNet-router handmatig in te stellen met de volgende stappen:
        1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
        2. Klik links op **Network** > **DNS**.
        3. Selecteer bij Mode de optie **Manual DNS**.
        4. Selecteer bij **DNS Server 1** de optie **Google Public DNS**.
        5. Klik op **Apply**.

## Situatie 5. De WireGuard-server werkt plotseling niet meer {#situation-5-the-wireguard-server-suddenly-stopped-working}

??? "Volg deze stappen"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Mogelijke oorzaak 1: er is mogelijk een stroomstoring op de locatie van je WireGuard-server**

    Controleer via de stappen in situatie 1 of via [GoodCloud](../interface_guide/cloud.md), als de router daaraan is gekoppeld, of de WireGuard-server nog online is.

    **Mogelijke oorzaak 2: je hebt Dynamic DNS (DDNS) niet ingeschakeld**

    Bij een dynamisch IP-adres, wat meestal het geval is, moet je DDNS inschakelen. [Schakel DDNS in](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) en volg de overige stappen om de WireGuard-server opnieuw in te stellen.

    **Mogelijke oorzaak 3: port forwarding werkt om onbekende redenen niet meer**

    [Stel port forwarding opnieuw in](../tutorials/how_to_set_up_port_forwarding.md) met een andere poort.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
