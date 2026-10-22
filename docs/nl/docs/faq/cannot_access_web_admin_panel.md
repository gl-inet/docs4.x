# Cannot access web Admin Panel {#cannot-access-web-admin-panel}

Soms kun je [http://192.168.8.1](http://192.168.8.1) niet openen en je daardoor niet aanmelden bij het webbeheerpaneel. Dit kan verschillende oorzaken hebben.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Mogelijke oorzaken {#the-possible-causes}

* Je computer of telefoon is niet met de router verbonden.
* `192.168.8.1` is het standaard-IP-adres van de router. Mogelijk heb je dit gewijzigd.
* The cache or extension of browser may cause the admin panel inaccessible.
* VPN- of proxysoftware verwerkt je verkeer en kan het beheerpaneel onbereikbaar maken.
* The router is bricked.

## Algemene stappen voor toegang tot het webbeheerpaneel controleren {#check-the-general-steps-to-access-web-admin-panel}

1. Power up the router without connecting to any device.
2. Verbind je telefoon of laptop met de wifi van de router en voer de wifisleutel op het etiket in.
3. Als stap 2 mislukt, schakel je wifi op de computer uit en sluit je deze met een Ethernetkabel aan op de LAN-poort.
4. Open een browser, voer `192.168.8.1` in de adresbalk in en druk op Enter. Het GL.iNet-webbeheerpaneel hoort te worden geopend.

Je kunt de router ook via [de app](mobile_app.md) openen.

## Andere oplossingen {#other-steps-to-fix-this-issue}

1. [Check the connection](#check-the-connection)
2. [Check router's IP address](#check-routers-ip-address)
3. [Access the router's IP address](#access-the-routers-ip-address)

---

### Verbinding controleren {#check-the-connection}

Controleer bij een Ethernetverbinding of de WAN/LAN-poorten correct zijn aangesloten:

- The WAN port is connected to an Internet source, such as a modem or a primary router.
- De LAN-poort is verbonden met het eindapparaat, zoals je laptop.

Controleer bij een wifiverbinding of je de juiste SSID en het juiste wachtwoord hebt gebruikt.

### Check router's IP address {#check-routers-ip-address}

Follow the steps below to check the router's IP address.

=== "Windows 10 / Windows 11"

    Open Control Panel en stel View by rechtsboven in op Large icons of Small icons.

    ![control panel](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/control_panel_view_by.png){class="glboxshadow"}

    Ga naar Control Panel -> Network and Sharing Center en klik op de verbinding. Selecteer bij meerdere verbindingen de verbinding van de router die je wilt controleren.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Er verschijnt een venster met de verbindingsstatus. Klik op de knop voor details.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    It will pop up a dialog of network connection detail, the IP address of router is the **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings

    Klik met de rechtermuisknop op het netwerk -> Status -> Details.

    The IP address of router is the **IPv4 Default Gateway**

    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. System Preferences -> Network

    2. Klik links op de netwerkverbinding. Bij een Ethernetverbinding wordt het IP-adres van de router weergegeven.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Klik bij een wifiverbinding op "Advanced..." en daarna bovenaan op het tabblad "TCP/IP". Het IP-adres van de router wordt weergegeven.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Settings -> Wi-Fi
    2. Tik bij het verbonden wifinetwerk op het informatiepictogram, een blauwe i in een cirkel. Het IP-adres van de router wordt weergegeven.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    De stappen verschillen per Android-apparaat.

    1. Settings -> Network & internet
    2. Tik op Wi-Fi, zoek het verbonden netwerk en klik op het instellingenpictogram.
    3. Open Advanced. Als je tussen Static en Dynamic IP kunt kiezen, selecteer je Static.
    4. Het IP-adres van de router staat onder Gateway.

### IP-adres van de router openen {#access-the-routers-ip-address}

1. Gebruik voor de beste compatibiliteit Chrome, Edge of Safari om het beheerpaneel te openen.

2. Open een incognitovenster om problemen door browsercache en extensies te vermijden en probeer het IP-adres opnieuw.

3. Disable any VPN or proxy software, including Tailscale and ZeroTier.

4. Schakel mobiele data uit als je een telefoon gebruikt.

    Sommige smartphones verbreken de wifi wanneer de router geen internet heeft en gebruiken mobiele data. Na verbreking kun je het webbeheerpaneel niet openen.

5. If above steps failed, try [Reset](repair_network_or_reset_firmware.md#reset-to-factory) the router to factory default.

6. Als de reset niet werkt, probeer je [herstel via U-Boot](debrick.md).

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
