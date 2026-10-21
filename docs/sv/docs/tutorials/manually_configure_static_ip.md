# Så konfigurerar du en statisk IP-adress manuellt på klientenheter {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    I Windows 11 kan du ange en statisk IP-adress för både trådlösa och trådbundna nätverkskort.

    **Ange en statisk IP-adress för Wi-Fi-kortet**

    1. Gå till **Settings** -> **Network & internet** -> **Wi-Fi** på en Windows 11-dator och välj den aktuella Wi-Fi-anslutningen.

    2. Leta reda på **IP assignment** och klicka på **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Välj **Manual** i popup-fönstret och aktivera **IPv4**.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Redigera IP-inställningarna enligt anvisningarna nedan.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Ange en statisk IP-adress, till exempel `10.1.4.119`.

        - Subnet mask: Ange en nätmask, till exempel `255.255.255.0`.

        - Gateway: Ange gatewayadressen, vanligtvis routerns LAN-IP-adress i samma subnät. Om IP-adressen exempelvis är `10.1.4.119` är gatewayen vanligtvis `10.1.4.1`.

        - Preferred DNS: Ange en primär DNS-adress (obligatoriskt). Du kan till exempel ange en offentlig DNS-server, som Googles DNS-server `8.8.8.8`.

        - Alternate DNS: Ange en alternativ DNS-adress (valfritt).

        - DNS over HTTPS: Välj "Off". Det finns tre alternativ:

            - Off: Överför all DNS-trafik utan kryptering.

            - On (automatic template): Skickar all DNS-trafik krypterad.

            - On (manual template): Låter dig ange en viss mall. Detta krävs endast om DNS-tjänsten inte fungerar automatiskt eller om tjänsten har en mall som fungerar på avsett sätt.

        - Inaktivera reglaget "Fallback to plaintext" om du aktiverar DNS over HTTPS.

            **Tips**: Om du aktiverar den här funktionen krypterar systemet DNS-trafiken, men tillåter att frågor skickas utan kryptering.

    5. Klicka på **Save** för att tillämpa inställningarna.

        När stegen ovan är klara tillämpas den statiska nätverkskonfigurationen på datorn. Testa de nya inställningarna genom att öppna en webbläsare och läsa in en webbplats.

    ---

    **Ange en statisk IP-adress för Ethernet-kortet**

    1. Gå till **Settings** -> **Network & internet** -> **Ethernet** på en Windows 11-dator.

    2. Leta reda på **IP assignment** och klicka på **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Välj **Manual** i popup-fönstret och aktivera **IPv4**.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Redigera IP-inställningarna enligt anvisningarna nedan.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Ange en statisk IP-adress, till exempel `10.1.4.119`.

        - Subnet mask: Ange en nätmask, till exempel `255.255.255.0`.

        - Gateway: Ange gatewayadressen, vanligtvis routerns LAN-IP-adress i samma subnät. Om IP-adressen exempelvis är `10.1.4.119` är gatewayen vanligtvis `10.1.4.1`.

        - Preferred DNS: Ange en primär DNS-adress (obligatoriskt). Du kan till exempel ange en offentlig DNS-server, som Googles DNS-server `8.8.8.8`.

        - Alternate DNS: Ange en alternativ DNS-adress (valfritt).

        - DNS over HTTPS: Välj "Off". Det finns tre alternativ:

            - Off: Överför all DNS-trafik utan kryptering.

            - On (automatic template): Skickar all DNS-trafik krypterad.

            - On (manual template): Låter dig ange en viss mall. Detta krävs endast om DNS-tjänsten inte fungerar automatiskt eller om tjänsten har en mall som fungerar på avsett sätt.

        - Inaktivera reglaget "Fallback to plaintext" om du aktiverar DNS over HTTPS.

            **Tips**: Om du aktiverar den här funktionen krypterar systemet DNS-trafiken, men tillåter att frågor skickas utan kryptering.

    5. Klicka på **Save** för att tillämpa inställningarna.

        När stegen ovan är klara tillämpas den statiska nätverkskonfigurationen på datorn. Testa de nya inställningarna genom att öppna en webbläsare och läsa in en webbplats.

=== "macOS"

    Så här anger du en statisk IP-adress i macOS.

    Välj **System Preferences** i Apple-menyn.

    Välj **Network**. På sidan som visas väljer du ett aktivt nätverksgränssnitt i sidofältet, till exempel **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Anteckna den aktuella IP-adressen som din Mac har tilldelats. Du behöver välja en ny IP-adress inom det privata IP-adressintervallet som anges.

    Klicka på **Advanced** längst ned till höger.

    Välj sedan **TCP/IP**. Följande sida visas.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: Välj "Manually".

    - IPv4 Address: Ange en statisk IP-adress. Behåll de tre första oktetterna i den aktuella IP-adressen och ändra den sista oktetten till ett ledigt värde. I nätverket `192.168.7.0/24` väljer du till exempel en adress mellan `192.168.7.2` och `192.168.7.254` som inte redan används (undvik `.1`, som är routern). Använd inte `192.168.7.0` eller `192.168.7.255`.

    - Subnet Mask: Ange `255.255.255.0` (eller nätmasken som nätverksadministratören har angett).

    - Router: Ange routerns LAN-IP-adress, till exempel `192.168.7.1`.

    Klicka på **OK** och sedan på **Apply**.

=== "iOS"

    Stegen kan variera beroende på iOS-version. Följande steg baseras på iOS version 26.2.2.

    1. Gå till **Settings** -> **WLAN**. Tryck på den blå informationsikonen (i) bredvid det anslutna Wi-Fi-nätverket.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Bläddra ned till **IPv4 Address** och välj **Manual** för **Configure IP**.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Ange **IP Address**, **Subnet Mask** och **Router IP** som du vill använda på din iPhone/iPad och tryck sedan på **Save** längst upp till höger.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Stegen kan variera beroende på Android-version. Följande steg baseras på Android version 11.

    1. Gå till **Settings** -> **Network & Internet** -> **Wi-Fi**. Tryck på det anslutna nätverket för att öppna inställningsmenyn.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Tryck på pennikonen längst upp till höger för att öppna nätverksinställningarna.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Tryck på **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Tryck på **IP Settings** och välj **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Ange **IP address**. Fältet **Gateway** ska fyllas i automatiskt utifrån IP-adressen. Ange annars nätverkets gateway. Gatewayen är vanligtvis routerns LAN-IP-adress i samma subnät.

        **Tips**: När du använder statiska IP-adresser i hemnätverk och andra privata nätverk väljer du en ledig värdadress i det aktuella subnätet. Standardintervallen för privata IP-adresser är följande:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Tryck på **Save** och vänta tills nätverket ansluter igen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
