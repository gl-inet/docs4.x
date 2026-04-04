# Ottenere i log del modulo

Alcuni router GL.iNet integrano moduli 3G/4G/5G. Quando la connessione di rete e' instabile, puo' essere necessario esportare il log del modulo per analizzarlo.

Di seguito trovi i passaggi per esportare il log del modulo cellulare.

## 1. Collega il computer al router

Collega un laptop al Wi-Fi del router, trovi SSID e password sull'etichetta nella parte inferiore del dispositivo, oppure collega la porta Ethernet del computer alla porta LAN del router tramite un cavo Ethernet.

## 2. Accedi al router tramite SSH

Fai riferimento a [questo link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Ottenere i log del modulo

### Per GL-XE300/GL-X750/GL-X300B

1. Usa i seguenti comandi per ottenere qlog dal server GL.iNet e conferma che lo SHA256 del file qlog sia corretto.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. Inserisci una chiavetta USB e usa il comando `df` per ottenere il percorso di mount; ricordalo.

    Il percorso di mount della mia chiavetta USB e' `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Usa il seguente comando per aprire la modalita' debug del modulo.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Usa il seguente comando per avviare qlog.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

    `/tmp/mountd/disk1_part1` e' il percorso della mia chiavetta USB; devi sostituirlo con il tuo percorso.

5. Usa il seguente comando per riavviare il modulo.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Attendi da 1 a 3 minuti, poi usa il seguente comando per fermare qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. Troverai una directory nella chiavetta USB contenente alcuni file. Questi file sono dati acquisiti da qlog e devono essere decodificati con lo strumento Quectel, quindi inviali al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### Per GL-X3000/GL-XE3000

1. Inserisci una chiavetta USB e usa il comando `df` per ottenere il percorso di mount; ricordalo.

    Il percorso di mount della mia chiavetta USB e' `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Ottieni qlog dal server GL.iNet e conferma che lo sha256 del file qlog sia corretto.

    Usa i seguenti comandi per ottenere qlog.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4  && sha256sum qlog-mtk7981a-sha256-78dda4 && sha256sum /etc/default_v15.cfg
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_get_qlog.png){class="glboxshadow"}

3. Usa il seguente comando per avviare qlog.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Usa il seguente comando per riavviare il modulo.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Dopo aver catturato i pacchetti con qlog, usa il seguente comando per fermare qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. Troverai una directory nella chiavetta USB contenente alcuni file. Questi file sono dati acquisiti da qlog e devono essere decodificati con lo strumento Quectel, quindi inviali al supporto tecnico GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
