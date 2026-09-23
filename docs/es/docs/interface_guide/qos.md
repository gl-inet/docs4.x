# QoS (Quality of Service)

**Nota**: Esta función se introdujo en el firmware v4.9.

Algunos modelos, como Mango 2 (GL-MG1300), no admiten QoS por falta de memoria, incluso con firmware v4.9 o posterior. Consulte [Modelos compatibles](#supported-models) para obtener más información.

---

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) optimiza la asignación del ancho de banda priorizando actividades críticas, como videollamadas y juegos, durante la congestión de la red, lo que reduce la latencia y mejora el rendimiento general.

**Nota**:

1. Esta función solo afecta al tráfico que pasa por el router cuando opera como puerta de enlace, incluido el tráfico de los clientes locales y el tráfico del cliente VPN. No se aplica al tráfico entrante cuando el router actúa como servidor VPN.
2. QoS no surtirá efecto cuando el router esté en modo Drop-in Gateway.
3. QoS y SQM no pueden habilitarse al mismo tiempo.
4. QoS no puede funcionar con Network Acceleration. Al habilitar QoS, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.

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

Active el interruptor para habilitar QoS y complete la configuración siguiendo los pasos que se indican a continuación.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Introduzca manualmente las velocidades de subida y bajada de la WAN (rango: 1 - 10000), o haga clic en **Run Speedtest** para medirlas y rellenar los campos automáticamente. La prueba de velocidad requiere una conexión a Internet activa.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Nota**: Los valores introducidos están en **Mbps** (megabits por segundo). El equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

2. **Scheduling Policy**

    Puede seleccionar un modo de política. Las reglas avanzadas tienen prioridad sobre la política básica para el tráfico coincidente.

    - **Device Priority**

        En este modo, los clientes locales seleccionados reciben una mayor prioridad de red cuando la conexión WAN está congestionada. Haga clic en **Add Device** y seleccione los dispositivos que deben recibir prioridad de ancho de banda cuando la WAN esté sometida a una carga elevada.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Puede buscar dispositivos por nombre de cliente, dirección MAC o dirección IP. Seleccione los dispositivos y haga clic en **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        En este modo puede definir prioridades para distintas aplicaciones. El router asignará el ancho de banda en consecuencia.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Para personalizar la prioridad de las aplicaciones, seleccione **Customize** y haga clic en **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        En la ventana emergente, todas las categorías tienen prioridad media de forma predeterminada.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Arrastre las categorías para ajustar su prioridad y haga clic en **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        En este modo puede crear reglas avanzadas de QoS para el tráfico de alta prioridad. Haga clic en **Add Rule** para definir reglas basadas en el protocolo, el puerto y la IP de origen.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Especifique Name, Protocol, Source Address y Destination Port y haga clic en **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Para firmware v4.9 a v4.10

Active el interruptor para habilitar QoS y la página se mostrará como en la imagen siguiente.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Defina las velocidades máximas de subida y bajada (rango de entrada: 1 - 10000) para la programación del tráfico. Ajústelas al ancho de banda real de su conexión a Internet para obtener los mejores resultados.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Nota**: Los valores introducidos en el campo están en **Mbps** (megabits por segundo). El valor equivalente en **MB/s** (megabytes por segundo) se muestra como referencia.

Después, establezca prioridades para las distintas aplicaciones. El router asignará el ancho de banda en consecuencia.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Para personalizar la prioridad de las aplicaciones, seleccione **Customize** y haga clic en **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

En la ventana emergente, todas las categorías están configuradas con prioridad media por defecto.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Arrastre las categorías para ajustar su prioridad según sea necesario y haga clic en **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
