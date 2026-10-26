# GoodCloud Site to Site {#goodcloud-site-to-site}

## Inleiding {#introduction}

Met GoodCloud Site to Site kunnen kantoren op verschillende locaties via internet beveiligde verbindingen met elkaar opzetten. Hiermee wordt het bedrijfsnetwerk uitgebreid, zodat computerbronnen op de ene locatie beschikbaar zijn voor medewerkers op andere locaties in het netwerk.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: tientallen filialen van hetzelfde bedrijf moeten worden samengevoegd tot één particulier netwerk, zodat bronnen op alle locaties probleemloos kunnen worden gedeeld.

**Scenario 2**: als twee bedrijven die nauw samenwerken zakelijke samenwerking nodig hebben, biedt Site to Site een gedeelde en beveiligde netwerkomgeving.

**Scenario 3**: gezinnen met IP-camera's kunnen met Site to Site op afstand toegang krijgen tot het apparaat wanneer gezinsleden niet thuis zijn, zodat toezicht overal mogelijk is.

## Voorwaarden {#conditions}

1. Je hebt ten minste twee GL.iNet-routers nodig om een Site to Site-netwerk te bouwen.

2. Ten minste één router moet een openbaar IP-adres hebben om als primair knooppunt te kunnen worden ingesteld. [Controleer of je ISP je een openbaar IP-adres toewijst](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    Gebruik bij voorkeur de router met de beste prestaties en hoogste netwerksnelheid als hoofdknooppunt.

3. Het wordt **NIET** aanbevolen om Site to Site uit te voeren wanneer de subknooppunten ook een VPN-client, Tailscale, ZeroTier of AstroWarp uitvoeren. Hierdoor kan de netwerkconfiguratie bijzonder complex worden.

## Een Site to Site-netwerk bouwen {#build-a-site-to-site-network}

1. Koppel je routers aan je GoodCloud-account. Zie [Apparaten aan de cloud koppelen](../interface_guide/cloud.md#bind-devices-to-cloud).

2. Meld je aan bij [GoodCloud](https://www.goodcloud.xyz/#/login){target="_blank"}, ga in de linkerzijbalk naar **Site to Site** en klik rechtsboven op **Create Network**.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Schakel het selectievakje links in om ten minste twee apparaten te selecteren.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    De geselecteerde apparaten worden onderaan de pagina weergegeven.

    De standaardpoort van Site to Site is **51830**. Klik linksonder op **Advanced** als je een andere poort wilt gebruiken en wijzig de poort. Klik vervolgens op **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Een Site to Site-netwerk kan voor stabiele prestaties maximaal 10 apparaten bevatten.

4. Geef je netwerk een naam en klik op **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing controleert of een apparaat als Main Node kan worden ingesteld.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Controleer het volgende als geen van je apparaten als Main Node kan worden gebruikt:

    - Ten minste één router heeft een openbaar IP-adres. Dit kan een statisch of dynamisch openbaar IP-adres zijn.
    - De poort is geopend. De standaardpoort voor Site to Site is 51830. Je kunt ook een andere poort instellen en het opnieuw proberen.
    - Als de router die je als Main Node wilt instellen zich achter NAT bevindt, moet je mogelijk port forwarding instellen.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Als meer dan één apparaat als Main Node kan worden ingesteld, kies je er één om door te gaan. We raden aan de router met de beste prestaties en hoogste netwerksnelheid als Main Node te selecteren.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Als slechts één apparaat als Main Node kan worden ingesteld, wordt de detailpagina van Site to Site rechtstreeks geopend.

6. Het netwerk is standaard uitgeschakeld. Zorg dat de LAN-IP-adressen van alle knooppunten elkaar niet overlappen. Klik indien nodig op het tandwielpictogram om het LAN-IP-adres te wijzigen en klik op **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Wacht enkele minuten. Zodra de stippellijn ononderbroken wordt, is het Site to Site-netwerk tot stand gebracht.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## De Site to Site-verbinding testen {#testing-the-site-to-site-connection}

1. Verbind je pc of smartphone met een van de knooppunten in dit Site to Site-netwerk.

2. Open een webbrowser en ga naar het LAN-IP-adres van een ander knooppunt. Als je de aanmeldpagina kunt openen, werkt de verbinding tussen deze twee knooppunten.

## Route en andere opties {#route-and-other-options}

Standaard heeft elk knooppunt toegang tot het LAN van de andere knooppunten. Uit veiligheidsoverwegingen raden we aan alleen de IP-adressen van specifieke services open te stellen.

Stel dat zich een Server A (172.30.97.100) in het subnet van Node 1 bevindt. Als je wilt dat andere knooppunten alleen toegang hebben tot Service A van Node 1, kun je dit als volgt instellen:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Je kunt ook bovenliggende routes van knooppunten toevoegen.

Elk Sub Node bouwt een versleuteld tunnelnetwerk naar Main Node. Klik op **IP Address Range** als je het IP-adres van het tunnelsubnet wilt wijzigen.

Als je een wijziging in het IP-adresbereik toepast, wordt de netwerkverbinding enkele minuten verbroken.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
