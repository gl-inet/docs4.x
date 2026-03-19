# Cómo permitir acceso a la WAN cuando el cliente VPN está habilitado

Cuando el cliente VPN está habilitado en los routers GL.iNet, en el modo global predeterminado los dispositivos LAN no pueden acceder a los dispositivos o servicios de la WAN local, porque todo el tráfico de la LAN se enruta por el túnel VPN en lugar de por su red ascendente (WAN), con el fin de evitar fugas de DNS.
Este tutorial presenta los pasos para hacer accesibles los servicios de la WAN local, como una impresora, un NAS, etc., a los dispositivos LAN del cliente VPN.
![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Para firmware v4.7 y anteriores

Inicie sesión en el panel de administración web de su cliente VPN y vaya a **VPN** -> **VPN Dashboard** -> **VPN Client**. Haga clic en **Global Options** en la esquina superior derecha.
![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}
Habilite **Allow Access WAN** y haga clic en **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}
Si esta opción está habilitada, mientras la VPN esté conectada los dispositivos cliente seguirán pudiendo acceder a los servicios WAN de la subred superior, como su impresora, NAS, etc.

## Para firmware v4.8 y superior

La opción **Allow Access WAN** se ha eliminado del VPN Dashboard en el firmware v4.8. Sin embargo, puede conseguir acceso a la WAN local mediante políticas VPN.
Siga los pasos que se indican a continuación.

1. Inicie sesión en el panel de administración web de su cliente VPN y vaya a **VPN** -> **VPN Dashboard**.
    Haga clic en el modo situado en la esquina superior derecha.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}
    Cambie a **Policy Mode** y haga clic en **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}
    La página se actualizará y se mostrará como se indica a continuación.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}
2. Haga clic en el cuadro central para configurar el destino del túnel.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}
    Seleccione **Exclude Speficied Domain / IP**, introduzca la subred WAN de su router y luego haga clic en **Apply**.
    Esto garantiza que todo el tráfico destinado a la subred WAN se enrute por la WAN local y no por el túnel VPN.
    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}
    Aquí usamos la subred 192.168.0.1/24 como ejemplo. Introduzca esta subred y aplique los cambios; el túnel VPN se mostrará como se indica a continuación.
    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}
    ??? "¿Cómo sé cuál es la subred WAN de mi router GL.iNet?"

        La subred WAN del router GL.iNet normalmente se encuentra en la página **INTERNET**. La determina el dispositivo ascendente al que se conecta la interfaz WAN del router, como un módem del ISP o una puerta de enlace ascendente.
        Por ejemplo, si su router funciona como router secundario, es decir, su puerto WAN está conectado a otra red local como el módem del ISP o el puerto LAN de un router principal, y la IP WAN del router es 192.168.1.165, la Gateway es 192.168.1.1 y la Subnet Mask es 255.255.255.0, entonces la subred WAN correspondiente es 192.168.1.0/24. Esta también es la subred LAN del dispositivo ascendente.
        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}
        **Nota**: La longitud de prefijo de 192.168.1.0/24 es 24, lo que corresponde a la máscara de subred 255.255.255.0. Si la WAN Subnet Mask de su router no es 255.255.255.0, la longitud de prefijo de su subred WAN no será "/24". Confirme la subred WAN según la configuración WAN real.
3. Haga clic en el cuadro de la derecha para configurar la acción del túnel, es decir, usar VPN o no usar VPN.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}
    Seleccione **Use VPN** y elija un archivo de configuración VPN. A continuación, haga clic en **Apply**.
    Si no hay ninguna configuración disponible, suba primero una para configurar su router como cliente VPN. Luego vuelva a esta página, seleccione Use VPN, elija un archivo de configuración VPN y haga clic en Apply.
    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}
4. Active el interruptor en la esquina superior derecha para habilitar este túnel VPN. Comenzará a conectarse.
    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}
    Espere unos minutos. Cuando la conexión se haya establecido correctamente, el indicador se pondrá en verde.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}
    Busque su IP pública para probar la conexión VPN. Por ejemplo, abra un navegador y visite [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Mostrará su dirección IP pública y su ubicación, como se indica a continuación.
    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}
5. Acceda a los dispositivos o servicios de la subred WAN y compruebe si puede hacerlo correctamente.
    Puede utilizar el comando `ping` para probar la conectividad.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
