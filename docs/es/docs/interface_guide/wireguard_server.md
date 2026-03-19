# Configurar el servidor WireGuard en routers GL.iNet

WireGuard® es una VPN extremadamente simple, rápida y moderna que utiliza criptografía de última generación. Está diseñada para ser más rápida, más sencilla, más ligera y más útil que IPSec, evitando al mismo tiempo su gran complejidad. Su rendimiento previsto es considerablemente superior al de OpenVPN.

Para configurar el servidor WireGuard en un router GL.iNet, vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Asegúrese de tener una dirección IP pública

Haga clic [aquí](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) para comprobar si su proveedor de servicios de Internet le asigna una dirección IP pública.

**Si no es así, no podrá configurar su router como servidor WireGuard.**

Métodos alternativos:

1. Si tiene un router principal, inicie sesión en él y compruebe si recibe una IP pública de su ISP.
2. Solicite a su ISP una dirección IP pública. Esto puede implicar un coste adicional.
3. Si los dos métodos anteriores no funcionan, por ejemplo, si su red está detrás de CGNAT, puede probar nuestra solución SD-WAN [AstroWarp](https://www.astrowarp.net/){target="\_blank"}.

## Confirme si es necesario configurar el reenvío de puertos

**Topología de red**

??? "GL.iNet es el router principal"

    * Si el router GL.iNet es el router principal de su red, no es necesario configurar el reenvío de puertos. Pase al [siguiente paso](#configurar-el-servidor-wireguard).

??? "GL.iNet es el router secundario"

    * Si ya hay un router principal en uso y el router GL.iNet está configurado como router secundario, tendrá que configurar el [reenvío de puertos](../tutorials/how_to_set_up_port_forwarding.md) en el router principal.

    * Si ya hay un router principal en uso y el router GL.iNet está varios niveles por debajo del router principal, configure el [reenvío de puertos](../tutorials/how_to_set_up_port_forwarding.md) en cada nivel intermedio.

## Configurar el servidor WireGuard

Inicie sesión en el panel de administración web y vaya a **VPN** -> **WireGuard Server**.

1.  Haga clic en **Generate Configuration** solo durante la configuración inicial del servidor VPN.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2.  Compruebe la configuración.

    La configuración predeterminada funciona en la mayoría de los casos, como se muestra a continuación. No es necesario modificar la dirección IPv4 si no entra en conflicto con la puerta de enlace de su router ascendente.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    IPv6 está desactivado de forma predeterminada en GL.iNet. Si desea utilizar una dirección IPv6, habilite IPv6 en su router.

    Si observa que la dirección IPv4 entra en conflicto con la puerta de enlace de su router ascendente, cámbiela por otra, como **10.1.0.1/24**, y haga clic en **Apply**. Asegúrese de incluir la notación CIDR "/24" para evitar problemas de conectividad.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Por ejemplo, si hay un router Xfinity aguas arriba de un router GL.iNet, la IP del router Xfinity puede ser 10.0.0.1, lo que entrará en conflicto con la IP del túnel del servidor WireGuard cuando el router GL.iNet se configure como servidor WireGuard. En ese caso, deberá realizar los cambios anteriores.

    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3.  Añada un perfil.

    Cambie a la pestaña **Profiles** y haga clic en el botón **Add** para generar un perfil para su dispositivo.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Establezca un nombre descriptivo y haga clic en **Apply** para continuar.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Si necesita definir ajustes avanzados, haga clic en **Set More**. A continuación, haga clic en **Apply** para continuar.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Añada reglas de ruta si es necesario"

        En la mayoría de los casos no es necesario añadir reglas de ruta.

        Si desea acceder desde el servidor a los dispositivos de la LAN del cliente WireGuard, vaya a la pestaña **Route Rules** de la página **WireGuard Server** para configurar las reglas de ruta. Haga clic [aquí](../tutorials/wireguard_server_access_to_client_lan_side.md) para obtener más instrucciones.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        En caso contrario, pase al paso 4 para descargar una configuración de cliente.

4.  Descargue la configuración.

    Después de añadir un perfil y aplicarlo, se generará un archivo de configuración en tres formatos: código QR, texto sin formato y archivo .conf. Elija el método que prefiera para obtener el archivo de configuración.
    - **QR code**: Adecuado para dispositivos finales, como smartphones, tablets o portátiles, con la WireGuard App instalada. Si desea configurar un dispositivo como cliente WireGuard, solo tiene que abrir la WireGuard App, escanear el código QR y la configuración se importará automáticamente.

      ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: En formato de texto sin formato, puede revisar los detalles de la configuración y copiarlos y pegarlos cómodamente en otro lugar para una configuración manual, como en la WireGuard App o en un router GL.iNet.

      ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: Haga clic en el botón **Download** para guardar el archivo .conf en su dispositivo local. También es una opción cómoda y puede subirse directamente a la aplicación WireGuard o a un router GL.iNet.

      ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    Si es necesario, puede especificar la dirección del servidor entre la IP pública, el dominio DDNS y la IP WAN actual. Esta función está disponible desde el firmware v4.8. Cuando la cambie, la dirección del servidor en el archivo de configuración se actualizará al mismo tiempo.

    Por ejemplo, se recomienda habilitar [DDNS](ddns.md) y usar un dominio DDNS como dirección del servidor si la IP pública de su red cambia con frecuencia.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5.  Inicie el servidor WireGuard.

    Haga clic en el botón **Start** en la esquina superior derecha para iniciar el servidor WireGuard.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    El estado de la conexión se mostrará en la misma página.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Compruebe si el servidor WireGuard funciona correctamente

### Verifique el estado del servidor

Desde el firmware v4.8, puede consultar el estado de conexión del servidor en la página **WireGuard Server**.

Si se muestran estadísticas de tráfico de carga y descarga y dispositivos conectados en línea, significa que el servidor WireGuard está en funcionamiento y que hay clientes WireGuard conectados.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

Si se muestran 0 de tráfico y 0 clientes, significa que no hay ningún cliente WireGuard conectado.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

En el firmware v4.7 y versiones anteriores, consulte el estado de conexión del servidor en la página **VPN Dashboard**.

### Verifique la IP del cliente

Para verificar que la conexión al servidor se haya realizado correctamente, importe la configuración de WireGuard exportada anteriormente en un dispositivo de otra red, es decir, que no esté en la misma red local que el servidor. Luego abra un navegador web y busque su dirección IP y ubicación. Si coinciden con la IP y la ubicación del servidor VPN, en lugar de las de su proveedor de servicios de Internet, la conexión VPN se ha realizado correctamente.

El método más sencillo es usar un smartphone con la [WireGuard App](https://www.wireguard.com/install){target="\_blank"} oficial instalada. Primero, desactive la conexión Wi-Fi del smartphone y conéctelo a Internet exclusivamente mediante datos móviles 4G o 5G. Después, abra la WireGuard App, importe el archivo de configuración e inicie la conexión. Compruebe si el smartphone puede acceder a Internet y si su dirección IP coincide con la IP del servidor WireGuard.

Si la conexión falla, estas son algunas causas habituales:

- Su proveedor de servicios de Internet no le asigna una dirección IP pública. Consúltelo [aquí](#asegurese-de-tener-una-direccion-ip-publica).
- Puede que necesite configurar el reenvío de puertos. Consúltelo [aquí](#confirme-si-es-necesario-configurar-el-reenvio-de-puertos).
- El puerto utilizado por el servidor WireGuard está bloqueado por su proveedor de servicios de Internet. Cámbielo por otro puerto o póngase en contacto con el proveedor para obtener más ayuda.
- En algunos países o regiones, la conexión VPN puede estar bloqueada.

## Instalar la WireGuard App

Descargue la WireGuard App desde el [sitio web oficial de WireGuard](https://www.wireguard.com/install){target="\_blank"}.

---

WireGuard® es una marca registrada de Jason A.Donenfeld.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
