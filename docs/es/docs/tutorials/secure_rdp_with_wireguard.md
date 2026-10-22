# Proteger RDP desde una red externa con WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Es posible que necesite acceder de forma remota a su PC desde una red externa, o viceversa. La forma más segura es hacerlo mediante su propio túnel WireGuard. Esto ofrece más seguridad que usar redirección de puertos y acceder al PC directamente a través de su dirección IP pública. Después de configurar el túnel, puede usar **Windows Remote Desktop** para acceder a su PC desde cualquier lugar.

Este tutorial utiliza dos routers GL.iNet como ejemplo para mostrar cómo proteger Windows RDP mediante una red WireGuard.

## Topología {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Pasos de configuración {#setup-steps}

1. Configure su red WireGuard.

    Primero, configure su propio servidor WireGuard y cliente WireGuard con dos routers GL.iNet. Consulte [Crear su propio servidor WireGuard con dos routers GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Permita que el servidor WireGuard acceda a la LAN del cliente.

    Para habilitar el acceso bidireccional entre el servidor y el cliente, primero permita que el servidor acceda a la LAN del cliente. Consulte [Acceder a la LAN del cliente WireGuard desde el servidor](wireguard_server_access_to_client_lan_side.md).

    Los pasos pueden variar según la versión del firmware.

3. Permita que el cliente WireGuard acceda a la LAN del servidor.

    Este paso puede variar según la versión del firmware. Seleccione a continuación la versión del firmware del router configurado como cliente WireGuard.

    ??? note "Para firmware v4.7 y anteriores"

        Inicie sesión en el cliente WireGuard y vaya a **VPN** -> **VPN Dashboard**. Busque **VPN Server** y haga clic en el icono de engranaje de la derecha.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        En la ventana emergente, active **Remote Access LAN** y haga clic en **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Para firmware v4.8 y posteriores"

        Inicie sesión en el cliente WireGuard y vaya a **VPN** -> **WireGuard Server**. Haga clic en **Options** en la esquina superior derecha.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        En la ventana emergente, active **Allow Remote Access to the LAN Subnet** y haga clic en **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Conecte el equipo al que desea acceder al servidor VPN y averigüe su dirección IP de LAN.

    En el siguiente ejemplo, la dirección IP del PC del lado del servidor es **192.168.29.123**.

5. Configure el PC del lado del servidor para que sea accesible.

    En el PC del lado del servidor, vaya a **System Settings** y haga clic en **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Active **Remote Desktop** y haga clic en **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Acceda de forma remota desde el portátil del lado del cliente.

    Busque **Remote Desktop Connection** en la barra de búsqueda.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Abra la aplicación e introduzca la dirección IP del PC del lado del servidor, por ejemplo, **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Introduzca las credenciales del PC del lado del servidor para conectarse.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    A continuación, podrá controlar de forma remota el PC del lado del servidor.

    Si quiere hacerlo a la inversa, simplemente invierta los pasos entre el PC del servidor y el portátil del cliente.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
