# Parámetros de ofuscación de AmneziaWG

AmneziaWG es un protocolo VPN basado en WireGuard con ofuscación de tráfico integrada. Sus parámetros de ofuscación controlan cómo se disfraza el tráfico para evitar la detección por controles de red estrictos. A continuación se ofrece un desglose detallado de las diferencias de versión de AmneziaWG, los parámetros de ofuscación, sus restricciones y la configuración recomendada.

## AmneziaWG V2.0

En comparación con AmneziaWG v1.0, la versión 2.0 proporciona una ofuscación más potente al añadir nuevos parámetros (**S3~S4**) y utilizar encabezados dinámicos para los tipos de paquetes (**H1~H4** como rangos en lugar de valores fijos). Además, AmneziaWG 2.0 admite los parámetros **I1~I5**, que envían paquetes UDP formateados antes de cada handshake para disfrazar el tráfico de AmneziaWG como tráfico normal no VPN, lo que permite evitar eficazmente la inspección profunda de paquetes y mejorar la conectividad en redes restringidas.

Estas mejoras hacen que el tráfico VPN sea más difícil de detectar y, al mismo tiempo, conservan la alta velocidad y la baja latencia de WireGuard.

Así puede identificar la versión de AmneziaWG:

- **V1.0**: No hay parámetros S3~S4; H1~H4 son enteros fijos individuales.
- **V2.0**: Incluye los parámetros **S3~S4**; **H1~H4** se definen como rangos numéricos; admite los parámetros **I1~I5**.

**Nota**: Los parámetros I1-I5 no se generan automáticamente. Los usuarios pueden añadirlos manualmente como líneas extra en el archivo de configuración VPN para que el tráfico de AmneziaWG se parezca a otros protocolos comunes, como QUIC o WebRTC.

## Resumen de parámetros {#parameter-overview}

| Parámetro | Descripción | Restricciones | Generado automáticamente |
| --------- | ----------- | ------------- | ------------------------ |
| Jc | Número de paquetes basura antes de que el cliente inicie el handshake (para interferir con la detección de características del tráfico) | 1~128 | 4~12 |
| Jmin | Tamaño mínimo de los paquetes basura aleatorios (bytes); debe configurarse junto con Jmax para definir el tamaño de los paquetes basura | 0 ≤ Jmin < Jmax < 65535 | 0 <= jmin < jmax < 1280 |
| Jmax | Tamaño máximo de los paquetes basura aleatorios | 0 ≤ Jmin < Jmax < 65535 | 0≤ Jmin < Jmax < 1280 |
| S1 | Prefijos aleatorios para paquetes Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Prefijos aleatorios para paquetes Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Prefijos aleatorios para paquetes Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Prefijos aleatorios para paquetes Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | Encabezados dinámicos para tipos de paquetes; valores aleatorios (v1.0) o rangos (v2.0) | 5~2147483647; H1, H2, H3 y H4 deben ser diferentes | 5~2147483647 |
| I1~I5 | Paquetes de firma para la imitación de protocolos | blob hex arbitrario | N/A |

Referencias: [Documentación oficial de AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
