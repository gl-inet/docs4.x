# Firmware v4.11

Esta versión se centra en mejorar la supervisión de la calidad de la red y la evaluación de la seguridad, para ayudarle a identificar problemas de conectividad y posibles riesgos de seguridad. También incorpora nuevas funciones de Mesh, GL.iNet Account y VLAN, además de mejoras importantes en DNS, SQM, QoS y las estadísticas de tráfico.

Obtenga el firmware más reciente en el [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Calidad de la red

[Network Quality](../interface_guide/network_quality.md) es una nueva función que supervisa su conexión a Internet en tiempo real. Evalúa la capacidad de respuesta, la latencia y el rendimiento del DNS, y detecta cortes de conexión y pérdida de paquetes. Esto ayuda a identificar la inestabilidad de la red y los problemas de conectividad que las pruebas de ancho de banda por sí solas pueden no revelar.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Análisis de seguridad

[Security Scan](../interface_guide/security_scan.md) es una nueva función que evalúa los ajustes de seguridad del router y proporciona una puntuación de seguridad, alertas de riesgo y sugerencias de optimización. Comprueba aspectos como la seguridad Wi-Fi, el ping desde la WAN, el acceso SSH remoto, el reenvío de puertos y la protección de contenido mediante DPI, para ayudarle a identificar y resolver posibles riesgos de seguridad. El análisis se inicia automáticamente al abrir la página. También puede hacer clic en el icono de la puntuación para restablecer el análisis y ejecutarlo de nuevo.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md) es una función basada en el estándar Wi-Fi EasyMesh™ que amplía la cobertura Wi-Fi en todo el hogar y permite una itinerancia fluida. Si dispone de varios routers GL.iNet, configure uno como router principal y los demás como nodos de malla para disfrutar de una itinerancia Wi-Fi sin interrupciones por su hogar.

**Nota**: Esta función se publicó inicialmente para determinados modelos y se amplió a más modelos en la versión de firmware 4.11.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## Cuenta de GL.iNet

Una [GL.iNet Account](../interface_guide/glinet_account.md) proporciona acceso unificado a sus dispositivos y servicios en la nube. Con una sola cuenta de GL.iNet, puede acceder a GoodCloud y a la GL.iNet App para gestionar la red y los dispositivos con mayor comodidad. Además, puede usar GoodPAS para establecer rápidamente una conexión segura entre su router de viaje y su red doméstica, lo que permite un acceso remoto fluido cuando está fuera de casa.

**Nota**: Esta función se publicó inicialmente para determinados modelos y se amplió a más modelos en la versión de firmware 4.11.

![gli.net account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md) es una solución de acceso remoto basada en el protocolo AmneziaWG con ofuscación de tráfico integrada. Permite conectar de forma segura su router de viaje a su red doméstica mediante un código de acceso dinámico, sin necesidad de registrarse ni iniciar sesión.

**Nota**: Esta función se publicó inicialmente para determinados modelos y se amplió a más modelos en la versión de firmware 4.11.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md) permite el acceso remoto y la gestión centralizada de los routers GL.iNet. Puede gestionar dispositivos por lotes, desplegar configuraciones de red, actualizar el firmware y acceder remotamente al panel de administración web o al terminal SSH del router.

**Nota**: Esta función se publicó inicialmente para determinados modelos y se amplió a más modelos en la versión de firmware 4.11.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Puerto Ethernet

La página [Ethernet Port](../interface_guide/ethernet_port_v4.10.md) muestra todas las interfaces del router. Puede consultar el estado de conexión de cada interfaz, gestionar las funciones de los puertos Ethernet (WAN o LAN) y ver detalles como la dirección MAC, la velocidad negociada y el estado actual del enlace. Además, puede asignar interfaces físicas a cualquiera de las subredes que haya creado.

**Nota**: Esta función se publicó inicialmente para determinados modelos y se amplió a más modelos en la versión de firmware 4.11.

La siguiente imagen muestra Ethernet Port en el Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

Esta versión mejora la configuración de [DNS](../interface_guide/dns_v4.11.md) al reunir WAN DNS, VPN DNS y Manual DNS en una sola página. Puede consultar fácilmente el estado de DNS de cada tipo de conexión, configurar servidores DNS personalizados y elegir si los ajustes manuales de DNS se aplican a los túneles VPN o al propio router.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

[QoS](../interface_guide/qos.md) (Quality of Service) se ha mejorado en este firmware. Se incorpora la opción **Run Speedtest** para el ancho de banda WAN, que mide el ancho de banda de descarga y subida de la WAN y rellena automáticamente los campos correspondientes. Hay tres políticas de planificación disponibles, incluidas las nuevas **Device Priority** y **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority**: Los clientes locales seleccionados reciben una mayor prioridad de red cuando hay congestión en la WAN.

- **Application Priority**: Defina prioridades personalizadas para distintas aplicaciones y el router asignará el ancho de banda en consecuencia.

- **Advanced QoS**: Cree reglas avanzadas de QoS para el tráfico de alta prioridad.

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) ofrece la opción **Run Speedtest** para el ancho de banda WAN, que mide las velocidades de descarga y subida y rellena automáticamente los campos correspondientes. Para la disciplina de colas **cake**, la nueva función **Cake Autorate** ajusta dinámicamente el ancho de banda configurado en función del RTT de las sondas. Utiliza consultas ping de bajo consumo de recursos en lugar de pruebas activas de velocidad y se recomienda para conexiones WAN con ancho de banda variable.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## Estadísticas de datos

[Data Statistics](../interface_guide/data_statistics.md) ahora permite filtrar el tráfico por cliente e incorpora nuevas vistas de gráficos, incluidos gráficos de barras y circulares. Al consultar App Traffic Statistics, puede seleccionar un cliente específico y cambiar entre las vistas de gráficos para analizar con mayor claridad el uso del tráfico.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
