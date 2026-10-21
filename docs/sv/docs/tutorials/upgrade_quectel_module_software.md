# Uppgradera firmware för Quectel-modulen {#upgrade-quectel-module-firmware}

## Förberedelser {#preperation}

1. Kontrollera att routern är konfigurerad för internetåtkomst.

2. Anslut en dator till routern via Wi-Fi eller Ethernet-kabel.

## Uppgraderingssteg {#upgrade-steps}

### För GL-X3000/GL-XE3000 {#for-gl-x3000gl-xe3000}

**Metod 1. Uppgradera via GL.iNets grafiska gränssnitt**

1. Ladda ned rätt firmware för modulen längst ned i den här guiden.

2. Logga in på routerns webbadministrationspanel, gå till **SYSTEM** -> **Upgrade** -> **Modem Local Upgrade** och ladda upp modulens firmware (i .zip-format).

    ![modem local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/modem_local_upgrade.png){class="glboxshadow"}

**Metod 2. Uppgradera via SSH**

Vi använder uppgradering av RM520N-modulen som exempel.

1. Logga in på routern via SSH. Se [den här länken](ssh_log_in_to_the_router.md).

2. Ange kommandot nedan för att ladda ned modulens firmware.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Ange kommandot nedan för att packa upp modulens firmware.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Uppgradera modulens firmware med kommandot QFirehose enligt nedan.

    **Obs!** Ersätt "/RM520NGLAAR03A03M4G_01.201.01.201" med den faktiska sökvägen till mappen med modulens firmware.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Vänta några minuter. När uppgraderingen är klar visar systemet meddelandet "Upgrade module successfully".

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Starta om routern och logga sedan in via SSH igen.

7. Kör följande kommando för att kontrollera en extra gång att moduluppgraderingen lyckades.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### För GL-MiFi/GL-XE300/GL-X750/GL-E750 {#for-gl-mifigl-xe300gl-x750gl-e750}

Vi använder uppgradering av EM060K-modulen som exempel.

1. Förbered ett USB-minne. Ladda ned rätt firmware för modulen längst ned i den här guiden till USB-minnet. Packa sedan upp .zip-filen och placera den i USB-minnets rotkatalog.

2. Anslut USB-minnet till routern. Följ sedan [den här länken](ssh_log_in_to_the_router.md) för att logga in på routern via SSH.

3. Ange kommandot `df -h` för att kontrollera USB-minnets monteringssökväg och anteckna sökvägen.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Ange kommandot `ls -l` för att kontrollera mappen med modulens firmware.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Ange kommandot nedan för att hämta QFirehose från GL.iNets server.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Ge sedan filen körbehörighet.

    ```
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Uppgradera modulens firmware med kommandot QFirehose enligt nedan.

    **Obs!** Ersätt "/mnt/sdb1/EM060KGLAAR01A12M2GA" med den faktiska sökvägen till mappen med modulens firmware.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Vänta några minuter. När uppgraderingen är klar visar systemet meddelandet "Upgrade module successfully".

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Starta om routern och logga sedan in via SSH igen.

9. Kör följande kommando för att kontrollera en extra gång att moduluppgraderingen lyckades.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Webbadresser för nedladdning av firmware till Quectel-moduler {#quectel-module-firmware-download-url}

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
