# DNS

**Nota**: El contenido de esta página se introdujo por primera vez en el firmware v4.11.

Si el dispositivo utiliza otra versión del firmware, use el selector siguiente para cambiar a la guía correspondiente.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 y anteriores](dns.md)

</div>

---

En el menú lateral izquierdo del panel de administración web, vaya a **DNS**.

Los ajustes DNS del router controlan cómo se traducen los nombres de dominio en direcciones IP. Esta página permite utilizar los servidores DNS obtenidos automáticamente de los dispositivos de nivel superior o configurar servidores personalizados. También puede configurar opciones DNS y editar reglas de host estáticas.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

De forma predeterminada, las consultas DNS del tráfico que coincide con la política VPN utilizan los servidores DNS proporcionados por el túnel VPN. Las consultas DNS que no corresponden a la VPN utilizan los servidores obtenidos de la interfaz WAN activa. Si configura servidores DNS personalizados, puede aplicarlos a los túneles VPN, al propio router o a ambos. Cuando se activan estas opciones, las consultas del ámbito seleccionado se resuelven mediante los servidores especificados en lugar de los obtenidos de las interfaces de red correspondientes. Si no se configuran servidores personalizados, el router utiliza los servidores DNS obtenidos de las interfaces de red correspondientes.

## DNS de WAN

WAN DNS muestra los servidores DNS obtenidos de cada enlace ascendente WAN, incluidos Ethernet, Repeater, Tethering y Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Si un enlace WAN está activo, sus direcciones de servidor DNS aparecen a la derecha, como se muestra a continuación.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## DNS de VPN

VPN DNS muestra los servidores DNS obtenidos de cada túnel VPN activo.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Si hay un túnel VPN activo, las consultas DNS del tráfico VPN seguirán la configuración de VPN DNS, como se muestra a continuación.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## DNS manual

Manual DNS admite dos tipos de configuración: **Static DNS** y **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: Si esta opción está activada, se utilizará el DNS manual personalizado para los paquetes que atraviesen el túnel VPN en lugar de los ajustes DNS de la VPN.

- **Apply Manual DNS to Router Itself**: Esta opción está activada de forma predeterminada. Cuando está habilitada, los servicios integrados del router (como GoodCloud) aplican la configuración DNS manual personalizada.

### DNS estático

Static DNS permite introducir manualmente direcciones de servidores DNS IPv4 o IPv6. Puede escribir las direcciones directamente o seleccionar servidores DNS públicos predefinidos en la lista desplegable.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Puede introducir hasta cuatro direcciones de servidores DNS. Haga clic en **Apply** para guardar los cambios.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### DNS cifrado

El modo Encrypted DNS admite varios proveedores, entre ellos Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS y OpenDNS. También puede especificar manualmente un servidor DNS cifrado cuando sea necesario.

Seleccione primero el DNS Provider. Las opciones restantes cambiarán según su selección.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Si selecciona un proveedor DNS concreto (por ejemplo, NextDNS), elija un tipo de cifrado entre DNS over TLS (DoT), DNS over HTTPS (DoH) y DNS over QUIC (DoQ). DNS over QUIC (DoQ) se introdujo en el firmware v4.9 y solo está disponible al usar Control D, NextDNS o AdGuard DNS como proveedor.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Si selecciona Manual como proveedor DNS, elija un tipo de cifrado entre DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS y DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    A continuación, haga clic en **Add a Server** para añadir al menos un servidor DNS. Puede introducir directamente la URL o el formato de sello del DNS cifrado. Consulte la lista de servidores públicos en [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Comparación de los tipos de cifrado"

    1. **DNS over TLS (DoT)**

        Cifra las consultas DNS mediante un puerto TLS dedicado. Separa el tráfico DNS del tráfico web habitual y los operadores de red pueden identificarlo con facilidad.

    2. **DNS over HTTPS (DoH)**

        Transmite los datos DNS dentro del tráfico HTTPS estándar. Mezcla las solicitudes DNS con el tráfico web normal para ofrecer una mayor privacidad y evitar filtros de tráfico sencillos.

    3. **DNS over QUIC (DoQ)**

        Encapsula DNS mediante el protocolo QUIC. Ofrece baja latencia, reconexión rápida y rendimiento estable en redes inestables.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Una versión mejorada de DoH. Separa la IP del usuario de las consultas DNS e impide que tanto el servidor como los proveedores de red rastreen la actividad de navegación.

    5. **DNSCrypt**

        Un protocolo de cifrado maduro para DNS. Autentica y cifra el tráfico DNS, con énfasis en la protección contra manipulaciones y la compatibilidad con entornos de red antiguos.

## Opciones DNS

Haga clic en **Options** en la esquina superior derecha para configurar los ajustes DNS avanzados.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Puede activar o desactivar estas opciones según sea necesario.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: Activar esta opción puede provocar que fallen las búsquedas DNS privadas. Si la red tiene un portal cautivo, desactive esta opción.

- **Override DNS Settings of All Clients**: Si se activa esta opción, el router sustituye los ajustes DNS sin cifrar de todos los clientes.

## Editar hosts

Puede hacer clic en **Edit Hosts** en la esquina superior derecha para personalizar las reglas de host estáticas.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

El router da prioridad a estas reglas de host al resolver las solicitudes de los clientes conectados.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
