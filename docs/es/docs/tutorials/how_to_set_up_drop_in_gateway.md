# Cómo configurar Drop-in Gateway en un router GL.iNet

GL.iNet ofrece la función Drop-in Gateway, que amplía la funcionalidad de su router principal con características que quizá no tenga, como AdGuard Home, DNS cifrado y VPN. Al usar esta función, puede seguir utilizando su router principal como de costumbre mientras disfruta de funciones adicionales.

Puede habilitar Drop-in Gateway para [todos sus dispositivos](#habilitar-drop-in-gateway-para-todos-los-dispositivos) o para [dispositivos específicos](#habilitar-drop-in-gateway-para-dispositivos-específicos) conectados a su router principal. Siga la sección correspondiente según su configuración.

**Nota**: Los modelos con versiones de firmware anteriores a v4.5.0 solo admiten habilitar Drop-in Gateway para todos los dispositivos. Cuando Drop-in Gateway está habilitado, todos los dispositivos cliente se conectarán en red a través de Drop-in Gateway, lo que significa que todo el tráfico de los clientes conectados será gestionado primero por este router.

---

## Habilitar Drop-in Gateway para todos los dispositivos

### 1. Conecte el router GL.iNet al router principal

Conecte el puerto WAN del router GL.iNet al puerto LAN del router principal mediante un cable Ethernet.

### 2. Habilitar Drop-in Gateway

Hay dos formas de habilitar Drop-in Gateway: mediante el panel de administración del router o mediante la app móvil de GL.iNet.

??? "Usar el panel de administración web"

    1. En un navegador web, introduzca `192.168.8.1`.

    2. Introduzca la contraseña y haga clic en **Login**.

    3. En la barra lateral izquierda, haga clic en **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Junto a **Enable Drop-in Gateway Mode**, active el interruptor.

    5. Seleccione **All devices are networked through drop-in gateway**.

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Haga clic en **Apply**.

??? "Usar la app móvil de GL.iNet"

    **Nota**: Antes de empezar, instale la app móvil de GL.iNet en su dispositivo.

    1. En la pantalla principal de la app, toque la pestaña **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Toque **Enable**.

    3. En **Devices are networked via drop-in gateway**, toque **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Toque **Done**.

### 3. Deshabilitar el servidor DHCP en el router principal

Inicie sesión en el router principal para deshabilitar el servidor DHCP. Puede consultar las instrucciones proporcionadas por el fabricante de su router o contactar con su soporte.

### 4. Configurar AdGuard, DNS, VPN y otras funciones

Siga estas guías para habilitar las funciones que desee en su router GL.iNet.

- [AdGuard Home](../interface_guide/adguardhome.md){target="\_blank"}
- [Encrypted DNS](../interface_guide/dns.md){target="\_blank"}
- [Parental Control](../interface_guide/parental_control.md){target="\_blank"}
- [WireGuard Client](../interface_guide/wireguard_client.md){target="\_blank"}
- [OpenVPN Client](../interface_guide/openvpn_client.md){target="\_blank"}

---

## Habilitar Drop-in Gateway para dispositivos específicos

### 1. Conecte el router GL.iNet al router principal

Conecte el puerto WAN del router GL.iNet al puerto LAN del router principal mediante un cable Ethernet.

### 2. Habilitar Drop-in Gateway

Hay dos formas de habilitar Drop-in Gateway: mediante el [panel de administración del router](#usar-el-panel-de-administración-web) o mediante la [app móvil de GL.iNet](#usar-la-app-móvil-de-glinet).

??? "Usar el panel de administración web"

    1. En un navegador web, introduzca `192.168.8.1`.

    2. Introduzca la contraseña y haga clic en **Login**.

    3. En la barra lateral izquierda, haga clic en **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Junto a **Enable Drop-in Gateway Mode**, active el interruptor.

    5. Seleccione **Some devices select their own networking gateway**.

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Haga clic en **Apply**.

    **Nota**: No cierre esta pestaña. Necesitará introducir la dirección IP que aparece en pantalla en el siguiente paso.

??? "Usar la app móvil de GL.iNet"

    **Nota**: Antes de empezar, instale la app móvil de GL.iNet en su dispositivo.

    1. En la pantalla principal de la app, toque la pestaña **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Toque **Enable**.

    3. En **Devices are networked via drop-in gateway**, toque **part**.

        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Toque **Done**.

    **Nota**: No cierre esta pestaña. Necesitará introducir la dirección IP que aparece en pantalla en el siguiente paso.

### 3. Configurar la puerta de enlace y el DNS en un dispositivo específico

??? "Windows"

    1. Conecte su dispositivo al router principal.
    2. En Windows, abra **Settings** > **Network & Internet**.
    3. Según el método de conexión, siga estos pasos:
        * Ethernet: haga clic en **Ethernet**.
        * Wi-Fi: haga clic en **Wi-Fi** y luego en el nombre de la red Wi-Fi.
    4. Copie la dirección IPv4. Junto a **IP assignment**, haga clic en **Edit**.
    5. Haga clic en **Manual**.
    6. Active **IPv4**.
    7. Introduzca la información siguiente:
        * **IP address:** pegue la dirección IP que copió en el paso 4.
        * **Subnet mask:** introduzca **255.255.255.0**.
        * **Gateway:** introduzca la dirección IP que aparece en la página **Drop-in Gateway**.
        * **Preferred DNS:** introduzca la dirección IP que aparece en la página **Drop-in Gateway**.
    8. Haga clic en **Save**.

??? "Android" 1. Conecte su dispositivo al router principal. 2. En Android, abra **Settings**. 3. Toque **Connections** > **Wi-Fi**. 4. Toque el icono **Settings** situado junto a la red a la que está conectado. 5. Toque **View more**. 6. Toque **IP settings** > **Static**. 7. En **Gateway** y **DNS 1**, introduzca la dirección IP que aparece en la pantalla **Drop-in Gateway**. 8. Toque **Save**.

??? "iOS" 1. Conecte su dispositivo al router principal. 2. En iOS, abra **Settings**. 3. Toque **Wi-Fi**. 4. Toque la red Wi-Fi a la que está conectado. 5. En **IPv4 Address**, tome nota de **IP Address** y **Subnet Mask**. 6. Toque **Configure IP** > **Manual**. 7. Introduzca la información siguiente:
_ **IP Address:** introduzca la IP obtenida en el paso 5.
_ **Subnet Mask:** introduzca la máscara de subred obtenida en el paso 5. \* **Router:** introduzca la dirección IP que aparece en la pantalla **Drop-in Gateway**. 8. Toque **Save**. 9. Toque **Configure DNS** y luego **Manual**. 10. Toque **Add Server** e introduzca la dirección IP que aparece en la pantalla **Drop-in Gateway**. 11. Toque **Save**.

??? "Mac" 1. Conecte su dispositivo al router principal. 2. En su Mac, haga clic en el icono de Apple > **System Settings**. 3. En la barra lateral izquierda, haga clic en **Network**. 4. Junto a la red a la que está conectado, haga clic en **Details**. 5. Haga clic en **TCP/IP**. 6. Tome nota de **IP Address** y **Subnet Mask**. 7. Junto a **Configure IPv4**, haga clic en **Manually**. 8. Introduzca la información siguiente:
_ **IP address:** introduzca la dirección IP obtenida en el paso 6.
_ **Subnet mask:** introduzca la máscara de subred obtenida en el paso 6. \* **Router:** introduzca la dirección IP que aparece en la página **Drop-in Gateway**. 9. Haga clic en **OK** > **OK**.

### 4. Configurar AdGuard, DNS, VPN y otras funciones

Siga estas guías para habilitar las funciones que desee en su router GL.iNet.

- [AdGuard Home](../interface_guide/adguardhome.md){target="\_blank"}
- [Encrypted DNS](../interface_guide/dns.md){target="\_blank"}
- [Parental Control](../interface_guide/parental_control.md){target="\_blank"}
- [WireGuard Client](../interface_guide/wireguard_client.md){target="\_blank"}
- [OpenVPN Client](../interface_guide/openvpn_client.md){target="\_blank"}

---

Artículo relacionado:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
