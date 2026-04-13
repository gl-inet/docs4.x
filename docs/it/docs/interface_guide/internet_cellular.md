# Connettersi a Internet tramite rete cellulare

**Nota**: questa guida si basa sul firmware v4.8. Per le versioni precedenti, fai riferimento [qui](internet_cellular_v4.7.md).

---

La maggior parte dei router GL.iNet supporta la connettivita' cellulare. Questa guida copre tre tipi di modelli:

1. **Modelli 4G single-SIM integrati**

    Alcuni modelli includono un modulo 4G integrato con uno slot SIM singolo, come GL-E750 (Mudi). Fai riferimento a [Setup for Single-SIM models](#setup-for-single-sim-models).

2. **Modelli 5G dual-SIM integrati**

    Alcuni modelli includono un modulo 5G integrato con slot dual SIM, come GL-X3000 (Spitz AX). Le impostazioni cellulari nel pannello di amministrazione web possono differire leggermente. Fai riferimento a [Setup for Dual-SIM models](#setup-for-dual-sim-models).

3. **Modelli compatibili con modem USB**

    Alcuni modelli non hanno uno slot SIM integrato, ma dispongono di una porta USB e supportano la connettivita' cellulare tramite modem USB, come GL-MT3000 (Beryl AX). Fai riferimento a [Setup for USB modem](#setup-for-usb-modem).

**Nota:** alcune SIM richiedono l'attivazione prima del primo utilizzo. Per garantire la compatibilita', attiva la SIM in uno smartphone prima di inserirla nel router.

## Configurazione per modelli single-SIM

I passaggi seguenti si applicano ai modelli con modem cellulare integrato e uno slot SIM singolo.

Qui usiamo **GL-E750 (Mudi)** come esempio.

Ti consigliamo di spegnere prima il router, inserire una SIM gia' attivata nello slot e poi accenderlo. Se inserisci la SIM dopo l'avvio del router, il pannello di amministrazione web potrebbe non aggiornarsi automaticamente. In tal caso, aggiorna la pagina o riavvia il router.

### Configurazione automatica

Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

1. Quando non e' inserita alcuna SIM, la pagina mostra il messaggio "Your SIM card has not been detected".

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Inserisci una SIM. Il dispositivo iniziera' a connettersi come mostrato di seguito.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Se non si connette automaticamente, fai clic sul pulsante **Connect** se disponibile.

    Se la SIM non viene rilevata, prova a riavviare il router per verificare se puo' essere rilevata.

3. Una volta connessa la rete cellulare, la pagina mostrera' i dettagli di rete con un punto verde, a indicare una connessione riuscita.

    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Se la configurazione automatica non riesce, prova [Manual Setup](#manual-setup-single-sim).

### Configurazione manuale {#manual-setup-single-sim}

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**, quindi fai clic su **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Puoi visualizzare o modificare le impostazioni cellulari della SIM attuale.

**Nota**: alcune SIM possono richiedere un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni. Se necessario, configura l'APN corretto sul router.

L'applicazione delle modifiche attivera' una nuova connessione.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN, Access Point Name, e' un parametro gateway necessario per una connessione di rete cellulare. Consente al router di connettersi a Internet tramite il tuo operatore mobile. Puoi usare l'APN predefinito oppure impostarne uno personalizzato fornito dal tuo operatore.

- **Protocol**: il protocollo di comunicazione cellulare, ad esempio 3G, QMI o QCM. Di solito viene rilevato automaticamente e puoi modificarlo in base al modem e ai requisiti del tuo operatore.

- **Port**: la porta seriale usata per comunicare con il modem cellulare. Di solito viene rilevata automaticamente e non richiede regolazioni manuali.

- **TTL**: TTL, Time To Live, definisce il tempo massimo durante il quale i pacchetti possono sopravvivere nella rete. Per impostazione predefinita, il router decrementa di 1 il TTL dei pacchetti in ingresso dai dispositivi client prima di inoltrarli. Se hai bisogno di sovrascriverlo, puoi impostare qui un valore fisso. L'impostazione TTL e' valida solo per IPv4.

- **HL**: in IPv6, HL, Hop Limit, limita il numero di hop di trasmissione dei pacchetti nella rete e corrisponde al TTL in IPv4.

- **MTU**: il valore MTU predefinito e' 1500 byte.

- **Authentication**: scegli il metodo di autenticazione richiesto dal tuo operatore, ad esempio NONE, PAP o CHAP. Di solito e' impostato su NONE se non sono necessarie credenziali.

- **Band Masking**: puoi abilitare Band Masking se vuoi che il router blocchi alcune bande oppure usi solo specifiche bande cellulari. Fai clic [qui](#band-masking) per i dettagli.

## Configurazione per modelli dual-SIM

I passaggi seguenti si applicano ai modelli con modem cellulare integrato che supporta due SIM. Le pagine possono differire leggermente rispetto ai modelli single-SIM.

Qui usiamo **GL-X3000 (Spitz AX)** come esempio. Supporta Dual SIM, Single Standby, cioe' puo' contenere due SIM per l'accesso cellulare, ma solo una SIM puo' essere attiva alla volta. Puoi passare manualmente da una SIM all'altra.

Ti consigliamo di spegnere prima il router, inserire le SIM gia' attivate negli slot e poi accenderlo. Se inserisci la SIM dopo l'avvio del router, il pannello di amministrazione web potrebbe non aggiornarsi automaticamente. In tal caso, aggiorna la pagina o riavvia il router.

### Configurazione automatica

Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

1. Quando non e' inserita alcuna SIM, la pagina mostra il messaggio "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Quando e' inserita una SIM, la pagina verra' mostrata come segue. Fai clic su **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Se la SIM non viene rilevata, prova a riavviare il router per verificare se puo' essere rilevata.

3. Una volta connessa la rete cellulare, la pagina mostrera' i dettagli di rete con un punto verde, a indicare una connessione riuscita.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Fai clic su **View More Information** per mostrare piu' informazioni sulla rete cellulare, inclusi dettagli del modem, dettagli della SIM, dettagli Internet e segnale cellulare.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Se la configurazione automatica non riesce, prova [Manual Setup](#manual-setup-dual-sim).

### Configurazione manuale {#manual-setup-dual-sim}

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**, quindi fai clic su **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Puoi visualizzare o modificare le impostazioni cellulari della SIM attuale.

**Nota**: alcune SIM possono richiedere un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni. Se necessario, configura l'APN corretto sul router.

L'applicazione delle modifiche attivera' una nuova connessione.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN, Access Point Name, e' un parametro gateway necessario per una connessione di rete cellulare. Consente al router di connettersi a Internet tramite il tuo operatore mobile. Puoi usare l'APN predefinito oppure impostarne uno personalizzato fornito dal tuo operatore.

- **Protocol**: il protocollo di comunicazione cellulare rilevato automaticamente, ad esempio QMI o QCM, in base al modem e all'operatore.

- **Port**: la porta seriale rilevata automaticamente per la comunicazione con il modem cellulare.

- **TTL**: TTL, Time To Live, definisce il tempo massimo durante il quale i pacchetti possono sopravvivere nella rete. Per impostazione predefinita, il router decrementa di 1 il TTL dei pacchetti in ingresso dai dispositivi client prima di inoltrarli. Se hai bisogno di sovrascriverlo, puoi impostare qui un valore fisso. L'impostazione TTL e' valida solo per IPv4.

- **HL**: in IPv6, HL, Hop Limit, limita il numero di hop di trasmissione dei pacchetti nella rete e corrisponde al TTL in IPv4.

- **MTU**: il valore MTU predefinito e' 1500 byte.

- **Authentication**: scegli il metodo di autenticazione richiesto dal tuo operatore, ad esempio NONE, PAP o CHAP. Di solito e' impostato su NONE se non sono necessarie credenziali.

- **Band Masking**: puoi abilitare Band Masking se vuoi che il router blocchi alcune bande oppure usi solo specifiche bande cellulari. Fai clic [qui](#band-masking) per i dettagli.

### Impostazioni dello slot SIM

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**, quindi fai clic su **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Verranno mostrati il pulsante di commutazione automatica, la SIM attiva, l'ICCID e il Network Operator.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Se sono inserite due SIM, puoi abilitare **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

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

**Nota**: la funzione Auto Switch non passa immediatamente a un'altra SIM. Prima, il dispositivo ha bisogno di tempo per confermare che la SIM attuale non puo' accedere a Internet. Secondo, l'altra SIM non e' in modalita' standby e richiede tempo per attivarsi.

## Configurazione per modem USB

I passaggi seguenti si applicano ai modelli senza slot SIM integrato, ma con una porta USB per collegare un modem USB esterno.

Qui usiamo **GL-MT3000 (Beryl AX)** con il modem USB esterno **SIMPoYo uFi** come esempio.

Ti consigliamo di spegnere prima il router, inserire una SIM gia' attivata nel modem USB, collegare il modem alla porta USB del router e poi accendere il router. Se colleghi il modem USB dopo l'avvio del router, il pannello di amministrazione web potrebbe non aggiornarsi automaticamente. In tal caso, aggiorna la pagina o riavvia il router.

### Configurazione rapida

1. Spegni prima il router. Inserisci una SIM nel modem USB, collega il modem alla porta USB del router e poi accendi il router.

2. Accedi al pannello di amministrazione web del router, vai su **INTERNET** -> **Tethering**, quindi fai clic su **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Se hai bisogno di impostazioni avanzate, ad esempio TTL, HL e MTU, fai clic su **Advanced** per personalizzarle, quindi fai clic su **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    Iniziera' la connessione.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Una volta connesso, la pagina mostrera' i dettagli di rete con un punto verde, a indicare una connessione riuscita.

    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Nota:** dopo la configurazione iniziale, se riavvii il router con il modem USB collegato oppure ricolleghi il modem, esso verra' riconosciuto automaticamente e la connessione di rete verra' stabilita senza dover fare nuovamente clic sul pulsante Connect.

### Modem compatibili

Ecco un elenco dei modem supportati che sono stati testati in precedenza.

**SIMPoYo uFi** e' un dongle USB plug-and-play compatto con hotspot Wi-Fi, progettato per una connettivita' rapida e affidabile ovunque. Funziona perfettamente con la maggior parte dei router GL.iNet, cosi' come con laptop, power bank, porte USB per auto e altre fonti di alimentazione USB. Include 10 GB di dati gratuiti per 30 giorni, validi nel Regno Unito e in 34 paesi europei.

| Model                                  | Cellular | Tested | Tested by       | Comments* |
| -------------------------------------- | -------- | ------ | --------------- | --------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)                        | 5G    | Yes    | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/)               | 4G    | Yes    | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | Yes    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | Yes    | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | Yes    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | Yes    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | Yes    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | Yes    | akw2312         |           |
| Quectel RM520N-GL                      | 5G       | Yes    | akw2312         |           |
| Quectel UC20-E                         | 3G       | Yes    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G       | Yes    | GL.iNet         |           |
| Huawei E1550                           | 3G       | Yes    | GL.iNet         |           |
| Huawei E3276                           | 4G       | Yes    | GL.iNet         |           |
| Huawei E3372                           | 4G       | Yes    | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G       | Yes    | anonymous       | Host-less |
| TP-Link MA260                          | 3G       | Yes    | GL.iNet         |           |
| ZTE M823                               | 4G       | Yes    | Arnas Risqianto |           |
| ZTE MF190                              | 3G       | Yes    | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G       | Yes    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G       | Yes    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G       | Yes    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G       | Yes    | anonymous       | Host-less |

- **QMI**: questo modem supporta la modalita' QMI. Seleziona QMI come protocollo di comunicazione cellulare e **/dev/cdc-wdm0** come porta seriale nelle impostazioni della SIM.

- **Host-less**: questo modem supporta la modalita' Tethering. Gestisci la connessione tramite l'interfaccia Tethering del router anziche' tramite l'interfaccia Cellular.

## Statistiche del traffico

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**, quindi fai clic su **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Accederai alla pagina Traffic Statistics. Mostra i dati usati dalle SIM e fornisce impostazioni per il limite dati.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Se Data Used supera Data Cap Amount, modifica manualmente **Data Cap Amount** oppure **Data Used**. In caso contrario, la rete potrebbe essere disconnessa oppure la SIM potrebbe effettuare l'**Auto Switch**, per i modelli dual-SIM.

- **Modificare Data Used**

    Fai clic su **Modify** sul lato destro di SIM 1/2 Data Used.

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Poi puoi modificare o reimpostare i dati usati.

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Impostare il limite dati della SIM**

    Se vuoi impostare il limite dati della SIM, abilita prima **Save data when power off**. Questo significa che i dati possono essere salvati anche dopo lo spegnimento del dispositivo.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Poi abilita le impostazioni di limite per SIM 1 oppure SIM 2.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Per i modelli dual-SIM, suggeriamo di abilitare contemporaneamente **SIM Card Slot Auto Switch**. Se il limite dati di SIM 1 e' impostato e SIM Card Slot Auto Switch e' abilitato, SIM 1 passera' automaticamente a SIM 2 quando i dati superano Data Cap Amount e SIM 1 verra' disabilitata.

## Historical Signal Record

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**, quindi fai clic su **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Qui puoi controllare la qualita' della connessione cellulare. Se il segnale e' debole, prova a cambiare torre per ottenerne uno migliore.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Visualizza la cronologia della potenza del segnale selezionando diversi intervalli di tempo nell'angolo superiore destro.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Band Masking

Band Masking consente di bloccare bande specifiche oppure di usare solo le bande cellulari preferite per migliorare un segnale cellulare debole.

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular** -> **SIM Card Settings**, quindi abilita **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Seleziona **Masking Mode**, Block o Open, quindi seleziona LTE Bands, 5G NSA Bands e 5G SA Bands.

## SMS

Fai riferimento al [tutorial SMS](sms.md).

## SMS Forwarding

Fai riferimento al [tutorial SMS Forwarding](../tutorials/sms_forwarding.md).

## Lock Tower

!!! note "Modelli supportati"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) supporta questa funzione con firmware ver.4.7 o successivo.

Se vuoi ricevere un segnale di alta qualita' e garantire una connessione cellulare stabile, puoi provare il lock tower.

**Nota:** la torre bloccata deve corrispondere alle bande di frequenza supportate dal tuo operatore e dal dispositivo; in caso contrario, la connessione potrebbe non riuscire.

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**. Fai clic sull'icona con i tre puntini nell'angolo superiore destro, quindi seleziona **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Fai clic su **Scan** per avviare la scansione delle torri del segnale cellulare. L'operazione richiedera' alcuni minuti. Non aggiornare la pagina durante la scansione.

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

Verranno mostrate le torri disponibili.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Fai clic su una torre per visualizzarne i dettagli e bloccarla.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Nota**:

1. Il dispositivo potrebbe non riuscire a scansionare tutte le torri quando l'interfaccia Cellular e' abilitata.

2. Se la torre bloccata non corrisponde ai parametri di band masking o APN nelle impostazioni cellulari, il router non potra' connettersi alla rete cellulare.

3. Dopo aver bloccato una torre cellulare, se sposti il router in un'altra posizione, continuera' comunque a tentare la riconnessione alla torre bloccata dopo il riavvio. Questo potrebbe impedire al router di connettersi automaticamente alla rete cellulare nella nuova posizione. In tal caso, devi sbloccare la torre attuale oppure bloccarla manualmente su una nuova torre.

## Lock Operator

Questa funzione e' disponibile solo su GL-X3000, GL-XE3000 e GL-X2000, firmware ver.4.8 o successivo.

Bloccando un operatore mobile specifico, il router usera' solo la rete di quell'operatore, garantendo una connessione stabile ed evitando costi di roaming indesiderati, soprattutto nelle aree di confine dove il dispositivo potrebbe altrimenti connettersi a reti straniere.

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**. Fai clic sull'icona con i tre puntini nell'angolo superiore destro, quindi seleziona **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Esistono tre modalita' di blocco:

- **Auto**: connessione automatica a una rete operatore disponibile.
- **Manual**: blocco manuale su un operatore specifico.
- **Manual-Auto**: passaggio automatico a una rete operatore disponibile se il blocco manuale fallisce.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Modem AT Command

I comandi AT del modem sono istruzioni standard usate per comunicare con il modem cellulare. Con questa funzione puoi inviare comandi e controllare lo stato del modem.

Nel pannello di amministrazione web del router, vai su **INTERNET** -> **Cellular**. Fai clic sull'icona con i tre puntini nell'angolo superiore destro, quindi seleziona **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Accederai alla pagina AT Command.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Quando Shortcut e' impostato su **Manual command**, puoi digitare il comando desiderato nel campo AT Command.

Puoi anche fare clic sul menu a discesa Shortcut per selezionare da un elenco di **preset commands**.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Sono disponibili i seguenti comandi preimpostati:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

Come esempio, qui e' selezionata la scorciatoia "Request IMEI". Fai clic su "Send" e otterrai il risultato mostrato di seguito.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

Nell'angolo inferiore destro, puoi fare clic su **Export Debug Info** per scaricare un file .json.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Risoluzione dei problemi

Se non riesci a stabilire una connessione cellulare, fai clic sul messaggio di errore sotto per visualizzare le relative soluzioni.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Ecco alcuni suggerimenti per la risoluzione dei problemi.

    1. Aggiorna la pagina e attendi qualche minuto per controllare se la SIM puo' essere rilevata.

    2. Assicurati che la SIM sia installata correttamente. Allinea il taglio della SIM con il segno corrispondente sullo slot per confermare il corretto orientamento di inserimento.

    3. Spegni il router, rimuovi e reinserisci la SIM, quindi riaccendi il router.

    4. Prova a usare un'altra SIM, se disponibile.

    Se il problema persiste, scarica i log e inviali a [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Questo problema ha due tipi di messaggi di errore:

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Ecco alcuni suggerimenti per la risoluzione dei problemi.

    1. Aggiorna la pagina e attendi qualche minuto per verificare se l'errore scompare.

    2. Fai clic su **Disconnect**/**Abort**, quindi su **Connect** per tentare una nuova connessione.

    3. Riavvia il router.

    4. Verifica lo stato della SIM e assicurati che sia attivata. Prova la SIM inserendola in uno smartphone per confermare che possa accedere normalmente a Internet con un piano dati mobile attivo oppure contatta il tuo operatore di rete per la verifica.

    5. Alcuni operatori di rete possono richiedere il protocollo 3G per la connessione. Vai su **SIM Card Settings** -> **Protocol**, seleziona **3G**, quindi fai clic su **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Il dispositivo si ricolleghera' automaticamente. Attendi qualche minuto per controllare se la connessione e' riuscita.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Se la connessione e' riuscita, la pagina verra' mostrata come segue.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Alcune SIM possono avere restrizioni d'uso particolari, ad esempio la richiesta di un APN specifico. Se la SIM non riesce a registrarsi, contatta il tuo operatore per verificare eventuali restrizioni.

        Se necessario, vai su **SIM Card Settings** -> **APN**, configura l'APN corretto sul router, quindi fai clic su **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Fai clic su **View More Information** per controllare l'intensita' del segnale cellulare. Se il segnale e' debole, assicurati che l'antenna sia installata correttamente. Sposta il router in una posizione aperta e senza ostacoli per migliorare la ricezione del segnale.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. Controlla se **Band Masking** o **Lock Tower** sono abilitati. In tal caso, disabilita la funzione e prova a riconnetterti.

    Se il problema persiste, scarica i log e inviali a [support@gl-inet.com](mailto:support@gl-inet.com).

## Certificazione IoT {#iot-certification}

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
