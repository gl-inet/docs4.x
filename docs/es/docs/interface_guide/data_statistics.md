# Data Statistics

Data Statistics ofrece un panel intuitivo de tráfico que identifica el uso de la red por aplicación y protocolo. Permite consultar tendencias históricas de 1 hora, 1 día y 7 días, muestra clasificaciones de uso, supervisa el tráfico por dispositivo y permite bloquear aplicaciones no deseadas con un solo clic.

**Nota**: Esta función no puede trabajar junto con Network Acceleration. Al habilitarla, Network Acceleration se desactivará automáticamente para garantizar un funcionamiento correcto.

## Modelos compatibles

!!! note "Modelos compatibles"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **Data Statistics**.

Active el interruptor en la esquina superior derecha para ver **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Esta página consta de dos partes:

- **Top 10 Apps by Bandwidth Usage**: muestra un gráfico de tendencia basado en el tiempo (por ejemplo, del último día) para reflejar el consumo de ancho de banda de las 10 aplicaciones principales durante el periodo seleccionado.

    Pase el ratón sobre el gráfico para ver el uso de datos de las 10 aplicaciones que más ancho de banda consumen en un momento concreto.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: muestra métricas detalladas de tráfico para cada aplicación, incluidos Download, Upload y Total Bandwidth. Si lo necesita, puede buscar aplicaciones concretas en la barra de búsqueda.

    Haga clic en la flecha de ordenación situada junto al encabezado de cada columna para ordenar la lista de forma ascendente o descendente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Reglas de almacenamiento de datos

1. Las estadísticas de tráfico se guardan en RAM cada 15 segundos y se almacenan en la memoria flash cada 1 hora. Se evitan escrituras frecuentes en la memoria flash para proteger su vida útil.

2. Un reinicio suave no provocará pérdida de datos. El sistema primero escribe los datos desde la RAM a la memoria flash antes de reiniciarse.

3. Un reinicio forzado (desconectar y volver a conectar la alimentación) o una actualización de firmware (conservando los ajustes) puede provocar una pérdida de datos de hasta la hora más reciente.

## Cambiar el intervalo de tiempo

Puede cambiar el intervalo entre **Past Hour**, **Past Day** y **Past Week** según lo necesite.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

El intervalo elegido determina cómo se muestran los datos:

- **Para una vista detallada (por ejemplo, Past Hour)**: el gráfico muestra fluctuaciones finas en tiempo real. Los picos son más altos y las caídas más pronunciadas, lo que facilita detectar aumentos repentinos en el uso de ancho de banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Para una visión general amplia (por ejemplo, Past Day o Past Week)**: el gráfico condensa los datos en una línea temporal más larga. Las curvas se vuelven más suaves y muestran la tendencia general del tráfico en lugar de cada pequeño cambio.

    ![past day](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_day.png){class="glboxshadow"}

## Borrar estadísticas

Haga clic en el icono de la escoba en la esquina superior izquierda para borrar las estadísticas cuando lo necesite.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Después de borrarlas, la página se actualizará como se muestra a continuación. Es posible que tenga que esperar un momento para que empiecen a cargarse las nuevas estadísticas.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
