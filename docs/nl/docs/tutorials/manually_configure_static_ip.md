# Handmatig een statisch IP-adres configureren op clientapparaten {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    In Windows 11 kun je een statisch IP-adres instellen voor draadloze en bekabelde adapters.

    **Een statisch IP-adres instellen op een Wi-Fi-adapter**

    1. Ga op een Windows 11-pc naar **Settings** -> **Network & internet** -> **Wi-Fi** en selecteer de huidige Wi-Fi-verbinding.

    2. Zoek **IP assignment** en klik op **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Selecteer in het pop-upvenster **Manual** en schakel **IPv4** in.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Volg de onderstaande stappen om de IP-instellingen te bewerken.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: stel een statisch IP-adres in, bijvoorbeeld `10.1.4.119`.

        - Subnet mask: geef een subnetmasker op, bijvoorbeeld `255.255.255.0`.

        - Gateway: voer het gatewayadres in, doorgaans het LAN-IP-adres van je router in hetzelfde subnet. Als je IP-adres bijvoorbeeld `10.1.4.119` is, is de gateway doorgaans `10.1.4.1`.

        - Preferred DNS: geef een Preferred DNS-adres op (verplicht). Je kunt een openbare DNS-server invoeren, zoals de DNS-server van Google: `8.8.8.8`.

        - Alternate DNS: geef een Alternate DNS-adres op (optioneel).

        - DNS over HTTPS: selecteer "Off". Er zijn drie opties:

            - Off: verzendt al het DNS-verkeer zonder versleuteling.

            - On (automatic template): verzendt al het DNS-verkeer versleuteld.

            - On (manual template): hiermee kun je een specifieke sjabloon opgeven. Dit is alleen vereist als de DNS-service niet automatisch werkt of een bepaalde sjabloon nodig heeft.

        - Schakel "Fallback to plaintext" uit als je DNS over HTTPS inschakelt.

            **Tip**: als je deze functie inschakelt, versleutelt het systeem DNS-verkeer, maar kunnen query's zonder versleuteling worden verzonden.

    5. Klik op **Save** om de instellingen toe te passen.

        Nadat je de bovenstaande stappen hebt voltooid, wordt de statische netwerkconfiguratie op de computer toegepast. Je kunt de nieuwe instellingen testen door een webbrowser te openen en een website te laden.

    ---

    **Een statisch IP-adres instellen op een ethernetadapter**

    1. Ga op een Windows 11-pc naar **Settings** -> **Network & internet** -> **Ethernet**.

    2. Zoek **IP assignment** en klik op **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Selecteer in het pop-upvenster **Manual** en schakel **IPv4** in.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Volg de onderstaande stappen om de IP-instellingen te bewerken.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: stel een statisch IP-adres in, bijvoorbeeld `10.1.4.119`.

        - Subnet mask: geef een subnetmasker op, bijvoorbeeld `255.255.255.0`.

        - Gateway: voer het gatewayadres in, doorgaans het LAN-IP-adres van je router in hetzelfde subnet. Als je IP-adres bijvoorbeeld `10.1.4.119` is, is de gateway doorgaans `10.1.4.1`.

        - Preferred DNS: geef een Preferred DNS-adres op (verplicht). Je kunt een openbare DNS-server invoeren, zoals de DNS-server van Google: `8.8.8.8`.

        - Alternate DNS: geef een Alternate DNS-adres op (optioneel).

        - DNS over HTTPS: selecteer "Off". Er zijn drie opties:

            - Off: verzendt al het DNS-verkeer zonder versleuteling.

            - On (automatic template): verzendt al het DNS-verkeer versleuteld.

            - On (manual template): hiermee kun je een specifieke sjabloon opgeven. Dit is alleen vereist als de DNS-service niet automatisch werkt of een bepaalde sjabloon nodig heeft.

        - Schakel "Fallback to plaintext" uit als je DNS over HTTPS inschakelt.

            **Tip**: als je deze functie inschakelt, versleutelt het systeem DNS-verkeer, maar kunnen query's zonder versleuteling worden verzonden.

    5. Klik op **Save** om de instellingen toe te passen.

        Nadat je de bovenstaande stappen hebt voltooid, wordt de statische netwerkconfiguratie op de computer toegepast. Je kunt de nieuwe instellingen testen door een webbrowser te openen en een website te laden.

=== "macOS"

    Zo stel je een statisch IP-adres in op macOS.

    Selecteer **System Preferences** in het Apple-menu.

    Selecteer **Network**. De volgende pagina verschijnt. Selecteer in de zijbalk een actieve netwerkinterface, zoals **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Noteer het huidige IP-adres dat aan je Mac is toegewezen. Je moet een nieuw IP-adres selecteren binnen het weergegeven bereik van particuliere IP-adressen.

    Klik rechtsonder op **Advanced**.

    Selecteer vervolgens **TCP/IP**. De volgende pagina verschijnt.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: selecteer "Manually".

    - IPv4 Address: voer een statisch IP-adres in. Behoud de eerste drie octetten van je huidige IP-adres en wijzig het laatste octet in een ongebruikte waarde. Kies in het netwerk `192.168.7.0/24` bijvoorbeeld een adres tussen `192.168.7.2` en `192.168.7.254` dat nog niet in gebruik is. Vermijd `.1`, want dit is de router. Gebruik `192.168.7.0` of `192.168.7.255` niet.

    - Subnet Mask: voer `255.255.255.0` in, of het subnetmasker dat je netwerkbeheerder heeft opgegeven.

    - Router: voer het LAN-IP-adres van je router in, bijvoorbeeld `192.168.7.1`.

    Klik op **OK** en vervolgens op **Apply**.

=== "iOS"

    De stappen kunnen per iOS-versie verschillen. De volgende stappen zijn gebaseerd op iOS-versie 26.2.2.

    1. Ga naar **Settings** -> **WLAN**. Tik naast het Wi-Fi-netwerk waarmee je momenteel bent verbonden op het blauwe informatiepictogram (i).

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Scrol omlaag naar **IPv4 Address** en stel **Configure IP** in op **Manual**.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Geef het **IP Address**, **Subnet Mask** en **Router IP** op die je op je iPhone of iPad wilt gebruiken en tik rechtsboven op **Save**.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    De stappen kunnen per Android-versie verschillen. De volgende stappen zijn gebaseerd op Android-versie 11.

    1. Ga naar **Settings** -> **Network & Internet** -> **Wi-Fi**. Tik op het netwerk waarmee je momenteel bent verbonden om het instellingenmenu te openen.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Tik rechtsboven op het potloodpictogram om de netwerkinstellingen te openen.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Tik op **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Tik op **IP Settings** en selecteer **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Voer het **IP address** in. **Gateway** wordt op basis van het IP-adres automatisch ingevuld. Voer je netwerkgateway in als dit niet gebeurt. De gateway is doorgaans het LAN-IP-adres van je router in hetzelfde subnet.

        **Tip**: kies bij gebruik van statische IP-adressen in thuisnetwerken en andere particuliere netwerken een ongebruikt hostadres in je huidige netwerksubnet. De standaardbereiken voor particuliere IP-adressen zijn:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Tik op **Save** en wacht tot opnieuw verbinding met het netwerk is gemaakt.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
