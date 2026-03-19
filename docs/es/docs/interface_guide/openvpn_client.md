# Configurar el cliente OpenVPN en routers GL.iNet

OpenVPN es un protocolo VPN de código abierto que utiliza técnicas de red privada virtual para establecer conexiones seguras de sitio a sitio o de punto a punto.

Para configurar el cliente OpenVPN en un router GL.iNet, vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Antes de empezar, asegúrese de tener una suscripción activa con un proveedor de servicios VPN que admita la configuración manual de OpenVPN. Haga clic [aquí](https://www.gl-inet.com/solutions/vpn/){target="\_blank"} para consultar los proveedores OpenVPN compatibles con GL.iNet.

Por lo general, primero debe visitar el sitio web oficial del proveedor de servicios VPN al que está suscrito, obtener el archivo de configuración y subirlo al router para configurarlo como cliente OpenVPN. Si no sabe cómo obtener el archivo de configuración, consulte [este enlace](#obtener-archivos-de-configuración-de-proveedores-de-servicios-openvpn) o póngase en contacto con su soporte.

Puede configurar un cliente OpenVPN mediante el panel de administración web o la [aplicación móvil](../faq/mobile_app.md). A continuación se describen los pasos para configurarlo a través del panel de administración web.

---

En el panel de administración web, vaya a **VPN** -> **OpenVPN Client**.

Si tiene una suscripción a NordVPN, haga clic en **NordVPN** para iniciar sesión; de lo contrario, haga clic en **Add Manually** para subir los archivos de configuración de OpenVPN.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Configurar NordVPN

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="\_blank"} es un servicio VPN en línea popular por su velocidad y seguridad.

La configuración rápida de NordVPN está integrada en el panel de administración de los routers GL.iNet. Puede obtener en línea los archivos de configuración de todos los servidores NordVPN introduciendo las credenciales de su cuenta, obtenidas desde el panel de NordVPN, en el panel de administración web del router o en la aplicación móvil, lo que elimina la necesidad de subir archivos manualmente.

1. Inicie sesión en su cuenta web de NordVPN [aquí](https://my.nordaccount.com/){target="\_blank"}.

   ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

   Después de iniciar sesión, en el panel de Nord, haga clic en **NordVPN** y luego en **Set up NordVPN manually**.

   ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

   ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

   Encontrará las **service credentials**. Cópielas para usarlas más adelante.

   ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Inicie sesión en el panel de administración web del router, vaya a VPN -> OpenVPN Client -> NordVPN. Introduzca las **service credentials** obtenidas en el paso 1. Nota: **NO** son el correo electrónico ni la contraseña de su cuenta de inicio de sesión. Después, haga clic en **Save and Continue**.

   ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Seleccione el protocolo, el número máximo de servidores de cada ubicación y las ubicaciones, y haga clic en **Apply**.

   ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

   Se descargarán los archivos de configuración.

   ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Inicie una conexión.

   Seleccione el servidor que prefiera y haga clic en el icono de tres puntos de la derecha para iniciar la conexión.

   ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Actualizar servidores.

   Puede hacer clic en **Update Servers** para obtener la lista más reciente de servidores disponibles y evitar fallos de conexión causados por mantenimiento o cierre de servidores.

   ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Editar credenciales.

   Haga clic en el icono de engranaje para editar sus credenciales de inicio de sesión.

   ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Eliminar todos los archivos.

   Puede hacer clic en **Delete All** para eliminar todos los archivos de configuración con un solo clic.

   ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Configurar manualmente el cliente OpenVPN (para otros proveedores)

Si su proveedor de servicios OpenVPN no está integrado en nuestro panel de administración, visite primero el sitio web oficial del proveedor al que está suscrito para obtener el archivo de configuración. Después, súbalo al router para configurar un cliente OpenVPN.

En los pasos siguientes, usaremos [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="\_blank"} como ejemplo.

1. Descargue un archivo de configuración desde el sitio web oficial de Private Internet Access.

2. Inicie sesión en el panel de administración web del router, vaya a VPN -> OpenVPN Client y haga clic en **Add Manually**.

   ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. Se creará un grupo en la barra lateral izquierda.

   ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Asigne un nombre descriptivo al grupo, por ejemplo, private internet access.

   ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Suba su archivo de configuración de OpenVPN. Introduzca las credenciales si se requieren y haga clic en **Apply**.

   ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}
   - Hay 4 tipos de credenciales para la autenticación:
     1. Sin autenticación.
     2. Solo nombre de usuario y contraseña.
     3. Solo frase de contraseña.

     4. Nombre de usuario, contraseña y frase de contraseña.

   Después verá el archivo de configuración cargado.

   ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Haga clic en el icono de tres puntos de la derecha para iniciar una conexión.

   ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Una vez conectado, aparecerá un punto verde junto al archivo de configuración.

   ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

   Y los detalles de la conexión VPN se mostrarán en el **VPN Dashboard**.

   ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## Configurar el servidor OpenVPN en un router GL.iNet

Si tiene dos routers GL.iNet, puede considerar configurar uno como servidor OpenVPN, para lo que se requiere una IP pública, y el otro como cliente OpenVPN. De este modo, puede establecer su propia conexión VPN sin suscribirse a servicios VPN de terceros.

Para configurar el servidor OpenVPN, consulte [aquí](openvpn_server.md).

## Obtener archivos de configuración de proveedores de servicios OpenVPN

Hemos probado más de 30 proveedores de servicios OpenVPN y documentado los pasos para obtener los archivos de configuración. Si no está seguro de cómo obtener el archivo de configuración, consulte los pasos que se indican a continuación.

Si el proveedor de servicios al que está suscrito no aparece en la lista siguiente, póngase en contacto con su soporte para obtener ayuda adicional.

??? "NordVPN" ### NordVPN

    [Official Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Inicie sesión en su cuenta de NordVPN**

        Inicie sesión en el [sitio web oficial](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} y vaya al panel de cuenta de Nord, donde encontrará las service credentials.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Después de iniciar sesión en el panel de Nord, haga clic en NordVPN en el lado izquierdo y luego en **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Busque las **Service credentials**. Cópielas por si necesita usarlas al subir configuraciones.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Elija un servidor NordVPN y descargue el archivo de configuración**

        Vaya a la pestaña **Server recommendation**. Le recomendará un servidor según su red y le ofrecerá protocolos disponibles para descargar. Haga clic en **Get setup configuration** para continuar.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        En la ventana emergente, seleccione el protocolo **OpenVPN** y descargue la configuración UDP o TCP.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Puede descargar aquí todas las configuraciones de servidores: [aquí](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

    [Refer link](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    También puede usar la [aplicación móvil](../faq/mobile_app.md) para configurar NordVPN.

??? "AirVPN" ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Inicie sesión en su cuenta de AirVPN.

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Elija Config Generator en el lado izquierdo y luego seleccione Linux como sistema operativo. A continuación, elija el servidor que prefiera.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Verá la página de descarga del archivo de configuración.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill" ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Información citada de la [instrucción oficial de Astrill](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Genere y descargue el archivo ZIP de configuración OpenVPN de Astrill.

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Escriba una descripción, por ejemplo OPENVPN_GUI.

    3. Haga clic en el botón ADD to my certificates.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Cuando se haya añadido el certificado OpenVPN, haga clic en el botón Download.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN" ### BolehVPN

    [Official Website](https://www.bolehvpn.net/){target="_blank"}

    Inicie sesión en el [Dashboard](https://users.bolehvpn.net/){target="_blank"}, descargue sus archivos de configuración y seleccione el formato [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Extraiga los archivos zip después de completar la descarga.

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

    [Refer link](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN" ### CactusVPN

    [Official Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Descargue](https://www.cactusvpn.com/downloads/){target="_blank"} directamente.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm" ### Cryptostorm

    [Official Website](https://cryptostorm.is/){target="_blank"}

    [Descargue](https://cryptostorm.is/configs/ecc/){target="_blank"} directamente.

??? "CyberGhost" ### CyberGhost

    [Official Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Información citada de la [instrucción oficial de CyberGhost](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Inicie sesión en su cuenta en línea de CyberGhost VPN.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Seleccione "**VPN**" en el menú izquierdo, luego haga clic en "**Configure Device**" y cree la configuración del servidor como se describe a continuación:

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Ahora cree la configuración del servidor como se describe a continuación:

        * **Protocol** : **OpenVPN**
        * **Country** : Como las conexiones de protocolo nativo solo pueden usarse con exactamente un servidor, ahora debe elegir el país desde el que desea navegar; CyberGhost elegirá automáticamente el servidor concreto de ese país.
        * **Server group** : Elija el grupo de servidores y el protocolo OpenVPN, UDP o TCP, que desea usar.

        **OpenVPN UDP** permite más velocidad que la versión TCP, pero en algunos casos puede provocar descargas interrumpidas. Esta es la configuración predeterminada.

        **OpenVPN TCP** permite conexiones más estables que la versión UDP, pero es un poco más lento. Elija esta versión si tiene problemas recurrentes de conexión, como desconexiones repentinas.

        Una vez elegidos los parámetros deseados, guárdelos con **Save Configuration**.

    4. Para ver las credenciales de **OpenVPN** generadas para usted en el panel de configuración, pulse **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Después de configurar sus preferencias de conexión, tenga en cuenta lo siguiente:

        * **Server Group** : Es la dirección del país, es decir, del servidor, al que desea conectarse, por ejemplo, '12345-1-ca.cg-dialup.net'. Esta dirección cambia con cada país que haya elegido en el paso anterior. El servidor concreto que se usará será elegido automáticamente por CyberGhost.
        * **Username** : Es un nombre de usuario generado exclusivamente para este protocolo. **NO** es el nombre de usuario habitual de su cuenta CyberGhost; se usa únicamente para autenticarse en los servidores de CyberGhost mediante configuraciones manuales. Lo necesitará al configurar OpenVPN en routers GL.iNet.
        * **Password** : Es una contraseña generada exclusivamente para el uso de este protocolo. **NO** es la contraseña habitual de su cuenta CyberGhost; se usa únicamente para autenticarse en los servidores de CyberGhost mediante configuraciones manuales. La necesitará al configurar OpenVPN en routers GL.iNet.

        Una vez hecho esto, descargue el archivo de configuración. Para ello, haga clic en *Download Configuration* y descárguelo en su ordenador.

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN" ### ExpressVPN

    [Official Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Información citada de la [instrucción oficial de ExpressVPN](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Vaya al sitio web de [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} e inicie sesión con sus credenciales de ExpressVPN.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Introduzca el código de verificación** que se envía a su correo electrónico.

    2. En la sección "Set up your devices", haga clic en **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Haga clic en **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Verá su **username**, **password** y una lista de **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Haga clic en la ubicación o ubicaciones que desee para descargar los archivos .ovpn.

        **Mantenga abierta esta ventana del navegador**. Necesitará esta información para la configuración posterior.

    [Refer link](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN" ### FastestVPN

    [Official Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Descargue el archivo zip de configuraciones FastestVPN para OpenVPN TCP y UDP [aquí](https://support.fastestvpn.com/download/fastestvpn_ovpn/).

    Consejo: si el archivo zip es demasiado grande para subirlo, elimine algunos archivos .ovpn de la carpeta .zip o suba un solo archivo .ovpn.

    [Refer link](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN" ### FinchVPN

    [Official Website](https://www.finchvpn.com/){target="_blank"}

    1. Inicie sesión en su cuenta de FinchVPN.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Vaya a la página Download y haga clic en Download en FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Elija Linux.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Elija el protocolo según su preferencia. Por lo general, puede elegir la primera opción, **Port 8484 over UDP**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Recuerde marcar la casilla para incluir su nombre de usuario y contraseña antes de descargar el archivo.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN" ### HideIPVPN

    [Official Website](https://www.hideipvpn.com/){target="_blank"}

    1. Inicie sesión en su cuenta de HideIPVPN.

    2. Vaya a Package en el lado izquierdo, haga clic en su paquete y asegúrese de que esté activo.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. En la pestaña VPN encontrará los detalles de inicio de sesión VPN, nombre de usuario y contraseña; esos son los datos de inicio de sesión para la conexión OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Desplácese hacia abajo para descargar los archivos de configuración de OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN" ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Inicie sesión en su cuenta de Hide.me y busque Server Locations en el lado izquierdo.

    2. Descargue la configuración OpenVPN para Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield" ### Hotspot Shield

    [Official Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Nota: Los archivos de configuración Router de Hotspot Shield ya no están disponibles ni son compatibles. Los pasos siguientes se incluyen únicamente por motivos de compatibilidad heredada para quienes todavía tengan esos archivos instalados.**

    1. Vaya a [https://www.hotspotshield.com/](https://www.hotspotshield.com/) y haga clic en Account. Inicie sesión si se le solicita.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Go to [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)

        Vaya al menú desplegable Select location y elija la ubicación virtual que usará el router. Ahora haga clic en "Download file". El archivo de configuración, config.ovpn, se descargará en su ordenador. Deberá introducir el nombre de usuario y la contraseña al configurar el cliente OpenVPN en el router.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Refer link](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH" ### IPVANISH

    [Official Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Puede descargar todos los archivos de configuración de todos los servidores [aquí](https://configs.ipvanish.com/configs/configs.zip). Contiene todos los archivos de configuración del servidor, .ovpn, y un archivo de certificado, .crt. El archivo .zip puede ser un poco grande para algunos modelos; elimine la configuración .ovpn del servidor que no vaya a utilizar.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - También puede descargar archivos de configuración de servidores individuales [aquí](https://www.ipvanish.com/software/configs/), pero también tendrá que descargar **ca.ipvanish.com.crt**. Antes de subirlos al router, debe comprimir **ca.ipvanish.com.crt** y los archivos de configuración .ovpn en un archivo .zip.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Refer link](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY" ### IVACY

    [Official Website](https://billing.ivacy.com/page/22852){target="_blank"}

    Para configurar un cliente OpenVPN con Ivacy, necesitará lo siguiente:

    - Su nombre de usuario para la configuración manual de OpenVPN, que se muestra en la indicación "Download Configuration"
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Su contraseña, la misma que utilizó para iniciar sesión en su cuenta de Ivacy.
    - Un archivo de configuración OpenVPN.

    [Refer link](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN" ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    1. Descargue los [archivos de configuración OpenVPN](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Busque el ID de la cuenta en [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Al arrastrar el archivo de configuración a Add a New OpenVPN Configuration, se le pedirá que introduzca User Name y Password. El User Name es el ID de su cuenta, que comienza con las letras **ivpn**. La contraseña puede ser cualquiera, por ejemplo, **ivpn**.

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Refer link](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad" ### Mullvad

    [Official Website](https://mullvad.net/en){target="_blank"}

    1. Vaya al sitio web de [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} e inicie sesión con sus credenciales de Mullvad.

    2. Elija OpenVPN Configuration.

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Elija **Linux** y seleccione la ubicación del servidor.

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN" ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Solo tiene que iniciar sesión; después podrá obtener fácilmente el archivo de configuración de OpenVPN haciendo clic en el menú de abajo.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Elija el servidor y descárguelo.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    El nombre de usuario y la contraseña son los mismos que usa para iniciar sesión en OVPN.

??? "OysterVPN" ### OysterVPN

    [Official Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Acceda a [la página de lista de servidores de OysterVPN](https://support.oystervpn.com/server-list/){target="_blank"} y haga clic en **Download .ovpn file** para descargar el archivo de configuración.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. El nombre de usuario y la contraseña para la conexión OpenVPN son los mismos que utiliza para iniciar sesión en OysterVPN.

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

??? "PIA (Private Internet Access)" ### PIA

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Descargue](https://www.privateinternetaccess.com/openvpn/openvpn.zip) directamente.

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

??? "PrivadoVPN" ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Solo tiene que iniciar sesión; después podrá encontrar fácilmente **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

??? "PrivateVPN" ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Descargue](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank} directamente.

    [Aquí](https://privatevpn.com/client/PrivateVPN-TUN.zip) está el enlace oficial de descarga. Debido a un error encontrado al importar el archivo en el router, el nombre del archivo interno contiene caracteres especiales, como 'Bogotá'. Lo hemos renombrado y proporcionado el enlace de descarga anterior. Corregiremos este error en futuras versiones.

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

??? "Proton VPN" ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN dispone de servicio WireGuard; recomendamos usar WireGuard. Consúltelo [aquí](wireguard_client.md#wireguard-providers)**.

    1. Inicie sesión en su cuenta de [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}.

    2. Haga clic en **Download** en el lado izquierdo.

    3. Elija la plataforma Router, el protocolo, etc., y busque el país de destino para descargar el archivo de configuración.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. La credencial para conectarse mediante OpenVPN no es la misma que usa para iniciar sesión en el panel del sitio web de Proton. Puede encontrar la credencial en **Account -> OpenVPN/IKEv2 username**.

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN" ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Para configurar un cliente OpenVPN con PureVPN, necesitará su nombre de usuario y contraseña de OpenVPN, así como un archivo de configuración, que puede encontrar en su cuenta de PureVPN.

    1. [Sign in to your PureVPN account.](https://my.purevpn.com/)
    2. From the left sidebar, click **Subscriptions**.
    3. Scroll down to find your OpenVPN username and password.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. From the left sidebar, click **Manual Configuration**.
    5. Seleccione una ubicación VPN y haga clic en **Download** para descargar el archivo de configuración.

    [Refer link](https://support.purevpn.com/openvpn-files)

    Los routers GL.iNet no admiten la función [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} de PureVPN porque requiere PPTP.

??? "SaferVPN" ### SaferVPN

    [Official Website](https://safervpn.com/?a_aid=563){target="_blank"}

    [Descargue](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) directamente.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN" ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN dispone de servicio WireGuard; recomendamos usar WireGuard. Consúltelo [aquí](wireguard_client.md#starvpn).

    1. **Registre una cuenta en StarVPN**

        Diríjase a sus opciones de [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} y elija un plan VPN que se ajuste a sus necesidades. Puede registrarse en el proceso de compra o directamente [aquí](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. Información de inicio de sesión VPN

        Inicie sesión en el [dashboard](https://www.starvpn.com/dashboard){target="_blank"} del área de miembros de StarVPN. Puede encontrar su nombre de usuario y contraseña VPN para cada slot en la sección Manage Slots o en el área del dashboard.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        En el caso de varios slots, los ajustes y las credenciales de configuración VPN se encuentran en la sección “Manage Slots”.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. Descargar el archivo de configuración OpenVPN

        En el siguiente paso, debe descargar los archivos de configuración del servidor VPN necesarios para que el software OpenVPN sepa dónde conectarse. Descargue el archivo de configuración desde el dashboard del área de miembros.

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        Algunos routers GL.iNet no admiten IPv6 o DNS Leak Protection, por lo que puede experimentar un error de IP o de conexión. Edite el archivo de configuración ovpn y desactive IPv6 realizando estas sencillas tareas.

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}


??? "StreamVPN" ### StreamVPN

    [Official Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Inicie sesión con su cuenta de [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} y entonces podrá ver la información de su suscripción. Haga clic en **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Haga clic en **VPN Router** y se descargará un archivo .zip llamado `StreamVPN.zip`.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Nota:** Solo funciona el archivo de configuración cuyo nombre contiene "Primary".

??? "StrongVPN" ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Inicie sesión con su cuenta de [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} y verá el resumen VPN Accounts Summary. Haga clic en **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Busque la sección Manual setup y siga los pasos para obtener la configuración.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark" ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Busque sus datos de inicio de sesión**

        Las service credentials de Surfshark son diferentes de las credenciales de su cuenta de Surfshark, es decir, de su correo electrónico y su contraseña. Necesitará las service credentials de Surfshark para conectarse a la VPN mediante el método manual de configuración OpenVPN en el router.

        Inicie sesión en el [sitio web oficial](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} y vaya a [esta página](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, donde encontrará todos los datos necesarios para una conexión manual.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Elija un servidor de Surfshark**

        Seleccione la pestaña **Locations**, donde verá todos los servidores de Surfshark.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Se le pedirá que elija TCP o UDP. Haga clic [aquí](../faq/openvpn_tcp_udp.md) para ver la diferencia.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Puede descargar todas las configuraciones [aquí](https://api.surfshark.com/v1/server/configurations) directamente.

    Consejo: si el archivo zip es demasiado grande para subirlo, puede eliminar algunos archivos .ovpn del .zip o subir un solo archivo .ovpn.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC" ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate" ### VPNGate

    [Official Website](https://www.vpngate.net/en/){target="_blank"}

    Los archivos de configuración OpenVPN aparecen en el [sitio web de VPN Gate](https://www.vpngate.net/en/) según la ubicación del servidor.

    1. Haga clic en OpenVPN Config file en la columna **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Verá la página de descarga.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)" ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Información citada de la [instrucción oficial de VPN Unlimited](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Empiece iniciando sesión en su User Office, pulse Manage para el servicio VPN Unlimited y siga unos sencillos pasos:

    1. Seleccione un dispositivo.

        Elija un dispositivo de la lista o cree uno nuevo. Si se ha quedado sin slots libres, elimine un dispositivo antiguo o compre slots adicionales.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Elija la ubicación del servidor deseada.

        VPN Unlimited ofrece una gran variedad de servidores, más de 400 en más de 70 ubicaciones. En este caso, elijamos Alemania.

    3. Seleccione el protocolo VPN.

        Seleccione el protocolo OpenVPN.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Cree una configuración.

        Pulse Generate y obtendrá todos los datos necesarios para configurar una conexión VPN.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN" ### VyprVPN

    VyprVPN ofrece los archivos OpenVPN aquí: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    El archivo zip proporcionado contiene dos carpetas con los archivos .ovpn: una llamada OpenVPN160 y otra OpenVPN256. Simplemente elimine la carpeta OpenVPN160 del archivo zip y luego súbalo al router GL.iNet como de costumbre.

??? "Windscribe" ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Inicie sesión en su cuenta de Windscribe [aquí](https://windscribe.com/login?auth_required){target="_blank"} y después acceda a [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Seleccione la ubicación del servidor, el protocolo, UDP o TCP, el puerto, por ejemplo, 1194, y la versión de OpenVPN que desea usar, preferiblemente la más reciente, y haga clic en **Download Config**. A continuación, se descargará en su dispositivo local un archivo con el sufijo ".ovpn".

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Haga clic en el botón **Get Credentials** de la misma página. Recibirá las credenciales correspondientes, que se utilizarán posteriormente en el panel de administración web del router al subir el archivo de configuración al router para la autenticación. Copie las credenciales o mantenga abierta esta página web.

    4. Después, siga [esta guía](../interface_guide/openvpn_client.md#configurar-manualmente-el-cliente-openvpn-para-otros-proveedores) para continuar.

??? "ZoogVPN" ### ZoogVPN

    [Official Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Inicie sesión en su [sitio web oficial](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"} y después acceda a la [página de archivos de configuración de OpenVPN](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}; allí encontrará todos los servidores. Descargue el archivo de configuración en la columna TCP o en la columna UDP.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Después, siga la [guía para configurar el cliente OpenVPN en un router GL.iNet](#configurar-el-cliente-openvpn-en-routers-glinet); el nombre de usuario y la contraseña son los mismos que utiliza para iniciar sesión en el sitio web de ZoogVPN.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
