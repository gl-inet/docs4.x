# Urban Shield VPN instellen op een GL.iNet-router {#how-to-set-up-urban-shield-vpn-on-glinet-router}

[Urban Shield VPN](https://urbanshieldvpn.com/) is een VPN-provider die wereldwijd sterk beveiligde en krachtige VPN-oplossingen aanbiedt. De provider levert vooraf geconfigureerde GL.iNet VPN-routers en flexibele abonnementen voor veilig en privé browsen. Activeer Urban Shield VPN op je router om beschermd toegang te krijgen tot wereldwijde servers en veilig te browsen en streamen.

## Installatiehandleiding {#setup-guide}

Hieronder wordt GL-B3000 als WireGuard-client ingesteld om verbinding te maken met Urban Shield VPN.

### 1. Aanmelden bij Urban Shield VPN {#1-sign-up-urban-shield-vpn}

Ga naar de [officiële website van Urban Shield VPN](https://urbanshieldvpn.com/){target="_blank"} om een Urban Shield VPN-account te maken.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. De router inschakelen {#2-power-on-router}

Schakel de router in en verbind een apparaat, zoals een laptop of smartphone, via een Ethernet-kabel of Wi-Fi met de router.

### 3. Het webbeheerpaneel openen {#3-access-web-admin-panel}

Volg de onderstaande stappen om het webbeheerpaneel te openen. Als je al bent aangemeld, ga je naar het [volgende gedeelte](#4-network-setup).

Open een webbrowser, bij voorkeur Chrome, Edge of Safari, en ga naar [192.168.8.1](http://192.168.8.1){target="_blank"}. De eerste installatie van het webbeheerpaneel wordt geopend. Stel het beheerderswachtwoord in en klik op **Next** om door te gaan.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Stel je Wi-Fi-netwerk in. De pagina toont de Wi-Fi-fabrieksinstellingen, waaronder de Wi-Fi-naam (SSID) en het wachtwoord. Je kunt deze behouden of wijzigen. Verbind je apparaat opnieuw met de bijgewerkte Wi-Fi als je gegevens wijzigt.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Klik vervolgens op **Next** om je met het beheerderswachtwoord aan te melden.

### 4. Het netwerk instellen {#4-network-setup}

Rechtsboven staat een **Network Setup Wizard**, beschikbaar in firmware v4.7 en hoger. Volg de wizard om de router voor internettoegang te configureren voordat je de VPN instelt.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Urban Shield VPN activeren {#5-activate-urban-shield-vpn}

Ga in het linkermenu naar **VPN** -> **WireGuard Client**. De aanmeldpagina van Urban Shield VPN verschijnt.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Voer je Urban Shield VPN-aanmeldingsgegevens in, **Email** en **Password**, en klik op **Save And Continue**. Voor elke server wordt een configuratiebestand gegenereerd.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Selecteer de gewenste server en klik op **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

De beschikbare server(s) verschijnen vervolgens in de lijst.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Klik op het pictogram met drie stippen om de verbinding te starten.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Zodra de verbinding tot stand is gebracht, verschijnt een blauwe stip.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Je kunt de verbindingsstatus ook in VPN Dashboard bekijken.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Accountgegevens bewerken of afmelden {#edit-account-info-or-logout}

Klik op het tandwielpictogram om de accountgegevens te bewerken of je af te melden.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Abonnement verlengen {#go-renew}

Klik op **Go Renew** om op de officiële website je abonnement te verlengen.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Verwijderen {#delete}

Je kunt met één klik alle configuratiebestanden en de persoonlijke en openbare sleutel verwijderen.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
