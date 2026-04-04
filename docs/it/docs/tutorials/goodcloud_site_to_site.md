# GoodCloud Site to Site

## Introduzione

GoodCloud Site to Site consente a uffici in sedi diverse di stabilire connessioni sicure tra loro tramite Internet. Estende la rete aziendale, rendendo disponibili ai dipendenti di altre sedi le risorse informatiche di una posizione attraverso la rete.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenario 1**: decine di filiali della stessa azienda devono essere integrate in una rete privata unificata, consentendo la condivisione fluida delle risorse tra tutte le sedi.

**Scenario 2**: quando due aziende con una stretta collaborazione necessitano di lavorare insieme, Site to Site facilita il lavoro in un ambiente di rete condiviso e sicuro.

**Scenario 3**: per le famiglie con telecamere IP, Site to Site consente l'accesso remoto ai dispositivi quando i membri della famiglia sono fuori casa, garantendo un monitoraggio semplice da qualsiasi luogo.

## Condizioni

1. Sono necessari almeno due router GL.iNet per costruire una rete Site to Site.

2. Almeno un router deve avere un indirizzo IP pubblico per poter essere impostato come nodo principale. [Verifica se il tuo ISP ti assegna un indirizzo IP pubblico](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    E' preferibile usare come nodo principale un router con buone prestazioni e la migliore velocita' di rete.

3. **NON** e' consigliato eseguire Site to Site mentre i nodi secondari eseguono anche VPN client / Tailscale / ZeroTier / AstroWarp, poiche' questo puo' rendere la configurazione di rete particolarmente complessa.

## Creare una rete Site to Site

1. Collega i router al tuo account GoodCloud. [Come](../interface_guide/cloud.md/#setup-your-goodcloud-account)?

2. Accedi a [GoodCloud](https://www.goodcloud.xyz/#/login), vai su **Site to Site** nella barra laterale sinistra. Fai clic su **Create Network** in alto a destra.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Seleziona la casella a sinistra per scegliere almeno due dispositivi.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    I dispositivi selezionati verranno mostrati nella parte inferiore della pagina.

    La porta predefinita di Site to Site e' **51830**. Se vuoi usare un'altra porta, fai clic su **Advanced** nell'angolo in basso a sinistra per modificarla. Poi fai clic su **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Una rete Site to Site puo' avere fino a 10 dispositivi per garantire prestazioni stabili.

4. Assegna un nome alla rete e fai clic su **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Node Usability Testing iniziera' a verificare se uno dei dispositivi puo' essere impostato come Main Node.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Se nessuno dei tuoi dispositivi puo' essere usato come Main Node, assicurati che:

    - almeno un router abbia un IP pubblico, statico o dinamico;
    - la porta sia aperta. La porta predefinita per Site to Site e' 51830. Puoi anche cambiarla e riprovare;
    - se il router che vuoi impostare come Main Node e' dietro NAT, potresti dover configurare il port forwarding.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Se piu' di un dispositivo puo' essere impostato come Main Node, scegline uno per continuare. Suggeriamo di selezionare come Main Node il router con buone prestazioni e la migliore velocita' di rete.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Se solo un dispositivo puo' essere impostato come Main Node, verrai indirizzato direttamente alla pagina dei dettagli di Site to Site.

6. La rete e' disabilitata per impostazione predefinita. Assicurati che gli indirizzi IP LAN di tutti i nodi non entrino in conflitto tra loro. Fai clic sull'icona a ingranaggio per cambiare l'IP LAN se necessario, poi fai clic su **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Attendi alcuni minuti. Quando la linea tratteggiata diventa continua, significa che la rete Site to Site e' stata creata correttamente.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Testare la connessione Site to Site

1. Collega il PC o lo smartphone a uno dei nodi di questa rete Site to Site.

2. Avvia un browser web per accedere all'IP LAN di un altro nodo. Se riesci ad accedere alla pagina di login, la connessione tra questi due nodi funziona.

## Route e altre opzioni

Per impostazione predefinita, ogni nodo puo' accedere alla LAN degli altri nodi. Per motivi di sicurezza, consigliamo di aprire solo gli indirizzi IP di servizi specifici.

Ad esempio, nella subnet del Nodo 1 c'e' un Server A, 172.30.97.100. Se vuoi che gli altri nodi possano accedere solo al Service A del Nodo 1, puoi configurarlo come segue:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Puoi anche aggiungere le route parent del nodo.

Ogni Sub Node costruisce una rete tunnel crittografata verso il Main Node. Se vuoi cambiare l'IP della subnet del tunnel, fai clic su **IP Address Range** per modificarlo.

L'applicazione della modifica dell'intervallo IP provochera' una disconnessione della rete per alcuni minuti.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
