# Gestión de eSIM

En el lado izquierdo del panel de administración web, vaya a **APPLICATIONS** -> **eSIM Management**.

Esta página le permite comprobar el estado de la eSIM Physical Card y gestionar perfiles eSIM. Consta de dos partes: **Current eSIM Status** y **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Modelos compatibles

| Modelo de router      | Compatibilidad |
| :-------------------- | :------------: |
| GL-X2000 (Spitz Plus) |       √        |
| GL-X3000 (Spitz AX)   |       √        |
| GL-XE3000 (Puli AX)   |       √        |
| GL-E750V2 (Mudi V2)   |       √        |
| GL-E750 (Mudi)        |       √        |
| GL-XE300 (Puli)       |       ※        |
| GL-X750 (Spitz)       |       ※        |
| GL-X300B (Collie)     |       ※        |
| GL-E750V2 vSIM        |       X        |
| GL-E5800 (Mudi 7)     |       X        |

**Para los modelos marcados con ※**:

1. El firmware estable actual no admite eSIM. Para usar esta función, debe instalar firmware compatible con eSIM. [Póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"} para obtener más instrucciones.

2. En los modelos marcados con ※ que usan el módulo EP06-A, la eSIM no es compatible porque el software de Qualcomm no admite los comandos AT necesarios.

3. En GL-E750 (Mudi) y en los modelos marcados con ※ que usan el módulo EP06-E, consulte [este enlace](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} para actualizar primero el firmware del módulo y luego instalar el firmware compatible con eSIM para habilitar la función.

**Para los modelos marcados con X**:

1. GL-E750V2 vSIM no admite la función eSIM.

2. GL-E5800 (Mudi 7) incorpora una eSIM integrada. Por lo tanto, en Mudi 7 la eSIM Physical Card se reconocerá como una tarjeta SIM normal, sin funcionalidad eSIM.

## Current eSIM Status

Esta sección muestra información básica y detalles sobre el perfil eSIM activo en ese momento.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Identificador único global del eUICC (chip eSIM), utilizado para la identificación y la gestión de perfiles.
- **ICCID:** Integrated Circuit Card Identifier del perfil eSIM activo actualmente.
- **IMSI:** International Mobile Subscriber Identity del perfil eSIM activo actualmente.
- **eSIM OS Version:** Versión del sistema operativo del eUICC, que define su compatibilidad y las capacidades que admite.
- **eSIM Storage (remain/total):** Capacidad disponible y total del eUICC para almacenar perfiles eSIM.
- **eSIM Profile Number:** Número de perfiles eSIM almacenados actualmente en el eUICC. Tenga en cuenta que los perfiles eSIM ofrecidos por distintos operadores varían en tamaño, por lo que la cantidad que puede almacenarse en el eUICC también variará.

## eSIM Profile List

Esta sección muestra información sobre el seed profile y los perfiles normales.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: El seed profile viene precargado con 1 GB de datos gratuitos para EE. UU. y Europa, además de 100 MB de Global Data, válidos durante 1 año desde la fecha de activación. Estos datos le permiten descargar otros perfiles en cualquier parte del mundo. También puede supervisar su uso, incluidos los datos restantes, la asignación total y la fecha de caducidad.

- **Normal Profile**: Si compra un perfil eSIM y lo carga mediante un código QR o un código de activación, el perfil aparecerá aquí.

### Recargar el seed profile

GL.iNet ofrece un seed profile precargado con 100 MB de Global Data y 1 GB de datos válidos en Europa y EE. UU. para la configuración inicial y la activación de perfiles eSIM. Este plan está pensado para descargar nuevos perfiles eSIM cuando llegue a un destino sin acceso a Internet.

Si ya ha consumido los datos gratuitos precargados, o si estos han caducado y desea seguir usando el servicio, puede recargar su seed profile.

En la sección **Seed Profile**, haga clic en el botón **Top-up** que aparece a la derecha.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

En la ventana emergente, escanee el código QR y siga las instrucciones para completar la recarga.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Comprar un perfil eSIM

Puede comprar perfiles eSIM en nuestras tiendas recomendadas, en tiendas probadas o en otros proveedores externos de eSIM.

??? note "Opción 1: Comprar en nuestras tiendas recomendadas"

    Hay dos tiendas recomendadas: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} y [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    En la sección **Normal Profile**, haga clic en **eSIM Profile Recommended Store** a la derecha.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Escanee el código QR o haga clic en los enlaces para comprar perfiles eSIM.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Nota**: Todos los paquetes de perfiles eSIM comprados en estas dos tiendas son totalmente compatibles con los routers GL.iNet. Si tiene alguna duda, contacte con nuestro equipo de soporte en [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Opción 2: Comprar en tiendas probadas"

    Consulte [este enlace](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} para ver una lista de tiendas probadas por GL.iNet.

    **Nota**: No podemos garantizar la compatibilidad total con los routers GL.iNet de todos los perfiles o paquetes de estas tiendas. Como GL.iNet no mantiene acuerdos con ellas, no podemos ofrecer soporte posventa ni ayudar con reembolsos.

??? note "Opción 3: Comprar a otros proveedores externos de eSIM"

    También puede optar por comprar perfiles eSIM a otros proveedores externos de su elección.

    Sin embargo, no podemos garantizar la compatibilidad total con los routers GL.iNet de los perfiles eSIM adquiridos a otros proveedores externos. Realice la compra bajo su propio criterio. GL.iNet no se hace responsable de problemas de incompatibilidad.

    Para soporte posventa o reembolsos, póngase en contacto con el proveedor eSIM correspondiente.

### Cargar un perfil eSIM

Después de comprar un perfil eSIM, normalmente recibirá un código QR o un código de activación. Guarde ese código QR localmente y siga los pasos siguientes para cargar su perfil eSIM.

1. En la sección **Normal Profile**, haga clic en **Add eSIM Profile** en la parte inferior.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Cargue el código QR de su eSIM o introduzca el código de activación y, a continuación, haga clic en **Install**. Después se descargará e instalará el perfil eSIM en el router.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Nota:**

    1. La mayoría de los perfiles eSIM solo pueden descargarse e instalarse una vez.

    2. Un código QR con el formato correcto mostrará un código de activación que empieza por **LPA:**. Sin embargo, algunos códigos QR no estándar pueden proporcionar solo un código de activación sin el prefijo LPA. En ese caso, añada manualmente `LPA:` al principio del código antes de hacer clic en **Install**.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Si aún no ha comprado ningún perfil eSIM, puede adquirirlo en **eSIM Profile Recommended Store**. Haga clic [aquí](#comprar-un-perfil-esim) para ver los detalles.

3. Habilite su perfil eSIM.

    Después de cargarlo correctamente, el nuevo perfil eSIM aparecerá en la lista **Normal Profile**. Haga clic en **Enable** para activarlo.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Conéctese a Internet.

    Después de activar su perfil eSIM, vaya a **INTERNET** -> **Cellular**. Haga clic en **Connect** para establecer una conexión a Internet mediante su perfil eSIM.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Nota**: Algunos perfiles eSIM pueden requerir configuraciones adicionales, como APN, PIN o TTL. Si es necesario, haga clic en **Manual Setup** o **SIM Card Settings** para ajustar esos parámetros. En algunos casos, puede ser necesario reiniciar el dispositivo para establecer la conexión a Internet.*

5. Una vez que el router se conecte correctamente mediante el perfil eSIM, la página se mostrará de la siguiente manera:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Exportar registros para soporte

Haga clic en **Export Log for Support** para ver todos los registros relacionados con la eSIM. Si encuentra algún problema y necesita soporte técnico, exporte los registros de eSIM y compártalos con nuestro equipo de soporte por correo electrónico en [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Artículos relacionados:

- [¿Cómo usar la eSIM Physical Card con routers GL.iNet?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [¿Cómo usar la eSIM Physical Card con dispositivos Android?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Si todavía tiene preguntas, visite nuestro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
