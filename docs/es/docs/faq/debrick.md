# Usar U-Boot para recuperar un router bloqueado

Si su router quedó bloqueado debido a algún proyecto DIY o por instalar un firmware incorrecto, es posible que no pueda acceder a él. En este caso, puede reinstalar el firmware usando el modo de recuperación U-Boot failsafe.

**Nota:** La operación de U-Boot eliminará la configuración del router y los complementos instalados.

---

## Preparación

Prepare un ordenador con puerto Ethernet. Si su ordenador no tiene puerto Ethernet, prepare también un adaptador USB a Ethernet.

## Pasos para recuperar el router

Consulte este videotutorial o siga los procedimientos que se indican a continuación para acceder a la interfaz web de U-Boot y reinstalar el firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Los pasos para reinstalar el firmware mediante U-Boot son aproximadamente los mismos, y este vídeo toma como ejemplo Mudi/Mudi V2. Para otros modelos, puede seguir los procedimientos que se indican a continuación.</small>

1.  Descargue el firmware [aquí](https://dl.gl-inet.com/){target="\_blank"} en su ordenador.

    Algunos modelos, como GL-AR750S-EXT, están disponibles en dos formatos de firmware. Utilice el firmware para U-Boot, cuya extensión de archivo es **.img**.

2.  Desconecte la alimentación del router. Conecte su ordenador al **puerto LAN Ethernet** del router. **DEBE** dejar todos los demás puertos **sin conectar**.

    !!! note

        En algunos modelos, ciertos puertos LAN individuales y el puerto WAN son intercambiables. No utilice ese puerto LAN. Por ejemplo, en el GL-MT6000 (Flint 2), no use LAN 1. Use LAN 2, LAN 3 o LAN 4 en su lugar.

3.  Mantenga pulsado firmemente el botón Reset y, **al mismo tiempo, encienda el router**. Si su router no tiene botón de encendido, al conectar la alimentación se encenderá automáticamente.

    A continuación verá que el LED parpadea varias veces en una secuencia regular. Suelte el botón **después** de que cambie la secuencia.

    A continuación se describe la secuencia de parpadeo del LED de cada modelo.

    **Nota:** Los mismos modelos de router con diferentes fechas de fabricación pueden tener colores de LED o secuencias de parpadeo diferentes. Esto no afectará al proceso de U-Boot. Preste más atención al cambio en la secuencia del LED.
    - Para **GL-BE9300(Flint 3)**, el LED azul parpadea 6 veces y luego se queda en blanco fijo.

    - Para **GL-BE3600(Slate 7)**, después de mantener pulsado el botón reset durante unos 5 segundos, aparecerá una cuenta atrás de 5 segundos en la pantalla LED. Siga pulsando el botón reset hasta que aparezca el siguiente paso en la pantalla:
      1. Configure manualmente la dirección IP de su ordenador en 192.168.1.2
      2. Use el navegador para visitar http://192.168.1.1

      Pase al paso 4 para obtener más instrucciones.

    - Para **GL-B3000(Marble)**, el LED azul parpadea 7 veces y luego se queda en blanco fijo.

    - Para **GL-MT6000(Flint 2)**, el LED azul parpadea 6 veces y luego se queda en blanco fijo.

    - Para **GL-MT3000(Beryl AX)**, el LED azul parpadea 6 veces y luego se queda en blanco fijo.

    - Para **GL-MT2500/GL-MT2500A(Brume 2)**, el LED azul parpadea 5 veces y luego se queda en blanco fijo.

    - Para **GL-S200**, el LED cian parpadea 5 veces, luego se vuelve brevemente púrpura y finalmente queda fijo en cian.

    - Para **GL-A1300(Slate Plus)**, el LED parpadea lentamente 5 veces, luego permanece encendido un momento y después parpadea rápidamente de forma continua.

    - Para **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)** y **microuter-N300**, el LED parpadea 5 veces.

    - Para **GL-E750(Mudi)**, la pantalla mostrará primero "Booting", luego "Reset Counting 1 to 4" y finalmente "Please Open Web 192.168.1.1".

    - Para **GL-S1300(Convexa-S)** y **GL-B1300(Convexa-B)**, el LED parpadea 4 veces.

      El LED de alimentación situado más a la izquierda puede permanecer encendido todo el tiempo mientras el LED Wi-Fi de la derecha parpadea 4 veces; después, el LED Mesh central queda encendido de forma fija.

      Para algunos GL-B1300 antiguos, el LED de alimentación izquierdo permanece encendido todo el tiempo, mientras que el LED central y el LED derecho parpadean 5 veces simultáneamente y luego quedan encendidos.

    - Para **GL-SF1200**, el LED 5G parpadea 5 veces y luego queda fijo.

    - Para **GL-AX1800(Flint)**, el LED azul parpadea 5 veces y luego se queda en blanco fijo.

    - Para **GL-AXT1800(Slate AX)**, el LED azul parpadea 5 veces y luego queda fijo.

    - Para **GL-XE300(Puli)**, el LED LAN parpadea 5 veces y luego el LED Wi-Fi queda encendido.

    - Para **GL-X300B(Collie)**, el LED WAN parpadea 5 veces y luego el LED Wi-Fi queda encendido.

    - Para **GL-X3000(Spitz AX)**, el LED WAN parpadea 5 veces y luego el LED Wi-Fi queda encendido.

    - Para **GL-XE3000(Puli AX)**, el LED WAN parpadea 5 veces y luego el LED Wi-Fi queda encendido.

    - Para **GL-SFT1200(Opal)**, el LED azul parpadea 5 veces y luego se queda en blanco fijo.

    - Para **GL-AP1300(Cirrus)**, el LED de alimentación parpadea lentamente 5 veces, luego permanece encendido un momento y después parpadea rápidamente de forma continua.

    - Para **GL-MT1300(Beryl)**, el LED comienza en azul, parpadea dos veces lentamente, luego parpadea 5 veces más rápido y se queda en blanco fijo.

    - Para **GL-B2200(Velica)**, los dos LED comienzan en azul, luego se vuelven blancos y parpadean 5 veces, y finalmente quedan fijos en azul.

    - Para **GL-MV1000/GL-MV1000W(Brume)**, no hay señal repetitiva de parpadeo LED. Los LED de alimentación y WAN permanecerán encendidos todo el tiempo.

    - Para **GL-MiFi**, el LED parpadea 6 veces.

    - Para **GL-MT300N**, **GL-MT300A**, el LED parpadea 3 veces.

4.  Configure manualmente la dirección IP de su ordenador en **192.168.1.2**. Consulte la guía paso a paso para distintos sistemas operativos a continuación:

    ??? "Windows 7 / Windows 10"

        1. Vaya a **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Haga clic con el botón derecho en **Local Area Connection** -> **Properties**.

        3. Haga clic en **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Configure manualmente la **IP address** en `192.168.1.2`.

        5. Configure la **Subnet mask** en `255.255.255.0`.

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

        13. Establezca la **IP address** estática en **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Especifique la **Subnet mask** como **255.255.255.0**.

        15. Haga clic en el botón **Save**.

    ??? "macOS"

        16. Haga clic en el icono **Apple** situado en la esquina superior izquierda de la pantalla y seleccione **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Haga clic en **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Haga clic en **Ethernet** a la izquierda y luego en el cuadro desplegable junto a **Configure IPv4**; seleccione **Manually**. Si está utilizando un adaptador USB a Ethernet, es posible que no aparezca Ethernet y que se muestre con el nombre del adaptador USB a Ethernet.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Introduzca **IPv4 Address** como `192.168.1.2`, **Subnet Mask** como `255.255.255.0` y **Router** como `192.168.1.1`, luego haga clic en el botón Apply en la esquina inferior derecha.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5.  Use el navegador para visitar **http://192.168.1.1**. Esta es la interfaz web de U-Boot.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note

        - Si no puede acceder a la interfaz web de U-Boot, compruebe si tiene algún software VPN o proxy en ejecución. Desactive cualquier software VPN o proxy, incluidos Tailscale y ZeroTier.

        - La interfaz web de U-Boot mostrada arriba puede no ser exactamente igual a la que usted ve, porque la versión de U-Boot varía según la fecha de producción. En algunos casos extremos, recomendamos actualizar la versión de U-Boot. Consulte el tutorial [aquí](upgrade_uboot_version.md).

6.  Haga clic en el botón **Choose file** para buscar el archivo de firmware. Después haga clic en el botón **Update firmware**.

7.  Espere unos 3 minutos. No apague el dispositivo durante la actualización. El router estará listo cuando tanto el LED de alimentación como el LED Wi-Fi estén encendidos, o cuando pueda encontrar su SSID en su dispositivo.

8.  Restaure la configuración IP que realizó en el paso 4 y conecte su dispositivo a la LAN o al Wi-Fi del router. Podrá volver a acceder al router a través de **192.168.8.1**.

    **Nota:** Puede ser necesario usar el modo incógnito o eliminar la caché y las cookies del navegador para acceder al router.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
