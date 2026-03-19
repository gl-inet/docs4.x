# macOS no puede escribir en un recurso compartido Samba

Al utilizar un dispositivo de almacenamiento formateado en exFAT para un recurso compartido Samba, algunos dispositivos macOS pueden encontrar uno de los siguientes errores al intentar escribir archivos en el recurso.

- "The operation can't be completed because an unexpected error occurred, error code 100093."

  ![error code 100093](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyerror.jpg){class="glboxshadow"}

- "The operation can't be completed because an unexpected error occurred, error code -50."

  ![error code -50](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/error-code-50.jpg){class="glboxshadow"}

Intente resolver este problema con los siguientes métodos.

1.  **Comprobar los permisos del recurso Samba.**

    Asegúrese de que el recurso Samba esté configurado con acceso de escritura. Inicie sesión en el panel de administración web del router y verifique que la carpeta compartida tenga habilitados los permisos "Read/Write" para su cuenta de usuario.

2.  **Use el comando `cp -X file-name` para copiar el archivo.**

    Como Finder añade automáticamente atributos extendidos, por ejemplo, resource forks y metadata, durante las transferencias, lo que puede entrar en conflicto con el manejo de exFAT por parte de Samba, pruebe a usar el comando **cp -X file-name** para copiar el archivo.

    ![macopyfile](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfile.png){class="glboxshadow"}

    O use el comando **cp -rX folder-name** para copiar la carpeta.

    ![macopyfolder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/macos_cannot_write_samba/macopyfolder.png){class="glboxshadow"}

3.  **Reinicie su Mac.**

    Haga clic en el menú Apple y luego en Reiniciar. Si el problema persiste, apague el equipo, desconecte todos los dispositivos externos, espere 30 segundos y vuelva a iniciarlo.

4.  **Cambie el nombre del archivo.**

    Haga clic con el botón derecho en el archivo y luego en Rename. Use nombres sencillos y evite caracteres especiales como !@# o espacios.

5.  **Vuelva a conectar el dispositivo de almacenamiento.**

    Si utiliza una unidad externa, como una memoria USB, expúlsela antes de desconectarla, espere 10 segundos y luego vuelva a conectarla. También puede probar con otro puerto USB.

6.  **Repare errores del disco con First Aid.**

    Los datos dañados del disco pueden provocar fallos de escritura. Puede usar macOS Disk Utility para solucionar problemas.
    1. Abra Finder -> Applications -> Utilities -> Disk Utility.
    2. Seleccione la unidad o dispositivo de almacenamiento, local o externo, en la barra lateral izquierda.
    3. Haga clic en First Aid -> Run. Espere a que finalice el proceso.

7.  **Ajuste el sistema de archivos o formatee la unidad.**

    Si usa una unidad formateada en exFAT, pueden surgir problemas de compatibilidad con Samba en macOS. Puede probar los siguientes métodos.
    - **Formatear a FAT32**, para unidades externas y compatibilidad multiplataforma
      1. Haga primero una copia de seguridad de los datos de la unidad, ya que el formateo borra todos los archivos.
      2. Abra Disk Utility -> seleccione la unidad -> Erase.
      3. Elija "MS-DOS (FAT)", FAT32, como formato -> haga clic en Erase.

    - **Formatear a ext4**

      !!! Note

            ext4 es compatible principalmente con sistemas Linux. Después de formatear a ext4, el dispositivo de almacenamiento puede volverse incompatible con sistemas Windows, lo que podría provocar problemas como que Windows no reconozca la unidad o no pueda escribir en ella.

      1. Haga una copia de seguridad de todos los datos de la unidad, ya que el formateo los borrará.
      2. Use una herramienta como Disk Utility o un sistema Linux para formatear la unidad en ext4.

8.  **Actualice macOS y limpie las cachés.**

    El software desactualizado o las cachés dañadas pueden causar conflictos. Vaya a System Settings -> General -> Software Update, instale la última versión y limpie las cachés del sistema.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
