# Det går inte att öppna webbadministrationspanelen {#cannot-access-web-admin-panel}

Ibland går det inte att öppna [http://192.168.8.1](http://192.168.8.1), och du kan därför inte logga in på webbadministrationspanelen. Det kan finnas flera orsaker.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Möjliga orsaker {#the-possible-causes}

* Datorn eller mobiltelefonen är inte ansluten till routern.
* `192.168.8.1` är routerns standard-IP-adress. Du kan ha ändrat IP-adressen.
* Webbläsarens cache eller ett tillägg kan göra administrationspanelen otillgänglig.
* VPN- eller proxyprogram hanterar trafiken och kan göra administrationspanelen otillgänglig.
* Routern fungerar inte längre.

## Grundläggande steg för att öppna webbadministrationspanelen {#check-the-general-steps-to-access-web-admin-panel}

1. Slå på routern utan att ansluta den till någon enhet.
2. Anslut mobilen eller den bärbara datorn till routerns Wi-Fi och ange Wi-Fi-nyckeln som står på routeretiketten.
3. Om steg 2 misslyckas stänger du av Wi-Fi på datorn eller den bärbara datorn. Anslut den i stället till routerns LAN-port med en Ethernet-kabel.
4. Öppna en webbläsare, skriv `192.168.8.1` i adressfältet och tryck på Enter. GL.iNets webbadministrationspanel ska öppnas.

Du kan även använda [appen](mobile_app.md) för att öppna routern.

## Andra steg för att lösa problemet {#other-steps-to-fix-this-issue}

1. [Kontrollera anslutningen](#check-the-connection)
2. [Kontrollera routerns IP-adress](#check-routers-ip-address)
3. [Öppna routerns IP-adress](#access-the-routers-ip-address)

---

### Kontrollera anslutningen {#check-the-connection}

Om du är ansluten med en Ethernet-kabel kontrollerar du att anslutningarna till routerns WAN-/LAN-portar är korrekta:

- WAN-porten är ansluten till en internetkälla, till exempel ett modem eller en primär router.
- LAN-porten är ansluten till slutenheten, till exempel din bärbara dator.

Om du är ansluten via Wi-Fi kontrollerar du att du har valt rätt SSID på enheten och angett rätt lösenord.

### Kontrollera routerns IP-adress {#check-routers-ip-address}

Följ stegen nedan för att kontrollera routerns IP-adress.

=== "Windows 10/Windows 11"

    Öppna Control Panel och kontrollera att View by i det övre högra hörnet är inställt på Large icons eller Small icons.

    ![control panel](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/control_panel_view_by.png){class="glboxshadow"}

    Gå till Control Panel -> Network and Sharing Center -> klicka på anslutningen. Du kan ha flera anslutningar. Välj den anslutning som hör till routern du vill kontrollera.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    En dialogruta med anslutningens status öppnas. Klicka på knappen Details.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    En dialogruta med information om nätverksanslutningen öppnas. Routerns IP-adress är **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings

    Högerklicka på nätverket -> Status -> Details

    Routerns IP-adress är **IPv4 Default Gateway**.

    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. System Preferences -> Network

    2. Klicka på nätverksanslutningen i den vänstra kolumnen. För en Ethernet-anslutning visas routerns IP-adress.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    För en Wi-Fi-anslutning klickar du på knappen "Advanced..." och sedan på fliken "TCP/IP" högst upp i fönstret. Routerns IP-adress visas.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Settings -> Wi-Fi
    2. Tryck på informationsikonen (ett blått i i en cirkel) för det Wi-Fi-nätverk som är anslutet. Routerns IP-adress visas.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Stegen varierar mellan olika Android-enheter.

    1. Settings -> Network & internet
    2. Tryck på Wi-Fi, leta reda på nätverket du är ansluten till och tryck på inställningsikonen för att hantera inställningarna.
    3. Tryck på listrutan Advanced. Om du kan välja mellan en statisk och dynamisk IP-adress väljer du Static.
    4. Routerns IP-adress visas under Gateway.

### Öppna routerns IP-adress {#access-the-routers-ip-address}

1. Använd Chrome, Edge eller Safari för att öppna routerns administrationspanel med bättre kompatibilitet.

2. Öppna ett inkognitofönster för att undvika problem som orsakas av webbläsarens cache och tillägg. Försök sedan öppna routerns IP-adress igen.

3. Inaktivera alla VPN- och proxyprogram, inklusive Tailscale och ZeroTier.

4. Om du använder en mobiltelefon stänger du av mobildata.

    Vissa smarttelefoner kopplar från routerns Wi-Fi och använder mobildata i stället när de upptäcker att routern saknar internetanslutning. Om telefonen kopplas från routern går det dock inte att öppna webbadministrationspanelen.

5. Om stegen ovan misslyckas försöker du [återställa](repair_network_or_reset_firmware.md#reset-to-factory) routern till fabriksinställningarna.

6. Om återställningen inte fungerar försöker du [återställa routern via U-Boot](debrick.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
