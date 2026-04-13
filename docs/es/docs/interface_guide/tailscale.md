# Tailscale

Tailscale es un servicio VPN que hace que los dispositivos y aplicaciones que posee sean accesibles desde cualquier lugar del mundo, de forma segura y sencilla. Para obtener más información sobre Tailscale, visite el [sitio web oficial de Tailscale](https://tailscale.com/).

La función Tailscale en los routers GL.iNet, disponible desde el firmware v4.2, permite que el router se una a una red virtual de Tailscale. Una vez conectado, podrá acceder al router de forma remota, incluidos sus recursos WAN y LAN.

**Nota**:

1. Como Tailscale se basa en WireGuard, no se recomienda usar Tailscale al mismo tiempo que cualquiera de las siguientes funciones o servicios, ya que puede causar conflictos de enrutamiento: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier y AstroWarp.

2. Esta función se encuentra actualmente en fase beta y puede presentar algunos errores.

3. Los routers GL.iNet **todavía no están disponibles como exit nodes**.

## Modelos compatibles

??? "Modelos compatibles" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-AX1800 (Flint) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus)

??? "Modelos no compatibles" - GL-SFT1200 (Opal) - GL-MT1300 (Beryl) - GL-E750/E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-S1300 (Convexa-S) - GL-X300B (Collie)

## Configurar la red Tailscale

A continuación se muestra un ejemplo con el GL-MT2500.

1. Vincule sus dispositivos.

   Primero registre una cuenta de Tailscale y, a continuación, vincule uno o dos dispositivos, por ejemplo un smartphone o un portátil, a su cuenta de Tailscale para realizar pruebas.

   Después de la vinculación, podrá ver sus dispositivos y su estado en la consola Tailscale Admin.

   ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Habilite Tailscale en el router GL.iNet.

   Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Tailscale**.

   ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

   Active Tailscale y luego haga clic en **Apply**.

   ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Después de un momento, la interfaz mostrará un **Device Bind Link**. Haga clic en ese enlace.

   ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

   En la ventana emergente se mostrará un enlace de Tailscale. Haga clic en el enlace para ir al sitio web de Tailscale e iniciar sesión.

   ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

   Una vez iniciada la sesión, se le pedirá que confirme el dispositivo que desea conectar. Haga clic en **Connect**.

   ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

   Cuando la conexión se realice correctamente, será redirigido automáticamente a la consola Tailscale Admin. Podrá ver que la dirección IP del GL-MT2500 es `100.88.54.21`. Ahora puede usar esta IP para acceder al router.

   ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

4. Probar la conectividad.

   En los dispositivos conectados a la misma red Tailscale, puede probar la conectividad de las tres formas siguientes.
   - Usar el comando ping

     ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

   - Acceder al router mediante SSH

     ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

   - Acceder al panel de administración web

     ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Allow Remote Access WAN

Si esta opción está habilitada, se podrá acceder a los recursos del lado WAN del dispositivo a través de la red virtual de Tailscale.

Por ejemplo, como se muestra en la topología siguiente, si esta función está habilitada, puede acceder al `GL-AXT1800` mediante su dirección IP (`192.168.29.1`) desde `leo-phone`. Esto se debe a que el GL-AXT1800 es el dispositivo de nivel superior del `GL-MT2500`, y este último está conectado a la misma red Tailscale que leo-phone.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Los pasos son los siguientes.

1. Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Tailscale**.

   Habilite **Allow Remote Access WAN** y haga clic en **Apply**.

   ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Vaya a la consola Tailscale Admin y verá una alerta indicando que el GL-MT2500 tiene subredes.

   Haga clic en el icono de tres puntos situado a la derecha del GL-MT2500 y seleccione **Edit route settings**.

   ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Habilite las rutas de subred.

   ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Ahora puede acceder al GL-AXT1800 mediante su dirección IP (`192.168.29.1`) desde otros dispositivos. En realidad, puede acceder a todos los dispositivos dentro de la subred `192.168.29.0/24`.

   ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

Si esta opción está habilitada, se podrá acceder a los recursos del lado LAN del dispositivo a través de la red virtual de Tailscale.

Por ejemplo, como se muestra en la topología siguiente, si esta función está habilitada, puede iniciar sesión por SSH en `Ubuntu` mediante su dirección IP (`192.168.8.110`) desde `leo-phone`. Esto se debe a que `Ubuntu` es el dispositivo de nivel inferior del `GL-MT2500`, y este último está conectado a la misma red Tailscale que leo-phone.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Los pasos son los siguientes.

1. Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Tailscale**.

   Habilite **Allow Remote Access LAN** y haga clic en **Apply**.

   ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Vaya a la consola Tailscale Admin y verá una alerta indicando que el GL-MT2500 tiene subredes.

   Haga clic en el icono de tres puntos situado a la derecha del GL-MT2500 y seleccione **Edit route settings**.

   ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Habilite las rutas de subred.

   ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Ahora puede hacer ping o iniciar sesión por SSH en Ubuntu mediante su dirección IP (`192.168.8.110`) desde otros dispositivos. En realidad, puede acceder a todos los dispositivos dentro de la subred `192.168.8.0/24`.

   ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Custom Exit Nodes

De forma predeterminada, Tailscale actúa como una red superpuesta: solo enruta tráfico entre dispositivos que ejecutan Tailscale y no procesa su tráfico de Internet público, por ejemplo, cuando navega por sitios web como Google.

Sin embargo, puede haber situaciones en las que quiera que Tailscale enrute también su tráfico de Internet público. Por ejemplo, si está fuera de casa o viajando al extranjero y necesita acceder a servicios en línea, como la banca electrónica, que solo están disponibles en su país de origen, puede configurar su ordenador de sobremesa doméstico con IP pública como Exit Node y hacer que otros dispositivos del mismo Tailnet —como el GL-AXT1800 y el GL-MT3000 que aparecen en la imagen inferior— envíen su tráfico a través de él. Así, todo su tráfico público de Internet se reenviará a través del Exit Node.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Cuando todo el tráfico se enruta a través de un Exit Node, en la práctica se están utilizando las rutas predeterminadas (0.0.0.0/0, ::/0), lo que funciona de forma similar a una conexión VPN tradicional.

En resumen, un Exit Node enruta el tráfico saliente de Internet de sus dispositivos del Tailnet y actúa, en la práctica, como un servidor VPN. Cuando se conecta a un Exit Node, todo el tráfico de Internet que no es de Tailscale parece originarse desde su ubicación, lo que puede ayudarle a acceder a contenido restringido geográficamente y mejorar su privacidad en línea. El dispositivo que se encarga de reenviar ese tráfico se denomina “exit node”.

**Nota**: Si el servidor DNS del router usa una dirección IP privada accesible solo desde la red local, puede perder la conectividad a Internet al usar un Exit Node. Para solucionarlo, inicie sesión en el router, vaya a **NETWORK** -> **DNS** y configure manualmente un servidor DNS público, como `8.8.8.8`.

---

En el siguiente ejemplo, un router GL.iNet **GL-MT2500** y un **Leo-Desktop** están en el mismo Tailnet. A continuación se indican los pasos para configurar Leo-Desktop como Exit Node.

1. Habilite las rutas de subred del GL-MT2500 en la consola Tailscale Admin.

   Vaya a la consola Tailscale Admin, haga clic en el icono de tres puntos situado a la derecha del GL-MT2500 y seleccione **Edit route settings**.

   ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

   En la ventana emergente, habilite las rutas de subred.

   ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. En el dispositivo que quiera usar como Exit Node, por ejemplo Leo-Desktop en este ejemplo, seleccione **Run exit node**. A continuación se muestra un ejemplo en Windows.

   ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

   A continuación, haga clic en **Yes**.

   ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. En la consola Tailscale Admin, configure Leo-Desktop como Exit Node.

   ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

   ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Inicie sesión en el panel de administración web del GL-MT2500, vaya a **APPLICATIONS** -> **Tailscale** y habilite **Custom Exit Nodes**. Haga clic en el botón de actualización y seleccione en el menú desplegable la dirección IP de Leo-Desktop. Después, haga clic en **Apply**.

   ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

   A partir de ese momento, los dispositivos conectados al router enrutarán su tráfico a través del Exit Node para acceder a Internet, y todo el tráfico de Internet parecerá originarse desde la ubicación del Exit Node.

Referencias: [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
