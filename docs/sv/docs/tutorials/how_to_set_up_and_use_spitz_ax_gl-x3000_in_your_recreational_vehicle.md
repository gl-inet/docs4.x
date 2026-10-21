# Så installerar och använder du Spitz AX (GL-X3000) i en husbil {#how-to-set-up-and-use-spitz-ax-gl-x3000-in-your-recreational-vehicle}

Den här guiden visar hur du installerar och använder Spitz AX i en husbil. Beroende på internetanslutning kan du behöva SIM-kort eller USB-kabel för internetdelning. Be operatören om APN om du använder SIM-kort. Du kan även behöva en takantenn för bättre täckning och ett [Starlink-abonnemang](https://www.starlink.com/roam){target="_blank"} för områden utan mobiltäckning.

---

## 1. Installera Spitz AX och annan utrustning {#1-install-your-spitz-ax-and-other-equipment}

### Steg 1: Välj plats för Spitz AX {#step-1-choose-a-location-for-your-spitz-ax}

Välj en central plats utan hinder för bästa täckning. Platsen måste ligga högst 1 meter från strömkällan, vilket motsvarar nätadapterkabelns längd.

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Du kan ställa Spitz AX på en plan yta eller montera den på väggen.

### (Valfritt) Steg 2: Montera Spitz AX på väggen {#optional-step-2-install-your-spitz-ax-on-the-wall}

Använd den medföljande självhäftande dynan eller väggfästena. Skruva fast fästet på väggen och tryck sedan fast Spitz AX i fästet.

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Valfritt) Steg 3: Installera husbilens takantenn {#optional-step-3-install-the-rv-roof-antenna}

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

För bättre signal rekommenderas [MobileMarks flerbandsantenn LTMG942](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/){target="_blank"}. Andra takantenner måste ha fyra mobilantenner för 600M~6GHz och två Wi-Fi-antenner för 2.4G~2.5GHz och 5.15~5.84GHz.

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Obs!** En 7-i-1-antenn med GPS kan användas, men endast sex antenner ansluts till Spitz AX. Gränssnittet DIV/GNSS stöder GPS eftersom mobilantennen på 600M~6GHz omfattar GPS-frekvensen. GPS-positionen kan visas på kommandoraden, men för närvarande inte på en karta.

RF-kabeln mellan takantennen och Spitz AX bör inte vara längre än 5 meter för att begränsa dämpningen. En 5 meter lång MobileMark-kabel minskar till exempel signalen vid 3000MHz med 3dB, alltså till halva styrkan. Dämpningen ökar med frekvensen.

[Läs om hur du byter antenner på Spitz AX.](how_to_install_or_change_antennas.md)

---

## 2. Konfigurera internet för Spitz AX {#2-set-up-the-internet-for-your-spitz-ax}

Spitz AX har en inbyggd 5G NR-modul och stöd för dubbla SIM-kort. Operatörernas abonnemang och APN skiljer sig åt, så kontrollera rätt APN med operatören.

1. Sätt i SIM-kortet eller SIM-korten.
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Anslut nätadaptern och starta routern.

Ange APN genom att öppna `192.168.8.1` i en webbläsare och logga in. Klicka på **Manual Setup** under operatörens namn, ange APN vid **APN** och klicka på **Apply**.

Om du använder två SIM-kort är bara ett aktivt åt gången. Du kan välja kort manuellt eller aktivera [Auto Switch](../interface_guide/internet_cellular.md#setup-for-dual-sim-models). Om routern upptäcker att ett kort saknar fungerande internetanslutning växlar den automatiskt till det andra. Växlingen tar cirka 1 minut.

---

## 3. Använd Spitz AX i olika situationer {#3-use-spitz-ax-in-different-scenarios}

### På vägen {#on-the-road}

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Under körning ansluter du till internet via SIM-korten som du konfigurerade ovan.

### På en campingplats {#at-a-campground}

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Använd campingplatsens offentliga Wi-Fi för att spara mobildata. [Läs om hur du ansluter till ett befintligt Wi-Fi-nätverk.](../interface_guide/internet_repeater.md) Spitz AX sparar nätverksnamn och lösenord och ansluter automatiskt nästa gång nätverket finns i närheten.

### I områden utan mobiltäckning {#in-areas-without-cellular-coverage}

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Använd Starlink i områden utan mobiltäckning. Använd Spitz AX 5G där mobiltäckningen är god och Starlink där den saknas. Starlink-antennen måste ha fri sikt; parkera om möjligt borta från hinder som träd längs vägen.

---

## 4. Ange prioritet för redundansväxling {#4-set-failover-priorities}

Spitz AX stöder Multi-WAN med redundansväxling och lastbalansering.

| Situation| Prioritet |
| --------| ------- |
| På campingplatsen (ansluten till Wi-Fi som repeater) | <p>Ge repeatern högre prioritet än mobilanslutningen.</p> <p>När du lämnar campingplatsen växlar routern automatiskt till mobilanslutningen.</p>|
| Starlink (Ethernet) + mobilanslutning | Ge mobilanslutningen högre prioritet än Ethernet. <p>Där det finns mobiltäckning används mobilnätet.</p> <p>Utan mobiltäckning växlar routern automatiskt till Starlink via Ethernet.</p>|

Se avsnittet [Redundansväxling](../interface_guide/multi-wan.md) för konfiguration.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
