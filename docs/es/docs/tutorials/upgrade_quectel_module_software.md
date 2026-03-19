# Actualizar el firmware del módulo Quectel

## Preparación

1. Asegúrese de que su router esté configurado para acceder a Internet.

2. Conecte un ordenador o un portátil al router mediante Wi-Fi o un cable Ethernet.

## Pasos de actualización

### Para GL-X3000/GL-XE3000

**Método 1. Actualización mediante la GUI de GL.iNet**

1. Descargue el firmware del módulo correspondiente desde la parte inferior de este tutorial.

2. Inicie sesión en el panel de administración web del router, vaya a **SYSTEM** -> **Upgrade** -> **Module Local Upgrade** y suba el firmware del módulo, en formato .zip.

   ![module local upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/upgrade/module_local_upgrade.png){class="glboxshadow"}

**Método 2. Actualización mediante SSH**

Tomemos como ejemplo la actualización del módulo RM520N.

1. Inicie sesión en el router por SSH. Consulte [este enlace](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

2. Introduzca el comando siguiente para descargar el firmware del módulo.

   ```
   wget https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A03M4G_01.201.01.201.zip -P /
   ```

   ![mtk7981a_get_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/download_firmware.png){class="glboxshadow"}

3. Introduzca el comando siguiente para descomprimir el firmware del módulo.

   ```
   unzip /RM520NGLAAR03A03M4G_01.201.01.201.zip -d /RM520NGLAAR03A03M4G_01.201.01.201
   ```

   ![mtk7981a_decompress_module_software](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/unzip_firmware.png){class="glboxshadow"}

4. Actualice el firmware del módulo con el comando QFirehose, como se muestra a continuación.

   **Nota**: Sustituya "/RM520NGLAAR03A03M4G_01.201.01201" por la ruta real de la carpeta del firmware del módulo.

   ```
   QFirehose-mtk7981a-sha256-c0b944 -f /RM520NGLAAR03A03M4G_01.201.01.201
   ```

   ![mtk7981a_upgrade_via_qfirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_via_qfirehose.png){class="glboxshadow"}

5. Espere unos minutos. Cuando la actualización finalice, el sistema mostrará el mensaje "Upgrade module successfully".

   ![mtk7981a_upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/upgrade_success.png){class="glboxshadow"}

6. Reinicie el router y vuelva a iniciar sesión en él por SSH.

7. Ejecute el comando siguiente para comprobar de nuevo si la actualización del módulo se realizó correctamente.

   ```
   gl_modem -B 0001:01:00.0 AT AT+QGMR
   ```

   ![mtk7981a_check_version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/x3000_xe3000/check_module_version.png){class="glboxshadow"}

### Para GL-MiFi/GL-XE300/GL-X750/GL-E750

Tomemos como ejemplo la actualización del módulo EM060K.

1. Prepare una memoria USB. Descargue en ella el firmware del módulo correspondiente desde la parte inferior de este tutorial, luego descomprima el archivo .zip y colóquelo en el directorio raíz de la unidad USB.

2. Conecte la memoria USB al router. Después, consulte [este enlace](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) para iniciar sesión en el router por SSH.

3. Introduzca el comando `df - h` para comprobar la ruta de montaje de la unidad USB y anótela.

   ![check mounting path](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_mounting_path.png){class="glboxshadow"}

4. Introduzca el comando `ls -l` para comprobar la carpeta del firmware del módulo.

   ![check firmware folder](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_firmware_folder.png){class="glboxshadow"}

5. Introduzca el comando siguiente para obtener QFirehose desde el servidor de GL.iNet.

   ```
   cd /usr/bin/ && wget https://fw.gl-inet.com/tools/quectel_tool/QFirehose-ar9531
   ```

   A continuación, concédale permisos de ejecución.

   ```
   chmod 775 /usr/bin/QFirehose-ar9531
   ```

   ![obtain QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/obtain_qfirehose.jpg){class="glboxshadow"}

6. Actualice el firmware del módulo con el comando QFirehose, como se muestra a continuación.

   **Nota**: Sustituya "/mnt/sdb1/EM060KGLAAR01A12M2GA" por la ruta real de la carpeta del firmware del módulo.

   ```
   /usr/bin/QFirehose-ar9531 -f /mnt/sdb1/EM060KGLAAR01A12M2GA
   ```

   ![upgrade via QFirehose](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_via_qfirehose.png){class="glboxshadow"}

7. Espere unos minutos. Cuando la actualización finalice, el sistema mostrará el mensaje "Upgrade module successfully".

   ![upgrade_success](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/upgrade_success.png){class="glboxshadow"}

8. Reinicie el router y vuelva a iniciar sesión en él por SSH.

9. Ejecute el siguiente comando para volver a confirmar si la actualización del módulo se realizó correctamente.

   ```
   gl_modem AT AT+QGMR
   ```

   ![check module version](https://static.gl-inet.com/docs/router/en/4/tutorials/upgrade_quectel_module_software/other_model/check_module_version.png){class="glboxshadow"}

## URL de descarga del firmware del módulo Quectel

EP06-A: [https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip](https://fw.gl-inet.com/download/EP06A-modem-firmware/EP06ALAR02A08M4G_01.009.01.009.zip)

EP06-E: [https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip](https://fw.gl-inet.com/download/EP06E-modem-firmware/EP06ELAR04A22M4G.zip)

EM060K: [https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip](https://fw.gl-inet.com/download/EM060K-modem-firmware/EM060KGLAAR01A12M2GA.zip)

RM520N-GL_AA: [https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip](https://fw.gl-inet.com/download/RM520GL-modem_firmware/RM520NGLAAR03A04M4G_01.202.01.202.zip)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
