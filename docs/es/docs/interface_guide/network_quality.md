# Calidad de la red

**Nota**: Esta función se incorporó en el firmware v4.11.

---

En el menú lateral izquierdo del panel de administración web, vaya a **FLOW CONTROL** -> **Network Quality**.

El panel Network Quality supervisa la calidad de la conexión a Internet en tiempo real. Evalúa la capacidad de respuesta, la latencia y el rendimiento de DNS, a la vez que detecta interrupciones de la conexión y pérdida de paquetes. Estas métricas ayudan a identificar problemas de estabilidad y conectividad que una prueba de ancho de banda por sí sola podría no revelar.

En esta página puede evaluar su conexión a Internet mediante Network Quality Score y ejecutar pruebas de velocidad locales cuando sea necesario.

**Nota**:

1. La puntuación general GL.iNet Network Quality Score se calcula mediante la fórmula ponderada:

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest es una prueba de velocidad local ejecutada en el router y está sujeta a las reglas de limitación de velocidad de funciones como SQM y QoS.

## Network Quality Score

Esta sección muestra la puntuación general Network Quality Score, calculada a partir de Response Score y Reliable Score. Puede consultar cada puntuación por separado. El panel también muestra métricas relacionadas, como latencia, fluctuación y pérdida de paquetes, además de las tasas de descarga y carga en tiempo real en KB/s. De forma predeterminada, el panel utiliza `google.com` como destino para comprobar la conectividad a Internet y la resolución DNS.

Haga clic en el icono de ajustes para configurar los destinos de las pruebas.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Puede seleccionar destinos de prueba para Internet Reachability y DNS Resolution, entre ellos Baidu, Tencent, Alibaba, Google, Microsoft o Cloudflare. También puede introducir manualmente un dominio personalizado.

Los destinos configurados se utilizan para realizar pruebas de conectividad y DNS y calcular Network Quality Score.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: Se utiliza para comprobar la conectividad a Internet y medir la latencia de extremo a extremo (destino de ping Hop2).

- **DNS Resolution Target**: El dominio que se resuelve durante las consultas DNS. Se consultan tanto los registros A (IPv4) como AAAA (IPv6).

## Speedtest

Esta prueba de velocidad integrada utiliza Cloudflare Speed Test para medir las velocidades de descarga y carga, la latencia del ping y el bufferbloat. Durante la prueba se muestran gráficos de velocidad en tiempo real.

Haga clic en **Run Speedtest** para iniciar la prueba.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Cuando finalice la prueba, la página mostrará los resultados.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
