# Data Statistics

**Nota**: Esta función se introdujo en el firmware v4.9. Algunos modelos, como Mango 2 (GL-MG1300), no admiten Data Statistics debido a que no disponen de memoria suficiente, aunque ejecuten el firmware v4.9 o posterior.

---

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **Data Statistics**.

Data Statistics ofrece un panel intuitivo de tráfico que identifica el uso de la red por aplicación y protocolo. Permite consultar tendencias históricas de 1 hora, 1 día y 7 días, muestra clasificaciones de uso, supervisa el tráfico por dispositivo y permite bloquear aplicaciones no deseadas con un solo clic.

**Nota**:

1. Data Statistics no surtirá efecto cuando el router esté en modo Drop-in Gateway.
2. Data Statistics no puede funcionar con Network Acceleration. Al habilitar Data Statistics, Network Acceleration se desactivará automáticamente para garantizar un rendimiento estable.
3. Data Statistics solo registra el uso del tráfico de los dispositivos que aparecen en la página **Clients**. Si un dispositivo se conecta al router mediante una interfaz de túnel (por ejemplo, VPN Client, Tailscale o AstroWarp), el tráfico originado en ese dispositivo y reenviado a través del router no se incluye en estas estadísticas.

## Para firmware v4.11 y versiones posteriores

Active el interruptor en la esquina superior derecha para ver **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Esta página consta de dos partes:

- **Top 10 Apps by Bandwidth Usage**: muestra un gráfico de tendencia temporal (por ejemplo, del último día) con el consumo de ancho de banda de las 10 aplicaciones principales durante el periodo seleccionado.

    Pase el ratón sobre el gráfico para ver el uso de datos de las 10 aplicaciones que más ancho de banda consumen en un momento determinado.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: muestra métricas detalladas de tráfico para cada aplicación, incluidos Download, Upload y Total Bandwidth. Si es necesario, busque aplicaciones concretas en la barra de búsqueda.

    Haga clic en la flecha de ordenación junto al encabezado de la columna para ordenar la lista de forma ascendente o descendente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Reglas de almacenamiento de datos

1. Las estadísticas de tráfico se guardan en RAM cada 15 segundos y en la memoria flash cada hora. Se evitan las escrituras frecuentes en la memoria flash para proteger su vida útil.

2. Un reinicio suave no provoca la pérdida de datos. Antes de reiniciarse, el sistema escribe los datos de la RAM en la memoria flash.

3. Un reinicio forzado (desconectar y volver a conectar la alimentación) o una actualización del firmware que conserve los ajustes puede provocar la pérdida de los datos de hasta la última hora.

### Selector de clientes

El selector de clientes permite seleccionar un cliente concreto o mantener la opción predeterminada **All clients**. El gráfico y la tabla de estadísticas se actualizan automáticamente para mostrar solo los datos de tráfico del dispositivo seleccionado.

**Nota**: Esta función se introdujo en el firmware v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Cambiar la vista del gráfico

Al consultar **App Traffic Statistics**, puede cambiar el tipo de gráfico según sus necesidades.

**Nota**: Esta función se introdujo en el firmware v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: muestra el uso del ancho de banda durante el intervalo seleccionado. Las curvas continuas permiten observar la evolución del tráfico y detectar fácilmente tendencias ascendentes o descendentes.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: compara el uso del ancho de banda de las aplicaciones. Las barras permiten identificar rápidamente qué aplicaciones consumen más ancho de banda.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: desglosa el uso total del ancho de banda en porcentajes. Cada sector representa la proporción relativa de tráfico consumida por una aplicación.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Cambiar el intervalo de tiempo

Puede cambiar el intervalo entre **Past hour**, **Past day** y **Past week** según lo necesite.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

El intervalo elegido determina cómo se muestran los datos:

- **Para una vista detallada (por ejemplo, Past Hour)**: el gráfico muestra fluctuaciones detalladas en tiempo real. Los picos son más altos y las caídas más pronunciadas, lo que facilita detectar aumentos repentinos del uso del ancho de banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **Para una visión general (por ejemplo, Past Day o Past Week)**: el gráfico condensa los datos en una línea temporal más larga. Las curvas se suavizan y muestran la tendencia general del tráfico en lugar de cada pequeña variación.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Borrar estadísticas

Haga clic en el icono de la escoba de la esquina superior izquierda para borrar las estadísticas cuando lo necesite.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Después de borrarlas, la página se actualizará como se muestra a continuación. Es posible que deba esperar un momento para que comiencen a cargarse nuevas estadísticas.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Para firmware v4.9 a v4.10

Active el interruptor en la esquina superior derecha para ver **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Esta página consta de dos partes:

- **Top 10 Apps by Bandwidth Usage**: muestra un gráfico de tendencia basado en el tiempo (por ejemplo, del último día) para reflejar el consumo de ancho de banda de las 10 aplicaciones principales durante el periodo seleccionado.

    Pase el ratón sobre el gráfico para ver el uso de datos de las 10 aplicaciones que más ancho de banda consumen en un momento concreto.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: muestra métricas detalladas de tráfico para cada aplicación, incluidos Download, Upload y Total Bandwidth. Si lo necesita, puede buscar aplicaciones concretas en la barra de búsqueda.

    Haga clic en la flecha de ordenación situada junto al encabezado de cada columna para ordenar la lista de forma ascendente o descendente.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Reglas de almacenamiento de datos

1. Las estadísticas de tráfico se guardan en RAM cada 15 segundos y se almacenan en la memoria flash cada 1 hora. Se evitan escrituras frecuentes en la memoria flash para proteger su vida útil.

2. Un reinicio suave no provocará pérdida de datos. El sistema primero escribe los datos desde la RAM a la memoria flash antes de reiniciarse.

3. Un reinicio forzado (desconectar y volver a conectar la alimentación) o una actualización de firmware (conservando los ajustes) puede provocar una pérdida de datos de hasta la hora más reciente.

### Cambiar el intervalo de tiempo

Puede cambiar el intervalo entre **Past Hour**, **Past Day** y **Past Week** según lo necesite.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

El intervalo elegido determina cómo se muestran los datos:

- **Para una vista detallada (por ejemplo, Past Hour)**: el gráfico muestra fluctuaciones finas en tiempo real. Los picos son más altos y las caídas más pronunciadas, lo que facilita detectar aumentos repentinos en el uso de ancho de banda.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Para una visión general amplia (por ejemplo, Past Day o Past Week)**: el gráfico condensa los datos en una línea temporal más larga. Las curvas se vuelven más suaves y muestran la tendencia general del tráfico en lugar de cada pequeño cambio.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Borrar estadísticas

Haga clic en el icono de la escoba en la esquina superior izquierda para borrar las estadísticas cuando lo necesite.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Después de borrarlas, la página se actualizará como se muestra a continuación. Es posible que tenga que esperar un momento para que empiecen a cargarse las nuevas estadísticas.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
