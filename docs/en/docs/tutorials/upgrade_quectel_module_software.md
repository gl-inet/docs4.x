# Upgrade Quectel Module Firmware

## Preperation

1. Ensure your router is configured to Internet access.

2. Connect a computer or laptop to the router via Wi-Fi or Ethernet cable.

## Upgrade steps

### For GL-X3000/GL-XE3000

**Method 1. Upgrade via GL.iNet GUI**

1. Download the corresponding module firmware from the bottom of this tutorial.

2. Log in to your router's web admin panel, navigate to **SYSTEM** -> **Upgrade** -> **Module Local Upgrade**, and upload the module firmware (in .zip format).
    
    ![module local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/module_local_upgrade.png){class="glboxshadow"}

**Method 2. Upgrade via SSH**

Take the upgrade of the RM520N module as an example.

1. SSH log in to your router. Please refer to [this link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Enter the command below to download the module firmware.

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Enter the command below to decompress the module firmware.

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Upgrade the module firmware using the QFirehose command, as shown below.

    **Note**: Please replace "/RM520NGLAAR03A03M4G_01.201.01201" with the actual module firmware folder path.

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Wait a few minutes. When the upgrade is completed, the system will prompt "Upgrade module successfully".

    ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Reboot your router, then SSH log in to your router again. 

7. Run the following command to double confirm if the module upgrade was successful.

    ```
    gl_modem -B 0001:01:00.0 AT AT+QGMR
    ```

    ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### For GL-MiFi/GL-XE300/GL-X750/GL-E750

Take the upgrade of the EM060K module as an example.

1. Prepare a USB flash drive. Download the corresponding module firmware to the USB flash drive from the bottom of this tutorial, then decompress the. zip file and place it in the root directory of the USB drive.

2. Plug the USB flash drive into your router. Then refer to [this link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) to SSH log in to your router.

3. Enter the command `df - h` to check the USB drive mounting path, and record the path.

    ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Enter the command `ls -l` to check the file folder of module firmware.

    ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Enter the command below to obtain the QFirehose from GL.iNet server.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
    ```

    Then grant it executable permissions.

    ``` 
    chmod 775 /usr/bin/QFirehose-ar9531
    ```

    ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Upgrade the module firmware using the QFirehose command, as shown below.

    **Note**: Please replace "/mnt/sdb1/EM060KGLAAR01A12M2GA" with the actual module firmware folder path.

    ```
    /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
    ```

    ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Wait a few minutes. When the upgrade is completed, the system will prompt "Upgrade module successfully".

    ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Reboot your router, then SSH log in to your router again. 

9. Run the following command to double confirm if the module upgrade was successful.

    ```
    gl_modem AT AT+QGMR
    ```
    ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## Quectel module firmware download URL

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
