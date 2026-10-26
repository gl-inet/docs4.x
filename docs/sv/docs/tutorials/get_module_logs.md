# Så använder du qlog för att registrera modemloggar {#how-to-use-qlog-to-capture-modem-logs}

Vissa GL.iNet-routrar har inbyggda 3G/4G/5G-modem. Om nätverksanslutningen är instabil kan du behöva exportera modemets loggar för analys.

Följ stegen nedan för att exportera mobilmodemets loggar.

## 1. Anslut datorn till routern {#1-connect-your-computer-to-the-router}

Anslut en bärbar dator till routerns Wi-Fi (SSID och lösenord finns på etiketten på enhetens undersida), eller anslut datorns Ethernet-port till routerns LAN-port med en Ethernet-kabel.

## 2. Logga in på routern via SSH {#2-ssh-log-in-to-your-router}

Se [den här länken](ssh_log_in_to_the_router.md).

## 3. Hämta modemloggar {#3-get-modem-logs}

Välj stegen för din enhetsmodell.

### GL-E5800 {#gl-e5800}

1. Sätt i ett USB-minne, kör `df -h` för att hämta monteringssökvägen och anteckna den.

    USB-minnet i följande exempel är monterat på `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Ladda ned cfg-konfigurationsfilen.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Kör följande kommando för att börja registrera modemloggen. Ersätt `/tmp/mountd/disk1_part1` med USB-minnets faktiska monteringssökväg.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Starta om modemet. Ersätt `<sim_slot>` med numret på den SIM-kortplats som är aktiv (`1` eller `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Om SIM-kort **1** är aktivt:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Vänta i 3 minuter och kör sedan följande kommando för att stoppa qlog.

    ```
    diag_mdlog -k
    ```

6. På USB-minnet finns nu en mapp med filer som innehåller registrerade qLog-data. De måste avkodas med Quectels verktyg. Skicka filerna till GL.iNets eller Quectels tekniska support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Sätt i ett USB-minne, kör `df -h` för att hämta monteringssökvägen och anteckna den.

    USB-minnet i följande exempel är monterat på `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Ladda ned cfg-konfigurationsfilen.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Ladda ned qlog-verktyget och ge det körbehörighet.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Kör följande kommando för att starta qlog. Ersätt `/tmp/mountd/disk1_part1` med USB-minnets faktiska monteringssökväg.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Starta om modemet.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Vänta i 3 minuter och kör sedan följande kommando för att stoppa qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. På USB-minnet finns nu en mapp med filer som innehåller registrerade qLog-data. De måste avkodas med Quectels verktyg. Skicka filerna till GL.iNets eller Quectels tekniska support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}

### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Sätt i ett USB-minne, kör `df -h` för att hämta monteringssökvägen och anteckna den.

    USB-minnet i följande exempel är monterat på `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Kör följande kommandon för att ladda ned qlog från GL.iNets server och ge filen körbehörighet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Kör följande kommando för att aktivera modemets felsökningsläge.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Kör följande kommando för att starta qlog. Ersätt `/tmp/mountd/disk1_part1` med USB-minnets faktiska monteringssökväg.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Starta om modemet.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Vänta i 3 minuter och kör sedan följande kommando för att stoppa qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. På USB-minnet finns nu en mapp med filer som innehåller registrerade qLog-data. De måste avkodas med Quectels verktyg. Skicka filerna till GL.iNets eller Quectels tekniska support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Sätt i ett USB-minne, kör `df -h` för att hämta monteringssökvägen och anteckna den.

    USB-minnet i följande exempel är monterat på `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Kör följande kommandon för att ladda ned qlog från GL.iNets server och ge filen körbehörighet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Kör följande kommando för att starta qlog. Ersätt `/tmp/mountd/disk1_part1` med USB-minnets faktiska monteringssökväg.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Starta om modemet.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Vänta i 3 minuter och kör sedan följande kommando för att stoppa qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. På USB-minnet finns nu en mapp med filer som innehåller registrerade qLog-data. De måste avkodas med Quectels verktyg. Skicka filerna till GL.iNets eller Quectels tekniska support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
