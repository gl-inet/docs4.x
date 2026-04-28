# ¿Qué debo hacer si falla la instalación del perfil eSIM?

Si intenta añadir un perfil eSIM en su router GL.iNet pero la instalación falla, consulte los siguientes pasos de solución de problemas:

1. Asegúrese de que el router esté conectado a Internet.

    Compruebe que el router se haya conectado correctamente a Internet. Una red inestable puede afectar a la carga del perfil eSIM y hacer que el router no pueda obtenerlo ni instalarlo.

    Si es posible, pruebe a conectar el router a otra fuente de red, como el hotspot de su smartphone o una red Wi-Fi pública, y luego vuelva a cargar el perfil eSIM para comprobarlo.

2. Cambie la configuración de DNS.

    Si Internet funciona correctamente, inicie sesión en el panel de administración web del router y vaya a **NETWORK** -> **DNS**.

    Cambie el modo DNS a **Manual DNS** y configure otros servidores DNS públicos para probar, como Google DNS (`8.8.8.8`, `8.8.4.4`) o Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Haga clic en **Apply** para guardar los cambios y vuelva a intentar cargar el perfil eSIM.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Desactive AdGuard Home.

    Si AdGuard Home está disponible y habilitado en el router, desactívelo e intente instalar de nuevo su perfil eSIM.

4. Compruebe la disponibilidad del perfil eSIM.

    Verifique si ese perfil eSIM o código QR ya se ha activado o instalado en otro dispositivo.

    La mayoría de los perfiles eSIM solo pueden instalarse una vez y no pueden activarse en varios dispositivos. Si es posible, contacte con su proveedor eSIM para confirmar si el perfil actual sigue disponible. Si el código QR o el código de activación ha caducado, solicite uno nuevo y vuelva a intentarlo.

5. Compruebe el código de activación.

    Un código QR con el formato correcto mostrará un código de activación que empieza por **LPA:**. Sin embargo, algunos códigos QR no estándar pueden proporcionar solo un código de activación sin el prefijo LPA. En ese caso, añada manualmente `LPA:` al principio del código antes de hacer clic en **Install**.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Compruebe si se requiere un código de confirmación.

    Algunos perfiles eSIM requieren introducir un código de confirmación durante la instalación, como Smarty eSIM. Revise su paquete eSIM o la guía de instalación para verificar si se necesita un código de confirmación. Si es así, introduzca el código correcto.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Si los pasos anteriores no resuelven el problema, exporte el registro eSIM desde la página **eSIM Management**.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Después, envíe el registro junto con la información clave siguiente a [support@gl-inet.com](mailto:support@gl-inet.com) para obtener más ayuda.

    - El problema que ha encontrado
    - Los métodos de solución de problemas que ya ha probado
    - Su proveedor eSIM

---
