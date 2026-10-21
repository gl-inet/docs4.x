# Wat moet ik doen als de WireGuard-server niet goed werkt? {#what-should-i-do-if-the-wireguard-server-is-not-working-properly}

Er zijn verschillende mogelijke oorzaken als de WireGuard-server op je GL.iNet-router niet goed werkt.

Volg de stappen die bij jouw probleem horen.

## Situatie 1. De WireGuard-server start, maar er kan geen verbinding worden gemaakt {#situation-1-the-wireguard-server-is-starting-but-cant-be-connected}

??? "Follow these steps"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Port forwarding op de primaire router naar de secundaire GL.iNet-router werkt mogelijk niet goed.
    Stuur de HTTPS-poort van de primaire router door naar de WireGuard-server om port forwarding te controleren:

    1. Forward your primary router's HTTPS port to your WireGuard server

        1. Sign in to your primary router's admin panel.
        2. Go to the port forwarding screen.
        3. Create a new port and name it **HTTPS**.
        4. Enter the following information:
            * **External port/Internal port:** Enter **443**.
            * **Protocol:** Choose **All** or **UDP/TCP**.
            * **Internal IP** (of **Host IP**): voer het WAN-IP-adres van de secundaire router in of selecteer deze in de keuzelijst.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. DDNS en externe HTTPS-toegang inschakelen op de GL.iNet-router

        1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
        2. Klik links op **Applications** > **Dynamic DNS**.
        3. Schakel **Enable DDNS** in en selecteer **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Noteer de hostnaam voor later gebruik en klik op **Apply**.
        5. Klik links op **System** > **Security**.
        6. Under **Remote Access Control**, toggle **HTTPS Remote Access** to on.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Click **Apply**.

    3. Controleren of je het beheerpaneel van de GL.iNet-router kunt openen

        1. On another device (e.g., laptop or mobile device), connect to a different Wi-Fi network or the cellular network.
        2. Voer in de adresbalk de eerder opgeslagen hostnaam in, bijvoorbeeld abcd123.glddns.com.
        3. Click **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Click **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Als het aanmeldscherm van de secundaire GL.iNet-router verschijnt, werkt port forwarding op de primaire router goed.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Als het aanmeldscherm niet verschijnt, werkt port forwarding niet goed. Configureer het opnieuw of gebruik een primaire router die port forwarding ondersteunt.

## Situatie 2. De WireGuard-server toont een verbonden client, maar de VPN-client heeft geen internet {#situation-2-the-wireguard-server-shows-connected-client-but-the-vpn-client-cannot-access-the-internet}

??? "Follow these steps"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Possible cause 1: You internet service provider may not be able to resolve GL.iNet's DNS servers**

    Try to manually configure the DNS server addresses by following these steps:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **Network** > **DNS**.
    3. For **Mode**, select **Manual DNS**.
    4. For **DNS Server 1**, select **Google Public DNS**.
    5. Click **Apply**.

    **Possible cause 2: Your primary router's gateway IP is in conflict with the WireGuard server's IP address**

    Try to change the IPv4 address by following these steps:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **VPN** > **WireGuard Server**.
    3. Voer op het tabblad **Configuration** bij **IPv4 Address** een nieuw IP-adres in, bijvoorbeeld 10.1.0.1/24.
    4. Click **Apply**.

    **Possible cause 3: If both your WireGuard server and WireGuard client were set up on GL.iNet routers, their LAN IP addersses are in conflict**

    Try to change the LAN IP address on either router by following these steps:

    1. In a web browser, sign in to the admin panel of either GL.iNet router (e.g., 192.168.8.1).
    2. Klik links op **Network** > **LAN**.
    3. In the **Router IP address** field, enter a new LAN IP address (e.g., 192.168.10.1).
    4. Click **Apply**.

    **Possible cause 4: The WireGuard server's IP address was updated but the subnet is missing**

    Add a subnet to your WireGuard server IP address by following these steps:

    1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
    2. Klik links op **VPN** > **WireGuard Server**.
    3. Voeg op het tabblad **Configuration** bij **IPv4 Address** **/24** toe na **10.0.0.1**.
    4. Click **Apply**.

## Situatie 3. De WireGuard-server draait, maar de VPN-client kan geen verbinding maken {#situation-3-the-wireguard-server-is-running-but-vpn-client-cannot-connect-to-it}

??? "Follow these steps"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Possible cause 1: The port forwarding you have set up on your primary router may not be working properly**

    Controleer port forwarding door de HTTPS-poort naar de WireGuard-server door te sturen volgens de stappen in situatie 1.

    **Possible cause 2: You may not have a public IP address**

    Volg [deze pagina](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) om dit te controleren.

    **Possible cause 3: If both your WireGuard server and WireGuard client were set up on GL.iNet routers, their LAN IP addersses are in conflict**

    Change the LAN IP address on either router by following these steps:

    1. In a web browser, sign in to the admin panel of either GL.iNet router (e.g., 192.168.8.1).
    2. Klik links op **Network** > **LAN**.
    3. In the **Router IP address** field, enter a new LAN IP address (e.g., 192.168.10.1).
    4. Click **Apply**.

    **Possible cause 4: The device you are using to connect to the WireGuard server is connected to its Wi-Fi network or its LAN port**

    Connect your device to a different Wi-Fi network or its cellular network.

    **Possible cause 5: Some lines may be missing in the configuration file you uploaded to your client device**

    Upload your configuration information again.

## Situatie 4. De WireGuard-server is verbonden, maar de verbinding is instabiel {#situation-4-the-wireguard-server-is-connected-but-the-connection-is-not-stable}

??? "Follow these steps"

    Volg de onderstaande stappen en controleer na elke stap of het probleem is opgelost. Sla daarna de overige stappen over.

    1. Verlaag op de VPN-client de MTU van **1420** naar bijvoorbeeld 1380.
    2. Schakel VPN passthrough op de primaire router in als dit beschikbaar is.
    3.  Try to manually configure DNS servers on your GL.iNet router by following these steps:
        1. Open in een webbrowser het beheerpaneel van de GL.iNet-router, bijvoorbeeld via 192.168.8.1, en meld je aan.
        2. Klik links op **Network** > **DNS**.
        3. For Mode, select **Manual DNS**.
        4. For **DNS Server 1**, select **Google Public DNS**.
        5. Click **Apply**.

## Situatie 5. De WireGuard-server werkt plotseling niet meer {#situation-5-the-wireguard-server-suddenly-stopped-working}

??? "Follow these steps"

    Volg de stappen voor elke mogelijke oorzaak en controleer of het probleem is opgelost. Sla de rest over zodra het werkt.

    **Possible cause 1: There may be a power outage in where you set up your WireGuard server**

    Controleer via de stappen in situatie 1 of via [GoodCloud](../interface_guide/cloud.md), als de router daaraan is gekoppeld, of de WireGuard-server nog online is.

    **Possible cause 2: You did not enable the Dynamic DNS (DDNS)**

    Bij een dynamisch IP-adres, wat meestal het geval is, moet je DDNS inschakelen. [Schakel DDNS in](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) en volg de overige stappen om de WireGuard-server opnieuw in te stellen.

    **Possible cause 3: The port forwarding stopped working for unknown reasons**

    [Set up port forwarding](../tutorials/how_to_set_up_port_forwarding.md) again with another port.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
