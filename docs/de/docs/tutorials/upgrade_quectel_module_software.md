# Quectel-Modul-Firmware aktualisieren

## Vorbereitung

1. Stellen Sie sicher, dass Ihr Router für den Internetzugang eingerichtet ist.

2. Verbinden Sie einen Computer oder Laptop per WLAN oder Ethernet-Kabel mit dem Router.

## Schritte für das Upgrade

### Für GL-X3000/GL-XE3000

**Methode 1. Upgrade über die GL.iNet-GUI**

1. Laden Sie die passende Modul-Firmware am Ende dieses Tutorials herunter.

2. Melden Sie sich im Web-Admin-Panel Ihres Routers an, gehen Sie zu **SYSTEM** -> **Upgrade** -> **Module Local Upgrade** und laden Sie die Modul-Firmware (im `.zip`-Format) hoch.
    
    ![Lokales Modul-Upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/module_local_upgrade.png){class="glboxshadow"}

**Methode 2. Upgrade per SSH**

Das Upgrade des RM520N-Moduls wird hier als Beispiel verwendet.

1. Melden Sie sich per SSH an Ihrem Router an. Bitte beachten Sie [diesen Link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Geben Sie den folgenden Befehl ein, um die Modul-Firmware herunterzuladen.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![Modul-Firmware herunterladen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Geben Sie den folgenden Befehl ein, um die Modul-Firmware zu entpacken.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![Modul-Firmware entpacken](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Aktualisieren Sie die Modul-Firmware mit dem Befehl `QFirehose`, wie unten gezeigt.

    **Hinweis**: Ersetzen Sie bitte "/RM520NGLAAR03A03M4G_01.201.01201" durch den tatsächlichen Ordnerpfad der Modul-Firmware.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![Upgrade über QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Warten Sie einige Minuten. Nach Abschluss des Upgrades zeigt das System "Upgrade module successfully" an.

    ![Upgrade erfolgreich](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Starten Sie Ihren Router neu und melden Sie sich anschließend erneut per SSH am Router an.

7. Führen Sie den folgenden Befehl aus, um zusätzlich zu prüfen, ob das Modul-Upgrade erfolgreich war.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![Version prüfen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Für GL-MiFi/GL-XE300/GL-X750/GL-E750

Das Upgrade des EM060K-Moduls wird hier als Beispiel verwendet.

1. Bereiten Sie einen USB-Stick vor. Laden Sie die passende Modul-Firmware am Ende dieses Tutorials auf den USB-Stick herunter, entpacken Sie die .zip-Datei und legen Sie sie im Stammverzeichnis des USB-Sticks ab.

2. Stecken Sie den USB-Stick in Ihren Router ein. Melden Sie sich dann gemäß [diesem Link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) per SSH an Ihrem Router an.

3. Geben Sie den Befehl `df - h` ein, um den Einhängepfad des USB-Sticks zu prüfen, und notieren Sie sich den Pfad.

    ![Einhängepfad prüfen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Geben Sie den Befehl `ls -l` ein, um den Ordner der Modul-Firmware zu prüfen.

    ![Firmware-Ordner prüfen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Geben Sie den folgenden Befehl ein, um `QFirehose` vom GL.iNet-Server abzurufen.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Gewähren Sie der Datei anschließend Ausführungsrechte.

    ``` 
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![QFirehose abrufen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Aktualisieren Sie die Modul-Firmware mit dem Befehl `QFirehose`, wie unten gezeigt.

    **Hinweis**: Ersetzen Sie bitte "/mnt/sdb1/EM060KGLAAR01A12M2GA" durch den tatsächlichen Ordnerpfad der Modul-Firmware.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![Upgrade über QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Warten Sie einige Minuten. Nach Abschluss des Upgrades zeigt das System "Upgrade module successfully" an.

    ![Upgrade erfolgreich](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Starten Sie Ihren Router neu und melden Sie sich anschließend erneut per SSH an Ihrem Router an.

9. Führen Sie den folgenden Befehl aus, um zusätzlich zu prüfen, ob das Modul-Upgrade erfolgreich war.

    ```
    gl_modem AT AT+QGMR
    ```
    ![Modulversion prüfen](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Download-URLs für Quectel-Modul-Firmware

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
