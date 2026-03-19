# ¿Cómo hacer que todos los datos pasen por la VPN?

Si desea que todo el tráfico de red del router se enrute a través de la VPN y bloquear todas las conexiones a Internet cuando la VPN falle, siga los pasos que se indican a continuación para activar el **VPN Kill Switch**.

**Nota**: Configure primero un cliente VPN en su router GL.iNet antes de activar el VPN Kill Switch.

## Para firmware v4.7 o anterior

Inicie sesión en el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard** -> sección **VPN Client**, y haga clic en **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Active **Block Non-VPN Traffic** (también llamado Kill Switch en algunas versiones de firmware) y luego haga clic en **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Nota:** Cuando **Block Non-VPN Traffic** o **Kill Switch** está activado, si su VPN se desactiva o se desconecta, todos los dispositivos conectados al router tendrán restringido el acceso a Internet para evitar fugas de DNS.

## Para firmware v4.8 o posterior

En el firmware v4.8, el VPN Kill Switch se ha dividido en dos modos.

- **Tunnel Kill Switch**: Se activa de forma predeterminada cuando se activa el túnel VPN correspondiente.

- **Enhanced Kill Switch (in Policy Mode)**: Está desactivado de forma predeterminada para garantizar que todo el tráfico no cubierto por los túneles VPN y las políticas anteriores aún pueda acceder a Internet. En resumen, mantiene el acceso normal a Internet para el tráfico no VPN.

### Tunnel Kill Switch

En el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard**.

Si configura el router como cliente VPN, el Kill Switch de este túnel VPN se activa de forma predeterminada una vez que la VPN está activa.

![global mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![policy mode kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

Haga clic en el icono de engranaje situado junto al nombre del túnel para entrar en **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

El Kill Switch de este túnel está activado de forma predeterminada.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Enhanced Kill Switch

Esta opción está disponible en **Policy Mode**.

En el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard**, cambie el modo VPN a **Policy Mode** y luego busque una sección llamada **All Other Traffic** en la parte inferior. Esta sección puede variar ligeramente según la versión del firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** es un túnel predeterminado que garantiza el acceso normal a Internet para el tráfico no cubierto por los túneles VPN y las políticas anteriores, o para el tráfico que haya pasado por conmutación por error desde conexiones VPN. Este túnel está activado de forma predeterminada y es mutuamente excluyente con **Enhanced Kill Switch**.

**Nota**: Si desactiva **All Other Traffic**, solo podrá acceder a Internet a través de la VPN. Todo el tráfico no coincidente se bloqueará. Esta configuración no anula el Kill Switch individual de cada túnel.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
