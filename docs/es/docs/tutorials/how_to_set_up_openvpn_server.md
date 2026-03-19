# Cómo configurar un servidor OpenVPN en los routers GL.iNet

Este tutorial le mostrará cómo configurar un servidor OpenVPN en los routers GL.iNet. Un servidor VPN le permite establecer de forma remota una conexión segura con su red doméstica o de oficina. Con un router GL.iNet, puede configurar un servidor OpenVPN en unos pocos minutos.

!!! note "Antes de comenzar, asegúrese de cumplir los siguientes requisitos"

    **Dirección IP pública**

    Configurar un servidor OpenVPN requiere una dirección IP pública. Para comprobar si dispone de ella, consulte [este enlace](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Port forwarding**

    Si su router GL.iNet está conectado detrás de un router principal, [configure port forwarding en el router principal](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Inicie sesión en el router

Abra un navegador web y acceda al panel de administración web del router, IP predeterminada: 192.168.8.1. Inicie sesión con su contraseña de administrador.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Habilite Dynamic DNS, opcional

Configurar un servidor OpenVPN suele requerir una **dirección IP pública estática**, que proporciona un extremo fijo para que otros dispositivos accedan a su servidor VPN.

Sin embargo, si no dispone de una dirección IP pública estática, por ejemplo porque tiene una dirección dinámica, es posible que necesite habilitar **Dynamic DNS (DDNS)** en su router GL.iNet. Esto permite mantener la conectividad con el servidor OpenVPN incluso cuando su dirección IP pública cambia dinámicamente.

Siga los pasos siguientes para habilitar Dynamic DNS.

1. En el panel de administración web del router, vaya a **APPLICATIONS** > **Dynamic DNS**.
   ![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Active **Enable DDNS**, lea y acepte los **Terms of Service & Privacy Policy**, y luego haga clic en **Apply**.
   ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Descargar el archivo de configuración

1. En el panel de administración web del router, vaya a **VPN** > **OpenVPN Server**.
2. Haga clic en **Generate Configuration**.
3. Mantenga la configuración predeterminada tal como está y haga clic en **Export Client Configuration**.
   ![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. En la ventana emergente, active **Use DDNS Domain** si ya configuró **Dynamic DNS** anteriormente.
5. Haga clic en **Download** y guarde el archivo.
6. En la parte superior de la página **OpenVPN Server**, haga clic en **Start**.
   ![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "Opcional: para acceder a la red local del servidor VPN, habilite esta configuración:"

    Para firmware v4.7 y anteriores:

    1. En la barra lateral izquierda, haga clic en **VPN** > **VPN Dashboard**.
    2. Haga clic en el icono Options.
    3. Active **Remote Access LAN**.
    4. Haga clic en **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Para firmware v4.8 y posteriores:

    1. En la barra lateral izquierda, haga clic en **VPN** > **OpenVPN Server**.
    2. Haga clic en **Options** en la esquina superior derecha.
    3. Active **Allow Remote Access the LAN Subnet**.
    4. Haga clic en **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

## 4. Conectarse al servidor OpenVPN

Para conectarse al servidor OpenVPN, necesitará un cliente OpenVPN. Puede configurarlo mediante uno de los siguientes métodos:

??? "Método 1: una app cliente OpenVPN de terceros, use este método si no dispone de otro router compatible con cliente OpenVPN"

    En este tutorial usaremos como ejemplo la app OpenVPN Connect, la aplicación oficial desarrollada por OpenVPN Inc.

    1. En otro dispositivo, conéctese a una red Wi-Fi distinta, o a la red celular si usa un dispositivo móvil.
    2. Envíe al dispositivo el archivo de configuración que descargó anteriormente, por ejemplo por correo electrónico, y descárguelo en ese dispositivo.
    3. Descargue OpenVPN Connect para el sistema operativo de su dispositivo:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. En la aplicación, lea los términos y condiciones y seleccione **Agree**.
    5. Seleccione **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Seleccione **Browse** y luego el archivo de configuración descargado anteriormente.
    7. Seleccione **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Seleccione **Connect** > **OK** > **Allow**.

    Verá la palabra "Connected" en la parte superior del perfil VPN.
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Método 2: un router compatible con la configuración de un cliente OpenVPN"

    Puede usar cualquier router que admita la configuración manual del cliente OpenVPN. En este tutorial usaremos como ejemplo el router de viaje de GL.iNet [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/).

    1. En otro dispositivo, conéctese a una red Wi-Fi distinta, o a la red celular si usa un dispositivo móvil.
    2. En la barra de direcciones de un navegador web, introduzca la URL del panel de administración de su router, por ejemplo 192.168.8.1.
    3. Introduzca la contraseña y haga clic en **Login**.
    4. En la barra lateral izquierda, haga clic en **VPN** > **OpenVPN Client**.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Haga clic en **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Introduzca un nombre en el campo y haga clic en el icono de verificación.
    7. Suba el archivo de configuración que descargó anteriormente.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Haga clic en **Apply**.
    9. Haga clic en el icono de tres puntos y luego en **Start**.
    10. Conecte un dispositivo al router que ejecuta el cliente OpenVPN.

## 5. Verificar la conexión VPN

Abra un navegador web y busque su dirección IP y ubicación. Si coinciden con la IP y la ubicación del servidor VPN, en lugar de las de su proveedor de servicios de Internet, la conexión VPN se ha establecido correctamente.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
