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

Aquí puede ver el estado de su eSIM y gestionar los perfiles eSIM.

Solo puede haber un perfil eSIM activo a la vez. Un punto verde indica que el perfil eSIM seleccionado está activo en ese momento.

---

Artículo relacionado:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

¿Aún tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
