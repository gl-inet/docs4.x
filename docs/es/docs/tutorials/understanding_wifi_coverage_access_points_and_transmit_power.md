---
title: Comprender la cobertura Wi-Fi, los puntos de acceso y la potencia de transmisión
---

# Comprender la cobertura Wi-Fi, los puntos de acceso y la potencia de transmisión

Muchos usuarios suponen que aumentar la potencia de transmisión de un router siempre mejora la cobertura y el rendimiento Wi-Fi.

Aunque una mayor potencia de transmisión suele aumentar la cobertura de un solo router, la potencia máxima no siempre es ideal en redes con varios puntos de acceso (AP), nodos mesh o implementaciones Wi-Fi empresariales.

Comprender las celdas de cobertura, el roaming, la planificación de canales y la potencia de transmisión puede ayudar a mejorar el rendimiento inalámbrico.

## Router único frente a varios puntos de acceso

### Router único

Si solo tiene un router proporcionando cobertura Wi-Fi:

- Una mayor potencia de transmisión suele aumentar la cobertura.
- Los dispositivos cliente pueden mantener una conexión utilizable a mayor distancia.
- Reducir la potencia de transmisión normalmente disminuye la señal recibida y la relación señal-ruido (SNR) de bajada.

Para la mayoría de los usuarios con un solo router, se recomienda dejar la potencia de transmisión en su ajuste predeterminado o automático.

Reducir la potencia de transmisión de su router no reduce la energía de RF transmitida por redes Wi-Fi vecinas. Sus routers y AP siguen transmitiendo con la misma potencia.

### Varios puntos de acceso

Cuando se despliegan varios AP, el objetivo no es necesariamente maximizar el área de cobertura de cada AP.

En su lugar, el objetivo es crear varias celdas de cobertura más pequeñas y bien definidas que se solapen solo lo suficiente para proporcionar cobertura continua y roaming fiable.

La ubicación adecuada de los AP, la potencia de transmisión y la selección de canales son importantes.

## Solapamiento de celdas de cobertura

Si cada AP transmite a potencia máxima, sus áreas de cobertura pueden solaparse en exceso.

Un dispositivo cliente puede permanecer conectado a un AP lejano incluso cuando un AP más cercano proporciona una señal más fuerte. Esto se conoce habitualmente como **sticky client**.

Un cliente conectado al AP incorrecto puede experimentar:

- SNR más baja
- Tasas de modulación y codificación más bajas
- Más retransmisiones
- Menor rendimiento
- Mayor latencia

Reducir la potencia de transmisión de los AP puede reducir el tamaño de las celdas de cobertura y animar a los dispositivos cliente a hacer roaming antes.

## Comprender el roaming de clientes

En la mayoría de las redes Wi-Fi, el dispositivo cliente decide cuándo hacer roaming.

El router o AP puede proporcionar asistencia de roaming, pero el teléfono, portátil, tableta u otro cliente normalmente toma la decisión final de abandonar un AP y conectarse a otro.

Los distintos dispositivos cliente utilizan diferentes umbrales y algoritmos de roaming. Por lo tanto, un dispositivo puede permanecer conectado a un AP mientras considere que la conexión es utilizable, incluso cuando otro AP ofrezca una señal más fuerte.

Reducir el solapamiento excesivo de cobertura puede ayudar a los clientes a tomar mejores decisiones de roaming.

## Reutilización espacial

Wi-Fi es un medio compartido.

Antes de transmitir, los dispositivos Wi-Fi escuchan para determinar si el canal ya está en uso. Si los AP que usan el mismo canal pueden oírse entre sí en un área amplia, pueden pasar más tiempo esperando a que el canal esté disponible.

Esto reduce el tiempo de aire utilizable y el rendimiento general.

Reducir adecuadamente la potencia de transmisión puede permitir que AP que usan el mismo canal en distintas áreas físicas funcionen de forma más independiente. Esto se conoce como **reutilización espacial**.

La reutilización espacial no significa que reducir la potencia de transmisión de su AP disminuya la interferencia transmitida por redes vecinas. En cambio, unas celdas de cobertura del tamaño adecuado pueden reducir la contención innecesaria y permitir reutilizar el mismo canal en áreas suficientemente separadas.

## Planificación de canales

La potencia de transmisión y la selección de canales deben considerarse conjuntamente.

### 2,4 GHz

La banda de 2,4 GHz tiene relativamente pocos canales sin solapamiento.

En muchas regiones regulatorias, los canales 1, 6 y 11 se usan habitualmente con un ancho de canal de 20 MHz.

Siempre que sea posible, los AP cercanos deben usar canales diferentes que no se solapen.

### 5 GHz y 6 GHz

Las bandas de 5 GHz y 6 GHz proporcionan más canales disponibles, lo que facilita asignar canales diferentes a AP cercanos.

El uso de canales no solapados reduce la contención cocanal, aunque el solapamiento excesivo de cobertura todavía puede afectar al comportamiento de roaming.

Los canales disponibles dependen del modelo del router, el país o región, el ancho de canal y la normativa local.

## AP cableados y redes mesh

### Puntos de acceso cableados

Una conexión Ethernet cableada entre el router principal y los AP adicionales suele ser la implementación preferida.

Como la conexión cableada transporta el tráfico de backhaul, la potencia de transmisión Wi-Fi puede ajustarse principalmente para la cobertura de clientes, el roaming y la reutilización espacial.

### Mesh con backhaul cableado

Los nodos mesh que usan backhaul cableado pueden optimizarse de forma similar a los AP cableados.

La potencia de transmisión puede ajustarse para reducir el solapamiento excesivo de celdas manteniendo al mismo tiempo una cobertura continua.

### Mesh con backhaul inalámbrico

En una implementación mesh inalámbrica, las radios Wi-Fi también pueden transportar tráfico entre nodos mesh.

Reducir la potencia de transmisión de forma demasiado agresiva puede debilitar la conexión de backhaul inalámbrica y reducir el rendimiento general.

Al usar backhaul inalámbrico, asegúrese de que los nodos mesh mantengan una conexión fuerte y estable entre sí.

## Ejemplo de implementación multi-AP

Considere dos routers GL.iNet conectados por Ethernet:

- El router principal proporciona servicios de enrutamiento, DHCP, NAT y firewall.
- El segundo router funciona en modo Access Point.
- Ambos dispositivos emiten el mismo nombre de red Wi-Fi y los mismos ajustes de seguridad.
- Los AP cercanos usan canales diferentes que no se solapan.
- La potencia de transmisión se ajusta para que las celdas de cobertura se solapen lo suficiente para el roaming, pero no en exceso.

La potencia de transmisión ideal depende de los materiales de construcción, la ubicación de los AP, los dispositivos cliente, las redes Wi-Fi vecinas y el área de cobertura deseada.

No existe un único valor de potencia de transmisión correcto para todas las implementaciones.

## Conceptos erróneos comunes

### La potencia máxima siempre proporciona el mejor Wi-Fi

La potencia máxima suele proporcionar el área de cobertura más grande, pero puede crear solapamiento excesivo y un mal comportamiento de roaming en implementaciones multi-AP.

### Reducir la potencia de transmisión reduce la interferencia entrante

Reducir la potencia de transmisión de su AP disminuye la señal generada por su propio AP. No reduce la potencia transmitida por routers o AP vecinos.

### Reducir la potencia de transmisión hace que el receptor del AP sea más sensible

La potencia de transmisión y la sensibilidad del receptor son características independientes. Reducir la potencia de transmisión no mejora por sí mismo la capacidad del AP para recibir transmisiones de clientes.

### Los dispositivos cliente siempre se conectan al AP más cercano

Los dispositivos cliente normalmente seleccionan AP y hacen roaming entre ellos usando sus propios algoritmos internos. Pueden permanecer conectados a un AP más lejano incluso cuando hay un AP más cercano disponible.

## Puntos de partida recomendados

| Implementación | Recomendación |
| --- | --- |
| Router único | Deje la potencia de transmisión en su ajuste predeterminado o automático. |
| Dos o más AP cableados | Use canales no solapados y ajuste la potencia de transmisión para reducir el solapamiento excesivo. |
| Mesh con backhaul cableado | Optimice las celdas de cobertura para un roaming fiable. |
| Mesh con backhaul inalámbrico | Evite reducir la potencia lo suficiente como para debilitar la conexión de backhaul. |

Después de realizar cambios, pruebe el rendimiento en varias ubicaciones y verifique:

- Intensidad de señal
- Rendimiento de subida y bajada
- Latencia
- Roaming entre AP
- Calidad del backhaul inalámbrico, si corresponde

Cambie un ajuste cada vez para poder medir con precisión su efecto.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com) o [contáctenos](https://www.gl-inet.com/contact-us/).
