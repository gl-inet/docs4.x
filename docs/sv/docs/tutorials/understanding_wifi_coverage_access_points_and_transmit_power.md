---
title: Förstå Wi-Fi-täckning, åtkomstpunkter och sändningseffekt
---

# Förstå Wi-Fi-täckning, åtkomstpunkter och sändningseffekt {#understanding-wi-fi-coverage-access-points-and-transmit-power}

Många antar att högre sändningseffekt alltid förbättrar Wi-Fi-täckning och prestanda. Det ökar vanligtvis räckvidden för en ensam router, men maximal effekt är inte alltid bäst i nätverk med flera åtkomstpunkter, meshnoder eller företags-Wi-Fi.

## En router jämfört med flera åtkomstpunkter {#single-router-vs-multiple-access-points}

### En router {#single-router}

Med en enda router ger högre effekt normalt större täckning och låter klienter behålla en användbar anslutning längre bort. Lägre effekt minskar normalt mottagen signal och SNR för nedlänken. För de flesta rekommenderas standardläget eller automatisk effekt.

Lägre effekt på din router minskar inte radioenergin från närliggande Wi-Fi-nätverk.

### Flera åtkomstpunkter {#multiple-access-points}

Med flera åtkomstpunkter är målet flera mindre, tydliga täckningsceller som överlappar precis tillräckligt för obruten täckning och tillförlitlig roaming. Placering, effekt och kanalval är alla viktiga.

## Överlappning mellan täckningsceller {#coverage-cell-overlap}

Om alla åtkomstpunkter sänder med maximal effekt kan cellerna överlappa för mycket. En klient kan stanna kvar på en avlägsen åtkomstpunkt trots en starkare närliggande signal, en så kallad **sticky client**. Det kan ge lägre SNR, lägre modulations- och kodningshastighet, fler omsändningar, lägre kapacitet och högre latens.

Lägre effekt kan krympa cellerna och få klienterna att roama tidigare.

## Förstå klientroaming {#understanding-client-roaming}

Klienten bestämmer normalt när den ska roama. Routern kan hjälpa till, men telefonen, datorn eller surfplattan fattar slutbeslutet. Olika enheter har olika trösklar och algoritmer och kan stanna på en åtkomstpunkt så länge anslutningen anses användbar. Mindre överlappning kan underlätta bättre beslut.

## Rumslig återanvändning {#spatial-reuse}

Wi-Fi är ett delat medium. Enheter lyssnar innan de sänder. Om åtkomstpunkter på samma kanal hör varandra över ett stort område väntar de längre på ledig kanal, vilket minskar tillgänglig sändningstid och kapacitet.

Rätt reducerad effekt kan låta åtkomstpunkter på samma kanal i skilda områden arbeta mer oberoende. Detta kallas **rumslig återanvändning**. Det minskar inte störningar som grannnät sänder, men rätt dimensionerade celler minskar onödig konkurrens.

## Kanalplanering {#channel-planning}

Effekt och kanalval bör planeras tillsammans.

### 2.4 GHz {#24-ghz}

2.4 GHz-bandet har få kanaler som inte överlappar. I många regioner används kanal 1, 6 och 11 med 20 MHz kanalbredd. Närliggande åtkomstpunkter bör om möjligt använda olika, icke överlappande kanaler.

### 5 GHz och 6 GHz {#5-ghz-and-6-ghz}

5 GHz- och 6 GHz-banden har fler kanaler, vilket underlättar olika kanalval. Tillgängliga kanaler beror på routermodell, land eller region, kanalbredd och lokala regler.

## Kabelanslutna åtkomstpunkter och meshnät {#wired-aps-and-mesh-networks}

### Kabelanslutna åtkomstpunkter {#wired-access-points}

Ethernet mellan huvudrouter och extra åtkomstpunkter är vanligtvis bäst. Då kan Wi-Fi-effekten anpassas efter klienttäckning, roaming och rumslig återanvändning.

### Mesh med kabelansluten backhaul {#mesh-with-wired-backhaul}

Meshnoder med kabelansluten backhaul kan optimeras på samma sätt genom att minska onödig överlappning och behålla obruten täckning.

### Mesh med trådlös backhaul {#mesh-with-wireless-backhaul}

I trådlösa meshnät bär radion även trafik mellan noder. För kraftig effektreduktion kan försvaga backhaul-anslutningen. Se till att noderna har en stark och stabil anslutning till varandra.

## Exempel med flera åtkomstpunkter {#example-multi-ap-deployment}

Två Ethernet-anslutna GL.iNet-routrar kan konfigureras så att huvudroutern hanterar routning, DHCP, NAT och brandvägg, medan den andra kör åtkomstpunktsläge. Båda sänder samma nätverksnamn med samma säkerhetsinställningar, använder olika icke överlappande kanaler och har precis tillräckligt överlappande celler.

Rätt effekt beror på byggmaterial, placering, klienter, grannnät och önskat täckningsområde. Det finns inget värde som passar alla installationer.

## Vanliga missuppfattningar {#common-misconceptions}

### Maximal effekt ger alltid bäst Wi-Fi {#maximum-transmit-power-always-provides-the-best-wi-fi}

Maximal effekt ger störst räckvidd men kan orsaka för stor överlappning och dålig roaming med flera åtkomstpunkter.

### Lägre effekt minskar inkommande störningar {#lower-transmit-power-reduces-incoming-interference}

Den minskar endast signalen från din egen åtkomstpunkt, inte effekten från grannroutrar.

### Lägre effekt gör mottagaren känsligare {#lower-transmit-power-makes-the-ap-receiver-more-sensitive}

Sändningseffekt och mottagarkänslighet är separata egenskaper. Lägre effekt förbättrar inte i sig mottagningen från klienter.

### Klienter ansluter alltid till närmaste åtkomstpunkt {#client-devices-always-connect-to-the-closest-ap}

Klienter väljer och växlar åtkomstpunkt med egna algoritmer och kan stanna på en mer avlägsen punkt.

## Rekommenderade utgångslägen {#recommended-starting-points}

| Installation | Rekommendation |
| --- | --- |
| En router | Behåll standardläget eller automatisk sändningseffekt. |
| Två eller fler kabelanslutna åtkomstpunkter | Använd icke överlappande kanaler och minska överdriven täckningsöverlappning. |
| Mesh med kabelansluten backhaul | Optimera cellerna för tillförlitlig roaming. |
| Mesh med trådlös backhaul | Sänk inte effekten så mycket att backhaul-anslutningen försvagas. |

Testa efter ändringar signalstyrka, uppladdnings- och nedladdningskapacitet, latens, roaming och eventuell trådlös backhaul på flera platser. Ändra en inställning i taget så att effekten kan mätas.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com) eller [kontakta oss](https://www.gl-inet.com/contact-us/).
