# Modemprotokolle mit qlog erfassen {#how-to-use-qlog-to-capture-modem-logs}

Einige GL.iNet-Router verfügen über integrierte 3G/4G/5G-Modems. Bei instabiler Netzwerkverbindung kann es erforderlich sein, die Modemprotokolle zur Analyse zu exportieren.

Im Folgenden wird beschrieben, wie Sie die Protokolle des Mobilfunkmodems exportieren.

## 1. Verbinden Sie Ihren Computer mit dem Router {#1-connect-your-computer-to-the-router}

Verbinden Sie einen Laptop mit dem WLAN des Routers (SSID und Passwort finden Sie auf dem Etikett an der Unterseite des Geräts) oder verbinden Sie den Ethernet-Port Ihres Computers per Ethernet-Kabel mit dem LAN-Port des Routers.

## 2. Melden Sie sich per SSH an Ihrem Router an {#2-ssh-log-in-to-your-router}

Bitte beachten Sie [diesen Link](ssh_log_in_to_the_router.md).

## 3. Modemprotokolle abrufen {#3-get-modem-logs}

Wählen Sie die für Ihr Gerätemodell geeigneten Schritte aus.

### GL-E5800 {#gl-e5800}

1. Schließen Sie einen USB-Stick an und führen Sie `df -h` aus, um den Einhängepfad zu ermitteln. Notieren Sie diesen Pfad.

    Im folgenden Beispiel ist der USB-Stick unter `/tmp/mountd/disk1_part1` eingehängt.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Laden Sie die cfg-Konfigurationsdatei herunter.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Führen Sie den folgenden Befehl aus, um die Modemprotokollerfassung zu starten. Ersetzen Sie `/tmp/mountd/disk1_part1` durch den tatsächlichen Einhängepfad Ihres USB-Sticks.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Starten Sie das Modem neu. Ersetzen Sie `<sim_slot>` durch die Nummer des aktuell aktiven SIM-Kartensteckplatzes (`1` oder `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Beispiel für eine aktive SIM-Karte **1**:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Warten Sie 3 Minuten und führen Sie dann den folgenden Befehl aus, um qlog zu beenden.

    ```
    diag_mdlog -k
    ```

6. Auf dem USB-Stick finden Sie einen Ordner mit den von qLog erfassten Daten. Zum Dekodieren dieser Dateien ist das Quectel-Tool erforderlich. Senden Sie die Dateien an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Schließen Sie einen USB-Stick an und führen Sie `df -h` aus, um den Einhängepfad zu ermitteln. Notieren Sie diesen Pfad.

    Im folgenden Beispiel ist der USB-Stick unter `/tmp/mountd/disk1_part1` eingehängt.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Laden Sie die cfg-Konfigurationsdatei herunter.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Laden Sie das qlog-Tool herunter.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Führen Sie den folgenden Befehl aus, um qlog zu starten. Ersetzen Sie `/tmp/mountd/disk1_part1` durch den tatsächlichen Einhängepfad Ihres USB-Sticks.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Starten Sie das Modem neu.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Warten Sie 3 Minuten und führen Sie dann den folgenden Befehl aus, um qlog zu beenden.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Auf dem USB-Stick finden Sie einen Ordner mit den von qLog erfassten Daten. Zum Dekodieren dieser Dateien ist das Quectel-Tool erforderlich. Senden Sie die Dateien an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Schließen Sie einen USB-Stick an und führen Sie `df -h` aus, um den Einhängepfad zu ermitteln. Notieren Sie diesen Pfad.

    Im folgenden Beispiel ist der USB-Stick unter `/tmp/mountd/disk1_part1` eingehängt.

    ![Pfad des USB-Sticks](https://static.gl-inet.com/docs/router/de/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Führen Sie die folgenden Befehle aus, um qlog vom GL.iNet-Server herunterzuladen.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Führen Sie den folgenden Befehl aus, um den Debug-Modus des Modems zu aktivieren.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Führen Sie den folgenden Befehl aus, um qlog zu starten. Ersetzen Sie `/tmp/mountd/disk1_part1` durch den tatsächlichen Einhängepfad Ihres USB-Sticks.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Starten Sie das Modem neu.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Warten Sie 3 Minuten und führen Sie dann den folgenden Befehl aus, um qlog zu beenden.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Auf dem USB-Stick finden Sie einen Ordner mit den von qLog erfassten Daten. Zum Dekodieren dieser Dateien ist das Quectel-Tool erforderlich. Senden Sie die Dateien an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs-Dateien](https://static.gl-inet.com/docs/router/de/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Schließen Sie einen USB-Stick an und führen Sie `df -h` aus, um den Einhängepfad zu ermitteln. Notieren Sie diesen Pfad.

    Im folgenden Beispiel ist der USB-Stick unter `/tmp/mountd/disk1_part1` eingehängt.

    ![Pfad des USB-Sticks](https://static.gl-inet.com/docs/router/de/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Führen Sie die folgenden Befehle aus, um qlog vom GL.iNet-Server herunterzuladen.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Führen Sie den folgenden Befehl aus, um qlog zu starten. Ersetzen Sie `/tmp/mountd/disk1_part1` durch den tatsächlichen Einhängepfad Ihres USB-Sticks.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Starten Sie das Modem neu.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Warten Sie 3 Minuten und führen Sie dann den folgenden Befehl aus, um qlog zu beenden.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Auf dem USB-Stick finden Sie einen Ordner mit den von qLog erfassten Daten. Zum Dekodieren dieser Dateien ist das Quectel-Tool erforderlich. Senden Sie die Dateien an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs-Dateien](https://static.gl-inet.com/docs/router/de/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
