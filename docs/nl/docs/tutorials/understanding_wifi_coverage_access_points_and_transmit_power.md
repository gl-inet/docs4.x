---
title: Inzicht in Wi-Fi-dekking, access points en zendvermogen
---

# Inzicht in Wi-Fi-dekking, access points en zendvermogen {#understanding-wi-fi-coverage-access-points-and-transmit-power}

Veel gebruikers gaan ervan uit dat een hoger zendvermogen van de router altijd voor een betere Wi-Fi-dekking en betere prestaties zorgt.

Een hoger zendvermogen vergroot doorgaans het dekkingsgebied van één router, maar het maximale zendvermogen is niet altijd ideaal in netwerken met meerdere access points (AP's), meshknooppunten of bedrijfs-Wi-Fi.

Inzicht in dekkingscellen, roaming, kanaalplanning en zendvermogen kan helpen de draadloze prestaties te verbeteren.

## Eén router en meerdere access points {#single-router-vs-multiple-access-points}

### Eén router {#single-router}

Als slechts één router voor Wi-Fi-dekking zorgt:

- Een hoger zendvermogen vergroot doorgaans de dekking.
- Clientapparaten kunnen op grotere afstand een bruikbare verbinding behouden.
- Een lager zendvermogen vermindert doorgaans het ontvangen signaal en de signaal-ruisverhouding (SNR) van de downlink.

Voor de meeste gebruikers met één router wordt aanbevolen het zendvermogen op de standaard- of automatische instelling te laten staan.

Het verlagen van het zendvermogen van je router vermindert niet de RF-energie die door naburige Wi-Fi-netwerken wordt uitgezonden. Hun routers en AP's blijven met hetzelfde vermogen uitzenden.

### Meerdere access points {#multiple-access-points}

Als meerdere AP's worden gebruikt, is het doel niet noodzakelijk om het dekkingsgebied van elk AP te maximaliseren.

Het doel is meerdere kleinere, duidelijk begrensde dekkingscellen te maken die net voldoende overlappen voor ononderbroken dekking en betrouwbare roaming.

Een goede plaatsing van AP's, een geschikt zendvermogen en de juiste kanaalselectie zijn allemaal belangrijk.

## Overlap tussen dekkingscellen {#coverage-cell-overlap}

Als elk AP met maximaal vermogen uitzendt, kunnen de dekkingsgebieden te veel overlappen.

Een clientapparaat kan verbonden blijven met een verafgelegen AP, zelfs als een dichterbij gelegen AP een sterker signaal biedt. Dit wordt vaak een **sticky client** genoemd.

Een client die met het verkeerde AP is verbonden, kan last hebben van:

- Lagere SNR
- Lagere modulatie- en coderingssnelheden
- Meer hertransmissies
- Lagere doorvoersnelheid
- Hogere latentie

Door het zendvermogen van AP's te verlagen, kun je de dekkingscellen verkleinen en clientapparaten stimuleren eerder te roamen.

## Roaming van clients begrijpen {#understanding-client-roaming}

In de meeste Wi-Fi-netwerken bepaalt het clientapparaat wanneer het roamt.

De router of het AP kan roaming ondersteunen, maar de telefoon, laptop, tablet of andere client neemt doorgaans de uiteindelijke beslissing om een AP te verlaten en met een ander AP verbinding te maken.

Verschillende clientapparaten gebruiken verschillende drempelwaarden en algoritmen voor roaming. Een apparaat kan daardoor verbonden blijven met een AP zolang het de verbinding bruikbaar vindt, zelfs als een ander AP een sterker signaal biedt.

Door overmatige overlap tussen dekkingscellen te verminderen, kunnen clients betere beslissingen over roaming nemen.

## Ruimtelijk hergebruik {#spatial-reuse}

Wi-Fi is een gedeeld medium.

Voordat Wi-Fi-apparaten uitzenden, luisteren ze of het kanaal al in gebruik is. Als AP's die hetzelfde kanaal gebruiken elkaar over een groot gebied kunnen horen, moeten ze mogelijk langer wachten tot het kanaal beschikbaar is.

Dit vermindert de bruikbare zendtijd en de totale doorvoersnelheid.

Door het zendvermogen op de juiste manier te verlagen, kunnen AP's die hetzelfde kanaal in verschillende fysieke gebieden gebruiken onafhankelijker werken. Dit wordt **ruimtelijk hergebruik** genoemd.

Ruimtelijk hergebruik betekent niet dat een lager zendvermogen van je AP de storing van naburige netwerken vermindert. Dekkingscellen met de juiste grootte kunnen wel onnodige concurrentie om het kanaal verminderen en hetzelfde kanaal opnieuw laten gebruiken in gebieden die voldoende van elkaar zijn gescheiden.

## Kanaalplanning {#channel-planning}

Houd bij de configuratie rekening met zowel het zendvermogen als de kanaalselectie.

### 2.4 GHz {#24-ghz}

De 2.4GHz-band heeft relatief weinig kanalen die elkaar niet overlappen.

In veel regelgevingsgebieden worden de kanalen 1, 6 en 11 vaak gebruikt met een kanaalbreedte van 20 MHz.

Gebruik waar mogelijk voor nabijgelegen AP's verschillende kanalen die elkaar niet overlappen.

### 5 GHz en 6 GHz {#5-ghz-and-6-ghz}

De 5GHz- en 6GHz-band bieden meer beschikbare kanalen, zodat het eenvoudiger is om verschillende kanalen aan nabijgelegen AP's toe te wijzen.

Kanalen die elkaar niet overlappen verminderen de concurrentie op hetzelfde kanaal, hoewel overmatige dekkingsoverlap nog steeds invloed kan hebben op roaming.

Welke kanalen beschikbaar zijn, hangt af van het routermodel, het land of de regio, de kanaalbreedte en de lokale regelgeving.

## Bekabelde AP's en meshnetwerken {#wired-aps-and-mesh-networks}

### Bekabelde access points {#wired-access-points}

Een bekabelde ethernetverbinding tussen de hoofdrouter en aanvullende AP's heeft doorgaans de voorkeur.

Omdat de bekabelde verbinding het backhaulverkeer draagt, kan het Wi-Fi-zendvermogen hoofdzakelijk worden afgestemd op clientdekking, roaming en ruimtelijk hergebruik.

### Mesh met bekabelde backhaul {#mesh-with-wired-backhaul}

Meshknooppunten met bekabelde backhaul kunnen op een vergelijkbare manier als bekabelde AP's worden geoptimaliseerd.

Je kunt het zendvermogen aanpassen om overmatige overlap tussen cellen te verminderen en toch ononderbroken dekking te behouden.

### Mesh met draadloze backhaul {#mesh-with-wireless-backhaul}

In een draadloos meshnetwerk kunnen de Wi-Fi-radio's ook verkeer tussen meshknooppunten vervoeren.

Als je het zendvermogen te sterk verlaagt, kan de draadloze backhaulverbinding verzwakken en kunnen de totale prestaties afnemen.

Zorg bij gebruik van draadloze backhaul dat meshknooppunten een sterke en stabiele onderlinge verbinding behouden.

## Voorbeeld van een implementatie met meerdere AP's {#example-multi-ap-deployment}

Neem als voorbeeld twee GL.iNet-routers die via ethernet met elkaar zijn verbonden:

- De primaire router verzorgt routering, DHCP, NAT en firewallservices.
- De tweede router werkt in de modus Access Point.
- Beide apparaten zenden dezelfde Wi-Fi-netwerknaam en beveiligingsinstellingen uit.
- Nabijgelegen AP's gebruiken verschillende kanalen die elkaar niet overlappen.
- Het zendvermogen is zo ingesteld dat de dekkingscellen voldoende overlappen voor roaming, maar niet overmatig.

Het ideale zendvermogen hangt af van bouwmaterialen, de plaatsing van AP's, clientapparaten, naburige Wi-Fi-netwerken en het gewenste dekkingsgebied.

Er is geen enkele waarde voor het zendvermogen die voor elke implementatie geschikt is.

## Veelvoorkomende misvattingen {#common-misconceptions}

### Het maximale zendvermogen biedt altijd de beste Wi-Fi {#maximum-transmit-power-always-provides-the-best-wi-fi}

Het maximale vermogen biedt doorgaans het grootste dekkingsgebied, maar kan in implementaties met meerdere AP's te veel overlap en slecht roaminggedrag veroorzaken.

### Een lager zendvermogen vermindert inkomende storing {#lower-transmit-power-reduces-incoming-interference}

Als je het zendvermogen van je AP verlaagt, vermindert het signaal dat je eigen AP produceert. Het vermogen dat naburige routers of AP's uitzenden, neemt niet af.

### Een lager zendvermogen maakt de ontvanger van het AP gevoeliger {#lower-transmit-power-makes-the-ap-receiver-more-sensitive}

Zendvermogen en ontvangergevoeligheid zijn afzonderlijke eigenschappen. Een lager zendvermogen verbetert niet automatisch het vermogen van het AP om transmissies van clients te ontvangen.

### Clientapparaten maken altijd verbinding met het dichtstbijzijnde AP {#client-devices-always-connect-to-the-closest-ap}

Clientapparaten selecteren AP's en roamen tussen AP's doorgaans met hun eigen interne algoritmen. Ze kunnen verbonden blijven met een verder weg gelegen AP, zelfs als een dichterbij gelegen AP beschikbaar is.

## Aanbevolen begininstellingen {#recommended-starting-points}

| Implementatie | Aanbeveling |
| --- | --- |
| Eén router | Laat het zendvermogen op de standaard- of automatische instelling staan. |
| Twee of meer bekabelde AP's | Gebruik kanalen die elkaar niet overlappen en pas het zendvermogen aan om overmatige overlap te verminderen. |
| Mesh met bekabelde backhaul | Optimaliseer de dekkingscellen voor betrouwbare roaming. |
| Mesh met draadloze backhaul | Verlaag het vermogen niet zo sterk dat de backhaulverbinding verzwakt. |

Test na wijzigingen de prestaties op verschillende locaties en controleer:

- Signaalsterkte
- Upload- en downloaddoorvoersnelheid
- Latentie
- Roaming tussen AP's
- Kwaliteit van de draadloze backhaul, indien van toepassing

Wijzig één instelling tegelijk, zodat je het effect nauwkeurig kunt meten.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com) of [neem contact met ons op](https://www.gl-inet.com/contact-us/).
