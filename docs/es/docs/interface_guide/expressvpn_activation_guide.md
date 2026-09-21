# Guía de activación de ExpressVPN

**Nota:** Esta guía solo se aplica al router de marca compartida de GL.iNet y ExpressVPN **Fortify (GL-MT6000)**.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} es uno de los servicios VPN premium líderes en el mundo diseñado para proteger su privacidad en línea, asegurar su conexión a Internet y permitir la transmisión segura desde cualquier lugar. Ofrece velocidades ultrarrápidas, cifrado de nivel militar y acceso a servidores en más de 100 países. Ya sea que desee transmitir, navegar de forma privada o proteger sus datos en una red Wi-Fi pública, ExpressVPN le brinda una experiencia rápida y segura.

**Fortify (GL-MT6000)** es un enrutador de marca compartida lanzado conjuntamente por GL.iNet y ExpressVPN. Cada unidad viene con una suscripción gratuita a ExpressVPN por un año. Los usuarios pueden canjear la suscripción y conectar sus cuentas directamente en el Panel de administración web del enrutador. Una vez activado, todo el tráfico que pase a través del enrutador aprovechará la red de alta velocidad y el cifrado sólido de ExpressVPN para proteger toda su conexión de red y su privacidad en línea.

Esta guía lo guía para canjear el plan ExpressVPN de 12 meses dentro del Panel de administración web del enrutador. También cubre la personalización de políticas de VPN según sus escenarios y requisitos de uso, ayudándolo a disfrutar sin esfuerzo de una conectividad a Internet cifrada, segura y de alta velocidad.

## Canjear el plan ExpressVPN

Inicie sesión en el panel de administración web de Fortify y navegue hasta **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Lea y acepte **Terms of Service** y **Privacy Policy**, luego haga clic en **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Haga clic en **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

En la ventana emergente, ingrese su **Order ID**. Si compró este enrutador en la tienda GL.iNet, también se requiere **Order Email**. Luego haga clic en **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

Se le dirigirá al proceso de pago de ExpressVPN. Se aplicó un código de canje en el derecho para activar la suscripción de 12 meses sin cargo adicional.

Ingrese su dirección de correo electrónico en la parte superior y agregue un método de pago para garantizar un acceso VPN ininterrumpido al final del plazo inicial. Luego haga clic en **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Tu plan ha sido activado. Regrese al Panel de administración web de su enrutador Fortify para iniciar sesión con su cuenta.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Inicie sesión en ExpressVPN

En el panel de administración web de Fortify, vaya a **VPN** -> **VPN Client Profile**.

Haga clic en **Log in to ExpressVPN** y será dirigido a la página de inicio de sesión seguro de ExpressVPN.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Ingrese su correo electrónico y haga clic en **Send Code**. Se enviará un código de verificación de 6 dígitos a su correo electrónico.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Ingrese el código de verificación y haga clic en **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Cambie su contraseña para activar su cuenta.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

En el siguiente paso, haga clic en **Yes** para autorizar el acceso a ExpressVPN en su enrutador.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Inicie sesión exitosamente. Puede cerrar esta ventana del navegador y volver a su dispositivo.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

En el panel de administración web de Fortify, vaya a **VPN** -> **VPN Client Profile**.

Ha iniciado sesión en ExpressVPN en este enrutador. Haga clic en **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Ahora puedes agregar túneles VPN y configurar políticas VPN según tus necesidades.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## Agregar túnel VPN

### Pasos generales

Siga los pasos a continuación para agregar su túnel VPN y configurar políticas VPN. Consulte la [Referencia del caso](#case-reference) si es necesario.

1. En el panel de administración web de Fortify, vaya a **VPN** -> **ExpressVPN Dashboard**. Haga clic en **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Seleccione el perfil VPN y luego haga clic en **Next**.

    Obtendrá una lista de perfiles de ExpressVPN. Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        Cuando se seleccionan varios perfiles, el túnel intentará conectarse utilizando cada perfil en orden de prioridad hasta que se establezca una conexión exitosamente. Si todos los perfiles dentro de un único túnel no logran conectarse, el sistema determinará si se debe cambiar a la red local (WAN) del enrutador según el estado del Kill Switch en las configuraciones [Opciones de túnel](#tunnel-options) y [All Other Traffic](#all-other-traffic).

3. Seleccione la fuente del cliente y luego haga clic en **Next**.

    Hay cuatro opciones:

    - **All Clients**: si se selecciona, el tráfico de todos los dispositivos coincidirá con esta regla.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: si se selecciona, el tráfico de tipos de conexión específicos (por ejemplo, subred LAN, puerta de enlace directa, red de invitados) coincidirá con esta regla.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: si se selecciona, el tráfico de dispositivos específicos (identificados por la dirección MAC) coincidirá con esta regla.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: si se selecciona, el tráfico de dispositivos específicos (identificados por la dirección MAC) no coincidirá con esta regla.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Seleccione el destino de destino y luego haga clic en **Apply**.

    Hay tres opciones:

    - **All Targets**: si se selecciona, el tráfico que coincida con esta regla se enrutará a todos los destinos.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: si se selecciona, el tráfico que coincida con esta regla se enrutará a dominios o direcciones IP específicos. Debe ingresarlos manualmente.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: si se selecciona, el tráfico que coincida con esta regla no se enrutará a dominios o direcciones IP específicos. Debe ingresarlos manualmente.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. Se agrega correctamente un túnel VPN. Se le dirigirá al **ExpressVPN Dashboard**. Agregue más túneles VPN si es necesario.

### Referencia de caso {#case-reference}

A continuación se muestran dos casos típicos de configuración de políticas VPN con instrucciones de configuración paso a paso para su referencia.

??? note "Caso 1: Enrutar solo los dispositivos especificados a través de la VPN."

    **Requisitos:**

    1. Solo dispositivos específicos conectados a este enrutador acceden a Internet a través de la VPN. Todos los demás dispositivos acceden a Internet a través de la WAN local.

    2. Los dispositivos seleccionados deben utilizar únicamente la conexión VPN. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet de estos dispositivos para evitar fugas de DNS y seguimiento de IP.

    **Pasos de configuración:**

    1. Seleccione el perfil VPN.

        Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario, luego haga clic en **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Seleccione la fuente del cliente.

        Haga clic en la pestaña **Specified Devices**, seleccione los dispositivos que desea usar la VPN y luego haga clic en **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Seleccione el destino de destino.

        Haga clic en la pestaña **All Targets**, configúrela como destino del tráfico y luego haga clic en **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

4. Se le dirigirá al Panel de ExpressVPN. Ahora se ha agregado exitosamente un túnel VPN.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Asegúrese de que el **Kill Switch** para este túnel esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet para el tráfico que coincida con este túnel para evitar fugas de DNS y seguimiento de IP.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Asegúrese de que **Allow Non-VPN Traffic** esté habilitado. Esto está habilitado de forma predeterminada para garantizar que el tráfico que no coincida con el túnel VPN aún pueda acceder a Internet a través de la red WAN local.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Haga clic en el botón central para activar este túnel.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluida la política de VPN, la IP virtual del cliente, la dirección del servidor, el puerto de escucha y las estadísticas de tráfico.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Ahora, sólo dos dispositivos específicos acceden a Internet a través de VPN. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet de estos dispositivos para evitar fugas de DNS y seguimiento de IP. En su lugar, todos los demás dispositivos accederán a Internet a través de la red WAN local.

??? note "Caso 2: Enrutar todos los dispositivos a través de la VPN 1 para sitios web específicos y el resto del tráfico a través de la VPN 2."

    **Requisitos:**

    1. Todos los dispositivos usan el Túnel VPN 1 al acceder a sitios web de redes sociales y servicios de transmisión específicos, y usan el Túnel VPN 2 para el resto del acceso a Internet.

    2. Si los túneles VPN se desconectan inesperadamente, se bloqueará el acceso a Internet de todos los dispositivos para evitar fugas de DNS y seguimiento de IP.

    **Pasos de configuración:**

    1. Seleccione el perfil VPN para el Túnel 1.

        Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario, luego haga clic en **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Seleccione la fuente del cliente.

        Haga clic en la pestaña **All Clients**, configúrela como fuente de cliente para el Túnel 1 y luego haga clic en **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Seleccione el destino de destino.

        Haga clic en la pestaña **Specified Domain / IP List**, ingrese dominios de redes sociales y servicios de transmisión específicos, como se muestra a continuación, luego haga clic en **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. Se le dirigirá al Panel de ExpressVPN. Ahora el túnel VPN 1 se ha agregado correctamente.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Asegúrese de que el **Kill Switch** para el túnel 1 esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet para el tráfico que coincida con este túnel para evitar fugas de DNS y seguimiento de IP.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Haga clic en **Add New Tunnel** para agregar el túnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Seleccione el perfil VPN para el Túnel 2.

        Seleccione uno o varios perfiles y ajuste su prioridad a la derecha según sea necesario, luego haga clic en **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

    8. Seleccione la fuente del cliente.

        Haga clic en la pestaña **All Clients**, configúrela como fuente de cliente para el Túnel 2 y luego haga clic en **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    9. Seleccione el destino de destino.

        Haga clic en la pestaña **All Targets**, configúrela como destino del tráfico para el Túnel 2 y luego haga clic en **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. Serás dirigido al Panel de VPN. Ahora el túnel VPN 2 se ha agregado correctamente.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Asegúrese de que **Kill Switch** para el túnel 2 esté habilitado. Si la VPN se desconecta inesperadamente, se bloqueará el acceso a Internet para el tráfico que coincida con este túnel para evitar fugas de DNS y seguimiento de IP.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Haga clic en el ícono de ajustes en la parte superior derecha, habilite **Enhanced Kill Switch** y luego haga clic en **Apply**. Esto garantiza que todo el tráfico sólo pueda llegar a Internet a través de VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        Una vez aplicado, **Enhanced Kill Switch** aparecerá en la parte superior de la página.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Haga clic en el botón central para activar el Túnel 1 y el Túnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Una vez conectado, la página mostrará los detalles de la conexión VPN, incluida la política de VPN, la IP virtual del cliente, la dirección del servidor, el puerto de escucha y las estadísticas de tráfico.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Ahora, todos los dispositivos usarán **VPN Tunnel 1** al acceder a dominios específicos y usarán **VPN Tunnel 2** para todo el acceso restante a Internet. Si los túneles VPN se desconectan inesperadamente, se bloqueará el acceso a Internet de todos los dispositivos para evitar fugas de DNS y seguimiento de IP.

## Kill Switch

Kill Switch es una característica de seguridad para conexiones VPN. Corta automáticamente todo el acceso a Internet para su red local si la conexión VPN se cae inesperadamente, evitando que su dirección IP real y sus datos en línea queden expuestos y garantizando privacidad y seguridad continuas. Esta función es particularmente útil para mantener un acceso a Internet seguro y anónimo, como cuando se utilizan redes públicas, se procesan datos confidenciales o se oculta su dirección IP real.

Cuando está habilitado, bloquea cualquier tráfico de cliente que intente evitar el túnel VPN, deteniendo efectivamente las fugas de VPN causadas por problemas de configuración de DNS, desconexiones inesperadas, solicitudes de IP directas y otros escenarios similares.

Fortify admite la configuración Kill Switch para la conexión VPN global, así como para cada túnel VPN individual.

- Para configurar Kill Switch para la conexión VPN global (es decir, Enhanced Kill Switch), consulte [All Other Traffic](#all-other-traffic).

- Para configurar Kill Switch para cada túnel VPN individual, consulte [Opciones de túnel](#tunnel-options).

## All Other Traffic

Haga clic en el ícono de ajustes en la esquina superior derecha para configurar la política para el tráfico que no coincide con el túnel VPN.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Esta política controla si el tráfico que no coincide con ninguno de sus grupos de túneles VPN puede acceder a Internet o no. Dos opciones disponibles: **Allow Non-VPN Traffic** y **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: habilitado de forma predeterminada para garantizar el acceso normal a Internet para el tráfico que no es VPN.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Obliga a todos los dispositivos a acceder a Internet a través de una VPN. Se bloqueará cualquier tráfico que no coincida con un túnel VPN. Esta configuración global no anula el Kill Switch configurado para túneles VPN individuales.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Opciones de túnel {#tunnel-options}

Puede configurar ajustes avanzados para cada túnel VPN, como VPN Kill Switch, IP Masquerading y MTU.

Haga clic en el ícono de ajustes en un grupo de túneles y seleccione **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: si está habilitado, el tráfico que coincida con este túnel VPN se bloqueará si la conexión VPN falla inesperadamente. Si está deshabilitado, dicho tráfico conmutará por error al túnel **All Other Traffic**.

- **Services from GL.iNet Use VPN**: si están habilitados, los servicios GoodCloud, DDNS y rtty transmitirán paquetes a través de túneles VPN. Esta opción está deshabilitada por defecto, ya que estos servicios normalmente requieren la dirección IP real del dispositivo para funcionar correctamente.

- **Allow Remote Access to the LAN Subnet**: Si está habilitado, se permitirá el acceso remoto a este enrutador y sus dispositivos LAN a través de la VPN. Requiere que el servidor VPN anuncie una ruta de regreso a su subred LAN.

- **IP Masquerading**: si está habilitado, las direcciones IP de origen de los clientes LAN se reescribirán en la IP del túnel VPN del enrutador. Desactive esto solo para configuraciones de sitio a sitio donde el par remoto conoce sus subredes LAN.

- **MTU**: el valor de MTU que establezca para el túnel anulará la configuración de MTU en el archivo de configuración.

## Prioridad del túnel

Para ajustar la prioridad del túnel, haga clic en el ícono de ajustes en un grupo de túneles y seleccione **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Haga clic y mantenga presionado el ícono de tres líneas a la derecha para reordenar los túneles, luego haga clic en **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router routes traffic according to the following rules**:

1. El tráfico primero intentará coincidir con la regla del túnel de mayor prioridad. Si coincide, será encaminado a través de ese túnel; de lo contrario, intentará el siguiente túnel de prioridad, y así sucesivamente.

2. Cada grupo de túneles opera de forma independiente. Una vez que el tráfico coincida con una regla de túnel, se enrutará a través de ese túnel y no realizará conmutación por error entre grupos de túneles.

3. Se pueden seleccionar varios perfiles dentro de cada grupo de túneles para permitir la conmutación por error dentro del túnel. Cuando el perfil de mayor prioridad en un grupo de túneles deja de funcionar, el túnel se conectará automáticamente utilizando el segundo perfil de mayor prioridad, y así sucesivamente.

4. Si un túnel VPN se desconecta inesperadamente, el sistema determinará si se debe realizar una conmutación por error del tráfico al túnel All Other Traffic en función de si el **Kill Switch** de este túnel está habilitado.

    - Si el Kill Switch está habilitado, el tráfico se bloqueará y no pasará por error al túnel para All Other Traffic.
    - Si el Kill Switch está desactivado, el tráfico pasará por error al túnel para All Other Traffic.

5. En el túnel **All Other Traffic**, diferentes modos determinan si el tráfico que no coincide con el túnel VPN puede acceder a Internet.

    - **Allow Non-VPN Traffic**: está habilitado de forma predeterminada para garantizar que el tráfico que no coincida con los túneles VPN aún pueda acceder a Internet a través de la WAN local.

    - **Enhanced Kill Switch**: Obliga a todos los dispositivos a acceder a Internet a través de una VPN. Se bloqueará cualquier tráfico que no coincida con un túnel VPN. Esta configuración global no anula el Kill Switch configurado para túneles VPN individuales. En resumen, fortalece el Kill Switch y bloquea el acceso regular a Internet para evitar fugas de IP.

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
