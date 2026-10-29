# UPnP {#upnp}

**Nota**: Questa funzione è stata introdotta nel firmware v4.11.

---

Nel menu a sinistra del pannello di amministrazione web, vai su **SECURITY** -> **UPnP**.

UPnP (Universal Plug and Play) consente ai dispositivi LAN e alle applicazioni compatibili di richiedere automaticamente mappature delle porte sui router GL.iNet. Queste mappature inoltrano il traffico WAN in ingresso a indirizzi IP e porte LAN specifici, consentendo ai client esterni di connettersi ai servizi locali senza regole di port forwarding configurate manualmente.

UPnP si distingue dal [port forwarding](./port_forwarding.md) e dalla [DMZ](./port_forwarding.md#dmz): UPnP crea automaticamente le mappature su richiesta dei dispositivi. Il port forwarding espone le porte selezionate, mentre la DMZ espone tutte le porte di un host LAN; entrambi richiedono una configurazione manuale. Prima di abilitare queste funzioni, assicurati di comprenderne il funzionamento e i rischi di sicurezza associati.

**Nota**: 

1. Quando UPnP è abilitato, i dispositivi LAN e le applicazioni compatibili possono richiedere mappature delle porte senza approvazione per ogni richiesta.

2. Un dispositivo compromesso o un’applicazione dannosa può usare UPnP per esporre servizi locali su Internet. Abilita UPnP solo su reti affidabili e disabilitalo quando non serve.

3. UPnP richiede un IP pubblico sull’interfaccia WAN del router per accettare connessioni in ingresso da Internet. Non funzionerà se il tuo operatore utilizza CGNAT.

Gli usi comuni di UPnP includono:

- **Giochi online**: i giochi e le console compatibili (ad esempio, giochi multigiocatore Steam, Xbox Series X|S, PlayStation 5, Nintendo Switch) possono creare automaticamente mappature delle porte per facilitare le connessioni con altri giocatori.

- **Condivisione di file peer-to-peer**: i client BitTorrent e altre applicazioni P2P compatibili possono mappare automaticamente le porte di ascolto per accettare connessioni in ingresso dai peer.

- **Accesso remoto**: i dispositivi e le applicazioni che supportano la mappatura delle porte UPnP, come alcuni dispositivi NAS, telecamere IP e server multimediali, possono configurare automaticamente le mappature per l’accesso dall’esterno della rete locale.

## Configurazione rapida {#quick-setup}

Attiva l’interruttore per abilitare UPnP. I dispositivi e le applicazioni compatibili possono quindi richiedere mappature delle porte secondo necessità, come nell’esempio seguente.

![enable upnp](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/upnp.png){class="glboxshadow"}

- **Client / Application**: descrizione del client o dell’applicazione e indirizzo IP LAN del dispositivo richiedente.

- **Protocol**: protocollo di trasporto della mappatura, ad esempio `TCP` o `UDP`.

- **External Port**: porta WAN per le connessioni in ingresso.

- **Internal Target**: indirizzo IP LAN e porta di destinazione.

- **Lease**: tempo rimanente prima della scadenza della mappatura. La durata predefinita del lease è di 7 giorni.

- **Action**: fai clic sull’icona del cestino per eliminare la mappatura. Il client o l’applicazione può richiederla di nuovo se è ancora in esecuzione.

Le mappature delle porte attive vengono rimosse quando il client le rilascia o quando scadono i lease. Fai clic su **Refresh** per visualizzare le mappature delle porte più recenti.

![refresh port mappings](https://static.gl-inet.com/docs/router/en/4/interface_guide/upnp/refresh_upnp_information.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
