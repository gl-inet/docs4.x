# Come configurare e usare Spitz AX (GL-X3000) nel tuo veicolo ricreazionale

Questa guida mostra come configurare e usare Spitz AX nel tuo veicolo ricreazionale. Prima di iniziare, dovrai o potresti dover preparare le seguenti attrezzature e servizi aggiuntivi:

- SIM card oppure cavo USB, per il tethering, a seconda del metodo di connessione Internet che usi. Se usi una o piu' SIM card, chiedi al tuo operatore l'APN.
- Un'antenna da tetto, se desideri una copertura migliore.
- [Un abbonamento a Starlink](https://www.starlink.com/roam), se vai in aree senza copertura cellulare.

---

## 1. Installa Spitz AX e le altre apparecchiature

Prima di iniziare il viaggio, configura Spitz AX seguendo questi passaggi.

### Passaggio 1: scegli una posizione per Spitz AX

Si consiglia di scegliere una posizione centrale e libera da ostacoli per ottenere la massima copertura. Assicurati che la posizione si trovi entro 1 metro dalla fonte di alimentazione, che corrisponde alla lunghezza del cavo dell'alimentatore.

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Puoi posizionare Spitz AX su una superficie piana oppure montarlo a parete. Se scegli il montaggio a parete, segui il passaggio successivo.

### Passaggio 2, opzionale: installa Spitz AX a parete

Esistono due modi per installare Spitz AX a parete:
- usa il pad adesivo in dotazione
- usa i supporti da parete

I supporti da parete sono inclusi nella confezione. Per montare Spitz AX a parete, segui i passaggi seguenti:

1. Fissa il supporto alla parete usando le viti.
2. Aggancia Spitz AX al supporto.

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### Passaggio 3, opzionale: installa l'antenna da tetto per RV

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Per ottenere un segnale migliore, usa un'antenna da tetto per Spitz AX. Consigliamo di usare la [antenna multi-band MobileMark LTMG942](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/), che fornisce segnali di rete ottimali. Se vuoi usare antenne da tetto di altri marchi, assicurati che soddisfino i seguenti requisiti:

- 4 antenne cellulari, intervallo di frequenza ricevuta 600M~6GHz.
- 2 antenne Wi-Fi, intervallo di frequenza ricevuta 2.4G~2.5GHz, 5.15~5.84GHz.

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Nota**: puoi usare un'antenna 7-in-1, che include anche un'antenna GPS, ma dovrai collegare solo le sei antenne di Spitz AX. L'interfaccia DIV/GNSS di Spitz AX supporta i segnali GPS perche' l'antenna cellulare, che riceve frequenze 600M~6GHz, copre anche la frequenza GPS. Spitz AX supporta la visualizzazione della posizione GPS tramite riga di comando, ma attualmente non supporta la visualizzazione della posizione sulla mappa.

Per evitare attenuazione del segnale, il cavo a radiofrequenza dall'antenna da tetto a Spitz AX non dovrebbe superare i 5 metri. Ad esempio, quando il cavo radiofrequenza MobileMark e' lungo 5 metri, la ricezione del segnale a 3000MHz si riduce di 3dB, cioe' a meta' della potenza. Maggiore e' la frequenza del segnale, maggiore sara' l'attenuazione.

[Scopri come installare o sostituire le antenne esterne per router cellulari.](how_to_install_or_change_antennas.md)

---

## 2. Configura Internet per Spitz AX

Per assicurarti l'accesso a Internet durante il viaggio, configura Internet usando le SIM card.

Spitz AX ha un modulo 5GNR integrato e supporta dual SIM. I diversi operatori mobili offrono pacchetti cellulari diversi per le SIM card e usano APN differenti. Dovrai inserire l'APN nelle impostazioni, quindi verifica con il tuo operatore quale sia l'APN corretto.

Per configurare le SIM card, segui questi passaggi:

1. Inserisci la SIM card o le SIM card.
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Collega l'alimentatore e accendi il router.

Per inserire il tuo APN, segui questi passaggi:

1. inserisci `192.168.8.1` in un browser web ed effettua l'accesso.
2. Dovresti vedere il nome del tuo operatore nell'angolo in alto a sinistra. Fai clic su **Manual Setup**.
3. Accanto a **APN**, inserisci l'APN.
4. Fai clic su **Apply**.

Se usi due SIM card, tieni presente che solo una SIM funziona alla volta. Puoi selezionare manualmente quale SIM usare ogni volta. In alternativa, abilita la [funzione Auto Switch](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models). Se il router rileva che una delle SIM non riesce ad accedere correttamente a Internet, passera' automaticamente all'altra SIM. Il passaggio richiede circa 1 minuto.

---

## 3. Usa Spitz AX in scenari diversi

### In viaggio

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Quando stai guidando, dovresti poterti collegare a Internet tramite la SIM card o le SIM card configurate nel passaggio precedente.

### In campeggio

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Se durante il viaggio ti fermi in un campeggio, puoi usare la rete Wi-Fi pubblica fornita dal sito e risparmiare i tuoi dati cellulari. [Scopri come collegarti a una rete Wi-Fi esistente.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/)

Dopo esserti collegato una volta alla rete Wi-Fi, Spitz AX puo' ricordarne nome e password. Si colleghera' automaticamente alla rete la prossima volta che sarai nelle vicinanze.

### In aree senza copertura cellulare

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Se prevedi di guidare in un'area senza copertura cellulare, ad esempio una zona desertica scarsamente popolata, usa Starlink, un servizio Internet satellitare. In questo modo, nelle aree con buona copertura cellulare userai il segnale 5G ricevuto da Spitz AX, mentre nelle aree senza copertura cellulare userai Starlink.

Quando configuri l'antenna Starlink, assicurati che non ci siano ostacoli. Gli ostacoli ai lati della strada, ad esempio alberi, influenzano la ricezione, quindi cerca di parcheggiare lontano da qualsiasi ostacolo.

---

## 4. Imposta le priorita' di failover

Spitz AX supporta multi-WAN, failover e load balancing. Puoi impostare priorita' di failover diverse per le varie reti in base al tuo scenario.

| Scenario | Priorita' |
| -------- | --------- |
| In campeggio, connesso alla rete Wi-Fi del campeggio tramite repeater | <p>Assegna al repeater una priorita' superiore rispetto alla rete cellulare.</p> <p>Non appena lascerai il campeggio, il router passera' automaticamente alla rete cellulare.</p> |
| Starlink, ethernet + rete cellulare | Assegna alla rete cellulare una priorita' superiore rispetto a ethernet. <p>Nelle aree con copertura cellulare, il router usera' la rete cellulare.</p> <p>Quando arriverai in aree senza copertura cellulare, il router passera' automaticamente a Starlink tramite ethernet.</p> |

Per configurare il failover, leggi la sezione [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
