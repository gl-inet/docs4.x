# ¿Cómo reparar la red o restablecer a fábrica?

Todos los routers GL.iNet están equipados con un mecanismo físico de restablecimiento, ya sea un botón de reset o un orificio para pin. Pulsar el botón o insertar el pin produce el mismo efecto: restaurar la conectividad de red o restablecer el router a los valores de fábrica.

En los modelos con orificio para pin, use un pin, un clip enderezado o una herramienta similar para realizar la acción.

Asegúrese de que el router haya arrancado completamente antes de realizar el restablecimiento. **NO** pulse el botón de reset inmediatamente después de encenderlo, ya que esto puede activar el modo failsafe de U-Boot.

## Reparar la red

Mantenga pulsado el botón de reset durante **4 segundos** y luego suéltelo para realizar un restablecimiento suave, que puede reparar la red.

Esta operación reiniciará la interfaz de red y restaurará la interfaz de Internet a la configuración predeterminada, conservando la configuración de Wi-Fi, la configuración de VPN, la configuración del sistema, etc.

**Nota**:

1. Si el Wi-Fi ha sido deshabilitado, un restablecimiento suave volverá a activarlo con su estado predeterminado.

2. Un restablecimiento suave también puede utilizarse para cambiar rápidamente del modo no router al modo router.

## Restablecer a fábrica

Vea este vídeo o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jguDqBWP-Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Hay dos formas de restablecer el firmware.

1. Usar el mecanismo físico de restablecimiento, botón o pinhole.

   Mantenga pulsado el botón de reset, o inserte un pin en el pinhole, durante **10 segundos** y luego suéltelo para restablecer el router a los valores de fábrica. Se borrarán todos los datos del usuario.

   **Nota:** Si el restablecimiento de fábrica no funciona, puede que tenga que seguir el [tutorial de Uboot](debrick.md) para recuperar su router.

2. Restablecer el firmware desde el panel de administración web.

   Inicie sesión en el panel de administración web del router y vaya a SYSTEM -> Reset Firmware. Haga clic en el botón para restablecer el firmware.

   **Nota:** Se perderán todos sus ajustes y datos actuales. El proceso tardará unos 2 minutos. NO apague el router durante este proceso.

   ![glinet reset firmware](https://static.gl-inet.com/docs/router/en/4/tutorials/reset_firmware/reset_firmware_4.8.png){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
