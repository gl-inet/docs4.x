# WireGuard-client instellen op GL.iNet-routers {#set-up-wireguard-client-on-glinet-routers}

De inhoud van deze pagina is gebaseerd op firmware v4.7 en hoger. Als je apparaat een andere firmwareversie gebruikt, kies je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.7 and above" markdown="1">

- [Firmware v4.6 en ouder](wireguard_client_v4.6.md)

</div>

---

WireGuard® is een zeer eenvoudige, snelle en moderne VPN die geavanceerde cryptografie gebruikt. Het is ontworpen om sneller, eenvoudiger, compacter en gebruiksvriendelijker te zijn dan IPsec, zonder de bijbehorende complexiteit. Het biedt doorgaans aanzienlijk betere prestaties dan OpenVPN.

Bekijk deze video of volg de onderstaande stappen om een WireGuard-client op een GL.iNet-router in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

GL.iNet-routers bieden ingebouwde WireGuard-ondersteuning voor de volgende VPN-providers. Als je een actief abonnement hebt, voer je op de pagina **WireGuard Client** jouw servicegegevens in om de installatie snel te voltooien.

Selecteer hieronder de juiste WireGuard-serviceprovider om snel naar de stapsgewijze instructies te gaan.

* [AzireVPN instellen](#set-up-azirevpn)
* [Hide.me instellen](#set-up-hideme)
* [IPVanish instellen](#set-up-ipvanish)
* [Mullvad instellen](#set-up-mullvad)
* [NordVPN instellen](#set-up-nordvpn)
* [PIA (Private Internet Access) instellen](#set-up-pia-private-internet-access)
* [PureVPN instellen](#set-up-purevpn)
* [Surfshark instellen](#set-up-surfshark)
* [Windscribe instellen](#set-up-windscribe)
* [Set Up X-VPN](#set-up-x-vpn)

Als je een abonnement bij een andere WireGuard-serviceprovider hebt, download je een configuratiebestand van de website van die provider en upload je het naar je router om de VPN-verbinding in te stellen.

* [WireGuard Client handmatig instellen (voor andere providers)](#set-up-wireguard-client-manually-for-other-providers)

## AzireVPN instellen {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is een privacygerichte VPN-dienst die veilige, moderne en robuuste tunnels zoals WireGuard biedt.

Bekijk deze video om AzireVPN via het webbeheerpaneel of de mobiele app op GL.iNet-routers in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Of volg de onderstaande stappen om AzireVPN via het webbeheerpaneel in te stellen.

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Voer je AzireVPN-**Username** en -**Password** in, dus de gegevens waarmee je je bij AzireVPN aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![azirevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![azirevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

3. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![azirevpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Abonnement verlengen.

    Als je op **Go Renew** klikt, word je naar de officiële website geleid om je abonnement te verlengen.

    ![azirevpn go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![azirevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Hide.me instellen {#set-up-hideme}

[Officiële website](https://hide.me/en/){target="_blank"}

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Voer je Hide.me-**Username** en -**Password** in, dus de gegevens waarmee je je bij Hide.me aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![hideme login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![hideme start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![hideme connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

3. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![hideme update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![hideme edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![hide.me delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## IPVanish instellen {#set-up-ipvanish}

[Officiële website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Voer je IPVanish-**Username** en -**Password** in, dus de gegevens waarmee je je bij IPVanish aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![ipvanish login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![ipvanish select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![ipvanish start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![ipvanish connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![ipvanish update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![ipvanish edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![ipvanish delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Mullvad instellen {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} is een VPN-dienst die je onlineactiviteiten, identiteit en locatie privé helpt te houden.

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Voer je Mullvad-**Account** in, een nummer van 16 cijfers, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![mullvad login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![mullvad select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![mullvad start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![mullvad update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![mullvad edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Abonnement verlengen.

    Als je op **Go Renew** klikt, word je naar de officiële website geleid om je abonnement te verlengen.

    ![mullvad go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![mullvad delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## NordVPN instellen {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} is een online VPN-dienst die snelheid en beveiliging combineert.

1. Klik [hier](https://my.nordaccount.com/){target="_blank"} om je aan te melden bij je NordVPN-webaccount.

    ![nordvpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

    Klik na het aanmelden bij het Nord-dashboard in het linkermenu op **NordVPN**, zoek het gedeelte **Access Token** en klik op **Get Access token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

    Klik op de volgende pagina op **Generate new token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

    Selecteer in het pop-upvenster de vervaldatum van het token en klik op **Generate token**.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

    Je krijgt vervolgens het toegangstoken te zien. Kopieer het token voor later gebruik.

    **Opmerking**: het toegangstoken wordt maar één keer weergegeven. Kopieer het daarom meteen. Nadat je dit venster hebt gesloten, is het token niet meer zichtbaar en moet je zo nodig een nieuw token genereren.

    ![nordvpn token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Meld je aan bij het webbeheerpaneel van de router en ga naar **VPN** -> **WireGuard Client** -> **NordVPN**.

    Voer **Token** in en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![nordvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![nordvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

5. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![nordvpn edit credentials or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![nordvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## PIA (Private Internet Access) instellen {#set-up-pia-private-internet-access}

[Officiële website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **PIA**.

1. Voer je PIA-**Username** en -**Password** in, dus de gegevens waarmee je je bij PIA aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![pia login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![pia select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![pia start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![pia connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![pia update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![pia edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![pia delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## PureVPN instellen {#set-up-purevpn}

[Officiële website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

[PureVPN 15 dagen gratis proberen](https://purevpn.com/refer-a-friend-v2?referrer=bEZTci9KcmtQSTFPbXlPak03NWtENWZaL1BHNENlR0JOMzV6RURhWFhSOD0=){target="_blank"}

1. Klik [hier](https://www.purevpn.com/){target="_blank"} om je aan te melden bij je PureVPN-dashboard.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_login.png){class="glboxshadow"}

    Klik na het aanmelden in het linkermenu op **Subscriptions**, scrol omlaag naar je **credentials** en kopieer de gebruikersnaam en het wachtwoord voor later gebruik.

    ![purevpn credentials](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_credentials.png){class="glboxshadow"}

2. Meld je aan bij het webbeheerpaneel van de router en ga naar **VPN** -> **WireGuard Client** -> **PureVPN**.

    Voer de gekopieerde **Username** en **Password** in en klik op **Save and Continue**.

    ![purevpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Alle beschikbare configuratiebestanden worden gegenereerd.

    ![purevpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![purevpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![purevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![purevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![purevpn edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![purevpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Surfshark instellen {#set-up-surfshark}

[Officiële website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Voer je Surfshark-**Username** en -**Password** in, dus de gegevens waarmee je je bij Surfshark aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![surfshark login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![surfshark select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![surfshark start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![surfshark connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![surfshark update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![surfshark edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Vernieuwen.

    Klik op **Refresh** om de openbare sleutel bij te werken als er geen verbinding met de VPN-server kan worden gemaakt.

    ![surfshark refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![surfshark delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Windscribe instellen {#set-up-windscribe}

[Officiële website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Voer je Windscribe-**Username** en -**Password** in, dus de gegevens waarmee je je bij Windscribe aanmeldt, en klik op **Save and Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![windscribe login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Servers selecteren.

    Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![windscribe select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Vervolgens krijg je een lijst met configuratiebestanden voor de geselecteerde server.

    ![windscribe config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![windscribe start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![windscribe connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

4. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![windscribe update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Aanmeldgegevens bewerken of afmelden.

    Klik op het tandwielpictogram om je aanmeldgegevens te bewerken of je af te melden.

    ![windscribe edit credential or logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Vernieuwen.

    Klik op **Refresh** om de openbare sleutel bij te werken als er geen verbinding met de VPN-server kan worden gemaakt.

    ![windscribe refresh](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Alles verwijderen.

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen. Je kunt daarbij kiezen of je ook de privé- en openbare sleutels verwijdert.

    ![windscribe delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Set Up X-VPN {#set-up-x-vpn}

[Officiële website](https://xvpn.io/){target="_blank"}

**Opmerking**: X-VPN is vanaf firmware v4.11 in GL.iNet-routers geïntegreerd.

1. Haal eerst een X-VPN-token op via de officiële website.

    Klik [hier](https://xvpn.io/login){target="_blank"} om je aan te melden bij je X-VPN-webaccount.

    ![xvpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn1.png){class="glboxshadow"}

    Klik na het aanmelden in het linkermenu op **Settings**. Zoek **Login Token** en klik op **Generate**.

    ![xvpn settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn2.png){class="glboxshadow"}

    De pagina genereert een token dat 15 minuten geldig is. Kopieer het token voor later gebruik.

    ![xvpn generate token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn3.png){class="glboxshadow"}

2. Meld je aan bij het webbeheerpaneel van je GL.iNet-router, ga naar **VPN** -> **VPN Client Profile** en klik op **X-VPN**.

    ![xvpn enter token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn4.png){class="glboxshadow"}

    Voer het token in en klik op **Save and Continue**.

    ![xvpn enter token](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn5.png){class="glboxshadow"}

3. Selecteer de server(s) waarmee je verbinding wilt maken en klik op **Apply**.

    ![xvpn select servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn6.png){class="glboxshadow"}

    Vervolgens krijg je een lijst met configuratiebestanden voor de geselecteerde server.

    ![xvpn config files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn7.png){class="glboxshadow"}

4. Een verbinding starten.

    Selecteer de gewenste server en klik rechts op het pictogram met drie puntjes om een verbinding te starten.

    ![xvpn start](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn8.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    ![xvpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn9.png){class="glboxshadow"}

    Op het **VPN Dashboard** kun je ook de details van de VPN-verbinding bekijken en VPN-tunnels en beleidsregels maken en beheren.

5. Servers bijwerken.

    Klik op **Update Servers** om de nieuwste lijst met beschikbare servers op te halen en verbindingsproblemen door onderhoud of uitschakeling van servers te voorkomen.

    ![xvpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn10.png){class="glboxshadow"}

6. Abonnement verlengen.

    Als je op **Go Renew** klikt, word je naar de officiële website geleid om je abonnement te verlengen.

    ![xvpn renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn11.png){class="glboxshadow"}

7. Configuraties verwijderen.

    Klik rechts op het tandwielpictogram en selecteer **Delete Configurations** om bepaalde of alle configuratiebestanden in één keer te verwijderen.

    ![xvpn delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn12.png){class="glboxshadow"}

8. Verificatiegegevens wijzigen.

    Klik rechts op het tandwielpictogram en selecteer **Modify Authentication Information** om zo nodig je aanmeldingstoken te bewerken.

    ![xvpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn13.png){class="glboxshadow"}

    ![xvpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn14.png){class="glboxshadow" width="600"}

9. Log out.

    Klik rechts op het tandwielpictogram en selecteer **Logout** om je zo nodig af te melden. Hiermee worden de accountgegevens, bijbehorende openbare en privésleutel en de configuratiebestanden op de router verwijderd. Ga voorzichtig te werk.

    ![xvpn logout](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn15.png){class="glboxshadow"}

## WireGuard Client handmatig instellen (voor andere providers) {#set-up-wireguard-client-manually-for-other-providers}

Als je een abonnement bij een andere WireGuard-serviceprovider hebt, download je een configuratiebestand van de website van die provider. Volg daarna de onderstaande stappen om WireGuard Client in te stellen. Raadpleeg [deze handleiding](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) of neem contact op met de ondersteuning van de provider als je niet weet hoe je de configuratiebestanden downloadt.

Ga in het webbeheerpaneel naar **VPN** -> **WireGuard Client**.

1. Klik op **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. Er wordt een groep in de linkerzijbalk gemaakt.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Geef de groep een duidelijke naam, bijvoorbeeld azirevpn. Upload vervolgens een configuratiebestand (ondersteunde indelingen: zip, tar, gz, conf en txt) of voeg de configuratiegegevens handmatig als tekst toe.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Een configuratiebestand uploaden**.

        Klik op het uploadgebied om je WireGuard-configuratiebestand te uploaden en klik vervolgens op **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Configuratie handmatig toevoegen**.

        Klik onderaan het uploadgebied op **Manually Add Configuration**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Geef de configuratie een duidelijke naam, plak deze in het tekstvak en klik op **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Als je elk veld wilt controleren, schakel je over naar Item mode en controleer je de configuratiegegevens. Klik vervolgens op **Apply**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Klik rechts op het pictogram met drie puntjes om de verbinding te starten.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

    Je kunt de details van de VPN-verbinding ook controleren op het **VPN Dashboard**.

## WireGuard Client via de mobiele app instellen {#set-up-wireguard-client-via-mobile-app}

Je kunt een WireGuard-client ook instellen via de [mobiele app](https://www.gl-inet.com/app/#download-app-glinet).

De mobiele app is geïntegreerd met enkele WireGuard-serviceproviders, waaronder AzireVPN, Mullvad VPN, OVPN, StrongVPN en PIA VPN. Je kunt eenvoudig een WireGuard-client instellen door de aanmeldgegevens van je WireGuard-dienst in te voeren.

Installeer de app en volg de instructies op het scherm om de gewenste configuratie in te stellen.

## WireGuard-server op een GL.iNet-router instellen {#set-up-wireguard-server-on-glinet-router}

Wil je geen abonnement op een externe VPN-dienst? Je kunt twee GL.iNet-routers aanschaffen en de ene als WireGuard-server en de andere als WireGuard-client instellen.

Dit is vooral geschikt wanneer de internetprovider van je thuisnetwerk een openbaar IP-adres biedt en je onderweg veilig via VPN verbinding wilt maken met je thuisnetwerk en interne netwerkbronnen. Zo vermijd je de kosten en het beheer van een doorlopend abonnement op een commerciële VPN-dienst.

Raadpleeg [deze pagina](wireguard_server.md) om een WireGuard-server in te stellen.

---

WireGuard® is een geregistreerd handelsmerk van Jason A. Donenfeld.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
