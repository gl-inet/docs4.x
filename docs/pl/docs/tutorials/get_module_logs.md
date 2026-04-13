# Pobieranie logów modułu

Niektóre routery GL.iNet mają wbudowane moduły 3G/4G/5G. Gdy połączenie sieciowe jest niestabilne, może być konieczne wyeksportowanie logów modułu w celu analizy.

Poniżej znajdują się kroki do wyeksportowania logów modułu komórkowego.

## 1. Podłącz komputer do routera

Podłącz laptop do sieci Wi-Fi routera (SSID i hasło znajdziesz na etykiecie u spodu urządzenia) lub podłącz port Ethernet komputera do portu LAN routera kablem Ethernet.

## 2. Zaloguj się do routera przez SSH

Zapoznaj się z [tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Pobierz logi modułu

### Dla GL-XE300/GL-X750/GL-X300B

1. Użyj poniższych komend, aby pobrać qlog z serwera GL.iNet i potwierdzić, czy suma kontrolna SHA256 pliku qlog jest prawidłowa.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. Włóż pendrive USB i użyj komendy df, aby uzyskać ścieżkę montowania, zapamiętaj ścieżkę.

    Moja ścieżka montowania pendrive USB to `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Użyj poniższej komendy, aby włączyć tryb debugowania modułu.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Użyj poniższej komendy, aby uruchomić qlog.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    `/tmp/mountd/disk1_part1` to mój pendrive USB, musisz zmienić ścieżkę na swoją.

5. Użyj poniższej komendy, aby ponownie uruchomić moduł.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Poczekaj 1-3 minuty, użyj poniższej komendy, aby zatrzymać qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. Znajdziesz katalog na pendrive USB, w którym znajdują się pliki — są to dane zebrane przez qlog, które wymagają dekodowania za pomocą narzędzia Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### Dla GL-X3000/GL-XE3000

1. Włóż pendrive USB i użyj komendy df, aby uzyskać ścieżkę montowania, zapamiętaj ścieżkę.

    Moja ścieżka montowania pendrive USB to `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Pobierz qlog z serwera GL.iNet i potwierdź, czy suma kontrolna sha256 pliku qlog jest prawidłowa.

    Użyj poniższych komend, aby pobrać qlog
    
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

3. Użyj poniższej komendy, aby uruchomić qlog.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```
    
4. Użyj poniższej komendy, aby ponownie uruchomić moduł.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Po przechwyceniu pakietów za pomocą qlog użyj poniższej komendy, aby zatrzymać qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. Znajdziesz katalog na pendrive USB, w którym znajdują się pliki — są to dane zebrane przez qlog, które wymagają dekodowania za pomocą narzędzia Quectel. Prześlij te pliki do wsparcia technicznego GL.iNet lub Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
