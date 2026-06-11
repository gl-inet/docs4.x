# Wireless (Firmware v4.9)

> Esta guía se aplica al firmware v4.9 y versiones posteriores. Para versiones anteriores, haga clic [aquí](wireless.md).

En el lado izquierdo del panel de administración web, vaya a **WIRELESS**.

La página Wireless le permite configurar varias redes Wi‑Fi, incluidas MLO Wi‑Fi (disponible en determinados modelos), Main Network, Guest Network e IoT Network. Las bandas Wi‑Fi compatibles varían según el modelo.

## Multi-Link Operation (MLO)

??? "Modelos compatibles"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Modelos no compatibles"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) es una de las funciones principales de Wi‑Fi 7 (802.11be), diseñada para mejorar el rendimiento de la red, reducir significativamente la latencia y aumentar la estabilidad de la conexión al utilizar varias bandas de frecuencia al mismo tiempo, como 2.4 GHz, 5 GHz y 6 GHz.

Se recomienda que los clientes Wi‑Fi 7 se conecten a la red MLO Wi‑Fi, ya que mejora notablemente el rendimiento y la fiabilidad de la red mediante conexiones multibanda.

Haga clic en **Add** para configurar una red MLO Wi‑Fi y luego en **Apply**. Tenga en cuenta que las bandas Wi‑Fi disponibles varían según el modelo.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: seleccione al menos dos bandas de radio.
- Wi-Fi Security: si se selecciona la banda de 6 GHz, WPA3-SAE es la única opción disponible y la recomendada. Funciona mejor con la mayoría de los dispositivos compatibles con MLO.
- Enable Randomized BSSID: cuando se selecciona la banda de 6 GHz, el BSSID de 6 GHz de la red MLO Wi‑Fi se sincronizará con la Wi‑Fi principal.

Una vez habilitada, la página se mostrará de la siguiente manera.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Main Network

Main Network es su red Wi‑Fi principal y admite difusión simultánea en distintas bandas de radio, todas habilitadas de forma predeterminada. Puede configurar ajustes independientes para cada banda, como SSID Wi‑Fi, modo de seguridad, contraseña, BSSID aleatorio, potencia TX, ancho de banda y canal.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

Haga clic en el icono de engranaje de la derecha para ver o modificar la configuración Wi‑Fi de cada banda. Tenga en cuenta que las bandas Wi‑Fi disponibles varían según el modelo.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Guest Network

Guest Network es una red Wi‑Fi dedicada para visitantes, con todas las bandas deshabilitadas de forma predeterminada. Puede habilitar y configurar los ajustes básicos de red para cada banda, como SSID Wi‑Fi, modo de seguridad, contraseña y BSSID aleatorio.

Haga clic en **Add** para configurar una red Guest Wi‑Fi y luego en **Apply**. Tenga en cuenta que las bandas Wi‑Fi disponibles varían según el modelo.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

Una vez habilitada, la página se mostrará de la siguiente manera.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## IoT Network

IoT Network es una red Wi‑Fi dedicada para dispositivos inteligentes, con todas las bandas deshabilitadas de forma predeterminada. Puede habilitar y configurar los ajustes básicos de red para cada banda, como SSID Wi‑Fi, modo de seguridad, contraseña y BSSID aleatorio.

Haga clic en **Add** para configurar una red IoT Wi‑Fi y luego en **Apply**. Tenga en cuenta que esta red no incluye la banda de 6 GHz y que las bandas Wi‑Fi disponibles varían según el modelo.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

Una vez habilitada, la página se mostrará de la siguiente manera.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"}.
