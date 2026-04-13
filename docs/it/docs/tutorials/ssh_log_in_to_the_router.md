# Accedere al router tramite SSH

Secure Shell, SSH, e un protocollo di rete crittografico per gestire in modo sicuro i servizi di rete su una rete non protetta. L'esempio piu noto e l'accesso remoto ai sistemi informatici da parte degli utenti. A volte hai bisogno di strumenti di base per collegarti in SSH al server. Questa guida spiega come effettuare il login SSH sui router GL.iNet.

---

## Per utenti Windows

Esistono diversi modi per accedere al terminale del router su Windows, ad esempio tramite Windows Cmd, PowerShell, Bitvise o PuTTY.

### Usare Windows Cmd

1. Apri il Prompt dei comandi

    Premi **Win** + **R** per aprire la finestra Esegui. Digita **cmd** e premi Enter.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Si aprira una finestra nera del prompt dei comandi.

    ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Accedi al router

    Nella finestra del prompt dei comandi, digita `ssh root@192.168.8.1` e premi Enter.

    ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Nota**: `192.168.8.1` e l'indirizzo IP predefinito del router. Se lo hai cambiato in precedenza, usa invece il tuo IP personalizzato.

    Quindi digita la password amministratore del router e premi Enter. **Per motivi di sicurezza, la password non viene mostrata sullo schermo**.

    ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Se la password e corretta, accederai con successo al router.

    ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Risoluzione dei problemi"

    1. **Errore: Connection timed out**

        Assicurati che il tuo dispositivo, ad esempio un laptop, sia collegato al router. Ricollegati al Wi-Fi del router o alla porta LAN e riprova.

    2. **Errore: Permission denied**

        Assicurati di digitare la password amministratore corretta. Se hai dimenticato la password, ripristina il router premendo il pulsante RESET per 10 secondi.

### Usare PowerShell

1. Apri Windows PowerShell

    Fai clic sull'icona di ricerca nella barra delle applicazioni, digita **PowerShell**, seleziona **Windows PowerShell** ed eseguilo come amministratore.

    ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Accedi al router

    Nella finestra PowerShell, digita `ssh root@192.168.8.1` e premi Enter.

    ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Nota**: `192.168.8.1` e l'indirizzo IP predefinito del router. Se lo hai cambiato in precedenza, usa invece il tuo IP personalizzato.

    Il sistema ti chiedera di confermare la connessione. Digita `yes` e premi Enter.

    ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Ti verra chiesto di inserire la password amministratore del router. Inserisci la password corretta e premi Enter. **Per motivi di sicurezza, la password non viene mostrata sullo schermo**.

    ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

    A questo punto accederai con successo al terminale del router.

    ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Risoluzione dei problemi"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Questo accade se la chiave di sicurezza del router e cambiata, ad esempio dopo un ripristino di fabbrica o un aggiornamento firmware, oppure se ti eri collegato in precedenza a un altro router, causando il fallimento della verifica della chiave host.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Per risolvere, apri Esplora file, vai in `C:\Users\Administrator\.ssh` e trova il file **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Fai doppio clic sul file known_hosts e aprilo con Notepad.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Elimina la voce relativa all'indirizzo IP del router, ad esempio 192.168.8.1, e salva il file. Poi chiudi Esplora file.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Tornato in PowerShell, usa di nuovo il comando `ssh root@192.168.8.1` per collegarti al router. Ti verra chiesto di confermare la connessione. Digita `yes` e premi Enter, quindi inserisci la password di accesso del router. A questo punto accederai con successo al terminale del router.

    2. **Cosa devo fare se ho cambiato la porta SSH del router?**

        Se hai cambiato la porta SSH del router, specifica la porta tramite il parametro `-p` quando usi il comando ssh. Ad esempio:

        ``ssh -p [nuovo numero di porta] [nome utente]@[indirizzo IP del router]``

### Usare Bitvise

Guarda questo video per accedere al router tramite Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Usare PuTTY

1. Scarica PuTTY

    Scarica l'ultima versione di PuTTY da [qui](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Installa PuTTY

    ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Avvia PuTTY

    Fai clic su **PuTTY** dal menu Start.

    ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Vedrai la seguente finestra di configurazione.

    ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    Inserisci come Host Name, o IP address, `192.168.8.1`, lascia la porta predefinita `22` e seleziona come tipo di connessione `SSH`.

    Inserisci `Your Session` nelle sessioni salvate e fai clic su `Save` per salvare il contenuto.

    Poi fai clic su `Open` in basso.

    ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    Comparira un avviso di sicurezza come mostrato sotto: fai clic su `Yes`.

    ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    login as: `root`

    Quindi inserisci la password amministratore. **Per motivi di sicurezza, la password non viene mostrata sullo schermo**.

    ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Quando vedi l'immagine sopra, significa che hai effettuato con successo il login SSH al router.

---

## Per utenti Linux/Mac

Il processo su Linux e Mac OS e generalmente lo stesso. Di seguito usiamo Ubuntu come esempio.

### Usare Ubuntu

1. Avvia Terminal

    Avvia Ubuntu. Fai doppio clic sull'icona Terminal per avviare il terminale.

    ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Accedi al router

    Inserisci il comando di login SSH: `ssh root@192.168.8.1`

    ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Il sistema ti chiedera di confermare la connessione. Digita `yes` e premi Enter.

    ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Quindi inserisci la password amministratore del router. **Per motivi di sicurezza, la password non viene mostrata sullo schermo**.

    ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Quando vedi l'immagine sopra, significa che hai effettuato con successo il login al router.

??? "Risoluzione dei problemi"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Questo accade se la chiave di sicurezza del router e cambiata, ad esempio dopo un ripristino di fabbrica o un aggiornamento firmware, oppure se ti eri collegato in precedenza a un altro router, causando il fallimento della verifica della chiave host.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Se questo accade, esegui il comando mostrato nel riquadro rosso sopra. Copia esattamente il comando mostrato nel tuo terminale.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Poi prova a collegarti di nuovo.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        Potresti incontrare questo errore durante la connessione. E dovuto a una modifica del pacchetto Openssh dalla versione 8.8. Per risolvere, apri il file **~/.ssh/config** con un editor di testo, ad esempio Nano o Vim, e aggiungi le seguenti righe:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Assicurati di cambiare l'IP host se non e quello predefinito.

        Per maggiori dettagli su questo problema, fai riferimento [qui](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
