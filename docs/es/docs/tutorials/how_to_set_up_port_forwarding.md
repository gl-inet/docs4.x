# Cómo configurar el reenvío de puertos en su router principal

Si está configurando un servidor, como un [servidor OpenVPN](how_to_set_up_openvpn_server.md) o un [servidor WireGuard](build_your_own_wireguard_home_server_with_two_glinet_routers.md), en su router GL.iNet y este está conectado a un router principal, tendrá que configurar el reenvío de puertos en el router principal. Esto garantiza que se pueda acceder correctamente al servidor.

Tenga en cuenta que, si hay otros routers entre el router principal y el router GL.iNet, tendrá que configurar el reenvío de puertos en todos esos routers intermedios.

## Preparación

Antes de configurar el reenvío de puertos, recomendamos **reservar una dirección IP estática** para el router GL.iNet en su router principal. Esto garantiza que al router GL.iNet siempre se le asigne una dirección IP fija.

De lo contrario, si el router principal o el router GL.iNet se reinicia, el router principal puede asignar una nueva dirección IP al router GL.iNet, lo que hará que falle la regla de reenvío de puertos.

A continuación, configure el reenvío de puertos en su router principal para el router GL.iNet.

Los pasos para configurar el reenvío de puertos varían según la marca y el modelo del router. Consulte la sección correspondiente a continuación.

## Uso de un router GL.iNet como router principal

Consulte [este enlace](../interface_guide/port_forwarding.md){target="\_blank"}.

## Uso de otra marca de router como router principal

!!! note "Asegúrese de introducir la siguiente información al configurar el reenvío de puertos"

    Al configurar el reenvío de puertos, asegúrese de proporcionar la siguiente información. Tenga en cuenta que la terminología puede variar según la marca y el modelo del router.

    * **External port/Internal port:** introduzca el puerto que esté utilizando. Por ejemplo, los puertos predeterminados son **1194** para servidores OpenVPN y **51820** para servidores WireGuard.
    * **Protocol:** elija **All** o **UDP/TCP**.
    * **Internal IP** o **Host IP**: introduzca la dirección IP WAN de su router secundario o seleccione el router secundario en la lista desplegable si está disponible.

A continuación se muestran instrucciones paso a paso para configurar el reenvío de puertos en algunas marcas y modelos comunes de routers principales.

Si la marca o el modelo de su router principal no aparece a continuación, consulte la documentación de su router o póngase en contacto con su equipo de soporte para obtener más ayuda.

### AT&T

- [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="\_blank"}
- [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="\_blank"}
- [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="\_blank"}

### Comcast (Xfinity)

- [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="\_blank"}

### TP-Link

- [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="\_blank"}
- [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="\_blank"}

### Eero

Consulte [este enlace](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="\_blank"}.

### Linksys

Consulte [este enlace](https://support.linksys.com/kb/article/318-en/){target="\_blank"}.

### Netgear

Consulte [este enlace](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="\_blank"}.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
