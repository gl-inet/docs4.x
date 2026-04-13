# Connettersi a Internet tramite rete cellulare, firmware v4.7 e precedenti

**Nota**: questa guida si basa sul firmware v4.7 e precedenti. Per le versioni piu' recenti, fai riferimento [qui](internet_cellular.md).

---

La maggior parte dei router GL.iNet supporta la connettivita' cellulare. Questa guida copre tre tipi di modelli:

1. **Modelli 4G single-SIM integrati**

    Alcuni modelli includono un modulo 4G integrato con uno slot SIM singolo, come GL-XE300 (Puli). Fai riferimento a [Setup for Single-SIM models](#setup-for-single-sim-models).

2. **Modelli compatibili con modem USB**

    Alcuni modelli dispongono di una porta USB e supportano la connettivita' cellulare tramite modem USB, come GL-AXT1800 (Slate AX). I passaggi di configurazione sono simili a quelli dei modelli 4G single-SIM integrati. Fai riferimento a [Setup for Single-SIM models](#setup-for-single-sim-models).

3. **Modelli 5G dual-SIM integrati**

    Alcuni modelli includono un modulo 5G integrato con due slot SIM, come GL-X3000 (Spitz AX). Le impostazioni cellulari nel pannello di amministrazione web possono differire leggermente. Fai riferimento a [Setup for Dual-SIM models](#setup-for-dual-sim-models).

**Nota:** alcune SIM richiedono l'attivazione prima del primo utilizzo. Per garantire la compatibilita', attiva la SIM in uno smartphone prima di inserirla nel router.

## Configurazione per modelli single-SIM

I passaggi seguenti si applicano ai modelli con modem cellulare integrato e uno slot SIM singolo, ad esempio GL-XE300 Puli, oppure con una porta USB per collegare un modem USB esterno, ad esempio GL-AXT1800 Slate AX.

Qui usiamo **GL-AXT1800 (Slate AX)** con un modem USB esterno come esempio.

Ti consigliamo di spegnere prima il router. Inserisci una SIM gia' attivata nel modem USB, quindi collega il modem alla porta USB del router. Dopodiche', accendi il router.

Se colleghi il modem USB dopo l'avvio del router, il pannello di amministrazione web potrebbe non aggiornarsi automaticamente. In tal caso, aggiorna la pagina o riavvia il router.

### Configurazione automatica

Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

1. Quando accedi per la prima volta, potrebbe non connettersi automaticamente, ma dovrebbe mostrare il nome dell'operatore nell'angolo superiore sinistro e l'IMEI. Fai clic su **Auto Setup**.

    Ignora l'avviso *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Iniziera' la connessione.

    **Nota:** alcune SIM possono avere restrizioni d'uso particolari, ad esempio la richiesta di un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni speciali.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Una volta connesso, la pagina mostrera' i dettagli della rete con un punto verde, a indicare una connessione riuscita.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Nota:** dopo la configurazione iniziale, se riavvii il router con il modem USB collegato o lo ricolleghi, il modem USB verra' riconosciuto automaticamente e la connessione di rete verra' stabilita senza dover fare di nuovo clic sul pulsante Auto Setup.

Se Auto Setup non riesce, prova [Manual Setup](#manual-setup).

### Configurazione manuale

Nella sezione Cellular, fai clic su **Manual Setup** per visualizzare o modificare le impostazioni cellulari della SIM attuale.

**Nota**: alcune SIM possono richiedere un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni. Se necessario, configura l'APN corretto sul router.

L'applicazione delle modifiche attivera' una nuova connessione.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: il protocollo di comunicazione cellulare, ad esempio 3G, QMI o QCM. Di solito viene rilevato automaticamente, ma puoi modificarlo in base al modem e ai requisiti del tuo operatore.

- **Port**: la porta seriale usata per comunicare con il modem cellulare. Di solito viene rilevata automaticamente e non richiede regolazioni manuali.

- **APN**: APN, Access Point Name, e' un parametro gateway necessario per una connessione di rete cellulare. Consente al router di connettersi a Internet tramite il tuo operatore mobile. Puoi usare l'APN predefinito oppure impostarne uno personalizzato fornito dal tuo operatore.

- **PIN**: se la SIM e' protetta da un codice PIN, inseriscilo qui. Questo campo e' facoltativo se non e' impostato alcun PIN.

- **TTL**: TTL, Time To Live, definisce il tempo massimo durante il quale i pacchetti possono sopravvivere nella rete. Per impostazione predefinita, il router decrementa di 1 il TTL dei pacchetti in ingresso dai dispositivi client prima di inoltrarli. Se hai bisogno di sovrascriverlo, puoi impostare qui un valore fisso. L'impostazione TTL e' valida solo per IPv4.

- **Service**: seleziona il tipo di servizio cellulare per definire le tecnologie di rete che il modem usera'.

- **Dial Number**: inserisci il numero di composizione fornito dal tuo operatore. Spesso e' preconfigurato e, nella maggior parte delle reti moderne, puo' essere lasciato vuoto.

- **Authentication**: scegli il metodo di autenticazione richiesto dal tuo operatore, ad esempio NONE, PAP o CHAP. Di solito e' impostato su NONE se non sono necessarie credenziali.

### Modem compatibili

Ecco un elenco dei modem supportati che sono stati testati in precedenza.

| Model                                  | 3G/4G | Tested | Tested by       | Comments* |
| -------------------------------------- | ----- | ------ | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Yes    | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Yes    | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Yes    | akw2312         |           |
| Quectel UC20-E                         | 3G    | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G    | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G    | Yes    | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G    | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Yes    | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Yes    | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Yes    | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Yes    | anonymous       | Host-less |

- **QMI**: questo modem supporta la modalita' QMI. Seleziona QMI come protocollo e **/dev/cdc-wdm0** come porta seriale per il tuo router cellulare.

- **Host-less**: questo modem supporta la modalita' Tethering. Gestisci la connessione tramite l'interfaccia Tethering del router anziche' tramite l'interfaccia Cellular.

## Configurazione per modelli dual-SIM

I passaggi seguenti si applicano ai modelli con modem cellulare integrato che supporta due SIM. Il pannello di amministrazione web puo' differire leggermente rispetto ai modelli single-SIM.

Qui usiamo **GL-X3000 (Spitz AX)** come esempio. Supporta Dual SIM, Single Standby, cioe' puo' contenere due SIM per l'accesso cellulare, ma solo una SIM puo' essere attiva alla volta. Puoi passare manualmente da una SIM all'altra.

Ti consigliamo di spegnere prima il router, inserire le SIM gia' attivate negli slot e poi riaccenderlo. Se inserisci la SIM dopo l'avvio del router, il pannello di amministrazione web potrebbe non aggiornarsi automaticamente. In tal caso, aggiorna la pagina o riavvia il router.

### Configurazione automatica

Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

1. Quando non e' inserita alcuna SIM, la pagina viene visualizzata come segue.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Quando e' inserita una SIM, il router iniziera' a connettersi automaticamente.

    Se la connessione riesce, la pagina verra' visualizzata come segue.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Se non si connette automaticamente, fai clic su **Auto Setup** e attendi che il router si connetta, oppure prova **Manual Setup**.

### Configurazione manuale

Nella sezione Cellular, fai clic su **Manual Setup** per accedere a Cellular Settings.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Puoi visualizzare o modificare le impostazioni cellulari della SIM attuale. Inoltre, vengono memorizzati alcuni profili preconfigurati e puoi aggiungere manualmente configurazioni in "Saved Settings".

### Impostazioni dello slot SIM

Nella sezione Cellular, fai clic su **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Accederai a **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Se sono inserite due SIM, puoi abilitare **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **Auto Switch**: abilita il passaggio automatico tra SIM 1 e SIM 2. Il metodo di rilevamento della rete per SIM Auto Switch e' lo stesso configurato nella pagina Multi-WAN.

- **Preferred SIM Card Slot**: imposta la SIM preferita su SIM 1 oppure SIM 2.

- **Failover Interval**: i valori disponibili vanno da 5 minuti a 24 ore.

    Se la connessione Internet non e' ancora disponibile dopo un failover, il dispositivo tornera' allo slot SIM preferito e attendera' questo intervallo prima di riprovare il failover.

    Questa opzione si applica quando sia la SIM preferita sia la SIM di backup non hanno segnale. Il dispositivo passera' tra le SIM finche' una di esse non ottiene un segnale valido.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Quando e' abilitata, il dispositivo controllera' quotidianamente lo slot SIM preferito all'ora configurata e tentera' di tornare a esso se la SIM preferita riacquista l'accesso a Internet.

    Questo evita che la SIM di backup consumi una quantita' eccessiva di dati. Se la SIM preferita continua a non avere segnale, il dispositivo continuera' a usare la SIM di backup.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Nota**: la funzione Auto Switch non passa immediatamente a un'altra SIM. Prima, il dispositivo ha bisogno di tempo per confermare che la SIM corrente non puo' accedere a Internet. Inoltre, l'altra SIM non e' in modalita' standby e richiede tempo per attivarsi.

## Statistiche del traffico

Nella sezione Cellular, fai clic su **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Entrerai nella pagina Traffic Statistics.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Fai riferimento al [tutorial SMS](sms.md).

## SMS Forwarding

Fai riferimento al [tutorial SMS Forwarding](../tutorials/sms_forwarding.md).

## Gestione modem

Nella sezione Cellular, fai clic sul pulsante **Tool** nell'angolo superiore destro per accedere alla pagina Modem Management.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Include due sezioni: **Modem Info** e **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

I comandi AT sono istruzioni standard usate per comunicare con il modem cellulare.

Quando Shortcut e' impostato su **Manual command**, digita il comando desiderato nel campo AT Command per controllare lo stato del modem.

Puoi anche fare clic sul menu a discesa Shortcut per selezionare da un elenco di **preset commands**.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Sono disponibili i seguenti comandi preimpostati:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

Come esempio, qui e' selezionata la scorciatoia "Request IMEI". Fai clic su "Send" e otterrai il risultato mostrato di seguito.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Carrier profile

Puoi salvare profili diversi per lo stesso operatore oppure per operatori diversi.

Nella sezione Cellular, fai clic sul pulsante **Profile** nell'angolo superiore destro per gestire i profili.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Aggiungi un nuovo profilo oppure salva il profilo corrente.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Crea il tuo profilo in base ai requisiti del tuo operatore.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

La prossima volta potrai selezionare un profilo salvato.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Scegli qualsiasi profilo necessario.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Lock Tower

Questa funzione e' disponibile solo su GL-X3000, GL-XE3000 e GL-X2000, firmware v4.7 o successivo.

Se vuoi ricevere un segnale di alta qualita' e garantire una connessione cellulare stabile, puoi provare il lock tower.

**Nota:** la torre bloccata deve corrispondere alle bande di frequenza supportate dal tuo operatore e dal dispositivo; in caso contrario, la connessione potrebbe non riuscire.

Nella sezione Cellular, fai clic sull'icona **Tower** nell'angolo superiore destro.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Verranno mostrate le torri disponibili.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Fai clic su una torre per visualizzarne i dettagli e bloccarla.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

Lo stato della torre, ad esempio Locked o Unlocked, verra' visualizzato nella parte superiore.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Nota**:

1. Il dispositivo potrebbe non riuscire a scansionare tutte le torri quando l'interfaccia Cellular e' abilitata.

2. Se la torre bloccata non corrisponde ai parametri di band masking o APN delle impostazioni cellulari, il router non potra' connettersi alla rete cellulare.

3. Dopo aver bloccato una torre cellulare, se sposti il router in un'altra posizione, il router continuera' a tentare di riconnettersi alla torre bloccata dopo il riavvio. Questo potrebbe impedire al router di connettersi automaticamente alla rete cellulare nella nuova posizione. In tal caso, devi sbloccare la torre cellulare corrente oppure bloccarla manualmente su una nuova torre.

## Historical Signal Record

Nella sezione Cellular, fai clic sull'icona **Signal** nell'angolo superiore destro per controllare la cronologia dell'intensita' del segnale.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Questo ti aiuta a determinare la qualita' della connessione cellulare. Se il segnale e' debole, prova a cambiare torre per ottenerne uno migliore.

Puoi visualizzare la cronologia dell'intensita' del segnale cellulare selezionando diversi intervalli di tempo.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking

Nella sezione Cellular, fai clic su **View More** e seleziona **Cells Info** per controllare i dettagli delle celle.

Vedrai le bande attualmente in uso e il relativo stato del segnale.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Se il segnale e' debole, puoi abilitare Band Masking per bloccare alcune bande. In alternativa, se il segnale e' buono, puoi consentire al router di usare solo specifiche bande cellulari.

Fai clic su **Manual Setup** per accedere alla pagina Cellular Settings, quindi abilita **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Seleziona **Masking Mode**, Block o Open, quindi seleziona LTE Bands, 5G NSA Bands e 5G SA Bands.

## Risoluzione dei problemi

Se non riesci a stabilire una connessione cellulare, fai clic sul messaggio di errore sotto per visualizzare le relative soluzioni.

??? note "No SIM / Your SIM card has not been detected"

    1. Aggiorna la pagina e attendi qualche minuto per controllare se la SIM puo' essere rilevata.

    2. Assicurati che la SIM sia installata correttamente. Allinea il taglio della SIM con il segno corrispondente sullo slot per confermare il corretto orientamento di inserimento.

    3. Spegni il router, rimuovi e reinserisci la SIM, quindi riaccendi il router.

    4. Prova a usare un'altra SIM, se disponibile.

    Se il problema persiste, scarica i log e inviali a [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Aggiorna la pagina e attendi qualche minuto per verificare se l'errore scompare.

    2. Fai clic su **Disconnect**/**Abort**, quindi su **Connect** per tentare una nuova connessione.

    3. Riavvia il router.

    4. Verifica lo stato della SIM e assicurati che sia attivata. Prova la SIM inserendola in uno smartphone per confermare che possa accedere normalmente a Internet con un piano dati mobile attivo oppure contatta il tuo operatore di rete per la verifica.

    5. Alcuni operatori di rete possono richiedere il protocollo 3G per la connessione. Vai su **Manual Setup** -> **Cellular Settings** -> **Protocol**, seleziona **3G**, quindi fai clic su **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Il dispositivo si ricolleghera' automaticamente. Attendi qualche minuto per controllare se la connessione e' riuscita.

    6. Alcune SIM possono avere restrizioni d'uso particolari, ad esempio la richiesta di un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni.

        Se necessario, vai su **Manual Setup** -> **Cellular Settings** -> **APN**, configura l'APN corretto sul router, quindi fai clic su **Apply**.

    7. Fai clic su **View More** e seleziona **Cells Info** per controllare l'intensita' del segnale cellulare. Se il segnale e' debole, assicurati che l'antenna sia installata correttamente. Sposta il router in una posizione aperta e senza ostacoli per migliorare la ricezione del segnale.

    8. Controlla se **Band Masking** o **Lock Tower** sono abilitati. In tal caso, disabilita la funzione e prova a riconnetterti.

    Se il problema persiste, scarica i log e inviali a [support@gl-inet.com](mailto:support@gl-inet.com).

## Certificazione IoT

### Certificazione AT&T

Fai clic sul link [att device certification](https://iotdevices.att.com/certified-devices.aspx#) e inserisci il nome del dispositivo per trovarlo.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Certificazione T-Mobile

Fai clic sul link [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) e scegli 5G in **Filter** per trovarlo.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}

---

Articoli correlati

- [Pagina Internet](internet.md)
- [Come impostare la priorita' di ciascun metodo di accesso a Internet?](multi-wan.md)
- [Come impostare il bilanciamento del carico quando vengono usati contemporaneamente piu' metodi di accesso a Internet?](multi-wan.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
