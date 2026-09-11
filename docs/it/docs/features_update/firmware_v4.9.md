# Firmware v4.9

Questa versione si concentra su un controllo della rete più preciso, una gestione del traffico migliorata, una sicurezza di rete rafforzata e un’interfaccia utente rinnovata, con l’obiettivo di offrire una migliore esperienza complessiva.

Scarica il firmware più recente dal [Centro download firmware](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control è un modulo centrale di gestione della rete che consente l’identificazione, il monitoraggio, la regolazione e il filtraggio precisi del traffico di rete. Ottimizza l’allocazione delle risorse di rete, elimina la congestione della larghezza di banda e standardizza i comportamenti di accesso alla rete, offrendo un’esperienza più fluida, sicura e controllabile. Nel firmware v4.9, questo modulo si integra con più funzioni pratiche per una gestione completa del traffico.

Il modulo Flow Control include DPI Engine, Data Statistics, Content Filter, QoS, SQM e Parental Control.

### DPI Engine

A differenza dei router tradizionali, che identificano soltanto gli indirizzi di origine e destinazione, DPI (Deep Packet Inspection) analizza in modo approfondito il contenuto dei pacchetti e identifica con precisione applicazioni e siti web tramite una libreria di corrispondenza delle caratteristiche, consentendo di classificare e controllare il traffico in modo granulare.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics offre un dashboard intuitivo del traffico che identifica l’utilizzo della rete per applicazione e protocollo. Consente di visualizzare le tendenze storiche di 1 ora, 1 giorno e 7 giorni, mostra le classifiche di utilizzo, monitora il traffico per dispositivo e permette di bloccare con un clic le app indesiderate.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter è una funzione intelligente di sicurezza online basata sulla classificazione DPI. Blocca automaticamente i siti web dannosi e malevoli per mantenere la rete sicura e supporta anche regole personalizzate per bloccare app, domini o indirizzi IP specifici.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS (Quality of Service) ottimizza l’allocazione della larghezza di banda dando priorità alle attività essenziali, ad esempio videochiamate e giochi, durante la congestione della rete. In questo modo riduce la latenza e migliora le prestazioni complessive della rete.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) gestisce in modo intelligente il traffico di rete del router per ridurre al minimo la latenza e il «bufferbloat», garantendo giochi e chiamate vocali più fluidi.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

In precedenza classificata nel menu **Applications**, questa funzione viene spostata nel menu **Flow Control** nel firmware v4.9. Sfrutta il DPI Engine aggiornato per identificare e bloccare con precisione applicazioni e contenuti di rete inappropriati, offrendo restrizioni di accesso basate sul traffico più professionali e precise.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

Il firmware v4.9 migliora in modo completo la logica di instradamento sottostante e l’interfaccia interattiva del modulo VPN. Corregge potenziali conflitti di instradamento, semplifica la logica di configurazione e rende l’uso più intuitivo.

Gli adeguamenti principali sono i seguenti.

### Tunnel VPN isolato

Ogni tunnel VPN opera come un gruppo indipendente senza failover tra gruppi. Quando il traffico di rete corrisponde a uno specifico gruppo VPN, non passa automaticamente ad altri gruppi VPN anche se il tunnel corrente non funziona, garantendo un instradamento del traffico stabile e prevedibile.

**Nota**: la policy tradizionale «Not Use VPN» è stata rimossa nel firmware v4.9, eliminando configurazioni ridondanti per evitare conflitti di instradamento causati da regole di tunnel multiple e complesse.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Failover dei profili VPN

Un singolo gruppo di tunnel VPN può contenere più profili di configurazione. Gli utenti possono personalizzare la priorità di ciascun profilo nello stesso gruppo, abilitando il failover interno automatico per mantenere la connettività VPN quando un singolo profilo non funziona.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Dashboard ridisegnata

La VPN Dashboard è stata completamente ridisegnata con un layout più intuitivo. Lo stato dei tunnel, i dettagli della connessione e le voci di configurazione sono presentati con maggiore chiarezza, migliorando notevolmente le attività quotidiane di gestione e amministrazione. Inoltre, nella nuova architettura, Kill Switch è abilitato per impostazione predefinita per tutti i tunnel VPN, in modo da proteggere sempre il traffico.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

Il firmware v4.9 introduce ufficialmente il protocollo AmneziaWG 2.0, dotato di più nuovi parametri di offuscamento del traffico. Il protocollo aggiornato evita efficacemente il rilevamento da parte di DPI e altri sistemi di identificazione del traffico, migliorando in modo significativo la riservatezza della connessione e la resistenza alle interferenze. Ciò consente di stabilire connessioni VPN stabili e affidabili in regioni con restrizioni di rete e in ambienti di rete complessi.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## Rete IoT

Nel firmware v4.9 puoi creare una rete Wi-Fi dedicata e indipendente per i dispositivi smart IoT. Essendo isolata fisicamente e logicamente dalla rete principale, evita l’occupazione delle risorse di rete e i rischi di sicurezza derivanti dall’accesso dei dispositivi IoT alla rete principale. Questa ottimizzazione offre una compatibilità più ampia con vari client IoT smart e migliora complessivamente il sistema di sicurezza della rete domestica.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL, abbreviazione di Access Control List, è una funzione centrale di gestione della sicurezza di rete che consente agli utenti di creare regole di accesso personalizzate per gestire il traffico interno ed esterno in base a protocolli di connessione, indirizzi IP dei dispositivi e porte. Supporta un controllo preciso delle autorizzazioni per consentire o bloccare specifici comportamenti di accesso alla rete. Quando più regole ACL generano conflitti, il sistema esegue automaticamente la regola con priorità più alta per garantire l’applicazione corretta della policy.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL si distingue da Port Forwarding per il ruolo principale: ACL si concentra sulla gestione della sicurezza di rete controllando le autorizzazioni di accesso di dispositivi e traffico, mentre Port Forwarding viene usato per il reindirizzamento delle risorse di rete, inoltrando il traffico esterno a dispositivi locali specifici per implementare l’accesso remoto ai servizi della rete locale.

## Interfaccia Wireless

L’interfaccia Wireless è stata completamente ridisegnata con un layout semplificato e uno stile visivo uniforme, riducendo la complessità operativa e migliorando notevolmente la semplicità e l’usabilità generale dell’interfaccia.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## DNS cifrato

Il DNS cifrato è stato ampliato per supportare più protocolli di cifratura, inclusi DoH, DoT e DoQ. Inoltre, sono stati integrati altri provider DNS ufficiali ed è stata aggiunta la configurazione manuale di server DNS cifrati personalizzati per soddisfare diverse esigenze di risoluzione sicura dei domini.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

I router GL.iNet ora supportano il funzionamento come Tailscale Exit Node. Tutto il traffico Internet in uscita dai dispositivi nel Tailnet può essere instradato tramite l’indirizzo IP pubblico del router, realizzando una gestione dell’uscita di rete unificata e sicura per l’intera rete Tailscale. Consulta [questa pagina](../interface_guide/tailscale.md#run-exit-node) per maggiori dettagli.

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
