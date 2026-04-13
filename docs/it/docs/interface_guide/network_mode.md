# Network Mode

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Network Mode**.

La modalita' di rete si riferisce ai diversi ruoli operativi e alle funzioni che un router puo' assumere per soddisfare differenti esigenze di implementazione della rete. Queste modalita' sono pensate per scenari che vanno dalla copertura Wi-Fi domestica al networking multi-link di livello aziendale, con ciascuna modalita' che disabilita o abilita specifiche funzioni del router per ottimizzare le prestazioni.

!!! note

    1. Quando cambi la modalita' di rete del router, potrebbe essere necessario riconnettere tutti i dispositivi client.

    2. **Quando il router e' in modalita' Access Point / WDS / Bridge, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale.** Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalita' Router predefinita.

    3. **In modalita' Extender**, puoi comunque accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale.

    4. **In modalita' Non-Router, le seguenti funzioni non saranno disponibili**: Access Control (Allowlist and Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Per i modelli con Wi-Fi

Fatta eccezione per modelli specifici, la maggior parte dei router wireless GL.iNet dispone della funzionalita' Wi-Fi.

I modelli con funzionalita' Wi-Fi di solito supportano quattro modalita' di rete: Router, Access Point, Extender e WDS. Tieni presente che alcuni modelli non supportano la modalita' WDS.

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: e' la modalita' operativa predefinita per la maggior parte dei router domestici e per piccoli uffici, progettata per creare una rete locale privata e fungere da gateway dedicato tra Internet pubblico e i dispositivi connessi.

    In Router Mode, il dispositivo abilita funzioni fondamentali tra cui NAT, DHCP e firewall integrato. Si collega a una linea a monte, ad esempio fibra broadband, assegna automaticamente indirizzi IP privati ai dispositivi connessi e fornisce sicurezza di rete all'intera rete privata.

    ---

- **Access Point**: questa modalita' consente a un router di collegarsi a una rete cablata tramite cavo LAN e trasmettere segnali wireless, ampliando la copertura Wi-Fi in spazi ampi per consentire a piu' dispositivi di accedere alla rete.

    In modalita' Access Point, il router disabilita le funzioni NAT e DHCP e opera esclusivamente come trasmettitore di segnale wireless e switch, invece che come gateway autonomo.

    Dopo il passaggio alla modalita' Access Point, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo AP e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalita' Router predefinita.

    ---

- **Extender**: questa modalita' e' progettata per estendere la copertura Wi-Fi di una rete wireless esistente ed eliminare le zone d'ombra del segnale nelle aree con scarsa connettivita'.

    Consente al router di ricevere in modalita' wireless i segnali dal router principale, amplificarli e ritrasmettere il segnale potenziato. A differenza della modalita' Access Point, non richiede una connessione cablata al router principale, ma puo' portare a un dimezzamento della larghezza di banda, poiche' il dispositivo deve gestire contemporaneamente ricezione e trasmissione del segnale.

    In modalita' Extender, potrai comunque accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale.

    ---

- **WDS**: la modalita' Wireless Distribution System (WDS) e' simile alla modalita' Extender poiche' estende la copertura Wi-Fi in modalita' wireless, ma supporta il bridging wireless tra piu' router compatibili. E' consigliata per l'espansione della rete wireless quando il router a monte dispone della funzionalita' WDS.

    Questa modalita' e' ideale per scenari come la copertura di edifici a piu' piani o piccoli campus di uffici in cui piu' router devono collaborare per formare una rete wireless unificata. A differenza della modalita' Extender, che trasmette solo i segnali da un router principale a un singolo extender, la modalita' WDS consente ai router interconnessi sia di inviare sia di ricevere segnali, permettendo una copertura continua su aree piu' ampie con piu' nodi di segnale.

    Dopo il passaggio alla modalita' WDS, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router WDS e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalita' Router predefinita.

## Per i modelli senza Wi-Fi

GL-MT2500/GL-MT2500A non supporta le modalita' Access Point, Extender o WDS, poiche' non dispone della funzionalita' Wi-Fi. Supporta pero' la modalita' Router e la modalita' Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: e' la modalita' operativa predefinita per la maggior parte dei router domestici e per piccoli uffici, progettata per creare una rete locale privata (LAN) e fungere da gateway dedicato tra Internet pubblico e i dispositivi connessi.

    In Router Mode, il dispositivo abilita funzioni fondamentali tra cui NAT, DHCP e firewall integrato. Si collega a una linea a monte, ad esempio fibra broadband, assegna automaticamente indirizzi IP privati ai dispositivi connessi e fornisce sicurezza di rete all'intera rete privata.

    ---

- **Bridge**: consente al router di collegarsi a una rete cablata e funzionare come bridge tra dispositivi di rete.

    In questa modalita', il router opera essenzialmente come uno switch, inoltrando dati tra i dispositivi connessi senza eseguire servizi NAT, firewall o DHCP. Questo consente una comunicazione senza interruzioni tra i dispositivi sulla stessa rete, agendo come semplice punto di connessione piuttosto che come gateway di rete.

    Dopo il passaggio alla modalita' Bridge, non potrai accedere al pannello di amministrazione web usando l'indirizzo IP LAN originale. Dovrai invece accedere al router a monte per trovare l'indirizzo IP assegnato a questo router Bridge e poi usare tale indirizzo IP per accedere al pannello di amministrazione web. Se non hai accesso al router a monte, tieni premuto il pulsante di reset per 4 secondi per riportarlo alla modalita' Router predefinita.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
