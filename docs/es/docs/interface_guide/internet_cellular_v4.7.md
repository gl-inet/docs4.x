# Conectarse a Internet mediante red celular (firmware v4.7 y anteriores)

**Nota**: Esta guía se basa en el firmware v4.7 y versiones anteriores. Para versiones más recientes, consulte [aquí](internet_cellular.md).

---

La mayoría de los routers GL.iNet admiten conectividad celular. Esta guía cubre tres tipos de modelos:

1. **Modelos 4G de una sola SIM integrados**

   Algunos modelos incluyen un módulo 4G integrado con una sola ranura para tarjeta SIM, como el GL-XE300 (Puli). Consulte [Configuración para modelos de una sola SIM](#configuracion-para-modelos-de-una-sola-sim).

2. **Modelos compatibles con módem USB**

   Algunos modelos disponen de un puerto USB y admiten conectividad celular mediante un módem USB, como el GL-AXT1800 (Slate AX). Los pasos de configuración son similares a los de los modelos 4G integrados de una sola SIM. Consulte [Configuración para modelos de una sola SIM](#configuracion-para-modelos-de-una-sola-sim).

3. **Modelos 5G de doble SIM integrados**

   Algunos modelos incluyen un módulo 5G integrado con dos ranuras para tarjeta SIM, como el GL-X3000 (Spitz AX). La configuración celular en el panel web de administración puede variar ligeramente. Consulte [Configuración para modelos de doble SIM](#configuracion-para-modelos-de-doble-sim).

**Nota:** Algunas tarjetas SIM requieren activación antes del primer uso. Para garantizar la compatibilidad, active la tarjeta SIM en un smartphone antes de insertarla en el router.

## Configuración para modelos de una sola SIM

Los siguientes pasos se aplican a modelos con un módem celular integrado y una sola ranura para tarjeta SIM, como el GL-XE300 Puli, o con un puerto USB para conectar un módem USB externo, como el GL-AXT1800 Slate AX.

Aquí usaremos como ejemplo el **GL-AXT1800 (Slate AX)** con un módem USB externo.

Recomendamos apagar primero el router. Inserte una tarjeta SIM previamente activada en el módem USB y, a continuación, conecte el módem al puerto USB del router. Después, encienda el router.

Si conecta el módem USB después de que el router haya arrancado, es posible que el panel web de administración no se actualice automáticamente. En ese caso, actualice la página o reinicie el router.

### Configuración automática

Inicie sesión en el panel web de administración del router y vaya a **INTERNET** -> **Cellular**.

1. Cuando acceda por primera vez, puede que no se conecte automáticamente, pero debería mostrar en la esquina superior izquierda el nombre de su operador y el IMEI. Haga clic en **Auto Setup**.

   Ignore la advertencia _Incompatible Modem_.

   ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Comenzará a conectarse.

   **Nota:** Algunas tarjetas SIM pueden tener restricciones especiales de uso, como requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existen restricciones especiales.

   ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Una vez establecida la conexión, la página mostrará los detalles de la red con un punto verde, lo que indica que la conexión se ha realizado correctamente.

   ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

   **Nota:** Después de la configuración inicial, si reinicia el router con el módem USB conectado, o vuelve a conectarlo, el módem USB se reconocerá automáticamente y la conexión de red se establecerá sin necesidad de volver a pulsar el botón **Auto Setup**.

Si **Auto Setup** falla, pruebe con [Configuración manual](#configuracion-manual).

### Configuración manual

En la sección **Cellular**, haga clic en **Manual Setup** para ver o modificar la configuración celular de la tarjeta SIM actual.

**Nota**: Algunas tarjetas SIM pueden requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existe alguna restricción. Configure el APN correcto en el router si es necesario.

Aplicar los cambios provocará una nueva conexión.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: El protocolo de comunicación celular, por ejemplo 3G, QMI o QCM. Normalmente se detecta automáticamente y puede cambiarlo para ajustarlo a su módem y a los requisitos de su operador.

- **Port**: El puerto serie utilizado para comunicarse con el módem celular. Normalmente se detecta automáticamente y no requiere ajuste manual.

- **APN**: APN (Access Point Name) es un parámetro de pasarela necesario para una conexión de red celular. Permite que el router se conecte a Internet a través del operador móvil. Puede usar el APN predeterminado o configurar un APN personalizado proporcionado por su operador.

- **PIN**: Si la tarjeta SIM está protegida por un código PIN, introdúzcalo aquí. Este campo es opcional si no se ha configurado ningún PIN.

- **TTL**: TTL (Time To Live) define el tiempo máximo que los paquetes pueden permanecer en la red. De forma predeterminada, el router reduce en 1 el TTL de los paquetes entrantes desde los dispositivos cliente antes de reenviarlos. Si necesita sobrescribirlo, puede establecer aquí un valor fijo. La configuración de TTL solo es válida para IPv4.

- **Service**: Seleccione el tipo de servicio celular para definir las tecnologías de red que utilizará el módem.

- **Dial Number**: Introduzca el número de marcación proporcionado por su operador. A menudo viene preconfigurado y puede dejarse en blanco en la mayoría de las redes modernas.

- **Authentication**: Elija el método de autenticación requerido por su operador, por ejemplo NONE, PAP o CHAP. Normalmente se establece en NONE si no se necesitan credenciales.

### Módems compatibles

Aquí se muestra una lista de módems compatibles que hemos probado anteriormente.

| Modelo                                 | 3G/4G | Probado | Probado por     | Comentarios\* |
| -------------------------------------- | ----- | ------- | --------------- | ------------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Sí      | GL.iNet         |               |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Sí      | GL.iNet         |               |
| Serie Quectel EC200A                   | 4G    | Sí      | akw2312         | Host-less     |
| Quectel EP06-E, EP06-A                 | 4G    | Sí      | akw2312         |               |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Sí      | akw2312         |               |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Sí      | akw2312         |               |
| Quectel RM520N-GL                      | 5G    | Sí      | akw2312         |               |
| Quectel UC20-E                         | 3G    | Sí      | GL.iNet         |               |
| ZTE ME909s-821                         | 4G    | Sí      | GL.iNet         |               |
| Huawei E1550                           | 3G    | Sí      | GL.iNet         |               |
| Huawei E3276                           | 4G    | Sí      | GL.iNet         |               |
| TP-Link MA260                          | 3G    | Sí      | GL.iNet         |               |
| ZTE M823                               | 4G    | Sí      | Arnas Risqianto |               |
| ZTE MF190                              | 3G    | Sí      | Arnas Risqianto |               |
| Huawei E3372                           | 4G    | Sí      | anónimo         |               |
| Pantech UML290VW (Verizon)             | 4G    | Sí      | GL.iNet/steven  | QMI           |
| Pantech UML295 (Verizon)               | 4G    | Sí      | GL.iNet/steven  | Host-less     |
| Novatel USB551L (Verizon)              | 4G    | Sí      | GL.iNet/steven  | QMI           |
| Verizon U620L (Verizon)                | 4G    | Sí      | anónimo         | Host-less     |
| Huawei E3372h-320 (Ukraine)            | 4G    | Sí      | anónimo         | Host-less     |

- **QMI**: Este módem admite el modo QMI. Seleccione QMI como protocolo y **/dev/cdc-wdm0** como puerto serie para su router celular.

- **Host-less**: Este módem admite el modo Tethering. Gestione la conexión mediante la interfaz **Tethering** del router en lugar de la interfaz **Cellular**.

## Configuración para modelos de doble SIM

Los siguientes pasos se aplican a modelos con un módem celular integrado que admite dos tarjetas SIM. El panel web de administración puede diferir ligeramente del de los modelos de una sola SIM.

Aquí usamos como ejemplo el **GL-X3000 (Spitz AX)**. Admite Dual SIM, Single Standby, lo que significa que puede alojar dos tarjetas SIM para acceso celular, pero solo una de ellas puede estar activa al mismo tiempo. Puede cambiar manualmente entre las dos tarjetas SIM.

Recomendamos apagar primero el router, insertar la tarjeta o tarjetas SIM previamente activadas en las ranuras y, a continuación, encenderlo. Si inserta la tarjeta SIM después de que el router haya arrancado, es posible que el panel web de administración no se actualice automáticamente. En ese caso, actualice la página o reinicie el router.

### Configuración automática

Inicie sesión en el panel web de administración del router y vaya a **INTERNET** -> **Cellular**.

1. Cuando no haya ninguna tarjeta SIM insertada, la página se mostrará como sigue.

   ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Cuando se inserte una tarjeta SIM, el router comenzará a conectarse automáticamente.

   Si la conexión se realiza correctamente, la página se mostrará como sigue.

   ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Si no se conecta automáticamente, haga clic en **Auto Setup** y espere a que el router se conecte, o pruebe con **Manual Setup**.

### Configuración manual

En la sección **Cellular**, haga clic en **Manual Setup** para acceder a **Cellular Settings**.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Puede ver o modificar la configuración celular de la tarjeta SIM actual. También almacena algunos perfiles preconfigurados y puede añadir configuraciones manualmente en **Saved Settings**.

### Configuración de la ranura para tarjeta SIM

En la sección **Cellular**, haga clic en **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Entrará en **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Si se insertan dos tarjetas SIM, puede activar **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

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

## Estadísticas de tráfico

En la sección **Cellular**, haga clic en **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Entrará en la página **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Consulte el [tutorial de SMS](sms.md).

## Reenvío de SMS

Consulte el [tutorial de reenvío de SMS](../tutorials/sms_forwarding.md).

## Gestión del módem

En la sección **Cellular**, haga clic en el botón **Tool** de la esquina superior derecha para acceder a la página de gestión del módem.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Incluye dos secciones: **Modem Info** y **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

Los comandos AT son instrucciones estándar utilizadas para comunicarse con el módem celular.

Cuando **Shortcut** esté configurado como **Manual command**, escriba el comando deseado en el campo **AT Command** para comprobar el estado del módem.

También puede hacer clic en la lista desplegable **Shortcut** para seleccionar una lista de **preset commands**.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Los siguientes comandos están disponibles como ajustes predefinidos:

- Request IMEI
- Request QCCID
- Request IMSI
- Check Signal Quality
- Reset modem
- Operator Names
- Request SIM card status

Como ejemplo, aquí se selecciona el acceso directo "Request IMEI". Haga clic en "Send" y obtendrá el resultado como se muestra a continuación.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Perfil del operador

Puede guardar diferentes perfiles para el mismo operador o para operadores distintos.

En la sección **Cellular**, haga clic en el botón **Profile** de la esquina superior derecha para gestionar los perfiles.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Añada un perfil nuevo o guarde el perfil actual.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Cree su propio perfil según los requisitos de su operador.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

La próxima vez podrá seleccionar un perfil guardado.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Elija cualquiera de los perfiles que necesite.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Bloqueo de torre

Esta función solo está disponible en GL-X3000, GL-XE3000 y GL-X2000 (firmware ver. 4.7 o posterior).

Si desea recibir una señal de alta calidad y garantizar una conexión celular estable, puede probar el bloqueo de torre.

**Nota:** La torre bloqueada debe coincidir con las bandas de frecuencia admitidas por su operador y su dispositivo; de lo contrario, la conexión puede fallar.

En la sección **Cellular**, haga clic en el icono **Tower** de la esquina superior derecha.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Se mostrarán las torres disponibles.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Haga clic en una torre para ver los detalles y bloquearla.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

El estado de la torre, por ejemplo Locked/Unlocked, se mostrará en la parte superior.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Nota**:

1. Es posible que el dispositivo no pueda escanear todas las torres cuando la interfaz **Cellular** esté habilitada.

2. Si la torre bloqueada no coincide con los parámetros de enmascaramiento de banda o APN de su configuración celular, el router no podrá conectarse a la red celular.

3. Después de bloquear una torre celular, si mueve el router a otra ubicación, seguirá intentando reconectarse a la torre bloqueada tras reiniciarse. Esto puede impedir que el router se conecte automáticamente a la red celular en la nueva ubicación. En ese caso, debe desbloquear la torre celular actual o bloquearla manualmente en una nueva torre.

## Registro histórico de la señal

En la sección **Cellular**, haga clic en el icono **Signal** de la esquina superior derecha para comprobar el historial de intensidad de la señal.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Esto le ayuda a determinar la calidad de su conexión celular. Si la señal es débil, intente cambiar de torre para obtener una mejor señal.

Puede ver el historial de intensidad de la señal celular seleccionando distintos periodos de tiempo.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Enmascaramiento de banda

En la sección **Cellular**, haga clic en **View More** y seleccione **Cells Info** para consultar los detalles de las celdas.

Verá las bandas que está utilizando actualmente y el estado de su señal.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Si la señal es débil, puede habilitar **Band Masking** para bloquear determinadas bandas. Alternativamente, si la señal es buena, puede permitir que el router use solo bandas celulares específicas.

Haga clic en **Manual Setup** para acceder a la página **Cellular Settings** y, a continuación, habilite **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Seleccione **Masking Mode** (Block u Open) y, a continuación, seleccione las bandas LTE, las bandas 5G NSA y las bandas 5G SA.

## Solución de problemas

Si no consigue establecer una conexión celular, haga clic en el mensaje de error correspondiente a continuación para ver las soluciones relevantes.

??? note "No SIM / Your SIM card has not been detected"

    1. Actualice la página y espere unos minutos para comprobar si se detecta la tarjeta SIM.

    2. Asegúrese de que la tarjeta SIM esté instalada correctamente. Alinee la muesca de la tarjeta SIM con la marca correspondiente en la ranura para confirmar la orientación correcta de inserción.

    3. Apague el router, retire y vuelva a insertar la tarjeta SIM y, a continuación, vuelva a encender el router.

    4. Pruebe con otra tarjeta SIM si dispone de una.

    Si el problema persiste, descargue los registros y envíelos a [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Actualice la página y espere unos minutos para comprobar si el error desaparece.

    2. Haga clic en **Disconnect**/**Abort** y, a continuación, en **Connect** para intentar reconectarse.

    3. Reinicie el router.

    4. Verifique el estado de la tarjeta SIM y asegúrese de que esté activada. Pruebe la tarjeta SIM insertándola en un smartphone para confirmar que puede acceder normalmente a Internet con un plan de datos móviles activo, o contacte con su operador de red para verificarlo.

    5. Algunos operadores pueden requerir un protocolo 3G para la conexión de red. Vaya a **Manual Setup** -> **Cellular Settings** -> **Protocol**, seleccione **3G** y, a continuación, haga clic en **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        El dispositivo se reconectará automáticamente. Espere unos minutos para comprobar si la conexión se ha establecido correctamente.

    6. Algunas tarjetas SIM pueden tener restricciones especiales de uso, como requerir un APN específico. Si su tarjeta SIM no logra registrarse, contacte con su operador para comprobar si existe alguna restricción.

        Si es necesario, vaya a **Manual Setup** -> **Cellular Settings** -> **APN**, configure el APN correcto en el router y, a continuación, haga clic en **Apply**.

    7. Haga clic en **View More** y seleccione **Cells Info** para comprobar la intensidad de la señal celular. Si la señal es débil, asegúrese de que la antena esté instalada correctamente. Coloque el router en un lugar abierto y sin obstáculos para mejorar la recepción de la señal.

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
