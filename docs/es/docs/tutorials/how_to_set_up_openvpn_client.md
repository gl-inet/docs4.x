# Cómo configurar un cliente OpenVPN en routers GL.iNet

Este tutorial le mostrará cómo configurar un cliente OpenVPN en routers GL.iNet.

Vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Antes de empezar, asegúrese de tener una suscripción activa con un proveedor de servicios VPN que admita la configuración manual de OpenVPN. Haga clic [aquí](https://www.gl-inet.com/solutions/vpn/){target="\_blank"} para consultar los proveedores OpenVPN compatibles con GL.iNet.

A continuación se indican los pasos para configurar un cliente OpenVPN mediante el panel de administración web del router.

## 1. Inicie sesión en su router

Abra un navegador web y acceda al panel de administración web del router, con IP predeterminada `192.168.8.1`. Inicie sesión con su contraseña de administrador.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Configura el cliente VPN

Consulte la sección correspondiente al proveedor de servicio VPN que esté utilizando.

??? "NordVPN"

    1. En el panel de administración web del router, vaya a **VPN** > **OpenVPN Client**.

    2. Haga clic en **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Introduzca sus credenciales del servicio y haga clic en **Save and Continue**.

        Nota: NO es el correo electrónico ni la contraseña de la cuenta de inicio de sesión, sino las credenciales del servicio obtenidas en el sitio web de NordVPN -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. En el aviso, seleccione las ubicaciones VPN a las que desea conectarse y haga clic en **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Seleccione el servidor VPN al que desea conectarse, haga clic en el icono de tres puntos y luego en **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Otros proveedores de servicios VPN, por ejemplo Surfshark"

    1. En el panel de administración web del router, vaya a **VPN** > **OpenVPN Client**.

    2. Haga clic en **Add Manually**.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Defina un nombre. Puede introducir el nombre de su proveedor de servicio VPN y luego hacer clic en el icono de verificación.

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Asegúrese de haber descargado el archivo de configuración proporcionado por su proveedor de servicio VPN, así como las credenciales del servicio si las hubiera.
    5. Cargue el archivo de configuración que descargó.

        Introduzca las credenciales del servicio si es necesario y luego haga clic en **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Junto a la dirección del servidor VPN, haga clic en el icono de tres puntos y luego en **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Verifica la conexión VPN

Abra un navegador web y busque su dirección IP y su ubicación. Si coinciden con la IP del servidor VPN, en lugar de la IP de su proveedor de servicios de Internet, y con la ubicación del servidor VPN, la conexión VPN se ha establecido correctamente.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
