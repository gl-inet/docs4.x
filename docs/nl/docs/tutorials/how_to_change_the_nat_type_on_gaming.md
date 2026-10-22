# Het NAT-type voor games wijzigen {#how-to-change-the-nat-type-on-gaming}

Veel gamefabrikanten adviseren UPnP op de router in te schakelen voor een beter NAT-type, maar UPnP is geen veilig protocol.

Je kunt hetzelfde veiliger bereiken met DMZ of port forwarding.

## Het IP-adres van je gameapparaat controleren {#check-your-game-ip}

Open de clientlijst en controleer het IP-adres van je gameapparaat. Gebruik dit adres in de volgende instellingen.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Method 1 DMZ {#method-1-dmz}

Ga in de zijbalk naar **Network > Port Forwarding** en schakel DMZ in met het IP-adres van je gameapparaat.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Method 2 Port forward {#method-2-port-forward}

Ga in de zijbalk naar **Network > Port Forwarding** en voeg de vereiste poorten met het IP-adres van je gameapparaat toe.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Example: Ports for PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Xbox port

UDP 88, 3074

TCP 3074

Voor sommige games moet je andere poorten doorsturen. Raadpleeg deze website voor details.

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Je kunt Full Cone NAT onder **Network > NAT Settings** inschakelen om de latentie te verbeteren.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* This function is available on Firmware 4.5 or above.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
