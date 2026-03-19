# Data Statistics

Data Statistics ofrece un panel inteligente de análisis de tráfico que categoriza y visualiza el uso de la red por aplicaciones, ayudándole a supervisar el tráfico en tiempo real e histórico para mejorar la visibilidad y el control de la red.

**Nota**:

1. Esta función está disponible actualmente solo en **GL-MT5000 (Brume 3)**.

2. Esta función no puede trabajar junto con Network Acceleration. Al habilitarla, Network Acceleration se desactivará automáticamente para garantizar un funcionamiento correcto.

---

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** > **Data Statistics**.

Active el interruptor en la esquina superior derecha para ver **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: Muestra un gráfico de tendencia basado en el tiempo, por ejemplo, del último día, para mostrar el consumo de ancho de banda de las 10 aplicaciones principales durante el periodo seleccionado.

  Cambie la línea temporal entre Past Hour, Past Day y Past Week si es necesario.

- **App Traffic Statistics**: Muestra métricas detalladas de tráfico para cada aplicación, incluidos los datos de Download, Upload y Total Bandwidth.

  Busque aplicaciones específicas en la barra de búsqueda si es necesario.

## Reglas de almacenamiento de datos

1. Las estadísticas de tráfico se guardan en RAM cada 15 segundos y se almacenan en la memoria flash cada 1 hora. Se evitan escrituras frecuentes en la memoria flash para proteger su vida útil.

2. Un reinicio suave no provocará pérdida de datos. El sistema primero escribe los datos desde la RAM a la memoria flash antes de reiniciarse.

3. Un reinicio forzado, desconectar y volver a conectar la alimentación, o una actualización de firmware, conservando los ajustes, puede provocar una pérdida de datos de hasta la última hora.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
