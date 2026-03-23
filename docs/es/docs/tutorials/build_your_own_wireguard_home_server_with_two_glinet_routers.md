# Cree su propio servidor doméstico WireGuard con dos routers GL.iNet

Este artículo explica cómo configurar su router doméstico como servidor VPN WireGuard y su router de viaje como cliente VPN WireGuard para conectarlos de forma remota, de modo que pueda usar la dirección IP de su hogar con el router de viaje desde cualquier lugar.

Vea este vídeo o siga los pasos indicados a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Este vídeo usa GL-MT5000 (Brume 3) y GL-MT3600BE (Beryl 7) para demostrar la configuración de la VPN.)</small>

En los siguientes pasos, tomamos como ejemplo GL-MT6000 (Flint 2) y GL-MT3000 (Beryl AX):

- GL-MT6000, un router doméstico, se configurará como servidor VPN WireGuard. Si no necesita capacidad inalámbrica, también puede considerar nuestro gateway de seguridad GL-MT2500 u otros modelos.

- GL-MT3000, un router de viaje, se configurará como cliente VPN WireGuard para conectarse de forma remota al servidor VPN de su hogar.

## Por qué necesita crear su propio servidor doméstico WireGuard

1. Usar la dirección IP de su hogar como dirección de Internet, como si realmente estuviera en casa.
2. No tener que pagar una cuota mensual en comparación con servicios VPN de terceros.
3. Enrutar todo el tráfico de Internet hacia su red doméstica mediante un túnel VPN cifrado y proteger su privacidad.
4. Acceder fácilmente a sus recursos internos y a servicios de streaming locales.

## Preparativos

### Compruebe si tiene una IP pública

Primero, asegúrese de que el GL-MT6000 tenga una dirección IP pública en el lado WAN, para que pueda accederse a él globalmente. De lo contrario, su router de viaje no podrá establecer una conexión VPN con él mientras esté de viaje.

Para comprobar si dispone de una dirección IP pública, abra un navegador web y escriba [what is my ip](https://whatismyipaddress.com/){target="\_blank"} en la barra de direcciones.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Se mostrará su dirección IP pública. Si coincide con la IP WAN que su ISP proporciona al GL-MT6000, entonces dispone de una IP pública.

Si no dispone de una IP pública, aquí tiene algunos métodos de referencia.

1. Si tiene un router principal, inicie sesión en él y compruebe si recibe la IP pública de su ISP.
2. Solicite a su ISP una dirección IP pública. Puede requerir un coste adicional.
3. Si las dos opciones anteriores no funcionan, por ejemplo si está detrás de CGNAT, puede utilizar un método de proxy inverso como [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md). Como alternativa, puede probar una solución SDWAN, como [AstroWarp](https://www.astrowarp.net/).

### Compruebe si necesita Port Forwarding

??? "GL.iNet como router principal"

    Si su router GL.iNet está conectado directamente a un módem del ISP mediante un cable Ethernet, el router GL.iNet es el router principal.

    **¿Cómo comprobar si su router GL.iNet está conectado directamente al módem del ISP?**

    Pasos:

    1. Inicie sesión en el panel de administración de GL.iNet.

    2. Seleccione INTERNET en la barra lateral izquierda. Revise la topología y los detalles de conexión:

        Si está conectado directamente por Ethernet, verá una sección llamada "Ethernet" con detalles como Protocol, IP address, Gateway, etc.

        Tomando la siguiente imagen como ejemplo, la IP Address marcada es la IP WAN proporcionada por el ISP para este router GL.iNet.

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Esta IP WAN es una dirección IP pública, por lo tanto este router GL.iNet, actuando como router principal, tiene una IP pública y **no necesita configurar Port Forwarding**.

        Solo necesita configurar este router GL.iNet como servidor WireGuard y un router de viaje como cliente WireGuard conectado al servidor. Así se creará un túnel VPN entre ambos.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet como subrouter"

    Configure **Port Forwarding** en su router principal para el router GL.iNet si este último está detrás de NAT.

    Topología

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Ejemplo: un router TP-Link como router principal de su hogar.

    Conéctese al Wi-Fi o a la LAN de su router doméstico. Luego inicie sesión en el panel de administración web. Compruebe la dirección IP WAN que recibe de su ISP. En la siguiente imagen puede ver que su IP pública es **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Antes de configurar el reenvío de puertos, recomendamos reservar una dirección IP para el router GL.iNet en su router principal, de modo que se le pueda asignar una IP fija.** De lo contrario, si el router principal o el router GL.iNet se reinician, el router principal podría asignar una IP distinta al router GL.iNet, haciendo que la regla de reenvío de puertos deje de funcionar.

    A continuación, configure Port Forwarding en su router principal para el router GL.iNet.

    1. Vaya a “Advanced”, haga clic en “virtual Server” y luego en “Add”.

    2. Internal IP (Device IP): es la dirección IP asignada al router GL.iNet, que puede encontrar en la lista de clientes de TP-Link.

    3. External/Internal port: rellene ambos con "51820".

    4. Protocol: puede elegir "All o UDP o TCP/UDP".

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Más ejemplos de [Port Forward](how_to_set_up_port_forwarding.md)**

## Configurar el servidor WireGuard

### Habilitar DDNS, opcional

Habilite la función DDNS si no dispone de una IP pública estática, sino solo de una IP pública dinámica.

Inicie sesión en el panel de administración web del GL-MT6000 y vaya a **APPLICATIONS** -> **Dynamic DNS**. Active el interruptor **Enable DDNS**.

Marque la casilla **Terms of Service & Privacy Policy** y haga clic en **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Luego vaya a **WireGuard Server** -> pestaña Configuration, asegúrese de que Listen Port sea 51820 y haga clic en **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Generar la configuración

En la misma página, haga clic en la pestaña **Profiles**, junto a la pestaña Configuration, y luego haga clic en **Add**, marcado como 1 en la imagen siguiente.

Se generará automáticamente una configuración de cliente. Haga clic en el **icono de reenvío**, marcado como 2.

En la ventana emergente, active DDNS Domain deslizando el control, marcado como 3, lo cual es opcional y solo debe habilitarse si tiene una IP pública dinámica.

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Después puede escanear el QR con la [mobile app](https://www.wireguard.com/install/) de WireGuard para probar el servidor. Para más detalles, haga clic [aquí](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

Como alternativa, puede exportar una configuración en formato de texto para la conexión del cliente VPN.

Cambie la configuración de código QR a formato de texto haciendo clic en la pestaña **Configuration File**.

Copie el texto del cliente, o haga clic en el botón Download y guárdelo para usarlo más adelante.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Configurar el cliente WireGuard

### Cambiar la IP LAN

Como en este tutorial usamos GL-MT6000 y GL-MT3000 como ejemplos, y sus IP LAN predeterminadas son ambas **192.168.8.1**, necesitamos cambiar una de ellas por una IP LAN diferente para evitar conflictos.

Estos son los pasos para cambiar la IP LAN del GL-MT3000, el cliente WireGuard.

Inicie sesión en el panel de administración web del GL-MT3000 y vaya a **NETWORK** -> **LAN** desde la barra lateral izquierda para cambiar la IP LAN. Por ejemplo, puede cambiarla desde la IP predeterminada 192.168.8.1 a `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Para más detalles sobre la interfaz LAN, haga clic [aquí](../interface_guide/lan.md).

### Añadir la configuración

En el panel de administración web del GL-MT3000, vaya a **VPN** -> **WireGuard Client** y haga clic en **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Cree un grupo a la izquierda y asígnele un nombre; luego seleccione el archivo de configuración para cargarlo o arrástrelo al cuadro de carga situado a la derecha.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Una vez que el archivo haya pasado la verificación, haga clic en **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

También puede hacer clic en **Manually Add Configuration**, pegar el texto de configuración y luego hacer clic en **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

El archivo de configuración se mostrará en la página WireGuard Client una vez que se haya cargado correctamente.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Iniciar la conexión

Haga clic en el icono de tres puntos y luego en **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Espere unos minutos. Una vez que se conecte correctamente, se encenderá un punto verde.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Vaya a **VPN Dashboard** y verá que su cliente se está conectando al servidor con la IP pública de su hogar. La página puede variar ligeramente según la versión del firmware.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Vuelva a iniciar sesión en el panel de administración web del GL-MT6000, el servidor WireGuard, vaya a **VPN** -> **WireGuard Server**, o a **VPN** -> **VPN Dashboard** si usa firmware v4.7 o anterior, y también verá el estado de la conexión, lo que indica que el cliente está conectado.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Página WireGuard Server en FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(Página VPN Dashboard en FW v4.7 y anteriores)</small>

## Preparación para futuras correcciones remotas de la VPN

En caso de problemas imprevistos durante el viaje, vincule previamente ambos routers a su cuenta de GoodCloud para facilitar la resolución remota de problemas de la VPN.

A veces su servidor puede quedar fuera de servicio por un corte eléctrico u otros motivos. Para mantener la accesibilidad del servidor, vincúlelo a GL.iNet GoodCloud.

---

Artículos relacionados

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

¿Aún tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="\_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="\_blank"}.
