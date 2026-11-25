# ¿Cómo hacer que todos los datos pasen por la VPN? {#how-to-let-all-data-go-through-vpn}

Si desea que todo el tráfico de red del router se enrute a través de la VPN y bloquear todas las conexiones a Internet cuando la VPN falle, siga los pasos que se indican a continuación para activar el **VPN Kill Switch**.

**Nota**: Configure primero un cliente VPN en su router GL.iNet antes de activar el VPN Kill Switch.

## Para firmware v4.7 o anterior {#for-firmware-v47-or-earlier}

Inicie sesión en el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard** -> sección **VPN Client**, y haga clic en **Global Options**.

![global options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Active **Block Non-VPN Traffic** (también llamado Kill Switch en algunas versiones de firmware) y luego haga clic en **Apply**.

![global options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Nota:** Cuando **Block Non-VPN Traffic** o **Kill Switch** está activado, si su VPN se desactiva o se desconecta, todos los dispositivos conectados al router tendrán restringido el acceso a Internet para evitar fugas de DNS.

## Para firmware v4.8 {#for-firmware-v48}

En el firmware v4.8, el VPN Kill Switch se ha dividido en dos modos.

- **Tunnel Kill Switch**: Se activa de forma predeterminada cuando se activa el túnel VPN correspondiente.

- **Enhanced Kill Switch (in Policy Mode)**: Está desactivado de forma predeterminada para garantizar que todo el tráfico no cubierto por los túneles VPN y las políticas anteriores aún pueda acceder a Internet. En resumen, mantiene el acceso normal a Internet para el tráfico no VPN.

### Tunnel Kill Switch {#tunnel-kill-switch}

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

### Enhanced Kill Switch {#enhanced-kill-switch}

Esta opción está disponible en **Policy Mode**.

En el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard**, cambie el modo VPN a **Policy Mode** y luego busque una sección llamada **All Other Traffic** en la parte inferior. Esta sección puede variar ligeramente según la versión del firmware.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** es el túnel predeterminado. Permite el acceso normal a Internet al tráfico que no coincide con ninguno de los túneles VPN ni con las políticas anteriores, así como al tráfico redirigido a este túnel por conmutación por error de la VPN. Está activado de forma predeterminada. Al desactivarlo, se bloquea todo ese tráfico, incluido el que se redirigiría por conmutación por error de una conexión VPN. Así, solo el tráfico gestionado por los túneles VPN configurados puede acceder a Internet, con la misma protección que ofrece **Enhanced Kill Switch**.

**Nota**: El ajuste **All Other Traffic** no anula el Kill Switch individual de cada túnel.

## Para el firmware v4.9 y versiones posteriores {#for-firmware-v49-and-above}

A partir del firmware v4.9, hay dos tipos de Kill Switch de VPN disponibles, **Tunnel Kill Switch** y **Enhanced Kill Switch**.

### Tunnel Kill Switch {#for-firmware-v49-and-above-tunnel-kill-switch}

En el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard**.

Si configura el router como cliente VPN, el Kill Switch de este túnel VPN se activa de forma predeterminada al activar la VPN.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Haga clic en el icono de engranaje junto al nombre del túnel para abrir **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

El Kill Switch de este túnel está activado de forma predeterminada.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Enhanced Kill Switch {#for-firmware-v49-and-above-enhanced-kill-switch}

En el panel de administración web del router, vaya a **VPN** -> **VPN Dashboard** y haga clic en el icono de engranaje de la esquina superior derecha.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

El ajuste de la política de tráfico ofrece dos opciones, **Allow Non-VPN Traffic** y **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic** está activada de forma predeterminada. Permite el acceso normal a Internet al tráfico que no coincide con ninguno de los túneles VPN ni con las políticas anteriores, así como al que se redirige aquí por conmutación por error de la VPN.

- **Enhanced Kill Switch** obliga a todos los dispositivos a acceder a Internet a través de una VPN cuando se activa. Se bloquea todo el tráfico que no coincide con un túnel VPN. Este ajuste no anula el Kill Switch configurado para cada túnel.


---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
