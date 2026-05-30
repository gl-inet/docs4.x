# DNS

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **DNS**.

La configuración de DNS del router controla cómo se traducen los nombres de dominio en direcciones IP. Esta página le permite usar los servidores DNS obtenidos automáticamente de los dispositivos upstream, o configurar servidores personalizados y definir prioridades de DNS.

Si configura servidores DNS personalizados, cualquier consulta DNS se resolverá mediante los servidores especificados, en lugar de usar los servidores DNS obtenidos a través de cada interfaz de red. De lo contrario, se usarán los ajustes DNS configurados para cada interfaz.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Al activar esta opción, las consultas DNS privadas pueden fallar. Si su red usa un portal cautivo, desactive esta opción.

- **Override DNS Settings for All Clients:** Si está habilitada, el router sobrescribirá la configuración DNS no cifrada de todos los clientes.

- **Allow Custom DNS to Override VPN DNS:** Si está habilitada, una vez que configure un DNS personalizado, los paquetes transmitidos por el túnel VPN se resolverán usando ese DNS personalizado en lugar de la configuración DNS proporcionada por las conexiones VPN.

## Configuración del servidor DNS

Hay cuatro modos: Automático, DNS cifrado, DNS manual y Proxy DNS.

### Automático

En este modo, el router usará automáticamente el servidor DNS proporcionado por el dispositivo upstream, por ejemplo un módem del ISP o el router principal, o la configuración DNS correspondiente a cada interfaz de red.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### DNS cifrado

Consulte las instrucciones siguientes según la versión de su firmware.

!!! note "Para firmware v4.8 y anteriores"
    
    Hay cuatro tipos de cifrado disponibles: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS y Oblivious DNS over HTTPS.

    Seleccione primero el **Encryption Type**. Las opciones restantes cambiarán según su selección.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - **Para DNS over TLS (DoT)**, elija un proveedor DNS entre **Control D**, **NextDNS** y **Cloudflare**.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - **Para los otros tres tipos (es decir, DNSCrypt-Proxy, DNS over HTTPS y Oblivious DNS over HTTPS)**, seleccione al menos un servidor DNS del repositorio.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "Para firmware v4.9 y posteriores"

    Además de Control D, NextDNS y Cloudflare, ahora hay más proveedores DNS disponibles para el modo DNS cifrado, incluidos **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** y **OpenDNS**. También puede especificar manualmente un servidor DNS cifrado según sea necesario.

    Seleccione primero el **DNS Provider**. Las opciones restantes cambiarán según su selección.

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - Si selecciona un proveedor DNS específico (por ejemplo, NextDNS), elija un tipo de cifrado entre **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** y **DNS over QUIC (DoQ)**. Tenga en cuenta que DNS over QUIC (DoQ) se introdujo en el firmware v4.9 y solo está disponible cuando se usa Control D, NextDNS o AdGuard DNS como proveedor DNS.

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - Si selecciona **Manual** como proveedor DNS, elija un tipo de cifrado entre **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** y **DNSCrypt**.

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        Después, haga clic en **Add a Server** para añadir al menos un servidor DNS. Puede introducir directamente la URL o el formato stamp del DNS cifrado. Para ver una lista de servidores públicos, consulte [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Comparación de tipos de cifrado

1. **DNS over TLS (DoT)**

    Cifra las consultas DNS a través de un puerto TLS dedicado. Separa el tráfico DNS del tráfico web normal y los operadores de red pueden identificarlo fácilmente.

2. **DNS over HTTPS (DoH)**

    Transmite los datos DNS dentro del tráfico HTTPS estándar. Mezcla las solicitudes DNS con el tráfico web normal para ofrecer una privacidad sólida y evitar filtros de tráfico sencillos.

3. **DNS over QUIC (DoQ)**
    
    Encapsula DNS sobre el protocolo QUIC. Ofrece baja latencia, reconexión rápida y un rendimiento estable en redes inestables.

4. **Oblivious DNS over HTTPS (ODoH)**

    Es una versión mejorada de DoH. Separa la IP del usuario de las consultas DNS, evitando que tanto el servidor como los proveedores de red rastreen su actividad de navegación.

5. **DNSCrypt**

    Es un protocolo maduro de cifrado para DNS. Autentica y cifra el tráfico DNS, con especial enfoque en la protección contra manipulaciones y la compatibilidad con entornos de red heredados.

### DNS manual

En este modo, puede personalizar el servidor DNS de su router. Seleccione al menos un servidor DNS para el router en la lista desplegable.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### Proxy DNS

En este modo, el router dirigirá todas las consultas DNS de la LAN a la dirección del servidor proxy que especifique, por ejemplo `8.8.8.8#53`. Esto puede resultar útil si está ejecutando otro servidor DNS o Pi-hole en su red.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Editar Hosts

Puede hacer clic en el botón **Edit Hosts** situado en la parte superior derecha para personalizar reglas estáticas de hosts.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

El router dará prioridad a estas reglas de hosts al resolver las solicitudes de los clientes conectados.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
