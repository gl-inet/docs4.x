# Content Filter

Content Filter es una función de seguridad inteligente en línea basada en clasificación DPI. Bloquea automáticamente sitios web dañinos o maliciosos para mantener la red limpia y segura, y también permite crear reglas personalizadas para bloquear aplicaciones, dominios o direcciones IP concretos.

## Modelos compatibles

!!! note "Modelos compatibles"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **Content Filter**.

Active el interruptor en la esquina superior derecha, personalice el contenido bloqueado (como aplicaciones, dominios o direcciones IP) y haga clic en **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Esta página consta de dos partes:

- **Blocked Apps List**: esta sección incluye tres categorías preseleccionadas: Gambling, Adult y Malware. Cuando están habilitadas, se bloquearán los sitios web, servicios o aplicaciones relacionados con estas tres categorías.

    También puede hacer clic en **Edit App** para añadir más categorías, como Game o Social Media, según sus necesidades.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    En la ventana emergente, seleccione las categorías que desea bloquear. Las tres categorías predeterminadas están vacías; todas las demás categorías incluyen una lista de aplicaciones.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Haga clic en cualquier categoría para ver y seleccionar las aplicaciones que desea bloquear, o haga clic en **Select All** en la parte superior derecha para bloquear todas las aplicaciones de esa categoría de una sola vez. Después, haga clic en **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

    Después verá las aplicaciones seleccionadas en la **Blocked App List**.

- **Blocked Domain / IP List**: esta sección permite introducir manualmente dominios concretos (por ejemplo, `google.com`), rangos CIDR (por ejemplo, `192.168.8.0/24`) o direcciones IP (por ejemplo, `192.168.10.10`) para bloquear el acceso a ellos. La lista admite hasta 10000 entradas.

    Introduzca los dominios o direcciones IP que desea bloquear y haga clic en **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Prueba de Content Filter

Por ejemplo, hemos seleccionado la categoría **Game**, que incluye Nintendo.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

En un portátil conectado a su router, el sitio `nintendo.com` ya no se puede abrir, aunque antes de habilitar Content Filter sí era accesible.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

En el panel de administración web del router podrá ver el número de solicitudes de acceso que se han bloqueado.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
