# Як записати журнали модема за допомогою qlog {#how-to-use-qlog-to-capture-modem-logs}

Деякі маршрутизатори GL.iNet мають вбудовані модеми 3G/4G/5G. Якщо мережеве з’єднання нестабільне, може знадобитися експорт журналів модема для аналізу.

Нижче описано експорт журналів стільникового модема.

## 1. Підключення комп’ютера до маршрутизатора {#1-connect-your-computer-to-the-router}

Підключіть ноутбук до Wi-Fi маршрутизатора (SSID і пароль зазначені на нижній етикетці) або з’єднайте порт Ethernet комп’ютера з портом LAN маршрутизатора кабелем Ethernet.

## 2. Вхід до маршрутизатора через SSH {#2-ssh-log-in-to-your-router}

Див. [цю інструкцію](ssh_log_in_to_the_router.md).

## 3. Отримання журналів модема {#3-get-modem-logs}

Виберіть відповідні кроки для моделі вашого пристрою.

### GL-E5800 {#gl-e5800}

1. Вставте USB-флешнакопичувач, визначте його точку монтування командою `df -h` і запишіть шлях.

    У цьому прикладі точка монтування USB-накопичувача — `/tmp/mountd/disk1_part1`.

    ![Точка монтування USB-накопичувача](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Завантажте файл конфігурації cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Виконайте наведену нижче команду, щоб розпочати запис журналів модема. Замініть `/tmp/mountd/disk1_part1` фактичним шляхом до точки монтування вашого USB-накопичувача.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Перезапустіть модем. Замініть `<sim_slot>` номером активного слота SIM-карти (`1` або `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Наприклад, якщо активна SIM-карта **1**:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Зачекайте 3 хвилини та виконайте наведену нижче команду, щоб зупинити qlog.

    ```
    diag_mdlog -k
    ```

6. На USB-накопичувачі з’явиться папка з даними, зібраними qLog. Для їхнього декодування потрібен інструмент Quectel. Надішліть ці файли службі технічної підтримки GL.iNet або Quectel.

    ![Файли журналів qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Вставте USB-флешнакопичувач, визначте його точку монтування командою `df -h` і запишіть шлях.

    У цьому прикладі точка монтування USB-накопичувача — `/tmp/mountd/disk1_part1`.

    ![Точка монтування USB-накопичувача](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Завантажте файл конфігурації cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![Завантаження файлу cfg](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Завантажте інструмент qlog.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![Завантаження інструмента qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Виконайте наведену нижче команду, щоб запустити qlog. Замініть `/tmp/mountd/disk1_part1` фактичним шляхом до точки монтування вашого USB-накопичувача.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Перезапустіть модем.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Зачекайте 3 хвилини та виконайте наведену нижче команду, щоб зупинити qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. На USB-накопичувачі з’явиться папка з даними, зібраними qLog. Для їхнього декодування потрібен інструмент Quectel. Надішліть ці файли службі технічної підтримки GL.iNet або Quectel.

    ![Файли журналів qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Вставте USB-флешнакопичувач, визначте його точку монтування командою `df -h` і запишіть шлях.

    У цьому прикладі точка монтування USB-накопичувача — `/tmp/mountd/disk1_part1`.

    ![Точка монтування USB-накопичувача](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Виконайте наведені нижче команди, щоб завантажити qlog із сервера GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Увімкніть режим налагодження модема такою командою:

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Виконайте наведену нижче команду, щоб запустити qlog. Замініть `/tmp/mountd/disk1_part1` фактичним шляхом до точки монтування вашого USB-накопичувача.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

5. Перезапустіть модем.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Зачекайте 3 хвилини та виконайте наведену нижче команду, щоб зупинити qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. На USB-накопичувачі з’явиться папка з даними, зібраними qLog. Для їхнього декодування потрібен інструмент Quectel. Надішліть ці файли службі технічної підтримки GL.iNet або Quectel.

    ![Файли журналів qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Вставте USB-флешнакопичувач, визначте його точку монтування командою `df -h` і запишіть шлях.

    У цьому прикладі точка монтування USB-накопичувача — `/tmp/mountd/disk1_part1`.

    ![Точка монтування USB-накопичувача](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Виконайте наведені нижче команди, щоб завантажити qlog із сервера GL.iNet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Виконайте наведену нижче команду, щоб запустити qlog. Замініть `/tmp/mountd/disk1_part1` фактичним шляхом до точки монтування вашого USB-накопичувача.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

4. Перезапустіть модем.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Зачекайте 3 хвилини та виконайте наведену нижче команду, щоб зупинити qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. На USB-накопичувачі з’явиться папка з даними, зібраними qLog. Для їхнього декодування потрібен інструмент Quectel. Надішліть ці файли службі технічної підтримки GL.iNet або Quectel.

    ![Файли журналів qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
