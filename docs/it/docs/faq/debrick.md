# Usare Uboot per sbloccare il router

Se hai bloccato il router a causa di alcuni progetti fai-da-te o del caricamento di un firmware errato, potresti non riuscire più ad accedervi. In questo caso, puoi reinstallare il firmware usando la modalità failsafe U-Boot.

**Nota:** l'operazione U-Boot rimuoverà le impostazioni del router e i plugin installati.

---

## Preparazione

Prepara un computer con una porta Ethernet. Se il computer non dispone di una porta Ethernet, prepara un adattatore USB Ethernet aggiuntivo.

**Nota**: GL-E5800 (Mudi 7) al momento non supporta il flashing del firmware tramite U-Boot.

## Passaggi per lo sblocco

Fai riferimento a questo video tutorial oppure segui la procedura riportata di seguito per accedere all'interfaccia web U-Boot e reinstallare il firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>I passaggi per reinstallare il firmware usando U-Boot sono in gran parte gli stessi; questo video usa Mudi/Mudi V2 come esempio. Per altri modelli, puoi seguire la procedura qui sotto.</small>

1. Scarica il firmware U-Boot [qui](https://dl.gl-inet.com/){target="_blank"} sul computer.

    Alcuni modelli offrono due varianti di firmware. Scarica il firmware compatibile con U-Boot.

2. Scollega l'alimentazione del router. Collega il computer alla **porta Ethernet LAN** del router. **TUTTE** le altre porte devono rimanere **scollegate**.

    !!! note

        Per alcuni modelli, alcune singole porte LAN e la porta WAN sono intercambiabili. Non usare questa porta LAN. Ad esempio, su GL-MT6000 (Flint 2), non usare LAN 1. Usa invece LAN 2, LAN 3 o LAN 4.

3. Tieni premuto con decisione il pulsante Reset e **allo stesso tempo accendi il router**. Se il router non ha un pulsante di alimentazione, collegare l'alimentazione lo accenderà automaticamente.

    Vedrai quindi il LED lampeggiare in una sequenza regolare alcune volte; rilascia il dito **dopo** che la sequenza cambia.

    !!! note "Sequenze di lampeggiamento LED per modello"

        **Nota:** modelli identici ma prodotti in lotti diversi possono avere colori dei LED o sequenze di lampeggiamento differenti. Questo non influisce sul processo di recupero U-Boot. Presta soprattutto attenzione al cambiamento dello stato del LED.

        - Per **GL-MT3600BE (Beryl 7)**: il LED blu lampeggia 7 volte, poi diventa bianco fisso.

        - Per **GL-MT5000 (Brume 3)**: il LED Power lampeggia in blu 7 volte, poi diventa bianco fisso.

        - Per **GL-BE6500 (Flint 3e)**: il LED blu lampeggia 6 volte, poi diventa bianco fisso.

        - Per **GL-BE9300 (Flint 3)**: il LED blu lampeggia 6 volte, poi diventa bianco fisso.

        - Per **GL-BE3600 (Slate 7)**: dopo aver tenuto premuto il pulsante Reset per circa 5 secondi, sul touchscreen apparirà un conto alla rovescia di 5 secondi. Continua a tenerlo premuto finché sullo schermo non compare il messaggio successivo, ad esempio di impostare manualmente l'IP del computer su 192.168.1.2 e visitare http://192.168.1.1 con il browser. Passa al passaggio 4 per ulteriori istruzioni.

        - Per **GL-X2000 (Spitz Plus)**: il LED Internet lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-B3000 (Marble)**: il LED blu lampeggia 7 volte, poi diventa bianco fisso.

        - Per **GL-MT6000 (Flint 2)**: il LED blu lampeggia 6 volte, poi diventa bianco fisso.

        - Per **GL-MT3000 (Beryl AX)**: il LED blu lampeggia 6 volte, poi diventa bianco fisso.

        - Per **GL-MT2500/GL-MT2500A (Brume 2)**: il LED Power lampeggia in blu 5 volte, poi diventa bianco fisso.

        - Per **GL-X3000 (Spitz AX)**: il LED Internet lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-XE3000 (Puli AX)**: il LED Internet lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-XE300 (Puli)**: il LED LAN lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-E750 (Mudi)**: sullo schermo appariranno in sequenza "Booting", poi "Reset Counting 1 to 4" e infine "Please Open Web 192.168.1.1".

        - Per **GL-X750 (Spitz)**: il LED Internet lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-AX1800 (Flint)**: il LED blu lampeggia 5 volte, poi diventa bianco fisso.

        - Per **GL-AXT1800 (Slate AX)**: il LED blu lampeggia 5 volte, poi diventa bianco fisso.

        - Per **GL-SFT1200 (Opal)**: il LED blu lampeggia 5 volte, poi diventa bianco fisso.

        - Per **GL-MT1300 (Beryl)**: il LED blu lampeggia due volte lentamente, poi lampeggia 5 volte più velocemente e diventa bianco fisso.

        - Per **GL-A1300 (Slate Plus)**: il LED lampeggia lentamente 5 volte, rimane acceso per un breve periodo e poi lampeggia rapidamente in continuazione.

        - Per **GL-MT300N-V2 (Mango)** e **GL-AR300M (Shadow)**: il LED lampeggia 5 volte.

        - Per **GL-X300B (Collie)**: il LED WAN lampeggia 5 volte, poi il LED Wi-Fi rimane acceso.

        - Per **GL-AP1300 (Cirrus)**: il LED Power lampeggia lentamente 5 volte, rimane acceso per un breve periodo e poi lampeggia rapidamente in continuazione.

        - Per **GL-B1300 (Convexa-B)** e **GL-S1300 (Convexa-S, EOL)**: il LED lampeggia 4 volte.

            Il LED Power più a sinistra rimane acceso per tutto il tempo, mentre il LED Wi-Fi più a destra lampeggia 4 volte, poi il LED Mesh centrale rimane acceso fisso.

            Per alcuni vecchi GL-B1300, il LED Power più a sinistra rimane acceso per tutto il tempo e sia il LED centrale sia quello più a destra lampeggiano 5 volte contemporaneamente, poi restano accesi.

        - Per **GL-B2200 (Velica)**: i due LED partono blu, poi diventano bianchi e lampeggiano 5 volte, quindi tornano blu fissi.

        - Per **GL-SF1200**: il LED 5G lampeggia 5 volte, poi resta acceso fisso.

        - Per **GL-S200**: il LED ciano lampeggia 5 volte, poi diventa brevemente viola e infine ciano fisso.

        - Per **GL-AR750 (Creta)** e **GL-AR750S-EXT (Slate)**: il LED lampeggia 5 volte.

        - Per **GL-USB150 (Microuter)**, **microuter-N300** e **GL-AR150 (White)**: il LED lampeggia 5 volte.

        - Per **GL-MV1000/GL-MV1000W (Brume)**: non c'è una sequenza LED ripetuta di lampeggio. I LED Power e WAN restano accesi per tutto il tempo.

        - Per **GL-MiFi**: il LED lampeggia 6 volte.

        - Per **GL-MT300N** e **GL-MT300A**: il LED lampeggia 3 volte.

4. Imposta manualmente l'indirizzo IP del computer su **192.168.1.2**. Consulta la guida dettagliata per i diversi sistemi operativi qui sotto:

    ??? "Windows 7 / Windows 10"

        1. Vai su **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Fai clic con il tasto destro su **Local Area Connection** -> **Properties**.

        3. Fai clic su **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Imposta manualmente **IP address** su `192.168.1.2`.

        5. Imposta **Subnet mask** su `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Fai clic sul pulsante **OK**.

    ??? "Windows 11"

        7. Apri Settings.

        8. Fai clic su **Network & Internet**.

        9. Fai clic sulla scheda **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Nella sezione "IP assignment", fai clic sul pulsante **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Seleziona l'opzione **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Attiva l'interruttore **IPv4**.

        13. Imposta l'**IP address** statico su **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Specifica **Subnet mask** come **255.255.255.0**.

        15. Fai clic sul pulsante **Save**.

    ??? "macOS"

        16. Fai clic sull'icona **Apple** in alto a sinistra dello schermo e seleziona **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Fai clic su **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Fai clic su **Ethernet** a sinistra e poi sulla casella a discesa accanto a **Configure IPv4**, quindi seleziona **Manually**. Se stai usando un adattatore USB Ethernet, Ethernet potrebbe non essere visibile e potrebbe comparire invece il nome dell'adattatore USB Ethernet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Inserisci **IPv4 Address** come `192.168.1.2`, **Subnet Mask** come `255.255.255.0`, **Router** come `192.168.1.1`, quindi fai clic sul pulsante Apply in basso a destra.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Usa il browser per visitare **http://192.168.1.1**. Questa è la U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note

        - Se non riesci ad accedere alla U-Boot Web UI, controlla se sono in esecuzione software VPN o proxy. Disabilita eventuali software VPN o proxy, inclusi Tailscale e ZeroTier.

        - La U-Boot Web UI mostrata sopra potrebbe non essere esattamente uguale a quella che vedi, perché la versione di U-Boot varia a seconda della data di produzione. In alcuni casi estremi, consigliamo di aggiornare la versione di U-Boot. Fai riferimento al tutorial [qui](upgrade_uboot_version.md).

6. Fai clic sul pulsante **Choose file** per individuare il file del firmware. Poi fai clic sul pulsante **Update firmware**.

7. Attendi circa 3 minuti. Non spegnere il dispositivo durante l'aggiornamento del firmware.

    Il router è pronto quando il LED continua a lampeggiare in blu; per alcuni modelli cellulari, è pronto quando sia il LED Power sia il LED Wi-Fi rimangono accesi fissi.

8. Ripristina le impostazioni IP modificate al passaggio 4 e collega il dispositivo alla LAN o al Wi-Fi del router. Potrai nuovamente accedere al router tramite **192.168.8.1**.

    **Nota:** potrebbe essere necessario usare la modalità in incognito oppure eliminare cache e cookie del browser per accedere al router.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
