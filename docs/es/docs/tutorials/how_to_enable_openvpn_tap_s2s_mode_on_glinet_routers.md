# Cómo habilitar el modo OpenVPN TAP-S2S en routers GL.iNet

## Escenarios de uso

Después de habilitar el modo TAP-S2S, el dispositivo cliente OpenVPN puede acceder remotamente al dispositivo servidor OpenVPN, y el dispositivo servidor OpenVPN también puede acceder remotamente al dispositivo cliente OpenVPN. Sin embargo, la desventaja es que, después de habilitar el modo TAP-S2S, las reglas VPN configuradas en el propio cliente OpenVPN dejarán de surtir efecto.

## TAP-S2S frente a modo TUN

Topología de red

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}
![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}
TAP-S2S y TUN usan el mismo método de conexión física, pero sus métodos de conexión lógica son diferentes. Estas son las diferencias:

1. Cuando los dispositivos del lado LAN del GL-X3000 acceden al panel de administración del GL-MT6000, el modo TAP-S2S no utiliza una IP virtual, mientras que el modo TUN sí.
2. Cuando los dispositivos del lado LAN del GL-X3000 acceden al panel de administración del GL-X3000, el modo TAP-S2S utiliza una IP virtual, mientras que el modo TUN no.
3. Cuando un dispositivo del lado LAN del GL-X3000 conoce la dirección IP de un dispositivo del lado LAN del GL-MT6000, el modo TAP-S2S permite el acceso remoto directo, mientras que el modo TUN no puede acceder directamente sin habilitar ajustes adicionales.
4. En modo TAP-S2S, el GL-X3000 necesita pasar por el GL-MT6000 para acceder a Internet, mientras que en modo TUN el GL-X3000 puede acceder directamente a Internet. Por ello, en modo TAP-S2S las reglas VPN configuradas en el GL-X3000 no surten efecto y deben seguirse las reglas VPN configuradas en el GL-MT6000.

## Tutoriales

Primero, use un router con IP pública, por ejemplo un GL-MT6000, para abrir **OpenVPN Server**, configurar el modo del dispositivo como **TAP-S2S**, hacer clic en **Apply** y luego en **Export Client Configuration**.
![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}
![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}
Además, use otro router, por ejemplo un GL-X3000, para abrir **OpenVPN Client**, importar el archivo de configuración descargado en los pasos anteriores, hacer clic en **Apply** y luego habilitar la función.
![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}
![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}
En ese momento, la dirección IP del router GL-X3000 cambiará. Puede iniciar sesión en el panel de administración del GL-MT6000, abrir **Clients** y encontrar la nueva dirección IP del GL-X3000.
![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}
Si el GL-MT6000 pierde la conexión de red o desactiva **OpenVPN Server**, o si el GL-X3000 desactiva **OpenVPN Client**, la dirección IP del GL-X3000 se restaurará.

Puntos a tener en cuenta:

- Ambos dispositivos deben actualizarse a la versión v4.5; de lo contrario, no podrán conectarse.
- TAP-S2S solo funciona con **Global Proxy Mode**; se ajustará automáticamente cuando OpenVPN esté activado.
- Después de habilitar esta función, no podrán usarse las siguientes funciones: **VPN server**, **Adguard Home**, **Parental Control**, **ZeroTier**, **Tailscale**, **Tor**, **Firewall**, **Multi-WAN**, **LAN**, **DNS**, **Network Mode**, **IPv6**, **MAC Address**, **Drop-in Gateway**, **IGMP Snooping**, etc.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
