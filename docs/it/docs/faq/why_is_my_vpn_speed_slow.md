# Perché la velocità della mia VPN è più lenta del previsto?

Se hai notato che la velocità della connessione VPN è inferiore alla velocità massima teorica (testata in una rete locale ideale), in realtà è normale nell'uso reale.

Le VPN sono progettate per dare priorità a sicurezza e privacy, e questo influisce inevitabilmente sulla velocità. In condizioni di rete tipiche, è normale che la velocità VPN si collochi tra il 30% e il 50% della velocità massima pubblicizzata. Questa differenza è dovuta a molteplici fattori che influenzano le prestazioni; di seguito li spieghiamo insieme ad alcuni suggerimenti per ottimizzare l'esperienza.

**Nota**: i metodi seguenti possono aiutare a migliorare la velocità VPN, ma non possono garantire il raggiungimento della velocità pubblicizzata, poiché le prestazioni reali dipendono da molteplici fattori.

## Velocità della CPU del router

La VPN crittografa i dati per proteggere la privacy, aggiungendo elaborazione extra. Questa cifratura e decifratura può rallentare la connessione. Scegli un router con una CPU più veloce per migliorare la velocità VPN.

Abbiamo elencato le velocità di test VPN per tutti i modelli nella nostra [pagina prodotto](https://www.gl-inet.com/products/). Tieni presente però che:

* I test vengono eseguiti su una rete locale. Le velocità reali possono variare in base alla configurazione della rete.
* Le velocità OpenVPN e WireGuard saranno inferiori quando il router viene usato come server. I risultati sopra riportati si riferiscono alla modalità client.

## Distanza del server

Se il server VPN è lontano dalla tua posizione fisica, i dati devono percorrere una distanza maggiore, con conseguente aumento della latenza e riduzione della velocità.

Puoi vedere l'esempio qui sotto, che mostra le velocità client quando ci si collega a server in posizioni diverse nello stesso momento della giornata.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Carico del server

Se molti utenti sono collegati allo stesso server VPN, il server può congestionarsi e rallentare la velocità per tutti.

## Velocità di upload del server

Se stai usando un tunnel VPN privato, la velocità di upload dell'Internet Service Provider (ISP) lato server sarà il collo di bottiglia per la velocità di download lato client, poiché il client VPN scarica i dati attraverso il server.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Differenze tra protocolli

Protocolli VPN diversi come OpenVPN o WireGuard differiscono per sicurezza e velocità. Alcuni possono essere più lenti a causa dei loro metodi di cifratura.

## Limitazione da parte dell'ISP

Alcuni Internet Service Provider (ISP) possono limitare la velocità per gli utenti che usano VPN, soprattutto se sospettano un uso intenso dei dati. Questo è particolarmente comune in alcuni paesi in via di sviluppo o in piccole città dove molti utenti condividono un'infrastruttura Internet limitata.

## DNS

Alcuni Internet Service Provider (ISP) potrebbero non riuscire a risolvere i domini VPN. Prova a usare [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) nelle impostazioni Network del router.

## MTU

Alcuni Internet Service Provider (ISP), specialmente gli operatori mobili, possono limitare la dimensione dei pacchetti dati. Prova a cambiare l'MTU predefinito da 1420 a 1380 o 1280 nelle VPN Client Options.

Per firmware v4.8 e successivi, fai riferimento [qui](../interface_guide/vpn_dashboard_v4.8.md/#tunnel-options).

Per firmware v4.7 e precedenti, fai riferimento [qui](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
