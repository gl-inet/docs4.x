# AstroWarp {#astrowarp}

**Opmerking**: deze handleiding geldt voor de nieuwe versie van AstroWarp. De functie is in firmware v4.11, of v4.10 voor GL-MG1300, hernoemd naar [GoodPAS](./goodpas.md).


De nieuwe AstroWarp is geïntegreerd in de GL.iNet-router-SDK. De functie gebruikt het AmneziaWG-protocol met ingebouwde verkeersobfuscatie en biedt stabiele, veilige verbindingen voor betrouwbare externe toegang, altijd en overal.

Deze functie biedt naadloze externe toegang tot je thuisnetwerk. Je kunt apparaten rechtstreeks via een dynamische toegangscode in het webbeheerpaneel instellen en koppelen. Zo breng je binnen enkele seconden een beveiligde verbinding tussen je reisrouter en thuisnetwerk tot stand, zonder registratie of aanmelding.

De oudere AstroWarp, die nog zichtbaar is in het webbeheerpaneel, gebruikte een afzonderlijk AstroWarp-platform om externe netwerkverbindingen tot stand te brengen. Klik [hier](https://docs.astrowarp.net/){target="_blank"} voor de documentatie van de oudere AstroWarp.

**Note:**

1. Het wordt afgeraden AstroWarp tegelijk met een van de volgende functies te gebruiken, omdat dit routeringsconflicten kan veroorzaken: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, Tailscale en Tor.

2. Wanneer AstroWarp is ingeschakeld, kan Network Mode niet worden gebruikt.

3. Wanneer AstroWarp is ingeschakeld, heeft het de hoogste routeringsprioriteit en kan het niet met VPN Client worden gecascadeerd.

    Als Router A en Router B bijvoorbeeld een AstroWarp-netwerk tot stand brengen met Router B als exit node, verlaat via AstroWarp doorgestuurd verkeer het netwerk via het openbare WAN-IP-adres van Router B, ook wanneer VPN Client op Router B is ingeschakeld. Dit verkeer wordt niet via de VPN Client-tunnel van Router B doorgestuurd.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"

    Deze modellen zijn compatibel met de nieuwe AstroWarp. Klik [hier](https://docs.astrowarp.net/en/quick_start/){target="_blank"} voor de lijst met modellen die de oudere AstroWarp ondersteunen.

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-MG1300 (Mango 2)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-X2000 (Spitz Plus)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-MT2500/GL-MT2500A (Brume 2)

    **Opmerking**: modellen met ※ ondersteunen de geïntegreerde AstroWarp in bètafirmware.

??? "Niet-ondersteunde modellen"

    Deze apparaten zijn niet compatibel met de nieuwe AstroWarp. Bepaalde modellen werken nog wel met de oudere AstroWarp. Raadpleeg [deze pagina](https://docs.astrowarp.net/en/quick_start/){target="_blank"} voor meer informatie.

    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-B3000 (Marble)
    - GL-A1300 (Slate Plus)
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
    - GL-X300B (Collie)

## Snelle installatie {#quick-setup}

In het volgende voorbeeld gebruiken we **Flint 3 (GL-BE9300)** en **Slate 7 (GL-BE3600)** om een AstroWarp-netwerk in te stellen.

Flint 3 werkt als thuisrouter. Slate 7 werkt als reisrouter en routeert netwerkverkeer terug naar Flint 3 voor internettoegang.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

1. Configureer Flint 3 voor internet.

    Meld je aan bij het webbeheerpaneel van Flint 3 en ga naar de pagina **INTERNET**. Verbind de router met internet via een van de ondersteunde methoden: Ethernet, Repeater, Tethering of Cellular.

    Zoals hieronder weergegeven, is de thuisrouter Flint 3 met een Ethernet-kabel verbonden met de modem van de internetprovider (Hong Kong Broadband Network Ltd).

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Genereer een Access Code.

    Ga in het webbeheerpaneel van Flint 3 naar **CLOUD SERVICES** -> **AstroWarp**. Klik op **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Er wordt een **Access Code** gegenereerd. Kopieer deze code voor later gebruik.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configureer Slate 7 voor internet.

    Meld je aan bij het webbeheerpaneel van Slate 7 en ga naar de pagina **INTERNET**. Verbind de router met internet via een van de ondersteunde methoden: Ethernet, Repeater, Tethering of Cellular.

    Zoals hieronder weergegeven, is de reisrouter Slate 7 verbonden met de persoonlijke hotspot van een iPhone 15 Pro in Shenzhen via het netwerk van China Unicom Guangdong Province.

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Voer de Access Code in.

    Ga in het webbeheerpaneel van Slate 7 naar **CLOUD SERVICES** -> **AstroWarp**. Klik op **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Voer de Access Code uit stap 2 in.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Wacht tot de verificatie is voltooid.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    De verbinding met de thuisrouter Flint 3 wordt tot stand gebracht. Je kunt nu veilig via je thuisnetwerk internetten.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    Het webbeheerpaneel van Flint 3 toont ook de verbindingsstatus, zoals hieronder weergegeven.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Verbinding testen {#test-connectivity}

1. Verbind een laptop of smartphone met de Wi-Fi van de reisrouter Slate 7.

2. Open een browser en ga naar [ipcheck.ing](https://ipcheck.ing/){target="_blank"} of een andere website om IP-adressen op te zoeken.

    Het openbare IP-adres van Flint 3 wordt weergegeven. Dit geeft aan dat Slate 7 via je thuisrouter Flint 3 internet gebruikt.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Verbreek de AstroWarp-verbinding op Slate 7 en vernieuw de webpagina om het IP-verzoek opnieuw uit te voeren.

    Het openbare IP-adres van Slate 7 wordt weergegeven. Dit geeft aan dat Slate 7 via het lokale netwerk internet gebruikt.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## FAQ {#faq}

1. **V: Welke indeling heeft de dynamische toegangscode en hoe lang is deze geldig?**

    A: Het is een code van 8 tekens, bestaande uit cijfers en hoofdletters, die 10 minuten geldig is.

2. **V: Wat gebeurt er met de reisrouter als ik de verbinding op de thuisrouter beëindig?**

    A: De reisrouter verbreekt de verbinding en krijgt in afwachting geen netwerktoegang. Zodra de thuisrouter de verbinding hervat, kan de reisrouter automatisch opnieuw verbinding maken zonder de toegangscode opnieuw in te voeren.

3. **V: Wanneer krijgt de reisrouter de status in afwachting?**

    A: De reisrouter krijgt de status in afwachting wanneer op de thuisrouter een van de volgende omstandigheden optreedt:

    - De AstroWarp-verbinding wordt beëindigd
    - De internettoegang valt weg

4. **V: Wat doet de knop Reset rechtsboven?**

    A: Alle geautoriseerde apparaten worden gewist en de pagina voor het opnieuw selecteren van de routerrol wordt geopend.

5. **V: Wat gebeurt er met de reisrouter als ik AstroWarp op de thuisrouter reset?**

    A: Nadat de thuisrouter is gereset, worden de extern verbonden apparaten van het AstroWarp-netwerk losgekoppeld en gebruiken ze hun lokale netwerk voor internettoegang.

6. **V: Hoe schakel ik de nieuwe AstroWarp in het webbeheerpaneel van de router uit en ga ik terug naar de oudere AstroWarp?**

    A: Ga in het webbeheerpaneel van de router naar **CLOUD SERVICES** -> **AstroWarp** en klik rechtsboven op **Reset**.

    ![reset](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/reset.png){class="glboxshadow"}

    Meld je vervolgens met je cloudaccount aan bij [astrowarp.net](https://my.astrowarp.net/#/login){target="_blank"}. Klik na het aanmelden op de knop **"+"** om de router aan je AstroWarp-netwerk toe te voegen.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/add_device.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
