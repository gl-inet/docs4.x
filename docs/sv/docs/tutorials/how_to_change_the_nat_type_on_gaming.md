# Ändra NAT-typ för spel {#how-to-change-the-nat-type-on-gaming}

Vissa spelutvecklare rekommenderar att du aktiverar UPnP på routern för att få en bättre NAT-typ. UPnP medför dock potentiella säkerhetsrisker.

Du kan konfigurera DMZ eller portvidarebefordran på routern för att uppnå samma resultat. Innan du aktiverar någon av funktionerna bör du förstå hur den fungerar och vilka säkerhetsrisker den medför.

## Kontrollera spelenhetens IP-adress {#check-your-game-ip}

Logga först in på routern. Öppna klientlistan och kontrollera vilken IP-adress som har tilldelats spelenheten. Du behöver använda IP-adressen i följande konfiguration.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metod 1: DMZ {#method-1-dmz}

Gå till **Network** -> **Port Forwarding** i sidofältet och aktivera DMZ med spelenhetens IP-adress.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metod 2: Portvidarebefordran {#method-2-port-forward}

Gå till **Network** -> **Port Forwarding** i sidofältet och lägg till de portar som behövs med spelenhetens IP-adress.

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

Du kan aktivera Full Cone NAT för att minska latensen. Funktionen har varit tillgänglig sedan firmware v4.5.

Gå till **Network** -> **NAT Settings**, aktivera **Full Cone NAT** vid behov och klicka på **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
