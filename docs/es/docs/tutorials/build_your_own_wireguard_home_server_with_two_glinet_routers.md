# Cree su propio servidor doméstico WireGuard con dos routers GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Este artículo explica cómo configurar su router doméstico como servidor VPN WireGuard y su router de viaje como cliente VPN WireGuard para conectarlos de forma remota, de modo que pueda usar la dirección IP de su hogar con el router de viaje desde cualquier lugar.

Vea este vídeo o siga los pasos indicados a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Este vídeo usa GL-MT5000 (Brume 3) y GL-MT3600BE (Beryl 7) para demostrar la configuración de la VPN.)</small>

En los siguientes pasos, tomamos como ejemplo GL-MT6000 (Flint 2) y GL-MT3000 (Beryl AX):

- GL-MT6000, un router doméstico, se configurará como servidor VPN WireGuard. Si no necesita capacidad inalámbrica, también puede considerar nuestro gateway de seguridad GL-MT2500 u otros modelos.

- GL-MT3000, un router de viaje, se configurará como cliente VPN WireGuard para conectarse de forma remota al servidor VPN de su hogar.

## Por qué crear su propio servidor doméstico WireGuard {#why-build-your-own-wireguard-home-server}

1. Usar la dirección IP de su hogar como IP pública, de modo que el tráfico parezca originarse allí.
2. Evitar las cuotas mensuales de los servicios VPN de terceros.
3. Cifrar todo el tráfico de Internet que pasa por el túnel hacia su red doméstica para proteger su privacidad.
4. Acceder a sus dispositivos domésticos y a los servicios de streaming locales desde cualquier lugar.

## Preparativos {#preparations}

### Compruebe si tiene una IP pública {#check-if-you-have-a-public-ip}

Primero, asegúrese de que el GL-MT6000 tenga una dirección IP pública en el lado WAN, para que pueda accederse a él globalmente. De lo contrario, su router de viaje no podrá establecer una conexión VPN con él mientras esté de viaje.

Para comprobar si dispone de una dirección IP pública, abra un navegador web y escriba [what is my ip](https://whatismyipaddress.com/){target="_blank"} en la barra de direcciones.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Se mostrará su dirección IP pública. Si coincide con la IP WAN que su ISP proporciona al GL-MT6000, entonces dispone de una IP pública.

Si no dispone de una IP pública, aquí tiene algunos métodos de referencia.

1. Si tiene un router principal, inicie sesión en él y compruebe si recibe la IP pública de su ISP.
2. Solicite a su ISP una dirección IP pública. Puede requerir un coste adicional.
3. Si los dos métodos anteriores no funcionan, por ejemplo, si su red está detrás de CGNAT, puede probar nuestra solución SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Compruebe si necesita Port Forwarding {#check-if-port-forwarding-is-required}

??? "GL.iNet como router principal"

    Si su router GL.iNet está conectado directamente a un módem del ISP mediante un cable Ethernet, el router GL.iNet es el router principal.

    **¿Cómo comprobar si su router GL.iNet está conectado directamente al módem del ISP?**

    Inicie sesión en el panel de administración de GL.iNet. Seleccione **INTERNET** en la barra lateral izquierda y revise la topología y los detalles de la conexión.

    Si está conectado directamente por Ethernet, verá una sección llamada "Ethernet" con detalles como Protocol, IP address, Gateway, etc.

    Tomando la siguiente imagen como ejemplo, la IP Address marcada es la IP WAN proporcionada por el ISP para este router GL.iNet.

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Esta IP WAN es una dirección IP pública, por lo tanto este router GL.iNet, actuando como router principal, tiene una IP pública y **no necesita configurar Port Forwarding**.

    Solo necesita configurar este router GL.iNet como servidor WireGuard y un router de viaje como cliente WireGuard conectado al servidor. Así se creará un túnel VPN entre ambos.

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet como subrouter"

    Configure **Port Forwarding** en su router principal para el router GL.iNet si este último está detrás de NAT.

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

## Configurar el servidor WireGuard {#set-up-wireguard-server}

1. Inicie sesión en el panel de administración web y vaya a **VPN** -> **WireGuard Server**. Haga clic en **Generate Configuration** solo durante la configuración inicial del servidor VPN.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Compruebe la configuración.

    La configuración predeterminada funciona en la mayoría de los casos, como se muestra a continuación.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address**. Es la dirección IP del túnel del servidor WireGuard. Puede conservarla si no entra en conflicto con la puerta de enlace del router situado aguas arriba.

        Si hay un conflicto, cámbiela por otra dirección, como **10.1.0.1/24**, y haga clic en **Apply**. Incluya el prefijo CIDR `/24` para evitar problemas de conectividad.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Por ejemplo, si el router GL.iNet está conectado a un router Xfinity, este último podría tener la dirección IP 10.0.0.1. Esa dirección puede entrar en conflicto con la IP del túnel cuando algunos modelos GL.iNet se configuran como servidor WireGuard. En ese caso, cambie la dirección como se indica arriba. Si no hay conflicto, omita el cambio.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 está desactivado de forma predeterminada en los routers GL.iNet. Para utilizar una dirección IPv6, active [IPv6](../interface_guide/ipv6.md) en el router.

    - **Listen Port**. El servidor WireGuard escucha de forma predeterminada en el puerto UDP `51820`. Si lo cambia y usa el reenvío de puertos, actualice la regla del router situado aguas arriba para que reenvíe el tráfico al nuevo puerto de escucha del servidor. Use el puerto externo de la regla en el campo `Endpoint` de cada perfil de cliente. Si el servidor es accesible directamente, use su puerto de escucha.

    - **Enable Obfuscation**. Al activar esta opción, el servidor VPN usa el protocolo de ofuscación AmneziaWG para disfrazar el tráfico VPN. Se recomienda mantener los ajustes predeterminados y cambiarlos solo si conoce estos parámetros. Consulte las siguientes guías.

        - [Ofuscación de AmneziaWG en routers GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Cómo configurar la ofuscación VPN en routers GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Añada un perfil.

    Cambie a la pestaña **Profiles** y haga clic en **Add** para generar un perfil para su dispositivo.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Introduzca un nombre descriptivo y haga clic en **Apply** para continuar.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Si necesita ajustar la configuración avanzada, haga clic en **Set More**. A continuación, haga clic en **Apply** para continuar.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Añada reglas de enrutamiento si es necesario"

        En la mayoría de los casos no es necesario añadir reglas de enrutamiento.

        Para acceder desde el servidor a los dispositivos de la LAN del cliente WireGuard, abra la pestaña **Route Rules** de la página **WireGuard Server** y configure las reglas. Consulte la guía de [acceso a la LAN del cliente desde el servidor WireGuard](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Si no necesita añadir reglas, pase al paso 4 para descargar la configuración de cliente.

4. Descargue la configuración.

    Después de añadir un perfil y hacer clic en **Apply**, el router ofrece la configuración como código QR, texto sin formato o archivo `.conf` descargable.

    - **QR code**. Escanee el código en la aplicación WireGuard para importar un perfil WireGuard estándar. Si ha activado la ofuscación, use la aplicación AmneziaWG u otro cliente compatible con la ofuscación de AmneziaWG.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**. Puede revisar y copiar los detalles en texto sin formato para configurar manualmente la aplicación WireGuard o un router GL.iNet, por ejemplo.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**. Haga clic en **Download** para guardar el archivo .conf en su dispositivo. Puede cargarlo directamente en la aplicación WireGuard o en un router GL.iNet.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    Si lo necesita, puede usar como dirección del servidor la IP pública, el dominio DDNS o la IP WAN actual. Esta función está disponible desde el firmware v4.8. Si cambia la dirección, también se actualizará en el archivo de configuración.

    Por ejemplo, si la dirección IP pública de su red cambia con frecuencia, active [DDNS](../interface_guide/ddns.md) y use el dominio DDNS como dirección del servidor.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Haga clic en **Start** en la esquina superior derecha para iniciar el servidor WireGuard. El estado de la conexión aparecerá en la misma página.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Configurar el cliente WireGuard {#set-up-wireguard-client}

### Cambiar la IP LAN {#change-the-lan-ip}

Como en este tutorial usamos GL-MT6000 y GL-MT3000 como ejemplos, y sus IP LAN predeterminadas son ambas **192.168.8.1**, necesitamos cambiar una de ellas por una IP LAN diferente para evitar conflictos.

A continuación se explica cómo cambiar la IP LAN del GL-MT3000, que actúa como cliente WireGuard.

Inicie sesión en el panel de administración web del GL-MT3000 y vaya a **NETWORK** -> **LAN** para cambiar la IP LAN. Por ejemplo, puede sustituir la dirección predeterminada 192.168.8.1 por `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Añadir la configuración {#add-the-configuration}

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

### Iniciar la conexión {#start-the-connection}

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

## Preparación para futuras correcciones remotas de la VPN {#prep-for-remote-vpn-fixes-ahead}

Vincule ambos routers a su cuenta de GoodCloud antes de viajar. Esto permite resolver problemas de forma remota si la conexión VPN falla por problemas de configuración o de red. El acceso remoto solo funciona mientras los routers permanecen encendidos y conectados a Internet.

---

Artículos relacionados

- [Configurar el servidor WireGuard en routers GL.iNet](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

¿Aún tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
