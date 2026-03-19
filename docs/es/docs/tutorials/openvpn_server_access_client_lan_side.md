# Cómo acceder al lado LAN del cliente OpenVPN desde el servidor

Este tutorial presenta los pasos para acceder, desde el lado de su servidor OpenVPN, a la subred LAN del cliente OpenVPN, por ejemplo un NAS, una cámara IP, etc.

## Topología

Como se muestra a continuación, el GL-AXT1800 es un servidor OpenVPN y el GL-MT2500 es un cliente OpenVPN conectado a él. Puede acceder desde el lado del servidor a los dispositivos del lado LAN del GL-MT2500, por ejemplo un NAS o un GL-MT3000 como subrouter.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Añadir una regla de ruta en el servidor

??? "Para firmware v4.7 y anteriores"

    Inicie sesión en el panel de administración web de <u>su servidor OpenVPN</u> y vaya a **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Haga clic en el icono de ruta de la derecha para acceder a la regla de ruta.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    En la ventana emergente, haga clic en el botón **Add Route Rule** a la derecha e introduzca la subred a la que quiere acceder.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Por ejemplo, la subred LAN del cliente OpenVPN GL-MT2500 es **192.168.48.0/24**, por lo que **Target Address** debe ser **192.168.48.0/24**.

    **Gateway** es la IP del cliente que su servidor OpenVPN generó para este cliente OpenVPN. Aquí configuramos **Gateway** como **10.8.0.1** y luego hacemos clic en **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Nota: Si tiene varios clientes OpenVPN cuyas subredes LAN deben ser accesibles, consulte [este enlace](reserve_fixed_IP_for_ovpn_client.md) para reservar una IP de cliente para cada cliente OpenVPN antes de configurar las reglas de ruta.

??? "Para firmware v4.8 y posteriores"

    Inicie sesión en el panel de administración web de <u>su servidor OpenVPN</u> y vaya a **VPN** -> **OpenVPN Server**.

    Haga clic en la pestaña **Route Rules** y luego en el botón **Add Route Rule** a la derecha.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    En la ventana emergente, introduce la subred a la que quieres acceder.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Por ejemplo, la subred LAN del cliente OpenVPN GL-MT2500 es **192.168.48.0/24**, por lo que **Target Address** debe ser **192.168.48.0/24**.

    **Gateway** es la IP del cliente que su servidor OpenVPN generó para este cliente OpenVPN. Aquí configuramos **Gateway** como **10.8.0.2** y luego hacemos clic en **Apply**.

    ![ovpnserver route rule](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Nota: Si tiene varios clientes OpenVPN cuyas subredes LAN deben ser accesibles, consulte [este enlace](reserve_fixed_IP_for_ovpn_client.md) para reservar una IP de cliente para cada cliente OpenVPN antes de configurar las reglas de ruta.

## 2. Permitir el acceso remoto a la LAN del cliente

??? "Para firmware v4.7 y anteriores"

    Inicie sesión en el panel de administración web de <u>su cliente OpenVPN</u> y vaya a **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Haga clic en el icono de engranaje para entrar en las opciones del cliente.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    En la ventana emergente, habilite **Remote Access LAN** y luego haga clic en **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Para firmware v4.8 y posteriores"

    Inicie sesión en el panel de administración web de <u>su cliente OpenVPN</u> y vaya a **VPN** -> **VPN Dashboard**.

    En la esquina superior izquierda de su túnel VPN, haga clic en el icono de engranaje para abrir las opciones del túnel.

    ![ovpnclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    En la ventana emergente, habilite **Allow Remote Access the LAN Subnet** y luego haga clic en **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Probar la conexión

Aquí tiene un ejemplo de acceso al GL-MT3000, un dispositivo de la LAN del cliente OpenVPN, con la IP **192.168.48.211**.

En un dispositivo conectado a su servidor OpenVPN, haga ping a la dirección IP del GL-MT3000, **192.168.48.211**. Esta es la dirección IP que el cliente OpenVPN, es decir, el GL-MT2500, asigna al GL-MT3000 dentro de su LAN.

Si puede hacer ping correctamente, significa que la configuración es correcta. Podrá acceder a todos los demás dispositivos de la subred LAN del cliente OpenVPN mediante sus direcciones IP.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
