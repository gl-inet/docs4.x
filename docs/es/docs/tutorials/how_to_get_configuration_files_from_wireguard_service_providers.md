# Cómo obtener archivos de configuración de proveedores de servicios WireGuard

??? "AzireVPN"
    ### AzireVPN

    [Official Website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Acceda al [sitio web oficial de AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} e inicie sesión; después, abra el [generador de configuración de WireGuard](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. En la opción de IP, seleccione **IPv4**. Después haga clic en **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-azirevpn) para continuar.

    4. También puede usar la [mobile app](../faq/mobile_app.md) para configurar AzireVPN.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Official Website](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN ofrece una forma sencilla de usar su servicio WireGuard en un router GL.iNet.

    1. Conéctese al router por [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Copie la siguiente URL de instalación, péguela en el terminal y pulse Enter. Puede pegarla haciendo clic con el botón derecho del ratón.

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. Se iniciará la instalación y luego se le pedirá el nombre de usuario y la contraseña. Al escribir o pegar la contraseña, no verá ningún cambio en el terminal; pulse Enter después de introducirla.

    4. Cuando termine, vaya al panel de administración web y verá que se ha creado un grupo de hide.me VPN con archivos de configuración ya incluidos. Solo tiene que conectarse como lo haría con cualquier otro archivo de configuración.

    **Nota:** La clave del archivo de configuración de Hide.me VPN se regenera antes de cada conexión y deja de ser válida después de la desconexión, por lo que copiar este archivo de configuración a otros dispositivos no permitirá conectarse correctamente.

    [Refer link](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Official Website](https://mullvad.net/){target="_blank"}

    1. Acceda al [sitio web oficial de Mullvad](https://mullvad.net/){target="_blank"} e inicie sesión; después, abra el [generador de archivos de configuración de WireGuard](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Luego siga [esta guía](../interface_guide/wireguard_client.md/#set-up-mullvad) para continuar.

    3. También puede usar la [mobile app](../faq/mobile_app.md) para configurar Mullvad.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Official Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    No es posible descargar configuraciones WireGuard desde su sitio web. Use la [mobile app](../faq/mobile_app.md) para configurar PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Official Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Si utiliza [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, inicie sesión y vaya a [esta página](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}; haga clic en **Router** y seleccione **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. En la ventana siguiente, seleccione **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Seleccione **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Una vez generada la clave, seleccione **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Por último, elija la ubicación que desee configurar y pulse el botón **download** junto a esa ubicación. Podrá descargar los archivos de configuración.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-surfshark) para continuar.

    [Refer link](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Official Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Si utiliza [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, inicie sesión en su sitio web, vaya a [Client Area](https://airvpn.org/client/){target="_blank"} y haga clic en [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. En la página Config Generator, seleccione WireGuard en la sección de protocolos.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Seleccione un servidor, desplácese hasta el final y haga clic en el botón **Generate**. Se descargará el archivo de configuración.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "Astrill"
    ### Astrill

    [Official Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Si utiliza [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, inicie sesión y abra [esta página](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} para generar configuraciones WireGuard.

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "IVPN"
    ### IVPN

    [Official Website](https://www.ivpn.net/){target="_blank"}

    Si utiliza [IVPN](https://www.ivpn.net/){target="_blank"}, deberá generar manualmente la configuración de WireGuard. Siga la guía correspondiente a su sistema operativo.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "NVPN"
    ### NVPN

    [Official Website](https://www.nvpn.net/){target="_blank"}

    Siga la guía disponible [aquí](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} para crear la configuración.

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "OVPN"
    ### OVPN

    [Official Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Inicie sesión en [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} y localice el menú que se muestra a continuación para obtener los archivos de configuración de WireGuard.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Haga clic en **Generate WireGuard keys**, elija el servidor que desee y descargue la configuración.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Abra la configuración con un editor de texto y copie su contenido.

        La configuración puede incluir contenido IPv6. Como los routers GL.iNet no ofrecen un soporte suficientemente bueno para IPv6, elimine ese contenido. En el siguiente ejemplo, la parte resaltada corresponde al contenido IPv6.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

    5. También puede usar la [mobile app](../faq/mobile_app.md) para configurar OVPN.

??? "PrivateVPN"
    ### PrivateVPN

    [Official Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Inicie sesión y acceda al [Control panel](https://privatevpn.com/control-panel){target="_blank"}.

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Seleccione un servidor.

        ![select a server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Haga clic en **GENERATE CONFIG** y luego copie la configuración.

        ![generate config](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Official Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Acceda al sitio web de PrivadoVPN e inicie sesión.

    En el panel, busque la sección Manual Configuration, haga clic en WireGuard, seleccione el servidor al que desee conectarse y haga clic en Download Configuration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "Proton VPN"
    ### Proton VPN

    [Official Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Si utiliza [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, siga la guía disponible [aquí](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} para generar el archivo de configuración WireGuard.

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "PureVPN"
    ### PureVPN

    [Official Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Consulte [esta guía](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} o siga los pasos indicados a continuación para obtener manualmente el archivo de configuración de PureVPN.

    1. Inicie sesión con su cuenta en el [PureVPN Member Area](https://my.puremember.com/){target="_blank"}. Después de iniciar sesión, haga clic en **Manual Configuration** en el menú izquierdo.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Seleccione la ciudad de destino y haga clic en **Download** a la derecha.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. En la ventana emergente, seleccione **WireGuard** como protocolo.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Seleccione **Linux** como tipo de dispositivo y luego haga clic en **Generate Configuration**. El archivo de configuración se descargará en su dispositivo local.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para completar la configuración.

    [Refer link](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Official Website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Inicie sesión en [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) y busque la sección para obtener la configuración de su VPN. Siga los pasos para obtenerla.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Descargue la configuración de VPN.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "StarVPN"
    ### StarVPN

    [Official Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Registre una cuenta en StarVPN**

        Vaya a sus opciones de [pricing plan](https://www.starvpn.com/#pricing){target="_blank"} y elija un plan VPN que se ajuste a sus necesidades. Puede registrarse durante el proceso de compra o directamente [aquí](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Descargue la configuración WireGuard**

        Inicie sesión en el [dashboard](https://www.starvpn.com/dashboard){target="_blank"} del área de miembros de StarVPN. Haga clic en **WireGuard Config** para descargar el archivo de configuración. Cada slot contendrá un archivo de configuración WireGuard único.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Consejo**: Si desea usar las técnicas de ofuscación de AmneziaWG, haga clic en **AmneziaWG Config** para descargar el archivo de configuración. Cada slot contendrá un archivo de configuración AmneziaWG único.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Edite el archivo de configuración (opcional)**

        La configuración puede contener una dirección IPv6. Para evitar problemas de compatibilidad y conectividad, abra el archivo `.conf` y elimine la dirección IPv6, como se muestra a continuación.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. A continuación, siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para subir el archivo de configuración a su router GL.iNet.

    Referencias:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Official Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Si utiliza [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, inicie sesión en [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.

    2. Seleccione una ubicación en el menú desplegable, haga clic en **GENERATE** y abra el archivo de texto descargado.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

    4. También puede usar la [app móvil](../faq/mobile_app.md) para configurar StrongVPN.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Official Website](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Acceda a [https://trust.zone/setup](https://trust.zone/setup) e inicie sesión.

    2. Desplácese hasta la sección WireGuard, elija el puerto que desee y descargue la configuración de un servidor específico o un archivo zip con todas las configuraciones.

    3. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "VPN.AC"
    ### VPN.AC

    [Official Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Si utiliza [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, debe iniciar sesión en el panel de control y buscar WireGuard Manager en el menú "Services".

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Cree la configuración y descárguela.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Official Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Si utiliza [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, inicie sesión en su [User Office](https://my.keepsolid.com/){target="_blank"} > seleccione la aplicación VPN Unlimited® > haga clic en **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Pulse el campo situado bajo **Device** y haga clic en **Manually create a new device…** > establezca un nombre personalizado, por ejemplo WireGuard > elija la ubicación adecuada en **Server** > seleccione el protocolo **WireGuard**® en el menú desplegable > haga clic en **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/02.jpg){class="glboxshadow"}

    3. Los parámetros de configuración aparecerán a continuación en formato de texto.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/03.jpg){class="glboxshadow"}

        Combine la configuración como se muestra a continuación.

        <p>
        [Interface]</br>
        PrivateKey = <i>pegue la PrivateKey desde su User Office</i></br>
        ListenPort = <i>pegue los datos de ListenPort</i></br>
        Address = <i>pegue la información de Address</i></br>
        DNS = <i>pegue los datos de DNS desde su User Office</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>pegue la PublicKey desde su User Office</i></br>
        PresharedKey = <i>pegue los datos de PresharedKey</i></br>
        AllowedIPs = <i>pegue los datos de AllowedIPs</i></br>
        Endpoint = <i>pegue la información de Endpoint</i></br>
        </p>

    4. Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

    [Refer link 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Refer link 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Official Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Inicie sesión en su cuenta de miembro de Windscribe [aquí](https://windscribe.com/login?auth_required){target="_blank"} y luego acceda al [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Seleccione la ubicación del servidor y el puerto que desea usar, y luego haga clic en **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "xvpn"
    ### xvpn

    [Official Website](https://xvpn.io){target="_blank"}

    Si utiliza [xvpn](https://xvpn.io){target="_blank"}, inicie sesión y siga los pasos a continuación para descargar los archivos de configuración de WireGuard.

    ![xvpn WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn_vpn_on_router.png){class="glboxshadow"}

    1. En el menú de la izquierda, vaya a **VPN** -> **VPN on Router**.

    2. En el lado derecho, busque **Step 1** y seleccione **WireGuard** como protocolo.

    3. En **Step 2**, elija la **Region** y la **State/City** que prefiera, y luego haga clic en el botón **Search**.

    4. En los resultados de búsqueda, haga clic en el botón de descarga para obtener el archivo de configuración del servidor deseado.

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

??? "12VPX"
    ### 12VPX

    [Official Website](https://12vpx.com/?aff=1174){target="_blank"}

    Si utiliza [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, inicie sesión y acceda a [esta página](https://12vpx.com/setup/wireguard){target="_blank"}; allí verá las configuraciones de todos los servidores.

    Luego siga [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) para continuar.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
