# QoS (Quality of Service)

QoS (Quality of Service) optimiza la asignación del ancho de banda priorizando actividades críticas, como videollamadas y juegos, durante la congestión de la red, lo que reduce la latencia y mejora el rendimiento general.

**Nota**:

1. Esta función solo afecta al tráfico que pasa por el router cuando opera como puerta de enlace, incluido el tráfico de los clientes locales y el tráfico del cliente VPN. No se aplica al tráfico entrante cuando el router actúa como servidor VPN.
2. QoS no surtirá efecto cuando el router esté en modo Drop-in Gateway.
3. QoS y SQM no pueden habilitarse al mismo tiempo.
4. QoS no puede funcionar con Network Acceleration. Al habilitar QoS, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.

## Modelos compatibles

!!! note "Modelos compatibles"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Nota: Los modelos marcados con ※ admiten QoS a partir del firmware v4.9.

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **QoS**.

Active el interruptor para habilitar QoS y la página se mostrará como en la imagen siguiente.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Defina las velocidades máximas de subida y bajada (rango de entrada: 1 - 10000) para la programación del tráfico. Ajústelas al ancho de banda real de su conexión a Internet para obtener los mejores resultados.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Nota**: Los valores introducidos en el campo están en **Mbps** (megabits por segundo). El valor equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

Después, establezca prioridades para las distintas aplicaciones. El router asignará el ancho de banda en consecuencia.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## Personalizar la prioridad de las aplicaciones

Para personalizar la prioridad de las aplicaciones, seleccione **Customize** y haga clic en **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

En la ventana emergente, todas las categorías están configuradas con prioridad media por defecto.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Arrastre las categorías para ajustar su prioridad según sea necesario y haga clic en **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
