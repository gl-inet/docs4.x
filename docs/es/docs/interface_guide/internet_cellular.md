# Conectarse a Internet mediante red celular

**Nota**: Esta guía se basa en el firmware v4.8. Para versiones anteriores, consulte [aquí](internet_cellular_v4.7.md).

---

La mayoría de los routers GL.iNet admiten conectividad celular. Esta guía cubre tres tipos de modelos:

1. **Modelos 4G de una sola SIM integrados**

   Algunos modelos incluyen un módulo 4G integrado con una sola ranura para tarjeta SIM, como el GL-E750 (Mudi). Consulte [Configuración para modelos de una sola SIM](#configuracion-para-modelos-de-una-sola-sim).

2. **Modelos 5G de doble SIM integrados**

   Algunos modelos incluyen un módulo 5G integrado con dos ranuras para tarjeta SIM, como el GL-X3000 (Spitz AX). La configuración celular en el panel web de administración puede variar ligeramente. Consulte [Configuración para modelos de doble SIM](#configuracion-para-modelos-de-doble-sim).

3. **Modelos compatibles con módem USB**

   Algunos modelos no tienen una ranura para tarjeta SIM integrada, pero disponen de un puerto USB y admiten conectividad celular mediante un módem USB, como el GL-MT3000 (Beryl AX). Consulte [Configuración para módem USB](#configuracion-para-modem-usb).

**Nota:** Algunas tarjetas SIM requieren activación antes del primer uso. Para garantizar la compatibilidad, active la tarjeta SIM en un smartphone antes de insertarla en el router.

## Configuración para modelos de una sola SIM {#configuracion-para-modelos-de-una-sola-sim}

Los siguientes pasos se aplican a modelos con un módem celular integrado y una sola ranura para tarjeta SIM.

Aquí usamos el **GL-E750 (Mudi)** como ejemplo.

Recomendamos apagar primero el router, insertar una SIM previamente activada en la ranura y, a continuación, encenderlo. Si inserta la tarjeta SIM después de que el router haya arrancado, es posible que el panel web de administración no se actualice automáticamente. En ese caso, actualice la página o reinicie el router.

### Configuración automática

Inicie sesión en el panel web de administración del router y vaya a **INTERNET** -> **Cellular**.

1. Cuando no haya ninguna tarjeta SIM insertada, la página mostrará el mensaje "Your SIM card has not been detected".

   ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Inserte una tarjeta SIM. El dispositivo comenzará a conectarse como se muestra a continuación.

   ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

   Si no se conecta automáticamente, haga clic en el botón **Connect** si está disponible.

   Si no se detecta la tarjeta SIM, pruebe a reiniciar el router para comprobar si puede detectarse.

3. Una vez conectada la red celular, la página mostrará los detalles de la red con un punto verde, lo que indica que la conexión se ha realizado correctamente.

   ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Si la configuración automática falla, pruebe con [Configuración manual](#manual-setup-single-sim).

### Configuración manual {#manual-setup-single-sim}

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** y haga clic en **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Puede ver o modificar la configuración celular de la tarjeta SIM actual.

**Nota**: Algunas tarjetas SIM pueden requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existe alguna restricción. Configure el APN correcto en el router si es necesario.

Aplicar los cambios provocará una nueva conexión.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) es un parámetro de pasarela necesario para una conexión de red celular. Permite que el router se conecte a Internet a través del operador móvil. Puede usar el APN predeterminado o configurar un APN personalizado proporcionado por su operador.

- **Protocol**: El protocolo de comunicación celular, por ejemplo 3G, QMI o QCM. Normalmente se detecta automáticamente y puede cambiarlo para ajustarlo a su módem y a los requisitos de su operador.

- **Port**: El puerto serie utilizado para comunicarse con el módem celular. Normalmente se detecta automáticamente y no requiere ajuste manual.

- **TTL**: TTL (Time To Live) define el tiempo máximo que los paquetes pueden permanecer en la red. De forma predeterminada, el router reduce en 1 el TTL de los paquetes entrantes desde los dispositivos cliente antes de reenviarlos. Si necesita sobrescribirlo, puede establecer aquí un valor fijo. La configuración de TTL solo es válida para IPv4.

- **HL**: En IPv6, HL (Hop Limit) limita el número de saltos de transmisión de los paquetes de datos en la red y equivale al TTL en IPv4.

- **MTU**: El valor MTU predeterminado es de 1500 bytes.

- **Authentication**: Elija el método de autenticación requerido por su operador, por ejemplo NONE, PAP o CHAP. Normalmente se establece en NONE si no se necesitan credenciales.

- **Band Masking**: Puede habilitar **Band Masking** si desea que el router bloquee determinadas bandas o use solo bandas celulares específicas. Haga clic [aquí](#band-masking) para ver los detalles.

## Configuración para modelos de doble SIM {#configuracion-para-modelos-de-doble-sim}

Los siguientes pasos se aplican a modelos con un módem celular integrado que admite dos tarjetas SIM. Las páginas pueden diferir ligeramente de las de los modelos de una sola SIM.

Aquí usamos el **GL-X3000 (Spitz AX)** como ejemplo. Admite Dual SIM, Single Standby, lo que significa que puede alojar dos tarjetas SIM para acceso celular, pero solo una de ellas puede estar activa al mismo tiempo. Puede cambiar manualmente entre las dos tarjetas SIM.

Recomendamos apagar primero el router, insertar la tarjeta o tarjetas SIM previamente activadas en las ranuras y, a continuación, encenderlo. Si inserta la tarjeta SIM después de que el router haya arrancado, es posible que el panel web de administración no se actualice automáticamente. En ese caso, actualice la página o reinicie el router.

### Configuración automática

Inicie sesión en el panel web de administración del router y vaya a **INTERNET** -> **Cellular**.

1. Cuando no haya ninguna tarjeta SIM insertada, la página mostrará el mensaje "Your SIM card has not been detected".

   ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Cuando se inserte una tarjeta SIM, la página se mostrará como sigue. Haga clic en **Connect**.

   ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

   Si no se detecta la tarjeta SIM, pruebe a reiniciar el router para comprobar si puede detectarse.

3. Una vez conectada la red celular, la página mostrará los detalles de la red con un punto verde, lo que indica que la conexión se ha realizado correctamente.

   ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Haga clic en **View More Information** para mostrar más información celular, incluidos los detalles del módem, los detalles de la tarjeta SIM, los detalles de Internet y la señal celular.

   ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

   ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Si la configuración automática falla, pruebe con [Configuración manual](#manual-setup-dual-sim).

### Configuración manual {#manual-setup-dual-sim}

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** y haga clic en **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Puede ver o modificar la configuración celular de la tarjeta SIM actual.

**Nota**: Algunas tarjetas SIM pueden requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existe alguna restricción. Configure el APN correcto en el router si es necesario.

Aplicar los cambios provocará una nueva conexión.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) es un parámetro de pasarela necesario para una conexión de red celular. Permite que el router se conecte a Internet a través del operador móvil. Puede usar el APN predeterminado o configurar un APN personalizado proporcionado por su operador.

- **Protocol**: El protocolo de comunicación celular detectado automáticamente, por ejemplo QMI o QCM, según su módem y su operador.

- **Port**: El puerto serie detectado automáticamente para comunicarse con el módem celular.

- **TTL**: TTL (Time To Live) define el tiempo máximo que los paquetes pueden permanecer en la red. De forma predeterminada, el router reduce en 1 el TTL de los paquetes entrantes desde los dispositivos cliente antes de reenviarlos. Si necesita sobrescribirlo, puede establecer aquí un valor fijo. La configuración de TTL solo es válida para IPv4.

- **HL**: En IPv6, HL (Hop Limit) limita el número de saltos de transmisión de los paquetes de datos en la red y equivale al TTL en IPv4.

- **MTU**: El valor MTU predeterminado es de 1500 bytes.

- **Authentication**: Elija el método de autenticación requerido por su operador, por ejemplo NONE, PAP o CHAP. Normalmente se establece en NONE si no se necesitan credenciales.

- **Band Masking**: Puede habilitar **Band Masking** si desea que el router bloquee determinadas bandas o use solo bandas celulares específicas. Haga clic [aquí](#band-masking) para ver los detalles.

### Configuración de la ranura para tarjeta SIM

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** y haga clic en **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Se mostrarán el botón de cambio automático, la tarjeta SIM activa, el ICCID y el operador de red.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Si se insertan dos tarjetas SIM, puede activar **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: Activa el cambio automático entre SIM 1 y SIM 2. El método de detección de red para **SIM Auto Switch** es el mismo que el configurado en la página **Multi-WAN**.

- **Preferred SIM Card Slot**: Configure la tarjeta SIM preferida como SIM 1 o SIM 2.

- **Failover Interval**: Los valores disponibles van de 5 minutos a 24 horas.

  Si la conexión a Internet sigue sin estar disponible después de una conmutación por error, el dispositivo volverá a la ranura SIM preferida y esperará este intervalo antes de intentar de nuevo la conmutación por error.

  Esta opción se aplica cuando tanto la tarjeta SIM preferida como la tarjeta SIM de respaldo no tienen señal. El dispositivo cambiará entre tarjetas SIM hasta que una de ellas obtenga una señal válida.

  ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

  Cuando está activado, el dispositivo comprobará diariamente la ranura SIM preferida a la hora configurada e intentará volver a ella si la SIM preferida recupera el acceso a Internet.

  Esto evita que la SIM de respaldo consuma una cantidad excesiva de datos. Si la SIM preferida sigue sin señal, el dispositivo continuará usando la SIM de respaldo.

  ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Nota**: La función **Auto Switch** no cambia a otra tarjeta SIM de inmediato. Primero, el dispositivo necesita tiempo para confirmar que la SIM actual no puede acceder a Internet. Segundo, la otra SIM no está en modo de espera y requiere tiempo para activarse.

## Configuración para módem USB {#configuracion-para-modem-usb}

Los siguientes pasos se aplican a modelos sin ranura para tarjeta SIM integrada, pero con un puerto USB para conectar un módem USB externo.

Aquí usamos el **GL-MT3000 (Beryl AX)** con el módem USB externo **SIMPoYo uFi** como ejemplo.

Recomendamos apagar primero el router, insertar una SIM previamente activada en el módem USB, conectar el módem al puerto USB del router y, a continuación, encender el router. Si conecta el módem USB después de que el router haya arrancado, es posible que el panel web de administración no se actualice automáticamente. En ese caso, actualice la página o reinicie el router.

### Configuración rápida

1. Apague primero el router. Inserte una tarjeta SIM en el módem USB, conecte el módem al puerto USB del router y, a continuación, encienda el router.

2. Inicie sesión en el panel web de administración del router, vaya a **INTERNET** -> **Tethering** y haga clic en **Connect**.

   ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

   Si necesita establecer configuraciones avanzadas, como TTL, HL y MTU, haga clic en **Advanced** para personalizarlas y, a continuación, haga clic en **Connect**.

   ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

   Comenzará a conectarse.

   ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Una vez conectado, la página mostrará los detalles de la red con un punto verde, lo que indica que la conexión se ha realizado correctamente.

   ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

   **Nota:** Después de la configuración inicial, si reinicia el router con el módem USB conectado, o vuelve a conectarlo, se reconocerá automáticamente y la conexión de red se establecerá sin necesidad de volver a pulsar el botón de conexión.

### Módems compatibles

Aquí se muestra una lista de módems compatibles que hemos probado anteriormente.

**SIMPoYo uFi** es un dongle USB compacto plug and play con punto de acceso Wi-Fi, diseñado para ofrecer conectividad rápida y fiable en cualquier lugar. Funciona perfectamente con la mayoría de los routers GL.iNet, así como con portátiles, baterías externas, puertos USB de automóvil y otras fuentes de alimentación USB. Incluye 10 GB de datos gratuitos durante 30 días, válidos en el Reino Unido y en 34 países europeos.

| Modelo                                                                      | Red celular | Probado | Probado por     | Comentarios\* |
| --------------------------------------------------------------------------- | ----------- | ------- | --------------- | ------------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)          | 5G          | Sí      | GL.iNet         |               |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/) | 4G          | Sí      | GL.iNet         |               |
| Quectel EC20-E, EC20-A, EC20-C                                              | 4G          | Sí      | GL.iNet         |               |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C                                      | 4G          | Sí      | GL.iNet         |               |
| Serie Quectel EC200A                                                        | 4G          | Sí      | akw2312         | Host-less     |
| Quectel EP06-E, EP06-A                                                      | 4G          | Sí      | akw2312         |               |
| Quectel EM060K-GL, EM120K-GL                                                | 4G          | Sí      | akw2312         |               |
| Quectel EM120R-GL, EM160R-GL                                                | 4G          | Sí      | akw2312         |               |
| Quectel RM520N-GL                                                           | 5G          | Sí      | akw2312         |               |
| Quectel UC20-E                                                              | 3G          | Sí      | GL.iNet         |               |
| ZTE ME909s-821                                                              | 4G          | Sí      | GL.iNet         |               |
| Huawei E1550                                                                | 3G          | Sí      | GL.iNet         |               |
| Huawei E3276                                                                | 4G          | Sí      | GL.iNet         |               |
| Huawei E3372                                                                | 4G          | Sí      | anónimo         |               |
| Huawei E3372h-320 (Ukraine)                                                 | 4G          | Sí      | anónimo         | Host-less     |
| TP-Link MA260                                                               | 3G          | Sí      | GL.iNet         |               |
| ZTE M823                                                                    | 4G          | Sí      | Arnas Risqianto |               |
| ZTE MF190                                                                   | 3G          | Sí      | Arnas Risqianto |               |
| Pantech UML290VW (Verizon)                                                  | 4G          | Sí      | GL.iNet/steven  | QMI           |
| Pantech UML295 (Verizon)                                                    | 4G          | Sí      | GL.iNet/steven  | Host-less     |
| Novatel USB551L (Verizon)                                                   | 4G          | Sí      | GL.iNet/steven  | QMI           |
| Verizon U620L (Verizon)                                                     | 4G          | Sí      | anónimo         | Host-less     |

- **QMI**: Este módem admite el modo QMI. Seleccione QMI como protocolo de comunicación celular y **/dev/cdc-wdm0** como puerto serie en la configuración de la tarjeta SIM.

- **Host-less**: Este módem admite el modo Tethering. Gestione la conexión mediante la interfaz **Tethering** del router en lugar de la interfaz **Cellular**.

## Estadísticas de tráfico

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** y haga clic en **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Entrará en la página **Traffic Statistics**. Esta muestra los datos usados por la tarjeta o tarjetas SIM y proporciona configuraciones de límite de datos.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Si **Data Used** supera **Data Cap Amount**, modifique manualmente **Data Cap Amount** o **Data Used**. De lo contrario, la red puede desconectarse o la tarjeta SIM puede cambiar automáticamente mediante **Auto Switch** en los modelos de doble SIM.

- **Modificar el uso de datos**

  Haga clic en **Modify** a la derecha de **SIM 1/2 Data Used**.

  ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

  Luego podrá modificar o restablecer los datos usados.

  ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Configurar el límite de datos de la SIM**

  Si desea configurar el límite de datos de la SIM, active primero **Save data when power off**. Esto significa que los datos pueden guardarse incluso después de apagar el dispositivo.

  ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

  A continuación, active la configuración de límite de SIM 1 o SIM 2.

  ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Para los modelos de doble SIM, sugerimos habilitar al mismo tiempo **SIM Card Slot Auto Switch**. Si se establece **SIM 1 Data Cap Amount** y está habilitado **SIM Card Slot Auto Switch**, la SIM 1 cambiará automáticamente a la SIM 2 cuando sus datos superen **Data Cap Amount**, y la SIM 1 se deshabilitará.

## Registro histórico de la señal

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** y haga clic en **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Aquí puede comprobar la calidad de su conexión celular. Si la señal es débil, intente cambiar de torre para obtener una mejor señal.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Vea el historial de intensidad de la señal seleccionando distintos periodos de tiempo en la esquina superior derecha.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Enmascaramiento de banda {#band-masking}

**Band Masking** le permite bloquear bandas específicas o usar solo las bandas celulares preferidas para mejorar una señal celular débil.

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular** -> **SIM Card Settings** y active **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Seleccione **Masking Mode** (Block u Open) y, a continuación, seleccione las bandas LTE, las bandas 5G NSA y las bandas 5G SA.

## SMS

Consulte el [tutorial de SMS](sms.md).

## Reenvío de SMS

Consulte el [tutorial de reenvío de SMS](../tutorials/sms_forwarding.md).

## Bloqueo de torre

!!! note "Modelos compatibles"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *El GL-X2000 (Spitz Plus) admite esta función con firmware ver. 4.7 o posterior.

Si desea recibir una señal de alta calidad y garantizar una conexión celular estable, puede probar el bloqueo de torre.

**Nota:** La torre bloqueada debe coincidir con las bandas de frecuencia admitidas por su operador y su dispositivo; de lo contrario, la conexión puede fallar.

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular**. Haga clic en el icono de tres puntos de la esquina superior derecha y luego seleccione **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Haga clic en **Scan** para comenzar a escanear las torres de señal celular. Esto tardará unos minutos. No actualice la página durante el escaneo.

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

Se mostrarán las torres disponibles.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Haga clic en una torre para ver los detalles y bloquearla.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Nota**:

1. Es posible que el dispositivo no pueda escanear todas las torres cuando la interfaz **Cellular** esté habilitada.

2. Si la torre bloqueada no coincide con los parámetros de enmascaramiento de banda o APN de su configuración celular, el router no podrá conectarse a la red celular.

3. Después de bloquear una torre celular, si mueve el router a otra ubicación, seguirá intentando reconectarse a la torre bloqueada tras reiniciarse. Esto puede impedir que el router se conecte automáticamente a la red celular en la nueva ubicación. En ese caso, debe desbloquear la torre celular actual o bloquearla manualmente en una nueva torre.

## Bloqueo de operador

Esta función solo está disponible en GL-X3000, GL-XE3000 y GL-X2000 (firmware ver. 4.8 o posterior).

Al bloquear un operador móvil específico, el router utilizará únicamente la red de ese operador, lo que garantiza una conexión estable y evita cargos de roaming no deseados, especialmente en zonas fronterizas donde el dispositivo podría conectarse de otro modo a redes extranjeras.

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular**. Haga clic en el icono de tres puntos de la esquina superior derecha y luego seleccione **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Hay tres modos de bloqueo:

- **Auto**: Se conecta automáticamente a una red de operador disponible.
- **Manual**: Bloquea manualmente un operador específico.
- **Manual-Auto**: Cambia automáticamente a una red de operador disponible si falla el bloqueo manual.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Comandos AT del módem

Los comandos AT del módem son instrucciones estándar utilizadas para comunicarse con el módem celular. Con esta función, puede enviar comandos y comprobar el estado del módem.

En el panel web de administración del router, vaya a **INTERNET** -> **Cellular**. Haga clic en el icono de tres puntos de la esquina superior derecha y luego seleccione **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Entrará en la página **AT Command**.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Cuando **Shortcut** esté configurado como **Manual command**, puede escribir el comando deseado en el campo **AT Command**.

También puede hacer clic en la lista desplegable **Shortcut** para seleccionar una lista de **preset commands**.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Los siguientes comandos están disponibles como ajustes predefinidos:

- Request IMEI
- Request QCCID
- Request IMSI
- Check Signal Quality
- Reset modem
- Operator Names
- Request SIM card status

Como ejemplo, aquí se selecciona el acceso directo "Request IMEI". Haga clic en "Send" y obtendrá el resultado como se muestra a continuación.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

En la esquina inferior derecha, puede hacer clic en **Export Debug Info** para descargar un archivo .json.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Solución de problemas

Si no consigue establecer una conexión celular, haga clic en el mensaje de error correspondiente a continuación para ver las soluciones relevantes.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Estas son algunas sugerencias para la solución de problemas.

    1. Actualice la página y espere unos minutos para comprobar si se detecta la tarjeta SIM.

    2. Asegúrese de que la tarjeta SIM esté instalada correctamente. Alinee la muesca de la tarjeta SIM con la marca correspondiente en la ranura para confirmar la orientación correcta de inserción.

    3. Apague el router, retire y vuelva a insertar la tarjeta SIM y, a continuación, vuelva a encender el router.

    4. Pruebe con otra tarjeta SIM si dispone de una.

    Si el problema persiste, descargue los registros y envíelos a [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Este problema tiene dos tipos de mensajes de error:

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Estas son algunas sugerencias para la solución de problemas.

    1. Actualice la página y espere unos minutos para comprobar si el error desaparece.

    2. Haga clic en **Disconnect**/**Abort** y, a continuación, en **Connect** para intentar reconectarse.

    3. Reinicie el router.

    4. Verifique el estado de la tarjeta SIM y asegúrese de que esté activada. Pruebe la tarjeta SIM insertándola en un smartphone para confirmar que puede acceder normalmente a Internet con un plan de datos móviles activo, o contacte con su operador de red para verificarlo.

    5. Algunos operadores pueden requerir un protocolo 3G para la conexión de red. Vaya a **SIM Card Settings** -> **Protocol**, seleccione **3G** y, a continuación, haga clic en **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        El dispositivo se reconectará automáticamente. Espere unos minutos para comprobar si la conexión se ha establecido correctamente.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Si la conexión se realiza correctamente, la página se mostrará como sigue.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Algunas tarjetas SIM pueden tener restricciones especiales de uso, como requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existe alguna restricción.

        Si es necesario, vaya a **SIM Card Settings** -> **APN**, configure el APN correcto en el router y, a continuación, haga clic en **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Haga clic en **View More Information** para comprobar la intensidad de la señal celular. Si la señal es débil, asegúrese de que la antena esté instalada correctamente. Coloque el router en un lugar abierto y sin obstáculos para mejorar la recepción de la señal.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. Compruebe si **Band Masking** o **Lock Tower** están habilitados. Si es así, desactive la función y vuelva a intentar la conexión.

    Si el problema persiste, descargue los registros y envíelos a [support@gl-inet.com](mailto:support@gl-inet.com).

## Certificación IoT

### Certificación de AT&T

Haga clic en el enlace [att device certification](https://iotdevices.att.com/certified-devices.aspx#) e introduzca el nombre del dispositivo para encontrarlo.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Certificación de T-Mobile

Haga clic en el enlace [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) y elija 5G en **Filter** para encontrarlo.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}

---

Artículos relacionados

- [Página de Internet](internet.md)
- [¿Cómo establecer la prioridad de cada método de acceso a Internet?](multi-wan.md)
- [¿Cómo configurar el equilibrio de carga cuando se utilizan varios métodos de acceso a Internet al mismo tiempo?](multi-wan.md)

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
