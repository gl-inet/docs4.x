# Toggle Button Settings

Toggle Button Settings le permite asignar funciones específicas al interruptor físico del router (también llamado interruptor de modo en algunos modelos) para acceder y controlar rápidamente funciones habituales.

Puede personalizar el comportamiento del interruptor en el panel de administración web.

## Modelos compatibles

??? "Modelos compatibles"
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-MT1300 (Beryl)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-E750V2 (Mudi V2)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)

??? "Modelos no compatibles"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Configuración

En el lado izquierdo del panel de administración web, vaya a **SYSTEM** -> **Toggle Button Settings**.

![toggle button settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

Antes del firmware v4.8, había cinco opciones que permitían personalizar la función del interruptor.

- No Function
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

Desde el firmware v4.8, se han añadido más opciones: Repeater, Wi‑Fi y LED. Los usuarios pueden personalizar el interruptor según sus necesidades.

- No Function
- Repeater
- Wi-Fi (Main/Guest Wi-Fi)
- VPN
- Tor
- AdGuard Home
- LED

![toggle button 4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_4.8.png){class="glboxshadow"}

Al aplicar los ajustes, puede decidir si habilitar o deshabilitar inmediatamente la función seleccionada según la posición on/off (izquierda/derecha) del interruptor.

**Nota**: Después de reiniciar el dispositivo, el sistema aplicará automáticamente el estado de la función según la posición del interruptor.

Por ejemplo, si configura WireGuard Client para que se controle con el interruptor: cuando el interruptor está a la IZQUIERDA (ON), WireGuard Client se inicia automáticamente. Cuando el interruptor está a la DERECHA (OFF), WireGuard Client permanece deshabilitado.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="_blank"}.
