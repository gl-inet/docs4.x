# ZeroTier {#zerotier}

ZeroTier is een softwarematig virtueel privénetwerk (VPN) voor veilige, versleutelde communicatie tussen apparaten via internet. Het maakt een privé virtueel netwerk waarin apparaten communiceren alsof ze zich in hetzelfde lokale netwerk bevinden, ongeacht locatie of topologie. ZeroTier is eenvoudig te installeren en biedt end-to-endversleuteling, netwerksegmentatie en bridging.

De ZeroTier-functie op GL.iNet-routers is beschikbaar sinds firmware v4.2 en laat de router deelnemen aan een virtueel ZeroTier-netwerk. Daarna kun je op afstand de router en zijn WAN- en LAN-bronnen openen.

**Note**:

1. Gelijktijdig gebruik van ZeroTier met OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale of AstroWarp wordt wegens mogelijke routeringsconflicten afgeraden.

2. Deze functie is momenteel in bèta en kan fouten bevatten.

3. Sommige modellen ondersteunen ZeroTier wegens onvoldoende geheugen niet, ook niet met firmware v4.2 of hoger.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Niet-ondersteunde modellen"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## ZeroTier-netwerk instellen {#set-up-zerotier-network}

Er zijn twee versies van ZeroTier Central: New Central en Legacy Central.

- **New Central**: een nieuwere versie met verbeterd gebruiksgemak en nieuwe functies. Aanbevolen voor nieuwe gebruikers.

- **Legacy Central**: voor accounts die vóór november 2025 zijn gemaakt. Bestaande gebruikers kunnen hun netwerken ermee blijven beheren.

Beide versies kunnen naast elkaar worden gebruikt, maar er is momenteel geen rechtstreeks migratiepad.

Selecteer de juiste versie om door te gaan.

### New Central {#new-central}

GL-MT3600BE wordt hieronder als voorbeeld gebruikt.

1. Ga naar de [officiële ZeroTier-website](https://www.zerotier.com/){target="_blank"} en meld je aan.

    ![zerotier login](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Maak een organisatie.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Selecteer een abonnement. Personal omvat 10 apparaten, 1 netwerkbeheerder en 1 netwerk. Kies Essential of Scale voor meer netwerken, apparaten, aangepaste routes of DNS.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Het ZeroTier-netwerk is gemaakt. Noteer rechtsboven de **Network ID** van 16 alfanumerieke tekens; deze is nodig om andere apparaten te verbinden.

    ![network id](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Schakel ZeroTier op de GL.iNet-router in.

    Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **ZeroTier**.

    Schakel ZeroTier in, voer Network ID in en klik op **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Na korte tijd meldt de interface dat autorisatie vereist is. Klik op **ZeroTier Central** om ZeroTier Central te openen.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autoriseer je apparaat in ZeroTier Central.

    Zoek in ZeroTier Central het Pending-apparaat en autoriseer het.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Na autorisatie ziet de pagina er als volgt uit.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Voeg met [deze handleiding](https://docs.zerotier.com/platforms/){target="_blank"} een computer, smartphone of ander apparaat aan hetzelfde netwerk toe.

    Hieronder wordt een Windows 10 Pro-laptop gebruikt.

    1. Installeer ZeroTier op de laptop via [deze link](https://www.zerotier.com/download/){target="_blank"}.

    2. Start ZeroTier. Het pictogram verschijnt rechtsonder in het systeemvak.

    3. Klik met rechts op het pictogram, selecteer **Join New Network** en voer Network ID uit stap 4 in.

        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Ga naar ZeroTier Central, zoek het Pending-apparaat en autoriseer het.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Na autorisatie ziet de pagina er als volgt uit. Je ziet apparaatgegevens zoals **Device ID**, **Name**, **Status**, **Managed IP** en **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Tip**: klik rechts op het pictogram met drie stippen om de apparaatnaam, Managed IP(s) en geavanceerde instellingen te wijzigen.

8. Klik op **Managed IP** van de router om het te kopiëren. Gebruik dit adres vanaf de laptop in hetzelfde ZeroTier-netwerk.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Test de verbinding.

    Open op de laptop in hetzelfde netwerk een browser en voer Managed IP van de router in.

    Als het webbeheerpaneel toegankelijk is, werkt de ZeroTier-verbinding.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Je kunt Managed IP ook vanaf de laptop `pingen`. Een antwoord bevestigt de verbinding.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central {#legacy-central}

GL-MT2500 wordt hieronder als voorbeeld gebruikt.

1. Maak je eerste ZeroTier-netwerk.

    Gebruik de officiële [Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} om een account en netwerk te maken. Noteer Network ID van 16 alfanumerieke tekens.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Schakel ZeroTier op de GL.iNet-router in.

    Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **ZeroTier**.

    Schakel ZeroTier in, voer Network ID in en klik op **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_enable.png){class="glboxshadow"}

    Na korte tijd meldt de interface dat autorisatie vereist is.

    Klik op **ZeroTier Central** om ZeroTier Central te openen.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autoriseer je apparaat in ZeroTier Central.

    Ga in ZeroTier Central naar **Members**, zoek het nieuwe apparaat en selecteer **Auth**. Pas zo nodig de apparaatnaam aan.

    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Na korte tijd wijst ZeroTier een **Managed IP** toe. Noteer dit adres voor de test.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/managed_ip.png){class="glboxshadow"}

4. Voeg met [deze handleiding](https://docs.zerotier.com/platforms/){target="_blank"} een ander apparaat aan hetzelfde netwerk toe.

5. Test de verbinding.

    Open op een ander apparaat in hetzelfde netwerk een browser en voer ZeroTier Managed IP van de router in.

    Het webbeheerpaneel van de router wordt geopend.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/web_admin_panel.png)

    Je kunt ook `ping` gebruiken. Raadpleeg de [Quickstart Guide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"}.

## Externe WAN-toegang toestaan {#allow-remote-access-wan}

Wanneer dit is ingeschakeld, zijn bronnen aan de WAN-zijde via ZeroTier toegankelijk.

In de onderstaande topologie kun je vanaf `leo-phone` GL-AXT1800 via `192.168.29.1` openen. GL-AXT1800 is het upstream apparaat van GL-MT2500 in hetzelfde ZeroTier-netwerk.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Opmerking**: hiervoor zijn routeringsregels in ZeroTier vereist. In Legacy Central kun je gratis één aangepaste route toevoegen; New Central vereist Essential of hoger. Klik [hier](https://www.zerotier.com/pricing/) voor meer informatie.

De volgende stappen gebruiken Legacy Central.

1. Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **ZeroTier**.

    Schakel **Allow Remote Access WAN** in en klik op **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Er wordt gevraagd routeringsregels te configureren. Houd de pagina open of noteer Destination en Via.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Ga in **ZeroTier Central** naar **Advanced**.

    Voer Destination en Via uit de vorige stap in en klik op **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_1.png){class="glboxshadow"}

    Na toevoeging ziet **Managed Routes** er als volgt uit.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_2.png){class="glboxshadow"}

3. Je kunt GL-AXT1800 vanaf andere apparaten via `192.168.29.1` openen, evenals alle apparaten in `192.168.29.0/24`.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Externe LAN-toegang toestaan {#allow-remote-access-lan}

Wanneer dit is ingeschakeld, zijn bronnen aan de LAN-zijde via ZeroTier toegankelijk.

In de onderstaande topologie kun je vanaf `leo-phone` via SSH bij Ubuntu op `192.168.8.110` aanmelden. Ubuntu is een downstream apparaat van GL-MT2500 in hetzelfde ZeroTier-netwerk.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Opmerking**: hiervoor zijn routeringsregels in ZeroTier vereist. In Legacy Central kun je gratis één aangepaste route toevoegen; New Central vereist Essential of hoger. Klik [hier](https://www.zerotier.com/pricing/) voor meer informatie.

De volgende stappen gebruiken Legacy Central.

1. Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **ZeroTier**.

    Schakel **Allow Remote Access LAN** in en klik op **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Er wordt gevraagd routeringsregels te configureren. Houd de pagina open of noteer Destination en Via.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Ga in **ZeroTier Central** naar **Advanced**.

    Voer Destination en Via uit de vorige stap in en klik op **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_3.png){class="glboxshadow"}

    Na toevoeging ziet **Managed Routes** er als volgt uit.

    ![add route](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_4.png){class="glboxshadow"}

3. Je kunt Ubuntu vanaf andere apparaten op `192.168.8.110` pingen of via SSH openen, evenals alle apparaten in `192.168.8.0/24`.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
