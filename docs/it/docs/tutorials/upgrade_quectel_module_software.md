# Aggiornare il firmware del modulo Quectel

## Preparazione

1. Assicurati che il router abbia accesso a Internet.

2. Collega un computer o un laptop al router tramite Wi-Fi o cavo Ethernet.

## Passaggi di aggiornamento

### Per GL-X3000/GL-XE3000

**Metodo 1. Aggiornamento tramite GUI GL.iNet**

1. Scarica il firmware del modulo corrispondente dal fondo di questo tutorial.

2. Accedi al pannello di amministrazione web del router, vai su **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** e carica il firmware del modulo, in formato `.zip`.

    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

**Metodo 2. Aggiornamento tramite SSH**

Prendiamo come esempio l'aggiornamento del modulo RM520N.

1. Accedi al router tramite SSH. Fai riferimento a [questo link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Inserisci il comando seguente per scaricare il firmware del modulo.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Inserisci il comando seguente per decomprimere il firmware del modulo.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Aggiorna il firmware del modulo usando il comando QFirehose, come mostrato sotto.

    **Nota**: sostituisci `/RM520NGLAAR03A03M4G_01.201.01201` con il percorso reale della cartella del firmware del modulo.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Attendi alcuni minuti. Quando l'aggiornamento e completato, il sistema mostrera il messaggio `Upgrade module successfully`.

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Riavvia il router, quindi accedi nuovamente al router tramite SSH.

7. Esegui il comando seguente per confermare ulteriormente che l'aggiornamento del modulo e riuscito.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Per GL-MiFi/GL-XE300/GL-X750/GL-E750

Prendiamo come esempio l'aggiornamento del modulo EM060K.

1. Prepara una chiavetta USB. Scarica il firmware del modulo corrispondente dal fondo di questo tutorial sulla chiavetta USB, poi decomprimi il file `.zip` e posizionalo nella directory principale dell'unita USB.

2. Inserisci la chiavetta USB nel router. Quindi fai riferimento a [questo link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) per accedere al router tramite SSH.

3. Inserisci il comando `df - h` per controllare il percorso di montaggio dell'unita USB e annota il percorso.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Inserisci il comando `ls -l` per controllare la cartella del firmware del modulo.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Inserisci il comando seguente per ottenere QFirehose dal server GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Poi assegna i permessi di esecuzione.

    ```
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Aggiorna il firmware del modulo usando il comando QFirehose, come mostrato sotto.

    **Nota**: sostituisci `/mnt/sdb1/EM060KGLAAR01A12M2GA` con il percorso reale della cartella del firmware del modulo.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Attendi alcuni minuti. Quando l'aggiornamento e completato, il sistema mostrera il messaggio `Upgrade module successfully`.

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Riavvia il router, quindi accedi nuovamente al router tramite SSH.

9. Esegui il comando seguente per confermare ulteriormente che l'aggiornamento del modulo e riuscito.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## URL di download del firmware del modulo Quectel

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
