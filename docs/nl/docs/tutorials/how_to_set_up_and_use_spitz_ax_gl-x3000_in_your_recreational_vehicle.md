# Spitz AX (GL-X3000) instellen en gebruiken in je camper {#how-to-set-up-and-use-spitz-ax-gl-x3000-in-your-recreational-vehicle}

In deze handleiding lees je hoe je Spitz AX instelt en gebruikt in je camper. Voordat je begint, heb je de volgende aanvullende apparatuur en services nodig of mogelijk nodig:

- Een of meer simkaarten of een USB-kabel voor tethering, afhankelijk van de methode waarmee je verbinding met internet maakt. Vraag je provider om de APN als je simkaarten gebruikt.
- Een dakantenne als je een betere dekking wilt.
- [Een Starlink-abonnement](https://www.starlink.com/roam){target="_blank"} als je naar gebieden zonder cellulaire dekking gaat.

---

## 1. Je Spitz AX en andere apparatuur installeren {#1-install-your-spitz-ax-and-other-equipment}

Stel je Spitz AX vóór vertrek in met de volgende stappen.

### Stap 1: een locatie voor je Spitz AX kiezen {#step-1-choose-a-location-for-your-spitz-ax}

Voor een zo groot mogelijke dekking wordt een centrale locatie zonder obstakels aanbevolen. Zorg dat de locatie zich binnen 1 meter van de stroombron bevindt, de lengte van de kabel van de voedingsadapter.

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Je kunt de Spitz AX op een vlak oppervlak plaatsen of aan een wand bevestigen. Volg de volgende stap als je de router aan een wand wilt bevestigen.

### (Optioneel) Stap 2: je Spitz AX aan een wand bevestigen {#optional-step-2-install-your-spitz-ax-on-the-wall}

Je kunt de Spitz AX op twee manieren aan een wand bevestigen:

- Met het meegeleverde zelfklevende kussentje
- Met de wandsteunen

De wandsteunen zijn meegeleverd. Volg deze stappen om de Spitz AX aan de wand te bevestigen:

1.	Bevestig de steun met schroeven aan de wand.
2.	Klik de Spitz AX op de steun.

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Optioneel) Stap 3: de dakantenne van de camper installeren {#optional-step-3-install-the-rv-roof-antenna}

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Gebruik een dakantenne voor je Spitz AX om een beter signaal te ontvangen. We raden de [LTMG942 multibandantenne van MobileMark](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/){target="_blank"} aan, die optimale netwerksignalen biedt. Zorg dat dakantennes van andere merken aan de volgende vereisten voldoen:

- 4 cellulaire antennes, ontvangstfrequentiebereik 600M~6GHz.
- 2 Wi-Fi-antennes, ontvangstfrequentiebereik: 2.4G~2.5GHz, 5.15~5.84GHz.

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Opmerking:** je kunt een 7-in-1-antenne gebruiken die ook een GPS-antenne bevat, maar je hoeft slechts zes antennes op de Spitz AX aan te sluiten. De DIV/GNSS-interface van de Spitz AX ondersteunt GPS-signalen, omdat de cellulaire antenne met een ontvangstfrequentie van 600M~6GHz de GPS-frequentie omvat. Spitz AX ondersteunt het bekijken van je GPS-locatie via de opdrachtregel, maar kan je locatie momenteel niet op de kaart weergeven.

Om signaalverzwakking te voorkomen, mag de radiofrequentiekabel van de dakantenne naar je Spitz AX niet langer zijn dan 5 meter. Als een radiofrequentiekabel van MobileMark bijvoorbeeld 5 meter lang is, wordt de signaalontvangst bij 3000MHz met 3dB verminderd, wat de helft van de sterkte is. Hoe hoger de signaalfrequentie, hoe groter de verzwakking.

[Lees hoe je de antennes van de Spitz AX vervangt.](how_to_install_or_change_antennas.md)

---

## 2. Internet instellen voor je Spitz AX {#2-set-up-the-internet-for-your-spitz-ax}

Stel internet via simkaarten in, zodat je onderweg internettoegang hebt.

Spitz AX heeft een ingebouwde 5G NR-module en ondersteunt twee simkaarten. Mobiele providers bieden verschillende cellulaire pakketten voor simkaarten en gebruiken verschillende APN's. Je moet de APN in de instellingen invoeren. Vraag je provider daarom welke APN je moet gebruiken.

Volg deze stappen om je simkaarten in te stellen:

1. Plaats je simkaart of simkaarten.
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Sluit de voedingsadapter aan en schakel de router in.

Volg deze stappen om je APN in te voeren:

1. Voer `192.168.8.1` in een webbrowser in en meld je aan.
2. De naam van je provider wordt linksboven weergegeven. Klik op **Manual Setup**.
3. Voer naast **APN** de APN in.
4. Klik op **Apply**.

Als je twee simkaarten gebruikt, werkt er steeds slechts één simkaart. Je kunt telkens handmatig selecteren welke simkaart je wilt gebruiken. Je kunt ook de functie [Auto Switch](../interface_guide/internet_cellular.md#setup-for-dual-sim-models) inschakelen. Als de router vaststelt dat een van de simkaarten geen goede internettoegang heeft, schakelt deze automatisch over naar de andere simkaart. Het overschakelen duurt ongeveer 1 minuut.

---

## 3. Spitz AX in verschillende situaties gebruiken {#3-use-spitz-ax-in-different-scenarios}

### Onderweg {#on-the-road}

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Onderweg kun je verbinding maken met internet via de simkaart of simkaarten die je in de vorige stap hebt ingesteld.

### Op een camping {#at-a-campground}

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Als je tijdens je reis op een camping stopt, kun je het openbare Wi-Fi-netwerk van de camping gebruiken en mobiele data besparen. [Lees hoe je verbinding maakt met een bestaand Wi-Fi-netwerk.](../interface_guide/internet_repeater.md)

Nadat je eenmaal verbinding hebt gemaakt met het Wi-Fi-netwerk, kan Spitz AX de netwerknaam en het wachtwoord onthouden. De router maakt automatisch verbinding wanneer je de volgende keer in de buurt bent.

### In gebieden zonder cellulaire dekking {#in-areas-without-cellular-coverage}

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Gebruik Starlink, een satellietinternetservice, als je naar een gebied zonder cellulaire dekking rijdt, zoals een dunbevolkt woestijngebied. Gebruik zo in gebieden met goede cellulaire dekking het 5G-signaal dat de Spitz AX ontvangt en in gebieden zonder cellulaire dekking Starlink.

Zorg bij het opstellen van de Starlink-antenne dat deze vrij zicht heeft. Obstakels aan beide zijden van de weg, zoals bomen, beïnvloeden de ontvangst. Probeer daarom uit de buurt van obstakels te parkeren.

---

## 4. Failoverprioriteiten instellen {#4-set-failover-priorities}
Spitz AX ondersteunt Multi-WAN met failover en load balancing. Je kunt op basis van je situatie failoverprioriteiten voor verschillende netwerken instellen.

| Situatie| Prioriteit |
| --------| ------- |
| Op de camping (verbonden met het Wi-Fi-netwerk via de repeater)    | <p> Geef de repeater een hogere prioriteit dan cellulair.</p> <p>Zodra je de camping verlaat, schakelt je router automatisch over naar cellulair.</p>|
| Starlink (ethernet) + cellulair | Geef cellulair een hogere prioriteit dan ethernet. <p>In gebieden met cellulaire dekking gebruikt je router het cellulaire netwerk.</p> <p>Wanneer je in een gebied zonder cellulaire dekking komt, schakelt je router automatisch via ethernet over naar Starlink.</p>|

Lees het gedeelte [Failover](../interface_guide/multi-wan.md) om failover in te stellen.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
