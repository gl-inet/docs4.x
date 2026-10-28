# Come cambiare il tipo di NAT per il gaming {#how-to-change-the-nat-type-on-gaming}

Alcuni sviluppatori di giochi consigliano di abilitare UPnP sul router per ottenere un tipo di NAT migliore. Tuttavia, UPnP comporta potenziali rischi per la sicurezza.

Puoi configurare DMZ o port forwarding sul router per ottenere lo stesso risultato. Prima di abilitare una di queste funzioni, assicurati di comprenderne il funzionamento e i rischi per la sicurezza associati.

## Controlla l'IP del tuo dispositivo di gioco {#check-your-game-ip}

Per prima cosa, accedi al router. Vai all'elenco client e controlla l'IP assegnato al tuo dispositivo di gioco. Ti servirà questo indirizzo IP nella configurazione seguente.

![gameip](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Metodo 1: DMZ {#method-1-dmz}

Vai nella barra laterale su **Network** -> **Port Forwarding** e abilita la DMZ usando l'IP del tuo dispositivo di gioco.

![dmz](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Metodo 2: Port forward {#method-2-port-forward}

Vai nella barra laterale su **Network** -> **Port Forwarding** e aggiungi le porte necessarie usando l'IP del tuo dispositivo di gioco.

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

## Full Cone NAT {#full-cone-nat}

Puoi abilitare Full Cone NAT per migliorare la latenza. Questa funzione è disponibile dal firmware v4.5.

Vai su **Network** -> **NAT Settings**, abilita **Full Cone NAT** se necessario, quindi fai clic su **Apply**.

![conenat](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
