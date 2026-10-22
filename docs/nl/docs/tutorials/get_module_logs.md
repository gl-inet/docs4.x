# Modemlogboeken vastleggen met qlog {#how-to-use-qlog-to-capture-modem-logs}

Sommige GL.iNet-routers hebben een ingebouwde 3G/4G/5G-modem. Als de netwerkverbinding instabiel is, kan het nodig zijn de logboeken van de modem voor analyse te exporteren.

Volg deze stappen om de logboeken van de cellulaire modem te exporteren.

## 1. Je computer met de router verbinden {#1-connect-your-computer-to-the-router}

Verbind een laptop met het Wi-Fi-netwerk van de router. Je vindt de SSID en het wachtwoord op het label aan de onderkant van het apparaat. Je kunt de ethernetpoort van je computer ook met een ethernetkabel op de LAN-poort van de router aansluiten.

## 2. Via SSH aanmelden bij je router {#2-ssh-log-in-to-your-router}

Raadpleeg [deze handleiding](ssh_log_in_to_the_router.md).

## 3. Modemlogboeken ophalen {#3-get-modem-logs}

Selecteer de stappen voor je apparaatmodel.

### GL-E5800 {#gl-e5800}

1. Plaats een USB-stick, voer `df -h` uit om het koppelpad te bepalen en noteer dit.

    In het volgende voorbeeld is de USB-stick gekoppeld aan `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Download het cfg-configuratiebestand.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Voer de volgende opdracht uit om het vastleggen van modemlogboeken te starten. Vervang `/tmp/mountd/disk1_part1` door het werkelijke koppelpad van je USB-stick.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Start de modem opnieuw op. Vervang `<sim_slot>` door het nummer van de momenteel actieve simkaartsleuf (`1` of `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Als bijvoorbeeld simkaart **1** actief is:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Wacht 3 minuten en voer de volgende opdracht uit om qlog te stoppen.

    ```
    diag_mdlog -k
    ```

6. Op de USB-stick staat nu een map met bestanden met vastgelegde qLog-gegevens. Voor het decoderen is het Quectel-hulpprogramma vereist. Stuur deze bestanden naar de technische ondersteuning van GL.iNet of Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Plaats een USB-stick, voer `df -h` uit om het koppelpad te bepalen en noteer dit.

    In het volgende voorbeeld is de USB-stick gekoppeld aan `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Download het cfg-configuratiebestand.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Download het qlog-hulpprogramma.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Voer de volgende opdracht uit om qlog te starten. Vervang `/tmp/mountd/disk1_part1` door het werkelijke koppelpad van je USB-stick.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Start de modem opnieuw op.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Wacht 3 minuten en voer de volgende opdracht uit om qlog te stoppen.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Op de USB-stick staat nu een map met bestanden met vastgelegde qLog-gegevens. Voor het decoderen is het Quectel-hulpprogramma vereist. Stuur deze bestanden naar de technische ondersteuning van GL.iNet of Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Plaats een USB-stick, voer `df -h` uit om het koppelpad te bepalen en noteer dit.

    In het volgende voorbeeld is de USB-stick gekoppeld aan `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Voer de volgende opdrachten uit om qlog van de GL.iNet-server te downloaden.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Voer de volgende opdracht uit om de foutopsporingsmodus van de modem in te schakelen.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Voer de volgende opdracht uit om qlog te starten. Vervang `/tmp/mountd/disk1_part1` door het werkelijke koppelpad van je USB-stick.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Start de modem opnieuw op.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Wacht 3 minuten en voer de volgende opdracht uit om qlog te stoppen.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Op de USB-stick staat nu een map met bestanden met vastgelegde qLog-gegevens. Voor het decoderen is het Quectel-hulpprogramma vereist. Stuur deze bestanden naar de technische ondersteuning van GL.iNet of Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Plaats een USB-stick, voer `df -h` uit om het koppelpad te bepalen en noteer dit.

    In het volgende voorbeeld is de USB-stick gekoppeld aan `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Voer de volgende opdrachten uit om qlog van de GL.iNet-server te downloaden.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Voer de volgende opdracht uit om qlog te starten. Vervang `/tmp/mountd/disk1_part1` door het werkelijke koppelpad van je USB-stick.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Start de modem opnieuw op.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Wacht 3 minuten en voer de volgende opdracht uit om qlog te stoppen.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Op de USB-stick staat nu een map met bestanden met vastgelegde qLog-gegevens. Voor het decoderen is het Quectel-hulpprogramma vereist. Stuur deze bestanden naar de technische ondersteuning van GL.iNet of Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
