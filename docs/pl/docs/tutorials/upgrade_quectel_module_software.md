# Aktualizacja oprogramowania modułu Quectel

## Przygotowanie

1. Upewnij się, że router ma skonfigurowany dostęp do Internetu.

2. Podłącz komputer lub laptop do routera przez Wi-Fi lub kabel Ethernet.

## Kroki aktualizacji

### Dla GL-X3000/GL-XE3000

**Metoda 1. Aktualizacja przez interfejs GL.iNet**

1. Pobierz odpowiednie oprogramowanie modułu z dolnej części tego poradnika.

2. Zaloguj się do panelu administracyjnego routera, przejdź do **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** i prześlij oprogramowanie modułu (w formacie .zip).
    
    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/modem_local_upgrade.png){class="glboxshadow"}

**Metoda 2. Aktualizacja przez SSH**

Jako przykład posłuży aktualizacja modułu RM520N.

1. Zaloguj się do routera przez SSH. Zapoznaj się z [tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Wprowadź poniższą komendę, aby pobrać oprogramowanie modułu.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Wprowadź poniższą komendę, aby rozpakować oprogramowanie modułu.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Zaktualizuj oprogramowanie modułu za pomocą komendy QFirehose, jak pokazano poniżej.

    **Uwaga**: Zamień „/RM520NGLAAR03A03M4G_01.201.01201" na rzeczywistą ścieżkę folderu z oprogramowaniem modułu.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Poczekaj kilka minut. Po zakończeniu aktualizacji system wyświetli komunikat „Upgrade module successfully".

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Uruchom router ponownie, a następnie zaloguj się ponownie przez SSH. 

7. Uruchom poniższą komendę, aby potwierdzić, czy aktualizacja modułu zakończyła się pomyślnie.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Dla GL-MiFi/GL-XE300/GL-X750/GL-E750

Jako przykład posłuży aktualizacja modułu EM060K.

1. Przygotuj pendrive USB. Pobierz odpowiednie oprogramowanie modułu na pendrive z dolnej części tego poradnika, rozpakuj plik .zip i umieść go w katalogu głównym pendrive'a.

2. Podłącz pendrive do routera. Następnie zapoznaj się z [tym linkiem](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/), aby zalogować się do routera przez SSH.

3. Wprowadź komendę `df - h`, aby sprawdzić ścieżkę montowania pendrive'a i zanotuj ją.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Wprowadź komendę `ls -l`, aby sprawdzić folder z plikami oprogramowania modułu.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Wprowadź poniższą komendę, aby pobrać QFirehose z serwera GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Następnie nadaj mu uprawnienia do wykonywania.

    ``` 
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Zaktualizuj oprogramowanie modułu za pomocą komendy QFirehose, jak pokazano poniżej.

    **Uwaga**: Zamień „/mnt/sdb1/EM060KGLAAR01A12M2GA" na rzeczywistą ścieżkę folderu z oprogramowaniem modułu.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Poczekaj kilka minut. Po zakończeniu aktualizacji system wyświetli komunikat „Upgrade module successfully".

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Uruchom router ponownie, a następnie zaloguj się ponownie przez SSH. 

9. Uruchom poniższą komendę, aby potwierdzić, czy aktualizacja modułu zakończyła się pomyślnie.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Adresy URL do pobierania oprogramowania modułów Quectel

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
