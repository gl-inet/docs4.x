# Cómo configurar Urban Shield VPN en un router GL.iNet

[Urban Shield VPN](https://urbanshieldvpn.com/) es un proveedor de VPN dedicado a ofrecer soluciones VPN de alta seguridad y alto rendimiento a usuarios de todo el mundo. Proporciona routers VPN GL.iNet preconfigurados y planes de suscripción flexibles para garantizar una navegación segura y privada. Solo tiene que activar Urban Shield VPN en su router para obtener acceso protegido a sus servidores globales y navegar o hacer streaming con tranquilidad.

## Guía de configuración

A continuación se usa un GL-B3000 como ejemplo para activar Urban Shield VPN configurándolo como WireGuard Client.

### 1. Registrar una cuenta de Urban Shield VPN

Visite el [sitio web oficial de Urban Shield VPN](https://urbanshieldvpn.com/){class="\_blank"} o haga clic [aquí](https://payment.urbanshieldvpn.com/sign-up) para registrar una cuenta de Urban Shield VPN.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Encender y conectar

Encienda el router. Conecte un dispositivo al router mediante un cable Ethernet o por Wi-Fi.

### 3. Acceder al panel de administración web

Siga los pasos siguientes para acceder al panel de administración web. Si ya ha iniciado sesión, vaya a la [siguiente parte](#4-network-setup).

Abra un navegador web, se recomienda Chrome, Edge o Safari, y visite [192.168.8.1](http://192.168.8.1){target="\_blank"}. Se le dirigirá a la configuración inicial del panel de administración web, como se muestra a continuación. Configure la contraseña de administrador y haga clic en **Next** para continuar.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Configure la red Wi-Fi. La página muestra los datos Wi-Fi de fábrica, incluidos el nombre de Wi-Fi, SSID, y la contraseña, que puede cambiar o mantener. Si cambia cualquier dato del Wi-Fi, vuelva a conectar su dispositivo a la red Wi-Fi actualizada.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Después, haga clic en **Next** para iniciar sesión con la contraseña de administrador.

### 4. Configuración de red

Hay un **Network Setup Wizard** en la esquina superior derecha, disponible en firmware v4.7 y superiores. Siga el asistente para configurar el acceso a Internet del router antes de configurar la VPN.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Activar Urban Shield VPN

Seleccione **VPN** en el menú izquierdo -> **WireGuard Client**. Verá una página integrada de inicio de sesión de Urban Shield VPN.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Introduzca su **Email** y **Password**, y luego haga clic en **Save And Continue**. El sistema generará archivos de configuración para cada servidor.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Seleccione el servidor que prefiera y haga clic en **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Los servidores disponibles aparecerán en la lista.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Haga clic en el icono de tres puntos para iniciar la conexión.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Una vez conectado, aparecerá un punto azul para indicar que la conexión se ha realizado correctamente.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

También puede comprobar el estado de la conexión en el VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Editar la información de la cuenta o cerrar sesión

Haga clic en el icono de engranaje para editar la información de la cuenta o cerrar sesión.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Renovar

Si hace clic en **Go Renew**, irá al sitio web oficial para renovar la suscripción.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Eliminar

Puede eliminar todos los archivos de configuración con un solo clic, así como la clave privada y la clave pública.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
