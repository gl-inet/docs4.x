# AstroWarp

**Nota**: Esta guía presenta la nueva versión de AstroWarp, integrada en el panel de administración web de GL.iNet.

Para consultar la documentación de AstroWarp heredado, visite [este enlace](https://docs.astrowarp.net/){target="_blank"}.

---

AstroWarp es una función de red avanzada integrada en los routers GL.iNet. Permite acceder de forma remota y sin interrupciones a su red doméstica sin necesidad de registrarse ni iniciar sesión. Gracias al protocolo AmneziaWG con ofuscación de tráfico integrada, mantiene la conexión estable y segura, por lo que resulta ideal para un acceso remoto fiable desde cualquier lugar.

Los usuarios pueden configurar una red AstroWarp directamente desde el panel de administración del router GL.iNet. Solo tiene que emparejar sus routers con un código de acceso y podrá conectar de forma segura su router de viaje a su red doméstica en cuestión de segundos.

**Nota:**

1. No se recomienda usar AstroWarp al mismo tiempo que las siguientes funciones, ya que puede causar conflictos de enrutamiento: GoodCloud Site to Site, ZeroTier, Tailscale y Tor.
2. Cuando AstroWarp está habilitado, no se puede usar Network Mode.

## Modelos compatibles

??? "Modelos compatibles"

    - GL-BE9300 (Flint 3), versión estable v4.8.4
    - GL-BE3600 (Slate 7), versión estable v4.8.3
    - GL-MT6000 (Flint 2), Beta v4.8.4
    - GL-X3000 (Spitz AX), Beta v4.8.4
    - GL-XE3000 (Puli AX), Beta v4.8.4
    - GL-AX1800 (Flint), Beta v4.8.4
    - GL-AXT1800 (Slate AX), Beta v4.8.3
    - GL-MT3000 (Beryl AX), Beta v4.8.2

??? "Modelos no compatibles"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Configuración rápida

En el siguiente ejemplo, usaremos **Flint 3 (GL-BE9300)** y **Slate 7 (GL-BE3600)** para configurar una red AstroWarp.

Flint 3 actuará como router doméstico, mientras que Slate 7 actuará como router de viaje que redirige el tráfico de red de vuelta a Flint 3 para acceder a Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Nota**: Cada router GL.iNet incluye **10 GB de datos gratuitos al mes** para redes AstroWarp. Los dispositivos de una red AstroWarp usarán los datos del router doméstico para acceder a Internet. Puede actualizar al plan AstroWarp+ para disponer de datos ilimitados según sea necesario.

1. Configure Flint 3 para Internet.

    Inicie sesión en el panel de administración web de Flint 3 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos compatibles: Ethernet, Repeater, Tethering o Cellular.

    Como se muestra a continuación, el router doméstico Flint 3 está conectado al módem del ISP (Hong Kong Broadband Network Ltd) mediante un cable Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Genere el código de acceso.

    En el panel de administración web de Flint 3, vaya a **CLOUD SERVICES** -> **AstroWarp**. Haga clic en **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Se generará un **Access Code**. Copie este código para usarlo más adelante.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configure Slate 7 para Internet.

    Inicie sesión en el panel de administración web de Slate 7 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos compatibles: Ethernet, Repeater, Tethering o Cellular.

    Como se muestra a continuación, el router de viaje Slate 7 está conectado al hotspot personal de un iPhone 15 Pro, situado en Shenzhen y usando la red China Unicom Guangdong Province.

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

2. Abra un navegador y visite [ipcheck.ing](https://ipcheck.ing/){target="_blank"} o cualquier otro sitio web de consulta de direcciones IP.

    Mostrará la dirección IP pública de Flint 3, lo que indica que Slate 7 accede a Internet a través de su router doméstico Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Desconecte la conexión AstroWarp en Slate 7 y, a continuación, actualice la página web para volver a enviar la consulta de IP.

    Mostrará la dirección IP pública de Slate 7, lo que indica que Slate 7 está accediendo a Internet a través de su red local.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Plan de actualización

Cada router GL.iNet incluye **10 GB de datos gratuitos al mes** para redes AstroWarp. Los dispositivos de una red AstroWarp usarán los datos del router doméstico para acceder a Internet.

Puede actualizar al plan **AstroWarp+** para disponer de datos ilimitados según sea necesario.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
