# El servidor WireGuard de mi router GL.iNet no funciona correctamente

Hay varias razones por las que el servidor WireGuard que ha configurado en su router GL.iNet puede no estar funcionando correctamente.

Si encuentra problemas, siga estos pasos de solución de problemas según su situación específica.

#### Situación 1: El servidor WireGuard se inicia, pero no se puede conectar

??? "Siga estos pasos"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    Es posible que el reenvío de puertos que configuró en su router principal, conectado a su router secundario, GL.iNet, no esté funcionando correctamente.
    Para comprobar si el reenvío de puertos funciona correctamente, intente reenviar el puerto HTTPS del router principal a su servidor WireGuard. Siga estos pasos:

    1. Reenvíe el puerto HTTPS de su router principal a su servidor WireGuard

        1. Inicie sesión en el panel de administración de su router principal.
        2. Vaya a la pantalla de reenvío de puertos.
        3. Cree un puerto nuevo y asígnele el nombre **HTTPS**.
        4. Introduzca la siguiente información:
            * **External port/Internal port:** introduzca **443**.
            * **Protocol:** elija **All** o **UDP/TCP**.
            * **Internal IP** o mostrado como **Host IP**: introduzca la dirección IP WAN de su router secundario o selecciónelo en la lista desplegable si está disponible.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Habilite DDNS y el acceso remoto por HTTPS, en el router GL.iNet

        1. En un navegador web, introduzca la URL del panel de administración de su router GL.iNet, por ejemplo, 192.168.8.1, e inicie sesión.
        2. En la barra lateral izquierda, haga clic en **Applications** > **Dynamic DNS**.
        3. Active **Enable DDNS** y marque la casilla **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Guarde el hostname en algún lugar porque lo necesitará más adelante y luego haga clic en **Apply**.
        5. En la barra lateral izquierda, haga clic en **System** > **Security**.
        6. En **Remote Access Control**, active **HTTPS Remote Access**.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Haga clic en **Apply**.

    3. Compruebe si puede acceder al panel de administración del router GL.iNet

        1. En otro dispositivo, por ejemplo, un portátil o móvil, conéctese a otra red Wi-Fi o a la red celular.
        2. En la barra de direcciones del navegador, introduzca el hostname que guardó antes, `abcd123.glddns.com`.
        3. Haga clic en **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Haga clic en **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Si ve la pantalla de inicio de sesión de su router GL.iNet, router secundario, el reenvío de puertos configurado en el router principal está funcionando correctamente.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Si no ve la pantalla de inicio de sesión de su router GL.iNet, router secundario, el reenvío de puertos no está funcionando correctamente. Vuelva a configurar el reenvío de puertos o asegúrese de utilizar como router principal un equipo que disponga de esta función y funcione correctamente.

#### Situación 2: El servidor WireGuard muestra que mi cliente VPN está conectado, pero el cliente VPN no puede acceder a Internet

??? "Siga estos pasos"

    Siga los pasos indicados para cada posible causa y compruebe si el problema se resuelve. Si se resuelve, puede omitir el resto de la sección.

    **Posible causa 1: Es posible que su proveedor de servicios de Internet no pueda resolver los servidores DNS de GL.iNet**

    Intente configurar manualmente las direcciones de los servidores DNS siguiendo estos pasos:

    1. En un navegador web, introduzca la URL del panel de administración de su router GL.iNet, por ejemplo, 192.168.8.1, e inicie sesión.
    2. En la barra lateral izquierda, haga clic en **Network** > **DNS**.
    3. En **Mode**, seleccione **Manual DNS**.
    4. En **DNS Server 1**, seleccione **Google Public DNS**.
    5. Haga clic en **Apply**.

    **Posible causa 2: La IP de gateway de su router principal entra en conflicto con la dirección IP del servidor WireGuard**

    Intente cambiar la dirección IPv4 siguiendo estos pasos:

    1. En un navegador web, introduzca la URL del panel de administración de su router GL.iNet, por ejemplo, 192.168.8.1, e inicie sesión.
    2. En la barra lateral izquierda, haga clic en **VPN** > **WireGuard Server**.
    3. En la pestaña **Configuration**, en el campo **IPv4 Address**, introduzca una nueva dirección IP, por ejemplo, `10.1.0.1/24`.
    4. Haga clic en **Apply**.

    **Posible causa 3: Si tanto el servidor WireGuard como el cliente WireGuard se configuraron en routers GL.iNet, sus direcciones IP LAN entran en conflicto**

    Intente cambiar la dirección IP LAN en cualquiera de los dos routers siguiendo estos pasos:

    1. En un navegador web, inicie sesión en el panel de administración de cualquiera de los dos routers GL.iNet, por ejemplo, 192.168.8.1.
    2. En la barra lateral izquierda, haga clic en **Network** > **LAN**.
    3. En el campo **Router IP address**, introduzca una nueva dirección IP LAN, por ejemplo, `192.168.10.1`.
    4. Haga clic en **Apply**.

    **Posible causa 4: Se actualizó la dirección IP del servidor WireGuard, pero falta la subred**

    Añada una subred a la dirección IP de su servidor WireGuard siguiendo estos pasos:

    1. En un navegador web, introduzca la URL del panel de administración de su router GL.iNet, por ejemplo, 192.168.8.1, e inicie sesión.
    2. En la barra lateral izquierda, haga clic en **VPN** > **WireGuard Server**.
    3. En la pestaña **Configuration**, en el campo **IPv4 Address**, añada **/24** después de **10.0.0.1**.
    4. Haga clic en **Apply**.

#### Situación 3: El servidor WireGuard está en ejecución, pero no puedo conectar mi cliente VPN a él

??? "Siga estos pasos"

    Siga los pasos indicados para cada posible causa y compruebe si el problema se resuelve. Si se resuelve, puede omitir el resto de la sección.

    **Posible causa 1: Es posible que el reenvío de puertos que configuró en su router principal no esté funcionando correctamente**

    Para comprobar si el reenvío de puertos funciona correctamente, intente reenviar el puerto HTTPS a su servidor WireGuard siguiendo los pasos de resolución descritos en la Situación 1.

    **Posible causa 2: Puede que no disponga de una dirección IP pública**

    Para comprobarlo, consulte esta [página](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Posible causa 3: Si tanto el servidor WireGuard como el cliente WireGuard se configuraron en routers GL.iNet, sus direcciones IP LAN entran en conflicto**

    Cambie la dirección IP LAN en cualquiera de los dos routers siguiendo estos pasos:

    1. En un navegador web, inicie sesión en el panel de administración de cualquiera de los dos routers GL.iNet, por ejemplo, 192.168.8.1.
    2. En la barra lateral izquierda, haga clic en **Network** > **LAN**.
    3. En el campo **Router IP address**, introduzca una nueva dirección IP LAN, por ejemplo, `192.168.10.1`.
    4. Haga clic en **Apply**.

    **Posible causa 4: El dispositivo que está usando para conectarse al servidor WireGuard está conectado a su red Wi-Fi o a su puerto LAN**

    Conecte su dispositivo a otra red Wi-Fi o a la red celular.

    **Posible causa 5: Puede que falten algunas líneas en el archivo de configuración que cargó en el dispositivo cliente**

    Vuelva a cargar la información de configuración.

#### Situación 4: El servidor WireGuard está conectado, pero la conexión no es estable

??? "Siga estos pasos"

    Siga los pasos siguientes para resolver el problema. Después de cada paso, compruebe si se ha resuelto. Si se resuelve, puede omitir el resto de los pasos.

    1. En su dispositivo cliente VPN, cambie el MTU de **1420** a un valor más bajo, por ejemplo, **1380**.
    2. En su router principal, habilite la función de VPN passthrough si está disponible.
    3. Intente configurar manualmente los servidores DNS en su router GL.iNet siguiendo estos pasos:
        1. En un navegador web, introduzca la URL del panel de administración de su router GL.iNet, por ejemplo, 192.168.8.1, e inicie sesión.
        2. En la barra lateral izquierda, haga clic en **Network** > **DNS**.
        3. En **Mode**, seleccione **Manual DNS**.
        4. En **DNS Server 1**, seleccione **Google Public DNS**.
        5. Haga clic en **Apply**.

#### Situación 5: El servidor WireGuard dejó de funcionar de repente

??? "Siga estos pasos"

    Siga los pasos indicados para cada posible causa y compruebe si el problema se resuelve. Si se resuelve, puede omitir el resto de la sección.

    **Posible causa 1: Puede haber un corte de electricidad en el lugar donde configuró el servidor WireGuard**

    Compruebe si su servidor WireGuard sigue en línea siguiendo los pasos de resolución de la Situación 1 o mediante [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/), si conectó previamente su router a este servicio.

    **Posible causa 2: No habilitó el Dynamic DNS, DDNS**

    Si tiene una dirección IP dinámica, lo más probable, tendrá que habilitar DDNS. [Habilite DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) y siga el resto de los pasos para configurar de nuevo el servidor WireGuard.

    **Posible causa 3: El reenvío de puertos dejó de funcionar por razones desconocidas**

    [Configure el reenvío de puertos](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) de nuevo con otro puerto.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
