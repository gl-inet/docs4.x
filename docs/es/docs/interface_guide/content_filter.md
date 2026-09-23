# Content Filter

**Nota**: Esta función se introdujo en el firmware v4.9.

Algunos modelos, como Mango 2 (GL-MG1300), no admiten Content Filter por falta de memoria, incluso con firmware v4.9 o posterior. Consulte [Modelos compatibles](#supported-models) para obtener más información.

---

Content Filter es una función de seguridad inteligente en línea basada en clasificación DPI. Bloquea automáticamente sitios web dañinos o maliciosos para mantener la red limpia y segura, y también permite crear reglas personalizadas para bloquear aplicaciones, dominios o direcciones IP concretos.

**Nota**:

1. Content Filter no surtirá efecto cuando el router esté en modo Drop-in Gateway.
2. Content Filter no puede funcionar con Network Acceleration. Al habilitar Content Filter, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.

## Modelos compatibles {#supported-models}

??? "Modelos compatibles"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Modelos no compatibles"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)


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
