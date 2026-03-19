# Aceleración de red

La aceleración de red reduce la carga de la CPU y acelera el reenvío de paquetes de tráfico, pero puede entrar en conflicto con algunas funciones.

Cuando la aceleración de red está habilitada, las siguientes funciones no funcionarán correctamente: la velocidad del cliente y las estadísticas de tráfico, y el límite de velocidad del cliente.

## Modelos compatibles

??? "Modelos compatibles" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-MT3000 (Beryl AX) - GL-MT2500/GL-MT2500A (Brume 2) - GL-SFT1200 (Opal) - GL-MT1300 (Beryl)

??? "Modelos no compatibles" - GL-AXT1800 (Slate AX) - GL-AX1800 (Flint) - GL-A1300 (Slate Plus) - GL-E750/E750V2 (Mudi) - GL-X750/GL-X750V2 (Spitz) - GL-AR750S (Slate) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-X300B (Collie)

## Configuración

En el lado izquierdo del panel de administración web, vaya a **NETWORK** -> **Network Acceleration**.

![Aceleración de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Hay tres modos.

- **Auto**

  El modo Auto cambiará automáticamente entre los dos modos de aceleración según el uso real.

- **Hardware Acceleration**

  La aceleración por hardware funciona con <u>Ethernet</u> y <u>Repeater</u>.

  La aceleración por hardware descarga tareas de red de alta frecuencia, como NAT, el reenvío de paquetes y la verificación de suma de comprobación, en hardware dedicado como NPU o chips HWNAT. Funciona específicamente con conexiones Ethernet (WAN/LAN por cable) y Repeater, y destaca en estos escenarios con rutas fijas y reglas sencillas para ofrecer alto rendimiento, baja latencia y una carga mínima de CPU en la transmisión de datos a velocidad de línea.

- **Software Acceleration**

  La aceleración por software funciona con <u>Cellular</u>.

  La aceleración por software se basa en la CPU general del router junto con kernels o controladores optimizados, como SWNAT. Funciona con acceso Cellular (4G/5G), normalmente el escenario principal en el que la aceleración por hardware no está disponible, y ofrece una gran compatibilidad y soporte para protocolos complejos. Aunque es flexible, puede alcanzar cuellos de botella en la CPU bajo cargas de gran ancho de banda, especialmente al ejecutar funciones avanzadas como DPI, QoS o el reenvío de puertos.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
