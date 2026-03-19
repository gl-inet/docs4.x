# AstroWarp

**Nota**: Esta guía presenta la nueva versión de AstroWarp, actualmente disponible en **Flint 3 (GL-BE9300)** y **Slate 7 (GL-BE3600)** con firmware v4.8.4 y v4.8.3, respectivamente.

Para otros modelos, consulte [este enlace](https://docs.astrowarp.net/){target="\_blank"} para obtener más información.

---

AstroWarp es una función de red avanzada integrada en los routers GL.iNet. Permite un acceso remoto fluido a su red doméstica sin necesidad de registro ni inicio de sesión. Al usar el protocolo AmneziaWG con ofuscación de tráfico incorporada, mantiene la conexión estable y segura, lo que lo hace ideal para un acceso remoto fiable dondequiera que esté.

Los usuarios pueden configurar una red AstroWarp directamente desde el panel de administración del router GL.iNet. Solo tiene que emparejar sus routers mediante un código de acceso y podrá conectar de forma segura su router de viaje a su red doméstica en cuestión de segundos.

**Nota:**

1. No se recomienda usar AstroWarp al mismo tiempo que cualquiera de las siguientes funciones, ya que esto puede causar conflictos de enrutamiento: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Cuando AstroWarp está habilitado, no se puede usar Network Mode.

## Configuración rápida

En el siguiente ejemplo, usaremos **Flint 3 (GL-BE9300)** y **Slate 7 (GL-BE3600)** para configurar una red AstroWarp.

Flint 3 actuará como router doméstico, mientras que Slate 7 actuará como router de viaje que redirige el tráfico de red de vuelta a Flint 3 para acceder a Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Nota**: Cada router GL.iNet incluye **10 GB de datos gratuitos al mes** para la red AstroWarp. Los dispositivos de una red AstroWarp usarán los datos del router doméstico para acceder a Internet. Puede actualizar al plan AstroWarp+ para disponer de datos ilimitados según sea necesario.

1. Configure Flint 3 para Internet.

   Inicie sesión en el panel de administración web de Flint 3 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos de conexión compatibles: Ethernet, Repeater, Tethering y Cellular.

   Como se muestra a continuación, el router doméstico Flint 3 está conectado al módem del ISP, Hong Kong Broadband Network Ltd, mediante un cable Ethernet.

   ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Genere el código de acceso.

   En el panel de administración web de Flint 3, vaya a **CLOUD SERVICES** -> **AstroWarp**. Haga clic en **Use At Home**.

   ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

   Se generará un **Access Code**. Copie este código para usarlo más adelante.

   ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configure Slate 7 para Internet.

   Inicie sesión en el panel de administración web de Slate 7 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos de conexión compatibles: Ethernet, Repeater, Tethering y Cellular.

   Como se muestra a continuación, el router de viaje Slate 7 está conectado al hotspot personal de un iPhone 15 Pro, ubicado en Shenzhen y usando la red China Unicom Guangdong Province.

   ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Introduzca el código de acceso.

   En el panel de administración web de Slate 7, vaya a **CLOUD SERVICES** -> **AstroWarp**. Haga clic en **Use While Travelling**.

   ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

   Introduzca el Access Code obtenido en el paso 2.

   ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

   Espere a que se complete la verificación.

   ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

   A continuación, se conectará correctamente al router doméstico Flint 3. Ahora podrá navegar por Internet a través de su red doméstica de forma segura.

   ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

   En el panel de administración web de Flint 3 también se mostrará el estado de la conexión, como se indica a continuación.

   ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Probar la conectividad

1. Conecte un portátil o smartphone al Wi-Fi del router de viaje Slate 7.

2. Abra un navegador y visite [ipcheck.ing](https://ipcheck.ing/){target="\_blank"} o cualquier otro sitio web de consulta de direcciones IP.

   Mostrará la dirección IP pública de Flint 3, lo que indica que Slate 7 está accediendo a Internet a través de su router doméstico Flint 3.

   ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Desconecte la conexión AstroWarp en Slate 7 y luego actualice la página web para volver a enviar la consulta de IP.

   Mostrará la dirección IP pública de Slate 7, lo que indica que Slate 7 está accediendo a Internet a través de su red local.

   ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Plan de actualización

Cada router GL.iNet incluye **10 GB de datos gratuitos al mes** para redes AstroWarp. Los dispositivos de una red AstroWarp usarán los datos del router doméstico para acceder a Internet.

Puede actualizar al plan **AstroWarp+** para disponer de datos ilimitados según sea necesario.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
