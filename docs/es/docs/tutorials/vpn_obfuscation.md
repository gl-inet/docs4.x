# Cómo configurar VPN Obfuscation en los routers GL.iNet

## ¿Qué es VPN Obfuscation?

La ofuscación de VPN es una técnica que disfraza el tráfico VPN para que parezca tráfico normal de Internet. Esto ayuda a los usuarios a sortear restricciones de red y censura, especialmente en regiones con políticas de Internet estrictas.

- Oculta las características propias de la VPN para evitar su detección por parte de los ISP, firewalls o sistemas de Deep Packet Inspection (DPI).

- Hace que la conexión VPN parezca tráfico web estándar, lo que mejora la estabilidad de la conexión y la tasa de éxito en redes restringidas.

## ¿Qué es AmneziaWG?

AmneziaWG es un protocolo VPN basado en WireGuard, con ofuscación de tráfico integrada. Conserva las principales ventajas de WireGuard, como alta velocidad, diseño ligero y baja latencia, al tiempo que añade un módulo específico de ofuscación. Este módulo oculta eficazmente los patrones del tráfico VPN, lo que permite tanto a usuarios particulares como a empresas proteger su privacidad en línea, sortear restricciones regionales y evitar interrupciones de conexión causadas por controles de red estrictos.

AmneziaWG es compatible con una amplia gama de dispositivos, incluidos Windows, macOS, iOS, Android, Linux y routers, y ofrece conexiones VPN ofuscadas fiables en distintos escenarios.

Actualmente, varios routers GL.iNet, por ejemplo **Brume 3**, **Flint 3**, **Flint 2** y **Beryl AX**, admiten el protocolo AmneziaWG en determinadas versiones de firmware. La compatibilidad oficial completa estará disponible en el firmware ver. 4.9 y se extenderá gradualmente a más modelos.

## Configuración rápida

A continuación se muestran dos escenarios típicos para configurar la ofuscación VPN de AmneziaWG en routers GL.iNet.

### Escenario 1. Usar dos routers GL.iNet

Este escenario utiliza dos routers GL.iNet para establecer una conexión VPN ofuscada mediante el protocolo AmneziaWG.

- **Brume 3 (GL-MT5000)**: actúa como servidor VPN para uso doméstico.
- **Beryl AX (GL-MT3000)**: actúa como cliente VPN portátil para uso fuera de casa.

#### Configurar el servidor VPN

1. Inicie sesión en el panel de administración web del Brume 3.

   Conecte un dispositivo, por ejemplo su portátil o PC, al puerto LAN del Brume 3 mediante un cable Ethernet. Abra un navegador, introduzca la dirección de administración predeterminada, normalmente `192.168.8.1`, e inicie sesión con su contraseña de administrador.

2. Complete la configuración inicial del Brume 3 para el acceso a Internet.

   Si el Brume 3 se utiliza como router principal, conecte su puerto WAN a la red ascendente, como un módem del ISP.

   Si no es el router principal, es decir, hay otro dispositivo ascendente, como un router del ISP, actuando como router principal, deberá configurar **port forwarding** en su router principal. Consulte [este enlace](how_to_set_up_port_forwarding.md).

3. Habilite DDNS, opcional.

   Active la función DDNS si su IP pública no es estática, sino dinámica.

   En la barra lateral izquierda, vaya a **APPLICATIONS** -> **Dynamic DNS**. Active **Enable DDNS**, acepte los **Terms of Service & Privacy Policy** y haga clic en **Apply**.

   ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. Habilite VPN Obfuscation.

   En la barra lateral izquierda, vaya a **VPN** -> **WireGuard Server** -> pestaña **Configurations**, active **Enable Obfuscation** y haga clic en **Apply**.

   ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

   Puede personalizar los parámetros de ofuscación según sus necesidades. Recomendamos mantener la configuración predeterminada.

   ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Exporte el archivo de configuración.

   En la página **WireGuard Server**, cambie a la pestaña **Profiles** y haga clic en el botón **Add** para crear un archivo de configuración que permita conectar el Beryl AX.

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

   Establezca un nombre descriptivo, por ejemplo Travel Router, y haga clic en **Apply**.

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

   En la ventana emergente, haga clic en **Export** para descargar la configuración en su equipo local, que usará más adelante.

   ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Inicie el servidor VPN.

   En la parte superior de la página **WireGuard Server**, haga clic en el botón **Start** para ejecutar el servidor.

   ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

   Con esto, su servidor VPN con ofuscación AmneziaWG quedará habilitado. Ahora puede conectarse a este servidor VPN del Brume 3 mediante la app de AmneziaWG o con un router GL.iNet que ejecute un firmware compatible con la ofuscación AmneziaWG.

   **Nota: Los clientes que no admiten la ofuscación AmneziaWG no podrán conectarse.**

   ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### Configurar el cliente VPN

1. Inicie sesión en el panel de administración web del Beryl AX.

   Conecte un dispositivo, por ejemplo su portátil o PC, a la red Wi-Fi o al puerto LAN del Beryl AX mediante un cable Ethernet. Abra un navegador, introduzca la dirección de administración predeterminada, normalmente `192.168.8.1`, e inicie sesión con su contraseña de administrador.

2. Complete la configuración inicial del Beryl AX para el acceso a Internet.

   **Consejo**: conecte el Beryl AX a una red distinta de la del Brume 3. Por ejemplo, puede habilitar un punto de acceso móvil para que el Beryl AX se conecte a él.

3. Suba el archivo de configuración.

   En la barra lateral izquierda, vaya a **VPN** -> **WireGuard Client**. Añada un grupo nuevo y establezca un nombre descriptivo, por ejemplo Home Router.

   ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

   Suba en la parte derecha el archivo de configuración exportado anteriormente.

   ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

   Después de subir el archivo de configuración y de que pase la verificación, haga clic en **Apply**.

   ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

   La página se actualizará y se mostrará un archivo de configuración en la lista.

4. Inicie la conexión VPN.

   Haga clic en el icono de tres puntos y seleccione **Start**.

   ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

   Espere aproximadamente 1 minuto. Si el indicador de estado se vuelve verde, significa que la conexión VPN se ha establecido correctamente.

   ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

   Vaya a **VPN Dashboard** y verá que el Beryl AX se ha conectado al router doméstico Brume 3.

   ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Vuelva a comprobarlo, opcional.

   Inicie sesión en el panel de administración web del Brume 3 y vaya a **VPN** -> **WireGuard Server**. También verá un cliente en línea, que es el Beryl AX, conectado actualmente a este servidor VPN del Brume 3.

   ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

   La conexión VPN ya está completa. Todos los dispositivos del Beryl AX acceden ahora a Internet a través de la puerta de enlace del Brume 3, lo que habilita una conexión VPN ofuscada.

### Escenario 2. Usar un solo router GL.iNet

Este escenario usa un único router GL.iNet, **Brume 3 (GL-MT5000)**, como cliente VPN para conectarse a un servidor AmneziaVPN.

No es necesario configurar su propio servidor. Puede establecer una conexión VPN ofuscada directamente usando los servidores oficiales de AmneziaVPN, se requiere una suscripción Amnezia Premium.

#### Descargar la configuración

1. Inicie sesión en el [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="\_blank"} con su Subscription Key.

   ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. En el panel de Amnezia, vaya a **Connection Assets** -> **Configuration Files**, seleccione un país y descargue un archivo de configuración en su equipo local para usarlo después.

   ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

#### Configurar el cliente VPN

1. Inicie sesión en el panel de administración web del Brume 3.

   Conecte un dispositivo, por ejemplo su portátil o PC, al puerto LAN del Brume 3 mediante un cable Ethernet. Abra un navegador, introduzca la dirección de administración predeterminada, normalmente `192.168.8.1`, e inicie sesión con su contraseña de administrador.

2. Complete la configuración inicial del Brume 3 para el acceso a Internet.

3. Suba el archivo de configuración.

   En la barra lateral izquierda, vaya a **VPN** -> **WireGuard Client**. Añada un grupo nuevo y establezca un nombre descriptivo, por ejemplo AmneziaVPN.

   ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

   Suba en la parte derecha el archivo de configuración de AmneziaVPN exportado previamente.

   ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

   Después de subir el archivo de configuración y de que pase la verificación, haga clic en **Apply**.

   ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

   La página se actualizará y se mostrará un archivo de configuración en la lista.

4. Inicie la conexión VPN.

   Haga clic en el icono de tres puntos y seleccione **Start**.

   ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

   Espere aproximadamente 1 minuto. Si el indicador de estado se vuelve verde, significa que la conexión VPN se ha establecido correctamente.

   ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

   Vaya a **VPN Dashboard** y verá que el Brume 3 se ha conectado a un servidor de AmneziaVPN.

   ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

   La conexión VPN ya está completa. Todos los dispositivos del Brume 3 acceden ahora a Internet a través del servidor de AmneziaVPN, lo que habilita una conexión VPN ofuscada.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
