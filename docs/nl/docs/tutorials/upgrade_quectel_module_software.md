# Firmware van een Quectel-module upgraden {#upgrade-quectel-module-firmware}

## Voorbereiding {#preperation}

1. Zorg dat je router is geconfigureerd voor internettoegang.

2. Verbind een computer of laptop via Wi-Fi of een ethernetkabel met de router.

## Upgradestappen {#upgrade-steps}

### Voor GL-X3000/GL-XE3000 {#for-gl-x3000gl-xe3000}

**Methode 1. Upgraden via de GL.iNet-GUI**

1. Download onderaan deze handleiding de bijbehorende modulefirmware.

2. Meld je aan bij het webbeheerpaneel van je router, ga naar **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** en upload de modulefirmware in .zip-indeling.

    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/modem_local_upgrade.png){class="glboxshadow"}

**Methode 2. Upgraden via SSH**

We gebruiken het upgraden van de RM520N-module als voorbeeld.

1. Meld je via SSH aan bij je router. Raadpleeg [deze handleiding](ssh_log_in_to_the_router.md).

2. Voer de onderstaande opdracht in om de modulefirmware te downloaden.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Voer de onderstaande opdracht in om de modulefirmware uit te pakken.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Upgrade de modulefirmware met de QFirehose-opdracht, zoals hieronder.

    **Opmerking**: vervang "/RM520NGLAAR03A03M4G_01.201.01.201" door het werkelijke pad van de map met modulefirmware.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Wacht enkele minuten. Wanneer de upgrade is voltooid, geeft het systeem de melding "Upgrade module successfully".

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Start je router opnieuw op en meld je daarna opnieuw via SSH aan bij je router.

7. Voer de volgende opdracht uit om nogmaals te controleren of de module-upgrade is geslaagd.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Voor GL-MiFi/GL-XE300/GL-X750/GL-E750 {#for-gl-mifigl-xe300gl-x750gl-e750}

We gebruiken het upgraden van de EM060K-module als voorbeeld.

1. Bereid een USB-stick voor. Download onderaan deze handleiding de bijbehorende modulefirmware naar de USB-stick, pak het .zip-bestand uit en plaats de uitgepakte map in de hoofdmap van de USB-stick.

2. Sluit de USB-stick aan op je router. Volg vervolgens [deze handleiding](ssh_log_in_to_the_router.md) om je via SSH bij de router aan te melden.

3. Voer de opdracht `df -h` in om het koppelpad van de USB-stick te controleren en noteer het pad.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Voer de opdracht `ls -l` in om de map met modulefirmware te controleren.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Voer de onderstaande opdracht in om QFirehose van de GL.iNet-server te downloaden.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Geef het bestand vervolgens uitvoeringsrechten.

    ```
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Upgrade de modulefirmware met de QFirehose-opdracht, zoals hieronder.

    **Opmerking**: vervang "/mnt/sdb1/EM060KGLAAR01A12M2GA" door het werkelijke pad van de map met modulefirmware.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Wacht enkele minuten. Wanneer de upgrade is voltooid, geeft het systeem de melding "Upgrade module successfully".

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Start je router opnieuw op en meld je daarna opnieuw via SSH aan bij je router.

9. Voer de volgende opdracht uit om nogmaals te controleren of de module-upgrade is geslaagd.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Download-URL's voor firmware van Quectel-modules {#quectel-module-firmware-download-url}

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
