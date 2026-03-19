# Cómo acceder al lado LAN del cliente WireGuard desde el servidor

Este tutorial presenta los pasos para acceder, desde el lado de su servidor WireGuard, a la subred LAN del cliente WireGuard, por ejemplo cámaras IP, NAS, etc.

## Topología

Como se muestra a continuación, el GL-MT2500 es un servidor WireGuard y el GL-AXT1800 es un cliente WireGuard conectado a él. Puede acceder desde el lado del servidor a los dispositivos del lado LAN del GL-AXT1800, por ejemplo una cámara IP o un NAS.

![Topology](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Añadir una regla de ruta en el servidor

??? "Para firmware v4.7 y anteriores"

    Inicie sesión en el panel de administración web de <u>su servidor WireGuard</u> y luego vaya a **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Haga clic en el icono de ruta de la derecha para acceder a la regla de ruta.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Haga clic en **Add Route Rule** en la esquina superior derecha e introduzca la subred a la que quiere acceder.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Por ejemplo, la subred LAN del cliente WireGuard GL-AXT1800 es **192.168.8.0/24**, por lo que **Target Address** debe ser **192.168.8.0/24**.

    **Gateway** es la IP del cliente que su servidor WireGuard generó para este cliente WireGuard. Puede encontrarla en la pestaña **Profiles** de la página **WireGuard Server**. Como se muestra a continuación, la IP del cliente WireGuard GL-AXT1800 es **10.0.0.4**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Por lo tanto, configure **Gateway** como **10.0.0.4** y **Scope** como **global**, y luego haga clic en **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Para firmware v4.8 y posteriores"

    Inicie sesión en el panel de administración web de <u>su servidor WireGuard</u> y luego vaya a **VPN** -> **WireGuard Server**.

    Haga clic en la pestaña **Route Rules** y en **Add Route Rule** a la derecha.

    ![add route rule 1](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    En la ventana emergente, introduzca la subred a la que quiere acceder.

    ![add route rule 2](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Por ejemplo, la subred LAN del cliente WireGuard GL-AXT1800 es **192.168.8.0/24**, por lo que **Target Address** debe ser **192.168.8.0/24**.

    **Gateway** es la IP del cliente que su servidor WireGuard generó para este cliente WireGuard. Puede encontrarla en la pestaña **Profiles** de la misma página. Como se muestra a continuación, la IP del cliente WireGuard GL-AXT1800 es **10.1.0.2**.

    ![client ip](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Por lo tanto, configure **Gateway** como **10.1.0.2** y luego haga clic en **Apply**.

    ![add route rule 3](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Permitir el acceso remoto a la LAN del cliente

??? "Para firmware v4.7 y anteriores"

    Inicie sesión en el panel de administración web de <u>su cliente WireGuard</u> y vaya a **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Haga clic en el icono de engranaje a la derecha de WireGuard.

    ![wgclient options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    En la ventana emergente, habilite **Remote Access LAN** y luego haga clic en **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Para firmware v4.8 y posteriores"

    Inicie sesión en el panel de administración web de <u>su cliente WireGuard</u> y vaya a **VPN** -> **VPN Dashboard**.

    En la esquina superior izquierda de su túnel VPN, haga clic en el icono de engranaje para abrir las opciones del túnel.

    ![tunnel options](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    En la ventana emergente, habilite **Allow Remote Access the LAN Subnet** y luego haga clic en **Apply**.

    ![allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

## 3. Probar la conexión

Compruebe si puede acceder desde el lado del servidor a los dispositivos LAN de su cliente WireGuard.

Puede probar la conexión con `ping`. Por ejemplo, en un dispositivo conectado al servidor WireGuard, es decir, el GL-MT2500, haga `ping` a la dirección IP de un dispositivo dentro de la LAN de su cliente WireGuard, es decir, el GL-AXT1800, y compruebe si responde correctamente.

![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
