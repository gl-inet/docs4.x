# GoodPAS

**Nota**: Esta función se introdujo en el firmware v4.10, versión en la que AstroWarp pasó a llamarse GoodPAS. Si su dispositivo ejecuta una versión de firmware anterior, consulte [AstroWarp](./astrowarp.md).

---

En el lado izquierdo del panel de administración web, vaya a **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS es una solución avanzada de acceso remoto integrada en el SDK de los routers GL.iNet. Utiliza el protocolo AmneziaWG con ofuscación de tráfico integrada para ofrecer conexiones estables y seguras que permiten un acceso remoto fiable en cualquier momento y lugar.

Esta función permite acceder de forma remota y fluida a su red doméstica. Puede configurar y emparejar dispositivos directamente mediante un código de acceso dinámico en el panel de administración web, estableciendo en pocos segundos una conexión segura entre el router de viaje y la red doméstica, sin necesidad de registrarse ni iniciar sesión.

**Nota**:

1. No se recomienda usar GoodPAS al mismo tiempo que las siguientes funciones, ya que podría causar conflictos de enrutamiento: GoodCloud Site to Site, ZeroTier, Tailscale y Tor.

2. Cuando GoodPAS está habilitado, no se puede usar Network Mode.

## Configuración rápida

En el siguiente ejemplo, usaremos **Flint 3 (GL-BE9300)** y **Mango 2 (GL-MG1300)** para configurar una red GoodPAS.

Flint 3 actuará como router doméstico, mientras que Mango 2 funcionará como router de viaje y enviará el tráfico de red de vuelta a Flint 3 para acceder a Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configure Flint 3 para acceder a Internet.

    Inicie sesión en el panel de administración web de Flint 3 y vaya a la página INTERNET. Conéctelo a Internet mediante uno de los métodos compatibles: Ethernet, Repeater, Tethering o Cellular.

    Como se muestra a continuación, el router doméstico Flint 3 está conectado mediante un cable Ethernet al módem del proveedor de Internet (Hong Kong Broadband Network Ltd).

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Genere un código de acceso.

    En el panel de administración web de Flint 3, vaya a **CLOUD SERVICES** -> **GoodPAS**. Haga clic en **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Se generará un Access Code. Cópielo para usarlo más adelante.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configure Mango 2 para acceder a Internet.

    Inicie sesión en el panel de administración web de Mango 2 y vaya a la página INTERNET. Conéctelo a Internet mediante uno de los métodos compatibles: Ethernet, Repeater, Tethering o Cellular.

    Como se muestra a continuación, el router de viaje Mango 2 está conectado al punto de acceso personal de un iPhone 17 (situado en Shenzhen y conectado a la red China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Introduzca el código de acceso.

    En el panel de administración web de Mango 2, vaya a **CLOUD SERVICES** -> **GoodPAS**. Haga clic en **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Introduzca el código de acceso obtenido en el paso 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Espere a que finalice la verificación.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    A continuación, se conectará correctamente al router doméstico Flint 3. Ahora podrá navegar por Internet de forma segura a través de su red doméstica.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    El panel de administración web de Flint 3 también muestra el estado de la conexión, como se indica a continuación.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Probar la conectividad

1. Conecte un portátil o smartphone al Wi-Fi del router de viaje Mango 2.

2. Abra un navegador y visite [ipcheck.ing](https://ipcheck.ing/){target="_blank"} o cualquier otro sitio web de consulta de direcciones IP.

    Se mostrará la dirección IP pública de Flint 3, lo que indica que Mango 2 está accediendo a Internet a través del router doméstico Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Desconecte GoodPAS en Mango 2 y, a continuación, actualice la página web para volver a enviar la consulta de IP.

    Se mostrará la dirección IP pública de Mango 2, lo que indica que Mango 2 está accediendo a Internet a través de su red local.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **P: ¿Qué formato tiene el código de acceso dinámico y durante cuánto tiempo es válido?**

    R: Es un código de 8 caracteres que combina números y letras mayúsculas, válido durante 10 minutos.

2. **P: ¿Qué ocurre con el router de viaje si finalizo la conexión en el router doméstico?**

    R: El router de viaje se desconectará y quedará en estado pendiente, sin acceso a la red. Cuando el router doméstico reanude la conexión, el router de viaje podrá reconectarse automáticamente sin tener que volver a introducir el código de acceso.

3. **P: ¿En qué situaciones entra el router de viaje en estado pendiente?**

    R: El router de viaje entrará en estado pendiente cuando el router doméstico cumpla alguna de las siguientes condiciones:

    - Finaliza la conexión GoodPAS.
    - Pierde el acceso a Internet.

4. **P: ¿Qué hace el botón Reset de la esquina superior derecha?**

    R: Borra todos los dispositivos autorizados y vuelve a la página de selección de la función del router para que pueda seleccionarla de nuevo.

5. **P: ¿Qué ocurre con el router de viaje si restablezco GoodPAS en el router doméstico?**

    R: Cuando se restablezca el router doméstico, los dispositivos conectados de forma remota se desconectarán de la red GoodPAS y volverán a usar su red local para acceder a Internet.

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
