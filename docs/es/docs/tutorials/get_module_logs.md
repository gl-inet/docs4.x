# Obtener registros del módulo

Algunos routers GL.iNet incorporan módulos 3G/4G/5G. Cuando la conexión de red es inestable, puede ser necesario exportar el registro del módulo para su análisis.
Estos son los pasos para exportar el registro del módulo celular.

## 1. Conecte su ordenador al router

Conecte un portátil al Wi-Fi del router, localizando el SSID y la contraseña en la etiqueta inferior del dispositivo, o conecte el puerto Ethernet de su ordenador al puerto LAN del router mediante un cable Ethernet.

## 2. Inicie sesión en el router por SSH

Consulte [este enlace](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

## 3. Obtenga los registros del módulo

### Para GL-XE300/GL-X750/GL-X300B

1. Utilice los siguientes comandos para obtener `qlog` desde el servidor de GL.iNet y confirme que el SHA256 del archivo `qlog` sea correcto.

    ```
    cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/qlog-ar9531-sha256-75fe8b
    ```

    ```
    chmod 775 qlog-ar9531-sha256-75fe8b  && sha256sum qlog-ar9531-sha256-75fe8b
    ```

    ![Get Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_get_qlog.png){class="glboxshadow"}

2. Inserte una memoria USB y utilice el comando `df` para obtener la ruta de montaje; recuerde esa ruta.

    La ruta de montaje de mi memoria USB es `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_u_flash_drive_path.png){class="glboxshadow"}

3. Utilice el siguiente comando para activar el modo de depuración del módulo.

    ```
    gl_modem AT AT+QCFG=\"dbgctl\",0
    ```

4. Utilice el siguiente comando para iniciar `qlog`.

    ```
    qlog-ar9531-sha256-75fe8b -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

    `/tmp/mountd/disk1_part1` es la ruta de mi memoria USB; debe cambiarla por la suya.

5. Utilice el siguiente comando para reiniciar el módulo.

    ```
    gl_modem AT AT+CFUN=0; sleep 1; gl_modem AT AT+CFUN=1
    ```

6. Espere entre 1 y 3 minutos y utilice el siguiente comando para detener `qlog`.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_start_and_stop_qlog.png){class="glboxshadow"}

7. Encontrará un directorio en la memoria USB con varios archivos. Estos archivos contienen los datos capturados por `qlog` y deben descodificarse con una herramienta de Quectel, así que envíelos al soporte técnico de GL.iNet o de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/ar9531_qlogs_files.png){class="glboxshadow"}

### Para GL-X3000/GL-XE3000

1. Inserte una memoria USB y utilice el comando `df` para obtener la ruta de montaje; recuerde esa ruta.

    La ruta de montaje de mi memoria USB es `/tmp/mountd/disk1_part1`

    ![U Flash Drive Path](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_u_flash_drive_path.png){class="glboxshadow"}

2. Obtenga `qlog` desde el servidor de GL.iNet y confirme que el SHA256 del archivo `qlog` sea correcto.

    Utilice los siguientes comandos para obtener `qlog`.

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

3. Utilice el siguiente comando para iniciar `qlog`.

    ```
    qlog-mtk7981a-sha256-78dda4 -f /etc/default_v15.cfg -s /tmp/mountd/disk1_part1/qlogs_$(date +%Y%m%d%H%M) &
    ```

4. Utilice el siguiente comando para reiniciar el módulo.

    ```
    gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=0; sleep 1; gl_modem -B 0001:01:00.0 SAT sp AT+CFUN=1
    ```

5. Después de capturar paquetes con `qlog`, utilice el siguiente comando para detener `qlog`.

    ```
    ps  | grep qlog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Start And Stop Qlog](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_start_and_stop_qlog.png){class="glboxshadow"}

6. Encontrará un directorio en la memoria USB con varios archivos. Estos archivos contienen los datos capturados por `qlog` y deben descodificarse con una herramienta de Quectel, así que envíelos al soporte técnico de GL.iNet o de Quectel.

    ![Qlogs Files](https://static.gl-inet.com/docs/router/en/4/tutorials/get_module_logs/mtk7981a_qlogs_files.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
