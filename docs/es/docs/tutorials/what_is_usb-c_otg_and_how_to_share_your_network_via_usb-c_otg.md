# Qué es USB-C OTG y cómo compartir la red mediante USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) es un estándar USB que permite a dispositivos compatibles, como routers, alternar entre los roles **Host** y **Device**. Esto permite la transmisión directa de datos y la interacción de alimentación sin un dispositivo host independiente.

Los dos modos siguientes pueden cambiarse mediante **USB OTG**:

- Cuando un dispositivo cambia al **modo Host** mediante USB OTG, actúa como host USB, inicia la transmisión de datos, suministra alimentación y controla todas las operaciones de lectura y escritura entre los dos dispositivos conectados.

- En **Device mode**, el dispositivo funciona como periférico, recibe alimentación del host y responde pasivamente a sus comandos, sin poder iniciar la comunicación por sí mismo.

## Compartir red mediante USB-C OTG en Mudi 7

El puerto USB-C compatible con OTG de Mudi 7 funciona en modo **Device** o **Host** para permitir compartir la red de forma flexible con dispositivos externos.

### Conectar a un ordenador

La mayoría de los ordenadores solo funcionan como hosts y no admiten OTG. Cuando un ordenador se conecta al router mediante USB, el router muestra una ventana de selección de modo. Puede elegir cualquier modo y Mudi 7 negociará automáticamente el rol. Después, el ordenador lo reconoce como un adaptador USB para acceso directo a Internet, sin controladores adicionales.

### Conectar a un smartphone

- **Device Mode**: Mudi 7 actúa como dispositivo USB y comparte su red con el teléfono.

- **Host Mode**: Si activa USB Tethering en el teléfono, este puede compartir su red celular con Mudi 7 mediante USB. Este enlace USB puede funcionar como una interfaz WAN independiente y permitir Multi-WAN.

!!! Note

    1. Cuando utilice la función OTG del teléfono para la interconexión, asegúrese de que el teléfono admita OTG y use un cable USB apto para datos. Los cables solo de carga no pueden transmitir señales de red.

    2. Cuando Device Mode está habilitado, el teléfono no muestra una notificación de conexión de red. Para verificar el funcionamiento, compruebe el estado de red en los ajustes del teléfono o ejecute una prueba de conectividad.

        Por ejemplo, si comparte la red de Mudi 7 con un teléfono mediante **Device Mode** (por ejemplo, iPhone 17 Pro), compruebe que Device Mode esté activo siguiendo estos pasos.

        1. Use un cable USB compatible con OTG para conectar el puerto USB 3.1 de Mudi 7 al iPhone 17 Pro.

        2. En Mudi 7, seleccione **Device Mode**.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. En los ajustes del teléfono verá que Mudi 7 proporciona acceso de red al teléfono, como se muestra en la captura siguiente.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

¿Aún tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
