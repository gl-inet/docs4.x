# ¿Cómo acceder de forma remota al panel de administración web de un router GL.iNet?

El siguiente método requiere una configuración previa mientras aún se encuentra físicamente junto al router.

## Método 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} es una plataforma diseñada para simplificar la implementación y gestión remotas de dispositivos conectados. Proporciona una forma sencilla de acceder y gestionar routers GL.iNet de forma remota. Solo tiene que vincular su router GL.iNet a GoodCloud; después podrá acceder de forma remota al panel de administración web del router en cualquier momento y desde cualquier lugar.

Consulte [esta guía](../interface_guide/cloud.md){target="_blank"} para obtener más información.

## Método 2. VPN

Si su router tiene una **IP pública**, puede acceder de forma remota a su panel de administración web mediante un túnel VPN. Tenga en cuenta que este método implica configuraciones avanzadas y requiere más tiempo de preparación.

1. Asegúrese de que su router tenga una IP pública. [¿Cómo puedo comprobar si tengo una dirección IP pública?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Configure su router como WireGuard Server. Consulte los detalles [aquí](../interface_guide/wireguard_server.md){target="_blank"}.

3. Exporte un archivo de configuración desde su WireGuard Server para usarlo más adelante.

4. En el panel de administración web del router, vaya a **VPN** -> **WireGuard Server** y haga clic en **Options** en la esquina superior derecha. Active **Allow Remote Access to the LAN Subnet** y, a continuación, haga clic en **Apply**.

5. Configure como WireGuard Client el dispositivo desde el que desea acceder de forma remota al router importando manualmente el archivo de configuración.

    - Si su WireGuard Client es un dispositivo final, como un smartphone o un portátil, [instale la aplicación WireGuard](https://www.wireguard.com/install){target="_blank"} y, a continuación, importe el archivo para iniciar una conexión.

    - Si su WireGuard Client es otro router GL.iNet, como un router de viaje GL.iNet, consulte [esta guía](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} para importar el archivo de configuración e iniciar una conexión.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
