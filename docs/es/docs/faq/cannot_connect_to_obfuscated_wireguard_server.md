# No se puede conectar a un servidor WireGuard ofuscado

La ofuscación de VPN es una técnica que disfraza el tráfico VPN para que parezca tráfico normal de Internet. Actualmente, algunos routers GL.iNet admiten el protocolo AmneziaWG, lo que permite configurar un servidor WireGuard con ofuscación de tráfico habilitada.

Si no puede establecer una conexión con un servidor WireGuard ofuscado, siga los pasos siguientes para solucionar el problema.

1. **Asegúrese de que la configuración de WireGuard importada en cada cliente sea exclusiva.**

    Cada cliente necesita un archivo de configuración de peer exclusivo. Compartir una misma configuración entre varios clientes provocará fallos de conexión.

    Si es necesario, vaya a **VPN** -> **WireGuard Server** -> **Profiles** para ver los perfiles exportados.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Asegúrese de que el cliente pueda verificar los parámetros de ofuscación.**

    El protocolo AmneziaWG es retrocompatible. Si su servidor WireGuard solo admite AmneziaWG v1.0, el archivo de configuración seguirá pasando la verificación al importarse en un cliente compatible con v2.0.
        
    Sin embargo, si el archivo de configuración incluye parámetros de ofuscación de AmneziaWG v2.0, asegúrese de que el cliente WireGuard admita AmneziaWG v2.0. De lo contrario, la verificación de parámetros podría fallar.

    !!! tip "¿Cómo identificar la versión de AmneziaWG?"

        **V1.0**: No hay parámetros S3-S4; H1-H4 son enteros fijos individuales.
        
        **V2.0**: Es V2.0 si se cumple cualquiera de las condiciones siguientes:
        
        - Incluye parámetros S3-S4
        - H1-H4 están configurados como rangos numéricos
        - Incluye parámetros I1-I5 personalizados.
        
        > Nota: I1-I5 no se generan automáticamente. Los usuarios pueden añadirlos manualmente como líneas adicionales en el archivo de configuración para que el tráfico de AmneziaWG se parezca a otros protocolos comunes, como QUIC o WebRTC.

    Si el cliente WireGuard es un router GL.iNet, compruebe su versión de AmneziaWG con los dos métodos siguientes.

    ??? note "Comprobar desde el Router Web Admin Panel"

        1. Inicie sesión en el Web Admin Panel del router.

        2. Vaya a **VPN** -> **WireGuard Server** -> **Configuration** y compruebe los parámetros de ofuscación. Si la configuración incluye **S3-S4** y **H1-H4** como rangos variables, en lugar de valores fijos, el router ejecuta AmneziaWG 2.0, como se muestra abajo.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            De lo contrario, usa AmneziaWG 1.0, como se muestra abajo.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Comprobar mediante comando SSH"

        1. Inicie sesión en el router por SSH.

        2. Ejecute `opkg list|grep awg` y compruebe el sufijo del paquete **kmod-amneziawg** en la salida. Si aparece marcado con **2.0**, el router admite AmneziaWG 2.0, como se muestra abajo.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            De lo contrario, ejecuta AmneziaWG 1.0, como se muestra abajo.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Ajuste los parámetros de ofuscación.**

    Si ha configurado manualmente [parámetros de ofuscación](amneziawg_obfuscation.md#parameter-overview), como Jc, Jmin o Jmax, en el servidor WireGuard, una configuración incorrecta puede provocar fallos de handshake.

    Pruebe a modificar estos parámetros de ofuscación y vuelva a conectarse para descartar problemas de discrepancia de parámetros. También puede restaurar los ajustes de ofuscación predeterminados para hacer pruebas.

4. **Pruebe la conexión con la app oficial AmneziaWG.**

    Realice una prueba comparativa: instale la app oficial AmneziaWG, importe en ella el archivo de configuración original exportado por el servidor e intente conectarse.

    - Si la conexión funciona en la app oficial, el archivo de configuración es válido. El problema puede estar en el dispositivo cliente original. Compruebe su conectividad de red o contacte con soporte para recibir ayuda.

    - Si la conexión sigue fallando, el problema se origina en la configuración del servidor del router. Compruebe los ajustes del servidor y los parámetros de ofuscación.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
