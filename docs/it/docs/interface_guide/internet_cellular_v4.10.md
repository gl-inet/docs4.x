# Connettersi a Internet tramite rete cellulare (v4.10)

Il contenuto di questa pagina si basa sulle versioni firmware v4.10 e successive. Se il dispositivo usa una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Versione firmware" data-placeholder="Firmware v4.10 e successivi" markdown="1">

- [Firmware v4.8 - v4.9](internet_cellular.md)
- [Firmware v4.7 e precedenti](internet_cellular_v4.7.md)

</div>

---

La maggior parte dei router GL.iNet supporta la connettività cellulare. Questa guida descrive le connessioni cellulari per due tipi di router:

1. **Router cellulari**

    I router cellulari GL.iNet dispongono di un modulo 4G/5G integrato e di uno o due slot per SIM, come Spitz AX (GL-X3000) e Mudi 7 (GL-E5800). Le impostazioni cellulari del pannello di amministrazione web possono variare leggermente in base al modello e alla versione firmware. Per configurare la connessione cellulare su questi modelli, consulta [Router cellulari](#cellular-routers).

2. **Router non cellulari**

    I router non cellulari includono altri tipi di router, ad esempio router domestici, da viaggio o mini router e gateway di sicurezza. Solitamente dispongono di una porta USB a cui collegare un dongle USB (non incluso) per la connettività cellulare. Per configurare la connessione cellulare su questi modelli, consulta [Router non cellulari](#non-cellular-routers).

**Nota:** alcune SIM devono essere attivate prima del primo utilizzo. Per garantire la compatibilità, attiva la SIM in uno smartphone prima di inserirla nel router.

## Router cellulari {#cellular-routers}

Questa sezione usa **Mudi 7 (GL-E5800)** come esempio per descrivere la configurazione cellulare e le funzioni correlate.

Poiché Mudi 7 dispone di una eSIM integrata e di due slot Nano-SIM con supporto Dual SIM Dual Standby, il suo pannello di amministrazione web può differire leggermente da quello di altri router cellulari, in particolare dai modelli con un solo slot SIM.

### Configurazione della rete

Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

1. Quando non è inserita alcuna SIM, la pagina mostra "Your SIM card has not been detected".

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Inserisci una SIM. Il router inizierà automaticamente la connessione. Una volta connesso, la pagina mostra l'operatore della SIM, la potenza del segnale, la banda, l'utilizzo dei dati e altre opzioni.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Se la SIM non viene rilevata, reinseriscila nel router oppure riavvia il router e riprova.

3. Per visualizzare i dettagli della rete, fai clic su **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    In **Network Information** puoi visualizzare SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address e IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Che cos'è Max Bit Rate (AMBR)?"

        Max Bit Rate (AMBR) significa Aggregate Maximum Bit Rate. Definisce il limite massimo aggregato della velocità in bit per tutti i bearer non-GBR dell'operatore. Questo parametro viene configurato dall'operatore di rete mobile.

4. Per configurare manualmente la rete, fai clic su **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    In **Network Settings** puoi configurare alcuni parametri di rete, ad esempio l'APN.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: le impostazioni APN vengono generalmente recuperate automaticamente dalla SIM. Alcune SIM richiedono un APN specifico. Se non conosci l'APN corretto, chiedilo al tuo operatore.

    - **IP Type**: viene rilevato automaticamente. Puoi impostare IPv4, IPv6 o entrambi. Assicurati che l'opzione selezionata corrisponda al tipo IP supportato dalla SIM. Se la SIM non supporta il tipo IP selezionato, oppure se qui è selezionato IPv6 ma IPv6 è disabilitato sul router, potrebbero verificarsi problemi di connessione.

    - **International Data Roaming**: è abilitato per impostazione predefinita per agevolare l'uso dei dati durante i viaggi internazionali. Puoi disabilitarlo se non è necessario o per evitare costi di roaming elevati.

    - **TTL**: alcuni operatori determinano se una SIM viene usata in un router leggendo il valore TTL. Se la SIM non funziona nel router, prova a impostare TTL su un valore diverso da 64 e 128, ad esempio 65.

    - **HL**: in IPv6, il campo HL (Hop Limit) limita il numero di hop di trasmissione dei pacchetti nella rete ed equivale al TTL in IPv4.

    - **MTU**: imposta il valore MTU in base allo scenario d'uso. Impostazioni errate possono interrompere la connessione Internet. Se modifichi MTU, riavvia il dispositivo affinché la modifica abbia effetto.

    - **Authentication**: generalmente è impostata su NONE se non sono richieste credenziali. Puoi impostarla su PAP, CHAP o PAP/CHAP.

### Statistiche del traffico

Per visualizzare le statistiche del traffico, fai clic su **Data Usage**.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Per impostare Data Cap Amount per la SIM o pianificare l'azzeramento periodico dei dati, abilita **SIM Limit Settings**.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Imposta Data Cap Amount, Data Reset Period, Start Day e Start Hour, quindi fai clic su **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Nota**:

1. Se Data Used supera Data Cap Amount, modifica Data Cap Amount o Data Used. In caso contrario, la rete potrebbe disconnettersi oppure il router potrebbe passare a un'altra SIM, ma solo se [SIM Failover](#sim-failover) è abilitato.

2. Se è impostato SIM 1 Data Cap Amount e SIM Auto Switch è abilitato, SIM 1 passerà automaticamente a SIM 2 quando l'utilizzo dati supera Data Cap Amount e SIM 1 verrà disabilitata.

3. Start Day: il numero massimo di giorni corrisponde al numero effettivo di giorni del mese corrente.

### Dettagli della connessione cellulare

Per visualizzare i dettagli della connessione cellulare, fai clic su **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In **Cellular Information** puoi visualizzare Network Type, TAC, Cell ID, Band e Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: viene rilevato automaticamente. Per specificarlo, passa alla scheda **Cellular Settings** e seleziona il tipo di rete dall'elenco a discesa.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Seleziona 5G per una maggiore velocità, se è disponibile un segnale 5G, oppure 4G per una maggiore stabilità.

    Se blocchi la stazione base, il tipo di rete viene fissato e non può essere modificato.

- **TAC**: abbreviazione di Tracking Area Code, un identificatore assegnato dalla rete che rappresenta un'area di tracciamento per la gestione della mobilità nella rete cellulare. Viene rilevato automaticamente dalla stazione base.

- **Cell ID**: identificatore univoco usato per distinguere una singola cella di una stazione base. Viene anch'esso rilevato automaticamente dalla stazione base.

- **Band Information**: fai clic per visualizzare altri parametri relativi alla banda cellulare.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: fai clic per visualizzare la cronologia della potenza del segnale. Puoi usarla per monitorare la qualità della connessione cellulare.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Band Masking

Band Masking consente di usare bande cellulari specifiche per migliorare il segnale.

Per abilitare Band Masking, fai clic su **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In **Cellular Settings**, abilita **Band Masking**, seleziona le bande da usare e fai clic su **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Blocco dell'operatore

!!! note "Modelli supportati"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) supporta questa funzione con firmware v4.8 o successivo.

Bloccando un operatore mobile specifico, il router userà soltanto la rete di quell'operatore, garantendo una connessione stabile ed evitando costi di roaming indesiderati, soprattutto nelle zone di confine in cui il dispositivo potrebbe altrimenti connettersi a reti straniere.

Per bloccare un operatore, fai clic su **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In **Cellular Settings**, fai clic su **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Prima di eseguire la scansione delle reti, puoi selezionare **Lock Mode**.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: blocca manualmente un operatore specifico.

- **Manual-Auto**: passa automaticamente a una rete operatore disponibile se il blocco manuale non riesce.

Fai quindi clic su **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Attendi circa un minuto. Verranno mostrati gli operatori disponibili. Selezionane uno e fai clic su **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Il segnale cellulare verrà bloccato sull'operatore selezionato.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Blocco della stazione base

!!! note "Modelli supportati"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) supporta questa funzione con firmware v4.7 o successivo.

Per ricevere un segnale di qualità elevata e garantire una connessione cellulare stabile, puoi provare a bloccare una stazione base. La stazione bloccata deve tuttavia corrispondere alle bande di frequenza supportate dall'operatore e dal dispositivo; in caso contrario, la connessione potrebbe non riuscire.

Per bloccare una stazione base, fai clic su **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

In **Cellular Settings**, fai clic su **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

Nella finestra a comparsa, fai clic su **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Attendi circa un minuto. Verranno mostrate le stazioni base disponibili.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Selezionane una per visualizzarne i dettagli, quindi fai clic su **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Il segnale cellulare verrà bloccato sulla stazione selezionata.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Nota**:

1. Quando l'interfaccia Cellular è abilitata, il dispositivo potrebbe non riuscire a rilevare tutte le stazioni base.

2. Se la stazione bloccata non corrisponde ai parametri Band Masking, se abilitati, o APN delle impostazioni cellulari, il router non riuscirà a connettersi alla rete cellulare.

3. Dopo aver bloccato una stazione base, se sposti il router in un'altra posizione, dopo il riavvio tenterà ancora di riconnettersi alla stazione bloccata. Ciò potrebbe impedire la connessione automatica alla rete cellulare nella nuova posizione. In tal caso, sblocca la stazione corrente oppure bloccane manualmente una nuova.

### SMS

Consulta [SMS](../tutorials/sms.md).

### Inoltro SMS

Consulta [Inoltro SMS](../tutorials/sms_forwarding.md).

### Modalità aereo

Per abilitare Airplane Mode, fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro e attiva **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Informazioni sul modem

Per visualizzare i dettagli del modem, fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro e seleziona **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Failover SIM {#sim-failover}

Questa funzione è disponibile solo sui router cellulari che supportano Dual-SIM.

SIM Failover consente al router di passare automaticamente tra SIM 1 e SIM 2. Quando l'utilizzo dei dati della SIM con priorità più alta supera Data Cap Amount oppure la SIM non riesce a connettersi a Internet, il router passa alla SIM di backup per mantenere la connessione.

Per abilitare SIM Failover, fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro e seleziona **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

Nella finestra a comparsa, abilita **Auto Switch**. Puoi trascinare il pulsante a destra per modificare la priorità delle SIM.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Per fare in modo che il router torni alla SIM preferita a un'ora specifica, abilita **Scheduled Switch to Preferred SIM**, imposta **Daily Execution Time** e fai clic su **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### Comandi AT

I comandi AT sono istruzioni standard usate per comunicare con il modem cellulare. Questa funzione consente di inviare comandi e controllare lo stato del modem.

Fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro e seleziona **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: quando Shortcut è impostato su **Manual command**, inserisci il comando desiderato nel campo **AT Command** e fai clic su **Send** in basso. Il risultato verrà mostrato nel riquadro di output sottostante.

    Puoi anche fare clic sul riquadro e selezionare un **preset command** dall'elenco a discesa.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Ad esempio, selezionando la scorciatoia "Request SIM card status" e lo slot SIM1, fai clic su "Send" per ottenere il risultato mostrato di seguito.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: scegli se il comando si applica a SIM1 o SIM2. Le opzioni disponibili dipendono dal numero di slot SIM del router cellulare.

- **AT Command**: quando Shortcut è impostato su "Manual command", inserisci in questo campo il comando desiderato.

## Router non cellulari {#non-cellular-routers}

Sebbene i router non cellulari non dispongano di un modem cellulare integrato, puoi collegare un dongle USB esterno (non incluso) alla porta USB per ottenere la connettività cellulare.

I dongle e i modem USB possono funzionare in modalità diverse: modalità modem USB standard o modalità host-less.

- **Modalità modem USB standard**: il router agisce come host USB, mentre il dongle funziona come modem USB slave. Il dongle espone sia le interfacce di comando (AT/QMI/MBIM) sia una porta Ethernet USB virtuale e può quindi essere gestito tramite la WAN Cellular nativa del router. Il router può leggere metriche cellulari di basso livello, tra cui ICCID, potenza del segnale e banda, mentre le impostazioni SIM vengono configurate direttamente dall’interfaccia web del router.

- **Modalità host-less**: il dongle esegue internamente la connessione cellulare e presenta al router un’interfaccia Ethernet USB virtuale. Il router lo riconosce come una WAN in tethering anziché come un modem controllabile; la connessione viene quindi stabilita tramite l’interfaccia Tethering e non tramite Cellular. Sul router non sono disponibili metriche cellulari di basso livello e tutte le configurazioni APN e SIM devono essere completate tramite l’interfaccia web integrata del dongle.

Consulta la sezione corrispondente alla modalità operativa del dongle USB.

### Modem USB standard

Questa sezione usa **Mango 2 (GL-MG1300)** e la scheda di sviluppo 5G [GL-M2](https://www.gl-inet.com/products/gl-m2){target="_blank"} (modulo 5G NR: RM520N-GL) come esempio per descrivere la configurazione cellulare e le funzioni correlate.

1. Inserisci una SIM nella scheda GL-M2, quindi collega la GL-M2 alla porta USB del router.

2. Accedi al pannello di amministrazione web del router e vai su **INTERNET** -> **Cellular**.

    Il router tenterà automaticamente di connettersi a Internet. Una volta connesso, la pagina mostra i dettagli della rete e un punto verde.

    ![m2 sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_active.png){class="glboxshadow"}

3. Impostazioni della SIM.

    Per visualizzare la configurazione della SIM, fai clic su **SIM Card Settings**.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings1.png){class="glboxshadow"}

    Puoi visualizzare le configurazioni SIM rilevate automaticamente, ad esempio APN, tipo IP e tipo di rete. La modifica di queste configurazioni comporta una nuova connessione alla rete cellulare.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings2.png){class="glboxshadow"}

4. Informazioni sulla SIM.

    Per visualizzare i dettagli della SIM, fai clic su **SIM Information**.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info1.png){class="glboxshadow"}

    Puoi visualizzare le informazioni di rete della SIM, ad esempio ICCID, indirizzo IP, DNS, banda cellulare e potenza del segnale.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info2.png){class="glboxshadow gl-80-desktop"}

5. SMS e inoltro SMS.

    Per usare gli SMS e l’inoltro SMS, consulta [SMS](../tutorials/sms.md) e [Inoltro SMS](../tutorials/sms_forwarding.md).

6. Gestione dei profili cellulari.

    Per gestire i profili SIM, fai clic sull’icona a forma di ingranaggio nell’angolo superiore destro e seleziona **Manage Cellular Profiles**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    Viene mostrato il profilo attualmente in uso.

    ![m2 manage profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_manage_profiles.png){class="glboxshadow"}

    Fai clic su **Add a New Profile** per aggiungere altri profili, se necessario.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile1.png){class="glboxshadow"}

    Inserisci i parametri richiesti, quindi fai clic su **Apply**.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile2.png){class="glboxshadow"}

7. Comando AT del modem.

    I comandi AT sono istruzioni standard usate per comunicare con il modem cellulare. Questa funzione consente di inviare comandi e controllare lo stato del modem.

    Per eseguire un comando AT, fai clic sull’icona a forma di ingranaggio nell’angolo superiore destro e seleziona **Modem AT Command**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    ![m2 atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_atcommand.png){class="glboxshadow"}

    - **Shortcut**: quando Shortcut è impostato su **Manual command**, inserisci il comando desiderato nel campo **AT Command** e fai clic su **Send**. Il risultato viene mostrato nel riquadro di output sottostante.

        Puoi anche fare clic sul riquadro e selezionare un **preset command** dall’elenco a discesa.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

        Ad esempio, seleziona la scorciatoia «Request SIM card status» e lo slot SIM1, quindi fai clic su «Send» per ottenere il risultato mostrato di seguito.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

    - **SIM Slot**: scegli se il comando si applica a SIM1 o SIM2. Le opzioni disponibili dipendono dagli slot SIM del modem USB esterno collegato al router.

    - **AT Command**: quando Shortcut è impostato su «Manual command», inserisci in questo campo il comando desiderato.

### Dongle host-less

Questa sezione usa **Flint 3 (GL-BE9300)** e il dongle USB esterno [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} come esempio per descrivere la configurazione della connessione cellulare.

1. Collega il dongle USB alla porta USB del router.

2. Accedi al pannello di amministrazione web del router, vai su **INTERNET** -> **Tethering**, quindi fai clic su **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Se devi configurare impostazioni avanzate, ad esempio TTL, HL e MTU, fai clic su **Advanced** e personalizzale prima di fare clic su **Connect**.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Una volta connesso, la pagina mostra i dettagli della rete e un punto verde, a indicare che la connessione è riuscita.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

4. Per configurare l’APN e le impostazioni SIM della scheda installata in SIMPoYo uFi, consulta [Gestire SIMPoYo uFi](../user_guide/simpoyo-4g-ufi/index.md#manage-simpoyo-ufi).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
