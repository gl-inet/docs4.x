# Drop-in Gateway {#drop-in-gateway}

Öppna **NETWORK** -> **Drop-in Gateway** på vänster sida i webbadministrationspanelen.

Drop-in Gateway utökar funktionerna hos en befintlig primär router utan att den behöver bytas ut eller konfigureras om. Genom att ansluta GL.iNet-routern till den primära routern med en Ethernet-kabel kan du lägga till avancerade nätverksfunktioner, till exempel:

- Filter advertisements via AdGuard Home
- Enable VPN client
- Use encrypted DNS

Vi rekommenderar en högpresterande router eller säkerhetsgateway med gott om minne, till exempel GL-MT2500 eller GL-MT5000, samt nödvändiga verktyg för trafikvidarebefordran och styrning.

## Network Topology {#network-topology}

Drop-in Gateway fungerar som ett mellanliggande nätverkssystem. Datatrafik från klientenheter dirigeras genom GL.iNet-routern för bearbetning innan den överförs via den primära routern. Befintliga nätverksinställningar, till exempel SSID och lösenord, bevaras för oavbruten anslutning, och du kan hantera trafiken för alla eller vissa klientenheter.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Diagrammet ovan innehåller grå linjer och gröna linjer med tre numrerade pilar.

1. **Grå linjer** visar den fysiska topologin: klientenheter ansluter till den primära routern, vars LAN-port ansluts till WAN-porten på GL.iNet-routern med Drop-in Gateway aktiverat via en Ethernet-kabel.

2. **Gröna linjer** visar dataöverföringsvägen när Drop-in Gateway är aktivt. De numrerade pilarna anger ordningen:

    1. Trafik från klientenheter dirigeras först till den primära routern.

    2. The primary router forwards the traffic to the GL.iNet router for processing (e.g., ad filtering, VPN encryption);

    3. Efter bearbetning skickas trafiken tillbaka till den primära routern, som levererar data till klientenheterna eller dirigerar dem till internet.

## Setup {#setup}

There are two deployment modes for different application scenarios: All client devices are networked through Drop-in Gateway, or only specific client devices are networked through Drop-in Gateway.

I följande exempel är gatewayadressen för den primära routern `192.168.1.1`.

### Alla enheter använder Drop-in Gateway {#all-devices-managed-by-the-drop-in-gateway}

1. Anslut LAN-porten på den primära routern till WAN-porten på GL.iNet-routern med en Ethernet-kabel.

2. Logga in på GL.iNet-routerns webbadministrationspanel och aktivera Drop-in Gateway. Systemet skapar automatiskt konfigurationsparametrarna.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** är GL.iNet-routerns WAN-IP-adress, som tilldelas dynamiskt av den primära routern. Den visas i avsnittet Ethernet på sidan [INTERNET](internet_ethernet.md).

    - Fälten **Gateway** och **DNS Server 1** fylls som standard automatiskt med den primära routerns IP-adress. Justera dem manuellt vid behov.

    Anteckna IP-adressen eftersom den används i följande steg.

    Välj den första konfigurationsmetoden och klicka på **Apply**.

3. Logga in på den primära routerns webbadministrationspanel.

    ??? "GL.iNet"

        Om den primära routern är en GL.iNet-router med firmware v4.2 eller senare följer du stegen nedan.

        Log in to the web Admin Panel -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Ange IP Address från steg 2, till exempel `192.168.1.23`, som DHCP Gateway och klicka på **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Om den primära routern är TP-Link följer du stegen nedan (TP-LINK Archer C3150 används som exempel).

        Log in to the TP-Link admin page, navigate to **Advanced** -> **Network** -> **DHCP Server**, then disable the **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Then click **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Om den primära routern är Linksys följer du stegen nedan (Linksys WHW01 används som exempel).

        Log in to the Linksys admin page, navigate to **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Klicka på fliken **Local Network**, inaktivera **DHCP Server** och klicka på **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        It will show a warning. Click **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Logga in på den primära routerns administratörspanel och inaktivera DHCP-servern. Se tillverkarens handbok eller kontakta supporten.

4. Gå tillbaka till GL.iNet-routern och konfigurera funktioner som [AdGuard Home](adguardhome.md), [krypterad DNS](dns.md), [WireGuard Client](wireguard_client.md) och [OpenVPN Client](openvpn_client.md).

### Vissa enheter använder Drop-in Gateway {#some-devices-managed-by-the-drop-in-gateway}

1. Anslut LAN-porten på den primära routern till WAN-porten på GL.iNet-routern med en Ethernet-kabel.

2. Logga in på GL.iNet-routerns webbadministrationspanel och aktivera Drop-in Gateway. Systemet skapar automatiskt konfigurationsparametrarna.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** är GL.iNet-routerns WAN-IP-adress, som tilldelas dynamiskt av den primära routern. Den visas i avsnittet Ethernet på sidan [INTERNET](internet_ethernet.md).

    - Fälten **Gateway** och **DNS Server 1** fylls som standard automatiskt med den primära routerns IP-adress. Justera dem manuellt vid behov.

    Anteckna IP-adressen eftersom den används i följande steg.

    Välj den andra konfigurationsmetoden och klicka på **Apply**.

3. Ange gateway och DNS på enheten som ska använda Drop-in Gateway till IP-adressen på sidan Drop-in Gateway.

    ??? "Windows"

        Windows 11 används som exempel; Windows 10 är liknande. Kontrollera att datorn är ansluten till den primära routern. Exemplet använder nätverkskabel, men konfigurationen är liknande via Wi-Fi.

        1. Open Settings.

        2. Click on **Network & Internet**.

        3. Click the **Ethernet** tab.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Leta reda på datorns IP-adress. Klicka på **Edit** under "IP assignment".

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option. Turn on the **IPv4 toggle** switch.

        6. Ange **IP address** till adressen från steg 4, **Subnet mask** till `255.255.255.0` och både **Gateway** och **Preferred DNS** till IP-adressen på sidan Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Click the **Save** button.

    ??? "Android"

        Samsung S21 används som exempel. Kontrollera att telefonen är ansluten till den primära routern.

        1. Open Settings, click on Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Click on Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Klicka på kugghjulsikonen för aktuellt SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Click **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Click **IP settings**, choose **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Ange **Gateway** och **DNS 1** till IP-adressen på sidan Drop-in Gateway och klicka på **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        iOS 16.3 på iPhone 8 används som exempel. Kontrollera att telefonen är ansluten till den primära routern.

        1. Open Settings, click Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Click the SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Bläddra ned och kontrollera att **Configure IP** är **Automatic**. Anteckna **IP Address** och **Subnet Mask**.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Ändra **Configure IP** till **Manual**, ange **IP Address** och **Subnet Mask** från föregående steg och ange **Router** till IP-adressen på sidan Drop-in Gateway. Klicka på **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Klicka på **Configure DNS** och ändra till **Manual**. Klicka på **Add Server**, ange DNS-serverns IP-adress till adressen på sidan Drop-in Gateway och klicka på **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Gå tillbaka till GL.iNet-routerns webbadministrationspanel och konfigurera funktioner som [AdGuard Home](adguardhome.md), [krypterad DNS](dns.md), [WireGuard Client](wireguard_client.md) och [OpenVPN Client](openvpn_client.md).

## Cautions {#cautions}

1. Enabling Drop-in Gateway increases network latency.

2. När Drop-in Gateway är aktiverat dirigeras även dataöverföring mellan valda LAN-enheter genom gatewayen. Bandbredden mellan den primära routern och Drop-in Gateway påverkar därför den totala LAN-bandbredden.

---

Related Article:

- [How to set up drop-in gateway on a GL.iNet router](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
