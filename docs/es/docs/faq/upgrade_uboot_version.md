# Actualizar la versión de Uboot

## Advertencia

**Actualizar U-Boot es muy peligroso y, en general, no se recomienda. Si falla, su dispositivo quedará bloqueado y no habrá forma de restaurarlo. Hágalo solo cuando sea necesario o si así se lo indica el soporte de GL.iNet**.

**NO apague el equipo durante el proceso de actualización, ya que esto puede provocar que la actualización falle y que el dispositivo quede bloqueado**.

## Preparación

- Un ordenador con puerto Ethernet. Si no lo tiene, prepare un adaptador USB a Ethernet adicional.
- Un cable Ethernet.
- Descargue el archivo Uboot según las instrucciones del personal de soporte de GL.iNet. Asegúrese de estar usando el archivo Uboot correcto. Si no sabe cómo descargarlo, contáctenos por correo electrónico en support@gl-inet.com.

## Pasos de actualización

Siga los procedimientos que se indican a continuación para acceder a la página de actualización de U-Boot.

1.  Desconecte la alimentación del router. Conecte su ordenador al **puerto Ethernet LAN** del router. **DEBE** dejar **todos los demás puertos desconectados**.

    !!! note

        En algunos modelos, ciertos puertos LAN y el puerto WAN son intercambiables. No utilice ese puerto LAN. Por ejemplo, en el GL-MT6000 (Flint 2), no utilice LAN 1. Use LAN 2, LAN 3 o LAN 4 en su lugar.

2.  Mantenga presionado con firmeza el botón Reset y, al mismo tiempo, encienda el router. Si su router no tiene botón de encendido, al conectar la alimentación se encenderá automáticamente.

    Luego verá que un LED parpadea varias veces en una secuencia regular; suelte el botón cuando cambie la secuencia.

3.  Configure manualmente la dirección IP de su ordenador como **192.168.1.2**. Consulte la guía paso a paso para los distintos sistemas operativos a continuación:

    ??? "Windows 7 / Windows 10"

        1. Vaya a **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Haga clic con el botón derecho en **Local Area Connection** -> **Properties**.

        3. Haga clic en **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Configure manualmente **IP adress** como `192.168.1.2`.

        5. Configure **Subnet mask** como `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Haga clic en el botón **OK**.

    ??? "Windows 11"

        7. Abra Settings.

        8. Haga clic en **Network & Internet**.

        9. Haga clic en la pestaña **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. En la sección "IP assignment", haga clic en el botón **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Seleccione la opción **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Active el interruptor **IPv4 toggle**.

        13. Configure la **IP address** estática como **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Especifique **Subnet mask** como **255.255.255.0**.

        15. Haga clic en el botón **Save**.

    ??? "macOS"

        16. Haga clic en el icono **Apple** en la esquina superior izquierda de la pantalla y seleccione **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Haga clic en **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Haga clic en **Ethernet** a la izquierda y luego en la lista desplegable junto a **Configure IPv4**, donde debe seleccionar **Manually**. Si usa un adaptador USB a Ethernet, puede que no aparezca como Ethernet y se muestre con el nombre del adaptador.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Introduzca **IPv4 Address** como `192.168.1.2`, **Subnet Mask** como `255.255.255.0`, **Router** como `192.168.1.1` y luego haga clic en el botón Apply en la esquina inferior derecha.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4.  **Use Google Chrome o Microsoft Edge para visitar `http://192.168.1.1/uboot.html`**

    **NO use Mozilla/Firefox, ya que podría bloquear su router.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5.  Haga clic en el botón **Choose file** y seleccione el archivo Uboot que descargó.

6.  Haga clic en el botón **Update U-Boot**. NO apague el equipo durante el proceso de actualización. La actualización tardará varios minutos.

7.  Tras una actualización correcta, el router se reiniciará. En ese momento puede restaurar la configuración IP del paso 3 e intentar acceder al panel de administración web mediante **192.168.8.1**. Si puede acceder normalmente al panel de administración web, significa que el router se ha reiniciado correctamente.

    **Nota:** Puede ser necesario usar el modo incógnito o eliminar la caché y las cookies del navegador para acceder al router.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
