# Parental Control

Il parental control e' un modo per proteggere i bambini online bloccando siti web inappropriati e limitando il tempo di utilizzo dei dispositivi. Aiuta a impedire l'accesso a contenuti dannosi, a gestire il tempo davanti allo schermo e a garantire un uso responsabile di Internet da parte dei bambini.

Questa funzione e' disponibile dal firmware v4.2.

Guarda questo video oppure segui i passaggi qui sotto per saperne di piu' su Parental Control sui router GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Versione locale

La versione locale e' fornita da GL.iNet. Al momento e' in beta e non ha costi aggiuntivi. In questa versione, se hai bisogno di filtrare le richieste per applicazione, devi inserire manualmente il dominio.

### Modelli supportati

??? "Modelli supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Modelli non supportati"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Configurazione

Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Parental Control**.

Per il firmware ver.4.8.4 e successivi, vai su **Flow Control** -> **Parental Control**.

Assicurati che l'orario del router sia corretto. In caso contrario, vai su **SYSTEM** -> **Time Zone** per sincronizzarlo prima.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Abilita Parental Control e fai clic su **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: viene usato per bloccare l'accesso a Internet dei dispositivi non gestiti.

Poi segui la procedura guidata per configurare Parental Control.

Di seguito trovi due casi d'uso di riferimento, che puoi adattare alla tua situazione.

**Case 1**

**Scenario**: i dispositivi del profilo possono accedere a Internet solo per studio dalle 8:00 alle 11:00 nei giorni feriali e per il gaming dalle 18:00 alle 20:00 nei fine settimana. In tutti gli altri orari, l'accesso a Internet e' bloccato per impostazione predefinita.

Segui i passaggi qui sotto.

1. Crea un profilo e assegnagli un nome.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

2. Seleziona i dispositivi che vuoi gestire. Se non sono ancora stati collegati al router, aggiungili manualmente inserendo i loro indirizzi MAC.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

3. Imposta il limite di accesso.

    Esistono due ruleset predefiniti: **Block Internet Access** e **No Limit**. Crea qui altri due ruleset per usarli piu' avanti: **Learning** e **Play**.

    Fai clic su **Add a New Ruleset**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

4. Specifica il nome del ruleset, ad esempio Learning, il colore e l'elenco dei siti da bloccare. Poi fai clic su **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

    **Nota**: i nomi di dominio inseriti nella blocklist devono includere anche i sottodomini. Ad esempio, se inserisci `example.com`, saranno inclusi anche eventuali sottodomini, come `subdomain.example.com`.

    Allo stesso modo, crea un altro ruleset chiamato Play. Specifica un colore, i siti da bloccare e fai clic su **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

5. Dopo l'applicazione, ci saranno in totale quattro ruleset, come mostrato di seguito.

    Assicurati di selezionare **Block Internet Access** come **Default Ruleset**, quindi fai clic su **Finish**.

    ![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

6. Poi vai su Set Schedule. Fai clic su **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

7. Aggiungi il ruleset **Learning** alla pianificazione. Imposta **Execution Time** dalle 8:00 alle 11:00 nei giorni feriali. Fai clic su **Apply**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

8. Verrai portato alla pagina di modifica del profilo appena creato.

    ![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

    Vedrai che e' stata creata una pianificazione. Fai clic su **Add Schedule** in alto a destra.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/add_schedule.png){class="glboxshadow"}

9. Aggiungi un altro ruleset, **Play**, alla pianificazione. Imposta **Execution Time** dalle 18:00 alle 20:00 nelle serate del fine settimana. Fai clic su **Apply**.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

10. Poi vedrai che anche il ruleset Play e' stato aggiunto alla pianificazione.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

    **Nota**: la linea rossa tratteggiata indica l'ora corrente.

    Puoi anche modificare il ruleset della pianificazione facendo clic su una determinata parte della pianificazione.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.jpg){class="glboxshadow"}

11. Fai clic su **Parental Control** in alto per tornare alla pagina Parental Control.

    ![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

    Vedrai la configurazione finale. Puoi modificare i profili e i ruleset esistenti oppure aggiungerne di nuovi.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/final_configuration.png){class="glboxshadow"}

**Case 2**

**Scenario**: i dispositivi del profilo possono accedere a Internet solo per giochi e video brevi dalle 18:00 alle 20:00 nelle serate del fine settimana. In tutti gli altri orari, compreso il tempo per dormire dalle 21:00 alle 7:00 del mattino successivo, l'accesso a Internet e' bloccato per impostazione predefinita.

Guarda il video tutorial qui sotto.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Risoluzione dei problemi

Se le impostazioni configurate non hanno effetto, verifica le seguenti possibili cause.

1. Cache DNS.

    Browser e sistemi operativi mantengono una cache DNS, quindi le modifiche potrebbero richiedere del tempo per avere effetto. Puoi svuotare la cache per applicare subito le modifiche.

      * [Svuotare la cache in Chrome desktop](https://support.google.com/accounts/answer/32050){target="_blank"}

      * [Svuotare la cache in Edge desktop](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. La pianificazione del profilo non e' ancora iniziata.

3. Il nome di dominio inserito potrebbe essere errato.

    Il dominio di un sito web e' pubblico, ma il dominio API usato da un'app spesso non lo e'. Per risolvere, usa uno strumento come Wireshark per catturare i pacchetti oppure cerca il dominio pertinente.

    Ad esempio, per bloccare `www.google.com`, usare `google.com` e' piu' efficace che usare `www.google.com`.

4. Il dispositivo di destinazione usa un indirizzo MAC casuale per ogni connessione, impedendo alle regole di avere effetto.

## Versione Bark

La versione [Bark](https://www.bark.us/){target="_blank"}, fornita e gestita da Bark sulla propria piattaforma, offre l'opzione di filtrare applicazioni e siti web con un solo clic e di monitorare la cronologia delle richieste.

Offre funzioni di monitoraggio per piu' di 24 app popolari e piattaforme social, incluse nell'elenco preimpostato della nostra funzione locale di parental control.

Grazie alla funzione di logging, registra quale client ha visitato quale sito web e a che ora. Questo consente ai genitori di visualizzare facilmente i log, identificare i siti non presenti nella blacklist e aggiungerli rapidamente all'ambito di gestione.

La funzione Bark Parental Control e' disponibile dal firmware v4.5 ed e' supportata solo su router GL.iNet selezionati.

**Nota**:

1. Il servizio Bark e' disponibile **solo negli Stati Uniti, in Australia e in Sudafrica**. Fai clic [qui](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} per i dettagli.
2. Il servizio Bark richiede in genere un abbonamento a pagamento. Tuttavia, nell'ambito della nostra partnership con Bark, GL.iNet offre gratuitamente il piano Bark Home su modelli di router selezionati, fornendo monitoraggio avanzato e avvisi senza costi aggiuntivi.
3. Le due versioni di Parental Control non possono essere abilitate contemporaneamente. Passare da una versione all'altra disabilitera' automaticamente l'altra.

### Modelli supportati

??? "Modelli supportati"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Modelli non supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Configurazione

Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Parental Control**.

Seleziona la versione Bark, attiva l'interruttore e fai clic su **Apply**.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Nota:** il servizio Bark potrebbe non essere disponibile in alcuni paesi. Poiche' GL.iNet non e' il fornitore di questo servizio, se riscontri problemi durante l'uso di Bark, contatta direttamente il [supporto tecnico Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet) per assistenza.

Il servizio Bark e' abilitato, ma questo dispositivo non e' ancora associato ad alcun account. Usa il [Device Pairing Link](https://www.bark.us/app/signup/?ref=glinet&home=glinet) per associare questo dispositivo al tuo account Bark.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Una volta completata l'associazione, la pagina verra' visualizzata come segue.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Il tuo dispositivo e' ora connesso ai Bark Cloud Services e associato al tuo account. Vai su [Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) e accedi al tuo account per creare un profilo per il controllo della rete.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
