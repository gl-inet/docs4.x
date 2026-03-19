# Cómo bloquear dispositivos cliente específicos en un router GL.iNet

Este tutorial le mostrará cómo bloquear dispositivos cliente específicos en un router GL.iNet. Al bloquear dispositivos cliente, evita accesos no autorizados a su red. Esto ayuda a reforzar la seguridad de la red o a controlar el acceso de su familia a Internet.
Los routers GL.iNet bloquean dispositivos cliente en función de sus direcciones MAC, que son identificadores únicos de 12 caracteres asignados a cada dispositivo dentro de una red. Este método también se conoce como filtrado por dirección MAC.
Hay dos formas de bloquear dispositivos cliente en su router GL.iNet: mediante el [panel de administración del router](#block-client-devices-via-the-admin-panel) o mediante la [aplicación móvil de GL.iNet](#block-client-devices-via-the-glinet-mobile-app).

## Bloquear dispositivos cliente mediante el panel de administración {#block-client-devices-via-the-admin-panel}

### 1. Iniciar sesión en el panel de administración

En un navegador web, introduzca `192.168.8.1`. Introduzca su contraseña y haga clic en **Login**.

### 2. Bloquear dispositivos cliente

Hay dos formas de bloquear dispositivos cliente, según disponga o no de sus direcciones MAC:

* Si no dispone de sus direcciones MAC: use el [primer método](#method-1-block-devices-without-their-mac-addresses), que le permite bloquear los dispositivos que aparecen en las listas.
* Si dispone de sus direcciones MAC: use el [segundo método](#method-2-block-devices-with-their-mac-addresses).

#### Método 1: Bloquear dispositivos sin conocer sus direcciones MAC {#method-1-block-devices-without-their-mac-addresses}

1. En la barra lateral izquierda, haga clic en **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}
2. Junto al dispositivo, active el interruptor.
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}
Si no ve en las listas los dispositivos que desea bloquear, tendrá que bloquearlos [añadiendo sus direcciones MAC a la lista de bloqueo](#method-2-block-devices-with-their-mac-addresses).

#### Método 2: Bloquear dispositivos con sus direcciones MAC {#method-2-block-devices-with-their-mac-addresses}

Para usar este método, primero necesita obtener la dirección MAC del dispositivo. Consulte las instrucciones proporcionadas por el fabricante del dispositivo.
Una vez tenga la dirección MAC del dispositivo, siga estos pasos:

1. En la barra lateral izquierda, haga clic en **Clients**.
2. En la parte superior, haga clic en **Blocklist**.
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Siga uno de estos métodos para bloquear dispositivos:
    - Para introducir las direcciones MAC una a una: escríbalas en el campo vacío.
    - Para importar una lista de direcciones MAC: haga clic en **Import Clients**. Importe un archivo y luego haga clic en **Import**.
4. Haga clic en **Apply**.
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Bloquear dispositivos cliente mediante la aplicación móvil de GL.iNet {#block-client-devices-via-the-glinet-mobile-app}

**Nota:** Antes de empezar, instale y configure la aplicación móvil de GL.iNet en su dispositivo.
Hay dos formas de bloquear dispositivos cliente, según disponga o no de sus direcciones MAC:

* Si no dispone de sus direcciones MAC: use el [primer método](#mobile-1), que le permite bloquear los dispositivos que aparecen en la lista.
* Si dispone de sus direcciones MAC: use el [segundo método](#mobile-2).

### Método 1: Bloquear dispositivos sin conocer sus direcciones MAC {#mobile-1}

1. En la pantalla principal de la aplicación, toque el dispositivo que desea bloquear en **Connected Clients** y **Office Clients**.
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}
2. En **Settings**, active el interruptor **Block**.
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}
Si no ve en las listas los dispositivos que desea bloquear, tendrá que bloquearlos [añadiendo sus direcciones MAC a la lista de bloqueo](#method-2-block-devices-with-their-mac-addresses-1).

### Método 2: Bloquear dispositivos con sus direcciones MAC {#mobile-2}

Para usar este método, primero necesita obtener la dirección MAC del dispositivo que desea bloquear. Consulte las instrucciones proporcionadas por el fabricante.
Una vez tenga la dirección MAC del dispositivo, siga estos pasos:

1. En la pantalla principal de la aplicación, toque el icono de Settings > **Access Control**.
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}
2. Toque **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}
3. Siga uno de estos métodos para bloquear dispositivos:
    - Para introducir las direcciones MAC una a una: toque **Add MAC address**. Introduzca la dirección MAC y después toque **Done**.
    - Para importar una lista de direcciones MAC: pulse **Import Clients** > **Import Clients**. Toque un archivo.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
