# Cosa devo fare se l'installazione del profilo eSIM non riesce?

Se provi ad aggiungere un profilo eSIM sul router GL.iNet ma l'installazione non riesce, fai riferimento ai seguenti passaggi di risoluzione dei problemi:

1. Assicurati che il router sia connesso a Internet.

    Verifica che il router sia connesso correttamente a Internet. Una rete instabile puo influire sul caricamento del profilo eSIM e impedire al router di ottenerlo e installarlo.

    Se possibile, prova a collegare il router a un'altra sorgente di rete, ad esempio l'hotspot del tuo smartphone o una rete Wi-Fi pubblica, poi carica di nuovo il profilo eSIM per fare una prova.

2. Cambia le impostazioni DNS.

    Se Internet funziona correttamente, accedi al pannello di amministrazione web del router e vai su **NETWORK** -> **DNS**.

    Imposta la modalita DNS su **Manual DNS** e configura altri server DNS pubblici per il test, ad esempio Google DNS (`8.8.8.8`, `8.8.4.4`) o Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Fai clic su **Apply** per salvare le modifiche, quindi prova di nuovo a caricare il profilo eSIM.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Disabilita AdGuard Home.

    Se AdGuard Home e disponibile e abilitato sul router, disabilitalo e prova di nuovo a installare il profilo eSIM.

4. Controlla la disponibilita del profilo eSIM.

    Verifica se questo profilo eSIM o QR code e gia stato attivato o installato su un altro dispositivo.

    La maggior parte dei profili eSIM puo essere installata una sola volta e non puo essere attivata su piu dispositivi. Se possibile, contatta il provider eSIM per confermare se il profilo attuale e ancora disponibile. Se il QR code o il codice di attivazione e scaduto, richiedine uno nuovo e riprova.

5. Controlla il codice di attivazione.

    Un QR code correttamente formattato mostrera un codice di attivazione che inizia con **LPA:**. Tuttavia, alcuni QR code non standard possono fornire solo un codice grezzo senza il prefisso LPA. In questo caso, aggiungi manualmente `LPA:` all'inizio del codice prima di fare clic su **Install**.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Verifica se e richiesto un codice di conferma.

    Alcuni profili eSIM richiedono l'inserimento di un codice di conferma durante l'installazione, come Smarty eSIM. Controlla il pacchetto eSIM o la guida di installazione per verificare se e necessario un codice di conferma. Se si, inserisci il codice corretto.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Se i passaggi sopra non risolvono il problema, esporta il log eSIM dalla pagina **eSIM Management**.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Invia quindi il log, insieme alle informazioni chiave riportate sotto, a [support@gl-inet.com](mailto:support@gl-inet.com) per ulteriore assistenza.

    - Il problema riscontrato
    - I metodi di risoluzione dei problemi gia provati
    - Il tuo provider eSIM

---
