# ¿Cómo usar VPN Cascading en routers GL.iNet?

## Introducción

VPN Cascading suele denominarse "Double VPN" en algunos contextos, aunque puede diferir ligeramente en los routers GL.iNet. El concepto principal se ilustra a continuación.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1, router como servidor VPN**: cuando el router actúa como servidor VPN, los clientes conectados a este servidor accederán a Internet a través de la red del ISP del router de forma predeterminada.

**VPN 2, router como cliente VPN**: el router también actúa como cliente VPN, conectándose a un servicio VPN de terceros.

**VPN Cascading**: el router reenviará el tráfico desde el túnel VPN 1 al túnel VPN 2, lo que permite que los dispositivos conectados al router mediante VPN 1 accedan a Internet a través del servicio VPN de terceros, es decir, VPN 2, en lugar de la red ISP del router.

## Cómo habilitar VPN Cascading

### Para firmware v4.7 y anteriores

1. Primero, configure su router como servidor VPN. Se recomienda el protocolo WireGuard por ofrecer mayor velocidad. Consulte [este enlace](../interface_guide/wireguard_server.md){target="\_blank"}.

2. Exporte un archivo de configuración desde su router y súbalo a un dispositivo cliente, que será el que se conectará al router por VPN.

3. Configure su router como cliente VPN, conectándolo a un servicio VPN de terceros. Se recomienda el protocolo WireGuard por ofrecer mayor velocidad. Consulte [este enlace](../interface_guide/wireguard_client.md){target="\_blank"}.

4. Una vez conectado, la página **VPN Dashboard** se mostrará como a continuación, donde el router está configurado al mismo tiempo como servidor VPN y como cliente VPN.

   ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

   Ve a la sección VPN Server de la misma página y haz clic en **Global Options**.

   ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

   Habilita **VPN Cascading** y haz clic en **Apply**.

   ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPN Cascading ya está habilitado. Los dispositivos conectados a su router mediante VPN accederán a Internet a través del servicio VPN de terceros, en lugar de la red ISP del router.

### Para firmware v4.8 y posteriores

1.  Primero, configure su router como servidor VPN. Se recomienda el protocolo WireGuard por ofrecer mayor velocidad. Consulte [este enlace](../interface_guide/wireguard_server.md){target="\_blank"}.

2.  Exporte un archivo de configuración desde su router y súbalo a un dispositivo cliente, que será el que se conectará al router por VPN.

3.  Configure su router como cliente VPN, conectándolo a un servicio VPN de terceros. Se recomienda el protocolo WireGuard por ofrecer mayor velocidad. Consulte [este enlace](../interface_guide/wireguard_client.md){target="\_blank"}.

4.  En el panel de administración web, vaya a **VPN Dashboard**. Elija las instrucciones correspondientes a continuación según su modo VPN.

    ??? "Global Mode"

        Si su modo VPN es **Global Mode**, una vez habilitado el cliente VPN, como se muestra a continuación, VPN Cascading se habilitará automáticamente.

        Los dispositivos conectados a su router mediante VPN accederán a Internet a través del servicio VPN de terceros, en lugar de la red ISP del router.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        Si su modo VPN es **Policy Mode**, debe configurar la regla del túnel VPN.

        Haga clic en el cuadro atenuado de la izquierda.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Seleccione el origen del tráfico al que se aplicará esta regla. Para habilitar VPN Cascading, seleccione **All Clients**, o bien seleccione **Specified Connection Types** y luego **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: incluye todos los dispositivos LAN, los dispositivos de Drop-in Gateway, los dispositivos de la red de invitados y los dispositivos conectados a su router mediante VPN.

            Si quiere que el tráfico de todos los dispositivos use la misma regla de túnel, seleccione **All Clients** y haga clic en **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: le permite especificar los dispositivos conectados al router mediante un método concreto, por ejemplo dispositivos conectados por VPN, para aplicarles esta regla de túnel.

            Si quiere que los clientes VPN de su router apliquen una regla distinta de la de otros dispositivos, seleccione **WireGuard/OpenVPN Server** y haga clic en **Apply**.

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            Este es un ejemplo de reglas de túnel VPN en **Policy Mode**.

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5.  VPN Cascading ya está habilitado. Los dispositivos conectados a su router mediante VPN accederán a Internet a través del servicio VPN de terceros, en lugar de la red ISP del router.

6.  **Prueba de conexión**: en un portátil conectado al router mediante VPN, abra un navegador y visite [What Is My IP](https://whatismyipaddress.com/){target="\_blank"} para comprobar su IP pública.

    Si muestra que la dirección IP del portátil está en la región del servidor VPN de terceros, que en este ejemplo es Buenos Aires, significa que VPN Cascading está funcionando.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
