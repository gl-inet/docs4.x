# Firmware v4.9

Questa versione si concentra su un controllo della rete più preciso, una gestione del traffico migliorata, una sicurezza di rete rafforzata e un’interfaccia utente rinnovata, con l’obiettivo di offrire una migliore esperienza complessiva. [Centro download firmware](https://dl.gl-inet.com/){target="_blank"}

## Flow Control

Flow Control è un modulo centrale di gestione della rete che consente l’identificazione, il monitoraggio, la regolazione e il filtraggio precisi del traffico di rete. Ottimizza l’allocazione delle risorse di rete, elimina la congestione della larghezza di banda e standardizza i comportamenti di accesso alla rete, offrendo un’esperienza più fluida, sicura e controllabile. Nel firmware v4.9, questo modulo si integra con più funzioni pratiche per una gestione completa del traffico.

Il modulo Flow Control include le seguenti funzioni:

!!! note "DPI Engine"
    
    Tecnologia Deep Packet Inspection per identificare con precisione protocolli applicativi, tipi di traffico e comportamenti di rete.

!!! note "Statistiche dati"
    
    Raccolta, analisi e visualizzazione dei dati di traffico di rete in tempo reale e storici per un monitoraggio intuitivo dello stato della rete.

!!! note "Filtro contenuti"
    
    Intercettazione e filtraggio intelligenti dei contenuti di rete inappropriati per standardizzare l’accesso alla rete.

!!! note "QoS (Quality of Service)"
    
    Allocazione della larghezza di banda e pianificazione delle priorità del traffico per garantire la qualità della rete alle applicazioni principali.

!!! note "SQM (Smart Queue Management)"
    
    Ottimizza la pianificazione delle code di rete per ridurre latenza e perdita di pacchetti, rendendo più fluida la trasmissione di rete.

!!! note "Controllo genitori"
    
    In precedenza classificata nel menu **Applications**, questa funzione viene migrata nel menu **Flow Control** in v4.9. Sfrutta il DPI Engine aggiornato per identificare e bloccare con precisione applicazioni e contenuti di rete inappropriati, ottenendo restrizioni di accesso basate sul traffico più professionali e precise.

## VPN

Il firmware v4.9 migliora in modo completo la logica di instradamento sottostante e l’interfaccia interattiva del modulo VPN. Corregge potenziali conflitti di instradamento, semplifica la logica di configurazione e rende l’uso più intuitivo.
    
Gli adeguamenti principali sono i seguenti:

!!! note "Raggruppamento VPN indipendente"

    Ogni tunnel VPN opera come un gruppo indipendente senza failover tra gruppi. Quando il traffico di rete corrisponde a uno specifico gruppo VPN, non passa automaticamente ad altri gruppi VPN anche se il tunnel corrente non funziona, garantendo un instradamento del traffico stabile e prevedibile.

!!! note "Failover dei profili nel gruppo"
    
    Un singolo gruppo di tunnel VPN può contenere più profili di configurazione. Gli utenti possono personalizzare la priorità di ciascun profilo nello stesso gruppo, abilitando il failover interno automatico per mantenere la connettività VPN quando un singolo profilo non funziona.
    
!!! note "Rimozione della policy \"Not Use VPN\""
    
    L’opzione tradizionale "Not Use VPN" per la configurazione delle policy VPN viene rimossa in v4.9. In questo modo si eliminano voci di configurazione ridondanti e si evitano efficacemente conflitti complessi nella logica di instradamento causati da più impostazioni di policy.
    
!!! note "VPN Dashboard ridisegnata"
        
    La VPN Dashboard è stata completamente ridisegnata con un layout più intuitivo. Mostra in modo più chiaro lo stato dei tunnel, le informazioni di connessione e le voci di configurazione, migliorando notevolmente le attività quotidiane di gestione e amministrazione.

## Protocollo AmneziaWG 2.0

Il firmware v4.9 introduce ufficialmente il protocollo AmneziaWG 2.0, dotato di più nuovi parametri di offuscamento del traffico. Il protocollo aggiornato evita efficacemente il rilevamento da parte di DPI e altri sistemi di identificazione del traffico, migliorando in modo significativo la riservatezza della connessione e la resistenza alle interferenze. Ciò consente di stabilire connessioni VPN stabili e affidabili in regioni con restrizioni di rete e in ambienti di rete complessi.

## Rete IoT

La nuova funzione di rete IoT supporta la creazione di una rete Wi-Fi dedicata e indipendente per dispositivi smart IoT. Essendo isolata fisicamente e logicamente dalla rete principale, evita l’occupazione delle risorse di rete e i rischi di sicurezza derivanti dall’accesso dei dispositivi IoT alla rete principale. Questa ottimizzazione offre una compatibilità più ampia con vari client IoT smart e migliora complessivamente il sistema di sicurezza della rete domestica.

## ACL (Access Control List)

ACL, abbreviazione di Access Control List, è una funzione centrale di gestione della sicurezza di rete che consente agli utenti di creare regole di accesso personalizzate per gestire il traffico interno ed esterno in base a protocolli di connessione, indirizzi IP dei dispositivi e porte. Supporta un controllo preciso delle autorizzazioni per consentire o bloccare specifici comportamenti di accesso alla rete. Quando più regole ACL generano conflitti, il sistema esegue automaticamente la regola con priorità più alta per garantire l’applicazione corretta della policy.

ACL si distingue da Port Forwarding per il ruolo principale: ACL si concentra sulla gestione della sicurezza di rete controllando le autorizzazioni di accesso di dispositivi e traffico, mentre Port Forwarding viene usato per il reindirizzamento delle risorse di rete, inoltrando il traffico esterno a dispositivi locali specifici per implementare l’accesso remoto ai servizi della rete locale.

## Altri miglioramenti

!!! note "Ridisegno dell’interfaccia Wireless"
    
    L’interfaccia delle impostazioni Wireless è stata completamente ridisegnata con un layout semplificato e uno stile visivo uniforme, riducendo la complessità operativa e migliorando notevolmente la semplicità e l’usabilità generale dell’interfaccia.

!!! note "DNS cifrato aggiornato"
    
    Il DNS cifrato viene ampliato per supportare più protocolli di cifratura, inclusi DoH, DoT e DoQ. Inoltre, vengono integrati altri provider DNS ufficiali e viene aggiunta la configurazione manuale di server DNS cifrati personalizzati per soddisfare esigenze diverse di risoluzione sicura dei domini.
    
!!! note "Supporto Tailscale Exit Node"
    
    I router GL.iNet ora supportano il funzionamento come Tailscale Exit Node. Tutto il traffico Internet in uscita dai dispositivi nel Tailnet può essere instradato tramite l’indirizzo IP pubblico del router, realizzando una gestione dell’uscita di rete unificata e sicura per l’intera rete Tailscale.
    
!!! note "Integrazione AstroWarp"
    
    AstroWarp è ufficialmente integrato nel GL.iNet Router SDK in v4.9. Basato sul protocollo AmneziaWG con capacità nativa di offuscamento del traffico, offre accesso remoto stabile, cifrato e sicuro. Gli utenti possono completare rapidamente l’abbinamento del dispositivo e la configurazione della connessione tramite un codice di accesso dinamico nel pannello di amministrazione web. Supporta una connessione sicura con un clic tra router da viaggio e reti domestiche in pochi secondi, senza registrazione dell’account o accesso.
