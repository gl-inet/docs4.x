# AstroWarp

**Nota**: Esta guía cubre la nueva versión de AstroWarp.

La nueva versión de AstroWarp está integrada en el SDK del router GL.iNet. Adopta el protocolo AmneziaWG con ofuscación de tráfico integrada para ofrecer conexiones estables y seguras, ideales para un acceso remoto fiable en cualquier momento y desde cualquier lugar.

Esta función permite acceder de forma remota y sin interrupciones a su red doméstica. Puede configurarla y emparejar los dispositivos directamente mediante un código de acceso dinámico en el panel de administración web, estableciendo rápidamente una conexión segura entre su router de viaje y su red doméstica en solo unos segundos, sin necesidad de registrarse ni iniciar sesión.

Aunque AstroWarp heredado sigue apareciendo en el panel de administración web, dependía de una plataforma AstroWarp independiente para establecer conexiones remotas de red. Haga clic [aquí](https://docs.astrowarp.net/){target="_blank"} para consultar la documentación de AstroWarp heredado.

**Nota:**

1. No se recomienda usar AstroWarp al mismo tiempo que las siguientes funciones, ya que puede causar conflictos de enrutamiento: GoodCloud Site to Site, ZeroTier, Tailscale y Tor.
2. Cuando AstroWarp está habilitado, no se puede usar Network Mode.

## Modelos compatibles

??? "Modelos compatibles"

    Estos modelos son compatibles con la nueva versión de AstroWarp. Para consultar la lista de modelos compatibles con AstroWarp heredado, haga clic [aquí](https://docs.astrowarp.net/en/quick_start/){target="_blank"}.

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Nota**: Los modelos marcados con ※ admiten AstroWarp integrado en firmware beta.

??? "Modelos no compatibles"
    Estos dispositivos no son compatibles con la nueva versión de AstroWarp, aunque algunos modelos siguen funcionando con AstroWarp heredado. Consulte [este enlace](https://docs.astrowarp.net/en/quick_start/){target="_blank"} para ver los detalles.

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

    Inicie sesión en el panel de administración web de Flint 3 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos compatibles: Ethernet, Repeater, Tethering y Cellular.

    Como se muestra a continuación, el router doméstico Flint 3 está conectado al módem del ISP (Hong Kong Broadband Network Ltd) mediante un cable Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Genere el código de acceso.

    En el panel de administración web de Flint 3, vaya a **CLOUD SERVICES** -> **AstroWarp**. Haga clic en **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Se generará un **Access Code**. Copie este código para usarlo más adelante.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configure Slate 7 para Internet.

    Inicie sesión en el panel de administración web de Slate 7 y vaya a la página **INTERNET**. Conéctelo a Internet usando uno de los métodos compatibles: Ethernet, Repeater, Tethering y Cellular.

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

## FAQ

1. **P: ¿Cuál es el formato del código de acceso dinámico y cuánto tiempo es válido?**

    R: Es un código de 8 caracteres que combina números y letras mayúsculas, válido durante 10 minutos.

2. **P: ¿Qué ocurre con el router de viaje si finalizo la conexión en el router doméstico?**

    R: El router de viaje se desconectará y quedará en estado pendiente, sin acceso a la red. Cuando el router doméstico reanude la conexión, el router de viaje podrá reconectarse automáticamente sin volver a introducir el código de acceso.

3. **P: ¿Qué ocurre si se agotan los datos gratuitos o caduca el plan AstroWarp+ en el router doméstico?**

    R: El router de viaje pasará al estado pendiente, sin acceso a la red, y no cambiará automáticamente a la red local.

4. **P: ¿En qué situaciones entra el router de viaje en estado pendiente?**

    R: El router de viaje entrará en estado pendiente cuando el router doméstico cumpla cualquiera de las siguientes condiciones:

    - Finaliza la conexión de AstroWarp.
    - Agota la cuota de datos gratuitos.
    - Llega a la fecha de vencimiento del plan AstroWarp+ (si corresponde).
    - Pierde el acceso a Internet.

5. **P: ¿Qué hace el botón Reset en la esquina superior derecha?**

    R: Borra todos los dispositivos autorizados y vuelve a la página de selección de la función del router para que pueda volver a elegirla.

6. **P: ¿Qué ocurre con el router de viaje si restablezco AstroWarp en el router doméstico?**

    R: Una vez restablecido AstroWarp en el router doméstico, los dispositivos conectados de forma remota se desconectarán de la red AstroWarp y volverán a su red local para acceder a Internet.

7. **P: Si actualizo el router doméstico al plan AstroWarp+ y cambio su función a router de viaje mientras el plan sigue vigente, ¿se conserva el tiempo restante del plan?**

    R: El periodo restante no se conserva y caducará en la fecha prevista. Para evitar pérdidas innecesarias, cambie la función del dispositivo después de que venza su plan actual.

8. **P: Si he habilitado la nueva versión de AstroWarp en el panel de administración web del router, ¿cómo la desactivo y vuelvo a AstroWarp heredado?**

    R: En el panel de administración web del router, vaya a **CLOUD SERVICES** -> **AstroWarp** y haga clic en **Reset** en la esquina superior derecha.

    ![reset](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/reset.png){class="glboxshadow"}

    Luego inicie sesión en [astrowarp.net](https://my.astrowarp.net/#/login){target="_blank"} con su cuenta en la nube. Después de iniciar sesión, haga clic en el botón **"+"** para añadir el router a su red AstroWarp.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/add_device.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
