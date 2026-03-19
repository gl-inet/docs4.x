# Tareas programadas

En el lado izquierdo del panel de administración web, vaya a **SYSTEM** -> **Scheduled Tasks**.

Scheduled Tasks le permite configurar programaciones diarias para operaciones básicas, como encender o apagar el LED, reiniciar el router, habilitar o deshabilitar el Wi-Fi y cambiar el nivel de potencia TX.

**Nota**: Sincronice primero la hora en [Time Zone](time_zone.md) antes de utilizar esta función. Si el dispositivo está apagado en la hora programada, la tarea no se ejecutará.

## Programación de la pantalla LED

Esta función le permite establecer una programación de encendido y apagado para la luz LED del router.

Cuando esté habilitada, establezca las horas de encendido y apagado, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![LED display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/led_display_schedule.png){class="glboxshadow gl-90-desktop"}

En los modelos con pantalla táctil, como el GL-BE3600 Slate 7, la programación de la pantalla LCD permite establecer un horario de encendido y apagado para la pantalla táctil.

![LCD display schedule](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/lcd_display_schedule.png){class="glboxshadow"}

## Reinicio programado

Esta función le permite establecer una programación para reiniciar automáticamente el router.

Cuando esté habilitada, establezca las horas de reinicio, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![Schedule Reboot](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/schedule_reboot.png){class="glboxshadow gl-90-desktop"}

## Programación del Wi-Fi

Esta función le permite configurar horarios del Wi-Fi según las bandas de frecuencia compatibles con su router, como 2.4 GHz, 5 GHz, 6 GHz y MLO Wi-Fi.

Excepto MLO Wi-Fi, que solo admite el modo de programación de encendido y apagado, todas las demás bandas de frecuencia Wi-Fi admiten dos modos de programación: Turn On/Off y Switch TX Power.

- **Turn On/Off**: Ayuda a equilibrar la comodidad de la conectividad y el ahorro energético habilitando o deshabilitando automáticamente la red inalámbrica en momentos concretos, por ejemplo apagándola durante las horas de sueño para reducir el consumo innecesario.

- **Switch TX Power**: Se refiere a ajustar automáticamente la potencia de transmisión inalámbrica, que determina la intensidad de la señal y la cobertura, en momentos concretos, equilibrando así el rendimiento y la eficiencia energética, por ejemplo reduciendo la potencia cuando el uso es bajo.

### Programación de MLO Wi-Fi

| Modelos compatibles   |     |
| :-------------------- | :-: |
| GL-E5800 (Mudi 7)     |  √  |
| GL-MT3600BE (Beryl 7) |  √  |
| GL-BE6500 (Flint 3e)  |  √  |
| GL-BE9300 (Flint 3)   |  √  |
| GL-BE3600 (Slate 7)   |  √  |

Puede establecer una programación de encendido y apagado tanto para el MLO Main Wi-Fi como para el Guest Wi-Fi.

Habilite la programación del Main o Guest Wi-Fi, establezca las horas de encendido y apagado, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![MLO Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/mlo_turn_on_off.png){class="glboxshadow"}

### Programación de Wi-Fi de 6 GHz

| Modelos compatibles |     |
| :------------------ | :-: |
| GL-E5800 (Mudi 7)   |  √  |
| GL-BE9300 (Flint 3) |  √  |

Cuando el modo de programación del Wi-Fi es **Turn On/Off**, puede establecer un horario de encendido y apagado tanto para el 6 GHz Main Wi-Fi como para el Guest Wi-Fi.

Habilite la programación del Main o Guest Wi-Fi, establezca las horas de encendido y apagado, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![6GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_turn_on_off.png){class="glboxshadow"}

Cuando el modo de programación del Wi-Fi es **Switch TX Power**, puede establecer una programación de cambio de potencia TX para el 6 GHz Main Wi-Fi. Tenga en cuenta que el 6 GHz Guest Wi-Fi no es compatible con este modo de programación.

Habilite la programación del Main Wi-Fi, establezca dos acciones temporizadas para cambiar la potencia TX, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![6GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/6g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Establece la potencia TX en un nivel determinado, por ejemplo Low, a una hora concreta, por ejemplo 22:00.
- **Restore**: Restaura la potencia TX a otro nivel, por ejemplo Max, en otra hora, por ejemplo 07:00.
- **days**: Selecciona los días efectivos de la semana para estos ajustes.

### Programación de Wi-Fi de 5 GHz

Cuando el modo de programación del Wi-Fi es **Turn On/Off**, puede establecer un horario de encendido y apagado tanto para el 5 GHz Main Wi-Fi como para el Guest Wi-Fi.

Habilite la programación del Main o Guest Wi-Fi, establezca las horas de encendido y apagado, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![5GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_turn_on_off.png){class="glboxshadow"}

Cuando el modo de programación del Wi-Fi es **Switch TX Power**, puede establecer una programación de cambio de potencia TX para el 5 GHz Main Wi-Fi. Tenga en cuenta que el 5 GHz Guest Wi-Fi no es compatible con este modo de programación.

Habilite la programación del Main Wi-Fi, establezca dos acciones temporizadas para cambiar la potencia TX, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![5GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/5g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Establece la potencia TX en un nivel determinado, por ejemplo Low, a una hora concreta, por ejemplo 22:00.
- **Restore**: Restaura la potencia TX a otro nivel, por ejemplo Max, en otra hora, por ejemplo 07:00.
- **days**: Selecciona los días efectivos de la semana para estos ajustes.

### Programación de Wi-Fi de 2.4 GHz

Cuando el modo de programación del Wi-Fi es **Turn On/Off**, puede establecer un horario de encendido y apagado tanto para el 2.4 GHz Main Wi-Fi como para el Guest Wi-Fi.

Habilite la programación del Main o Guest Wi-Fi, establezca las horas de encendido y apagado, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![2.4GHz Wi-Fi turn on/off](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_turn_on_off.png){class="glboxshadow"}

Cuando el modo de programación del Wi-Fi es **Switch TX Power**, puede establecer una programación de cambio de potencia TX para el 2.4 GHz Main Wi-Fi. Tenga en cuenta que el 2.4 GHz Guest Wi-Fi no es compatible con este modo de programación.

Habilite la programación del Main Wi-Fi, establezca dos acciones temporizadas para cambiar la potencia TX, seleccione los días de la semana en los que se aplicará y luego haga clic en Apply.

![2.4GHz Wi-Fi switch TX power](https://static.gl-inet.com/docs/router/en/4/tutorials/scheduled_tasks/2.4g_switch_tx_power.png){class="glboxshadow"}

- **Switch**: Establece la potencia TX en un nivel determinado, por ejemplo Low, a una hora concreta, por ejemplo 22:00.
- **Restore**: Restaura la potencia TX a otro nivel, por ejemplo Max, en otra hora, por ejemplo 07:00.
- **days**: Selecciona los días efectivos de la semana para estos ajustes.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
