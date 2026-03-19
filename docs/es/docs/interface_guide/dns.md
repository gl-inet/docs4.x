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

- **Automatic**: El router usará automáticamente el servidor DNS proporcionado por el dispositivo upstream, por ejemplo un módem del ISP o el router principal, o la configuración DNS correspondiente a cada interfaz de red.

  ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: Hay cuatro tipos de cifrado disponibles: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS y Oblivious DNS over HTTPS.

  ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}
  - Para DNS over TLS, seleccione un proveedor DNS entre Control D, NextDNS y Cloudflare.

    ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

  - Para los otros tres tipos, es decir, DNSCrypt-Proxy, DNS over HTTPS y Oblivious DNS over HTTPS, seleccione al menos un DNS Server del repositorio.

    ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: Seleccione al menos un DNS Server para su router en la lista desplegable.

  ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: El router dirigirá todas las consultas DNS de la LAN a la dirección del servidor proxy que usted especifique, por ejemplo `8.8.8.8#53`. Esto puede ser útil si está ejecutando otro servidor DNS o Pi-hole en su red.

  ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Editar Hosts

Las solicitudes de los clientes se resolverán prioritariamente utilizando las reglas DNS estáticas que escriba en Hosts.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
