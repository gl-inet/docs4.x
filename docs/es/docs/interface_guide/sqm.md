# SQM (Smart Queue Management)

SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el bufferbloat, lo que ayuda a que los juegos y las llamadas de voz sean más fluidos.

**Nota**:

1. Esta función solo afecta al tráfico que pasa por el router cuando opera como puerta de enlace, incluido el tráfico de los clientes locales y el tráfico del cliente VPN. No se aplica al tráfico entrante cuando el router actúa como servidor VPN.

2. Como SQM consume bastantes recursos, funciona mejor en redes con poco ancho de banda o congestionadas. Habilitarlo en conexiones de alta velocidad puede reducir el rendimiento máximo.
3. SQM no surtirá efecto cuando el router esté en modo Drop-in Gateway.
4. SQM y QoS no pueden habilitarse al mismo tiempo.
5. SQM no puede funcionar con Network Acceleration. Al habilitar SQM, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.

## Modelos compatibles

!!! note "Modelos compatibles"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Nota: Los modelos marcados con ※ admiten SQM a partir del firmware v4.9.

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **SQM**.

Active el interruptor para habilitar SQM y defina las velocidades máximas de subida y bajada (rango de entrada: 1 - 10000) para la programación del tráfico. Ajústelas al ancho de banda real de su conexión a Internet para obtener los mejores resultados.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

**Nota**: Los valores introducidos en el campo están en **Mbps** (megabits por segundo). El valor equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

![up down speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/up_down_speed.jpg){class="glboxshadow"}

Para **Queue Rule**, hay dos opciones disponibles:

- **cake**: modelado de tráfico inteligente y automático con un mejor control global de la latencia (recomendado).

- **fq_codel**: encolado justo simple y eficiente con reducción básica de la latencia.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
