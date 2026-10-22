# Ändra NAT-typ för spel {#how-to-change-the-nat-type-on-gaming}

De flesta speltillverkare rekommenderar att du aktiverar UPnP på routern för att få en bättre NAT-typ, men studier visar att UPnP är ett osäkert protokoll.

Du kan uppnå samma resultat på ett säkrare sätt med DMZ eller portvidarebefordran.

## Kontrollera spelenhetens IP-adress {#check-your-game-ip}

Öppna klientlistan och kontrollera vilken IP-adress som har tilldelats spelenheten. Du behöver använda IP-adressen i följande konfiguration.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metod 1: DMZ {#method-1-dmz}

Gå till **Network > Port Forwarding** i sidofältet och aktivera DMZ med spelenhetens IP-adress.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metod 2: Portvidarebefordran {#method-2-port-forward}

Gå till **Network > Port Forwarding** i sidofältet och lägg till de portar som behövs med spelenhetens IP-adress.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Exempel: Portar för PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox-portar

UDP 88, 3074

TCP 3074

Vissa spel kan kräva vidarebefordran av andra portar. Mer information finns på följande webbplats.

[Portvidarebefordran för olika spel](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Du kan aktivera Full Cone NAT under **Network > NAT Settings** för att minska latensen.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* Funktionen är tillgänglig i firmware 4.5 och senare.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
