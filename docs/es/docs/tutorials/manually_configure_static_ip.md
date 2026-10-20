# ¿Cómo configurar manualmente una IP estática en los dispositivos cliente?

=== "Windows 11"

    En Windows 11, puede configurar una dirección IP estática tanto para adaptadores inalámbricos como cableados.

    **Configurar una IP estática en el adaptador Wi-Fi**

    1. En un PC con Windows 11, vaya a **Settings** -> **Network & internet** -> **Wi-Fi** y seleccione la conexión Wi-Fi actual.

    2. Busque **IP assignment** y haga clic en el botón **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. En la ventana emergente, seleccione **Manual** y active **IPv4**.

        ![Configuración IP manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Siga estos pasos para editar la configuración IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Defina una dirección IP estática, por ejemplo, `10.1.4.119`.

        - Subnet mask: Especifique una máscara de subred, por ejemplo, `255.255.255.0`.

        - Gateway: Introduzca la dirección de la puerta de enlace, que normalmente es la IP LAN del router en la misma subred. Por ejemplo, si su IP es `10.1.4.119`, la puerta de enlace suele ser `10.1.4.1`.

        - Preferred DNS: Especifique una dirección DNS preferida (obligatoria). Puede utilizar un servidor DNS público, como el servidor DNS de Google `8.8.8.8`.

        - Alternate DNS: Especifique una dirección DNS alternativa (opcional).

        - DNS over HTTPS: Seleccione "Off". Hay tres opciones:

            - Off: transmite todo el tráfico DNS sin cifrado.

            - On (automatic template): envía todo el tráfico DNS con cifrado.

            - On (manual template): permite especificar una plantilla concreta. Solo es necesario si el servicio DNS no funciona automáticamente o dispone de una plantilla que funciona como se espera.

        - Desactive el interruptor "Fallback to plaintext" si habilita DNS over HTTPS.

            **Consejo**: Si habilita esta función, el sistema cifrará el tráfico DNS, pero permitirá enviar consultas sin cifrado.

    5. Haga clic en **Save** para aplicar la configuración.

        Cuando termine estos pasos, la configuración de red estática se aplicará al equipo. Puede probar la nueva configuración abriendo el navegador web y cargando un sitio web.

    ---

    **Configurar una IP estática en el adaptador Ethernet**

    1. En un PC con Windows 11, vaya a **Settings** -> **Network & internet** -> **Ethernet**.

    2. Busque **IP assignment** y haga clic en el botón **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. En la ventana emergente, seleccione **Manual** y active **IPv4**.

        ![Configuración IP manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Siga estos pasos para editar la configuración IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Defina una dirección IP estática, por ejemplo, `10.1.4.119`.

        - Subnet mask: Especifique una máscara de subred, por ejemplo, `255.255.255.0`.

        - Gateway: Introduzca la dirección de la puerta de enlace, que normalmente es la IP LAN del router en la misma subred. Por ejemplo, si su IP es `10.1.4.119`, la puerta de enlace suele ser `10.1.4.1`.

        - Preferred DNS: Especifique una dirección DNS preferida (obligatoria). Puede utilizar un servidor DNS público, como el servidor DNS de Google `8.8.8.8`.

        - Alternate DNS: Especifique una dirección DNS alternativa (opcional).

        - DNS over HTTPS: Seleccione "Off". Hay tres opciones:

            - Off: transmite todo el tráfico DNS sin cifrado.

            - On (automatic template): envía todo el tráfico DNS con cifrado.

            - On (manual template): permite especificar una plantilla concreta. Solo es necesario si el servicio DNS no funciona automáticamente o dispone de una plantilla que funciona como se espera.

        - Desactive el interruptor "Fallback to plaintext" si habilita DNS over HTTPS.

            **Consejo**: Si habilita esta función, el sistema cifrará el tráfico DNS, pero permitirá enviar consultas sin cifrado.

    5. Haga clic en **Save** para aplicar la configuración.

        Cuando termine estos pasos, la configuración de red estática se aplicará al equipo. Puede probar la nueva configuración abriendo el navegador web y cargando un sitio web.

=== "macOS"

    Así puede configurar una dirección IP estática en macOS.

    En el menú Apple, seleccione **System Preferences**.

    Seleccione **Network** y aparecerá la siguiente página. En la barra lateral, seleccione una interfaz de red activa, como **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Tome nota de la dirección IP actual asignada a su Mac. Tendrá que elegir una nueva dirección IP dentro del rango de direcciones IP privadas indicado.

    Haga clic en **Advanced** en la esquina inferior derecha.

    A continuación, seleccione **TCP/IP** y aparecerá la siguiente página.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: Seleccione "Manually".

    - IPv4 Address: Introduzca una dirección IP estática. Mantenga los tres primeros octetos de su IP actual y cambie el último por un valor sin usar. Por ejemplo, en la red `192.168.7.0/24`, elija una dirección de `192.168.7.2` a `192.168.7.254` que no esté en uso (evite `.1`, que corresponde al router). No utilice `192.168.7.0` ni `192.168.7.255`.

    - Subnet Mask: Introduzca `255.255.255.0` (o la máscara de subred proporcionada por su administrador de red).

    - Router: Introduzca la dirección IP LAN del router, por ejemplo, `192.168.7.1`.

    Haga clic en **OK** y después en **Apply**.

=== "iOS"

    Los pasos pueden variar según la versión de iOS. Los siguientes pasos se basan en iOS 26.2.2.

    1. Vaya a **Settings** -> **WLAN**. Toque el icono azul de información (i) situado junto a la red Wi-Fi conectada actualmente.

        ![IP estática en iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Desplácese hasta **IPv4 Address** y establezca **Configure IP** en **Manual**.

        ![IP estática en iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Especifique los valores de **IP Address**, **Subnet Mask** y **Router IP** que desea utilizar en su iPhone/iPad y toque **Save** en la esquina superior derecha.

        ![IP estática en iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Los pasos pueden variar según la versión de Android. Los siguientes pasos se basan en Android 11.

    1. Vaya a **Settings** -> **Network & Internet** -> **Wi-Fi**. Toque la red conectada actualmente para abrir el menú de configuración.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Toque el icono del lápiz en la esquina superior derecha para acceder a la configuración de red.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Toque **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Toque **IP Settings** y seleccione **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Introduzca la **IP address**. El campo **Gateway** debería rellenarse automáticamente en función de la dirección IP. Si no es así, introduzca la puerta de enlace de su red. Normalmente es la IP LAN del router en la misma subred.

        **Consejo**: Cuando use direcciones IP estáticas en redes domésticas y otras redes privadas, elija una dirección de host sin usar en la subred actual. Los rangos estándar de direcciones IP privadas son:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Toque **Save** y espere a que la red vuelva a conectarse.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
