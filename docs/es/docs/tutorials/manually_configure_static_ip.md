# ¿Cómo configurar manualmente una IP estática en los dispositivos cliente?

=== "Windows 11"

    En Windows 11, puede configurar una dirección IP estática desde la app Settings tanto para adaptadores inalámbricos como cableados.

    **Configurar una IP estática en el adaptador Wi-Fi**

    Para asignar una dirección IP estática a un adaptador Wi-Fi, siga estos pasos:

    1. Abra Settings en Windows 11 -> Network & Internet -> la pestaña Wi-Fi -> seleccione la conexión de red actual.

    2. En la sección “IP settings”, haga clic en el botón Edit.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. Siga los pasos que aparecen a continuación para configurarla:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Seleccione la opción Manual y active el interruptor IPv4.

        - Defina una dirección IP estática para Windows 11, por ejemplo, 10.1.4.119.

        - Especifique una Subnet mask, por ejemplo, 255.255.255.0.

        - Especifique una dirección Default Gateway.

        - Especifique una dirección Preferred DNS, obligatoria.

        - Opcional: especifique una dirección “Alternate DNS”.

        - Use el menú desplegable “DNS over HTTPS” y seleccione la opción Off para las direcciones preferida y alternativa, aunque también puede habilitar DoH con estas opciones:

            - Off: transmite todo el tráfico DNS sin cifrado.

            - On (automatic template): envía todo el tráfico DNS con cifrado.

            - On (manual template): permite especificar una plantilla concreta. Solo es necesario si el servicio DNS no funciona automáticamente o dispone de una plantilla que funciona como se espera.

        - Desactive el interruptor “Fallback to plaintext”, si habilitó DoH.

            - Consejo rápido: si habilita esta función, el sistema cifrará el tráfico DNS, pero permitirá enviar consultas sin cifrado.

    4. Haga clic en el botón Save.

        Cuando termine estos pasos, la configuración de red estática se aplicará al equipo. Puede probar la nueva configuración abriendo el navegador web y cargando un sitio web.


    ## **Configurar una IP estática en el adaptador Ethernet**

    Para asignar una dirección IP estática a un adaptador Ethernet por cable en Windows 11, siga estos pasos:

    1. Abra Settings -> Network & Internet -> pestaña Ethernet.

    2. En la sección “IP settings”, haga clic en el botón Edit.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. Siga los pasos que aparecen a continuación para configurarla:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Seleccione la opción Manual.

        - Active el interruptor IPv4.

        - Defina una dirección IP estática para Windows 11, por ejemplo, 10.1.4.119.

        - Especifique una Subnet mask, por ejemplo, 255.255.255.0.

        - Especifique una dirección Default Gateway.

        - Especifique una dirección Preferred DNS, obligatoria.

        - Opcional: especifique una dirección “Alternate DNS”.

        - Use el menú desplegable “DNS over HTTPS” y seleccione la opción Off para las direcciones preferida y alternativa, aunque también puede habilitar DoH con estas opciones:

            * Off: transmite todo el tráfico DNS sin cifrado.

            * On (automatic template): envía todo el tráfico DNS con cifrado.

            * On (manual template): permite especificar una plantilla concreta. Solo es necesario si el servicio DNS no funciona automáticamente o dispone de una plantilla que funciona como se espera.

        - Desactive el interruptor “Fallback to plaintext”, si habilitó DoH.

    4. Haga clic en el botón Save.

        Después de completar los pasos, puede probar la configuración abriendo un sitio web en el navegador.

=== "macOS"

    Así puede configurar una dirección IP estática en macOS:

    Si tiene un MacBook, es posible que quiera crear una nueva ubicación de red. Esto le permitirá usar la dirección IP estática en determinadas redes y no en otras.

    En el menú Apple, seleccione System Preferences.

    Seleccione Network. Aparecerá la ventana que se muestra a continuación.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    En la barra lateral, seleccione una interfaz de red activa. En este ejemplo, está conectado a una red inalámbrica, por lo que debe seleccionar Wi-Fi.

    Tome nota de la dirección IP actual asignada a su Mac. Tendrá que elegir una nueva dirección IP dentro del rango de direcciones IP privadas indicado. Esto se explica con más detalle enseguida.

    Haga clic en Advanced.

    Seleccione TCP/IP. Aparecerá la ventana que se muestra a continuación.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    En el menú Configure IPv4, seleccione Manually.

    Introduzca una dirección IP estática en el campo IPv4 Address. ¿Qué número debe introducir? Un método consiste en tomar su dirección IP actual y cambiar la última parte del número. En este ejemplo, podría elegir cualquier dirección entre 192.168.7.0 y 192.168.7.255, siempre que no estuviera ya asignada a otro dispositivo.

    Haga clic en OK -> Apply.

=== "Android"

    Los pasos pueden variar según la versión de Android. Esta documentación se basa en Android 11.

    1. Vaya a Settings -> seleccione Network & Internet, luego Wi-Fi -> toque la red conectada actualmente para abrir el menú de configuración.

    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. Para configurar una dirección IP estática, haga lo siguiente:

    - Seleccione el icono del lápiz en la parte superior derecha para acceder a la configuración de red.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Seleccione Advanced Options.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Seleccione IP Settings.

    - Cambie la configuración de DHCP a Static.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Cuando use direcciones IP estáticas en redes domésticas y otras redes privadas, deben elegirse dentro de estos rangos estándar de IP privadas: 10.0.0.0 a 10.255.255.255, 172.16.0.0 a 172.31.255.255 y 192.168.0.0 a 192.168.255.255.

    - Ahora introduzca la dirección IP.
        - Este paso depende de cada red. Por ejemplo: 192.168.1.128.

    - El Gateway debería rellenarse automáticamente en función de la dirección IP. Si no es así, copie la dirección IP y sustituya el último número por un 1.
        - Ejemplo, basándose en el caso anterior: 192.168.1.1.

    3. Toque Save y deje que la red vuelva a conectarse.

=== "iOS"

    Cuando use direcciones IP estáticas en redes domésticas y otras redes privadas, deben elegirse dentro de los siguientes rangos estándar de IP privadas:

    10.0.0.0 through 10.255.255.255
    172.16.0.0 through 172.31.255.255
    192.168.0.0 through 192.168.255.255

    Para configurar una dirección IP estática, haga lo siguiente:

    - Toque el icono Settings.

    - Vaya a Wi-Fi.

        - Toque el icono azul de información (i) situado junto al nombre de la red Wi-Fi.
            - Puede aparecer como una flecha azul si usa una versión anterior a iOS 7.

    - Vaya a la pestaña Static, como se muestra a continuación.


    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - Toque el campo IP Address.

    - Introduzca la dirección IP estática que desea usar en su iPhone o iPad.

    - Toque el campo Router.

    - Introduzca la dirección IP del router.

    - Toque Subnet Mask e introduzca la información correspondiente.

        - Normalmente será 255.255.0.0.

    - Toque el botón Wi-Fi en la esquina superior izquierda de la pantalla para guardar la configuración.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
