# DPI Engine

**Nota**: Esta función se introdujo en el firmware v4.9.

Algunos modelos, como Mango 2 (GL-MG1300), no admiten DPI Engine por falta de memoria, incluso con firmware v4.9 o posterior. Consulte [Modelos compatibles](#supported-models) para obtener más información.

---

La DPI (Deep Packet Inspection) es una tecnología central para la gestión inteligente de redes. A diferencia de los routers tradicionales, que solo identifican las direcciones de origen y destino, la DPI analiza en profundidad la carga útil de los paquetes e identifica con precisión aplicaciones y sitios web mediante una biblioteca de coincidencia de firmas, lo que permite una clasificación y un control del tráfico mucho más detallados.

El motor DPI de GL.iNet se ejecuta localmente en su router para ofrecer una gestión inteligente de la red con total privacidad. Proporciona acceso completo a estadísticas de tráfico, filtrado de contenido y QoS para un control integral del tráfico.

Integrado con [Netify](https://www.netify.ai/){target="_blank"}, el DPI de GL.iNet adopta un complemento integrado ligero para un despliegue eficiente. Gracias a la base de datos de firmas de Netify, actualizada en línea, permite una gestión fiable y hace que el control de red sea más preciso y eficiente.

**Nota**:

1. Cuando el router está en modo Drop-in Gateway, las funciones DPI (incluyendo Data Statistics, Content Filter y QoS) y SQM no surtirán efecto.

2. Cuando la DPI está habilitada, Network Acceleration se desactiva automáticamente para garantizar un rendimiento estable.

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

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **DPI Engine** y haga clic en **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

En la ventana emergente, lea y acepte los **Terms of Service & Privacy Policy**, y después haga clic en **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Espere mientras el router realiza las operaciones del sistema. Desactivará Network Acceleration y habilitará Data Statistics y Content Filter.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Una vez activado, haga clic en **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Se le dirigirá al **DPI Engine Version Center**, donde podrá ver la versión del programa DPI y la versión de la base de datos.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Nota**: Esta página solo muestra indicadores del estado del sistema principal. El procesamiento del tráfico comenzará cuando habilite las funciones correspondientes.

## Actualización de la base de datos

Si hay una versión más reciente de la base de datos disponible, solo tiene que hacer clic en **Upgrade** para actualizarla.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
