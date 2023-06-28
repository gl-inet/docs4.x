
# Use your pc or laptop to connect device
Use the laptop wifi to connect the device SSID(you will find the SSID and wifi password on the device bottom label), or use the Ethenet cable to connect device LAN port and laptop Ethenet port.
# Use the ssh protocol to login the device
Please refer to this link: [https://docs.gl-inet.com/router/en/3/tutorials/ssh/](https://docs.gl-inet.com/router/en/3/tutorials/ssh/)
# For XE300/X750/X300 products
## Get the qlog from gl.inet server and confirm the qlog file sha256 is right
Use the following commands to get qlog
```
cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
```
```
chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
```
![Get Qlog](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}
## Use the qlog
### 1 Insert a USB flash disk and use the df command to get the mount path, remember the path
My USB flash disk mount path is /tmp/mountd/disk1_part1
![U Flash Drive Path](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}
### 2 Use the following command to open module debug mode
```
gl_modem AT AT+QCFG=\"dbgctl\",0
```
### 3 Use the following command to start qlog
```
qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) & 
```
The /tmp/mountd/disk1_part1 is my USB flash disk, you must change the path to your path
### 4 Use the following command to reboot model.
```
gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
```
### 5 Wait 1~3 minutes, use the following command to stop qlog
```
killall qlog*
```
![Start And Stop Qlog](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}
### 6 You will find a directory in the USB flash disk, there are some files, these files are qlog get data and need use Quectel tool to decode, so please send these files to GL.iNet or Quectel technical support.
![Qlogs Files](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}
# For X3000/XE3000 products
## Get the qlog from gl.inet server and confirm the qlog file sha256 is right
Use the following commands to get qlog
```
cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
```
```
chmod 775 qlog-mtk7981a-sha256-78dda4  && sha256sum qlog-mtk7981a-sha256-78dda4
```
![Get Qlog](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/mtk7981a_get_qlog.png){class="glboxshadow"}
## Use the following command to start qlog
```
qlog-mtk7981a-sha256-78dda4 -s /tmp/qlogs_$(date +%Y%m%d%H%M) & 
```
## Wait 1~3 minutes, use the following command to stop qlog
```
killall qlog*
```
![Start And Stop Qlog](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}
## You will find a directory in /tmp/, there are some files, these files are qlog get data and need use Quectel tool to decode, so please send these files to GL.iNet or Quectel technical support.
![Qlogs Files](https://static.gl-inet.com/docs/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}