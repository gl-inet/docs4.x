# Network Mode {#network-mode}

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Network Mode**.

La modalità di rete si riferisce ai diversi ruoli operativi e alle funzioni che un router può assumere per soddisfare differenti esigenze di implementazione della rete. Queste modalità sono pensate per scenari che vanno dalla copertura Wi-Fi domestica al networking multi-link di livello aziendale, con ciascuna modalità che disabilita o abilita specifiche funzioni del router per ottimizzare le prestazioni.

!!! note

    1. Quando cambi la modalità di rete del router, potrebbe essere necessario riconnettere tutti i dispositivi client.

    2. **Quando il router è in modalità Access Point / WDS / Bridge, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale.** Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalità Router predefinita.

    3. **In modalità Non-Router, le seguenti funzioni non saranno disponibili**: Access Control (Allowlist and Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Per i modelli con Wi-Fi {#for-models-with-wi-fi}

Fatta eccezione per modelli specifici, la maggior parte dei router wireless GL.iNet dispone della funzionalità Wi-Fi.

I modelli con funzionalità Wi-Fi di solito supportano quattro modalità di rete: Router, Access Point, Extender e WDS. Tieni presente che alcuni modelli non supportano la modalità WDS.

![network mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: è la modalità operativa predefinita per la maggior parte dei router domestici e per piccoli uffici, progettata per creare una rete locale privata e fungere da gateway dedicato tra Internet pubblico e i dispositivi connessi.

    In Router Mode, il dispositivo abilita funzioni fondamentali tra cui NAT, DHCP e firewall integrato. Si collega a una linea a monte, ad esempio fibra broadband, assegna automaticamente indirizzi IP privati ai dispositivi connessi e fornisce sicurezza di rete all'intera rete privata.

    ---

- **Access Point**: questa modalità consente a un router di collegarsi a una rete cablata tramite cavo LAN e trasmettere segnali wireless, ampliando la copertura Wi-Fi in spazi ampi per consentire a più dispositivi di accedere alla rete.

    In modalità Access Point, il router disabilita le funzioni NAT e DHCP e opera esclusivamente come trasmettitore di segnale wireless e switch, invece che come gateway autonomo.

    Dopo il passaggio alla modalità Access Point, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo AP e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalità Router predefinita.

    Per confrontare connettività, prestazioni e gestione, consulta [Confronto tra le modalità Mesh, Extender e Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode).

    !!! tip

        Quando distribuisci più access point, posizionamento degli AP, selezione dei canali, sovrapposizione della copertura e potenza di trasmissione possono influire su roaming e prestazioni. Consulta [Comprendere copertura Wi-Fi, access point e potenza di trasmissione](../tutorials/understanding_wifi_coverage_access_points_and_transmit_power.md) per indicazioni sulla distribuzione.

    ---

- **Extender**: questa modalità è progettata per estendere la copertura Wi-Fi di una rete wireless esistente ed eliminare le zone d'ombra del segnale nelle aree con scarsa connettività.

    In modalità Extender, il dispositivo si connette a una rete Wi-Fi esistente e inoltra il traffico per estendere la copertura senza un collegamento Ethernet al router principale. Quando la connessione a monte e i client connessi condividono la stessa radio e lo stesso canale Wi-Fi, la ricezione e la ritrasmissione del traffico consumano ulteriore tempo di trasmissione e possono ridurre la velocità effettiva.

    Per confrontare connettività, prestazioni e gestione, consulta [Confronto tra le modalità Mesh, Extender e Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode).

    In modalità Extender, potrai comunque accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale.

    ---

- **WDS**: la modalità Wireless Distribution System (WDS) è simile alla modalità Extender poiché estende la copertura Wi-Fi in modalità wireless, ma supporta il bridging wireless tra più router compatibili. È consigliata per l'espansione della rete wireless quando il router a monte dispone della funzionalità WDS.

    Questa modalità è ideale per scenari come la copertura di edifici a più piani o piccoli campus di uffici in cui più router devono collaborare per formare una rete wireless unificata. A differenza della modalità Extender, che trasmette solo i segnali da un router principale a un singolo extender, la modalità WDS consente ai router interconnessi sia di inviare sia di ricevere segnali, permettendo una copertura continua su aree più ampie con più nodi di segnale.

    Dopo il passaggio alla modalità WDS, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router WDS e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalità Router predefinita.

## Per i modelli senza Wi-Fi {#for-models-without-wi-fi}

GL-MT2500/GL-MT2500A non supporta le modalità Access Point, Extender o WDS, poiché non dispone della funzionalità Wi-Fi. Supporta però la modalità Router e la modalità Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: è la modalità operativa predefinita per la maggior parte dei router domestici e per piccoli uffici, progettata per creare una rete locale privata (LAN) e fungere da gateway dedicato tra Internet pubblico e i dispositivi connessi.

    In Router Mode, il dispositivo abilita funzioni fondamentali tra cui NAT, DHCP e firewall integrato. Si collega a una linea a monte, ad esempio fibra broadband, assegna automaticamente indirizzi IP privati ai dispositivi connessi e fornisce sicurezza di rete all'intera rete privata.

    ---

- **Bridge**: consente al router di collegarsi a una rete cablata e funzionare come bridge tra dispositivi di rete.

    In questa modalità, il router opera essenzialmente come uno switch, inoltrando dati tra i dispositivi connessi senza eseguire servizi NAT, firewall o DHCP. Questo consente una comunicazione senza interruzioni tra i dispositivi sulla stessa rete, agendo come semplice punto di connessione piuttosto che come gateway di rete.

    Dopo il passaggio alla modalità Bridge, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router Bridge e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalità Router predefinita.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
