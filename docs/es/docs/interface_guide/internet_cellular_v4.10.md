# Conectarse a Internet mediante red celular (v4.10)

El contenido de esta página se basa en las versiones de firmware v4.10 y posteriores. Si su dispositivo ejecuta otra versión de firmware, use el selector siguiente para cambiar a la guía correspondiente.

<div class="gl-link-select" data-label="Versión de firmware" data-placeholder="Firmware v4.10 y posteriores" markdown="1">

- [Firmware v4.8 - v4.9](internet_cellular.md)
- [Firmware v4.7 y anteriores](internet_cellular_v4.7.md)

</div>

---

La mayoría de los routers GL.iNet admiten conectividad celular. Esta guía presenta las conexiones celulares para dos tipos de routers:

1. **Routers celulares**

    Los routers celulares GL.iNet incluyen un módulo 4G/5G integrado y una o dos ranuras para tarjetas SIM, como Spitz AX (GL-X3000) y Mudi 7 (GL-E5800). La configuración celular del panel de administración web puede variar ligeramente según el modelo y la versión de firmware. Para configurar la conexión celular de estos modelos, consulte [Routers celulares](#routers-celulares).

2. **Routers no celulares**

    Son otros tipos de routers, como los routers domésticos, de viaje y mini, además de las puertas de enlace de seguridad. Suelen disponer de un puerto USB al que puede conectarse un dongle USB (no incluido) para obtener conectividad celular. Para configurar la conexión celular de estos modelos, consulte [Routers no celulares](#routers-no-celulares).

**Nota:** Algunas tarjetas SIM deben activarse antes del primer uso. Para garantizar la compatibilidad, active la tarjeta SIM en un smartphone antes de insertarla en el router.

## Routers celulares

En esta sección se usa **Mudi 7 (GL-E5800)** como ejemplo para explicar los pasos de configuración celular y las funciones relacionadas.

Como Mudi 7 dispone de una eSIM integrada y dos ranuras Nano-SIM, y admite Dual SIM Dual Standby, su panel de administración web puede diferir ligeramente del de otros routers celulares, especialmente de los que solo tienen una ranura SIM.

### Configuración de red

Inicie sesión en el panel de administración web del router y vaya a **INTERNET** -> **Cellular**.

1. Si no se ha insertado ninguna tarjeta SIM, la página muestra «Your SIM card has not been detected».

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Inserte una tarjeta SIM. El router empezará a conectarse automáticamente. Una vez establecida la conexión, la página muestra el operador de la SIM, la intensidad de la señal, la banda, el uso de datos y otras opciones.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Si no se detecta la tarjeta SIM, vuelva a insertarla en el router o reinicie el router e inténtelo de nuevo.

3. Para ver los detalles de la red, haga clic en **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    En **Network Information** puede ver SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address e IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "¿Qué es Max Bit Rate (AMBR)?"

        AMBR significa Aggregate Maximum Bit Rate. Define el límite superior agregado de la tasa de bits para todos los portadores que no son GBR de su operador. Este parámetro lo proporciona el operador de la red móvil.

4. Para configurar la red manualmente, haga clic en **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    En **Network Settings** puede configurar parámetros de red como el APN.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: La configuración del APN suele obtenerse automáticamente de la tarjeta SIM. Algunas tarjetas SIM requieren un APN específico. Si no conoce el APN correcto, consulte a su operador de red.

    - **IP Type**: Se detecta automáticamente. Puede seleccionar IPv4, IPv6 o ambos. Asegúrese de que la opción seleccionada coincida con el tipo de IP compatible con la tarjeta SIM. Si la tarjeta SIM no admite el tipo de IP actual, o si selecciona IPv6 aquí pero IPv6 está deshabilitado en el router, pueden producirse problemas de marcación.

    - **International Data Roaming**: Está habilitado de forma predeterminada para facilitar el uso de datos durante los viajes internacionales. Puede deshabilitarlo si no lo necesita o si desea evitar cargos elevados de itinerancia de su operador.

    - **TTL**: Algunos operadores determinan si la tarjeta SIM se utiliza en un router leyendo el valor TTL. Si no puede usar la tarjeta SIM en el router, pruebe a configurar TTL con un valor distinto de 64 y 128, por ejemplo 65.

    - **HL**: En IPv6, el campo HL (Hop Limit) limita el número de saltos de transmisión de los paquetes de datos en la red y equivale a TTL en IPv4.

    - **MTU**: Defina el valor MTU según el caso de uso. Una configuración incorrecta puede interrumpir la conexión a Internet. Si modifica MTU, reinicie el dispositivo para que el cambio surta efecto.

    - **Authentication**: Normalmente se establece en NONE si no se requieren credenciales. Puede seleccionar PAP, CHAP o PAP/CHAP.

### Estadísticas de tráfico

Para ver las estadísticas de tráfico, haga clic en **Data Usage**.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Si desea establecer un límite de datos para la SIM o programar el restablecimiento periódico del uso de datos, habilite **SIM Limit Settings**.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Defina Data Cap Amount, Data Reset Period, Start Day y Start Hour y, a continuación, haga clic en **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Nota**:

1. Si Data Used supera Data Cap Amount, modifique Data Cap Amount o Data Used. De lo contrario, la red podría desconectarse o el router podría cambiar a otra SIM, siempre que [SIM Failover](#sim-failover) esté habilitado.

2. Si se establece Data Cap Amount para SIM 1 y SIM Auto Switch está habilitado, SIM 1 cambiará automáticamente a SIM 2 cuando supere el límite de datos y SIM 1 quedará deshabilitada.

3. Start Day: El número máximo de días corresponde al número real de días del mes actual.

### Detalles de la conexión celular

Para ver los detalles de la conexión celular, haga clic en **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

En **Cellular Information** puede ver Network Type, TAC, Cell ID, Band y Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: Se detecta automáticamente. Para especificarlo, cambie a la pestaña **Cellular Settings** y seleccione el tipo de red en la lista desplegable.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Seleccione 5G para obtener mayor velocidad (se requiere señal 5G) o 4G para obtener mayor estabilidad.

    Si bloquea una torre, el tipo de red quedará fijado y no podrá cambiarse.

- **TAC**: Sigla de Tracking Area Code. Es un identificador asignado por la red que representa un área de seguimiento para la gestión de movilidad en la red celular. Se detecta automáticamente desde la estación base celular.

- **Cell ID**: Identificador único que distingue una celda concreta de una estación base celular. También se detecta automáticamente desde la estación base.

- **Band Information**: Haga clic para ver más parámetros relacionados con la banda celular.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: Haga clic para consultar el historial de intensidad de la señal. Puede usarlo para supervisar la calidad de la conexión celular.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Enmascaramiento de bandas

Band Masking permite usar bandas celulares específicas para mejorar la señal celular.

Para habilitar Band Masking, haga clic en **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

En **Cellular Settings**, habilite **Band Masking**, seleccione las bandas que desea usar y haga clic en **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Bloqueo de operador

!!! note "Modelos compatibles"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *El GL-X2000 (Spitz Plus) admite esta función con firmware v4.8 o posterior.

Al bloquear un operador móvil específico, el router utiliza únicamente su red. Esto garantiza una conexión estable y evita cargos de itinerancia no deseados, especialmente en zonas fronterizas donde el dispositivo podría conectarse a redes extranjeras.

Para bloquear un operador, haga clic en **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

En **Cellular Settings**, haga clic en **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Antes de buscar redes, puede seleccionar el **Lock Mode**.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: Bloquea manualmente un operador específico.

- **Manual-Auto**: Cambia automáticamente a una red de operador disponible si falla el bloqueo manual.

A continuación, haga clic en **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Espere aproximadamente un minuto. Se mostrarán los operadores disponibles. Seleccione uno y haga clic en **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

La señal celular quedará bloqueada en el operador seleccionado.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Bloqueo de torre

!!! note "Modelos compatibles"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *El GL-X2000 (Spitz Plus) admite esta función con firmware v4.7 o posterior.

Para obtener una señal de alta calidad y garantizar una conexión celular estable, puede intentar bloquear una torre. La torre bloqueada debe coincidir con las bandas de frecuencia admitidas por el operador y el dispositivo; de lo contrario, la conexión podría fallar.

Para bloquear una torre, haga clic en **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

En **Cellular Settings**, haga clic en **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

En la ventana emergente, haga clic en **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Espere aproximadamente un minuto. Se mostrarán las torres disponibles.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Seleccione una para ver los detalles y haga clic en **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

La señal celular quedará bloqueada en la torre seleccionada.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Nota**:

1. Es posible que el dispositivo no pueda buscar todas las torres cuando la interfaz Cellular está habilitada.

2. Si la torre bloqueada no coincide con Band Masking (si está habilitado) o con los parámetros APN de la configuración celular, el router no podrá conectarse a la red celular.

3. Si mueve el router a otra ubicación después de bloquear una torre, seguirá intentando conectarse a ella tras reiniciarse. Esto puede impedir que se conecte automáticamente a la red celular en la nueva ubicación. En ese caso, desbloquee la torre actual o bloquee manualmente una nueva.

### SMS

Consulte [SMS](../tutorials/sms.md).

### Reenvío de SMS

Consulte [SMS Forwarding](../tutorials/sms_forwarding.md).

### Modo avión

Para habilitar Airplane Mode, haga clic en el icono de engranaje de la esquina superior derecha y active **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Información del módem

Para ver los detalles del módem, haga clic en el icono de engranaje de la esquina superior derecha y seleccione **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Conmutación por error de SIM

Esta función solo está disponible en routers celulares compatibles con Dual-SIM.

SIM Failover permite que el router cambie automáticamente entre SIM 1 y SIM 2. Cuando el uso de datos de la SIM de mayor prioridad supera Data Cap Amount o esta no puede conectarse a Internet, el router cambia a la SIM de respaldo para mantener la conexión de red.

Para habilitar SIM Failover, haga clic en el icono de engranaje de la esquina superior derecha y seleccione **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

En la ventana emergente, habilite **Auto Switch**. Puede arrastrar el botón de la derecha para ajustar la prioridad de las tarjetas SIM.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Si desea que el router vuelva a la SIM preferida a una hora determinada del día, habilite **Scheduled Switch to Preferred SIM**, defina **Daily Execution Time** y haga clic en **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### Comando AT

Los comandos AT son instrucciones estándar para comunicarse con el módem celular. Con esta función puede enviar comandos y comprobar el estado del módem.

Haga clic en el icono de engranaje de la esquina superior derecha y seleccione **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: Cuando Shortcut esté configurado como **Manual command**, introduzca el comando deseado en el campo **AT Command** y haga clic en **Send** en la parte inferior. El sistema devolverá el resultado en el cuadro de salida situado debajo.

    También puede hacer clic en el cuadro y seleccionar un **preset command** de la lista desplegable.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Por ejemplo, si selecciona el acceso directo «Request SIM card status» y la ranura SIM1, haga clic en «Send» para obtener el resultado mostrado a continuación.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: Elija si el comando se aplica a SIM1 o SIM2. Las opciones disponibles dependen del número de ranuras SIM del router celular.

- **AT Command**: Introduzca el comando deseado en este campo cuando Shortcut esté configurado como «Manual command».

## Routers no celulares

Aunque los routers no celulares no disponen de un módem celular integrado, puede conectar un dongle USB externo (no incluido) a su puerto USB para obtener conectividad celular.

Los distintos dongles o módems USB pueden funcionar en modos diferentes: modo de módem USB estándar o modo host-less.

- **Modo de módem USB estándar**: En este modo, el router actúa como host USB y el dongle funciona como módem USB esclavo. Al exponer interfaces de comandos (AT/QMI/MBIM) y un puerto Ethernet USB virtual, el dongle puede gestionarse mediante la WAN Cellular nativa del router. El router puede leer métricas celulares de bajo nivel, como ICCID, intensidad de la señal y banda, y el usuario configura los ajustes de la SIM directamente desde la interfaz web del router.

- **Modo host-less**: En este modo, el dongle establece internamente la conexión celular y expone una interfaz Ethernet USB virtual al router. El router lo reconoce como una WAN mediante tethering, no como un módem controlable, por lo que la conexión se establece a través de la interfaz Tethering en lugar de Cellular. El router no dispone de métricas celulares de bajo nivel y toda la configuración relacionada con el APN y la SIM debe realizarse mediante la interfaz web integrada del dongle.

Consulte el apartado correspondiente según el modo de funcionamiento del dongle USB.

### Módem USB estándar

En esta sección se usan **Mango 2 (GL-MG1300)** y la placa de desarrollo 5G [GL-M2](https://www.gl-inet.com/products/gl-m2){target="_blank"} (módulo 5G NR: RM520N-GL) como ejemplo para explicar los pasos de configuración celular y las funciones relacionadas.

1. Inserte una tarjeta SIM en la placa GL-M2 y conecte la GL-M2 al puerto USB del router.

2. Inicie sesión en el panel de administración web del router y vaya a **INTERNET** -> **Cellular**.

    El router intentará conectarse a Internet automáticamente. Una vez establecida la conexión, la página muestra los detalles de la red y un punto verde, lo que indica que la conexión se ha realizado correctamente.

    ![m2 sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_active.png){class="glboxshadow"}

3. Configuración de la tarjeta SIM.

    Para ver la configuración de la SIM, haga clic en **SIM Card Settings**.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings1.png){class="glboxshadow"}

    Verá la configuración de la SIM detectada automáticamente, como APN, tipo de IP y tipo de red. Si cambia esta configuración, se volverá a establecer la conexión.

    ![m2 sim settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings2.png){class="glboxshadow"}

4. Información de la SIM.

    Para ver los detalles de la SIM, haga clic en **SIM Information**.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info1.png){class="glboxshadow"}

    Verá los detalles de red de la SIM, como ICCID, dirección IP, DNS, banda celular e intensidad de la señal.

    ![m2 sim info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info2.png){class="glboxshadow gl-80-desktop"}

5. SMS y SMS Forwarding.

    Para usar SMS y SMS Forwarding, consulte [SMS](../tutorials/sms.md) y [SMS Forwarding](../tutorials/sms_forwarding.md).

6. Gestión de perfiles celulares.

    Para gestionar los perfiles SIM, haga clic en el icono de engranaje de la esquina superior derecha y seleccione **Manage Cellular Profiles**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    Se mostrará el perfil que está en uso.

    ![m2 manage profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_manage_profiles.png){class="glboxshadow"}

    Haga clic en **Add a New Profile** para añadir más perfiles si es necesario.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile1.png){class="glboxshadow"}

    Introduzca los parámetros necesarios y haga clic en **Apply**.

    ![m2 add profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile2.png){class="glboxshadow"}

7. Comando AT del módem.

    Los comandos AT son instrucciones estándar para comunicarse con el módem celular. Con esta función puede enviar comandos y comprobar el estado del módem.

    Para ejecutar un comando AT, haga clic en el icono de engranaje de la esquina superior derecha y seleccione **Modem AT Command**.

    ![m2 cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    ![m2 atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_atcommand.png){class="glboxshadow"}

    - **Shortcut**: Cuando Shortcut esté configurado como **Manual command**, introduzca el comando deseado en el campo **AT Command** y haga clic en **Send** en la parte inferior. El sistema devolverá el resultado en el cuadro de salida situado debajo.

        También puede hacer clic en el cuadro y seleccionar un **preset command** de la lista desplegable.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

        Por ejemplo, si selecciona el acceso directo «Request SIM card status» y la ranura SIM1, haga clic en «Send» para obtener el resultado mostrado a continuación.

        ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

    - **SIM Slot**: Elija si el comando se aplica a SIM1 o SIM2. Las opciones disponibles dependen de las ranuras SIM del módem USB externo conectado al router.

    - **AT Command**: Introduzca el comando deseado en este campo cuando Shortcut esté configurado como «Manual command».

### Dongle host-less

En esta sección se usan **Flint 3 (GL-BE9300)** y el dongle USB externo [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} como ejemplo para explicar la configuración celular.

1. Conecte el dongle USB al puerto USB del router.

2. Inicie sesión en el panel de administración web del router, vaya a **INTERNET** -> **Tethering** y haga clic en **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Si necesita definir opciones avanzadas, como TTL, HL y MTU, haga clic en **Advanced** para personalizarlas antes de hacer clic en **Connect**.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Una vez establecida la conexión, la página muestra los detalles de red y un punto verde, lo que indica que la conexión se ha realizado correctamente.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

4. Si necesita configurar el APN y otros ajustes de la SIM instalada en SIMPoYo uFi, consulte [Gestionar SIMPoYo uFi](../user_guide/simpoyo-4g-ufi/index.md#gestionar-simpoyo-ufi).

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
