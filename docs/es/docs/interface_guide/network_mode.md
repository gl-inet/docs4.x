# Modo de red

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Network Mode**.

El modo de red se refiere a los distintos roles y funciones operativas que un router puede asumir para satisfacer diferentes necesidades de implementación de red. Estos modos están adaptados a escenarios que van desde la cobertura Wi-Fi doméstica hasta redes empresariales multinodo, y cada modo desactiva o habilita funciones específicas del router para optimizar el rendimiento.

!!! note

    1. Cuando cambie el modo de red del router, es posible que deba volver a conectar todos los dispositivos cliente.

    2. **Cuando el router esté en modo Access Point / WDS / Bridge, no podrá acceder al panel de administración web usando la dirección IP LAN original.** En su lugar, deberá iniciar sesión en el router ascendente para encontrar la dirección IP que le ha asignado a este router y, a continuación, usar esa dirección IP para acceder al panel de administración web. Si no tiene acceso al router ascendente, mantenga pulsado el botón de reinicio durante 4 segundos para volver al modo Router predeterminado.

    3. **En el modo Non-Router, las siguientes funciones no estarán disponibles**: Access Control (Allowlist y Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Para modelos con Wi-Fi

Salvo algunos modelos específicos, la mayoría de los routers inalámbricos GL.iNet tienen funcionalidad Wi-Fi.

Los modelos con funcionalidad Wi-Fi suelen admitir cuatro modos de red: Router, Access Point, Extender y WDS. Tenga en cuenta que algunos modelos no admiten el modo WDS.

![modo de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: Es el modo de funcionamiento predeterminado para la mayoría de los routers domésticos y de pequeñas oficinas, diseñado para crear una red de área local privada y actuar como una puerta de enlace dedicada entre Internet pública y los dispositivos conectados.

  En el modo Router, el dispositivo habilita funciones básicas como NAT, DHCP y un firewall integrado. Se conecta a una línea ascendente como la fibra de banda ancha, asigna automáticamente direcciones IP privadas a los dispositivos conectados y proporciona seguridad de red a toda la red privada.

  ***

- **Access Point**: Este modo permite que un router se conecte a una red cableada mediante un cable LAN y emita señales inalámbricas, ampliando la cobertura Wi-Fi en espacios grandes para permitir que más dispositivos accedan a la red.

  En el modo Access Point, el router desactiva sus funciones NAT y DHCP, y funciona únicamente como transmisor de señal inalámbrica y switch, en lugar de como puerta de enlace independiente.

  Después de cambiar al modo Access Point, no podrá acceder al panel de administración web usando la dirección IP LAN original. En su lugar, deberá iniciar sesión en el router ascendente para encontrar la dirección IP que le ha asignado a este AP y, a continuación, usar esa dirección IP para acceder al panel de administración web. Si no tiene acceso al router ascendente, mantenga pulsado el botón de reinicio durante 4 segundos para volver al modo Router predeterminado.

  ***

- **Extender**: Este modo está diseñado para ampliar la cobertura Wi-Fi de una red inalámbrica existente y eliminar zonas muertas de señal en áreas con mala conectividad.

  Permite que el router reciba de forma inalámbrica las señales del router principal, las amplifique y retransmita la señal reforzada. A diferencia del modo Access Point, no requiere conexión por cable con el router principal, pero puede reducir el ancho de banda a la mitad, ya que el dispositivo debe gestionar simultáneamente la recepción y la transmisión de la señal.

  En el modo Extender, aún podrá acceder al panel de administración web usando su dirección IP LAN original.

  ***

- **WDS**: El modo Wireless Distribution System (WDS) es similar al modo Extender porque amplía la cobertura Wi-Fi de forma inalámbrica, pero admite puentes inalámbricos entre varios routers compatibles. Se recomienda para ampliar la red inalámbrica cuando el router ascendente tiene funcionalidad WDS.

  Este modo es ideal para escenarios como la cobertura de edificios de varias plantas o pequeños campus de oficinas en los que varios routers deben trabajar juntos para formar una red inalámbrica unificada. A diferencia del modo Extender, que solo transmite señales de un router principal a un único extensor, el modo WDS permite que los routers interconectados envíen y reciban señales, lo que posibilita una cobertura fluida en áreas más amplias con varios nodos de señal.

  Después de cambiar al modo WDS, no podrá acceder al panel de administración web usando la dirección IP LAN original. En su lugar, deberá iniciar sesión en el router ascendente para encontrar la dirección IP que le ha asignado a este router WDS y, a continuación, usar esa dirección IP para acceder al panel de administración web. Si no tiene acceso al router ascendente, mantenga pulsado el botón de reinicio durante 4 segundos para volver al modo Router predeterminado.

## Para modelos sin Wi-Fi

GL-MT2500/GL-MT2500A no admite los modos Access Point, Extender ni WDS, ya que no dispone de funcionalidad Wi-Fi. Pero sí admite el modo Router y el modo Bridge.

![modo de red de gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: Es el modo de funcionamiento predeterminado para la mayoría de los routers domésticos y de pequeñas oficinas, diseñado para crear una red de área local privada (LAN) y actuar como una puerta de enlace dedicada entre Internet pública y los dispositivos conectados.

  En el modo Router, el dispositivo habilita funciones básicas como NAT, DHCP y un firewall integrado. Se conecta a una línea ascendente como la fibra de banda ancha, asigna automáticamente direcciones IP privadas a los dispositivos conectados y proporciona seguridad de red a toda la red privada.

  ***

- **Bridge**: Permite que el router se conecte a una red cableada y funcione como un puente entre dispositivos de red.

  En este modo, el router funciona esencialmente como un switch, reenviando datos entre los dispositivos conectados sin realizar servicios de NAT, firewall ni DHCP. Esto permite una comunicación fluida entre dispositivos de la misma red al actuar como un punto de conexión sencillo en lugar de una puerta de enlace de red.

  Después de cambiar al modo Bridge, no podrá acceder al panel de administración web usando la dirección IP LAN original. En su lugar, deberá iniciar sesión en el router ascendente para encontrar la dirección IP que le ha asignado a este router Bridge y, a continuación, usar esa dirección IP para acceder al panel de administración web. Si no tiene acceso al router ascendente, mantenga pulsado el botón de reinicio durante 4 segundos para volver al modo Router predeterminado.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
