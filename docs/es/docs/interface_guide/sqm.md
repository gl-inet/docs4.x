# SQM (Smart Queue Management)

**Nota**: Esta función se introdujo en el firmware v4.9.

Algunos modelos, como Mango 2 (GL-MG1300), no admiten SQM por falta de memoria, incluso con firmware v4.9 o posterior.

---

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **SQM**.

SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el bufferbloat, lo que ayuda a que los juegos y las llamadas de voz sean más fluidos.

**Nota**:

1. Esta función solo afecta al tráfico que pasa por el router cuando opera como puerta de enlace, incluido el tráfico de los clientes locales y el tráfico del cliente VPN. No se aplica al tráfico entrante cuando el router actúa como servidor VPN.

2. Como SQM consume bastantes recursos, funciona mejor en redes con poco ancho de banda o congestionadas. Habilitarlo en conexiones de alta velocidad puede reducir el rendimiento máximo.
3. SQM no surtirá efecto cuando el router esté en modo Drop-in Gateway.
4. SQM y QoS no pueden habilitarse al mismo tiempo.
5. SQM no puede funcionar con Network Acceleration. Al habilitar SQM, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.

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


## Para firmware v4.11 y versiones posteriores

Active el interruptor para habilitar SQM y complete la configuración siguiendo estos pasos.

![sqm v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm_v4.11.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Introduzca manualmente las velocidades de subida y bajada de la WAN (rango: 1 - 10000), o haga clic en **Run Speedtest** para medirlas y rellenar los campos automáticamente. La prueba de velocidad requiere una conexión a Internet activa.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/wan_bandwidth.png){class="glboxshadow" width=600}

    **Nota**: Los valores introducidos están en **Mbps** (megabits por segundo). El equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

2. **Queue Discipline**

    Seleccione una regla de cola para gestionar el tráfico y reducir la latencia cuando la red esté sometida a carga.

    ![queue discipline](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/queue_discipline.png){class="glboxshadow" width=600}

    - **cake**: modelado de tráfico inteligente y automático con un mejor control general de la latencia (recomendado).

        Al seleccionar **cake** como disciplina de cola, **Cake Autorate** está disponible como función opcional.

        Cake Autorate es un modelador basado en la latencia que reduce o aumenta el ancho de banda de CAKE en tiempo real según el RTT de las sondas. No realiza pruebas de velocidad activas; solo utiliza pings ligeros. Se recomienda cuando el ancho de banda WAN fluctúa y no es necesario en enlaces estables.

        ![cake autorate](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/cake_autorate.png){class="glboxshadow" width=600}

        **Nota**: Cake Autorate genera tráfico continuo de sondeo en segundo plano. Tenga en cuenta este consumo adicional de datos si utiliza una conexión de uso medido.

        Los ajustes predeterminados son adecuados para la mayoría de las conexiones. Modifique los parámetros siguientes únicamente si comprende cómo afectan a Cake Autorate. Si es necesario, haga clic en **Reset to Default** para restaurar los valores predeterminados de sondeo y umbral.

        ![Probe & threshold parameters](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/probe_threshold_parameters.png){class="glboxshadow" width=600}

        - **Probe Server Addresses**: lista de direcciones IP separadas por comas que se utilizan para sondear la calidad de la red.

        - **Probe Interval**: los intervalos más cortos permiten responder con mayor rapidez, pero consumen más recursos de CPU.

        - **Concurrent Probes**: el número de sondas simultáneas no debe superar el número de servidores de sondeo; los valores más altos aumentan la carga de la CPU.

        - **Idle Detection Threshold**: cuando la velocidad de transferencia cae por debajo de este valor, la conexión se considera inactiva. Este valor no debe superar el 25 % del límite de velocidad configurado.

        - **Download Latency Threshold**: cuando la latencia de descarga supera este umbral, se reduce el ancho de banda.

        - **Upload Latency Threshold**: cuando la latencia de subida supera este umbral, se reduce el ancho de banda.

    - **fq_codel**: encolado justo simple y eficiente con una reducción básica de la latencia.

## Para firmware v4.9 a v4.10

Active el interruptor para habilitar SQM y defina las velocidades máximas de subida y bajada (rango de entrada: 1 - 10000) para la programación del tráfico. Ajústelas al ancho de banda real de su conexión a Internet para obtener los mejores resultados.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Nota**: Los valores introducidos en el campo están en **Mbps** (megabits por segundo). El valor equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Para **Queue Rule**, hay dos opciones disponibles:

- **cake**: modelado de tráfico inteligente y automático con un mejor control global de la latencia (recomendado).

- **fq_codel**: encolado justo simple y eficiente con reducción básica de la latencia.

!!! Tip

    Una diferencia entre los ajustes de QoS y SQM es que QoS permite establecer las prioridades de las aplicaciones y el router asigna el ancho de banda en consecuencia, mientras que SQM permite seleccionar una regla de cola.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
