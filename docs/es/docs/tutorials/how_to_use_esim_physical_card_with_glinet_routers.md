# ¿Cómo usar la eSIM Physical Card con routers GL.iNet?

Esta guía le muestra cómo usar con routers GL.iNet la eSIM Physical Card adquirida en la tienda en línea de GL.iNet.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Características

Los puntos destacados de la eSIM Physical Card son los siguientes:

- Admite redes 4G y 5G para conexiones rápidas y fiables.
- Permite gestionar fácilmente sus perfiles eSIM, ya sea para añadirlos, eliminarlos o habilitarlos.
- Permite seleccionar y comprar en cualquier momento los paquetes de datos que prefiera en la mayoría de las tiendas eSIM del mundo.
- Funciona con perfiles eSIM de la mayoría de las tiendas eSIM internacionales.
- Permite comprar perfiles eSIM en línea sin proporcionar información personal, lo que reduce el riesgo de vulneraciones de privacidad.
- Incluye un perfil inicial con 1 GB de datos gratuitos para EE. UU. y Europa, además de 100 MB de Global Data, válidos durante 1 año a partir de la fecha de activación.
- Es compatible con determinados dispositivos GL.iNet.

## Modelos compatibles

| Modelo de router      | Compatibilidad |
| :-------------------- | :------------: |
| GL-X2000 (Spitz Plus) |       √        |
| GL-X3000 (Spitz AX)   |       √        |
| GL-XE3000 (Puli AX)   |       √        |
| GL-E750V2 (Mudi V2)   |       √        |
| GL-E750 (Mudi)        |       ※        |
| GL-XE300 (Puli)       |       ※        |
| GL-X750 (Spitz)       |       ※        |
| GL-X300B (Collie)     |       ※        |
| GL-E750V2 vSIM        |       X        |
| GL-E5800 (Mudi 7)     |       X        |

**Para los modelos marcados con ※**:

1. El firmware estable actual no admite eSIM. Para usar la función eSIM, debe instalar firmware compatible con eSIM. [Contact us](https://www.gl-inet.com/contacts/){target="\_blank"} para obtener más instrucciones.

2. Si usa un modelo marcado con ※ equipado con el módulo EP06-A, la eSIM no es compatible porque el software de Qualcomm no admite determinados comandos AT.

3. Si usa un modelo marcado con ※ equipado con el módulo EP06-E, consulte [este enlace](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="\_blank"} para actualizar el firmware del módulo e instalar firmware compatible con eSIM a fin de habilitar esta función.

**Para los modelos marcados con X**:

1. GL-E750V2 vSIM no admite la función eSIM.

2. GL-E5800 (Mudi 7) incorpora una eSIM integrada. Por lo tanto, en Mudi 7 la eSIM Physical Card se reconocerá como una tarjeta SIM normal, sin funcionalidad eSIM.

## Configurar la eSIM Physical Card

Si usa la eSIM Physical Card por primera vez, vea este vídeo de configuración o siga los pasos indicados a continuación para configurarla en su router GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Paso 1:** Inserte la eSIM Physical Card en su router. Consulte las siguientes imágenes para ver una guía detallada.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Paso 2:** Abra un navegador y escriba `192.168.8.1` en la barra de direcciones para iniciar sesión en el panel de administración de GL.iNet.

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Paso 3:** Conecte su dispositivo a Internet.

Vaya a **INTERNET** y haga clic en **Connect** para conectarse a Internet mediante la red celular. En versiones de firmware antiguas, la opción puede mostrarse como **Auto Setup**.

_Esta eSIM Physical Card incluye un perfil inicial con 1 GB de datos gratuitos para EE. UU. y Europa, además de 100 MB de Global Data, válidos durante 1 año desde la fecha de activación. Tenga en cuenta que estos datos solo están pensados para comprar y descargar perfiles eSIM, y no para el acceso general a Internet._

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Si la conexión a Internet se establece correctamente, la pantalla aparecerá de la siguiente manera.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Gestionar su perfil eSIM

**Paso 1:** Asegúrese de que su dispositivo GL.iNet tenga instalado el firmware más reciente.

Verifique que la Version sea 4.0 o superior y que el número de Firmware Type sea 0319 o mayor.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Si su firmware **no está actualizado**, puede actualizarlo automáticamente en línea o manualmente.

<u>Opción 1</u>: Actualización de firmware en línea

1. Asegúrese de que su dispositivo esté conectado a Internet.

2. En el panel de administración web, vaya a **SYSTEM** > **Upgrade** > **Online Upgrade** y haga clic en **Install** para actualizar automáticamente al firmware más reciente.

   ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Opción 2</u>: Actualización manual del firmware

1. Descargue desde [aquí](https://dl.gl-inet.com/){target="\_blank"} el firmware correspondiente al modelo compatible con la función eSIM.

2. En el panel de administración web, vaya a **SYSTEM** > **Upgrade** > **Local Upgrade**. Seleccione el archivo de firmware o arrástrelo al área designada para actualizar a la versión más reciente.

   ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Algunos modelos, como Mudi (GL-E750), Puli (GL-XE300) y Spitz (GL-X750), no admiten eSIM si están equipados con módulos Quectel EP06-A, porque el software de Qualcomm no admite determinados comandos AT.

    2. Si tienen instalado un módulo EP06-E, consulte [este enlace](https://forum.gl-inet.com/t/48907){target="_blank"} para actualizar el módulo al software más reciente compatible con la función eSIM.

**Paso 2:** Vaya a eSIM Management.

Después de actualizar el firmware, espere a que el dispositivo se reinicie y luego vuelva a iniciar sesión en el panel de administración de GL.iNet.

Vaya a **APPLICATIONS** > **eSIM Management**. Allí podrá ver el estado actual de su eSIM.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Solo puede haber un perfil eSIM activo a la vez. Un punto verde indica que el perfil eSIM seleccionado está activo en ese momento.

## Guía de eSIM Management

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. Current eSIM Status:**

Esta sección muestra la información básica de la eSIM y los detalles del perfil activo actualmente.

- **EID:** Identificador único global del eUICC, es decir, el chip eSIM, utilizado para la identificación y el control de perfiles.
- **ICCID:** Integrated Circuit Card Identifier del perfil eSIM activo actualmente.
- **IMSI:** International Mobile Subscriber Identity del perfil eSIM activo actualmente.
- **eSIM OS Version:** Versión del sistema operativo del eUICC que define su compatibilidad y capacidades.
- **eSIM Storage (remain/total):** Capacidad disponible y total de almacenamiento en el eUICC para guardar perfiles eSIM.
- **eSIM Profile Number:** Número de perfiles eSIM almacenados actualmente en el eUICC.

**B. Seed Profile:**

Esta sección ofrece detalles sobre el perfil inicial. El perfil inicial viene precargado con 1 GB de datos gratuitos para EE. UU. y Europa, además de 100 MB de datos globales, válidos durante 1 año desde la fecha de activación. Estos datos le permiten descargar otros perfiles a nivel global. También puede supervisar el uso del perfil inicial, incluidos los datos restantes, los datos totales y la fecha de vencimiento.

**C. Normal Profile:**

Esta sección muestra la información de los perfiles normales. Si compra un perfil eSIM en una tienda en línea y carga el código QR mediante la función **Add eSIM Profile (QR Code Install)**, el perfil aparecerá aquí cuando se complete la carga.

**D. Add eSIM Profile (QR Code Install):**

Esta es la función principal para cargar e instalar perfiles eSIM. Cuando compra un perfil eSIM en una tienda en línea, recibirá un código QR. Haga clic en este botón para cargar el código QR; después, el router descargará e instalará el perfil eSIM.

**E. Export Log for Support:**

Esta sección le permite ver todos los registros relacionados con el funcionamiento de la eSIM. Si encuentra algún problema y necesita soporte técnico, puede exportar esos registros y compartirlos con nuestro equipo de soporte por correo electrónico en support@gl-inet.com.

**F. Top-up:**

Si agota los datos de cortesía y precargados proporcionados por GL.iNet, o si esos datos caducan y desea seguir usando el servicio, puede hacer clic en **Top-up** para escanear un código QR y comprar datos adicionales.

**G. Recommended eSIM Profile Stores:**

Para su comodidad, GL.iNet recomienda dos tiendas eSIM asociadas: EIOTCLUB y Tuge. Puede escanear los códigos QR o hacer clic en los enlaces, [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="\_blank"} o [the Tuge eSIM Store](https://esim_store.gl-inet.com/){target="\_blank"}, para comprar según sus necesidades. También puede optar por comprar paquetes eSIM de otros proveedores externos de su elección.

**H. Actions:**

Esta sección le permite gestionar fácilmente los perfiles eSIM, incluyendo habilitarlos, cambiarlos o eliminarlos.

## Recargar el perfil inicial eSIM

Para la configuración inicial o para comprar un perfil eSIM, GL.iNet proporciona datos precargados: 100 MB para uso global y 1 GB para Europa y EE. UU. Estos planes están diseñados con un coste más alto y están pensados para situaciones en las que necesite descargar un nuevo perfil eSIM al llegar a un lugar sin acceso a Internet.

Para recargar su perfil inicial eSIM, basta con hacer clic en **Top-up**, escanear el código QR y seguir las instrucciones.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## Comprar e instalar un perfil eSIM

Después de configurar el router, siga los pasos indicados a continuación para comprar y activar su perfil eSIM.

**Paso 1:** Compre un perfil eSIM en una tienda eSIM.

<u>Opción 1</u>: Compre un perfil eSIM en una de nuestras tiendas recomendadas, [the EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="\_blank"} o [the Tuge eSIM Store](https://esim_store.gl-inet.com){target="\_blank"}. Consulte la siguiente imagen para acceder a los enlaces directos a las tiendas.

_Todos los paquetes de perfiles eSIM comprados en estas dos tiendas son totalmente compatibles con nuestros routers. Si tiene alguna duda, contacte con nuestro equipo de soporte en support@gl-inet.com._

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Opción 2</u>: Consulte [este enlace](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="\_blank"} para obtener una lista de tiendas probadas por GL.iNet. Tenga en cuenta que no podemos garantizar que todos los paquetes de estas tiendas sean totalmente compatibles con los routers GL.iNet.

_Como GL.iNet no mantiene acuerdos con estas tiendas, no podemos ayudar con soporte posventa ni reembolsos relacionados con esos paquetes._

<u>Opción 3</u>: Compre un perfil eSIM a otros proveedores externos de su elección.

**Paso 2:** Instale su perfil eSIM.

Después de comprar el perfil eSIM, recibirá un código QR. Guarde ese código QR en su ordenador. A continuación, haga clic en **Add eSIM Profile (QR Code Install)** para cargar e instalar el perfil eSIM que ha comprado.

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Nota:** Como muestra la flecha verde en la imagen anterior, un código QR con el formato correcto mostrará un código de activación que comienza por **LPA:**.

_Sin embargo, algunos códigos QR no estándar pueden generar solo un código de activación sin el prefijo LPA. Si eso ocurre, añada manualmente `LPA:` al principio del código antes de hacer clic en **Download & Install**._

**Paso 3:** Habilite su nuevo perfil.

Una vez cargado correctamente el código QR, verá su nuevo perfil eSIM en la sección **Normal Profile**. Haga clic en **Enable** para activarlo.

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Paso 4:** Aplique su nuevo perfil eSIM y conéctese a Internet.

Después de habilitar su perfil eSIM, vaya a **INTERNET** y haga clic en **Connect** para aplicarlo y conectarse a Internet.

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

_Nota: Algunos perfiles eSIM pueden requerir ajustes adicionales, como APN, PIN o TTL. Si es necesario, haga clic en **Manual Setup** o **SIM Card Settings** para configurar estos parámetros. En algunos casos, puede ser necesario reiniciar el dispositivo para establecer la conexión a Internet._

Una vez configurado correctamente el perfil eSIM, la pantalla aparecerá de la siguiente manera:

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Paso 5:** Cambie o elimine perfiles eSIM fácilmente.

Puede cambiar fácilmente entre perfiles eSIM haciendo clic en **Enable** junto al perfil que quiera activar. Para eliminar un perfil eSIM, solo tiene que hacer clic en **Delete**.

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

¿Aún tiene preguntas? Visite nuestro [Community Forum](https://forum.gl-inet.com){target="\_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="\_blank"}.
