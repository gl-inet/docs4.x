# Aviso del problema y soluciones para el fallo de funcionamiento con tarjetas SIM EE en GL-X3000/GL-XE3000/GL-X2000

Estimados clientes de GL.iNet:

Recientemente hemos detectado que algunos clientes experimentan fallos de conectividad en los modelos GL-X3000/GL-XE3000/GL-X2000 al usar tarjetas SIM de EE. Tras un análisis más detallado, descubrimos que ciertas tarjetas SIM de EE solo admiten el protocolo IPv4. Sin embargo, la configuración predeterminada de los routers celulares de GL.iNet habilita simultáneamente IPv4 e IPv6, lo que provoca este problema.

## Soluciones y alternativas

1.  **Actualización de firmware**

    Hemos publicado nuevas versiones de firmware que cambian el protocolo predeterminado a IPv4 para resolver este problema. Los clientes que necesiten IPv6 pueden seguir modificando la configuración a IPv4 e IPv6 desde el panel de administración.

    | Modelo de router      |                                                                  |
    | :-------------------- | :--------------------------------------------------------------: |
    | GL-X3000 (Spitz AX)   | [Firmware Download](https://dl.gl-inet.com/router/x3000/stable)  |
    | GL-XE3000 (Puli AX)   | [Firmware Download](https://dl.gl-inet.com/router/xe3000/stable) |
    | GL-X2000 (Spitz Plus) | [Firmware Download](https://dl.gl-inet.com/router/x2000/stable)  |

2.  **Alternativa para otros modelos**

    Si tiene otros modelos o prefiere no usar el firmware anterior, ejecute los comandos AT en secuencia después de iniciar la conexión celular.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Nota**: `User_APN` suele ser `everywhere` para las tarjetas SIM de EE. Repita este proceso después de cada reinicio del router.

    ??? note "¿Cómo ejecuto un comando AT?"

        1. En el panel de administración web, vaya a la sección INTERNET -> Cellular, haga clic en el icono de tres puntos de la esquina superior derecha y seleccione **Modem AT Command**.

            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

            En versiones antiguas del firmware, haga clic en el botón de herramientas de la esquina superior derecha para acceder a la página de gestión del módem.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

        2. Localice el comando AT, como se muestra a continuación.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Si encuentra más problemas, póngase en contacto con nuestro equipo de soporte en [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Atentamente,

Soporte técnico de GL.iNet

17 de junio de 2025
