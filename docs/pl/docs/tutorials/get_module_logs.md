# Jak używać qlog do rejestrowania logów modemu {#how-to-use-qlog-to-capture-modem-logs}

Niektóre routery GL.iNet mają wbudowane modemy 3G/4G/5G. Gdy połączenie sieciowe jest niestabilne, może być konieczne wyeksportowanie logów modemu do analizy.

Poniżej opisano kroki eksportowania logów modemu komórkowego.

## 1. Podłącz komputer do routera {#1-connect-your-computer-to-the-router}

Podłącz laptop do sieci Wi-Fi routera (SSID i hasło znajdziesz na etykiecie u spodu urządzenia) lub podłącz port Ethernet komputera do portu LAN routera kablem Ethernet.

## 2. Zaloguj się do routera przez SSH {#2-ssh-log-in-to-your-router}

Zapoznaj się z [tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Pobierz logi modemu {#3-get-modem-logs}

Wybierz odpowiednią procedurę dla modelu swojego urządzenia.

### GL-E5800 {#gl-e5800}

1. Podłącz pamięć USB, a następnie uruchom `df -h`, aby sprawdzić ścieżkę montowania, i zapisz ją.

    W poniższym przykładzie pamięć USB jest zamontowana pod ścieżką `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Pobierz plik konfiguracyjny cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Uruchom poniższe polecenie, aby rozpocząć rejestrowanie logów modemu. Zastąp `/tmp/mountd/disk1_part1` rzeczywistą ścieżką montowania pamięci USB.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Uruchom modem ponownie. Zastąp `<sim_slot>` numerem aktualnie aktywnego gniazda karty SIM (`1` lub `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Na przykład, jeśli aktywna jest karta SIM **1**:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Poczekaj 3 minuty, a następnie uruchom poniższe polecenie, aby zatrzymać qlog.

    ```
    diag_mdlog -k
    ```

6. Na pamięci USB znajdziesz folder z plikami danych zarejestrowanych przez qLog. Do ich dekodowania wymagane jest narzędzie Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000 {#gl-x2000}

1. Podłącz pamięć USB, a następnie uruchom `df -h`, aby sprawdzić ścieżkę montowania, i zapisz ją.

    W poniższym przykładzie pamięć USB jest zamontowana pod ścieżką `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Pobierz plik konfiguracyjny cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Pobierz narzędzie qlog.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Uruchom poniższe polecenie, aby rozpocząć rejestrowanie przez qlog. Zastąp `/tmp/mountd/disk1_part1` rzeczywistą ścieżką montowania pamięci USB.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Uruchom modem ponownie.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Poczekaj 3 minuty, a następnie uruchom poniższe polecenie, aby zatrzymać qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Na pamięci USB znajdziesz folder z plikami danych zarejestrowanych przez qLog. Do ich dekodowania wymagane jest narzędzie Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B {#gl-xe300gl-x750gl-x300b}

1. Podłącz pamięć USB, a następnie uruchom `df -h`, aby sprawdzić ścieżkę montowania, i zapisz ją.

    W poniższym przykładzie pamięć USB jest zamontowana pod ścieżką `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Uruchom poniższe polecenia, aby pobrać qlog z serwera GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Uruchom poniższe polecenie, aby włączyć tryb debugowania modemu.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Uruchom poniższe polecenie, aby rozpocząć rejestrowanie przez qlog. Zastąp `/tmp/mountd/disk1_part1` rzeczywistą ścieżką montowania pamięci USB.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Uruchom modem ponownie.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Poczekaj 3 minuty, a następnie uruchom poniższe polecenie, aby zatrzymać qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Na pamięci USB znajdziesz folder z plikami danych zarejestrowanych przez qLog. Do ich dekodowania wymagane jest narzędzie Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000 {#gl-x3000gl-xe3000}

1. Podłącz pamięć USB, a następnie uruchom `df -h`, aby sprawdzić ścieżkę montowania, i zapisz ją.

    W poniższym przykładzie pamięć USB jest zamontowana pod ścieżką `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Uruchom poniższe polecenia, aby pobrać qlog z serwera GL.iNet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Uruchom poniższe polecenie, aby rozpocząć rejestrowanie przez qlog. Zastąp `/tmp/mountd/disk1_part1` rzeczywistą ścieżką montowania pamięci USB.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Uruchom modem ponownie.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Poczekaj 3 minuty, a następnie uruchom poniższe polecenie, aby zatrzymać qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Na pamięci USB znajdziesz folder z plikami danych zarejestrowanych przez qLog. Do ich dekodowania wymagane jest narzędzie Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
