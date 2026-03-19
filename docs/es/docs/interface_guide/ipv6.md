# IPv6

IPv6 (Internet Protocol version 6) es la versión más reciente del protocolo de Internet, diseñada para sustituir a IPv4. Ofrece un conjunto mucho mayor de direcciones IP únicas, resuelve el problema del agotamiento de direcciones de IPv4 y admite el creciente número de dispositivos conectados en todo el mundo.

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **IPv6**.

Esta página le permite habilitar y configurar IPv6 en su router.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

Cuando IPv6 está habilitado, las interfaces WAN, como Ethernet, obtendrán sus direcciones IPv6 mediante DHCPv6. También puede modificar manualmente la dirección IPv6 en la página de configuración de Ethernet.

**Nota**: Algunas funciones, por ejemplo firewall, GoodCloud y OpenVPN DCO, todavía no son compatibles con IPv6. Si utiliza estas funciones y IPv6 al mismo tiempo, es probable que se produzcan problemas de conectividad.

Active **Enable IPv6**, seleccione el modo para su red principal y el método de obtención de DNS y, a continuación, haga clic en **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: Hay cuatro modos disponibles: **Native**, **Passthrough**, **NAT6** y **Static IPv6**.

- Native: Este modo es aplicable cuando el router obtiene directamente una dirección IPv6 pública y asigna automáticamente direcciones IPv6 a los dispositivos conectados. Este modo puede satisfacer las necesidades de acceso IPv6 de la mayoría de los usuarios.

- Passthrough: Este modo es aplicable cuando los paquetes IPv6 deben pasarse directamente sin ningún procesamiento ni conversión. Por ejemplo, algunas aplicaciones o servicios de red específicos pueden requerir la preservación completa del contenido de los paquetes IPv6 para su posterior procesamiento o análisis, algo utilizado por personal técnico para depuración de red o análisis de seguridad.

- NAT6: Este modo es adecuado para escenarios en los que un router se utiliza como puerta de enlace de gestión para asignar direcciones IPv6 internas dinámicas a cada dispositivo de la red. En este modo, los dispositivos terminales se conectan a través de una Optical Network Terminal y obtienen una dirección IPv6 de red local.

- Static IPv6: Este modo es adecuado para dispositivos o servicios que requieren una dirección IPv6 fija, como servidores o impresoras de red. Este modo garantiza que el dispositivo utilice siempre la misma dirección IPv6, lo que facilita la administración y el acceso.

**Método de obtención de DNS**: Determina cómo obtiene el router las direcciones de los servidores DNS IPv6. Hay dos opciones: **Automatic** y **Manual**.

- Automatic: El router obtendrá dinámicamente las direcciones de los servidores DNS IPv6, por ejemplo mediante DHCPv6.

- Manual: Introduzca direcciones personalizadas de servidores DNS IPv6. Sin embargo, dado que el DNS se utiliza para resolver nombres de dominio a sus direcciones IP correspondientes, la configuración manual de servidores DNS puede provocar fallos en la resolución DNS. Úselo con precaución.

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
