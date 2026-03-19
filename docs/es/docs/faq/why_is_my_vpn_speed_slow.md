# ¿Por qué la velocidad de mi VPN es más lenta de lo esperado?

Si ha notado que la velocidad de su conexión VPN es inferior a la velocidad máxima teórica, probada en una red local ideal, esto es completamente normal en el uso real.

Las VPN están diseñadas para priorizar la seguridad y la privacidad, lo que afecta de forma inherente a la velocidad. Es normal que la velocidad de una VPN se sitúe entre el 30% y el 50% del máximo anunciado en condiciones de red habituales. Esta diferencia se debe a múltiples factores que afectan al rendimiento, los cuales se explican a continuación, junto con algunos consejos para optimizar su experiencia.

**Nota**: Los métodos siguientes pueden ayudar a mejorar la velocidad de la VPN, pero no pueden garantizar que alcance la velocidad anunciada, ya que el rendimiento real depende de múltiples factores.

## Velocidad de CPU del router

La VPN cifra sus datos para proteger la privacidad, lo que añade procesamiento adicional. Este cifrado y descifrado puede ralentizar la conexión. Elija un router con una CPU más rápida para mejorar la velocidad de su VPN.

Hemos incluido las velocidades de prueba de VPN de todos los modelos en nuestra [página de productos](https://www.gl-inet.com/products/). Sin embargo, tenga en cuenta lo siguiente:

- Las pruebas se realizan en una red local. Las velocidades reales pueden variar según la configuración de su red.
- Las velocidades de OpenVPN y WireGuard serán más lentas cuando el router se use como servidor. Los resultados anteriores corresponden al modo cliente.

## Distancia al servidor

Si el servidor VPN está lejos de su ubicación física, los datos deben recorrer una distancia mayor, lo que provoca más latencia y velocidades más bajas.

Puede ver el ejemplo siguiente, que muestra velocidades del cliente al conectarse a distintas ubicaciones de servidor a la misma hora del día.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Carga del servidor

Si muchos usuarios están conectados al mismo servidor VPN, este puede congestionarse y provocar velocidades más lentas para todos.

## Velocidad de subida del servidor

Si está usando un túnel VPN privado, la velocidad de subida del proveedor de servicios de Internet, ISP, en el lado del servidor será el cuello de botella para la velocidad de descarga en el lado del cliente, ya que el cliente VPN descarga los datos a través del servidor.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Diferencias entre protocolos

Diferentes protocolos VPN, como OpenVPN o WireGuard, varían en seguridad y velocidad. Algunos pueden ser más lentos debido a sus métodos de cifrado.

## Limitación por parte del ISP

Algunos proveedores de servicios de Internet, ISP, pueden limitar la velocidad de los usuarios que usan VPN, especialmente si sospechan un uso intensivo de datos. Esto es especialmente frecuente en algunos países en desarrollo o pequeñas ciudades donde muchos usuarios comparten una infraestructura de Internet limitada.

## DNS

Algunos proveedores de servicios de Internet, ISP, pueden no resolver correctamente los dominios de la VPN. Pruebe a usar [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) en la configuración de Network de su router.

## MTU

Algunos proveedores de servicios de Internet, ISP, especialmente los operadores móviles, pueden limitar el tamaño de los paquetes de datos. Pruebe a cambiar el MTU predeterminado de 1420 a 1380 o 1280 en las opciones del cliente VPN.

Para el firmware v4.8 y superior, consulte [aquí](../interface_guide/vpn_dashboard.md/#tunnel-options).

Para el firmware v4.7 y anteriores, consulte [aquí](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
