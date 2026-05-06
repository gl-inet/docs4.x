# ZeroTier

ZeroTier es una red privada virtual (VPN) basada en software que permite comunicaciones seguras y cifradas entre dispositivos a través de Internet. Crea una red privada virtual que permite que los dispositivos se comuniquen como si estuvieran en la misma red local, independientemente de su ubicación física o de la topología de la red. ZeroTier está diseñado para ser fácil de configurar y usar, y ofrece funciones como cifrado de extremo a extremo, segmentación de red y capacidades de conexión en puente.

La función ZeroTier en los routers GL.iNet, disponible desde el firmware v4.2, permite que el router se una a una red virtual ZeroTier. Una vez conectado, puede acceder al router de forma remota, incluidos sus recursos WAN y LAN.

**Nota**:

1. No se recomienda usar ZeroTier al mismo tiempo que ninguna de las siguientes funciones o servicios, ya que esto puede provocar conflictos de enrutamiento: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale y AstroWarp.

2. Esta función se encuentra actualmente en fase beta y puede contener algunos errores.

3. Algunos modelos, aunque ejecuten el firmware v4.2 o superior, no admiten ZeroTier por memoria insuficiente.

## Modelos compatibles

??? "Modelos compatibles" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-AX1800 (Flint) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus)

??? "Modelos no compatibles" - GL-X2000 (Spitz Plus) - GL-SFT1200 (Opal) - GL-MT1300 (Beryl) - GL-E750/E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-AP1300 (Cirrus) - GL-S1300 (Convexa-S) - GL-X300B (Collie)

## Configurar la red ZeroTier

Hay dos versiones de ZeroTier Central disponibles: New Central y Legacy Central.

- **New Central**: una versión más reciente de ZeroTier Central, con mejor usabilidad y nuevas funciones. Se recomienda a los nuevos usuarios para disfrutar de la mejor experiencia y las herramientas más recientes.

- **Legacy Central**: para cuentas creadas antes de noviembre de 2025. Legacy Central sigue permitiendo a los usuarios existentes gestionar sus redes.

Ambas versiones pueden utilizarse en paralelo, pero actualmente no existe una ruta de migración directa.

Seleccione la versión adecuada para continuar.

### New Central

El siguiente ejemplo utiliza el GL-MT3600BE.

1. Visite el [sitio web oficial de ZeroTier](https://www.zerotier.com/){target="\_blank"} e inicie sesión con su cuenta.

   ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Cree una organización.

   ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Seleccione un plan. Aquí usamos como ejemplo el plan Personal, que incluye 10 dispositivos, 1 administrador de red y 1 red. Si necesita crear más redes, añadir más dispositivos o agregar rutas personalizadas y DNS, elija el plan Essential o Scale.

   ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Ahora su red ZeroTier ya está creada. Tome nota del **Network ID**, que es una combinación alfanumérica de 16 caracteres situada en la esquina superior derecha, ya que será necesaria al conectar otros dispositivos más adelante.

   ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Habilite ZeroTier en el router GL.iNet.

   Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **ZeroTier**.

   Habilite ZeroTier, introduzca el Network ID en la misma página y haga clic en **Apply**.

   ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

   Al cabo de un momento, la interfaz indicará que se requiere autorización. Haga clic en el hipervínculo **ZeroTier Central** para ir a ZeroTier Central.

   ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autorice su dispositivo en ZeroTier Central.

   En ZeroTier Central, localice el dispositivo pendiente y autorícelo.

   ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

   Una vez autorizado, la página se mostrará de la siguiente manera.

   ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Añada otro dispositivo, como un ordenador o un smartphone, a la misma red ZeroTier siguiendo [esta guía](https://docs.zerotier.com/platforms/){target="\_blank"}.

   A continuación se muestra un ejemplo con un portátil con Windows 10 Pro.
   1. Instale ZeroTier en el portátil desde [aquí](https://www.zerotier.com/download/){target="\_blank"}.

   2. Inicie ZeroTier. El icono de ZeroTier aparecerá en la bandeja del sistema, en la esquina inferior derecha del escritorio.

   3. Haga clic con el botón derecho sobre el icono, seleccione **Join New Network** e introduzca en la ventana emergente el **Network ID** obtenido en el paso 4.

      ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

      Después, vaya a ZeroTier Central, localice el dispositivo pendiente y autorícelo.

      ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

   4. Una vez autorizado, la página se mostrará como se indica a continuación. Verá los detalles de los dispositivos miembros, como **Device ID**, **Name**, **Status**, **Managed IP** y **Public IP**.

      ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

      **Consejo**: Puede hacer clic en el icono de tres puntos de la derecha para editar la configuración del dispositivo miembro, incluido el nombre del dispositivo, la(s) Managed IP y la configuración avanzada.

8. Haga clic en la **Managed IP** del router para copiarla. Después podrá usar esa Managed IP para acceder al router desde el portátil que está en la misma red ZeroTier.

   ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Compruebe la conectividad.

   En el portátil conectado a la misma red ZeroTier, abra un navegador web e introduzca la Managed IP del router obtenida en el paso anterior.

   Si puede acceder al panel de administración web del router, la conexión ZeroTier se ha realizado correctamente.

   ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

   También puede hacer `ping` a la Managed IP del router desde su portátil para comprobar la conectividad. Si recibe una respuesta correcta, la conexión ZeroTier se ha establecido correctamente.

   ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

El siguiente ejemplo utiliza el GL-MT2500.

1. Cree su primera red ZeroTier.

   Consulte la [guía oficial de inicio](https://docs.zerotier.com/getting-started/getting-started/){target="\_blank"} de ZeroTier para crear una cuenta y una red ZeroTier. Recuerde tomar nota del Network ID, que es una combinación alfanumérica de 16 caracteres, ya que será necesaria al conectar otros dispositivos más adelante.

   ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Habilite ZeroTier en el router GL.iNet.

   Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **ZeroTier**.

   Habilite ZeroTier, introduzca el Network ID en la misma página y haga clic en **Apply**.

   ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

   Al cabo de un momento, la interfaz indicará que se requiere autorización.

   Haga clic en el hipervínculo **ZeroTier Central** para ir a ZeroTier Central.

   ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autorice su dispositivo en ZeroTier Central.

   En ZeroTier Central, vaya a la sección **Members**. Localice el nuevo dispositivo y marque la casilla **Auth** para autorizarlo. Si lo desea, personalice el nombre del dispositivo.

   ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

   Al cabo de un momento, ZeroTier asignará una **Managed IP** al dispositivo. Tome nota de esta dirección IP, ya que se utilizará en el paso de prueba.

   ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. Añada otro dispositivo, como un ordenador o un smartphone, a la misma red ZeroTier siguiendo [esta guía](https://docs.zerotier.com/platforms/){target="\_blank"}.

5. Compruebe la conectividad.

   En otro dispositivo conectado a la misma red ZeroTier, abra un navegador web e introduzca la ZeroTier Managed IP del router obtenida en el paso anterior.

   Podrá acceder al panel de administración web del router.

   ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

   También puede usar el comando `ping` para comprobar la conectividad. Consulte la [guía rápida](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="\_blank"} de ZeroTier.

## Allow Remote Access WAN

Si esta opción está habilitada, se podrá acceder a los recursos del lado WAN del dispositivo a través de la red virtual ZeroTier.

Por ejemplo, como se muestra en la topología siguiente, si esta función está habilitada, puede acceder al `GL-AXT1800` mediante su dirección IP (`192.168.29.1`) desde `leo-phone`. Esto se debe a que el GL-AXT1800 es el dispositivo de nivel superior del `GL-MT2500`, y este último está conectado a la misma red ZeroTier que leo-phone.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Nota**: Para que esta función surta efecto, es necesario añadir reglas de enrutamiento a la red ZeroTier. En Legacy Central se puede añadir una ruta personalizada gratuitamente, mientras que en New Central solo se pueden configurar rutas personalizadas con un plan Essential o superior. Haga clic [aquí](https://www.zerotier.com/pricing/) para obtener más información.

Los pasos siguientes usan Legacy Central como ejemplo.

1. Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **ZeroTier**.

   Habilite **Allow Remote Access WAN** y haga clic en **Apply**.

   ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

   El sistema le pedirá que configure reglas de enrutamiento. Mantenga esta página web abierta o anote los detalles de la ruta (Destination y Via), ya que serán necesarios en el siguiente paso.

   ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Vaya a **ZeroTier Central** y localice la sección **Advanced**.

   Introduzca los detalles de la ruta (Destination y Via) obtenidos en el paso anterior y, a continuación, haga clic en **Submit**.

   ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

   Una vez añadida la ruta, la sección **Managed Routes** se mostrará como se indica a continuación.

   ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Ahora puede acceder al `GL-AXT1800` mediante su dirección IP (`192.168.29.1`) desde otros dispositivos. De hecho, puede acceder a todos los dispositivos dentro de la subred `192.168.29.0/24`.

   ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

Si esta opción está habilitada, se podrá acceder a los recursos del lado LAN del dispositivo a través de la red virtual ZeroTier.

Por ejemplo, como se muestra en la topología siguiente, si esta función está habilitada, puede iniciar sesión por SSH en `Ubuntu` mediante su dirección IP (`192.168.8.110`) desde `leo-phone`. Esto se debe a que `Ubuntu` es el dispositivo de nivel inferior del `GL-MT2500`, y este último está conectado a la misma red ZeroTier que leo-phone.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Nota**: Para que esta función surta efecto, es necesario añadir reglas de enrutamiento a la red ZeroTier. En Legacy Central se puede añadir una ruta personalizada gratuitamente, mientras que en New Central solo se pueden configurar rutas personalizadas con un plan Essential o superior. Haga clic [aquí](https://www.zerotier.com/pricing/) para obtener más información.

Los pasos siguientes usan Legacy Central como ejemplo.

1. Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **ZeroTier**.

   Habilite **Allow Remote Access LAN** y haga clic en **Apply**.

   ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

   El sistema le pedirá que configure reglas de enrutamiento. Mantenga esta página web abierta o anote los detalles de la ruta (Destination y Via), ya que serán necesarios en el siguiente paso.

   ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Vaya a **ZeroTier Central** y localice la sección **Advanced**.

   Introduzca los detalles de la ruta (Destination y Via) obtenidos en el paso anterior y, a continuación, haga clic en **Submit**.

   ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

   Una vez añadida la ruta, la sección **Managed Routes** se mostrará como se indica a continuación.

   ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Ahora puede hacer ping o iniciar sesión por SSH en `Ubuntu` mediante su dirección IP (`192.168.8.110`) desde otros dispositivos. De hecho, puede acceder a todos los dispositivos dentro de la subred `192.168.8.0/24`.

   ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
