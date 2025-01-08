# Get Module Logs

Some GL.iNet routers come with built-in 3G, 4G, or 5G modules. When the network connection is not smooth, it may be necessary to export the module's log for analysis. Here are the steps to do so.

## Use your computer to connect device

Use the laptop wifi to connect the device SSID (you will find the SSID and wifi password on the device bottom label), or use the an ethenet cable to connect the LAN port of device and the the ethenet port of your computer.

## Use the SSH protocol to login the device

Please refer to this link: [https://docs.gl-inet.com/router/en/3/tutorials/ssh/](https://docs.gl-inet.com/router/en/3/tutorials/ssh/)

## For GL-XE300/GL-X750/GL-X300

### Get the qlog from GL.iNet server and confirm the qlog file SHA256 is right

Use the following commands to get qlog

```
cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
```

```
chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
```

![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

### Use the qlog

1. Insert a USB flash disk and use the df command to get the mount path, remember the path

    My USB flash disk mount path is `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Use the following command to open module debug mode

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

3. Use the following command to start qlog

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```

    The `/tmp/mountd/disk1_part1` is my USB flash disk, you must change the path to your path

4. Use the following command to reboot model.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

5. Wait 1~3 minutes, use the following command to stop qlog

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

6. You will find a directory in the USB flash disk, there are some files, these files are qlog get data and need use Quectel tool to decode, so please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

## For GL-X3000/GL-XE3000

1. Insert a USB flash disk and use the df command to get the mount path, remember the path

    My USB flash disk mount path is `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Get the qlog from GL.iNet server and confirm the qlog file sha256 is right

    Use the following commands to get qlog
    
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

3. Use the following command to start qlog

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
    ```
    
4. Use the following command to reboot model.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. After captured packets with qlog, use the following command to stop qlog

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. You will find a directory in the USB flash disk, there are some files, these files are qlog get data and need use Quectel tool to decode, so please send these files to GL.iNet or Quectel technical support.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
