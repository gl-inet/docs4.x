# Reenvío de SMS

Los routers celulares GL.iNet admiten el reenvío de SMS y envían automáticamente los mensajes entrantes a los destinatarios designados.

**Nota**: Esta función solo funciona en routers celulares GL.iNet con el módulo 4G LTE/5G NR original. No es compatible con otros módulos ni con ningún otro módulo USB.

## Modelos compatibles

??? "Modelos compatibles"
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Modelos no compatibles"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)

## Configuración

Tomemos el GL-XE3000 (Puli AX) como ejemplo.

En el lado izquierdo del panel de administración web, vaya a **INTERNET** -> **Cellular**.

Haga clic en el icono del sobre situado en la esquina superior derecha para entrar en la página de SMS. Allí encontrará la configuración de **SMS Forwarding**.

![sms setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sms.png){class="glboxshadow"}

### Reenviar por correo electrónico

![sms forwarding email](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: En la lista desplegable hay direcciones de servidor predefinidas para Gmail, Outlook, iCloud y Yahoo. Para otros proveedores de correo, consulte su documentación o contacte con su soporte.
- **Encryption Method**: Hay tres opciones disponibles: none, SSL/TLS y STARTTLS.
- **Username**: Introduzca aquí la dirección de correo electrónico.
- **Password**: Use una contraseña específica de la aplicación o la contraseña de la cuenta de inicio de sesión. Para Gmail, Outlook, iCloud y Yahoo, consulte la guía siguiente.
- **Subject**: Defina aquí el asunto del correo.

??? "Gmail"

    Para Gmail, debe iniciar sesión en su cuenta de Google y crear una **App Passwords**. Consulte la guía oficial [Sign in with App Passwords](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Antes de crear la **App Passwords**, debe habilitar la verificación en dos pasos.

    Se pueden usar los puertos 465 y 587.

??? "Outlook"

    Para Outlook, puede usar la contraseña directamente sin ninguna configuración adicional, y es compatible con el puerto 587. Consulte la guía oficial [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}.

??? "iCloud"

    Para iCloud, debe crear una contraseña específica de la aplicación para iniciar sesión, y es compatible con el puerto 587. Consulte la guía oficial [iCloud Mail server settings for other email client apps](https://support.apple.com/en-hk/HT202304){target="_blank"} y [Generate an app-specific password](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Para Yahoo, debe configurar una contraseña de aplicación para iniciar sesión, y admite tanto el puerto 465 como el 587. Consulte la guía oficial [POP access settings and instructions for Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} y [Generate and manage third-party app passwords](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Nota**: Cada remitente de correo puede estar sujeto a límites de envío SMTP, por ejemplo, un límite diario en el número de correos enviados. Consulte a su proveedor de servicios.

Puede añadir hasta 10 direcciones de correo electrónico.

### Reenviar por SMS

![sms forwarding phone](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Seleccione el prefijo nacional, introduzca el número de teléfono y haga clic en **Apply**.

Puede añadir hasta 10 números de teléfono móvil.

---

Artículos relacionados

- [SMS](../interface_guide/sms.md)

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
