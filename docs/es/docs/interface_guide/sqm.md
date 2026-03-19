# SQM (Smart Queue Management)

SQM (Smart Queue Management) gestiona de forma inteligente el tráfico de red del router para minimizar la latencia y el bufferbloat, lo que ayuda a que los juegos y las llamadas de voz sean más fluidos.

**Nota**:

1. Esta función actualmente solo está disponible en **GL-MT5000 (Brume 3)**.

2. Esta función afecta al tráfico que pasa por el router cuando actúa como puerta de enlace, incluido el tráfico de clientes locales y el tráfico del cliente VPN, pero no al tráfico entrante cuando el router actúa como servidor VPN.

3. Como SQM consume bastantes recursos, funciona mejor en redes con poco ancho de banda o congestionadas. Habilitarlo en conexiones de alta velocidad puede reducir el rendimiento máximo.

---

En el lado izquierdo del panel de administración web, vaya a **FLOW CONTROL** > > **SQM**.

Primero, establezca sus velocidades máximas de carga y descarga para la programación del tráfico, con un rango de entrada de 1 a 10000. Ajústelas al ancho de banda real de su conexión a Internet para obtener los mejores resultados.

![sqm](https://static.gl-inet.com/docs/router/en/4/interface_guide/sqm/sqm.png){class="glboxshadow"}

Para Queue Rule, hay dos opciones disponibles:

- **cake**: Modelado de tráfico inteligente y automático con un mejor control global de la latencia, recomendado.

- **fq_codel**: Encolado justo simple y eficiente con reducción básica de la latencia.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
