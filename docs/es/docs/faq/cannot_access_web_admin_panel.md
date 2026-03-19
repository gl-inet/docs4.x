# No se puede acceder al panel de administración web

A veces no es posible acceder a [http://192.168.8.1](http://192.168.8.1), por lo que no se puede iniciar sesión en el panel de administración web. Puede haber varias razones.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Posibles causas

- Su ordenador o teléfono móvil no está conectado al router.
- `192.168.8.1` es la dirección IP predeterminada del router. Es posible que haya cambiado esta IP.
- La caché o una extensión del navegador pueden impedir el acceso al panel de administración.
- El software VPN o proxy gestiona su tráfico, lo que puede impedir el acceso al panel de administración.
- El router ha quedado bloqueado.

## Compruebe los pasos generales para acceder al panel de administración web

1. Encienda el router sin conectarlo a ningún otro dispositivo.
2. Conecte su móvil u ordenador portátil al Wi-Fi del router e introduzca la clave Wi-Fi impresa en la etiqueta del router.
3. Si el paso 2 falla, desactive el Wi-Fi en su ordenador o portátil. En su lugar, conéctelo al puerto LAN del router mediante un cable Ethernet.
4. Abra un navegador, escriba `192.168.8.1` en la barra de direcciones y pulse Intro. Debería poder acceder al panel de administración web de GL.iNet.

O bien puede utilizar [la aplicación](mobile_app.md) para acceder al router.

## Otros pasos para solucionar este problema

1. [Comprobar la conexión](#comprobar-la-conexion)
2. [Comprobar la dirección IP del router](#comprobar-la-direccion-ip-del-router)
3. [Acceder a la dirección IP del router](#acceder-a-la-direccion-ip-del-router)

---

### Comprobar la conexión

Si está conectado mediante un cable Ethernet, asegúrese de que la conexión de los puertos WAN/LAN del router sea correcta:

- El puerto WAN está conectado a una fuente de Internet, como un módem o un router principal.
- El puerto LAN está conectado al dispositivo terminal, como su ordenador portátil.

Si está conectado por Wi-Fi, asegúrese de haber seleccionado el SSID correcto en su dispositivo y de haber introducido la contraseña correcta.

### Comprobar la dirección IP del router

Siga los pasos que se indican a continuación para comprobar la dirección IP del router.

=== "Windows 10 / Windows 11"

    Abra el Panel de control y asegúrese de que, en la esquina superior derecha, esté seleccionada la vista por iconos grandes o iconos pequeños.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    Panel de control -> Centro de redes y recursos compartidos -> Haga clic en la conexión. Puede que tenga varias conexiones; elija la correspondiente al router que desea comprobar.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Aparecerá un cuadro de diálogo con el estado de la conexión. Haga clic en el botón de detalles.

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    Aparecerá un cuadro de diálogo con los detalles de la conexión de red. La dirección IP del router es la **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Panel de control -> Red e Internet -> Centro de redes y recursos compartidos -> Cambiar configuración del adaptador

    Haga clic con el botón derecho en la red -> Estado -> Detalles

    La dirección IP del router es la **IPv4 Default Gateway**

    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. Preferencias del Sistema -> Red

    2. En la columna izquierda, haga clic en la conexión de red. En una conexión Ethernet, se mostrará la dirección IP del router.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Para una conexión Wi-Fi, haga clic en el botón "Advanced..." y luego en la pestaña "TCP/IP" en la parte superior de la ventana. Se mostrará la dirección IP del router.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Ajustes -> Wi-Fi
    2. Toque el icono de información (una "i" azul dentro de un círculo) del Wi-Fi actualmente conectado. Se mostrará la dirección IP del router.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Esto puede variar según el dispositivo Android.

    1. Ajustes -> Network & internet
    2. Toque Wi-Fi y busque la red a la que está conectado; haga clic en el icono de configuración para administrar sus ajustes.
    3. Toque el menú desplegable Advanced. Si se le ofrecen opciones de IP estática o dinámica, seleccione Static.
    4. En cualquier caso, debería ver la IP de su router en Gateway.

### Acceder a la dirección IP del router

1. Utilice Chrome, Edge o Safari para acceder al panel de administración del router y obtener una mejor compatibilidad.

2. Para evitar problemas causados por la caché y las extensiones del navegador, abra una ventana de incógnito y vuelva a intentar acceder a la dirección IP del router.

3. Desactive cualquier software VPN o proxy, incluidos Tailscale y ZeroTier.

4. Si está usando un teléfono móvil, desactive los datos móviles.

   Algunos teléfonos inteligentes se desconectan del Wi-Fi del router y utilizan datos móviles cuando detectan que el router no tiene Internet. Sin embargo, desconectarse del router impedirá el acceso al panel de administración web.

5. Si los pasos anteriores no funcionan, intente [restablecer](repair_network_or_reset_firmware.md#reset-to-factory) el router a los valores predeterminados de fábrica.

6. Si el restablecimiento no funciona, pruebe [Desbloqueo mediante uboot](debrick.md).

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
