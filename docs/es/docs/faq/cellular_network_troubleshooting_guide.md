# Guía de solución de problemas de red celular

Si no puede establecer una conexión celular, compruebe los siguientes puntos.

??? "Comprobar el hardware del dispositivo"

    **1.1** Use un adaptador de corriente estándar para su dispositivo. Los adaptadores de corriente no estándar pueden provocar una alimentación insuficiente.

    **1.2** Asegúrese de que en el panel de administración web se muestren **Modem name**, **IMEI** y **SIM ICCID**.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    En la versión de firmware 4.8 y posteriores, haga clic en **View More Information** para encontrar el SIM ICCID.

    Si no puede encontrarlos, reinicie el router. Si el nombre del módem y el IMEI siguen sin reconocerse, póngase en contacto con nosotros en [support@gl-inet.com](mailto:support@gl-inet.com).

    **1.3** Haga clic en **View More** para comprobar **Cells Info** y confirmar que la señal es estable. Si la señal es muy débil, asegúrese de que las antenas estén instaladas correctamente, o mueva el router a una zona con buena señal y vuelva a probar.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}

    **1.4** Haga clic en **View More** para comprobar si la banda de frecuencia compatible con su dispositivo es compatible con su región.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Comprobar la configuración del software"

    **2.1** Inicie sesión en el panel de administración web y asegúrese de que el programa de conexión celular se haya iniciado. También puede hacer clic en **Abort** y luego en **Connect**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}

    **2.2** Algunos operadores de red pueden requerir el protocolo **3G** para conectarse. Cambie al protocolo 3G y vuelva a probar.

    Para la versión de firmware 4.7 y anteriores, vaya a **Manual Setup** -> **Protocol**, seleccione **3G** y luego haga clic en **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    Para la versión de firmware 4.8 y posteriores, vaya a **SIM Card Settings** -> **Protocol**, seleccione **3G** y luego haga clic en **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    El dispositivo se volverá a conectar automáticamente. Espere unos minutos para comprobar si la conexión se ha realizado correctamente.

    **2.3** Algunas tarjetas SIM requieren un APN específico. Si su tarjeta SIM no puede registrarse, póngase en contacto con su operador para comprobar si existe alguna restricción. Configure el APN correcto en el router si es necesario y luego haga clic en **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}

    **2.4** Active **Band Masking** y vuelva a probar. Para la versión de firmware 4.7 y anteriores, consulte [este enlace](../interface_guide/internet_cellular_v4.7.md/#band-masking). Para la versión de firmware 4.8 y posteriores, consulte [este enlace](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Bloquee o desbloquee una torre de señal y vuelva a probar. Esta función solo está disponible en GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) y GL-X2000 (Spitz Plus). Haga clic [aquí](../interface_guide/internet_cellular.md/#lock-tower) para ver más instrucciones.

    Bloquear una torre de señal concreta permite que el router acceda a un recurso de red de alta calidad y mantenga una conectividad celular estable.

    Sin embargo, una vez que se bloquea una torre, el router seguirá intentando volver a conectarse a ella después de reiniciarse, incluso si se traslada a una nueva ubicación. Esto puede impedir que el router se conecte automáticamente a la red celular. Si esto ocurre, puede desbloquear la torre actual desde el panel de administración web del router o bloquearla manualmente en una nueva torre.

    **Nota:** La torre bloqueada debe coincidir con las bandas de frecuencia compatibles con su operador y su dispositivo; de lo contrario, la conexión puede fallar.

??? "Comprobar la compatibilidad de la SIM"

    **3.1** Confirme el tipo de SIM. Los routers celulares GL.iNet están certificados como dispositivos IoT. En teoría, el dispositivo solo admite tarjetas SIM de tipo IoT. Si no está seguro del tipo de SIM, póngase en contacto con su operador.

    Los tipos de SIM más comunes incluyen: solo datos, solo datos + voz, IoT y hotspot. Recomendamos usar tarjetas SIM IoT o de hotspot. No se garantiza el funcionamiento de las tarjetas SIM de solo datos o de solo datos + voz.

    **3.2** Algunas tarjetas SIM deben activarse primero. Asegúrese de que la tarjeta SIM puede acceder a Internet cuando se inserta en un teléfono y luego pásela al router.

    **3.3** Algunas tarjetas SIM personalizadas solo pueden usarse en teléfonos móviles o dispositivos específicos. Confirme si la tarjeta SIM está bloqueada para un dispositivo concreto.

    **3.4** En algunos estados o ciudades de Estados Unidos, por ejemplo, AT&T en Seattle, puede que necesite registrar el IMEI del dispositivo con su operador. Si no está seguro sobre el registro, póngase en contacto con su operador.

    **3.5** Si el panel de administración web muestra "SIM card not registered", pruebe primero los pasos anteriores.

    Recomendamos apagar el router, insertar la tarjeta SIM y luego reiniciar el router. Algunos modelos no admiten intercambio en caliente y pueden no detectar la tarjeta SIM si se inserta mientras el equipo está encendido.

    Asegúrese de que todas las antenas estén correctamente instaladas y vuelva a probar en una zona exterior con señal celular fuerte. Una señal débil puede impedir que la tarjeta SIM se registre en la red.

    Si el problema persiste, la tarjeta SIM puede ser incompatible con el router. Póngase en contacto con su operador de red para obtener más ayuda.

    Si su operador confirma que el problema no está relacionado con la tarjeta SIM, póngase en contacto con nuestro equipo de soporte en [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Si la tarjeta SIM puede registrarse y obtener una dirección IP, pero no puede acceder a Internet, es decir, la subida funciona pero la descarga no, lo más probable es que la tarjeta SIM esté restringida por su operador de red. Póngase en contacto con su operador para eliminar la restricción, o configure el TTL en 65 y vuelva a probar como se muestra a continuación.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    Cuando se ponga en contacto con su operador de red, proporcione el nombre del módem del dispositivo, el IMEI, el SIM ICCID y el modelo del router.

Si ninguno de los pasos anteriores resuelve el problema, póngase en contacto con nuestro equipo de soporte en [support@gl-inet.com](mailto:support@gl-inet.com).
