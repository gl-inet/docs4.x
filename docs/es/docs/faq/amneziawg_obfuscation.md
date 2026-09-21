# Ofuscación de AmneziaWG

AmneziaWG es un protocolo VPN basado en WireGuard con ofuscación de tráfico integrada. Sus parámetros de ofuscación controlan cómo se disfraza el tráfico para evadir la detección bajo inspección de red restrictiva.

A continuación se ofrece una introducción detallada a AmneziaWG, las diferencias entre versiones, su uso en routers GL.iNet y un resumen de los parámetros.

## ¿Por qué AmneziaWG?

El predecesor de AmneziaWG, WireGuard, se ha consolidado como un protocolo VPN rápido y fiable gracias a su base de código compacta y su alta eficiencia. Sin embargo, sus encabezados de paquetes fijos y sus tamaños de paquetes predecibles crean una firma fácilmente reconocible. Los sistemas DPI pueden identificar estos paquetes con facilidad y terminar las conexiones de inmediato, lo que representa un problema crítico en países con una censura de Internet estricta.

AmneziaWG conserva la simplicidad arquitectónica y el alto rendimiento de la implementación original de WireGuard, pero añade un módulo de ofuscación específico para ocultar los patrones del tráfico VPN. Esto ayuda tanto a usuarios particulares como empresariales a proteger su privacidad en línea y mantener conexiones estables en entornos de red restrictivos.

En resumen:

- Enmascara las características de la VPN para evitar la detección por parte de ISP, cortafuegos o inspección profunda de paquetes (DPI).
- Hace que su conexión VPN parezca tráfico web estándar, mejorando la estabilidad y la tasa de éxito en redes restringidas.

## AmneziaWG V2.0

En comparación con AmneziaWG v1.0, la versión 2.0 proporciona una ofuscación más potente al añadir nuevos parámetros (**S3~S4**) y utilizar encabezados dinámicos para los tipos de paquetes (**H1~H4** como rangos en lugar de valores fijos). Además, AmneziaWG 2.0 admite los parámetros **I1~I5**, que envían paquetes UDP formateados antes de cada handshake para disfrazar el tráfico de AmneziaWG como tráfico normal no VPN, lo que permite evitar eficazmente la inspección profunda de paquetes y mejorar la conectividad en redes restringidas.

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

Estas mejoras hacen que el tráfico VPN sea más difícil de detectar y, al mismo tiempo, conservan la alta velocidad y la baja latencia de WireGuard.

!!! Tip "¿Cómo identificar la versión de AmneziaWG?"

    **V1.0**: No hay parámetros S3-S4; H1-H4 son enteros fijos individuales.
    
    **V2.0**: Es V2.0 si se cumple cualquiera de las condiciones siguientes:
            
    - Incluye parámetros S3-S4
    - H1-H4 están configurados como rangos numéricos
    - Incluye parámetros I1-I5 personalizados.
            
    > Nota: I1-I5 no se generan automáticamente. Los usuarios pueden añadirlos manualmente como líneas adicionales en el archivo de configuración para que el tráfico de AmneziaWG se parezca a otros protocolos comunes, como QUIC o WebRTC.

## Modelos compatibles

AmneziaWG 2.0 está disponible en routers GL.iNet con el firmware v4.9 o posterior.

Para configurar la ofuscación VPN en routers GL.iNet, consulte [esta guía](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md).

## Resumen de parámetros

| Parámetro | Descripción | Restricciones | Generado automáticamente |
| --------- | ----------- | ------------- | ------------------------ |
| Jc | Número de paquetes basura antes de que el cliente inicie el handshake (para interferir con la detección de características del tráfico) | 1~128 | 4~12 |
| Jmin | Tamaño mínimo de los paquetes basura aleatorios (bytes); debe configurarse junto con Jmax para definir el tamaño de los paquetes basura | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax | Tamaño máximo de los paquetes basura aleatorios | 0 ≤ Jmin < Jmax < 1280 | 0≤ Jmin < Jmax < 1280 |
| S1 | Prefijos aleatorios para paquetes Init | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Prefijos aleatorios para paquetes Response | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Prefijos aleatorios para paquetes Cookie | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Prefijos aleatorios para paquetes Data | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | Encabezados dinámicos para tipos de paquetes; valores aleatorios (v1.0) o rangos (v2.0) | 5~2147483647; H1, H2, H3 y H4 deben ser diferentes | 5~2147483647 |
| I1~I5 | Paquetes de firma para la imitación de protocolos | blob hex arbitrario | N/A |

Referencias: [Documentación oficial de AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Artículo relacionado:

- [Cómo configurar la ofuscación VPN en routers GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
