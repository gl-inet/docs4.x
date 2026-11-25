# Avis concernant un problème sur GL-MT2500/GL-X3000/GL-XE3000 {#problem-notification-for-gl-mt2500gl-x3000gl-xe3000}

**Dernière mise à jour le 11 novembre 2026**

Ce problème connu ne concerne que certains lots. Les appareils commandés à partir du 1er juillet 2025 proviennent très probablement d’un lot plus récent et ne nécessitent aucune mise à jour du chargeur de démarrage U-Boot.

Si vous ne connaissez pas le lot de votre appareil, envoyez les informations suivantes à [support@gl-inet.com](mailto:support@gl-inet.com) avant toute modification.

- Modèle du routeur et version du firmware
- Adresse MAC de l’appareil
- Description du problème, avec ce que vous faisiez au moment où il est survenu, les éventuels messages d’erreur et les étapes de dépannage déjà essayées

Nous confirmerons votre lot de production et vous indiquerons les étapes de dépannage adaptées.

---

L’avis d’origine est conservé ci-dessous à titre de référence. Ses étapes de mise à jour s’appliquent uniquement aux lots concernés. Si vous ne savez pas si votre appareil est concerné, contactez l’assistance comme indiqué ci-dessus avant toute modification.

**Publié le 26 mars 2025**

Chers clients GL.iNet,

Cette annonce concerne les échecs de démarrage et les problèmes de récupération du firmware via U-Boot sur les appareils GL-MT2500/GL-X3000/GL-XE3000. Le problème provenait d'un défaut logiciel dans lequel certains paramètres étaient définis de manière incorrecte, ce qui entraînait un fonctionnement anormal des routeurs. Nous estimons par conséquent que ce problème a pu réduire dans une certaine mesure la durée de vie des routeurs, et nous vous présentons nos sincères excuses.

Pour résoudre complètement ce problème, nous recommandons vivement à tous les utilisateurs des GL-MT2500, GL-X3000 et GL-XE3000 d'effectuer à la fois une mise à niveau du chargeur de démarrage U-Boot et une mise à niveau du firmware. Ces deux procédures sont essentielles et ne doivent pas être omises.

Même si votre appareil a déjà été mis à niveau vers le dernier firmware, la mise à niveau du chargeur de démarrage U-Boot reste obligatoire afin d'éviter tout problème potentiel. Après avoir terminé la mise à niveau du chargeur de démarrage U-Boot, si le dernier firmware est déjà installé, vous pouvez ne pas réinstaller le firmware.

Veuillez effectuer la mise à niveau avec Chrome ou Microsoft Edge. N'utilisez PAS Mozilla/Firefox.

## GL-MT2500 {#gl-mt2500}

1. Mettez à jour le chargeur de démarrage U-Boot.

    Téléchargez [uboot-mt2500-20250224.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-mt2500-20250224-md5-74286e770cfb041b611d80d4adaef189.bin){target="_blank"}, puis [mettez à jour le chargeur de démarrage U-Boot](upgrade_uboot_version.md).

2. Mettez à jour le firmware.

    Téléchargez [le dernier firmware de votre routeur](https://dl.gl-inet.com/router/mt2500/stable){target="_blank"}, puis [mettez à jour le firmware du routeur](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-X3000 {#gl-x3000}

1. Mettez à jour le chargeur de démarrage U-Boot.

    Téléchargez [uboot-x3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-x3000-20250225-md5-c9d7b2fd2451adbc0bb126e2d9729e87.bin){target="_blank"}, puis [mettez à jour le chargeur de démarrage U-Boot](upgrade_uboot_version.md).

2. Mettez à jour le firmware.

    Téléchargez [le dernier firmware de votre routeur](https://dl.gl-inet.com/router/x3000/stable){target="_blank"}, puis [mettez à jour le firmware du routeur](../tutorials/how_to_upgrade_downgrade_router.md).

## GL-XE3000 {#gl-xe3000}

1. Mettez à jour le chargeur de démarrage U-Boot.

    Téléchargez [uboot-xe3000-20250225.bin](https://github.com/gl-inet/mt798x-boot/blob/main/bin/uboot-xe3000-20250225-md5-05fadd9da27314d41dbadc6fbd239b3d.bin){target="_blank"}, puis [mettez à jour le chargeur de démarrage U-Boot](upgrade_uboot_version.md).

2. Mettez à jour le firmware.

    Téléchargez [le dernier firmware de votre routeur](https://dl.gl-inet.com/router/xe3000/stable){target="_blank"}, puis [mettez à jour le firmware du routeur](../tutorials/how_to_upgrade_downgrade_router.md).

<br>
Nous vous présentons nos sincères excuses pour la gêne occasionnée. À l'avenir, nous nous engageons à améliorer nos produits et nos firmwares avec encore plus de rigueur et de soin.

Pour les personnes qui possèdent actuellement ces routeurs, nous prolongerons la période de garantie d'un an sans frais. Si vous rencontrez le moindre problème, n'hésitez pas à contacter nos équipes d'assistance.

Si le problème persiste malgré la mise à niveau, veuillez contacter nos équipes d'assistance à l'adresse [support@gl-inet.com](mailto:support@gl-inet.com) ; nous vous fournirons gratuitement un appareil de remplacement.

Votre confiance et votre soutien comptent énormément pour nous, et nous vous en sommes profondément reconnaissants.

<br>
Cordialement,<br>
L’équipe GL.iNet<br>
26 mars 2025
