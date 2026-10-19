# Cómo usar qlog para capturar registros del módem

Algunos routers GL.iNet incorporan módems 3G/4G/5G. Si la conexión de red es inestable, puede ser necesario exportar los registros del módem para analizarlos.

A continuación se indican los pasos para exportar los registros del módem celular.

## 1. Conecte su ordenador al router

Conecte un portátil al Wi-Fi del router, localizando el SSID y la contraseña en la etiqueta inferior del dispositivo, o conecte el puerto Ethernet de su ordenador al puerto LAN del router mediante un cable Ethernet.

## 2. Inicie sesión en el router por SSH

Consulte [este enlace](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Obtener registros del módem

Seleccione los pasos adecuados para el modelo de su dispositivo.

### GL-E5800

1. Inserte una memoria USB y ejecute `df -h` para obtener su ruta de montaje. Anote esta ruta.

    En el siguiente ejemplo, la memoria USB está montada en `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_u_flash_drive_path.png){class="glboxshadow"}

2. Descargue el archivo de configuración cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/4G_5G_2.cfg
    ```

3. Ejecute el siguiente comando para iniciar la captura de registros del módem. Sustituya `/tmp/mountd/disk1_part1` por la ruta de montaje real de su memoria USB.

    ```
    diag_mdlog -u -i -f /etc/4G_5G_2.cfg -o /tmp/mountd/disk1_part1/diag_$(date +%Y%m%d%H%M) &
    ```

4. Reinicie el módem. Sustituya `<sim_slot>` por el número de la ranura de la tarjeta SIM activa (`1` o `2`).

    ```
    gl_modem -B cpu -U <sim_slot> AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U <sim_slot> AT AT+CFUN=1

    ```
    Por ejemplo, si la tarjeta SIM **1** está activa:

    ```
    gl_modem -B cpu -U 1 AT AT+CFUN=0; sleep 1; gl_modem -B cpu -U 1 AT AT+CFUN=1
    ```

5. Espere 3 minutos y ejecute el siguiente comando para detener qlog.

    ```
    diag_mdlog -k
    ```

6. Encontrará una carpeta en la memoria USB con los datos capturados por qLog. Estos archivos requieren la herramienta de Quectel para decodificarlos. Envíelos al soporte técnico de GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/E5800_qlogs_files.png){class="glboxshadow"}

### GL-X2000

1. Inserte una memoria USB y ejecute `df -h` para obtener su ruta de montaje. Anote esta ruta.

    En el siguiente ejemplo, la memoria USB está montada en `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/x2000_u_flash_drive_path.png){class="glboxshadow"}

2. Descargue el archivo de configuración cfg.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```
    ![download cfg file](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_cfg_file.png){class="glboxshadow"}

3. Descargue la herramienta qlog.

    ```
    cd /usr/bin && wget https://fw.gl-inet.com/tools/quectel_tool/QLog_X2000
    ```

    ```
    chmod 775 /usr/bin/QLog_X2000
    ```

    ![download qlog tool](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_download_qlog_tool.png){class="glboxshadow"}

4. Ejecute el siguiente comando para iniciar qlog. Sustituya `/tmp/mountd/disk1_part1` por la ruta de montaje real de su memoria USB.

    ```
    QLog_X2000 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Reinicie el módem.

    ```
    gl_modem -B 2-1 AT AT+CFUN=0; sleep 1; gl_modem -B 2-1 AT AT+CFUN=1
    ```

6. Espere 3 minutos y ejecute el siguiente comando para detener qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Encontrará una carpeta en la memoria USB con los datos capturados por qLog. Estos archivos requieren la herramienta de Quectel para decodificarlos. Envíelos al soporte técnico de GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/X2000_qlogs_files.png){class="glboxshadow"}


### GL-XE300/GL-X750/GL-X300B

1. Inserte una memoria USB y ejecute `df -h` para obtener su ruta de montaje. Anote esta ruta.

    En el siguiente ejemplo, la memoria USB está montada en `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

2. Ejecute los siguientes comandos para descargar qlog del servidor de GL.iNet.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b
    ```

3. Ejecute el siguiente comando para habilitar el modo de depuración del módem.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Ejecute el siguiente comando para iniciar qlog. Sustituya `/tmp/mountd/disk1_part1` por la ruta de montaje real de su memoria USB.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

5. Reinicie el módem.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Espere 3 minutos y ejecute el siguiente comando para detener qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

7. Encontrará una carpeta en la memoria USB con los datos capturados por qLog. Estos archivos requieren la herramienta de Quectel para decodificarlos. Envíelos al soporte técnico de GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### GL-X3000/GL-XE3000

1. Inserte una memoria USB y ejecute `df -h` para obtener su ruta de montaje. Anote esta ruta.

    En el siguiente ejemplo, la memoria USB está montada en `/tmp/mountd/disk1_part1`.

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Ejecute los siguientes comandos para descargar qlog del servidor de GL.iNet.

    ```
    cd /etc/ && wget https://fw.gl-inet.com/tools/quectel_tool/default_v15.cfg
    ```

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-mtk7981a-sha256-78dda4
    ```

    ```
    chmod 775 qlog-mtk7981a-sha256-78dda4
    ```

3. Ejecute el siguiente comando para iniciar qlog. Sustituya `/tmp/mountd/disk1_part1` por la ruta de montaje real de su memoria USB.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Reinicie el módem.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Espere 3 minutos y ejecute el siguiente comando para detener qlog.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

6. Encontrará una carpeta en la memoria USB con los datos capturados por qLog. Estos archivos requieren la herramienta de Quectel para decodificarlos. Envíelos al soporte técnico de GL.iNet o Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
