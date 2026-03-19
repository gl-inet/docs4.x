# NAT Settings

Esta función está disponible desde la versión v4.5.16.

En el lado izquierdo del panel web de administración, vaya a **NETWORK** -> **NAT Settings**.

Esta página le permite habilitar **Full Cone NAT** para mejorar la estabilidad de las conexiones peer-to-peer en aplicaciones como juegos o streaming, y **SIP ALG** para corregir problemas de compatibilidad con servicios telefónicos basados en VoIP/SIP.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Modelos compatibles

??? "Supported Models" - GL-E5800 (Mudi 7) - GL-MT5000 (Brume 3) - GL-MT3600BE (Beryl 7) - GL-BE6500 (Flint 3e) - GL-BE9300 (Flint 3) - GL-BE3600 (Slate 7) - GL-X2000 (Spitz Plus) - GL-B3000 (Marble) - GL-MT6000 (Flint2) - GL-AX1800 (Flint) - GL-X3000 (Spitz AX) - GL-XE3000 (Puli AX) - GL-MT2500/GL-MT2500A (Brume 2) - GL-MT3000 (Beryl AX) - GL-AXT1800 (Slate AX) - GL-A1300 (Slate Plus) - GL-X300B (Collie) - ※GL-SFT1200 (Opal) - ※GL-E750/E750V2 (Mudi)

    **Nota**: GL-SFT1200 (Opal) y GL-E750/E750V2 (Mudi) admiten esta función con firmware v4.7 y posteriores.

??? "Unsupported Models" - GL-MT1300 (Beryl) - GL-AR750 (Creta) - GL-AR750S (Slate) - GL-MT300N-V2 (Mango) - GL-AR300M Series (Shadow) - GL-X750/GL-X750V2 (Spitz) - GL-XE300 (Puli) - GL-B1300 (Convexa-B)

## Full Cone NAT

**Full Cone NAT** actúa como un "atajo directo" para dispositivos como consolas de videojuegos o teléfonos cuando se conectan con otros dispositivos en línea, por ejemplo en juegos multijugador o videollamadas.

Al permitir que los dispositivos externos lleguen directamente a los dispositivos locales a través del router, en lugar de ocultarlos tras múltiples capas, mejora la estabilidad de las conexiones peer-to-peer (P2P), reduce la latencia y resuelve fallos de conexión en aplicaciones P2P.

**Nota**: Habilitar esta función puede reducir la seguridad en comparación con otros tipos de NAT, ya que expone los puertos del dispositivo a la red pública.

## SIP ALG

**SIP ALG** (Application Layer Gateway) funciona como un "traductor" del router para servicios de comunicación basados en VoIP/SIP, como teléfonos de oficina o llamadas realizadas desde aplicaciones.

Diseñado para abordar los desafíos del cruce de NAT, ajusta los datos de las llamadas para garantizar una transmisión fluida a través de múltiples capas NAT, algo habitual en redes con varios routers, por ejemplo un router principal y un router GL.iNet, reduciendo así conflictos y evitando interrupciones en las llamadas.

**Nota**: Un SIP ALG incompatible o mal implementado puede degradar la calidad de la llamada y provocar problemas como audio en un solo sentido, timbrado sin respuesta, llamadas cortadas o llamadas dirigidas directamente al buzón de voz.

---

¿Aún tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
