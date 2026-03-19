# ¿Cómo actualizar al firmware 4.x?

**Este documento está desactualizado y ya no se mantiene. Haga clic [aquí](../interface_guide/upgrade.md) para consultar la guía de actualización más reciente.**

---

Siga los pasos que se indican a continuación para actualizar su router del firmware 3.x al 4.x.

Nota: No conserve la configuración al actualizar de v3.x a v4.x, ya que esto puede causar inestabilidad. Haga una copia de seguridad de cualquier configuración crítica antes de actualizar.

Los modelos GL-B1300 y GL-S1300 no admiten la función mesh en el firmware v4.x.

---

## Método 1. Actualización local

Puede actualizar el firmware a través del panel de administración web.

1. Actualice el firmware a la última versión estable 3.x.

2. Descargue el firmware 4.x [aquí](https://dl.gl-inet.com){target="\_blank"}. Asegúrese de **descargar el destinado a common upgrade**.

3. Inicie sesión en el panel de administración web, vaya a **Upgrade** -> **Local Upgrade**. Cargue el archivo de firmware que acaba de descargar.

   **Nota:** El firmware 4.x no es compatible con el firmware 3.x. Al actualizar desde el firmware 3.x, **NO** conserve la configuración.

   ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

## Método 2. Actualización mediante U-Boot

1. Descargue el firmware 4.x [aquí](https://dl.gl-inet.com){target="\_blank"}. Asegúrese de **descargar el destinado a U-Boot**.

2. Consulte esta guía de [U-Boot](debrick.md) para flashear el firmware.

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
