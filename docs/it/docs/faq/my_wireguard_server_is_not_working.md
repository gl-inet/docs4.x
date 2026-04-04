# Il server WireGuard sul router GL.iNet non funziona correttamente

Ci sono vari motivi per cui il server WireGuard configurato sul router GL.iNet potrebbe non funzionare correttamente.

Se riscontri problemi, segui questi passaggi di risoluzione in base alla tua situazione specifica.

#### Situazione 1: il server WireGuard si avvia ma non è possibile connettersi

??? "Segui questi passaggi"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Il port forwarding configurato sul router principale collegato al router secondario (GL.iNet) potrebbe non funzionare correttamente.
    Per verificare se il port forwarding funziona correttamente, prova a inoltrare la porta HTTPS del router principale al server WireGuard. Segui questi passaggi:

    1. Inoltra la porta HTTPS del router principale al server WireGuard

        1. Accedi al pannello di amministrazione del router principale.
        2. Vai alla schermata di port forwarding.
        3. Crea una nuova regola e chiamala **HTTPS**.
        4. Inserisci le seguenti informazioni:
            * **External port/Internal port:** inserisci **443**.
            * **Protocol:** scegli **All** oppure **UDP/TCP**.
            * **Internal IP** (oppure indicato come **Host IP**): inserisci l'indirizzo WAN IP del router secondario oppure selezionalo dal menu a discesa, se disponibile.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Abilita DDNS e l'accesso remoto HTTPS (sul router GL.iNet)

        1. In un browser web, inserisci l'URL del pannello di amministrazione del router GL.iNet (ad esempio 192.168.8.1) ed effettua l'accesso.
        2. Nella barra laterale sinistra, fai clic su **Applications** > **Dynamic DNS**.
        3. Attiva **Enable DDNS** e seleziona la casella **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Salva l'hostname in un luogo sicuro, perché ti servirà più tardi, quindi fai clic su **Apply**.
        5. Nella barra laterale sinistra, fai clic su **System** > **Security**.
        6. In **Remote Access Control**, attiva **HTTPS Remote Access**.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Fai clic su **Apply**.

    3. Verifica se riesci ad accedere al pannello di amministrazione del router GL.iNet

        1. Su un altro dispositivo (ad esempio laptop o telefono), collegati a una rete Wi-Fi diversa oppure alla rete cellulare.
        2. Nella barra degli indirizzi del browser, inserisci l'hostname salvato in precedenza (abcd123.glddns.com).
        3. Fai clic su **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Fai clic su **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Se vedi la schermata di accesso del router GL.iNet (router secondario), significa che il port forwarding configurato sul router principale funziona correttamente.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Se non vedi la schermata di accesso del router GL.iNet (router secondario), il port forwarding non funziona correttamente. Configuralo di nuovo oppure assicurati di usare come router principale un dispositivo con funzioni di port forwarding realmente funzionanti.

#### Situazione 2: il server WireGuard mostra che il client VPN è connesso, ma il client VPN non può accedere a Internet

??? "Segui questi passaggi"

    Segui i passaggi indicati per ciascuna possibile causa qui sotto e controlla se il problema è risolto. Se il problema si risolve, puoi saltare il resto della sezione.

    **Possibile causa 1: il tuo provider Internet potrebbe non riuscire a risolvere i server DNS di GL.iNet**

    Prova a configurare manualmente gli indirizzi DNS seguendo questi passaggi:

    1. In un browser web, inserisci l'URL del pannello di amministrazione del router GL.iNet (ad esempio 192.168.8.1) ed effettua l'accesso.
    2. Nella barra laterale sinistra, fai clic su **Network** > **DNS**.
    3. Per **Mode**, seleziona **Manual DNS**.
    4. Per **DNS Server 1**, seleziona **Google Public DNS**.
    5. Fai clic su **Apply**.

    **Possibile causa 2: l'IP gateway del router principale è in conflitto con l'indirizzo IP del server WireGuard**

    Prova a cambiare l'indirizzo IPv4 seguendo questi passaggi:

    1. In un browser web, inserisci l'URL del pannello di amministrazione del router GL.iNet (ad esempio 192.168.8.1) ed effettua l'accesso.
    2. Nella barra laterale sinistra, fai clic su **VPN** > **WireGuard Server**.
    3. Nella scheda **Configuration**, nel campo **IPv4 Address**, inserisci un nuovo indirizzo IP (ad esempio 10.1.0.1/24).
    4. Fai clic su **Apply**.

    **Possibile causa 3: se sia il server WireGuard sia il client WireGuard sono configurati su router GL.iNet, i loro indirizzi IP LAN sono in conflitto**

    Prova a cambiare l'indirizzo IP LAN su uno dei due router seguendo questi passaggi:

    1. In un browser web, accedi al pannello di amministrazione di uno dei due router GL.iNet (ad esempio 192.168.8.1).
    2. Nella barra laterale sinistra, fai clic su **Network** > **LAN**.
    3. Nel campo **Router IP address**, inserisci un nuovo indirizzo IP LAN (ad esempio 192.168.10.1).
    4. Fai clic su **Apply**.

    **Possibile causa 4: l'indirizzo IP del server WireGuard è stato aggiornato ma manca la sottorete**

    Aggiungi una sottorete all'indirizzo IP del server WireGuard seguendo questi passaggi:

    1. In un browser web, inserisci l'URL del pannello di amministrazione del router GL.iNet (ad esempio 192.168.8.1) ed effettua l'accesso.
    2. Nella barra laterale sinistra, fai clic su **VPN** > **WireGuard Server**.
    3. Nella scheda **Configuration**, nel campo **IPv4 Address**, aggiungi **/24** dopo **10.0.0.1**.
    4. Fai clic su **Apply**.

#### Situazione 3: il server WireGuard è in esecuzione ma non riesco a connettere il client VPN

??? "Segui questi passaggi"

    Segui i passaggi indicati per ciascuna possibile causa qui sotto e controlla se il problema è risolto. Se il problema si risolve, puoi saltare il resto della sezione.

    **Possibile causa 1: il port forwarding configurato sul router principale potrebbe non funzionare correttamente**

    Per verificare se il port forwarding funziona correttamente, prova a inoltrare la porta HTTPS al server WireGuard seguendo i passaggi descritti nella Situazione 1.

    **Possibile causa 2: potresti non avere un indirizzo IP pubblico**

    Per verificarlo, consulta [questa pagina](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Possibile causa 3: se sia il server WireGuard sia il client WireGuard sono configurati su router GL.iNet, i loro indirizzi IP LAN sono in conflitto**

    Cambia l'indirizzo IP LAN su uno dei due router seguendo questi passaggi:

    1. In un browser web, accedi al pannello di amministrazione di uno dei router GL.iNet (ad esempio 192.168.8.1).
    2. Nella barra laterale sinistra, fai clic su **Network** > **LAN**.
    3. Nel campo **Router IP address**, inserisci un nuovo indirizzo IP LAN (ad esempio 192.168.10.1).
    4. Fai clic su **Apply**.

    **Possibile causa 4: il dispositivo che usi per connetterti al server WireGuard è collegato alla sua rete Wi-Fi o alla sua porta LAN**

    Collega il dispositivo a una rete Wi-Fi diversa oppure alla rete cellulare.

    **Possibile causa 5: nel file di configurazione caricato sul dispositivo client potrebbero mancare alcune righe**

    Carica di nuovo le informazioni di configurazione.

#### Situazione 4: il server WireGuard è connesso ma la connessione non è stabile

??? "Segui questi passaggi"

    Segui i passaggi riportati di seguito per risolvere il problema. Dopo ogni passaggio, controlla se il problema è risolto. Se il problema si risolve, puoi saltare i passaggi restanti.

    1. Sul dispositivo client VPN, cambia l'MTU da **1420** a un valore più basso (ad esempio **1380**).
    2. Sul router principale, abilita la funzione VPN passthrough se disponibile.
    3. Prova a configurare manualmente i server DNS sul router GL.iNet seguendo questi passaggi:
        1. In un browser web, inserisci l'URL del pannello di amministrazione del router GL.iNet (ad esempio 192.168.8.1) ed effettua l'accesso.
        2. Nella barra laterale sinistra, fai clic su **Network** > **DNS**.
        3. Per **Mode**, seleziona **Manual DNS**.
        4. Per **DNS Server 1**, seleziona **Google Public DNS**.
        5. Fai clic su **Apply**.

#### Situazione 5: il server WireGuard ha smesso improvvisamente di funzionare

??? "Segui questi passaggi"

    Segui i passaggi indicati per ciascuna possibile causa qui sotto e controlla se il problema è risolto. Se il problema si risolve, puoi saltare il resto della sezione.

    **Possibile causa 1: potrebbe essersi verificata un'interruzione di corrente nel luogo in cui hai configurato il server WireGuard**

    Controlla se il server WireGuard è ancora online seguendo i passaggi di verifica della Situazione 1 oppure tramite [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/) (se hai collegato in precedenza il router).

    **Possibile causa 2: non hai abilitato il Dynamic DNS (DDNS)**

    Se hai un indirizzo IP dinamico (come nella maggior parte dei casi), devi abilitare il DDNS. [Abilita DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) e segui il resto dei passaggi per configurare di nuovo il server WireGuard.

    **Possibile causa 3: il port forwarding ha smesso di funzionare per motivi sconosciuti**

    Configura di nuovo il [port forwarding](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) usando un'altra porta.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
