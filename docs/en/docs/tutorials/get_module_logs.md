# How to use qlog to capture modem logs

Some GL.iNet routers come with built-in 3G/4G/5G modules. When the network connection is unstable, it may be necessary to export the module's log for analysis.

Here are the steps to export the cellular module's logs.

## 1. Connect your computer to the router

Connect a laptop to the router's Wi-Fi (find the SSID and password on the device bottom label), or connect the ethernet port of your computer to the router's LAN port via an ethernet cable.

## 2. SSH log in to your router

Please refer to [this link](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Get modem logs

Select the appropriate steps based on your device model.

### For GL-E5800

1. Insert a USB flash disk, then run the df command to get the mount path and remember it.

    The USB flash disk in the following example is mounted at `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Download the cfg configuration file.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Run the following command to start modem log collection. Replace `/tmp/mountd/disk1_part1` with the actual mount path of your USB flash disk.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) & 
    ```

4. Reboot the modem. Replace `<sim_slot>` with the number of the currently active SIM card slot (`1` or `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    For example, if SIM card **1** is active:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Wait several minutes, then run the following command to stop qlog.

    ```
    diag_mdlog -k
    ```

6. You will find a folder on the USB flash disk. It contains files with qLog captured data, which require the Quectel tool for decoding. Please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### For GL-X2000

1. Insert a USB flash disk, then run the df command to get the mount path and remember it.

    The USB flash disk in the following example is mounted at `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Download the cfg configuration file.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Download the qlog tool.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ``` 
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Use the following command to start qlog. Replace `/tmp/mountd/disk1_part1` with the actual mount path of your USB flash disk.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

5. Use the following command to reboot the modem.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Wait 3 minutes, then use the following command to stop qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. You will find a folder on the USB flash disk. It contains files with qLog captured data, which require the Quectel tool for decoding. Please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### For GL-XE300/GL-X750/GL-X300B

1. Insert a USB flash disk, then run the df command to get the mount path and remember it.

    The USB flash disk in the following example is mounted at `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Use the following commands to get qlog from the GL.iNet server.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Use the following command to open module debug mode.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Use the following command to start qlog.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    **Note**: `/tmp/mountd/disk1_part1` is a sample USB drive mount path. Replace it with your own mount path.

5. Use the following command to reboot the modem.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Wait 1~3 minutes, then use the following command to stop qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. You will find a folder on the USB flash disk. It contains files with qLog captured data, which require the Quectel tool for decoding. Please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### For GL-X3000/GL-XE3000

1. Insert a USB flash disk, then run the df command to get the mount path and remember it.

    The USB flash disk in the following example is mounted at `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Use the following commands to get qlog from the GL.iNet server.
    
    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Use the following command to start qlog.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```
    
4. Use the following command to reboot the modem.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. After capturing packets with qlog, use the following command to stop qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. You will find a folder on the USB flash disk. It contains files with qLog captured data, which require the Quectel tool for decoding. Please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
