# Wireless (firmware v4.8 y anteriores) {#wireless-firmware-v48-and-earlier}

El contenido de esta página se basa en la versión de firmware v4.8.x y anteriores. Si su dispositivo ejecuta otra versión de firmware, use el selector siguiente para cambiar a la guía correspondiente.

<div class="gl-link-select" data-label="Versión de firmware" data-placeholder="Firmware v4.8 y anteriores" markdown="1">

- [Firmware v4.9 y posteriores](wireless.md)

</div>

---


En el lado izquierdo del panel de administración web, vaya a **WIRELESS**.

La página Wireless permite configurar redes Wi-Fi independientes, incluidas 2.4 GHz, 5 GHz, 6 GHz y Wi-Fi MLO (la disponibilidad varía según el modelo). Cada banda puede configurarse como red Wi-Fi principal o red Wi-Fi de invitados para una gestión inalámbrica más flexible.

**Nota**: Algunos modelos no admiten Wi-Fi de 5 GHz, como GL-MT300N-V2 (Mango), GL-X300B (Collie) y GL-XE300 (Puli); otros no tienen función Wi-Fi, como GL-MT5000 (Brume 3) y GL-MT2500/GL-MT2500A (Brume 2).

## Wi-Fi MLO {#mlo-wi-fi}

| Modelos compatibles      |     |
| :----------------------- | :-: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000) |  √  |
| Beryl 7 (GL-MT3600BE)    |  √  |
| Flint 3e (GL-BE6500)     |  √  |
| Flint 3 (GL-BE9300)      |  √  |
| Slate 7 (GL-BE3600)      |  √  |

MLO (Multi-Link Operation) es una de las funciones principales de Wi-Fi 7 (802.11be), diseñada para mejorar el rendimiento de la red, reducir significativamente la latencia y aumentar la estabilidad de la conexión al utilizar varias bandas de frecuencia al mismo tiempo, como 2.4 GHz, 5 GHz y 6 GHz.

Haga clic en las pestañas siguientes para consultar la configuración de la Wi-Fi MLO principal y la Wi-Fi MLO de invitados.

=== "MLO Wi-Fi"

    La Wi-Fi MLO principal le permite configurar varios ajustes, entre ellos habilitar o deshabilitar la Wi-Fi, seleccionar bandas de radio (al menos dos), habilitar o deshabilitar el BSSID aleatorio, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña de la Wi-Fi y la visibilidad del SSID.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Si las bandas de radio de la Wi-Fi MLO incluyen 6 GHz, el BSSID de la Wi-Fi MLO se sincronizará cuando cambie el BSSID de la Wi-Fi de 6 GHz.

    - La seguridad Wi-Fi predeterminada de la Wi-Fi MLO es WPA3-SAE, adecuada para la mayoría de los dispositivos compatibles con MLO.

=== "MLO Guest Wi-Fi"

    La Wi-Fi MLO de invitados le permite configurar opciones simplificadas, entre ellas habilitar o deshabilitar la Wi-Fi, seleccionar bandas de radio (al menos dos), definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña y la visibilidad del SSID.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## Wi-Fi de 6 GHz {#6-ghz-wi-fi}

| Modelos compatibles      |     |
| :----------------------- | :-: |
| Slate 7 Pro (GL-BE10000) |  √  |
| Mudi 7 (GL-E5800)        |  √  |
| Flint 3 (GL-BE9300)      |  √  |

La Wi-Fi de 6 GHz proporciona una conectividad inalámbrica más rápida y estable, con menos congestión que las bandas de 2.4 GHz y 5 GHz.

Haga clic en las pestañas siguientes para consultar la configuración de la Wi-Fi principal de 6 GHz y la Wi-Fi de invitados de 6 GHz.

=== "6 GHz Wi-Fi"

    La Wi-Fi principal de 6 GHz le permite configurar varios ajustes, entre ellos habilitar o deshabilitar la Wi-Fi, ajustar la potencia TX, habilitar o deshabilitar el BSSID aleatorio, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña de la Wi-Fi, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - **Enable PSC**: cuando PSC (Preferred Scanning Channel) está habilitado, solo se reservarán los canales con mejor conectividad para garantizar la conexión de los dispositivos de 6 GHz.

=== "6 GHz Guest Wi-Fi"

    La Wi-Fi de invitados de 6 GHz le permite configurar opciones simplificadas, entre ellas habilitar o deshabilitar la Wi-Fi, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña y la visibilidad del SSID.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## Wi-Fi de 5 GHz {#5-ghz-wi-fi}

Haga clic en las pestañas siguientes para consultar la configuración de la Wi-Fi principal de 5 GHz y la Wi-Fi de invitados de 5 GHz.

=== "5 GHz Wi-Fi"

    La Wi-Fi principal de 5 GHz le permite configurar varios ajustes, entre ellos habilitar o deshabilitar la Wi-Fi, ajustar la potencia TX, habilitar o deshabilitar el BSSID aleatorio, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña de la Wi-Fi, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi-Fi"

    La Wi-Fi de invitados de 5 GHz le permite configurar opciones simplificadas, entre ellas habilitar o deshabilitar la Wi-Fi, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña y la visibilidad del SSID.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## Wi-Fi de 2.4 GHz {#24-ghz-wi-fi}

Haga clic en las pestañas siguientes para consultar la configuración de la Wi-Fi principal de 2.4 GHz y la Wi-Fi de invitados de 2.4 GHz.

=== "2.4 GHz Wi-Fi"

    La Wi-Fi principal de 2.4 GHz le permite configurar varios ajustes, entre ellos habilitar o deshabilitar la Wi-Fi, ajustar la potencia TX, habilitar o deshabilitar el BSSID aleatorio, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña de la Wi-Fi, la visibilidad del SSID, el modo Wi-Fi, el ancho de banda y el canal.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi-Fi"

    La Wi-Fi de invitados de 2.4 GHz le permite configurar opciones simplificadas, entre ellas habilitar o deshabilitar la Wi-Fi, definir el nombre de la Wi-Fi (SSID), la seguridad de la Wi-Fi, la contraseña y la visibilidad del SSID.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Ajustes comunes de Wi-Fi {#general-wi-fi-settings}

- Pase el cursor sobre el icono del código QR situado junto al SSID de la Wi-Fi para mostrar su código QR. Puede escanearlo con su teléfono o tableta para conectarse rápidamente a la red Wi-Fi correspondiente.

  ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

- **Randomized BSSID**: Está habilitado de forma predeterminada e impide rastrear el router mediante un BSSID fijo. Consulte [Randomized BSSID](#randomized-bssid) para obtener más información.

- **Bandwidth** y **Channel** no se pueden modificar cuando el router actúa como [repetidor](internet_repeater.md), ya que siguen la configuración de la red repetida.

- Cuando **Channel** está configurado como **Auto**, la Wi-Fi del router no cambiará automáticamente a un canal DFS.

- Al cambiar **Channel** de un canal no DFS a uno DFS, aparecerá la siguiente advertencia.

  ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

- Cuando **Bandwidth** se configura en **160 MHz** (solo disponible en algunos modelos), la Wi-Fi siempre utilizará un canal DFS, aunque elija un canal no DFS o **Auto** en la configuración de **Channel**.

## Randomized BSSID {#randomized-bssid}

Randomized BSSID es una función de privacidad disponible desde el firmware v4.6 y habilitada de forma predeterminada. Evita que el router sea localizado y rastreado mediante un BSSID Wi-Fi fijo (la dirección MAC de la interfaz inalámbrica del router).

**Por qué un BSSID fijo supone un riesgo para la privacidad**

Los sistemas operativos móviles (como Android e iOS) utilizan el posicionamiento Wi-Fi basado en datos colaborativos para ofrecer servicios de ubicación:

1. Los dispositivos cliente (teléfonos y portátiles) suben periódicamente los BSSID que detectan, junto con su propia ubicación obtenida mediante GPS, al servidor del proveedor del sistema operativo o del dispositivo.

2. Los proveedores agrupan estos datos en una base de datos global que asocia cada BSSID con una ubicación.

3. Cualquier dispositivo con Wi-Fi habilitado, incluso sin GPS, puede consultar esa base de datos para estimar su ubicación a partir de los BSSID cercanos.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

Como resultado, un router con un BSSID fijo actúa como una baliza de ubicación: puede geolocalizarse de forma remota y sus movimientos (por ejemplo, cuando viaja con él) pueden rastrearse a lo largo del tiempo. Los atacantes también pueden consultar estas bases de datos para localizar routers o identificarlos mediante la información del fabricante (OUI) del BSSID.

**Cómo le protege Randomized BSSID**

Cuando esta función está habilitada, el router genera un BSSID aleatorio y lo renueva en cada arranque. Al cambiar continuamente, el BSSID ya no puede asociarse a una ubicación fija en las bases de datos de los proveedores, lo que rompe la asociación entre BSSID y ubicación utilizada para el rastreo.

| Estado | Comportamiento |
| ----------------- | ---------------------- |
| Habilitado (predeterminado) | Se genera un nuevo BSSID aleatorio en cada arranque |
| Deshabilitado | El router utiliza su dirección MAC real de fábrica como BSSID |

**Notas**:

1. El BSSID solo cambia cuando el router se reinicia; permanece igual durante una sesión en ejecución.
2. En la red Wi-Fi de invitados, el BSSID coincide con el de la red Wi-Fi principal en la misma banda de frecuencia.
3. Si las bandas de la red Wi-Fi MLO incluyen 6 GHz, el BSSID de la red Wi-Fi MLO se sincroniza con el BSSID de la red Wi-Fi de 6 GHz.
4. Randomized BSSID bloquea el rastreo mediante el BSSID del router, pero no impide que los dispositivos cliente comuniquen su propia ubicación. No es una solución de privacidad completa: el SSID, el canal y las características de la señal siguen siendo observables.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"}.
