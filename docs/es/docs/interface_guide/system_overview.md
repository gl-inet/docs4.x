# Resumen del sistema

En el lado izquierdo del panel de administración web, vaya a **SYSTEM** -> **Overview**.

La página Overview muestra el estado de algunos componentes de hardware y admite algunos controles sencillos, entre ellos los siguientes:

- Estado de la CPU, la memoria, la memoria flash y los dispositivos de almacenamiento externo.
- Estado de componentes de hardware como el ventilador, la batería, etc.
- Control de los LED y del ventilador.
- Información del dispositivo.

Aquí se muestra un ejemplo del GL-MT3000.

![system overview](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/overview.png){class="glboxshadow"}

## Carga media de la CPU

En la mayoría de los modelos sin ventilador, la carga media de la CPU se muestra como se indica a continuación.

![system overview, cpu average load, no fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

En algunos modelos con ventilador integrado, la carga media de la CPU se muestra como se indica a continuación.

![system overview, cpu average load, with fan](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Pase el cursor sobre el gráfico para mostrar valores concretos.

Haga clic en la temperatura de la derecha para alternar entre Celsius y Fahrenheit.

Haga clic en el icono del ventilador, situado en la esquina superior derecha, para acceder a Fan Settings.

![system overview, fan settings](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Modelos con ventiladores integrados"

    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Uso de memoria

Pase el cursor sobre el gráfico para mostrar valores concretos.

**Nota**: La memoria que se muestra aquí es la memoria disponible para el sistema Linux. La memoria total será inferior a la memoria física porque parte de ella se asigna al subsistema Wi-Fi o a otras áreas de arranque.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## LED

Al hacer clic en el icono de engranaje, irá a [Scheduled Tasks](scheduled_tasks.md) del LED.

![system overview, memory usage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Flash

Muestra la memoria flash total, incluida la utilizada por el sistema, la utilizada por las aplicaciones y la disponible restante.

![system overview, flash](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/flash.png){class="glboxshadow"}

## Información del dispositivo

Esta sección muestra la información básica del dispositivo.

Device ID, device MAC y device S/N se añadieron en el firmware v4.7 y versiones posteriores.

![system overview, device info](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Almacenamiento externo

Esta sección, disponible desde la versión v4.5, muestra la capacidad total y disponible del disco USB.

Algunos modelos con firmware v4.7 y versiones posteriores admiten el cambio del protocolo USB.

![system overview, external storage](https://static.gl-inet.com/docs/router/en/4/tutorials/system_overview/external_storage.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
