# Drop-in Gateway

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway es una función de ampliación que permite añadir capacidades a un router principal ya existente sin sustituirlo ni reconfigurarlo. Al conectar el router GL.iNet al router principal mediante un cable Ethernet, los usuarios pueden agregar funciones avanzadas a la infraestructura de red existente, por ejemplo:

- Filtrar anuncios mediante AdGuard Home
- Habilitar un cliente VPN
- Usar DNS cifrado

Se recomienda utilizar un router o gateway de seguridad de mayor rendimiento y con memoria suficiente, por ejemplo GL-MT2500 o GL-MT5000, e instalar herramientas adicionales de control y reenvío de tráfico según sea necesario.

## Topología de red

Drop-in Gateway funciona como un sistema de red intermedio, encaminando el tráfico de datos de los dispositivos cliente a través del router GL.iNet para su procesamiento antes de transmitirlo por medio del router principal. Durante este proceso, no solo conserva la configuración de red existente, como el SSID y la contraseña, para garantizar una conectividad ininterrumpida de todos los dispositivos conectados, sino que también le permite gestionar el tráfico de red de todos los clientes o solo de determinados dispositivos según sea necesario.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

El diagrama anterior consta de dos tipos de líneas: líneas grises y líneas verdes marcadas con tres flechas, cada una con un número correspondiente.

1. Las **líneas grises** ilustran la topología de conexión física: los dispositivos cliente, por ejemplo un ordenador o un portátil, se conectan al router principal, y el puerto LAN del router principal se conecta al puerto WAN del router GL.iNet, con Drop-in Gateway habilitado, mediante un cable Ethernet.

2. Las **líneas verdes** representan la ruta secuencial de transmisión de datos cuando Drop-in Gateway está activo, y las flechas numeradas indican el orden del flujo de tráfico:
   1. El tráfico de los dispositivos cliente se enruta primero al router principal;

   2. El router principal reenvía el tráfico al router GL.iNet para su procesamiento, por ejemplo filtrado de anuncios o cifrado VPN;

   3. Tras el procesamiento, el tráfico se envía de vuelta al router principal, que luego entrega los datos finales a los dispositivos cliente originales o los enruta hacia Internet.

## Configuración

Hay dos modos de despliegue para distintos escenarios de aplicación: todos los dispositivos cliente pasan por Drop-in Gateway, o solo determinados dispositivos cliente pasan por Drop-in Gateway.

En el siguiente ejemplo, la dirección de gateway del router principal es `192.168.1.1`.

### Todos los dispositivos pasan por Drop-in Gateway

1.  Conecte el puerto LAN del router principal al puerto WAN del router GL.iNet mediante un cable Ethernet.

2.  Inicie sesión en el panel de administración web del router GL.iNet, habilite Drop-in Gateway y el sistema generará automáticamente los parámetros de configuración correspondientes.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}
    - **IP Address** se refiere a la dirección IP WAN del router GL.iNet, asignada dinámicamente por el router principal. Esta IP WAN puede verse en la sección Ethernet de la página [INTERNET](internet_ethernet.md).

    - Los campos **Gateway** y **DNS Server 1** se rellenan automáticamente con la dirección IP del router principal de forma predeterminada. Si estos parámetros no están configurados correctamente, puede ajustarlos manualmente según sea necesario.

    Anote aquí la dirección IP, ya que la utilizará en los siguientes pasos.

    Seleccione el primer método de configuración y haga clic en **Apply**.

3.  Inicie sesión en el panel de administración web de su router principal.

    ??? "GL.iNet"

        Si su router principal es un GL.iNet y ejecuta firmware v4.2 o superior, siga los pasos siguientes.

        Inicie sesión en el panel de administración web -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Introduzca en DHCP Gateway la dirección **IP Address** del paso 2, por ejemplo `192.168.1.23`, y haga clic en **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Si su router principal es TP-Link, siga los pasos siguientes, tomando como ejemplo el TP-LINK Archer C3150.

        Inicie sesión en la página de administración de TP-Link, vaya a **Advanced** -> **Network** -> **DHCP Server** y desactive **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Luego haga clic en **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Si su router principal es Linksys, siga los pasos siguientes, tomando como ejemplo Linksys WHW01.

        Inicie sesión en la página de administración de Linksys y vaya a **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Haga clic en la pestaña **Local Network**, desactive **DHCP Server** y luego haga clic en **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Aparecerá una advertencia. Haga clic en **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Inicie sesión en el panel de administración del router principal para desactivar su servidor DHCP. Puede consultar el manual de usuario del fabricante correspondiente o ponerse en contacto con su servicio de soporte.

4.  Vuelva al router GL.iNet y configure funciones como [AdGuard Home](adguardhome.md), [DNS cifrado](dns.md), [WireGuard Client](wireguard_client.md) y [OpenVPN Client](openvpn_client.md).

### Solo determinados dispositivos pasan por Drop-in Gateway

1.  Conecte el puerto LAN del router principal al puerto WAN del router GL.iNet mediante un cable Ethernet.

2.  Inicie sesión en el panel de administración web del router GL.iNet, habilite Drop-in Gateway y el sistema generará automáticamente los parámetros de configuración correspondientes.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}
    - **IP Address** se refiere a la dirección IP WAN del router GL.iNet, asignada dinámicamente por el router principal. Esta IP WAN puede verse en la sección Ethernet de la página [INTERNET](internet_ethernet.md).

    - Los campos **Gateway** y **DNS Server 1** se rellenan automáticamente con la dirección IP del router principal de forma predeterminada. Si estos parámetros no están configurados correctamente, puede ajustarlos manualmente según sea necesario.

    Anote aquí la dirección IP, ya que la utilizará en los siguientes pasos.

    Seleccione el segundo método de configuración y haga clic en **Apply**.

3.  Configure el gateway y el DNS del dispositivo en el que desea usar la función Drop-in Gateway con la dirección IP que aparece en la página Drop-in Gateway.

    ??? "Windows"

        A continuación se muestra un ejemplo con Windows 11; en Windows 10 el proceso es similar. Asegúrese de que el PC esté conectado al router principal. Aquí se asume que el ordenador está conectado al router principal mediante un cable de red, pero la configuración es similar si se conecta por Wi-Fi.

        1. Abra Settings.

        2. Haga clic en **Network & Internet**.

        3. Haga clic en la pestaña **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Encontrará la dirección IP de este PC. En la sección "IP assignment", haga clic en el botón **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Seleccione la opción **Manual**. Active el interruptor **IPv4 toggle**.

        6. Configure **IP address** con la IP que ve en el paso 4, configure **Subnet mask** como `255.255.255.0` y configure tanto **Gateway** como **Preferred DNS** con la dirección IP mostrada en la página Drop-in Gateway.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Haga clic en el botón **Save**.

    ??? "Android"

        A continuación se muestra un ejemplo con un Samsung S21. Asegúrese de que el smartphone esté conectado al router principal.

        1. Abra Settings y pulse Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Pulse Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Pulse el icono de engranaje del SSID actual.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Pulse **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Pulse **IP settings** y elija **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Configure **Gateway** y **DNS 1** con la dirección IP que aparece en la página Drop-in Gateway y luego pulse **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        A continuación se muestra un ejemplo con iOS 16.3 en un iPhone 8. Asegúrese de que el smartphone esté conectado al router principal.

        1. Abra Settings y pulse Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Pulse el SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Desplácese hacia abajo y verá que **Configure IP** está en **Automatic**. Anote **IP Address** y **Subnet Mask** para el siguiente paso.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Cambie **Configure IP** a **Manual**, configure **IP Address** y **Subnet Mask** con los mismos valores obtenidos en el paso anterior y configure **Router** con la dirección IP mostrada en la página Drop-in Gateway; luego pulse **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Pulse **Configure DNS** y cámbielo a **Manual**. Pulse **Add Server**, configure la IP del servidor DNS con la dirección IP mostrada en la página Drop-in Gateway y luego pulse **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4.  Vuelva al panel de administración web del router GL.iNet y configure las funciones que necesite, como [AdGuard Home](adguardhome.md), [DNS cifrado](dns.md), [WireGuard Client](wireguard_client.md) y [OpenVPN Client](openvpn_client.md).

## Precauciones

1. Habilitar Drop-in Gateway incrementa la latencia de red.

2. Cuando Drop-in Gateway está habilitado, la transmisión de datos entre los dispositivos LAN seleccionados también se enruta a través del drop-in gateway. Por lo tanto, el ancho de banda entre el router principal y el drop-in gateway afecta al ancho de banda total de la LAN.

---

Artículo relacionado:

- [How to set up drop-in gateway on a GL.iNet router](../tutorials/how_to_set_up_drop_in_gateway.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
