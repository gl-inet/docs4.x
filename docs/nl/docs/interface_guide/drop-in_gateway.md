# Drop-in Gateway {#drop-in-gateway}

Ga links in het webbeheerpaneel naar **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway breidt de mogelijkheden van een bestaande primaire router uit zonder deze te vervangen of opnieuw te configureren. Door de GL.iNet-router via een Ethernet-kabel met de primaire router te verbinden, kun je geavanceerde netwerkfuncties aan de bestaande infrastructuur toevoegen, zoals:

- Advertenties filteren via AdGuard Home
- VPN-client inschakelen
- Versleutelde DNS gebruiken

We raden een krachtige router of beveiligingsgateway met voldoende geheugen aan, zoals GL-MT2500 of GL-MT5000. Installeer zo nodig aanvullende hulpmiddelen voor het doorsturen en beheren van verkeer.

## Netwerktopologie {#network-topology}

Drop-in Gateway werkt als een tussengelegen netwerksysteem. Gegevensverkeer van clientapparaten wordt eerst via de GL.iNet-router verwerkt en daarna via de primaire router verzonden. Bestaande netwerkinstellingen, zoals SSID en wachtwoord, blijven behouden zodat alle apparaten verbonden blijven. Je kunt daarnaast naar behoefte het netwerkverkeer voor alle of specifieke clientapparaten beheren.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Het bovenstaande diagram bevat twee soorten lijnen: grijze lijnen en groene lijnen met drie genummerde pijlen.

1. **Grijze lijnen** tonen de fysieke verbindingstopologie: clientapparaten, zoals computers en laptops, zijn met de primaire router verbonden. De LAN-poort van de primaire router is via een Ethernet-kabel verbonden met de WAN-poort van de GL.iNet-router waarop Drop-in Gateway is ingeschakeld.

2. **Groene lijnen** tonen het opeenvolgende pad van de gegevensoverdracht wanneer Drop-in Gateway actief is. De genummerde pijlen geven de volgorde van de verkeersstroom aan:

    1. Verkeer van clientapparaten wordt eerst naar de primaire router geleid.

    2. De primaire router stuurt het verkeer voor verwerking naar de GL.iNet-router, bijvoorbeeld voor advertentiefiltering of VPN-versleuteling.

    3. Na verwerking wordt het verkeer teruggestuurd naar de primaire router. Deze levert de uiteindelijke gegevens aan de oorspronkelijke clientapparaten of routeert ze naar internet.

## Instellen {#setup}

Er zijn twee implementatiemodi: alle clientapparaten gebruiken Drop-in Gateway of alleen bepaalde clientapparaten gebruiken Drop-in Gateway.

In het volgende voorbeeld is het gatewayadres van de primaire router `192.168.1.1`.

### Alle apparaten gebruiken Drop-in Gateway {#all-devices-managed-by-the-drop-in-gateway}

1. Sluit de LAN-poort van de primaire router met een Ethernet-kabel aan op de WAN-poort van de GL.iNet-router.

2. Meld je aan bij het webbeheerpaneel van de GL.iNet-router en schakel Drop-in Gateway in. Het systeem genereert automatisch de bijbehorende configuratieparameters.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** is het WAN-IP-adres van je GL.iNet-router dat dynamisch door de primaire router wordt toegewezen. Je kunt dit WAN-IP-adres bekijken in het gedeelte Ethernet op de pagina [INTERNET](internet_ethernet.md).

    - De velden **Gateway** en **DNS Server 1** worden standaard automatisch ingevuld met het IP-adres van de primaire router. Als deze parameters onjuist zijn, kun je ze handmatig aanpassen.

    Noteer dit IP-adres, omdat je het in de volgende stappen nodig hebt.

    Selecteer de eerste configuratiemethode en klik op **Apply**.

3. Meld je aan bij het webbeheerpaneel van de primaire router.

    ??? "GL.iNet"

        Volg de onderstaande stappen als je primaire router een GL.iNet-router met firmware v4.2 of hoger is.

        Meld je aan bij het Web Admin Panel -> NETWORK -> LAN -> DHCP Server -> Advanced.

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Vul bij DHCP Gateway het IP Address uit stap 2 in, bijvoorbeeld `192.168.1.23`, en klik op **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Volg de onderstaande stappen als je primaire router van TP-Link is. TP-LINK Archer C3150 wordt als voorbeeld gebruikt.

        Meld je aan bij de beheerpagina van TP-Link, ga naar **Advanced** -> **Network** -> **DHCP Server** en schakel **DHCP** uit.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Klik vervolgens op **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Volg de onderstaande stappen als je primaire router van Linksys is. Linksys WHW01 wordt als voorbeeld gebruikt.

        Meld je aan bij de beheerpagina van Linksys en ga naar **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Open het tabblad **Local Network**, schakel **DHCP Server** uit en klik op **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Er verschijnt een waarschuwing. Klik op **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Overige"

        Meld je aan bij het beheerpaneel van de primaire router om de DHCP-server uit te schakelen. Raadpleeg de gebruikershandleiding of ondersteuning van de fabrikant.

4. Ga terug naar de GL.iNet-router en stel functies in zoals [AdGuard Home](adguardhome.md), [versleutelde DNS](dns.md), [WireGuard Client](wireguard_client.md) en [OpenVPN Client](openvpn_client.md).

### Alleen bepaalde apparaten gebruiken Drop-in Gateway {#some-devices-managed-by-the-drop-in-gateway}

1. Sluit de LAN-poort van de primaire router met een Ethernet-kabel aan op de WAN-poort van de GL.iNet-router.

2. Meld je aan bij het webbeheerpaneel van de GL.iNet-router en schakel Drop-in Gateway in. Het systeem genereert automatisch de bijbehorende configuratieparameters.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** is het WAN-IP-adres van je GL.iNet-router dat dynamisch door de primaire router wordt toegewezen. Je kunt dit WAN-IP-adres bekijken in het gedeelte Ethernet op de pagina [INTERNET](internet_ethernet.md).

    - De velden **Gateway** en **DNS Server 1** worden standaard automatisch ingevuld met het IP-adres van de primaire router. Als deze parameters onjuist zijn, kun je ze handmatig aanpassen.

    Noteer dit IP-adres, omdat je het in de volgende stappen nodig hebt.

    Selecteer de tweede configuratiemethode en klik op **Apply**.

3. Stel op het apparaat dat Drop-in Gateway moet gebruiken de gateway en DNS in op het IP-adres dat op de pagina Drop-in Gateway wordt weergegeven.

    ??? "Windows"

        Windows 11 wordt als voorbeeld gebruikt; Windows 10 werkt vergelijkbaar. Controleer of je pc met de primaire router is verbonden. In dit voorbeeld is de computer via een netwerkkabel verbonden; de configuratie via Wi-Fi is vergelijkbaar.

        1. Open Settings.

        2. Klik op **Network & Internet**.

        3. Klik op het tabblad **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Zoek het IP-adres van deze pc. Klik in het gedeelte "IP assignment" op **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Selecteer **Manual** en schakel **IPv4 toggle** in.

        6. Stel **IP address** in op het IP-adres uit stap 4, **Subnet mask** op `255.255.255.0` en zowel **Gateway** als **Preferred DNS** op het IP-adres van de pagina Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Klik op **Save**.

    ??? "Android"

        Samsung S21 wordt als voorbeeld gebruikt. Controleer of je smartphone met de primaire router is verbonden.

        1. Open Settings en klik op Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Klik op Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Klik op het tandwielpictogram van de huidige SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Klik op **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Klik op **IP settings** en kies **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Stel **Gateway** en **DNS 1** in op het IP-adres van de pagina Drop-in Gateway en klik op **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        iOS 16.3 op iPhone 8 wordt als voorbeeld gebruikt. Controleer of je smartphone met de primaire router is verbonden.

        1. Open Settings en klik op Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Klik op de SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Scrol omlaag. **Configure IP** staat op **Automatic**. Noteer **IP Address** en **Subnet Mask** voor de volgende stap.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Wijzig **Configure IP** in **Manual**, stel **IP Address** en **Subnet Mask** in op de waarden uit de vorige stap en stel **Router** in op het IP-adres van de pagina Drop-in Gateway. Klik vervolgens op **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Klik op **Configure DNS** en wijzig dit in **Manual**. Klik op **Add Server**, stel het IP-adres van de DNS-server in op het adres van de pagina Drop-in Gateway en klik op **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Ga terug naar het webbeheerpaneel van de GL.iNet-router en stel naar behoefte functies in, zoals [AdGuard Home](adguardhome.md), [versleutelde DNS](dns.md), [WireGuard Client](wireguard_client.md) en [OpenVPN Client](openvpn_client.md).

## Aandachtspunten {#cautions}

1. Het inschakelen van Drop-in Gateway verhoogt de netwerklatentie.

2. Wanneer Drop-in Gateway is ingeschakeld, wordt gegevensoverdracht tussen geselecteerde LAN-apparaten ook via de drop-in gateway gerouteerd. De bandbreedte tussen de primaire router en drop-in gateway beïnvloedt daardoor de totale LAN-bandbreedte.

---

Gerelateerd artikel:

- [Drop-in Gateway instellen op een GL.iNet-router](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
