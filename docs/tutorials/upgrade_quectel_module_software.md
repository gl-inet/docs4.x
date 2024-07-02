# Upgrade Quectel Module Software

## Use your computer to connect device

Use the laptop wifi to connect the device SSID (you will find the SSID and wifi password on the device bottom label), or use the an ethenet cable to connect the LAN port of device and the the ethenet port of your computer.

## Use the SSH protocol to login the device

Please refer to this link: [https://docs.gl-inet.com/router/en/3/tutorials/ssh/](https://docs.gl-inet.com/router/en/3/tutorials/ssh/)

### For GL-MiFi/GL-XE300/GL-X750/GL-E750/GL-X300B

1. Get the QFirehose from GL.iNet server and confirm the QFirehose file SHA256 is right

    Use the following commands to get QFirehose

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531-sha256-7383f4
    ```

    ``` 
    chmod 775 QFirehose-ar9531-sha256-7383f4  && sha256sum QFirehose-ar9531-sha256-7383f4
    ```

    ![ar9531_get_QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_get_QFirehose.png){class="glboxshadow"}

2. Drop down to the bottom of this document to download the required module firmware

    Put the zip package on a USB flash drive and unzip it

3. Insert a USB flash disk and use the df command to get the mount path, remember the path

    My USB flash disk mount path is /mnt/sdb1

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_u_flash_drive_path.png){class="glboxshadow"}

4. Use QFirehose to upgrade Quectel module software

    ```
    QFirehose-ar9531-sha256-7383f4 -f /mnt/sdb1/EP06ALAR02A08M4G_01.009.01.009
    ```

    ![ar9531_upgrade_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_upgrade_quectel_module_software.png){class="glboxshadow"}

5. Use the following command to check the Quectel module software version.

    ```
    gl_modem AT AT+QGMR
    ```

    ![ar9531_check_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/ar9531_check_quectel_module_software.png){class="glboxshadow"}

### For GL-X3000/GL-XE3000

1. Get the QFirehose from GL.iNet server and confirm the QFirehose file sha256 is right

    Use the following commands to get QFirehose

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-mtk7981a-sha256-c0b944
    ```

    ``` 
    chmod 775 QFirehose-mtk7981a-sha256-c0b944  && sha256sum QFirehose-mtk7981a-sha256-c0b944
    ```

    ![mtk7981a_get_QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_get_QFirehose.png){class="glboxshadow"}

2. Get the Quectel module software and upcompress(For example RM520, for other module software, please refer to note of at the end of the document)

    ```
    wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
    ```

    ![mtk7981a_get_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_get_quectel_module_software.png){class="glboxshadow"}

    ```
    unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upcompress_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_upcompress_quectel_module_software.png){class="glboxshadow"}

3. Use QFirehose to upgrade Quectel module software

    ```
    QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
    ```

    ![mtk7981a_upgrade_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_upgrade_quectel_module_software.png){class="glboxshadow"}

4. Use the following commands to check the Quectel module software version.

    ```
    echo 1 > /sys/devices/platform/11280000.pcie/pci0001:00/0001:00:00.0/0001:01:00.0/remove
    ```

    ```
    echo 1 > /sys/devices/platform/11280000.pcie/pci0001:00/0001:00:00.0/rescan
    ```

    ```
    gl_modem AT AT+QGMR
    ```

    ```
    rm /RM520NGLAAR03A03M4G_01.201.01.201* -rf
    ```

    ![mtk7981a_check_quectel_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/mtk7981a_check_quectel_module_software.png){class="glboxshadow"}

### Quectel module software donwload URL

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
