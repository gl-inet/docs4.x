# Cómo comprobar si tiene una dirección IP pública

Una dirección pública, a diferencia de una dirección IP privada, es un identificador numérico único asignado a sus dispositivos conectados a Internet. Necesitará una dirección IP pública si desea alojar un sitio web, configurar un servidor VPN o proporcionar cualquier servicio en línea. Normalmente, su proveedor de servicios de Internet se la proporciona.

Si no está seguro de tener una dirección IP pública, siga uno de estos métodos para comprobarlo.
**Método 1: Contacte directamente con su proveedor de servicios de Internet**

**Método 2: Compruebe su dirección IP en el panel de administración del router y en Internet**
1. Inicie sesión en el panel de administración de su router.
    * Para routers GL.iNet, introduzca `192.168.8.1` en un navegador web e inicie sesión.
    * Si tiene más de un router en la instalación, inicie sesión en el panel de administración del router principal.
2. En el panel de administración del router, localice su dirección IP WAN, por ejemplo 42.XXX.XX.
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. En un navegador web, busque "what is my ip".
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Si las dos direcciones IP coinciden, tiene una dirección IP pública.
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Si no dispone de una dirección IP pública, puede considerar usar una herramienta de penetración de intranet. Esto permite que su sitio web, servidor VPN o servicios sean accesibles desde Internet incluso si no dispone de una dirección IP pública.

---

Artículos relacionados

- [Configurar WireGuard Server en un router GL.iNet](../interface_guide/wireguard_server.md)
- [Configurar OpenVPN Server en un router GL.iNet](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
