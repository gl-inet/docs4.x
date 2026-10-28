# Een GL.iNet-router verbinden met openbare hotspots met een captive portal {#connect-a-glinet-router-to-public-hotspots-with-a-captive-portal}

## What is a captive portal? {#what-is-a-captive-portal}

Een captive portal is een webpagina waarop gebruikers van een openbare hotspot eerst een handeling moeten uitvoeren voordat ze internettoegang krijgen.

## Why use a router for public hotspots? {#why-use-a-router-for-public-hotspots}

* Openbare Wi-Fi is niet veilig

    Openbare wifi brengt aanzienlijke risico's met zich mee. Als je de GL.iNet-router met openbare wifi verbindt, kun je je via het beheerpaneel rechtstreeks bij je VPN-account aanmelden. Als je router is ingesteld om al het lokale verkeer via de VPN te leiden, wordt het verkeer van verbonden apparaten via de VPN versleuteld, zodat je niet op elk apparaat een VPN hoeft in te stellen.

* Gebruik als repeater om meerdere apparaten te verbinden

    Sommige openbare wifinetwerken, zoals hotelwifi, beperken bovendien het aantal apparaten. Verbind een reisrouter met de hotelwifi en gebruik deze als repeater voor je laptops, smartphones en tablets. De hotelwifi ziet de reisrouter als één apparaat. Je kunt meerdere apparaten met de reisrouter verbinden, tot het maximale aantal ondersteunde clients.

## Router verbinden met openbare hotspots met een captive portal {#how-to-connect-router-to-public-hotspots-with-captive-portal}

Bekijk deze video of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Connect a smartphone or computer to the router.

    Schakel de router in. Zoek op je smartphone of computer naar de SSID van de router en voer het wifiwachtwoord in. De standaard-SSID en het wachtwoord staan onder op de router.

2. Log in to your router's web Admin Panel.

    Open op je smartphone of computer een webbrowser en voer het IP-adres van de router in, standaard `192.168.8.1`. Het webbeheerpaneel wordt geopend.

    Selecteer bij de eerste aanmelding een taal en maak een wachtwoord voor het webbeheerpaneel.

3. Verbind de router met de openbare hotspot. Raadpleeg de handleiding voor [Repeater](../interface_guide/internet_repeater.md/).

## Probleemoplossing {#troubleshooting}

Als je de captive portal niet kunt openen, heeft de router mogelijk geen internettoegang. Probeer de volgende oplossingen.

### Method 1: Enable Public Hotspot Login Mode & Camouflage {#method-1-enable-public-hotspot-login-mode-camouflage}

**Opmerking**: deze twee functies zijn alleen beschikbaar in firmware v4.6 en hoger.

Wanneer je de router met een openbare hotspot verbindt, kunnen de volgende functies op de pagina **Join Network** de kans op een geslaagde verbinding vergroten.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    Als deze optie is ingeschakeld, activeert de router automatisch Login Mode for Public Hotspots wanneer hij wel met de hotspot maar niet met internet is verbonden. Sommige diensten worden dan onderbroken en de DNS-modus wordt automatisch ingesteld. Hierdoor kan je netwerkactiviteit zichtbaar zijn voor de hotspotprovider, zoals een hotel of winkelcentrum.

- Enable Camouflage

    Wanneer dit is ingeschakeld, doet de router zich voor als het clientapparaat waarmee je het beheerpaneel opent door het MAC-adres van dat apparaat na te bootsen.

---

### Method 2: Change router settings {#method-2-change-router-settings}

1. Meld je aan bij het webbeheerpaneel en ga naar NETWORK -> DNS. Controleer of **DNS Rebinding Attack Protection** is uitgeschakeld en **Mode** op **Automatic** staat.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. In the web Admin Panel, navigate to VPN -> VPN Dashboard. Make sure all VPN connections are disabled.

    **For firmware v4.7 and earlier**, the page is displayed as below.

    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}

    **For firmware v4.8 and higher**, the page is displayed as below.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. In the web Admin Panel, navigate to APPLICATIONS -> AdGuard Home. Make sure the AdGuard Home is disabled.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Open een webbrowser en open of vernieuw de pagina van de captive portal. Wacht een minuut en controleer of je automatisch naar de verificatiepagina wordt geleid.

    Als de browser op je smartphone niet wordt doorgestuurd, schakel je wifi uit en weer in en maak je opnieuw verbinding met de wifi van de router. De captive portal hoort direct na het invoeren van het wifiwachtwoord te verschijnen.

    ![connected](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Method 3：MAC Clone {#method-3mac-clone}

Sommige hotels beperken het aantal apparaten via hun MAC-adressen en registreren het adres bij de eerste verbinding. Kloon in dat geval het MAC-adres waarmee je telefoon verbinding met de hotelwifi maakt naar de router. De router gebruikt dit adres dan voor toegang tot de hotelwifi.

1. Verbind je telefoon met de hotelwifi en zoek het MAC-adres dat hiervoor wordt gebruikt.

    Voorbeeld voor iPhone (iOS 16.1.2): ga naar Settings -> Wi-Fi, selecteer de hotelwifi en noteer Wi-Fi Address.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    Bij sommige oudere modellen staat het MAC-adres niet in de wifi-instellingen. Het apparaat gebruikt dan mogelijk het werkelijke MAC-adres. Je vindt dit onder Settings > About of "About Phone".

2. Verbind je telefoon of computer met de router. Meld je aan bij het webbeheerpaneel en kloon of voer dit MAC-adres handmatig in.

    **Voor firmware v4.5 en ouder** selecteer je links NETWORK -> MAC Address.

    Selecteer Manual Mode, voer het MAC-adres uit stap 1 in en klik op Apply.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **Voor firmware v4.6 en hoger** selecteer je links INTERNET -> Repeater en klik je op Modify.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    Stel in het pop-upvenster MAC Mode in op Clone, voer het MAC-adres handmatig in en klik op Apply.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/faq/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Mogelijk moet je de router opnieuw opstarten voordat de wijziging van kracht wordt.

---

### Methode 4: hulp vragen aan hotelpersoneel {#method-4seek-help-from-hotel-staff}

Sommige hotels hanteren strenge netwerkverificatie. Als de bovenstaande methoden niet werken, vraag je het hotelpersoneel het MAC-adres van de router rechtstreeks aan de acceptatielijst toe te voegen. Gebruik het standaard-MAC-adres en niet een willekeurig adres.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
