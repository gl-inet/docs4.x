# GoodPAS {#goodpas}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.11, of v4.10 voor GL-MG1300, waarbij AstroWarp is hernoemd naar GoodPAS. Raadpleeg [AstroWarp](./astrowarp.md) als je apparaat een oudere firmwareversie gebruikt.

---

Ga links in het webbeheerpaneel naar **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS is een geavanceerde oplossing voor externe toegang die in de GL.iNet-router-SDK is geïntegreerd. De functie gebruikt het AmneziaWG-protocol met ingebouwde verkeersobfuscatie en biedt stabiele, veilige verbindingen voor betrouwbare externe toegang, altijd en overal.

Deze functie biedt naadloze externe toegang tot je thuisnetwerk. Je kunt apparaten rechtstreeks via een dynamische toegangscode in het webbeheerpaneel instellen en koppelen. Zo breng je binnen enkele seconden een beveiligde verbinding tussen je reisrouter en thuisnetwerk tot stand, zonder registratie of aanmelding.

**Note**:

1. Het wordt afgeraden GoodPAS tegelijk met een van de volgende functies te gebruiken, omdat dit routeringsconflicten kan veroorzaken: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, Tailscale en Tor.

2. Wanneer GoodPAS is ingeschakeld, kan Network Mode niet worden gebruikt.

3. Wanneer GoodPAS is ingeschakeld, heeft het de hoogste routeringsprioriteit en kan het niet met VPN Client worden gecascadeerd.

Als Router A en Router B bijvoorbeeld een GoodPAS-netwerk tot stand brengen met Router B als exit node, verlaat via GoodPAS doorgestuurd verkeer het netwerk via het openbare WAN-IP-adres van Router B, ook wanneer VPN Client op Router B is ingeschakeld. Dit verkeer wordt niet via de VPN Client-tunnel van Router B doorgestuurd.

## Snelle installatie {#quick-setup}

In het volgende voorbeeld gebruiken we **Flint 3(GL-BE9300)** en **Mango 2(GL-MG1300)** om een GoodPAS-netwerk in te stellen.

Flint 3 werkt als thuisrouter. Mango 2 werkt als reisrouter en routeert netwerkverkeer terug naar Flint 3 voor internettoegang.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configureer Flint 3 voor internet.

Meld je aan bij het webbeheerpaneel van Flint 3 en ga naar de pagina INTERNET. Verbind de router met internet via een van de ondersteunde methoden: Ethernet, Repeater, Tethering of Cellular.

    Zoals hieronder weergegeven, is de thuisrouter Flint 3 met een Ethernet-kabel verbonden met de modem van de internetprovider (Hong Kong Broadband Network Ltd).

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Genereer een Access Code.

    Ga in het webbeheerpaneel van Flint 3 naar **CLOUD SERVICES** -> **GoodPAS**. Klik op **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

Er wordt een Access Code gegenereerd. Kopieer deze code voor later gebruik.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configureer Mango 2 voor internet.

Meld je aan bij het webbeheerpaneel van Mango 2 en ga naar de pagina INTERNET. Verbind de router met internet via een van de ondersteunde methoden: Ethernet, Repeater, Tethering of Cellular.

    Zoals hieronder weergegeven, is de reisrouter Mango 2 verbonden met de persoonlijke hotspot van een iPhone 17 in Shenzhen via het netwerk van China Unicom Guangdong Province.

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Voer de Access Code in.

    Ga in het webbeheerpaneel van Mango 2 naar **CLOUD SERVICES** -> **GoodPAS**. Klik op **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Voer de Access Code uit stap 2 in.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Wacht tot de verificatie is voltooid.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    De verbinding met de thuisrouter Flint 3 wordt tot stand gebracht. Je kunt nu veilig via je thuisnetwerk internetten.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Het webbeheerpaneel van Flint 3 toont ook de verbindingsstatus, zoals hieronder weergegeven.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Verbinding testen {#test-connectivity}

1. Verbind een laptop of smartphone met de Wi-Fi van de reisrouter Mango 2.

2. Open een browser en ga naar [ipcheck.ing](https://ipcheck.ing/){target="_blank"} of een andere website om IP-adressen op te zoeken.

    Het openbare IP-adres van Flint 3 wordt weergegeven. Dit geeft aan dat Mango 2 via je thuisrouter Flint 3 internet gebruikt.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Verbreek de GoodPAS-verbinding op Mango 2 en vernieuw de webpagina om het IP-verzoek opnieuw uit te voeren.

    Het openbare IP-adres van Mango 2 wordt weergegeven. Dit geeft aan dat Mango 2 via het lokale netwerk internet gebruikt.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ {#faq}

1. **V: Welke indeling heeft de dynamische toegangscode en hoe lang is deze geldig?**

    A: Het is een code van 8 tekens, bestaande uit cijfers en hoofdletters, die 10 minuten geldig is.

2. **V: Wat gebeurt er met de reisrouter als ik de verbinding op de thuisrouter beëindig?**

    A: De reisrouter verbreekt de verbinding en krijgt in afwachting geen netwerktoegang. Zodra de thuisrouter de verbinding hervat, kan de reisrouter automatisch opnieuw verbinding maken zonder de toegangscode opnieuw in te voeren.

3. **V: Wanneer krijgt de reisrouter de status in afwachting?**

    A: De reisrouter krijgt de status in afwachting wanneer op de thuisrouter een van de volgende omstandigheden optreedt:

    - De GoodPAS-verbinding wordt beëindigd
    - De internettoegang valt weg

4. **V: Wat doet de knop Reset rechtsboven?**

    A: Alle geautoriseerde apparaten worden gewist en de pagina voor het opnieuw selecteren van de routerrol wordt geopend.

5. **V: Wat gebeurt er met de reisrouter als ik GoodPAS op de thuisrouter reset?**

    A: Nadat de thuisrouter is gereset, worden de extern verbonden apparaten van het GoodPAS-netwerk losgekoppeld en gebruiken ze hun lokale netwerk voor internettoegang.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
