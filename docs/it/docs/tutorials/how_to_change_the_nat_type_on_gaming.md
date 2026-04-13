# Come cambiare il tipo di NAT per il gaming

La maggior parte dei produttori di videogiochi chiede di abilitare UPnP sul router per ottenere un tipo di NAT migliore; tuttavia, gli studi mostrano che UPnP non e' un protocollo sicuro.

Puoi ottenere lo stesso risultato in modo piu' sicuro, usando la funzione DMZ oppure il port forwarding.

## Controlla l'IP del tuo dispositivo di gioco

Vai all'elenco client e controlla l'IP assegnato al tuo dispositivo di gioco. Ti servira' questo indirizzo IP nella configurazione seguente.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metodo 1: DMZ

Vai nella barra laterale su **Network > Port Forwarding** e abilita la DMZ usando l'IP del tuo dispositivo di gioco.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metodo 2: Port forward

Vai nella barra laterale su **Network > Port Forwarding** e aggiungi le porte necessarie usando l'IP del tuo dispositivo di gioco.

![inputport](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Esempio: porte per PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480

![ps5port](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Porte Xbox

UDP 88, 3074

TCP 3074

Alcuni giochi potrebbero richiedere l'inoltro di altre porte; puoi fare riferimento a questo sito per maggiori dettagli.

[Port forward on different Games](https://portforward.com/games/)

## Full Cone NAT

Puoi abilitare **Full Cone NAT** in **Network > NAT Settings** per migliorare la latenza.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

* Questa funzione e' disponibile con firmware 4.5 o superiore.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
