# Firmware v4.11 {#firmware-v411}

Esta versión se centra en mejorar la supervisión de la calidad de la red y la evaluación de la seguridad, para ayudarle a identificar problemas de conectividad y posibles riesgos de seguridad. También mejora DNS, QoS, SQM y las estadísticas de datos para ofrecer una gestión de red y un control del tráfico más flexibles.

Obtenga el firmware más reciente en el [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Calidad de la red {#network-quality}

[Network Quality](../interface_guide/network_quality.md) es una nueva función que supervisa su conexión a Internet en tiempo real. Evalúa la capacidad de respuesta, la latencia y el rendimiento del DNS, y detecta cortes de conexión y pérdida de paquetes. Esto ayuda a identificar la inestabilidad de la red y los problemas de conectividad que las pruebas de ancho de banda por sí solas pueden no revelar.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Análisis de seguridad {#security-scan}

[Security Scan](../interface_guide/security_scan.md) es una nueva función que evalúa los ajustes de seguridad del router y proporciona una puntuación de seguridad, alertas de riesgo y sugerencias de optimización. Comprueba aspectos como la seguridad Wi-Fi, el ping desde la WAN, el acceso SSH remoto, el reenvío de puertos y la protección de contenido mediante DPI, para ayudarle a identificar y resolver posibles riesgos de seguridad. El análisis se inicia automáticamente al abrir la página. También puede hacer clic en el icono de la puntuación para restablecer el análisis y ejecutarlo de nuevo.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

[UPnP](../interface_guide/upnp.md) permite que los dispositivos LAN y aplicaciones compatibles soliciten asignaciones de puertos automáticamente sin configurar el reenvío de puertos manualmente. Esto simplifica la conectividad para juegos en línea, intercambio de archivos entre pares y acceso remoto. En la página UPnP puede ver las asignaciones activas, comprobar el tiempo de concesión restante y eliminarlas según sea necesario.

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

Esta versión mejora la configuración de [DNS](../interface_guide/dns_v4.11.md) al reunir WAN DNS, VPN DNS y Manual DNS en una sola página. Puede consultar fácilmente el estado de DNS de cada tipo de conexión, configurar servidores DNS personalizados y elegir si los ajustes manuales de DNS se aplican a los túneles VPN o al propio router.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

[QoS](../interface_guide/qos.md) (Quality of Service) ofrece la opción **Run Speedtest** para el ancho de banda WAN, que mide las velocidades de descarga y subida y rellena automáticamente los campos correspondientes. Además de Application Priority, esta versión incorpora dos políticas de planificación: **Device Priority** y **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Los clientes locales seleccionados reciben una mayor prioridad de red cuando hay congestión en la WAN.

- **Application Priority**: Defina prioridades personalizadas para distintas aplicaciones y el router asignará el ancho de banda en consecuencia.

- **Advanced QoS**: Cree reglas avanzadas de QoS para el tráfico de alta prioridad.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) ofrece la opción **Run Speedtest** para el ancho de banda WAN, que mide las velocidades de descarga y subida y rellena automáticamente los campos correspondientes. Hay dos disciplinas de colas disponibles: **cake** y **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake**: Modelado de tráfico inteligente y automático con el mejor control global de la latencia (recomendado).

    Para esta disciplina de colas, la nueva función **Cake Autorate** ajusta dinámicamente el ancho de banda configurado en función del RTT de las sondas. Utiliza consultas ping de bajo consumo de recursos en lugar de pruebas activas de velocidad y se recomienda para conexiones WAN con ancho de banda variable.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel**: Colas equitativas sencillas y eficientes con una reducción básica de la latencia.

## Estadísticas de datos {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) ahora permite filtrar el tráfico por cliente e incorpora nuevas vistas de gráficos, incluidos gráficos de barras y circulares. Al consultar App Traffic Statistics, puede seleccionar un cliente específico y cambiar entre las vistas de gráficos para analizar con mayor claridad el uso del tráfico.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
