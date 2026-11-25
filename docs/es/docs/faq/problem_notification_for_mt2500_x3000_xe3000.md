# Notificación de problema para GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Última actualización: 11 de noviembre de 2026**

Este problema conocido afecta únicamente a determinados lotes de dispositivos. Es muy probable que los dispositivos pedidos a partir del 1 de julio de 2025 pertenezcan a lotes más recientes y no necesiten actualizar el gestor de arranque U-Boot.

Si no sabe a qué lote pertenece su dispositivo, envíe los siguientes datos a [support@gl-inet.com](mailto:support@gl-inet.com) antes de realizar cambios.

- Modelo del router y versión del firmware
- Dirección MAC del dispositivo
- Descripción del problema, con lo que estaba haciendo cuando ocurrió, los mensajes de error y las medidas que ya ha probado para solucionarlo

Confirmaremos el lote de fabricación y le indicaremos cómo solucionar el problema en su caso.

---

A continuación se conserva el aviso original como referencia. Los pasos de actualización solo se aplican a los lotes afectados. Si tiene dudas sobre si el problema afecta a su dispositivo, póngase en contacto con el equipo de soporte como se indica arriba antes de realizar cambios.

**Publicación: 26 de marzo de 2025**

Estimados clientes de GL.iNet:

Este anuncio trata los fallos de arranque y los problemas de recuperación de firmware mediante U-Boot en los dispositivos GL-MT2500/GL-X3000/GL-XE3000. El problema se originó por un defecto de software en el que algunos parámetros se definieron incorrectamente, lo que provocó un funcionamiento anómalo de los routers. Como consecuencia, evaluamos que este problema podría reducir en cierta medida la vida útil de los equipos, por lo que les pedimos disculpas sinceramente.

Para resolver completamente este problema, recomendamos encarecidamente que todos los usuarios de GL-MT2500, GL-X3000 y GL-XE3000 realicen tanto una actualización del bootloader U-Boot como una actualización de firmware. Ambos procedimientos son esenciales y no deben omitirse.

Aunque su dispositivo ya se haya actualizado a la última versión del firmware, la actualización del bootloader U-Boot sigue siendo obligatoria para evitar posibles problemas. Tras completar la actualización del bootloader U-Boot, si la última versión del firmware ya está instalada, puede omitir la reinstalación del firmware.

Intente realizar la actualización con Chrome o Microsoft Edge. NO use Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}. A continuación, [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [la última versión del firmware para su router](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"}. A continuación, [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}. A continuación, [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [la última versión del firmware para su router](https://dl.gl-inet.com/router/x3000/stable){target="_blank"}. A continuación, [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}. A continuación, [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [la última versión del firmware para su router](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"}. A continuación, [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Lamentamos sinceramente cualquier inconveniente que esto haya podido causar. A partir de ahora, nos comprometemos a mejorar nuestros productos y firmware con mayor diligencia y cuidado.

Para quienes ya poseen estos routers, ampliaremos el período de garantía un año adicional sin coste alguno. Si encuentra cualquier problema, no dude en ponerse en contacto con nuestros equipos de soporte.

Si el problema persiste a pesar de la actualización, contacte con nuestros equipos de soporte a través de [support@gl-inet.com](mailto:support@gl-inet.com) y le proporcionaremos un reemplazo nuevo sin coste.

Su confianza y apoyo significan muchísimo para nosotros, y le estamos profundamente agradecidos por ello.

<br>
Atentamente,<br>
Equipo de GL.iNet<br>
26 de marzo de 2025
