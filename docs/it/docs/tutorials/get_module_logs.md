# Come usare qlog per acquisire i log del modem {#how-to-use-qlog-to-capture-modem-logs}

Alcuni router GL.iNet sono dotati di modem 3G/4G/5G integrati. Quando la connessione di rete è instabile, potrebbe essere necessario esportare i log del modem per analizzarli.

Di seguito sono riportati i passaggi per esportare i log del modem cellulare.

## 1. Collega il computer al router {#1-connect-your-computer-to-the-router}

Collega un laptop al Wi-Fi del router, trovi SSID e password sull'etichetta nella parte inferiore del dispositivo, oppure collega la porta Ethernet del computer alla porta LAN del router tramite un cavo Ethernet.

## 2. Accedi al router tramite SSH {#2-ssh-log-in-to-your-router}

Fai riferimento a [questo link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Acquisisci i log del modem {#3-get-modem-logs}

Segui i passaggi appropriati per il modello del tuo dispositivo.

### GL-E5800 {#gl-e5800}

1. Inserisci un’unità flash USB, quindi esegui `df -h` per individuare il percorso di montaggio e annotalo.

    Nell’esempio seguente, l’unità flash USB è montata in `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Scarica il file di configurazione cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Esegui il comando seguente per avviare l’acquisizione dei log del modem. Sostituisci `/tmp/mountd/disk1_part1` con il percorso di montaggio effettivo dell’unità flash USB.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Riavvia il modem. Sostituisci `<sim_slot>` con il numero dello slot della scheda SIM attualmente attiva (`1` o `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Ad esempio, se è attiva la scheda SIM **1**:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Attendi 3 minuti, quindi esegui il comando seguente per arrestare qlog.

    ```
    diag_mdlog -k
    ```

6. Sull’unità flash USB troverai una cartella contenente i file dei dati acquisiti da qLog, che richiedono lo strumento Quectel per la decodifica. Invia questi file al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Inserisci un’unità flash USB, quindi esegui `df -h` per individuare il percorso di montaggio e annotalo.

    Nell’esempio seguente, l’unità flash USB è montata in `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Scarica il file di configurazione cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Scarica lo strumento qlog.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Esegui il comando seguente per avviare qlog. Sostituisci `/tmp/mountd/disk1_part1` con il percorso di montaggio effettivo dell’unità flash USB.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Riavvia il modem.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Attendi 3 minuti, quindi esegui il comando seguente per arrestare qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Sull’unità flash USB troverai una cartella contenente i file dei dati acquisiti da qLog, che richiedono lo strumento Quectel per la decodifica. Invia questi file al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Inserisci un’unità flash USB, quindi esegui `df -h` per individuare il percorso di montaggio e annotalo.

    Nell’esempio seguente, l’unità flash USB è montata in `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Esegui i comandi seguenti per scaricare qlog dal server GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Esegui il comando seguente per abilitare la modalità di debug del modem.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Esegui il comando seguente per avviare qlog. Sostituisci `/tmp/mountd/disk1_part1` con il percorso di montaggio effettivo dell’unità flash USB.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Riavvia il modem.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Attendi 3 minuti, quindi esegui il comando seguente per arrestare qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Sull’unità flash USB troverai una cartella contenente i file dei dati acquisiti da qLog, che richiedono lo strumento Quectel per la decodifica. Invia questi file al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Inserisci un’unità flash USB, quindi esegui `df -h` per individuare il percorso di montaggio e annotalo.

    Nell’esempio seguente, l’unità flash USB è montata in `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Esegui i comandi seguenti per scaricare qlog dal server GL.iNet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Esegui il comando seguente per avviare qlog. Sostituisci `/tmp/mountd/disk1_part1` con il percorso di montaggio effettivo dell’unità flash USB.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Riavvia il modem.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Attendi 3 minuti, quindi esegui il comando seguente per arrestare qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Sull’unità flash USB troverai una cartella contenente i file dei dati acquisiti da qLog, che richiedono lo strumento Quectel per la decodifica. Invia questi file al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
