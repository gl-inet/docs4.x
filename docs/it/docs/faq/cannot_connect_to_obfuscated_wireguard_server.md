# Impossibile connettersi a un server WireGuard offuscato

L'offuscamento VPN è una tecnica che maschera il traffico VPN facendolo apparire come normale traffico Internet. Attualmente alcuni router GL.iNet supportano il protocollo AmneziaWG, consentendo di configurare un server WireGuard con offuscamento del traffico abilitato.

Se non riesci a stabilire una connessione a un server WireGuard offuscato, segui i passaggi di risoluzione dei problemi qui sotto.

1. **Assicurati che la configurazione WireGuard importata in ogni client sia dedicata.**

    Ogni client richiede un file di configurazione peer esclusivo. Condividere la stessa configurazione tra più client causerà errori di connessione.

    Se necessario, vai su **VPN** -> **WireGuard Server** -> **Profiles** per visualizzare i profili esportati.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Assicurati che i parametri offuscati possano essere verificati dal client.**

    Il protocollo AmneziaWG è retrocompatibile. Se il server WireGuard supporta solo AmneziaWG v1.0, il file di configurazione supererà comunque la verifica quando viene importato in un client che supporta v2.0.
        
    Tuttavia, se il file di configurazione include parametri di offuscamento di AmneziaWG v2.0, assicurati che il client WireGuard supporti AmneziaWG v2.0. In caso contrario, la verifica dei parametri potrebbe non riuscire.

    !!! tip "Come identificare la versione di AmneziaWG?"

        **V1.0**: nessun parametro S3-S4; H1-H4 sono singoli numeri interi fissi.
        
        **V2.0**: è V2.0 se viene soddisfatta una delle condizioni seguenti:
        
        - Include parametri S3-S4
        - H1-H4 sono impostati come intervalli numerici
        - Include parametri I1-I5 personalizzati.
        
        > Nota: I1-I5 non vengono generati automaticamente. Gli utenti possono aggiungerli manualmente come righe aggiuntive nel file di configurazione per far sembrare il traffico AmneziaWG simile ad altri protocolli comuni, come QUIC o WebRTC.

    Se il client WireGuard è un router GL.iNet, controlla la sua versione di AmneziaWG con i due metodi seguenti.

    ??? note "Controllare dal Router Web Admin Panel"

        1. Accedi al Web Admin Panel del router.

        2. Vai su **VPN** -> **WireGuard Server** -> **Configuration** e verifica i parametri di offuscamento. Se la configurazione include **S3-S4** e **H1-H4** come intervalli variabili, invece di valori fissi, il router esegue AmneziaWG 2.0, come mostrato sotto.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            In caso contrario, usa AmneziaWG 1.0, come mostrato sotto.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Controllare tramite comando SSH"

        1. Accedi al router tramite SSH.

        2. Esegui `opkg list|grep awg` e controlla il suffisso del pacchetto **kmod-amneziawg** nell'output. Se è contrassegnato con **2.0**, il router supporta AmneziaWG 2.0, come mostrato sotto.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            In caso contrario, esegue AmneziaWG 1.0, come mostrato sotto.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Regola i parametri di offuscamento.**

    Se hai configurato manualmente i [parametri di offuscamento](amneziawg_obfuscation.md#parameter-overview), come Jc, Jmin o Jmax, sul server WireGuard, impostazioni errate possono causare errori di handshake.

    Prova a modificare questi parametri di offuscamento e riconnettiti per escludere problemi di mancata corrispondenza dei parametri. Puoi anche ripristinare le impostazioni di offuscamento predefinite per eseguire un test.

4. **Testa la connessione con l'app ufficiale AmneziaWG.**

    Esegui una prova comparativa: installa l'app ufficiale AmneziaWG, importa nell'app il file di configurazione originale esportato dal server e prova a connetterti.

    - Se la connessione riesce nell'app ufficiale, il file di configurazione è valido. Il problema potrebbe riguardare il dispositivo client originale. Verifica la sua connettività di rete o contatta il supporto per ulteriore assistenza.

    - Se la connessione continua a non riuscire, il problema proviene dalla configurazione del server sul router. Controlla le impostazioni del server e i parametri di offuscamento.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
