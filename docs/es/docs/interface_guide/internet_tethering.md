# Conectarse a Internet mediante tethering USB

Compartir la red desde su smartphone al router mediante un cable USB se denomina Tethering. Un módem Host-less también funciona en modo Tethering durante la configuración del módem.

**Nota:** Algunos operadores móviles limitan el tethering o cobran un cargo adicional por él. Le recomendamos consultarlo con su operador.

## Configuración

=== "iPhone"

    1. Conecte un iPhone al puerto USB del router mediante un cable USB. Aparecerá un cuadro de diálogo del sistema preguntando si confía en el dispositivo. Toque **Trust** para continuar.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Vaya a **Settings** -> **Personal Hotspot** del iPhone. Habilite **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Conecte un ordenador u otro teléfono al router y, a continuación, inicie sesión en el panel web de administración del router. Vaya a la sección **INTERNET** -> **Tethering** y haga clic en **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        Si necesita configurar ajustes avanzados como TTL, HL y MTU, haga clic en **Advanced** para personalizarlos y, a continuación, haga clic en **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        Comenzará a conectarse.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Una vez conectado, el estado del hotspot personal, como el número de dispositivos conectados, aparecerá en la barra de estado de la parte superior de la pantalla del teléfono.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        El panel web de administración también mostrará el estado de la conexión Tethering.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Conecte un teléfono Android al puerto USB del router mediante un cable USB. Puede aparecer un cuadro de diálogo del sistema pidiendo preferencias USB. Seleccione **USB Tethering** o **File Transfer** si se le solicita.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Vaya a **Settings** -> **Network & Internet** -> **Personal Hotspot** del teléfono. Habilite **Personal Hotspot** o **USB Tethering**.

        Los pasos para habilitar **USB Tethering** varían según la marca. Revise la configuración de su dispositivo para encontrar la ubicación exacta y contacte con el soporte del fabricante si es necesario.

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Conecte un ordenador u otro teléfono al router y, a continuación, inicie sesión en el panel web de administración del router. Vaya a la sección **INTERNET** -> **Tethering** y haga clic en **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        Si necesita configurar ajustes avanzados como TTL, HL y MTU, haga clic en **Advanced** para personalizarlos y, a continuación, haga clic en **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        Comenzará a conectarse.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Una vez conectado, el estado del hotspot personal, como el número de dispositivos conectados, aparecerá en la barra de estado de la parte superior de la pantalla del teléfono.

        El panel web de administración también mostrará el estado de la conexión Tethering.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Para la documentación oficial de Android, consulte [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Advertencia

Cuando no haya acceso a Internet, se mostrará la advertencia correspondiente:

**"The interface is connected, but the Internet can't be accessed."**

Soluciones:

1. Compruebe si el smartphone tiene acceso a Internet.

2. Vaya a la página [Multi-WAN](multi-wan.md) para determinar si puede acceder a Internet o no.

## Solución de problemas

Si la conexión falla, pruebe estos pasos de solución de problemas:

- Utilice la fuente de alimentación original del router.
- Desconecte y vuelva a conectar el cable USB.
- Use otro cable USB. Asegúrese de que admite transferencia de datos y no solo carga.
- Desactive y vuelva a activar "USB Tethering" varias veces en teléfonos Android.
- Desactive y vuelva a activar "Allow Others to Join" varias veces en iPhone.
- Reinicie el smartphone y vuelva a intentarlo.

---

Artículos relacionados

- [Página de Internet](internet.md)
- [¿Cómo establecer la prioridad de cada método de acceso a Internet?](multi-wan.md)
- [¿Cómo configurar el equilibrio de carga cuando se utilizan varios métodos de acceso a Internet al mismo tiempo?](multi-wan.md)

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
