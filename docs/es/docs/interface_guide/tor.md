# Tor

Tor, derivado de **The Onion Router**, es un software gratuito y de código abierto que permite la comunicación anónima. Ayuda a los usuarios a explorar Internet con mayor privacidad. [Más información sobre Tor](https://www.torproject.org/){target="\_blank"}.

**Nota**: Esta función se encuentra actualmente en fase beta y puede presentar problemas en algunos países. Cuando Tor está habilitado, las siguientes funciones no funcionarán correctamente:

- VPN
- DNS
- IPv6
- ADGuard Home.

## Modelos compatibles

??? "Modelos compatibles" - GL-MT3600BE (Beryl 7) - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-AX1800 (Flint) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus) - GL-AP1300 (Cirrus) - GL-S1300 (Convexa-S) - *GL-SFT1200 (Opal) - *GL-MT1300 (Beryl) - \*GL-E750/E750V2 (Mudi)

    **Nota**: Los modelos marcados con * no admiten Tor de forma nativa, pero los usuarios pueden instalarlo manualmente mediante un plug-in. Haga clic [aquí](#instalacion-manual) para obtener más detalles.

??? "Modelos no compatibles" - GL-X2000 (Spitz Plus) - GL-AR750S (Slate) - GL-X750/GL-X750V2 (Spitz) - GL-XE300 (Puli) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-B1300 (Convexa-B) - GL-X300B (Collie)

## Configuración rápida

En el lado izquierdo del panel de administración web, vaya a **VPN** -> **Tor**.

En el firmware v4.8.4 y posteriores, vaya a **APPLICATIONS** -> **Tor**.

Haga clic en el interruptor para habilitarlo, active **Custom Exit Nodes** si es necesario y, a continuación, haga clic en **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

Comenzará a conectarse. Si su red cumple los requisitos, se mostrará como conectado.

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## Instalación manual

**Nota**: En algunos modelos, Tor puede instalarse manualmente mediante un plug-in, pero esto puede aumentar la carga de la CPU y ralentizar la respuesta del sistema.

En el lado izquierdo del panel de administración web, vaya a **APPLICATIONS** -> **Plug-ins**.

Busque **gl-sdk4-ui-torview** e instálelo.

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

¿Todavía tiene preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
