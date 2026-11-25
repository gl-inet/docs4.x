# Aviso sobre un problema en GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Última actualización: 11 de noviembre de 2026**

Este problema conocido solo afecta a determinados lotes. Lo más probable es que los dispositivos pedidos a partir del 1 de julio de 2025 sean de un lote más reciente y no requieran actualizar el gestor de arranque U-Boot.

Si desconoce el lote de su dispositivo, envíe por correo electrónico los siguientes datos a [support@gl-inet.com](mailto:support@gl-inet.com) antes de realizar cambios.

- Modelo del router y versión del firmware
- Dirección MAC del dispositivo
- Descripción del problema, incluida la tarea que estaba realizando cuando ocurrió, los mensajes de error y los pasos de solución que ya ha probado

Confirmaremos su lote de fabricación y le indicaremos cómo diagnosticar el problema.

---

El aviso original se conserva a continuación como referencia. Sus pasos de actualización solo se aplican a los lotes afectados. Si desconoce si su dispositivo está afectado, contacte con el soporte como se indica arriba antes de realizar cambios.

**Publicado el 26 de marzo de 2025**

Estimados clientes de GL.iNet:

Este anuncio trata los fallos de arranque y los problemas de recuperación de firmware mediante U-Boot en los dispositivos GL-MT2500/GL-X3000/GL-XE3000. El problema se originó por un defecto de software en el que algunos parámetros se definieron incorrectamente, lo que provocó un funcionamiento anómalo de los routers. Como consecuencia, evaluamos que este problema podría reducir en cierta medida la vida útil de los equipos, por lo que les pedimos disculpas sinceramente.

Para resolver completamente este problema, recomendamos encarecidamente que todos los usuarios de GL-MT2500, GL-X3000 y GL-XE3000 realicen tanto una actualización del bootloader U-Boot como una actualización de firmware. Ambos procedimientos son esenciales y no deben omitirse.

Aunque su dispositivo ya se haya actualizado a la última versión del firmware, la actualización del bootloader U-Boot sigue siendo obligatoria para evitar posibles problemas. Tras completar la actualización del bootloader U-Boot, si la última versión del firmware ya está instalada, puede omitir la reinstalación del firmware.

Intente realizar la actualización con Chrome o Microsoft Edge. NO use Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"} y [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [el firmware más reciente para su router](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"} y [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"} y [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [el firmware más reciente para su router](https://dl.gl-inet.com/router/x3000/stable){target="_blank"} y [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Actualice el gestor de arranque U-Boot.

    Descargue [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"} y [actualice el gestor de arranque U-Boot](upgrade_uboot_version.md).

2. Actualice el firmware.

    Descargue [el firmware más reciente para su router](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"} y [actualice el firmware del router](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Lamentamos sinceramente cualquier inconveniente que esto haya podido causar. A partir de ahora, nos comprometemos a mejorar nuestros productos y firmware con mayor diligencia y cuidado.

Para quienes ya poseen estos routers, ampliaremos el período de garantía un año adicional sin coste alguno. Si encuentra cualquier problema, no dude en ponerse en contacto con nuestros equipos de soporte.

Si el problema persiste a pesar de la actualización, contacte con nuestros equipos de soporte a través de [support@gl-inet.com](mailto:support@gl-inet.com) y le proporcionaremos un reemplazo nuevo sin coste.

Su confianza y apoyo significan muchísimo para nosotros, y le estamos profundamente agradecidos por ello.

<br>
Atentamente,<br>
Equipo de GL.iNet<br>
26 de marzo de 2025
