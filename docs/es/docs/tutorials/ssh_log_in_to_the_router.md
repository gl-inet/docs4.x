# Iniciar sesión en el router por SSH

Secure Shell (SSH) es un protocolo de red criptográfico que permite operar servicios de red de forma segura sobre una red no segura. El ejemplo de uso más conocido es el inicio de sesión remoto en sistemas informáticos. En ocasiones, necesita herramientas básicas para conectarse por SSH al servidor. Esta guía explica cómo iniciar sesión por SSH en los routers GL.iNet.

---

## Para usuarios de Windows

Hay varias formas de acceder al terminal del router en Windows, como Windows Cmd, PowerShell, Bitvise o PuTTY.

### Usar Windows Cmd

1. Abrir Command Prompt

   Pulse **Win** + **R** para abrir la ventana Run. Escriba **cmd** y pulse Enter.

   ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

   Aparecerá una ventana negra de Command Prompt.

   ![cmd](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Iniciar sesión en el router

   En la ventana de comandos, escriba `ssh root@192.168.8.1` y pulse Enter.

   ![cmd ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

   **Nota**: 192.168.8.1 es la dirección IP predeterminada del router. Si la cambió anteriormente, utilice su IP personalizada.

   A continuación, escriba la contraseña de administración del router y pulse Enter. **Por seguridad, la contraseña no se muestra en pantalla**.

   ![cmd psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

   Si la contraseña es correcta, iniciará sesión en el router correctamente.

   ![cmd login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Solución de problemas"

    1. **Error: Connection timed out**

        Asegúrese de que su dispositivo, por ejemplo un portátil, esté conectado al router. Vuelva a conectarse a la red Wi-Fi del router o a su puerto LAN e inténtelo de nuevo.

    2. **Error: Permission denied**

        Asegúrese de escribir la contraseña de administración correcta. Si la olvidó, restablezca el router manteniendo pulsado el botón RESET durante 10 segundos.

### Usar PowerShell

1. Abrir Windows PowerShell

   Haga clic en el icono de búsqueda de la barra de tareas, escriba **PowerShell**, seleccione **Windows PowerShell** y **ejecútelo como administrador**.

   ![run powershell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Iniciar sesión en el router

   En la ventana de PowerShell, escriba `ssh root@192.168.8.1` y pulse Enter.

   ![powershell ssh root](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

   **Nota**: 192.168.8.1 es la dirección IP predeterminada del router. Si la cambió anteriormente, utilice su IP personalizada.

   El sistema le pedirá confirmar la conexión. Escriba `yes` y pulse Enter.

   ![powershell confirm](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

   Se le pedirá que introduzca la contraseña de administración del router. Introduzca la contraseña correcta y pulse Enter. **Por seguridad, la contraseña no se muestra en pantalla**.

   ![powershell psw](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}

   Después iniciará sesión correctamente en el terminal del router.

   ![powershell login](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Solución de problemas"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Esto ocurre si la clave de seguridad del router cambió, por ejemplo tras un restablecimiento de fábrica o una actualización de firmware, o si se conectó anteriormente a otro router, lo que hace que falle la verificación de la clave del host.

        ![warning](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Para solucionarlo, abra File Explorer, vaya a `C:\Users\Administrator\.ssh` y busque un archivo llamado **known_hosts**.

        ![known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Haga doble clic en el archivo known_hosts y ábralo con Notepad.

        ![open with notepad](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Elimine la entrada relacionada con la dirección IP del router, por ejemplo 192.168.8.1, y guarde el archivo. Después salga de File Explorer.

        ![delete known hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        De vuelta en PowerShell, use el comando `ssh root@192.168.8.1` para conectarse de nuevo al router. Se le pedirá que confirme la conexión. Escriba `yes` y pulse Enter, luego introduzca la contraseña de inicio de sesión del router. Después iniciará sesión correctamente en el terminal del router.

    2. **¿Qué debo hacer si cambié el puerto SSH del router?**

        Si ha cambiado el puerto SSH del router, especifique el puerto mediante el parámetro "-p" al usar el comando ssh. Por ejemplo:

        ``ssh -p [new port number] [username]@[router IP address]``

### Usar Bitvise

Vea este video para iniciar sesión en su router mediante Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Usar PuTTY

1. Descargar PuTTY

   Descargue la versión más reciente de PuTTY desde [aquí](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Instalar PuTTY

   ![Putty Install 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

   ![Putty Install 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

   ![Putty Install 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

   ![Putty Install 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Iniciar PuTTY

   Haga clic en **PuTTY** desde el menú Start.

   ![Launch Putty](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

   Verá la siguiente ventana de configuración.

   ![Setup Putty 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

   Introduzca Host Name, o la dirección IP, `192.168.8.1`, deje Port con el valor predeterminado `22` y seleccione `SSH` como tipo de conexión.

   Introduzca `Your Session` en saved sessions y pulse `Save`.

   Luego haga clic en `Open` en la parte inferior.

   ![Setup Putty 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

   Aparecerá una alerta de seguridad como la que se muestra a continuación. Haga clic en `Yes`.

   ![Setup Putty 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

   login as: `root`

   Después introduzca la contraseña de administración. **Por seguridad, la contraseña no se muestra en pantalla**.

   ![SSH login successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

   Cuando vea la imagen anterior, significará que ha iniciado sesión correctamente en el router por SSH.

---

## Para usuarios de Linux y Mac

El proceso en Linux y macOS es, por lo general, el mismo. A continuación se usa Ubuntu como ejemplo.

### Usar Ubuntu

1. Abrir Terminal.

   Inicie Ubuntu. Haga doble clic en el icono Terminal para abrirlo.

   ![Run Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Iniciar sesión en el router.

   Introduzca el comando de inicio de sesión SSH: `ssh root@192.168.8.1`

   ![Ubuntu sshin router 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

   El sistema le pedirá que confirme la conexión. Escriba `yes` y pulse Enter.

   ![Ubuntu sshin router 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

   Después introduzca la contraseña de administración del router. **Por seguridad, la contraseña no se muestra en pantalla**.

   ![Ubuntu sshin router 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

   Cuando vea la imagen anterior, significará que ha iniciado sesión correctamente en el router.

??? "Solución de problemas"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Esto ocurre si la clave de seguridad del router cambió, por ejemplo tras un restablecimiento de fábrica o una actualización de firmware, o si se conectó anteriormente a otro router, lo que provoca que falle la verificación de la clave del host.

        ![remove_ssh_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        Si esto sucede, ejecute el comando que aparece en el recuadro rojo de arriba. Copie exactamente el comando que se muestra en el terminal.

        `ssh-keygen -f "~/.ssh/known_hosts" -R "192.168.8.1"`

        ![removed_host_keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Luego intente conectarse de nuevo.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**

        Puede encontrar este error al conectarse. Se debe a un cambio en el paquete OpenSSH a partir de la versión 8.8. Para solucionarlo, abra el archivo **~/.ssh/config** con un editor de texto, por ejemplo Nano o Vim, y añada las siguientes líneas:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Asegúrese de cambiar la IP del host si no es la predeterminada.

        Para más información sobre este problema, consulte [aquí](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
