# Het NAT-type voor games wijzigen {#how-to-change-the-nat-type-on-gaming}

Sommige gameontwikkelaars raden aan UPnP op je router in te schakelen voor een beter NAT-type. UPnP brengt echter mogelijke beveiligingsrisico’s met zich mee.

Je kunt hetzelfde bereiken door DMZ of port forwarding op je router te configureren. Zorg dat je begrijpt hoe de functie werkt en welke beveiligingsrisico’s eraan verbonden zijn voordat je een van beide inschakelt.

## Het IP-adres van je gameapparaat controleren {#check-your-game-ip}

Meld je eerst aan bij je router. Open de clientlijst en controleer het IP-adres van je gameapparaat. Gebruik dit adres in de volgende instellingen.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Methode 1: DMZ {#method-1-dmz}

Ga in de zijbalk naar **Network** -> **Port Forwarding** en schakel DMZ in met het IP-adres van je gameapparaat.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Methode 2: Port forwarding {#method-2-port-forward}

Ga in de zijbalk naar **Network** -> **Port Forwarding** en voeg de vereiste poorten met het IP-adres van je gameapparaat toe.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Voorbeeld: poorten voor PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox-poorten

UDP 88, 3074

TCP 3074

Voor sommige games moet je andere poorten doorsturen. Raadpleeg deze website voor details.

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Je kunt Full Cone NAT inschakelen om de latentie te verbeteren. Deze functie is beschikbaar sinds firmware v4.5.

Ga naar **Network** -> **NAT Settings**, schakel indien nodig **Full Cone NAT** in en klik op **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
