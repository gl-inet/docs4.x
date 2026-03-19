# Configurar WAN Ethernet cableada dual mediante un adaptador de Ethernet a USB-A

Puede configurar acceso WAN Ethernet cableado dual en un router con un solo puerto WAN mediante un adaptador de Ethernet a USB-A.
Los routers GL.iNet son compatibles con adaptadores Ethernet a USB-A comunes, lo que le permite convertir el acceso Ethernet cableado desde su router del ISP en una conexión USB a través del puerto USB del router, proporcionando un acceso Ethernet cableado adicional junto con el puerto WAN.

## Topología

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Pasos de configuración

1. Conecte el adaptador de Ethernet a USB-A al puerto USB de su router GL.iNet y conecte el otro extremo a su router del ISP.
2. Instale el controlador USB.

    Inicie sesión en el panel de administración web del router, vaya a **Application** -> **Plug-ins** e instale el controlador de red USB correspondiente a su adaptador.
    Por ejemplo, si utiliza un adaptador Realtek, instale el controlador **kmod-usb-net-rtl8152**.
    ![plugins](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}
    Espere a que finalice la instalación.

    ![installation suceeded](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}
3. Conéctese mediante USB Tethering.

    Una vez completada la instalación del controlador, vaya a **INTERNET** -> **Tethering**.
    Se detectará la conexión USB, lo que le permitirá conectarse a su router del ISP.
    ![detected](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}
    Haga clic en **Connect** y espere un minuto. Cuando se encienda un punto verde y la página muestre información como la dirección IP, significará que la conexión USB Tethering se ha establecido correctamente.
    ![tether](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
