# Ofuscación de AmneziaWG {#amneziawg-obfuscation}

AmneziaWG es un protocolo VPN basado en WireGuard con ofuscación de tráfico integrada. Sus parámetros de ofuscación controlan cómo se disfraza el tráfico para evadir la detección bajo inspección de red restrictiva.

A continuación se explica en detalle qué es AmneziaWG y en qué se diferencian sus versiones.

## ¿Por qué AmneziaWG? {#why-amneziawg}

El predecesor de AmneziaWG, WireGuard, se ha consolidado como un protocolo VPN rápido y fiable gracias a su base de código compacta y su alta eficiencia. Sin embargo, sus encabezados de paquetes fijos y sus tamaños de paquetes predecibles crean una firma fácilmente reconocible. Los sistemas DPI pueden identificar estos paquetes con facilidad y terminar las conexiones de inmediato, lo que representa un problema crítico en países con una censura de Internet estricta.

AmneziaWG conserva la simplicidad arquitectónica y el alto rendimiento de la implementación original de WireGuard, pero añade un módulo de ofuscación específico para ocultar los patrones del tráfico VPN. Esto ayuda tanto a usuarios particulares como empresariales a proteger su privacidad en línea y mantener conexiones estables en entornos de red restrictivos.

En resumen:

- Enmascara las características de la VPN para evitar la detección por parte de ISP, cortafuegos o inspección profunda de paquetes (DPI).
- Hace que su conexión VPN parezca tráfico web estándar, mejorando la estabilidad y la tasa de éxito en redes restringidas.

## AmneziaWG V2.0 {#amneziawg-v20}

### Descripción general {#amneziawg-v20-overview}

<font color="red">**Nota**: Los routers GL.iNet con el firmware v4.9.0 o posterior admiten AmneziaWG 2.0.</font>

AmneziaWG 2.0 conserva los mecanismos de ofuscación de v1.0: la secuencia de paquetes basura (**Jc**, **Jmin**, **Jmax**) y los prefijos aleatorios para los paquetes Init y Response (**S1–S2**). Añade los siguientes mecanismos para ocultar los elementos de la conexión que seguían siendo predecibles:

* **S3–S4**: prefijos aleatorios para los paquetes Cookie y Data. En v1.0 solo se añadía relleno a los paquetes Init y Response, por lo que los paquetes Cookie medían exactamente 64 bytes y los paquetes Data medían lo mismo que su carga útil.

* **H1–H4 como intervalos**: el valor del encabezado de cada tipo de paquete se elige dentro de un intervalo, en lugar de ser un número fijo. Al recibir el paquete, se acepta cualquier valor dentro del intervalo correspondiente. Los cuatro intervalos no deben solaparse.

* **I1–I5**: paquetes UDP definidos por el usuario que se envían antes de cada handshake. Así, la sesión comienza con tráfico similar al de un protocolo UDP habitual, en vez de con un handshake de WireGuard.

Estas mejoras hacen que el tráfico VPN sea más difícil de detectar y, al mismo tiempo, conservan la alta velocidad y la baja latencia de WireGuard.

!!! Tip "¿Cómo distinguir entre AmneziaWG 1.0 y 2.0?"

    **V1.0**: No hay parámetros S3-S4; H1-H4 son enteros fijos individuales.
    
    **V2.0**: Es V2.0 si se cumple cualquiera de las condiciones siguientes:
            
    - Incluye parámetros S3-S4
    - H1-H4 están configurados como rangos numéricos
    - Incluye parámetros I1-I5 personalizados.
            
    > Nota: I1-I5 no se generan automáticamente. Los usuarios pueden añadirlos manualmente como líneas adicionales en el archivo de configuración para que el tráfico de AmneziaWG se parezca a otros protocolos comunes, como QUIC o WebRTC.

### Parámetros {#amneziawg-v20-parameters}

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
| I1~I5 | Paquetes de firma para la imitación de protocolos | secuencia arbitraria de bytes en hexadecimal | N/A |

Ejemplo de una sección de ofuscación de v2.0:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1318795025-1318795156
H2 = 1029272944-1029273095
H3 = 966737016-966737098
H4 = 282229905-429495047
```

Referencias: [Documentación oficial de AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Descripción general {#amneziawg-v31-overview}

<font color="red">**Nota**: Los routers GL.iNet con el firmware v4.11.1 o posterior admiten AmneziaWG 3.1.</font>

AmneziaWG 3.1 conserva todos los mecanismos de ofuscación de v2.0: los prefijos aleatorios para cada tipo de paquete (**S1–S4**), los encabezados dinámicos (**H1–H4**), los paquetes de firma que preceden al handshake (**I1–I5**) y la secuencia de paquetes basura (**Jc**, **Jmin**, **Jmax**). También incorpora los siguientes mecanismos para dificultar la identificación del tráfico por sus patrones:

- **Protección de encabezados**: utiliza ChaCha20 para ocultar los campos de los encabezados de paquetes WireGuard que normalmente quedarían sin cifrar.
- **Relleno del contenido**: añade una cantidad aleatoria de relleno a los paquetes de datos de transporte, dentro del espacio que permite la MTU.
- **Temporización personalizada**: permite configurar valores o intervalos para la renovación de claves, los reintentos de handshake, los mensajes de mantenimiento de la conexión y otras operaciones relacionadas. Se recomienda utilizar los valores generados automáticamente tanto en el servidor como en el cliente.
- **Sufijos aleatorios**: añade sufijos de longitud variable a los paquetes de handshake y de datos de transporte para aumentar la variación en sus tamaños.
- **Desactivación de cookies**: permite que el dispositivo deje de enviar respuestas de cookie durante el handshake. El dispositivo sigue recibiendo esas respuestas y procesando el resto del handshake.

### Parámetros {#amneziawg-v31-parameters}

AmneziaWG V3.1 incorpora los siguientes parámetros.

| Parámetro | Descripción | Restricciones | Intervalo o valor de GL.iNet |
| --------- | ----------- | ------------- | ----------------------------- |
| `HeaderProtectionKey` | Activa la protección mediante ChaCha20 de los campos del encabezado que normalmente quedarían sin cifrar | Exactamente 32 bytes. Al activarla, se deben configurar S1, S2, S3 y S4, cada uno con un valor ≥ 12. Se recomienda la combinación `H1=1`, `H2=2`, `H3=3`, `H4=4`: se desactiva el mecanismo de encabezados personalizados y la protección de encabezados oculta el tipo de mensaje | Clave de 32 bytes |
| `ContentPaddingAddition` | Añade a cada paquete de datos de transporte una cantidad aleatoria de bytes dentro del intervalo configurado | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` desactiva esta función. | 0–65535 (ejemplo: `10-50`) |
| `RekeyAfterTime` | Tiempo de uso de la clave actual antes de que se inicie la renovación activa de la clave (segundos) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` utiliza el valor predeterminado de WireGuard | 100–150 (valor predeterminado de WireGuard: 120) |
| `RekeyTimeout` | Tiempo de espera de respuesta a una solicitud de handshake antes de reintentar (segundos) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` utiliza el valor predeterminado de WireGuard | 4–7 (valor predeterminado de WireGuard: 5) |
| `RejectAfterTime` | Tiempo que puede transcurrir sin recibir datos antes de iniciar un nuevo handshake (segundos) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` utiliza el valor predeterminado de WireGuard | 180–240 (valor predeterminado de WireGuard: 180) |
| `KeepaliveTimeout` | Tiempo que puede transcurrir sin enviar datos antes de enviar un mensaje interno de mantenimiento de la conexión (segundos) | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` utiliza el valor predeterminado de WireGuard | 8–20 (valor predeterminado de WireGuard: 10) |
| `MaxHandshakeAttempts` | Número máximo de reintentos de handshake | `range<uint16>`, 0–65535, min ≤ max; `0` o `0-0` utiliza el valor predeterminado de WireGuard | 12–18 (valor predeterminado de WireGuard: 18) |
| `RandomTrailers` | Añade una cantidad variable de bytes al final de los paquetes: datos aleatorios en los paquetes de handshake y ceros después del paquete IP interno en los paquetes de transporte. La longitud del sufijo se elige de forma dinámica para respetar la MTU de ambos extremos | `off` desactiva esta función. Si la activa, se recomienda `S1 = S2 = S3 = S4` para reducir el riesgo de identificar incorrectamente el tipo de paquete debido a la variación aleatoria de su tamaño | `on` / `off` |
| `DisableCookies` | Impide que el dispositivo local envíe respuestas de cookie durante el handshake. La recepción de esas respuestas del par remoto y el resto del procesamiento del handshake no se ven afectados | `off` desactiva esta función. S3/H3 deben conservar valores válidos, ya que aún pueden utilizarse al recibir paquetes | `on` / `off` |

**Notas**

* Puede dejar que el router genere los valores de los intervalos de la última columna. `RandomTrailers` y `DisableCookies` se activan o desactivan por dispositivo.
* `HeaderProtectionKey` debe ser idéntica en el cliente y en el servidor.
* Durante el funcionamiento, cualquier valor de temporización fuera del intervalo indicado se sustituye por un valor aleatorio dentro del intervalo. Por tanto, puede que no se aplique el valor personalizado tal como se introdujo.
* `ContentPaddingAddition` y `S4` modifican la longitud de los paquetes de transporte, pero actúan en partes diferentes de cada paquete y pueden utilizarse al mismo tiempo.
* La protección de encabezados también admite valores dinámicos para `H1–H4`, aunque la configuración recomendada es `1/2/3/4`.

---

Ejemplo de una sección de ofuscación de v3.1:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

Referencias: [Documentación oficial de AmneziaWG](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Artículo relacionado:

- [Cómo configurar la ofuscación VPN en routers GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
