# Configurar el servidor OpenVPN en routers GL.iNet

OpenVPN es un protocolo VPN de código abierto que utiliza técnicas de red privada virtual para establecer conexiones seguras de sitio a sitio o de punto a punto.

Para configurar el servidor OpenVPN en un router GL.iNet, vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Asegúrese de tener una dirección IP pública

Haga clic [aquí](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) para comprobar si su proveedor de servicios de Internet le asigna una dirección IP pública.

**Si no es así, no podrá configurar su router como servidor OpenVPN.**

Métodos alternativos:

1. Si tiene un router principal, inicie sesión en él y compruebe si recibe una IP pública de su ISP.
2. Solicite a su ISP una dirección IP pública. Esto puede implicar un coste adicional.
3. Si los dos métodos anteriores no funcionan, por ejemplo, si su red está detrás de CGNAT, puede probar nuestra solución SD-WAN [AstroWarp](https://www.astrowarp.net/){target="\_blank"}.

## Confirme si es necesario configurar el reenvío de puertos

**Topología de red**

??? "GL.iNet es el router principal"

    * Si el router GL.iNet es el router principal de su red, no es necesario configurar el reenvío de puertos. Pase al [siguiente paso](#configurar-el-servidor-openvpn).

??? "GL.iNet es el router secundario"

    * Si ya hay un router principal en uso y el router GL.iNet está configurado como router secundario, tendrá que configurar el [reenvío de puertos](../tutorials/how_to_set_up_port_forwarding.md) en el router principal.

    * Si ya hay un router principal en uso y el router GL.iNet está varios niveles por debajo del router principal, configure el [reenvío de puertos](../tutorials/how_to_set_up_port_forwarding.md) en cada nivel intermedio.

## Configurar el servidor OpenVPN

Inicie sesión en el panel de administración web y vaya a **VPN** -> **OpenVPN Server**.

1. Haga clic en **Generate Configuration** solo durante la configuración inicial del servidor VPN.

   ![ovpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_generate_config.png){class="glboxshadow"}

2. Aplique la configuración.

   La configuración predeterminada funciona en la mayoría de los casos.

   Si no necesita modificarla, haga clic en **Export Client Configuration** en la parte inferior y pase al paso 3.

   Si ha modificado la configuración, haga clic en **Apply** antes de exportar la configuración del cliente.

   ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}
   - **Device Mode:** TAP-S2S o Tun. Haga clic [aquí](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode) para consultar las diferencias.

   - **Protocol:** UDP o TCP. Haga clic [aquí](../faq/openvpn_tcp_udp.md) para consultar las diferencias.

   - **Authentication Mode:** Determina el método de autenticación que se utilizará cuando el cliente se conecte al servidor. Hay tres opciones.
     - **Certificate Only**: Si se selecciona, el router generará automáticamente las claves de certificado del servidor y del cliente, y las integrará en el archivo de configuración del cliente. Cuando suba la configuración al cliente, no se requerirán credenciales adicionales.

     - **Username/Password Only**: Si se selecciona, el router generará la configuración del cliente sin claves de certificado. Antes de exportar la configuración del cliente, primero debe añadir un nombre de usuario y una contraseña en la pestaña **Users**. Al subir la configuración al cliente, deberá introducir estas credenciales para autenticarse.

     - **Username/Password and Certificate**: Si se selecciona, primero debe añadir un nombre de usuario y una contraseña en la pestaña **Users** antes de exportar la configuración del cliente. Además, el router generará automáticamente las claves de certificado del servidor y del cliente y las integrará en el archivo de configuración. Al subir la configuración al cliente, primero se verificará el certificado y la clave, y después se realizará la autenticación mediante nombre de usuario y contraseña para proporcionar seguridad de dos factores.

     A continuación se muestra un ejemplo de cómo crear un usuario.

     ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

   - **Advanced Configuration**: Si es necesario, puede modificar más ajustes del servidor.

     ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Exporte la configuración del cliente.

   Haga clic en **Export Client Configuration** en la parte inferior de la pestaña **Configuration** o aplique la configuración modificada. A continuación, aparecerá una ventana como la que se muestra a continuación.

   ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_export_configuration.png){class="glboxshadow"}
   - Si la IP pública de su red cambia con frecuencia, puede habilitar [DDNS](ddns.md) para usar un dominio DDNS como dirección del servidor.

   - Desde el firmware v4.8, puede especificar la dirección del servidor entre la IP pública, el dominio DDNS y la IP WAN actual. Cuando la cambie, la dirección del servidor en el archivo de configuración se actualizará al mismo tiempo.

   Después, haga clic en **Download** para exportar la configuración.

4. Inicie el servidor OpenVPN.

   Haga clic en el botón **Start** situado en la esquina superior derecha de la página **OpenVPN Server** para iniciar el servidor. Después, vaya a la página VPN Dashboard para comprobar su estado y otros ajustes.

   ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Compruebe si el servidor OpenVPN funciona correctamente

### Verifique el estado del servidor

Desde el firmware v4.8, puede consultar el estado de conexión del servidor en la página **OpenVPN Server**.

Si se muestran estadísticas de tráfico de carga y descarga, significa que el servidor OpenVPN está en funcionamiento.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

En el firmware v4.7 y versiones anteriores, consulte el estado de conexión del servidor en la página **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Verifique la IP del cliente

Para verificar que la conexión al servidor se haya realizado correctamente, importe la configuración de OpenVPN exportada anteriormente en un dispositivo de otra red, es decir, que no esté en la misma red local que el servidor. Luego abra un navegador web y busque su dirección IP y ubicación. Si coinciden con la IP y la ubicación del servidor VPN, en lugar de las de su proveedor de servicios de Internet, la conexión VPN se ha realizado correctamente.

El método más sencillo es usar un smartphone con la [OpenVPN App](https://openvpn.net/vpn-client/){target="\_blank"} oficial instalada. Primero, desactive la conexión Wi-Fi del smartphone y conéctelo a Internet exclusivamente mediante datos móviles 4G o 5G. Después, abra la aplicación OpenVPN, importe el archivo de configuración e inicie la conexión. Compruebe si el smartphone puede acceder a Internet y si su dirección IP coincide con la IP del servidor OpenVPN.

Al importar el archivo de configuración en la aplicación OpenVPN, puede aparecer un aviso como el que se muestra a continuación. Haga clic en **CONTINUE** para continuar, ya que el certificado ya está integrado en el archivo de configuración.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Si la conexión falla, estas son algunas causas habituales:

- Su proveedor de servicios de Internet no le asigna una dirección IP pública. Consúltelo [aquí](#asegurese-de-tener-una-direccion-ip-publica).
- Puede que necesite configurar el reenvío de puertos. Consúltelo [aquí](#confirme-si-es-necesario-configurar-el-reenvio-de-puertos).
- El puerto utilizado por el servidor OpenVPN está bloqueado por su proveedor de servicios de Internet. Cámbielo por otro puerto o póngase en contacto con el proveedor para obtener más ayuda.
- En algunos países o regiones, la conexión VPN puede estar bloqueada.

## Acceso de cliente a cliente

**Topología de red**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Active la opción client to client y exporte una nueva configuración para los clientes. De este modo, sus clientes podrán acceder entre sí.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## Instalar la OpenVPN App

Descargue la OpenVPN App desde el [sitio web oficial de OpenVPN](https://openvpn.net/vpn-client/){target="\_blank"}.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
