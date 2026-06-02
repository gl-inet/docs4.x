# VPN Client Profile

> Esta guía se aplica al firmware v4.9 y posteriores.

En el lado izquierdo del panel de administración web, vaya a **VPN** -> **VPN Client Profile**.

Desde el firmware v4.9, [OpenVPN Client](openvpn_client.md) y [WireGuard Client](wireguard_client.md) se han combinado en una sola página **VPN Client Profile** para ofrecer una gestión más ágil. Aunque el diseño se ha ajustado ligeramente, la funcionalidad principal permanece sin cambios. Si lo necesita, puede seguir consultando las guías independientes.

Esta página le permite iniciar sesión en algunos servicios VPN integrados y descargar fácilmente sus perfiles para la conexión VPN, o subir manualmente sus archivos de configuración exportados desde el sitio web de otro proveedor VPN. Puede cambiar el protocolo VPN en la esquina superior derecha si es necesario.

## WireGuard

WireGuard® es una VPN moderna, ligera y de alto rendimiento construida con criptografía de vanguardia. Ofrece una velocidad, simplicidad y practicidad superiores frente a IPsec, y supera notablemente a OpenVPN.

Los routers GL.iNet ofrecen compatibilidad integrada con WireGuard para los siguientes proveedores VPN. Si tiene una suscripción activa, solo tiene que introducir las credenciales del servicio en la página **VPN Client Profile** para completar la configuración rápidamente.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

Si está suscrito a otro proveedor de servicios WireGuard, descargue un archivo de configuración desde su sitio web y luego haga clic en **Add Manually** para subirlo al router para la conexión VPN. Si no sabe cómo descargar los archivos de configuración, consulte [aquí](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) o contacte con su soporte.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Tomemos [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} como ejemplo.

1. Haga clic en **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Introduzca **Username** y **Password**, y luego haga clic en **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    El sistema generará archivos de configuración para todos los servidores disponibles.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Consulte la guía correspondiente a continuación según sus necesidades reales.

    !!! note "Caso 1. Si desea que todos los clientes conectados usen la VPN para acceder a Internet, siga estos pasos."
    
        1. Seleccione el servidor que prefiera y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            Ahora la conexión VPN está activada y todos los clientes conectados a este router deberían usar la VPN para un acceso seguro a Internet.

        3. (Opcional) Si desea que el sistema corte automáticamente todo el acceso a Internet de su red local cuando la conexión VPN falle de forma inesperada, evitando que su dirección IP real y sus datos en línea queden expuestos y garantizando una privacidad y seguridad continuas, vaya a **VPN Dashboard** para habilitar **Kill Switch**.

            * Para configurar Kill Switch para cada túnel VPN individual, consulte [aquí](vpn_dashboard_v4.9.md#tunnel-options).
            
            * Para configurar Kill Switch para la conexión VPN global (es decir, Kill Switch Mejorado), consulte [aquí](vpn_dashboard_v4.9.md#all-other-traffic).

    !!! note "Caso 2. Si prefiere personalizar la política VPN, siga estos pasos."
    
        1. Haga clic en **Go to Dashboard** en la parte inferior.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Se le redirigirá a **VPN Dashboard** para configurar la política VPN. Haga clic [aquí](vpn_dashboard_v4.9.md#set-up-vpn-policy) para ver los detalles.

## OpenVPN

OpenVPN es un protocolo VPN de código abierto que utiliza técnicas de red privada virtual para establecer conexiones seguras de sitio a sitio o de punto a punto.

Los routers GL.iNet ofrecen compatibilidad integrada con OpenVPN para [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Si tiene una suscripción activa, solo tiene que introducir las credenciales del servicio en la página **VPN Client Profile** para completar la configuración rápidamente.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Si está suscrito a otro proveedor de servicios OpenVPN, descargue un archivo de configuración desde su sitio web y luego haga clic en **Add Manually** para subirlo al router para la conexión VPN. Si no sabe cómo descargar los archivos de configuración, consulte [aquí](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) o contacte con su soporte.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Artículos relacionados

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard_v4.9.md)
- [Configurar el cliente WireGuard en routers GL.iNet](wireguard_client.md)
- [Configurar el cliente OpenVPN en routers GL.iNet](openvpn_client.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
