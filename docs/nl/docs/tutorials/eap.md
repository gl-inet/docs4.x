# GL.iNet-routers verbinden met een EAP-netwerk {#connect-glinet-routers-to-an-eap-network}

Sommige GL.iNet-routers ondersteunen verbinding met EAP-Wi-Fi-netwerken (Extensible Authentication Protocol).

EAP is een verificatieraamwerk dat vaak samen met **802.1X-verificatie** wordt gebruikt voor **WPA2‑Enterprise-/WPA3‑Enterprise-netwerken**. Een bekend voorbeeld is **eduroam**, een wereldwijde Wi‑Fi-roamingservice voor onderwijs en onderzoek die gebruikmaakt van 802.1X en EAP.

In deze handleiding lees je hoe je op twee manieren een GL.iNet-router met een EAP-Wi-Fi-netwerk verbindt: via het GL.iNet Web Admin Panel en via LuCI.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-MG1300 (Mango 2)
    - <u>GL-BE14000 (Flint 4)</u><sup>1</sup>
    - <u>GL-BE10000 (Slate 7 Pro)</u><sup>1</sup>
    - <u>GL-MT3600BE (Beryl 7)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - <u>GL-BE3600 (Slate 7)</u><sup>1</sup>
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>

    ---

    **Voetnoot:**

    1. Bij verbinding met WPA/WPA2/WPA3-Enterprise-netwerken ondersteunen GL-BE14000 (Flint 4), GL-BE10000 (Slate 7 Pro), GL-MT3600BE (Beryl 7) en GL-BE3600 (Slate 7) alleen netwerken met PEAP-verificatie. Andere EAP-methoden, zoals EAP-TLS, EAP-TTLS en EAP-MD5, worden niet ondersteund.

    2. GL-MT6000 (Fortify), GL-MT6000 (Flint 2) en GL-MT3000 (Beryl AX) ondersteunen met de standaardfirmware geen verbinding met EAP-netwerken. GL.iNet biedt echter oorspronkelijke OpenWrt 24-firmware voor deze modellen, waarmee EAP-ondersteuning wordt toegevoegd. Zoek het model in het [Download Center](https://dl.gl-inet.com/){target="_blank"} en raadpleeg het tabblad OPENWRT 24 voor meer informatie.

    3. GL-SFT1200 (Opal) ondersteunt vanaf firmware v4.8 verbinding met EAP-netwerken.

??? "Niet-ondersteunde modellen"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Verbinding maken via het Web Admin Panel {#connect-via-web-admin-panel}

1. Meld je aan bij het Web Admin Panel, ga naar **INTERNET** -> het gedeelte **Repeater** en klik op **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    De beschikbare netwerken worden gescand. Zoek en selecteer de EAP-SSID waarmee je verbinding wilt maken.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Je kunt ook rechtsboven op **Join Other Network** klikken om handmatig verbinding te maken met het EAP-netwerk.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Voer de **SSID** in.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Selecteer WPA/WPA2/WPA3 Enterprise bij **Security**.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Voer **Username** en **Password** in en klik op **Apply** om verbinding te maken.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Verbinding maken via LuCI {#connect-via-luci}

Het GL.iNet Web Admin Panel ondersteunt slechts een beperkt aantal EAP-typen.

Als je via het Web Admin Panel geen verbinding kunt maken met het gewenste EAP-netwerk, probeer je via de LuCI-interface verbinding te maken.

> Opmerking: de volgende stappen dienen uitsluitend ter referentie. Raadpleeg de werkelijke LuCI-pagina van je apparaat.

1. Meld je aan bij het Web Admin Panel en ga naar **SYSTEM** -> **Advanced Settings**. Installeer LuCI en klik op **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Meld je met hetzelfde beheerderswachtwoord aan bij de LuCI-interface en ga naar Network -> Wireless.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Klik in het gedeelte 2.4G of 5G op **Scan**.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Maak verbinding met het gewenste netwerk.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Problemen oplossen {#troubleshooting}

Als voor het gewenste EAP-netwerk aanvullende parameters vereist zijn, zoals het EAP-type (bijvoorbeeld PEAP of TTLS), overeenkomend domeinachtervoegsel, identiteit of anonieme identiteit, kan de EAP-verbinding via het Web Admin Panel mislukken.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Volg de onderstaande stappen om je GL.iNet-router via de LuCI-interface te verbinden met EAP-netwerken waarvoor geavanceerde instellingen vereist zijn.

1. Verkrijg de configuratie.

    Verkrijg vooraf de configuratieparameters voor het gewenste EAP-netwerk. Bijvoorbeeld:

    - EAP Type (bijvoorbeeld PEAP, TTLS of TLS)
    - Authentication domain suffix (bijvoorbeeld @company.com)
    - Identity (doorgaans de volledige gebruikersnaam)
    - Anonymous Identity (optioneel)
    - Inner authentication type (bijvoorbeeld MSCHAPv2 of PAP)
    - CA certificate (indien vereist, bereid een bestand in .crt-indeling voor)

    Dit is ter referentie een voorbeeld van Xfinity Mobile Wi-Fi.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Meld je aan bij LuCI.

    Meld je aan bij het webbeheerpaneel van de router. Als je eerder via de WebGUI zonder succes verbinding probeerde te maken met het gewenste EAP-netwerk, breek je de verbinding af.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    Ga vervolgens naar **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Meld je bij LuCI aan met hetzelfde beheerderswachtwoord.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Configureer Repeater in LuCI.

    Ga in de LuCI-interface naar Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Klik in het gedeelte 5G of 2.4G op **Scan** om naar beschikbare Wi-Fi-netwerken te zoeken.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Zoek het gewenste EAP-netwerk in de scanresultaten en klik op **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    Voer op de pagina "Joining Network" de **WPA passphrase** in en klik op **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    De configuratiepagina voor de Wireless Client wordt geopend.

4. Ga naar **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Selecteer of voer de juiste configuratieparameters voor het gewenste EAP-netwerk in, zoals hieronder. **Klik nog niet op Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Ga naar het tabblad **Advanced Settings** en geef een interfacenaam op, zoals **wlan0**. Klik vervolgens rechtsonder op **Save**.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Je keert terug naar de pagina Wireless, waar wijzigingen in behandeling worden weergegeven. Klik rechtsonder op **Save & Apply**.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Je router maakt verbinding met het gewenste EAP-netwerk.

7. Controleer de verbinding.

    ??? "De verbinding controleren in de WebGUI"

        Nadat de router verbinding heeft gemaakt met het gewenste EAP-netwerk, licht in de WebGUI een repeaterpictogram op, zoals hieronder.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Opmerking**: de configuratie in LuCI wordt niet gesynchroniseerd met die in de WebGUI. Daarom verschijnen details van de repeaterinterface, zoals het verbonden IP-adres en de gateway, niet in de WebGUI.

        In de afbeelding is het repeatergedeelte onderaan leeg. De router is echter al als repeater met het gewenste EAP-netwerk verbonden, omdat het repeaterpictogram bovenaan oplicht.

    ??? "De verbinding controleren via SSH"

        1. Meld je via [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} aan bij je router.

        2. Voer **ifconfig** in en druk op Enter.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            Je kunt nu de status van interface **wlan0** controleren.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
