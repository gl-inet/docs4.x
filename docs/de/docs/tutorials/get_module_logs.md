# Modulprotokolle abrufen

Einige GL.iNet-Router sind mit integrierten 3G-/4G-/5G-Modulen ausgestattet. Wenn die Netzwerkverbindung instabil ist, kann es erforderlich sein, die Protokolle des Moduls zur Analyse zu exportieren.

Im Folgenden finden Sie die Schritte zum Exportieren der Protokolle des Mobilfunkmoduls.

## 1. Verbinden Sie Ihren Computer mit dem Router

Verbinden Sie einen Laptop mit dem WLAN des Routers (SSID und Passwort finden Sie auf dem Etikett an der Unterseite des Geräts) oder verbinden Sie den Ethernet-Port Ihres Computers per Ethernet-Kabel mit dem LAN-Port des Routers.

## 2. Melden Sie sich per SSH an Ihrem Router an

Bitte beachten Sie [diesen Link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Modulprotokolle abrufen

### Für GL-XE300/GL-X750/GL-X300B

1. Verwenden Sie die folgenden Befehle, um qlog vom GL.iNet-Server herunterzuladen, und prüfen Sie, ob die SHA256-Prüfsumme der qlog-Datei korrekt ist.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Qlog abrufen](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. Stecken Sie einen USB-Stick ein und verwenden Sie den Befehl `df`, um den Einhängepfad zu ermitteln. Merken Sie sich diesen Pfad.

    Der Einhängepfad meines USB-Sticks ist `/tmp/mountd/disk1_part1`

    ![Pfad des USB-Sticks](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Verwenden Sie den folgenden Befehl, um den Debug-Modus des Moduls zu aktivieren.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Verwenden Sie den folgenden Befehl, um qlog zu starten.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    `/tmp/mountd/disk1_part1` ist der Pfad meines USB-Sticks. Sie müssen ihn durch Ihren eigenen Pfad ersetzen.

5. Verwenden Sie den folgenden Befehl, um das Modul neu zu starten.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Warten Sie 1 bis 3 Minuten und verwenden Sie dann den folgenden Befehl, um qlog zu stoppen.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Qlog starten und stoppen](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. Auf dem USB-Stick finden Sie anschließend ein Verzeichnis mit mehreren Dateien. Diese Dateien sind die von qlog erfassten Daten und müssen mit einem Quectel-Tool decodiert werden. Senden Sie diese Dateien daher bitte an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs-Dateien](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### Für GL-X3000/GL-XE3000

1. Stecken Sie einen USB-Stick ein und verwenden Sie den Befehl `df`, um den Einhängepfad zu ermitteln. Merken Sie sich diesen Pfad.

    Der Einhängepfad meines USB-Sticks ist `/tmp/mountd/disk1_part1`

    ![Pfad des USB-Sticks](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Laden Sie qlog vom GL.iNet-Server herunter und prüfen Sie, ob die SHA256-Prüfsumme der qlog-Datei korrekt ist.

    Verwenden Sie die folgenden Befehle, um qlog herunterzuladen.
    
    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    
    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4  && sha256sum qlog-mtk7981a-sha256-78dda4 && sha256sum /etc/default_v15.cfg
    ```

    ![Qlog abrufen](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_get_qlog.png){class="glboxshadow"}

3. Verwenden Sie den folgenden Befehl, um qlog zu starten.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```
    
4. Verwenden Sie den folgenden Befehl, um das Modul neu zu starten.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Nachdem qlog Pakete erfasst hat, verwenden Sie den folgenden Befehl, um qlog zu stoppen.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Qlog starten und stoppen](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. Auf dem USB-Stick finden Sie anschließend ein Verzeichnis mit mehreren Dateien. Diese Dateien sind die von qlog erfassten Daten und müssen mit einem Quectel-Tool decodiert werden. Senden Sie diese Dateien daher bitte an den technischen Support von GL.iNet oder Quectel.

    ![Qlogs-Dateien](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
